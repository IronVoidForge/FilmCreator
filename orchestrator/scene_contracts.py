from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .book_librarian import search_book_index, search_chapter_context
from .character_bible import _is_film_facing_character  # reuse film-facing filtering
from .character_match import find_character_match_candidates
from .chapter_selection import chapter_matches, parse_chapter_selector
from .core.json_io import read_json, write_json
from .environment_bible import _is_film_facing_environment
from .environment_match import find_environment_match_candidates
from .features.authoring.packet_parser import parse_packet_document
from .lmstudio_client import LMStudioClient
from .scaffold import create_project
from .settings import load_runtime_settings
from .world_global import global_character_registry_path, global_environment_registry_path


@dataclass
class SceneContractMetadata:
    artifact_id: str
    artifact_type: str = "scene_contract"
    status: str = "generated"
    source_fingerprint: str | None = None
    created_at_utc: str = ""
    updated_at_utc: str = ""
    upstream_dependencies: list[dict[str, Any]] = field(default_factory=list)
    locked_fields: dict[str, bool] = field(default_factory=dict)
    manual_overrides: dict[str, Any] = field(default_factory=dict)
    revision_history: list[dict[str, Any]] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "artifact_id": self.artifact_id,
            "artifact_type": self.artifact_type,
            "status": self.status,
            "source_fingerprint": self.source_fingerprint,
            "created_at_utc": self.created_at_utc,
            "updated_at_utc": self.updated_at_utc,
            "upstream_dependencies": self.upstream_dependencies,
            "locked_fields": self.locked_fields,
            "manual_overrides": self.manual_overrides,
            "revision_history": self.revision_history,
        }


@dataclass
class SceneReference:
    label: str
    canonical_id: str | None = None
    display_name: str = ""
    status: str = "unresolved"
    entity_kind: str = ""
    resolution_score: int | None = None
    source_path: str = ""
    notes: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "label": self.label,
            "canonical_id": self.canonical_id,
            "display_name": self.display_name,
            "status": self.status,
            "entity_kind": self.entity_kind,
            "resolution_score": self.resolution_score,
            "source_path": self.source_path,
            "notes": self.notes,
        }


@dataclass
class SceneBeat:
    beat_id: str
    summary: str
    purpose: str = ""
    continuity_focus: str = ""
    coverage_hint: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "beat_id": self.beat_id,
            "summary": self.summary,
            "purpose": self.purpose,
            "continuity_focus": self.continuity_focus,
            "coverage_hint": self.coverage_hint,
        }


@dataclass
class SceneContract:
    scene_id: str
    chapter_id: str
    scene_title: str
    purpose: str
    summary: str
    emotional_arc: str
    production_intent: str
    characters_required: list[SceneReference] = field(default_factory=list)
    environments_required: list[SceneReference] = field(default_factory=list)
    continuity_constraints: list[str] = field(default_factory=list)
    visual_coverage_families: list[str] = field(default_factory=list)
    beat_list: list[SceneBeat] = field(default_factory=list)
    unresolved_questions: list[str] = field(default_factory=list)
    evidence_refs: list[dict[str, Any]] = field(default_factory=list)
    evidence_summary: list[str] = field(default_factory=list)
    storyboard_markdown: str = ""
    metadata: SceneContractMetadata | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "scene_id": self.scene_id,
            "chapter_id": self.chapter_id,
            "scene_title": self.scene_title,
            "purpose": self.purpose,
            "summary": self.summary,
            "emotional_arc": self.emotional_arc,
            "production_intent": self.production_intent,
            "characters_required": [item.to_dict() for item in self.characters_required],
            "environments_required": [item.to_dict() for item in self.environments_required],
            "continuity_constraints": self.continuity_constraints,
            "visual_coverage_families": self.visual_coverage_families,
            "beat_list": [item.to_dict() for item in self.beat_list],
            "unresolved_questions": self.unresolved_questions,
            "evidence_refs": self.evidence_refs,
            "evidence_summary": self.evidence_summary,
            "storyboard_markdown": self.storyboard_markdown,
            "metadata": self.metadata.to_dict() if self.metadata else None,
        }


@dataclass(frozen=True)
class SceneContractSynthesisSummary:
    project_slug: str
    total_scene_entries: int
    synthesized_count: int
    reused_count: int
    stale_locked_count: int
    review_queue_count: int
    written_files: list[str]
    warnings: list[str]

    def to_dict(self) -> dict[str, Any]:
        return {
            "project_slug": self.project_slug,
            "total_scene_entries": self.total_scene_entries,
            "synthesized_count": self.synthesized_count,
            "reused_count": self.reused_count,
            "stale_locked_count": self.stale_locked_count,
            "review_queue_count": self.review_queue_count,
            "written_files": self.written_files,
            "warnings": self.warnings,
        }


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _fingerprint(data: Any) -> str:
    raw = json.dumps(data, sort_keys=True, ensure_ascii=False)
    return hashlib.sha1(raw.encode("utf-8")).hexdigest()


def _scene_breakdown_root(project_dir: Path) -> Path:
    return project_dir / "02_story_analysis" / "scene_breakdowns" / "chapters"


def _scene_contract_root(project_dir: Path) -> Path:
    return project_dir / "02_story_analysis" / "contracts" / "scenes"


def _scene_breakdown_path(project_dir: Path, scene_id: str) -> Path:
    chapter_id = scene_id[:5]
    chapter_path = _scene_breakdown_root(project_dir) / chapter_id / f"{scene_id}.md"
    if chapter_path.exists():
        return chapter_path
    legacy_path = project_dir / "02_story_analysis" / "scene_breakdowns" / f"{scene_id}.md"
    if legacy_path.exists():
        return legacy_path
    raise FileNotFoundError(f"Scene breakdown not found: {chapter_path}")


def _chapter_summary_path(project_dir: Path, chapter_id: str) -> Path:
    return project_dir / "02_story_analysis" / "chapter_analysis" / f"{chapter_id}_summary.md"


def _load_scene_markdown(scene_path: Path) -> dict[str, str]:
    fields: dict[str, str] = {}
    lines = scene_path.read_text(encoding="utf-8").splitlines()
    current_key: str | None = None
    current_value: list[str] = []

    def flush() -> None:
        nonlocal current_key, current_value
        if current_key is None:
            return
        value = "\n".join(current_value).strip()
        if value:
            fields[current_key] = value
        current_key = None
        current_value = []

    for raw_line in lines:
        line = raw_line.strip()
        if not line:
            if current_key is not None:
                current_value.append("")
            continue
        if line.startswith("# "):
            fields.setdefault("scene_title", line[2:].strip())
            continue
        match = re.fullmatch(r"\*\*(.+?)\:\*\*\s*(.+)", line)
        if match:
            flush()
            current_key = _normalize_key(match.group(1))
            current_value = [match.group(2).strip()]
            continue
        if current_key is not None:
            current_value.append(raw_line.rstrip())
    flush()
    return fields


