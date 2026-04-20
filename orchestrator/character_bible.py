from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .character_bible_models import (
    CharacterBible,
    CharacterBibleMetadata,
    CharacterBibleSynthesisSummary,
)
from .core.json_io import read_json, write_json
from .lmstudio_client import LMStudioClient
from .settings import load_runtime_settings
from .scaffold import create_project
from .world_global import global_character_registry_path


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _fingerprint(data: Any) -> str:
    raw = json.dumps(data, sort_keys=True, ensure_ascii=False)
    return hashlib.sha1(raw.encode("utf-8")).hexdigest()


def _collect_evidence(entry: dict) -> tuple[list[str], list[dict[str, Any]]]:
    evidence_summary: list[str] = []
    evidence_refs: list[dict[str, Any]] = []

    desc = entry.get("description_layers", {})

    for item in desc.get("initial_extracted", []):
        if isinstance(item, dict) and item.get("summary"):
            evidence_summary.append(item["summary"])

    for chapter_id, items in desc.get("chapter_specific", {}).items():
        for item in items:
            summary = item.get("summary")
            if summary:
                evidence_summary.append(summary)
                evidence_refs.append({
                    "chapter_id": chapter_id,
                    "source_path": item.get("source_path"),
                })

    return evidence_summary[:25], evidence_refs


def _deterministic_synthesis(entry: dict, evidence_summary: list[str]) -> dict[str, Any]:
    return {
        "display_name": entry.get("display_name") or entry.get("canonical_id"),
        "stable_visual_summary": " ".join(evidence_summary[:3]),
        "physical_traits": [],
        "costume_signature": "",
        "personality": "",
        "role": entry.get("entity_kind", "character"),
        "voice_notes": "",
        "relationship_notes": [],
        "continuity_constraints": [],
        "unresolved_ambiguities": entry.get("open_questions", []),
    }


def _llm_synthesis(entry: dict, evidence_summary: list[str]) -> dict[str, Any] | None:
    settings = load_runtime_settings()
    client = LMStudioClient(settings)

    system = "You are a film character bible synthesis system. Only use provided evidence. Return strict JSON."

    user = f"""
EVIDENCE:
{json.dumps(evidence_summary, indent=2)}

ENTRY:
{json.dumps(entry, indent=2)}

Return JSON:
{{
  "display_name": str,
  "stable_visual_summary": str,
  "physical_traits": [str],
  "costume_signature": str,
  "personality": str,
  "role": str,
  "voice_notes": str,
  "relationship_notes": [str],
  "continuity_constraints": [str],
  "unresolved_ambiguities": [str]
}}
"""

    try:
        text = client.chat_completion(system_prompt=system, user_prompt=user)
        return json.loads(text)
    except Exception:
        return None


def _merge_with_existing(new: dict, existing: dict | None, metadata: CharacterBibleMetadata) -> dict:
    if not existing:
        return new

    merged = dict(new)

    # preserve locked fields
    for field, locked in metadata.locked_fields.items():
        if locked and field in existing:
            merged[field] = existing[field]

    # apply manual overrides
    for field, value in metadata.manual_overrides.items():
        merged[field] = value

    return merged


def run_character_bible_synthesis(
    project_slug: str,
    *,
    use_llm: bool = True,
    force: bool = False,
) -> CharacterBibleSynthesisSummary:
    project_dir = create_project(project_slug)

    registry_path = global_character_registry_path(project_slug)
    registry = read_json(registry_path) if registry_path.exists() else {}

    output_dir = project_dir / "02_story_analysis" / "bibles" / "characters"
    review_dir = output_dir / "review"
    output_dir.mkdir(parents=True, exist_ok=True)
    review_dir.mkdir(parents=True, exist_ok=True)

    synthesized = 0
    reused = 0
    stale_locked = 0
    review_queue: list[dict[str, Any]] = []
    written_files: list[str] = []

    for char_id, entry in registry.items():
        fp = _fingerprint(entry)

        path = output_dir / f"CHAR_{char_id}.json"
        existing = read_json(path) if path.exists() else None

        metadata = CharacterBibleMetadata(
            artifact_id=f"CHAR_{char_id}",
            source_fingerprint=fp,
            created_at_utc=_utc_now(),
            updated_at_utc=_utc_now(),
        )

        if existing and not force:
            old_meta = existing.get("metadata") or {}
            if old_meta.get("source_fingerprint") == fp:
                reused += 1
                continue

            if old_meta.get("status") == "locked":
                stale_locked += 1
                existing["metadata"]["status"] = "stale"
                write_json(path, existing)
                continue

        evidence_summary, evidence_refs = _collect_evidence(entry)

        data = None
        if use_llm:
            data = _llm_synthesis(entry, evidence_summary)

        if not data:
            data = _deterministic_synthesis(entry, evidence_summary)

        merged = _merge_with_existing(data, existing, metadata if existing else CharacterBibleMetadata(artifact_id=""))

        bible = CharacterBible(
            character_id=char_id,
            display_name=merged.get("display_name"),
            aliases=entry.get("aliases", []),
            status=entry.get("status", "canonical"),
            entity_kind=entry.get("entity_kind", "individual"),
            first_seen_chapter=entry.get("first_seen_chapter"),
            last_seen_chapter=entry.get("last_seen_chapter"),
            chapter_mentions=entry.get("chapter_mentions", []),
            stable_visual_summary=merged.get("stable_visual_summary", ""),
            physical_traits=merged.get("physical_traits", []),
            costume_signature=merged.get("costume_signature", ""),
            personality=merged.get("personality", ""),
            role=merged.get("role", ""),
            voice_notes=merged.get("voice_notes", ""),
            relationship_notes=merged.get("relationship_notes", []),
            continuity_constraints=merged.get("continuity_constraints", []),
            unresolved_ambiguities=merged.get("unresolved_ambiguities", []),
            evidence_refs=evidence_refs,
            evidence_summary=evidence_summary,
            metadata=metadata,
        )

        write_json(path, bible.to_dict())
        written_files.append(str(path))
        synthesized += 1

        if bible.unresolved_ambiguities:
            review_queue.append({
                "character_id": char_id,
                "issues": bible.unresolved_ambiguities,
            })

    write_json(review_dir / "CHARACTER_BIBLE_REVIEW_QUEUE.json", review_queue)

    return CharacterBibleSynthesisSummary(
        project_slug=project_slug,
        total_registry_entries=len(registry),
        synthesized_count=synthesized,
        reused_count=reused,
        stale_locked_count=stale_locked,
        review_queue_count=len(review_queue),
        written_files=written_files,
        warnings=[],
    )
