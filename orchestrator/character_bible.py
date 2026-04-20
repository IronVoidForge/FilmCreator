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
from .character_bible_writer import (
    write_character_bible_index,
    write_character_bible_review_index,
    write_character_bible_markdown,
    write_character_review_queue_markdown,
)
from .core.json_io import read_json, write_json
from .lmstudio_client import LMStudioClient
from .settings import load_runtime_settings
from .scaffold import create_project
from .features.authoring.packet_parser import parse_packet_document
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
        if isinstance(item, dict):
            summary = item.get("summary")
            if summary:
                evidence_summary.append(summary)
                evidence_refs.append(
                    {
                        "chapter_id": item.get("chapter_id"),
                        "source_path": item.get("source_path"),
                    }
                )
        elif isinstance(item, str) and item.strip():
            evidence_summary.append(item.strip())

    for chapter_id, items in desc.get("chapter_specific", {}).items():
        if not isinstance(items, list):
            continue
        for item in items:
            if isinstance(item, dict):
                summary = item.get("summary")
                if summary:
                    evidence_summary.append(summary)
                    evidence_refs.append(
                        {
                            "chapter_id": chapter_id,
                            "source_path": item.get("source_path"),
                        }
                    )
            elif isinstance(item, str) and item.strip():
                evidence_summary.append(item.strip())
                evidence_refs.append({"chapter_id": chapter_id, "source_path": None})

    seen: set[str] = set()
    deduped_summary: list[str] = []
    for item in evidence_summary:
        key = item.strip()
        if not key or key in seen:
            continue
        seen.add(key)
        deduped_summary.append(key)

    return deduped_summary[:25], evidence_refs


def _deterministic_synthesis(entry: dict, evidence_summary: list[str]) -> dict[str, Any]:
    visual_lines = evidence_summary[:3]
    unresolved = list(entry.get("open_questions", []))
    return {
        "display_name": entry.get("display_name") or entry.get("canonical_id"),
        "stable_visual_summary": " ".join(visual_lines) if visual_lines else "",
        "physical_traits": [],
        "costume_signature": "",
        "personality": "",
        "role": entry.get("entity_kind", "character"),
        "voice_notes": "",
        "relationship_notes": [],
        "continuity_constraints": [],
        "unresolved_ambiguities": unresolved,
    }