def _normalize_key(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", value.strip().lower()).strip("_")


def _split_list_value(value: str) -> list[str]:
    parts: list[str] = []
    buffer: list[str] = []
    depth = 0
    for char in value:
        if char == "(":
            depth += 1
        elif char == ")" and depth > 0:
            depth -= 1
        if char in {",", ";", "\n"} and depth == 0:
            item = "".join(buffer).strip()
            if item:
                parts.append(item)
            buffer = []
            continue
        buffer.append(char)
    tail = "".join(buffer).strip()
    if tail:
        parts.append(tail)
    seen: set[str] = set()
    deduped: list[str] = []
    for part in parts:
        if part not in seen:
            seen.add(part)
            deduped.append(part)
    return deduped


def _normalize_scene_label(value: str) -> str:
    return re.sub(r"[\s\.\,\;\:\!]+$", "", " ".join(value.split()).strip())


def _scene_title_from_fields(scene_id: str, scene_fields: dict[str, str]) -> str:
    raw_title = _first_nonempty(scene_fields.get("scene_title"), fallback="")
    if raw_title and raw_title.strip().upper() not in {scene_id.upper()} and not re.fullmatch(r"SC\d{3}", raw_title.strip().upper()):
        return raw_title.strip()

    for candidate in (
        scene_fields.get("scene_purpose", ""),
        scene_fields.get("scene_summary", ""),
        scene_fields.get("dominant_emotional_shift", ""),
    ):
        if candidate.strip():
            return _compact_snippet(candidate, limit=72)
    return scene_id


def _dedupe_scene_labels(values: list[str]) -> list[str]:
    deduped: list[str] = []
    seen: set[str] = set()
    for value in values:
        normalized = _normalize_scene_label(value)
        key = normalized.lower()
        if not normalized or key in seen:
            continue
        seen.add(key)
        deduped.append(normalized)
    return deduped


def _coerce_string_list(*values: object) -> list[str]:
    items: list[str] = []
    for value in values:
        if value is None:
            continue
        if isinstance(value, list):
            for item in value:
                if isinstance(item, str) and item.strip() and item.strip().lower() not in {"none", "(none)", "n/a"}:
                    items.append(item.strip())
        elif isinstance(value, str):
            stripped = value.strip()
            if not stripped or stripped.lower() in {"none", "(none)", "n/a"}:
                continue
            items.extend(_split_list_value(stripped) if ("," in stripped or ";" in stripped or "\n" in stripped) else [stripped])

    seen: set[str] = set()
    deduped: list[str] = []
    for item in items:
        if item not in seen:
            seen.add(item)
            deduped.append(item)
    return deduped


def _compact_snippet(text: str, *, limit: int = 220) -> str:
    collapsed = " ".join(text.split()).strip()
    if len(collapsed) <= limit:
        return collapsed
    return collapsed[: limit - 3].rstrip() + "..."


def _first_nonempty(*values: object, fallback: str = "") -> str:
    for value in values:
        if isinstance(value, str) and value.strip():
            return value.strip()
    return fallback


def _load_character_bible(project_dir: Path, canonical_id: str) -> dict[str, Any] | None:
    path = project_dir / "02_story_analysis" / "bibles" / "characters" / f"CHAR_{canonical_id}.json"
    if not path.exists():
        return None
    payload = read_json(path)
    if isinstance(payload, dict):
        return payload
    return None


def _load_environment_bible(project_dir: Path, canonical_id: str) -> dict[str, Any] | None:
    path = project_dir / "02_story_analysis" / "bibles" / "environments" / f"ENV_{canonical_id}.json"
    if not path.exists():
        return None
    payload = read_json(path)
    if isinstance(payload, dict):
        return payload
    return None


def _load_refined_registry_path(project_dir: Path, kind: str, project_slug: str) -> Path:
    if kind == "character":
        refined = project_dir / "02_story_analysis" / "world" / "refinement" / "CHARACTER_REGISTRY_GLOBAL_REFINED.json"
        return refined if refined.exists() else global_character_registry_path(project_slug)
    refined = project_dir / "02_story_analysis" / "world" / "refinement" / "ENVIRONMENT_REGISTRY_GLOBAL_REFINED.json"
    return refined if refined.exists() else global_environment_registry_path(project_slug)


def _load_registry_entry(project_dir: Path, project_slug: str, kind: str, canonical_id: str) -> dict[str, Any] | None:
    registry_path = _load_refined_registry_path(project_dir, kind, project_slug)
    if not registry_path.exists():
        return None
    payload = read_json(registry_path)
    if not isinstance(payload, dict):
        return None
    entry = payload.get(canonical_id)
    if isinstance(entry, dict):
        return entry
    return None


def _candidate_threshold(kind: str) -> int:
    return 32 if kind == "character" else 30


def _resolve_character_reference(project_slug: str, label: str, markdown: str, project_dir: Path) -> SceneReference:
    normalized_label = _normalize_scene_label(label)
    candidates = find_character_match_candidates(project_slug=project_slug, asset_id=label, aliases="", markdown=markdown, top_n=1)
    if not candidates:
        return SceneReference(label=normalized_label, display_name=normalized_label, notes="No character candidate found.")
    candidate = candidates[0]
    if candidate.score < _candidate_threshold("character"):
        return SceneReference(
            label=normalized_label,
            canonical_id=None,
            display_name=normalized_label,
            status="review",
            entity_kind="individual",
            resolution_score=candidate.score,
            source_path=candidate.source_paths[0] if candidate.source_paths else "",
            notes=_compact_snippet(" | ".join([candidate.display_name, *candidate.reasons[:2]])),
        )
    bible = _load_character_bible(project_dir, candidate.canonical_id) or {}
    registry_entry = _load_registry_entry(project_dir, project_slug, "character", candidate.canonical_id) or {}
    return SceneReference(
        label=normalized_label,
        canonical_id=candidate.canonical_id,
        display_name=_first_nonempty(str(bible.get("display_name", "")), candidate.display_name, str(registry_entry.get("display_name", "")), fallback=label),
        status=str(registry_entry.get("status", bible.get("status", "canonical"))),
        entity_kind=str(registry_entry.get("entity_kind", bible.get("entity_kind", "individual"))),
        resolution_score=candidate.score,
        source_path=candidate.source_paths[0] if candidate.source_paths else "",
        notes=_compact_snippet(" | ".join(candidate.reasons[:2])),
    )


def _resolve_environment_reference(project_slug: str, label: str, markdown: str, project_dir: Path) -> SceneReference:
    normalized_label = _normalize_scene_label(label)
    candidates = find_environment_match_candidates(project_slug=project_slug, asset_id=label, markdown=markdown, top_n=1)
    if not candidates:
        return SceneReference(label=normalized_label, display_name=normalized_label, notes="No environment candidate found.")
    candidate = candidates[0]
    if candidate.score < _candidate_threshold("environment"):
        return SceneReference(
            label=normalized_label,
            canonical_id=None,
            display_name=normalized_label,
            status="review",
            entity_kind="environment",
            resolution_score=candidate.score,
            source_path=candidate.source_paths[0] if candidate.source_paths else "",
            notes=_compact_snippet(" | ".join([candidate.display_name, *candidate.reasons[:2]])),
        )
    bible = _load_environment_bible(project_dir, candidate.canonical_id) or {}
    registry_entry = _load_registry_entry(project_dir, project_slug, "environment", candidate.canonical_id) or {}
    return SceneReference(
        label=normalized_label,
        canonical_id=candidate.canonical_id,
        display_name=_first_nonempty(str(bible.get("display_name", "")), candidate.display_name, str(registry_entry.get("display_name", "")), fallback=label),
        status=str(registry_entry.get("status", bible.get("status", "canonical"))),
        entity_kind=str(registry_entry.get("entity_kind", bible.get("entity_kind", "environment"))),
        resolution_score=candidate.score,
        source_path=candidate.source_paths[0] if candidate.source_paths else "",
        notes=_compact_snippet(" | ".join(candidate.reasons[:2])),
    )


def _scene_input_terms(scene_fields: dict[str, str]) -> list[str]:
    terms: list[str] = []
    for key in (
        "scene_purpose",
        "scene_summary",
        "dominant_emotional_shift",
        "likely_visual_coverage_families",
        "participating_characters",
        "participating_environments",
    ):
        value = scene_fields.get(key, "")
        if value:
            for part in re.split(r",|;|\n", value):
                normalized = " ".join(part.replace("_", " ").split()).strip()
                if normalized and normalized not in terms:
                    terms.append(normalized)
    return terms[:5]


def _collect_evidence(
    *,
    project_slug: str,
    project_dir: Path,
    scene_id: str,
    chapter_id: str,
    scene_fields: dict[str, str],
    character_refs: list[SceneReference],
    environment_refs: list[SceneReference],
) -> tuple[list[str], list[dict[str, Any]]]:
    evidence_lines: list[str] = []
    evidence_refs: list[dict[str, Any]] = []
    seen: set[str] = set()

    def add_line(line: str, ref: dict[str, Any]) -> None:
        normalized = " ".join(line.split()).strip()
        if not normalized or normalized in seen:
            return
        if len(normalized) > 260:
            normalized = normalized[:257].rstrip() + "..."
        evidence_lines.append(normalized)
        evidence_refs.append(ref)
        seen.add(normalized)

    add_line(
        f"[{scene_id}] Purpose: {scene_fields.get('scene_purpose', '')}",
        {"source": "scene_breakdown", "chapter_id": chapter_id, "scene_id": scene_id},
    )
    add_line(
        f"[{scene_id}] Summary: {scene_fields.get('scene_summary', '')}",
        {"source": "scene_breakdown", "chapter_id": chapter_id, "scene_id": scene_id},
    )
    if scene_fields.get("dominant_emotional_shift"):
        add_line(
            f"[{scene_id}] Emotional arc: {scene_fields.get('dominant_emotional_shift', '')}",
            {"source": "scene_breakdown", "chapter_id": chapter_id, "scene_id": scene_id},
        )
    if scene_fields.get("likely_visual_coverage_families"):
        add_line(
            f"[{scene_id}] Coverage: {scene_fields.get('likely_visual_coverage_families', '')}",
            {"source": "scene_breakdown", "chapter_id": chapter_id, "scene_id": scene_id},
        )
    if scene_fields.get("likely_continuity_sensitivities"):
        add_line(
            f"[{scene_id}] Continuity: {scene_fields.get('likely_continuity_sensitivities', '')}",
            {"source": "scene_breakdown", "chapter_id": chapter_id, "scene_id": scene_id},
        )

    chapter_summary_path = _chapter_summary_path(project_dir, chapter_id)
    if chapter_summary_path.exists():
        chapter_summary = chapter_summary_path.read_text(encoding="utf-8")
        add_line(
            f"[{chapter_id}] Chapter summary: {_compact_snippet(chapter_summary, limit=220)}",
            {"source": "chapter_summary", "chapter_id": chapter_id, "source_path": str(chapter_summary_path)},
        )

    query_terms = _scene_input_terms(scene_fields)
    index_hits = search_book_index(project_slug, " ".join(query_terms[:4]), top_n=3)
    for hit in index_hits:
        add_line(
            f"[{hit.get('chapter_id', '')}] {hit.get('title', '')} ({', '.join(str(reason) for reason in hit.get('reasons', [])[:2]) or 'book index hit'})",
            {"source": "book_index", "chapter_id": str(hit.get("chapter_id", "")), "source_path": str(hit.get("chapter_path", ""))},
        )

    for label_ref in character_refs[:3]:
        if not label_ref.canonical_id:
            continue
        bible = _load_character_bible(project_dir, label_ref.canonical_id) or {}
        summary = _first_nonempty(
            str(bible.get("stable_visual_summary", "")),
            str(bible.get("personality", "")),
            str(bible.get("role", "")),
            fallback=label_ref.display_name or label_ref.label,
        )
        add_line(
            f"Character {label_ref.canonical_id}: {summary}",
            {"source": "character_bible", "chapter_id": chapter_id, "canonical_id": label_ref.canonical_id},
        )

    for env_ref in environment_refs[:3]:
        if not env_ref.canonical_id:
            continue
        bible = _load_environment_bible(project_dir, env_ref.canonical_id) or {}
        summary = _first_nonempty(
            str(bible.get("visual_summary", "")),
            str(bible.get("layout_notes", "")),
            str(bible.get("lighting", "")),
            fallback=env_ref.display_name or env_ref.label,
        )
        add_line(
            f"Environment {env_ref.canonical_id}: {summary}",
            {"source": "environment_bible", "chapter_id": chapter_id, "canonical_id": env_ref.canonical_id},
        )

    search_terms = query_terms[:3]
    if not search_terms:
        search_terms = [label_ref.label for label_ref in character_refs[:2]] + [env_ref.label for env_ref in environment_refs[:2]]
    if search_terms:
        try:
            contexts = search_chapter_context(project_slug, chapter_id, search_terms, window=1, top_n=3)
        except Exception:
            contexts = []
        for context in contexts:
            snippet = _compact_snippet(context.preview or context.text)
            if snippet:
                add_line(
                    f"[{chapter_id} p{context.paragraph_start}-p{context.paragraph_end}] {snippet}",
                    {
                        "source": "paragraph_window",
                        "chapter_id": chapter_id,
                        "source_path": context.chapter_path,
                        "paragraph_start": context.paragraph_start,
                        "paragraph_end": context.paragraph_end,
                    },
                )

    if not evidence_lines:
        add_line(
            scene_fields.get("scene_summary", scene_fields.get("scene_purpose", scene_id)),
            {"source": "scene_breakdown", "chapter_id": chapter_id, "scene_id": scene_id},
        )

    return evidence_lines[:10], evidence_refs[:10]


def _derive_beats(
    *,
    scene_id: str,
    purpose: str,
    summary: str,
    emotional_arc: str,
    continuity_constraints: list[str],
    coverage_families: list[str],
) -> list[SceneBeat]:
    sentences = [sentence.strip() for sentence in re.split(r"(?<=[.!?])\s+", summary) if sentence.strip()]
    beats: list[SceneBeat] = []
    if len(sentences) >= 3:
        for index, sentence in enumerate(sentences[:4], start=1):
            beats.append(
                SceneBeat(
                    beat_id=f"BT{index:03d}",
                    summary=sentence,
                    purpose=purpose if index == 1 else "",
                    continuity_focus=continuity_constraints[min(index - 1, len(continuity_constraints) - 1)] if continuity_constraints else "",
                    coverage_hint=coverage_families[min(index - 1, len(coverage_families) - 1)] if coverage_families else "",
                )
            )
        return beats

    if summary:
        beats.append(SceneBeat(beat_id="BT001", summary=summary, purpose=purpose, continuity_focus=continuity_constraints[0] if continuity_constraints else "", coverage_hint=coverage_families[0] if coverage_families else ""))
    if emotional_arc:
        beats.append(SceneBeat(beat_id="BT002", summary=f"Carry the emotional arc through: {emotional_arc}.", continuity_focus=continuity_constraints[1] if len(continuity_constraints) > 1 else "", coverage_hint=coverage_families[1] if len(coverage_families) > 1 else ""))
    if not beats:
        beats.append(SceneBeat(beat_id="BT001", summary=f"Establish the production intent for {scene_id}.", purpose=purpose))
    if len(beats) == 1:
        beats.append(SceneBeat(beat_id="BT002", summary="Escalate the scene tension and staging clearly.", continuity_focus=continuity_constraints[0] if continuity_constraints else "", coverage_hint=coverage_families[0] if coverage_families else ""))
    if len(beats) == 2:
        beats.append(SceneBeat(beat_id="BT003", summary="Land the scene consequence or transition cleanly.", continuity_focus=continuity_constraints[-1] if continuity_constraints else "", coverage_hint=coverage_families[-1] if coverage_families else ""))
    return beats[:4]


def _synthesize_storyboard_markdown(contract: SceneContract) -> str:
    lines = [
        f"# Scene Contract: {contract.scene_id}",
        "",
        f"- chapter_id: `{contract.chapter_id}`",
        f"- scene_title: `{contract.scene_title}`",
        f"- status: `{contract.metadata.status if contract.metadata else 'generated'}`",
        "",
        "## Production Intent",
        "",
        contract.production_intent or "(none)",
        "",
        "## Purpose",
        "",
        contract.purpose or "(none)",
        "",
        "## Summary",
        "",
        contract.summary or "(none)",
        "",
        "## Emotional Arc",
        "",
        contract.emotional_arc or "(none)",
        "",
        "## Required Cast",
        "",
    ]
    if contract.characters_required:
        for ref in contract.characters_required:
            display = _first_nonempty(ref.display_name, ref.label, fallback=ref.canonical_id or ref.label)
            suffix = []
            if ref.canonical_id:
                suffix.append(ref.canonical_id)
            if ref.status:
                suffix.append(ref.status)
            if ref.entity_kind:
                suffix.append(ref.entity_kind)
            lines.append(f"- {display}" + (f" ({', '.join(suffix)})" if suffix else ""))
    else:
        lines.append("- (none)")

    lines.extend(["", "## Required Environments", ""])
    if contract.environments_required:
        for ref in contract.environments_required:
            display = _first_nonempty(ref.display_name, ref.label, fallback=ref.canonical_id or ref.label)
            suffix = []
            if ref.canonical_id:
                suffix.append(ref.canonical_id)
            if ref.status:
                suffix.append(ref.status)
            if ref.entity_kind:
                suffix.append(ref.entity_kind)
            lines.append(f"- {display}" + (f" ({', '.join(suffix)})" if suffix else ""))
    else:
        lines.append("- (none)")

    lines.extend(["", "## Continuity Constraints", ""])
    if contract.continuity_constraints:
        lines.extend([f"- {item}" for item in contract.continuity_constraints])
    else:
        lines.append("- (none)")

    lines.extend(["", "## Visual Coverage Families", ""])
    if contract.visual_coverage_families:
        lines.extend([f"- {item}" for item in contract.visual_coverage_families])
    else:
        lines.append("- (none)")

    lines.extend(["", "## Beat List", ""])
    for beat in contract.beat_list:
        bits = [beat.summary]
        if beat.purpose:
            bits.append(f"purpose: {beat.purpose}")
        if beat.continuity_focus:
            bits.append(f"continuity: {beat.continuity_focus}")
        if beat.coverage_hint:
            bits.append(f"coverage: {beat.coverage_hint}")
        lines.append(f"- {beat.beat_id}: " + " | ".join(bits))
    if not contract.beat_list:
        lines.append("- (none)")

    lines.extend(["", "## Evidence Summary", ""])
    if contract.evidence_summary:
        lines.extend([f"- {item}" for item in contract.evidence_summary])
    else:
        lines.append("- (none)")

    if contract.unresolved_questions:
        lines.extend(["", "## Unresolved Questions", ""])
        lines.extend([f"- {item}" for item in contract.unresolved_questions])

    return "\n".join(lines).strip() + "\n"


def _parse_scene_contract_packet(text: str, scene_id: str, chapter_id: str, fallback: dict[str, str]) -> dict[str, str]:
    packet = parse_packet_document(text, expected_task="scene_contract_synthesis")
    if not packet.records:
        raise ValueError("Scene contract response did not contain a scene contract record.")
    record = packet.records[0]
    sections = record.sections
    production_scalars, production_lists, production_freeform = _parse_section_markdown(sections.get("production_markdown", ""))
    beat_scalars, beat_lists, beat_freeform = _parse_section_markdown(sections.get("beat_markdown", ""))
    storyboard_text = sections.get("storyboard_markdown", "").strip()
    if not storyboard_text:
        storyboard_text = sections.get("markdown", "").strip()
    return {
        "production_intent": _first_nonempty(
            production_scalars.get("production_intent"),
            production_scalars.get("scene_function"),
            production_freeform[0] if production_freeform else None,
            fallback=fallback.get("production_intent", ""),
        ),
        "scene_title": _first_nonempty(
            production_scalars.get("scene_title"),
            fallback.get("scene_title"),
            fallback=scene_id,
        ),
        "storyboard_markdown": storyboard_text,
        "beat_overrides": beat_lists.get("beat_list", []) or beat_freeform,
        "continuity_overrides": production_lists.get("continuity_constraints", []),
        "coverage_overrides": production_lists.get("visual_coverage_families", []),
    }


def _parse_section_markdown(section_text: str) -> tuple[dict[str, str], dict[str, list[str]], list[str]]:
    scalars: dict[str, str] = {}
    lists: dict[str, list[str]] = {}
    freeform: list[str] = []
    current_list_key: str | None = None

    for raw_line in section_text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("- "):
            item = line[2:].strip()
            if current_list_key:
                if item and item.lower() not in {"none", "(none)", "n/a"}:
                    lists.setdefault(current_list_key, []).append(item)
            elif item:
                freeform.append(item)
            continue
        if ":" in line:
            key, value = line.split(":", 1)
            key = _normalize_key(key)
            value = value.strip()
            if value:
                scalars[key] = value
                current_list_key = None
            else:
                current_list_key = key
                lists.setdefault(key, [])
            continue
        if current_list_key:
            lists.setdefault(current_list_key, []).append(line)
        else:
            freeform.append(line)

    return scalars, lists, freeform


def _load_existing_metadata(existing: dict | None, artifact_id: str, fp: str) -> SceneContractMetadata:
    old_meta = (existing or {}).get("metadata") or {}
    return SceneContractMetadata(
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


def _merge_with_existing(new: dict[str, Any], existing: dict | None, metadata: SceneContractMetadata) -> dict[str, Any]:
    if not existing:
        return new

    merged = dict(new)
    for field_name, locked in metadata.locked_fields.items():
        if locked and field_name in existing:
            merged[field_name] = existing[field_name]
    for field_name, value in metadata.manual_overrides.items():
        merged[field_name] = value
    return merged


def _is_film_facing_scene(contract: SceneContract) -> bool:
    return bool(contract.purpose.strip() and contract.summary.strip() and contract.beat_list)


def _write_scene_contract_files(base_path: Path, contract: SceneContract) -> None:
    write_json(base_path.with_suffix(".json"), contract.to_dict())
    base_path.with_suffix(".md").write_text(_synthesize_storyboard_markdown(contract), encoding="utf-8")


def _scene_list(project_dir: Path) -> list[Path]:
    root = _scene_breakdown_root(project_dir)
    if not root.exists():
        return []
    scene_files = sorted(root.glob("CH*/CH*_SC*.md"))
    if scene_files:
        return scene_files
    legacy_root = project_dir / "02_story_analysis" / "scene_breakdowns"
    return sorted(legacy_root.glob("CH*_SC*.md"))


def _append_review_item(review_queue: list[dict[str, Any]], scene_id: str, issues: list[str], character_refs: list[SceneReference], environment_refs: list[SceneReference]) -> None:
    review_queue.append(
        {
            "scene_id": scene_id,
            "issues": _dedupe_scene_labels(issues),
            "character_refs": [
                ref.to_dict()
                for ref in _dedupe_scene_references(character_refs)
                if ref.status != "canonical" or not ref.canonical_id
            ],
            "environment_refs": [
                ref.to_dict()
                for ref in _dedupe_scene_references(environment_refs)
                if ref.status != "canonical" or not ref.canonical_id
            ],
        }
    )


def _dedupe_scene_references(refs: list[SceneReference]) -> list[SceneReference]:
    deduped: list[SceneReference] = []
    seen: set[str] = set()
    for ref in refs:
        key = ref.canonical_id or _normalize_scene_label(ref.label).lower()
        if key in seen:
            continue
        seen.add(key)
        deduped.append(ref)
    return deduped


def _build_deterministic_payload(
    *,
    scene_id: str,
    chapter_id: str,
    scene_title: str,
    scene_fields: dict[str, str],
    character_refs: list[SceneReference],
    environment_refs: list[SceneReference],
    evidence_summary: list[str],
) -> dict[str, Any]:
    purpose = scene_fields.get("scene_purpose", "")
    summary = scene_fields.get("scene_summary", "")
    emotional_arc = scene_fields.get("dominant_emotional_shift", "")
    continuity_constraints = _split_list_value(scene_fields.get("likely_continuity_sensitivities", ""))
    coverage_families = _split_list_value(scene_fields.get("likely_visual_coverage_families", ""))
    beats = _derive_beats(
        scene_id=scene_id,
        purpose=purpose,
        summary=summary,
        emotional_arc=emotional_arc,
        continuity_constraints=continuity_constraints,
        coverage_families=coverage_families,
    )
    production_intent = _first_nonempty(
        purpose,
        f"Stage {scene_id} with clear narrative intent, stable cast blocking, and continuity-aware coverage.",
        fallback="",
    )
    storyboard_markdown = "\n".join(
        [
            f"# Scene Contract: {scene_id}",
            "",
            f"- chapter_id: `{chapter_id}`",
            f"- scene_title: `{scene_title}`",
            "",
            "## Production Intent",
            "",
            production_intent,
            "",
            "## Storyboard",
            "",
            summary or "(none)",
        ]
    )
    return {
        "scene_title": scene_title,
        "production_intent": production_intent,
        "storyboard_markdown": storyboard_markdown,
        "beat_overrides": [beat.summary for beat in beats],
        "continuity_overrides": continuity_constraints,
        "coverage_overrides": coverage_families,
        "beats": beats,
        "character_refs": character_refs,
        "environment_refs": environment_refs,
        "evidence_summary": evidence_summary,
    }


def run_scene_contract_synthesis(
    project_slug: str,
    *,
    use_llm: bool = True,
    force: bool = False,
    chapters: str | None = None,
    run_tracker: "DownstreamRunTracker | None" = None,
) -> SceneContractSynthesisSummary:
    project_dir = create_project(project_slug)
    selected_chapters = set(parse_chapter_selector(chapters))
    scene_files = [path for path in _scene_list(project_dir) if chapter_matches(path.parent.name or path.stem[:5], selected_chapters)]

    output_root = _scene_contract_root(project_dir)
    review_dir = output_root / "review"
    output_root.mkdir(parents=True, exist_ok=True)
    review_dir.mkdir(parents=True, exist_ok=True)

    synthesized = 0
    reused = 0
    stale_locked = 0
    review_queue: list[dict[str, Any]] = []
    written_files: list[str] = []
    warnings: list[str] = []
    contract_records: list[SceneContract] = []
    review_records: list[SceneContract] = []
    phase_name = "scene_contracts"
    if run_tracker is not None:
        run_tracker.set_phase_total(phase_name, len(scene_files))

    for scene_path in scene_files:
        scene_id_match = re.search(r"(CH\d{3}_SC\d{3})\.md$", scene_path.name, re.IGNORECASE)
        if not scene_id_match:
            continue
        scene_id = scene_id_match.group(1).upper()
        chapter_id = scene_id[:5]
        scene_fields = _load_scene_markdown(scene_path)
        scene_fields.setdefault("scene_purpose", scene_fields.get("scene_purpose", ""))
        scene_fields.setdefault("scene_summary", scene_fields.get("scene_summary", ""))
        scene_title = _scene_title_from_fields(scene_id, scene_fields)
        scene_markdown = scene_path.read_text(encoding="utf-8")
        raw_characters = _dedupe_scene_labels(_split_list_value(scene_fields.get("participating_characters", "")))
        raw_environments = _dedupe_scene_labels(_split_list_value(scene_fields.get("participating_environments", "")))

        character_refs = _dedupe_scene_references(
            [_resolve_character_reference(project_slug, label, scene_markdown, project_dir) for label in raw_characters]
        )
        environment_refs = _dedupe_scene_references(
            [_resolve_environment_reference(project_slug, label, scene_markdown, project_dir) for label in raw_environments]
        )

        evidence_summary, evidence_refs = _collect_evidence(
            project_slug=project_slug,
            project_dir=project_dir,
            scene_id=scene_id,
            chapter_id=chapter_id,
            scene_fields=scene_fields,
            character_refs=character_refs,
            environment_refs=environment_refs,
        )

        fingerprint_payload = {
            "scene_id": scene_id,
            "chapter_id": chapter_id,
            "scene_fields": scene_fields,
            "character_refs": [ref.to_dict() for ref in character_refs],
            "environment_refs": [ref.to_dict() for ref in environment_refs],
            "evidence_summary": evidence_summary,
            "evidence_refs": evidence_refs,
        }
        fp = _fingerprint(fingerprint_payload)
        base_path = output_root / chapter_id / scene_id
        base_path.parent.mkdir(parents=True, exist_ok=True)
        existing = read_json(base_path.with_suffix(".json")) if base_path.with_suffix(".json").exists() else None
        metadata = _load_existing_metadata(existing, artifact_id=f"{scene_id}_SCENE_CONTRACT", fp=fp)
        old_meta = existing.get("metadata") or {} if isinstance(existing, dict) else {}

        if existing and old_meta.get("status") == "locked" and not (run_tracker is not None and run_tracker.is_item_completed(phase_name, scene_id, fp)):
            stale_locked += 1
            existing["metadata"]["status"] = "stale"
            write_json(base_path.with_suffix(".json"), existing)
            warnings.append(f"Locked scene contract became stale and was not regenerated: {scene_id}")
            continue

        if run_tracker is not None and run_tracker.is_item_completed(phase_name, scene_id, fp) and existing:
            reused += 1
            contract = SceneContract(
                scene_id=existing.get("scene_id", scene_id),
                chapter_id=existing.get("chapter_id", chapter_id),
                scene_title=existing.get("scene_title", scene_title),
                purpose=existing.get("purpose", scene_fields.get("scene_purpose", "")),
                summary=existing.get("summary", scene_fields.get("scene_summary", "")),
                emotional_arc=existing.get("emotional_arc", scene_fields.get("dominant_emotional_shift", "")),
                production_intent=existing.get("production_intent", ""),
                characters_required=[SceneReference(**item) for item in existing.get("characters_required", []) if isinstance(item, dict)],
                environments_required=[SceneReference(**item) for item in existing.get("environments_required", []) if isinstance(item, dict)],
                continuity_constraints=existing.get("continuity_constraints", []),
                visual_coverage_families=existing.get("visual_coverage_families", []),
                beat_list=[SceneBeat(**item) for item in existing.get("beat_list", []) if isinstance(item, dict)],
                unresolved_questions=existing.get("unresolved_questions", []),
                evidence_refs=existing.get("evidence_refs", []),
                evidence_summary=existing.get("evidence_summary", []),
                storyboard_markdown=existing.get("storyboard_markdown", ""),
                metadata=metadata,
            )
            contract_records.append(contract)
            if not _is_film_facing_scene(contract):
                review_records.append(contract)
                _append_review_item(review_queue, scene_id, ["Existing contract lacks a complete production shape."], contract.characters_required, contract.environments_required)
            continue

        if existing and not force and run_tracker is None:
            if old_meta.get("source_fingerprint") == fp:
                reused += 1
                contract = SceneContract(
                    scene_id=existing.get("scene_id", scene_id),
                    chapter_id=existing.get("chapter_id", chapter_id),
                    scene_title=existing.get("scene_title", scene_title),
                    purpose=existing.get("purpose", scene_fields.get("scene_purpose", "")),
                    summary=existing.get("summary", scene_fields.get("scene_summary", "")),
                    emotional_arc=existing.get("emotional_arc", scene_fields.get("dominant_emotional_shift", "")),
                    production_intent=existing.get("production_intent", ""),
                    characters_required=[SceneReference(**item) for item in existing.get("characters_required", []) if isinstance(item, dict)],
                    environments_required=[SceneReference(**item) for item in existing.get("environments_required", []) if isinstance(item, dict)],
                    continuity_constraints=existing.get("continuity_constraints", []),
                    visual_coverage_families=existing.get("visual_coverage_families", []),
                    beat_list=[SceneBeat(**item) for item in existing.get("beat_list", []) if isinstance(item, dict)],
                    unresolved_questions=existing.get("unresolved_questions", []),
                    evidence_refs=existing.get("evidence_refs", []),
                    evidence_summary=existing.get("evidence_summary", []),
                    storyboard_markdown=existing.get("storyboard_markdown", ""),
                    metadata=metadata,
                )
                contract_records.append(contract)
                if not _is_film_facing_scene(contract):
                    review_records.append(contract)
                    _append_review_item(review_queue, scene_id, ["Existing contract lacks a complete production shape."], contract.characters_required, contract.environments_required)
                continue

            if old_meta.get("status") == "locked":
                stale_locked += 1
                existing["metadata"]["status"] = "stale"
                write_json(base_path.with_suffix(".json"), existing)
                warnings.append(f"Locked scene contract became stale and was not regenerated: {scene_id}")
                continue

        fallback_payload = _build_deterministic_payload(
            scene_id=scene_id,
            chapter_id=chapter_id,
            scene_title=scene_title,
            scene_fields=scene_fields,
            character_refs=character_refs,
            environment_refs=environment_refs,
            evidence_summary=evidence_summary,
        )

        synthesized_payload: dict[str, Any] | None = None
        if use_llm:
            synthesized_payload = _llm_synthesis(
                project_slug=project_slug,
                scene_id=scene_id,
                chapter_id=chapter_id,
                scene_fields=scene_fields,
                character_refs=character_refs,
                environment_refs=environment_refs,
                evidence_summary=evidence_summary,
            )

        if not synthesized_payload:
            synthesized_payload = fallback_payload
            if use_llm:
                warnings.append(f"LLM synthesis failed or returned invalid packet for {scene_id}; used deterministic fallback.")

        merged = _merge_with_existing(synthesized_payload, existing, metadata)
        beats = _coerce_beats(merged.get("beat_overrides", []), scene_id=scene_id, fallback_beats=fallback_payload["beats"])
        continuity_constraints = _coerce_string_list(merged.get("continuity_overrides", [])) or _split_list_value(scene_fields.get("likely_continuity_sensitivities", ""))
        coverage_families = _coerce_string_list(merged.get("coverage_overrides", [])) or _split_list_value(scene_fields.get("likely_visual_coverage_families", ""))
        production_intent = _first_nonempty(merged.get("production_intent"), fallback_payload["production_intent"], fallback="")
        storyboard_markdown = _first_nonempty(merged.get("storyboard_markdown"), fallback_payload["storyboard_markdown"], fallback="")

        metadata.upstream_dependencies = [
            {
                "dependency_type": "scene_breakdown",
                "dependency_id": scene_id,
                "version": _fingerprint(scene_fields),
            },
            {
                "dependency_type": "character_resolutions",
                "dependency_id": scene_id,
                "version": _fingerprint([ref.to_dict() for ref in character_refs]),
            },
            {
                "dependency_type": "environment_resolutions",
                "dependency_id": scene_id,
                "version": _fingerprint([ref.to_dict() for ref in environment_refs]),
            },
        ]
        metadata.revision_history.append(
            {
                "timestamp_utc": _utc_now(),
                "action": "synthesized",
                "source_fingerprint": fp,
            }
        )

        contract = SceneContract(
            scene_id=scene_id,
            chapter_id=chapter_id,
            scene_title=_first_nonempty(str(merged.get("scene_title", "")), scene_title, fallback=scene_id),
            purpose=scene_fields.get("scene_purpose", ""),
            summary=scene_fields.get("scene_summary", ""),
            emotional_arc=scene_fields.get("dominant_emotional_shift", ""),
            production_intent=production_intent,
            characters_required=character_refs,
            environments_required=environment_refs,
            continuity_constraints=continuity_constraints,
            visual_coverage_families=coverage_families,
            beat_list=beats,
            unresolved_questions=[],
            evidence_refs=evidence_refs,
            evidence_summary=evidence_summary,
            storyboard_markdown=storyboard_markdown,
            metadata=metadata,
        )

        unresolved_questions = []
        for ref in character_refs + environment_refs:
            if ref.status != "canonical" or not ref.canonical_id:
                unresolved_questions.append(f"Resolve {ref.label} -> {ref.display_name or ref.label}")
        if not contract.beat_list:
            unresolved_questions.append("Beat list could not be derived.")
        contract.unresolved_questions = unresolved_questions
        contract.storyboard_markdown = contract.storyboard_markdown or _synthesize_storyboard_markdown(contract)
        contract.beat_list = contract.beat_list or fallback_payload["beats"]

        _write_scene_contract_files(base_path, contract)
        written_files.extend([str(base_path.with_suffix(".json")), str(base_path.with_suffix(".md"))])
        if run_tracker is not None:
            run_tracker.mark_item_completed(
                phase_name,
                scene_id,
                fp,
                outputs=[str(base_path.with_suffix(".json")), str(base_path.with_suffix(".md"))],
            )
        synthesized += 1
        contract_records.append(contract)

        if contract.unresolved_questions:
            review_records.append(contract)
            _append_review_item(review_queue, scene_id, contract.unresolved_questions, character_refs, environment_refs)

    write_json(review_dir / "SCENE_CONTRACT_REVIEW_QUEUE.json", review_queue)
    (review_dir / "SCENE_CONTRACT_REVIEW_QUEUE.md").write_text(_render_review_queue_markdown(review_queue), encoding="utf-8")

    main_records = [record for record in contract_records if _is_film_facing_scene(record)]
    write_json(
        output_root / "SCENE_CONTRACT_INDEX.json",
        [record.to_dict() for record in sorted(main_records, key=lambda item: item.scene_id)],
    )
    (output_root / "SCENE_CONTRACT_INDEX.md").write_text(_render_scene_contract_index(main_records), encoding="utf-8")
    write_json(
        output_root / "SCENE_CONTRACT_REVIEW_INDEX.json",
        [record.to_dict() for record in sorted(review_records, key=lambda item: item.scene_id)],
    )
    (output_root / "SCENE_CONTRACT_REVIEW_INDEX.md").write_text(_render_scene_contract_review_index(review_records), encoding="utf-8")

    written_files.extend(
        [
            str(review_dir / "SCENE_CONTRACT_REVIEW_QUEUE.json"),
            str(review_dir / "SCENE_CONTRACT_REVIEW_QUEUE.md"),
            str(output_root / "SCENE_CONTRACT_INDEX.json"),
            str(output_root / "SCENE_CONTRACT_INDEX.md"),
            str(output_root / "SCENE_CONTRACT_REVIEW_INDEX.json"),
            str(output_root / "SCENE_CONTRACT_REVIEW_INDEX.md"),
        ]
    )

    return SceneContractSynthesisSummary(
        project_slug=project_slug,
        total_scene_entries=len(scene_files),
        synthesized_count=synthesized,
        reused_count=reused,
        stale_locked_count=stale_locked,
        review_queue_count=len(review_queue),
        written_files=written_files,
        warnings=warnings,
    )


def _coerce_beats(raw_beats: Any, *, scene_id: str, fallback_beats: list[SceneBeat]) -> list[SceneBeat]:
    beats: list[SceneBeat] = []
    if isinstance(raw_beats, list):
        for index, item in enumerate(raw_beats, start=1):
            if isinstance(item, SceneBeat):
                beats.append(item)
                continue
            if isinstance(item, dict):
                beat_id = _first_nonempty(item.get("beat_id"), fallback=f"BT{index:03d}")
                beats.append(
                    SceneBeat(
                        beat_id=beat_id,
                        summary=_first_nonempty(item.get("summary"), item.get("markdown"), fallback=""),
                        purpose=_first_nonempty(item.get("purpose"), fallback=""),
                        continuity_focus=_first_nonempty(item.get("continuity_focus"), item.get("continuity"), fallback=""),
                        coverage_hint=_first_nonempty(item.get("coverage_hint"), fallback=""),
                    )
                )
            elif isinstance(item, str):
                summary = re.sub(r"^\s*BT\d{3}\s*:\s*", "", item).strip()
                beats.append(SceneBeat(beat_id=f"BT{index:03d}", summary=summary or item.strip()))
    if beats:
        return beats
    return fallback_beats


def _render_scene_contract_index(records: list[SceneContract]) -> str:
    lines = ["# Scene Contract Index", ""]
    if not records:
        lines.append("- No scene contracts.")
        return "\n".join(lines) + "\n"
    for record in sorted(records, key=lambda item: item.scene_id):
        lines.append(
            f"- `{record.scene_id}` - {record.purpose or record.summary or record.scene_title} "
            f"(beats={len(record.beat_list)}, cast={len(record.characters_required)}, envs={len(record.environments_required)})"
        )
    return "\n".join(lines) + "\n"


def _render_scene_contract_review_index(records: list[SceneContract]) -> str:
    lines = ["# Scene Contract Review Index", ""]
    if not records:
        lines.append("- No review entries.")
        return "\n".join(lines) + "\n"
    for record in sorted(records, key=lambda item: item.scene_id):
        flags: list[str] = []
        if record.unresolved_questions:
            flags.append(f"issues={len(record.unresolved_questions)}")
        unresolved_refs = [ref for ref in record.characters_required + record.environments_required if ref.status != "canonical" or not ref.canonical_id]
        if unresolved_refs:
            flags.append(f"unresolved_refs={len(unresolved_refs)}")
        lines.append(f"- `{record.scene_id}` - {record.scene_title} ({', '.join(flags) if flags else 'review'})")
    return "\n".join(lines) + "\n"


def _render_review_queue_markdown(queue: list[dict[str, Any]]) -> str:
    lines = ["# Scene Contract Review Queue", ""]
    if not queue:
        lines.append("- No review items.")
        return "\n".join(lines) + "\n"
    for item in queue:
        lines.append(f"- `{item.get('scene_id')}`")
        for issue in item.get("issues", []):
            lines.append(f"  - {issue}")
    return "\n".join(lines) + "\n"


def _llm_synthesis(
    *,
    project_slug: str,
    scene_id: str,
    chapter_id: str,
    scene_fields: dict[str, str],
    character_refs: list[SceneReference],
    environment_refs: list[SceneReference],
    evidence_summary: list[str],
) -> dict[str, Any] | None:
    settings = load_runtime_settings()
    client = LMStudioClient(settings)

    system = (
        "You are a film scene contract synthesis system. "
        "Use only the provided evidence. Prefer production clarity and continuity discipline. "
        "Do not invent unsupported details. Return one tagged FilmCreator markdown packet only. "
        "Do not return JSON."
    )

    character_lines = [f"- {ref.label} -> {ref.canonical_id or ref.display_name or 'unresolved'}" for ref in character_refs]
    environment_lines = [f"- {ref.label} -> {ref.canonical_id or ref.display_name or 'unresolved'}" for ref in environment_refs]

    user = f"""
Synthesize a production-ready scene contract from the provided evidence as tagged markdown.

PRIORITIES:
1. stable scene intent
2. continuity discipline
3. grounded cast and environment requirements
4. concise beat list that can drive shot planning

ENTRY:
{json.dumps(scene_fields, indent=2, ensure_ascii=False)}

CHARACTER RESOLUTIONS:
{json.dumps(character_lines, indent=2, ensure_ascii=False)}

ENVIRONMENT RESOLUTIONS:
{json.dumps(environment_lines, indent=2, ensure_ascii=False)}

EVIDENCE:
{json.dumps(evidence_summary, indent=2, ensure_ascii=False)}

Return exactly one FilmCreator packet in this structure:
[[FILMCREATOR_PACKET]]
task: scene_contract_synthesis
version: 1

[[FILMCREATOR_RECORD]]
type: scene_contract
artifact_id: {scene_id}_SCENE_CONTRACT
scene_id: {scene_id}
chapter_id: {chapter_id}
status: generated
entity_kind: scene

[[SECTION production_markdown]]
scene_title: <scene title or scene id>
production_intent: <one grounded paragraph>
scene_function: <one short sentence>
emotional_arc: <short arc note>
visual_coverage_families:
- coverage family 1
- coverage family 2
continuity_constraints:
- constraint 1
- constraint 2
[[/SECTION]]

[[SECTION beat_markdown]]
beat_list:
- BT001: <beat 1>
- BT002: <beat 2>
- BT003: <beat 3>
[[/SECTION]]

[[SECTION storyboard_markdown]]
# Scene Contract: {scene_id}

## Production Intent
...
## Required Cast
...
## Required Environments
...
## Continuity Constraints
...
## Beat List
...
[[/SECTION]]

[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
"""

    try:
        response = client.chat_completion(system_prompt=system, user_prompt=user, temperature=0.1)
        packet = parse_packet_document(response, expected_task="scene_contract_synthesis")
        if not packet.records:
            return None
        record = packet.records[0]
        production_scalars, production_lists, production_freeform = _parse_section_markdown(record.sections.get("production_markdown", ""))
        beat_scalars, beat_lists, beat_freeform = _parse_section_markdown(record.sections.get("beat_markdown", ""))
        storyboard_markdown = record.sections.get("storyboard_markdown", "").strip()
        return {
            "scene_title": _first_nonempty(production_scalars.get("scene_title"), fallback=scene_fields.get("scene_title", scene_id)),
            "production_intent": _first_nonempty(
                production_scalars.get("production_intent"),
                production_freeform[0] if production_freeform else None,
                fallback=scene_fields.get("scene_purpose", ""),
            ),
            "storyboard_markdown": storyboard_markdown,
            "beat_overrides": beat_lists.get("beat_list", []) or beat_freeform,
            "continuity_overrides": production_lists.get("continuity_constraints", []),
            "coverage_overrides": production_lists.get("visual_coverage_families", []),
        }
    except Exception:
        return None