def _llm_synthesis(entry: dict, evidence_summary: list[str]) -> dict[str, Any] | None:
    settings = load_runtime_settings()
    client = LMStudioClient(settings)

    system = (
        "You are a film character bible synthesis system. "
        "Use only the provided evidence. Prefer cinematic clarity and consistency. "
        "Do not invent unsupported details. Return strict JSON only."
    )

    user = f"""
Synthesize a canonical character bible from the provided evidence.

PRIORITIES:
1. stable visual identity
2. grounded, non-hallucinated summary
3. concise film-usable language
4. preserve unresolved ambiguity when evidence is weak

ENTRY:
{json.dumps(entry, indent=2, ensure_ascii=False)}

EVIDENCE:
{json.dumps(evidence_summary, indent=2, ensure_ascii=False)}

Return JSON with exactly these keys:
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
        text = client.chat_completion(system_prompt=system, user_prompt=user, temperature=0.1)
        payload = _parse_json_object(text)
        required = {
            "display_name",
            "stable_visual_summary",
            "physical_traits",
            "costume_signature",
            "personality",
            "role",
            "voice_notes",
            "relationship_notes",
            "continuity_constraints",
            "unresolved_ambiguities",
        }
        if not required.issubset(payload.keys()):
            return None
        return payload
    except Exception:
        return None


def _parse_json_object(text: str) -> dict[str, Any]:
    stripped = text.strip()
    if stripped.startswith("```"):
        stripped = stripped.replace("```json", "```", 1)
        stripped = stripped.strip("`").strip()

    start = stripped.find("{")
    end = stripped.rfind("}")
    if start == -1 or end == -1 or end < start:
        raise ValueError("LLM response did not contain a JSON object.")

    candidate = stripped[start : end + 1]
    return json.loads(candidate)


def _load_existing_metadata(existing: dict | None, artifact_id: str, fp: str) -> CharacterBibleMetadata:
    old_meta = (existing or {}).get("metadata") or {}
    return CharacterBibleMetadata(
        artifact_id=artifact_id,
        status=old_meta.get("status", "generated"),
        source_fingerprint=fp,
        created_at_utc=old_meta.get("created_at_utc") or _utc_now(),
        updated_at_utc=_utc_now(),
        upstream_dependencies=old_meta.get("upstream_dependencies", []),
        locked_fields=old_meta.get("locked_fields", {}),
        manual_overrides=old_meta.get("manual_overrides", {}),
        revision_history=old_meta.get("revision_history", []),
    )


def _merge_with_existing(new: dict[str, Any], existing: dict | None, metadata: CharacterBibleMetadata) -> dict[str, Any]:
    if not existing:
        return new

    merged = dict(new)
    for field_name, locked in metadata.locked_fields.items():
        if locked and field_name in existing:
            merged[field_name] = existing[field_name]

    for field_name, value in metadata.manual_overrides.items():
        merged[field_name] = value

    return merged


def _load_registry_for_synthesis(project_dir: Path, project_slug: str) -> tuple[dict[str, Any], Path]:
    refined_path = project_dir / "02_story_analysis" / "world" / "refinement" / "CHARACTER_REGISTRY_GLOBAL_REFINED.json"
    canonical_path = global_character_registry_path(project_slug)

    if refined_path.exists():
        return (read_json(refined_path), refined_path)
    if canonical_path.exists():
        return (read_json(canonical_path), canonical_path)
    return ({}, canonical_path)


def _is_film_facing_character(entry: dict[str, Any], bible: CharacterBible | None = None) -> bool:
    if entry.get("status") != "canonical":
        return False
    if entry.get("entity_kind") != "individual":
        return False
    if bible is not None and bible.unresolved_ambiguities:
        return False
    return True


def _write_json_and_markdown(base_path: Path, bible: CharacterBible) -> None:
    write_json(base_path.with_suffix(".json"), bible.to_dict())
    write_character_bible_markdown(base_path.with_suffix(".md"), bible)


def run_character_bible_synthesis(
    project_slug: str,
    *,
    use_llm: bool = True,
    force: bool = False,
) -> CharacterBibleSynthesisSummary:
    project_dir = create_project(project_slug)

    registry, registry_path = _load_registry_for_synthesis(project_dir, project_slug)

    output_dir = project_dir / "02_story_analysis" / "bibles" / "characters"
    review_dir = output_dir / "review"
    output_dir.mkdir(parents=True, exist_ok=True)
    review_dir.mkdir(parents=True, exist_ok=True)

    synthesized = 0
    reused = 0
    stale_locked = 0
    review_queue: list[dict[str, Any]] = []
    written_files: list[str] = []
    warnings: list[str] = []
    bible_records: list[CharacterBible] = []
    review_records: list[CharacterBible] = []

    for char_id, entry in registry.items():
        fp = _fingerprint(entry)
        base_path = output_dir / f"CHAR_{char_id}"
        existing = read_json(base_path.with_suffix(".json")) if base_path.with_suffix(".json").exists() else None
        metadata = _load_existing_metadata(existing, artifact_id=f"CHAR_{char_id}", fp=fp)

        if existing and not force:
            old_meta = existing.get("metadata") or {}
            if old_meta.get("source_fingerprint") == fp:
                reused += 1
                bible = CharacterBible(
                    character_id=existing.get("character_id", char_id),
                    display_name=existing.get("display_name", char_id),
                    aliases=existing.get("aliases", []),
                    status=existing.get("status", "canonical"),
                    entity_kind=existing.get("entity_kind", "individual"),
                    first_seen_chapter=existing.get("first_seen_chapter"),
                    last_seen_chapter=existing.get("last_seen_chapter"),
                    chapter_mentions=existing.get("chapter_mentions", []),
                    stable_visual_summary=existing.get("stable_visual_summary", ""),
                    physical_traits=existing.get("physical_traits", []),
                    costume_signature=existing.get("costume_signature", ""),
                    personality=existing.get("personality", ""),
                    role=existing.get("role", ""),
                    voice_notes=existing.get("voice_notes", ""),
                    relationship_notes=existing.get("relationship_notes", []),
                    continuity_constraints=existing.get("continuity_constraints", []),
                    unresolved_ambiguities=existing.get("unresolved_ambiguities", []),
                    evidence_refs=existing.get("evidence_refs", []),
                    evidence_summary=existing.get("evidence_summary", []),
                    metadata=metadata,
                )
                bible_records.append(bible)
                if not _is_film_facing_character(entry, bible):
                    review_records.append(bible)
                continue

            if old_meta.get("status") == "locked":
                stale_locked += 1
                existing["metadata"]["status"] = "stale"
                write_json(base_path.with_suffix(".json"), existing)
                warnings.append(f"Locked character bible became stale and was not regenerated: {char_id}")
                continue

        evidence_summary, evidence_refs = _collect_evidence(entry)
        synthesized_payload = _llm_synthesis(entry, evidence_summary) if use_llm else None
        if not synthesized_payload:
            synthesized_payload = _deterministic_synthesis(entry, evidence_summary)
            if use_llm:
                warnings.append(f"LLM synthesis failed or returned invalid JSON for {char_id}; used deterministic fallback.")

        merged = _merge_with_existing(synthesized_payload, existing, metadata)

        metadata.upstream_dependencies = [
            {
                "dependency_type": "character_registry_entry",
                "dependency_id": char_id,
                "version": fp,
            }
        ]
        metadata.revision_history.append(
            {
                "timestamp_utc": _utc_now(),
                "action": "synthesized",
                "source_fingerprint": fp,
            }
        )

        bible = CharacterBible(
            character_id=char_id,
            display_name=merged.get("display_name") or entry.get("display_name") or char_id,
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

        _write_json_and_markdown(base_path, bible)
        written_files.extend([str(base_path.with_suffix(".json")), str(base_path.with_suffix(".md"))])
        synthesized += 1
        bible_records.append(bible)

        if not _is_film_facing_character(entry, bible):
            review_records.append(bible)

        if bible.unresolved_ambiguities:
            review_queue.append(
                {
                    "character_id": char_id,
                    "issues": bible.unresolved_ambiguities,
                }
            )

    write_json(review_dir / "CHARACTER_BIBLE_REVIEW_QUEUE.json", review_queue)
    write_character_review_queue_markdown(review_dir / "CHARACTER_BIBLE_REVIEW_QUEUE.md", review_queue)
    main_records = [record for record in bible_records if _is_film_facing_character(entry=registry.get(record.character_id, {}), bible=record)]
    write_character_bible_index(output_dir / "CHARACTER_BIBLE_INDEX.md", main_records)
    write_character_bible_review_index(output_dir / "CHARACTER_BIBLE_REVIEW_INDEX.md", review_records)
    write_json(
        output_dir / "CHARACTER_BIBLE_INDEX.json",
        [record.to_dict() for record in sorted(main_records, key=lambda item: item.character_id)],
    )
    write_json(
        output_dir / "CHARACTER_BIBLE_REVIEW_INDEX.json",
        [record.to_dict() for record in sorted(review_records, key=lambda item: item.character_id)],
    )

    written_files.extend(
        [
            str(review_dir / "CHARACTER_BIBLE_REVIEW_QUEUE.json"),
            str(review_dir / "CHARACTER_BIBLE_REVIEW_QUEUE.md"),
            str(output_dir / "CHARACTER_BIBLE_INDEX.md"),
            str(output_dir / "CHARACTER_BIBLE_INDEX.json"),
            str(output_dir / "CHARACTER_BIBLE_REVIEW_INDEX.md"),
            str(output_dir / "CHARACTER_BIBLE_REVIEW_INDEX.json"),
        ]
    )

    return CharacterBibleSynthesisSummary(
        project_slug=project_slug,
        total_registry_entries=len(registry),
        synthesized_count=synthesized,
        reused_count=reused,
        stale_locked_count=stale_locked,
        review_queue_count=len(review_queue),
        written_files=written_files,
        warnings=warnings,
    )
