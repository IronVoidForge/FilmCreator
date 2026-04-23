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

SCENE_CONTRACT_SCHEMA_VERSION = "2026-04-23-scene-contracts-v4"


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
    action_start: str = ""
    action_end: str = ""
    active_subjects: list[str] = field(default_factory=list)
    passive_subjects: list[str] = field(default_factory=list)
    spatial_context: str = ""
    blocking_hint: str = ""
    environment_subzone: str = ""
    continuity_focus: str = ""
    coverage_hint: str = ""
    coverage_priority: str = ""
    handoff_to_next: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "beat_id": self.beat_id,
            "summary": self.summary,
            "purpose": self.purpose,
            "action_start": self.action_start,
            "action_end": self.action_end,
            "active_subjects": self.active_subjects,
            "passive_subjects": self.passive_subjects,
            "spatial_context": self.spatial_context,
            "blocking_hint": self.blocking_hint,
            "environment_subzone": self.environment_subzone,
            "continuity_focus": self.continuity_focus,
            "coverage_hint": self.coverage_hint,
            "coverage_priority": self.coverage_priority,
            "handoff_to_next": self.handoff_to_next,
        }


@dataclass
class PlannedShotSeed:
    planned_shot_id: str
    beat_id: str
    narrative_function: str = ""
    planned_shot_moment_summary: str = ""
    primary_subject_seed: str = ""
    secondary_subjects_seed: list[str] = field(default_factory=list)
    subject_visibility: str = ""
    narration_mode: str = ""
    environment_subzone: str = ""
    planned_shot_required_anchor_1: str = ""
    planned_shot_scale_proof_detail: str = ""
    start_state_seed: str = ""
    end_state_seed: str = ""
    action_seed: str = ""
    blocking_seed: list[str] = field(default_factory=list)
    shot_size: str = ""
    camera_angle: str = ""
    lens_family: str = ""
    camera_motion: str = ""
    zoom_behavior: str = ""
    focus_strategy: str = ""
    lighting_style: str = ""
    primary_subject_angle: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "planned_shot_id": self.planned_shot_id,
            "beat_id": self.beat_id,
            "narrative_function": self.narrative_function,
            "planned_shot_moment_summary": self.planned_shot_moment_summary,
            "primary_subject_seed": self.primary_subject_seed,
            "secondary_subjects_seed": self.secondary_subjects_seed,
            "subject_visibility": self.subject_visibility,
            "narration_mode": self.narration_mode,
            "environment_subzone": self.environment_subzone,
            "planned_shot_required_anchor_1": self.planned_shot_required_anchor_1,
            "planned_shot_scale_proof_detail": self.planned_shot_scale_proof_detail,
            "start_state_seed": self.start_state_seed,
            "end_state_seed": self.end_state_seed,
            "action_seed": self.action_seed,
            "blocking_seed": self.blocking_seed,
            "shot_size": self.shot_size,
            "camera_angle": self.camera_angle,
            "lens_family": self.lens_family,
            "camera_motion": self.camera_motion,
            "zoom_behavior": self.zoom_behavior,
            "focus_strategy": self.focus_strategy,
            "lighting_style": self.lighting_style,
            "primary_subject_angle": self.primary_subject_angle,
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
    scene_short_description: str = ""
    scene_primary_scale_story_point: str = ""
    scene_required_anchor_catalog: list[str] = field(default_factory=list)
    scene_start_state: str = ""
    scene_end_state: str = ""
    dominant_action_line: str = ""
    scene_spatial_layout: list[str] = field(default_factory=list)
    character_spatial_map: list[str] = field(default_factory=list)
    environment_subzones: list[str] = field(default_factory=list)
    entry_vectors: list[str] = field(default_factory=list)
    exit_vectors: list[str] = field(default_factory=list)
    beat_transition_map: list[str] = field(default_factory=list)
    characters_required: list[SceneReference] = field(default_factory=list)
    environments_required: list[SceneReference] = field(default_factory=list)
    continuity_constraints: list[str] = field(default_factory=list)
    visual_coverage_families: list[str] = field(default_factory=list)
    beat_list: list[SceneBeat] = field(default_factory=list)
    planned_shots: list[PlannedShotSeed] = field(default_factory=list)
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
            "scene_short_description": self.scene_short_description,
            "scene_primary_scale_story_point": self.scene_primary_scale_story_point,
            "scene_required_anchor_catalog": self.scene_required_anchor_catalog,
            "scene_start_state": self.scene_start_state,
            "scene_end_state": self.scene_end_state,
            "dominant_action_line": self.dominant_action_line,
            "scene_spatial_layout": self.scene_spatial_layout,
            "character_spatial_map": self.character_spatial_map,
            "environment_subzones": self.environment_subzones,
            "entry_vectors": self.entry_vectors,
            "exit_vectors": self.exit_vectors,
            "beat_transition_map": self.beat_transition_map,
            "characters_required": [item.to_dict() for item in self.characters_required],
            "environments_required": [item.to_dict() for item in self.environments_required],
            "continuity_constraints": self.continuity_constraints,
            "visual_coverage_families": self.visual_coverage_families,
            "beat_list": [item.to_dict() for item in self.beat_list],
            "planned_shots": [item.to_dict() for item in self.planned_shots],
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
    placeholder_tokens = {"", "none", "(none)", "n/a", "null", "[]", "[ ]", "{}", "{ }"}
    items: list[str] = []
    for value in values:
        if value is None:
            continue
        if isinstance(value, list):
            for item in value:
                if not isinstance(item, str):
                    continue
                stripped = item.strip()
                if not stripped or stripped.lower() in placeholder_tokens:
                    continue
                items.append(stripped)
        elif isinstance(value, str):
            stripped = value.strip()
            if not stripped or stripped.lower() in placeholder_tokens:
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


def _chapter_number(chapter_id: str) -> int | None:
    match = re.search(r"CH(\d{3})", str(chapter_id or "").upper())
    if not match:
        return None
    try:
        return int(match.group(1))
    except ValueError:
        return None


def _normalize_resolution_key(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", value.strip().lower()).strip("_")


def _strip_parenthetical_text(value: str) -> str:
    return re.sub(r"\([^)]*\)", " ", value or "")


def _strip_bracket_markup(value: str) -> str:
    return re.sub(r"\[\[|\]\]", "", value or "")


def _strip_leading_articles(value: str) -> str:
    return re.sub(r"^(the|a|an)\s+", "", value.strip(), flags=re.IGNORECASE)


def _strip_character_titles(value: str) -> str:
    return re.sub(
        r"^(captain|capt\.?|general|gen\.?|major|maj\.?|colonel|col\.?|lieutenant|lt\.?|sergeant|sgt\.?|doctor|dr\.?|mr\.?|mrs\.?|ms\.?|miss|the)\s+",
        "",
        value.strip(),
        flags=re.IGNORECASE,
    )


def _resolution_label_variants(label: str, *, kind: str) -> list[str]:
    raw = _normalize_scene_label(_strip_bracket_markup(label))
    if not raw:
        return []

    variants: list[str] = []

    def add_variant(value: str) -> None:
        normalized = _normalize_resolution_key(value)
        if normalized and normalized not in variants:
            variants.append(normalized)

    add_variant(raw)
    add_variant(_strip_parenthetical_text(raw))
    article_stripped = _strip_leading_articles(_strip_parenthetical_text(raw))
    add_variant(article_stripped)

    if kind == "character":
        titled = _strip_character_titles(article_stripped)
        add_variant(titled)
        # Remove descriptive lifecycle/state markers after stripping titles.
        descriptive_trimmed = re.sub(
            r"\b(younger|elderly|older|deceased|dead|corpse|body|wounded|injured|late)\b",
            " ",
            titled,
            flags=re.IGNORECASE,
        )
        add_variant(descriptive_trimmed)
    else:
        slash_parts = [part.strip() for part in re.split(r"/|\bor\b", article_stripped, flags=re.IGNORECASE) if part.strip()]
        for part in slash_parts:
            add_variant(part)

    return variants


def _load_registry_entries(project_dir: Path, project_slug: str, kind: str) -> dict[str, dict[str, Any]]:
    registry_path = _load_refined_registry_path(project_dir, kind, project_slug)
    if not registry_path.exists():
        return {}
    payload = read_json(registry_path)
    if not isinstance(payload, dict):
        return {}
    return {canonical_id: entry for canonical_id, entry in payload.items() if isinstance(canonical_id, str) and isinstance(entry, dict)}


def _entry_chapter_mentions(entry: dict[str, Any]) -> list[str]:
    chapters: list[str] = []
    for value in entry.get("chapter_mentions", []):
        text = str(value or "").strip().upper()
        if re.fullmatch(r"CH\d{3}", text) and text not in chapters:
            chapters.append(text)
    for field_name in ("first_seen_chapter", "last_seen_chapter"):
        text = str(entry.get(field_name, "") or "").strip().upper()
        if re.fullmatch(r"CH\d{3}", text) and text not in chapters:
            chapters.append(text)
    for item in entry.get("source_history", []):
        if not isinstance(item, dict):
            continue
        text = str(item.get("chapter_id", "") or "").strip().upper()
        if re.fullmatch(r"CH\d{3}", text) and text not in chapters:
            chapters.append(text)
    for item in entry.get("alias_history", []):
        if not isinstance(item, dict):
            continue
        text = str(item.get("chapter_id", "") or "").strip().upper()
        if re.fullmatch(r"CH\d{3}", text) and text not in chapters:
            chapters.append(text)
    return chapters


def _chapter_affinity_score(chapter_id: str, chapters: list[str]) -> int:
    current = _chapter_number(chapter_id)
    if current is None or not chapters:
        return 0
    distances = [
        abs(current - chapter_number)
        for chapter in chapters
        if (chapter_number := _chapter_number(chapter)) is not None
    ]
    if not distances:
        return 0
    distance = min(distances)
    if distance == 0:
        return 18
    if distance == 1:
        return 10
    if distance == 2:
        return 4
    return -min(12, distance * 2)


def _entry_resolution_keys(canonical_id: str, entry: dict[str, Any], *, kind: str) -> set[str]:
    raw_values: list[str] = [
        canonical_id,
        str(entry.get("display_name", "")),
        *(str(alias) for alias in entry.get("aliases", []) if isinstance(alias, str)),
    ]
    for item in entry.get("alias_history", []):
        if isinstance(item, dict) and item.get("alias"):
            raw_values.append(str(item.get("alias")))
    keys: set[str] = set()
    for raw in raw_values:
        for variant in _resolution_label_variants(raw, kind=kind):
            keys.add(variant)
    return {key for key in keys if key}


def _best_registry_source_path(entry: dict[str, Any], chapter_id: str) -> str:
    same_chapter_paths: list[str] = []
    other_paths: list[str] = []
    for item in entry.get("source_history", []):
        if not isinstance(item, dict):
            continue
        source_path = str(item.get("source_path", "") or "").strip()
        if not source_path:
            continue
        source_chapter = str(item.get("chapter_id", "") or "").strip().upper()
        if source_chapter == chapter_id.upper():
            same_chapter_paths.append(source_path)
        else:
            other_paths.append(source_path)
    for path in entry.get("sources", []):
        if not isinstance(path, str) or not path.strip():
            continue
        chapter_match = re.search(r"CH\d{3}", path.upper())
        if chapter_match and chapter_match.group(0) == chapter_id.upper():
            same_chapter_paths.append(path.strip())
        else:
            other_paths.append(path.strip())
    ordered = same_chapter_paths + other_paths
    return ordered[0] if ordered else ""


def _scene_reference_from_registry_entry(
    *,
    project_dir: Path,
    project_slug: str,
    kind: str,
    label: str,
    canonical_id: str,
    entry: dict[str, Any],
    resolution_score: int,
    notes: str,
    chapter_id: str,
) -> SceneReference:
    if kind == "character":
        bible = _load_character_bible(project_dir, canonical_id) or {}
        fallback_entity_kind = "individual"
    else:
        bible = _load_environment_bible(project_dir, canonical_id) or {}
        fallback_entity_kind = "environment"
    registry_entry = _load_registry_entry(project_dir, project_slug, kind, canonical_id) or entry
    return SceneReference(
        label=_normalize_scene_label(label),
        canonical_id=canonical_id,
        display_name=_first_nonempty(
            str(bible.get("display_name", "")),
            str(registry_entry.get("display_name", "")),
            fallback=label,
        ),
        status=str(registry_entry.get("status", bible.get("status", "canonical"))),
        entity_kind=str(registry_entry.get("entity_kind", bible.get("entity_kind", fallback_entity_kind))),
        resolution_score=resolution_score,
        source_path=_best_registry_source_path(registry_entry, chapter_id),
        notes=_compact_snippet(notes, limit=180),
    )


def _resolve_direct_registry_match(
    *,
    project_dir: Path,
    project_slug: str,
    kind: str,
    label: str,
    chapter_id: str,
) -> SceneReference | None:
    label_variants = _resolution_label_variants(label, kind=kind)
    if not label_variants:
        return None

    best: tuple[int, str, dict[str, Any], str] | None = None
    entries = _load_registry_entries(project_dir, project_slug, kind)
    for canonical_id, entry in entries.items():
        entry_keys = _entry_resolution_keys(canonical_id, entry, kind=kind)
        if not entry_keys:
            continue
        matched_variant = next((variant for variant in label_variants if variant in entry_keys), "")
        if not matched_variant:
            continue
        score = 120 + _chapter_affinity_score(chapter_id, _entry_chapter_mentions(entry))
        notes = f"Direct registry match for '{matched_variant}'."
        if best is None or score > best[0]:
            best = (score, canonical_id, entry, notes)

    if best is None:
        return None

    score, canonical_id, entry, notes = best
    return _scene_reference_from_registry_entry(
        project_dir=project_dir,
        project_slug=project_slug,
        kind=kind,
        label=label,
        canonical_id=canonical_id,
        entry=entry,
        resolution_score=score,
        notes=notes,
        chapter_id=chapter_id,
    )


def _best_fuzzy_candidate(
    *,
    project_slug: str,
    project_dir: Path,
    kind: str,
    label: str,
    markdown: str,
    chapter_id: str,
) -> SceneReference | None:
    normalized_label = _normalize_scene_label(label)
    if kind == "character":
        candidates = find_character_match_candidates(project_slug=project_slug, asset_id=label, aliases="", markdown=markdown, top_n=5)
    else:
        candidates = find_environment_match_candidates(project_slug=project_slug, asset_id=label, markdown=markdown, top_n=5)

    if not candidates:
        return SceneReference(label=normalized_label, display_name=normalized_label, notes=f"No {kind} candidate found.")

    threshold = _candidate_threshold(kind)
    best_candidate: Any | None = None
    best_adjusted_score: int | None = None
    for candidate in candidates:
        has_strong_reason = any(
            "asset id exactly matches" in reason
            or "query matches alias" in reason
            or "token overlap" in reason
            for reason in candidate.reasons
        )
        adjusted = int(candidate.score) + _chapter_affinity_score(chapter_id, list(candidate.source_chapters))
        if not has_strong_reason:
            adjusted -= 18
        if best_candidate is None or adjusted > (best_adjusted_score or -9999):
            best_candidate = candidate
            best_adjusted_score = adjusted

    if best_candidate is None or best_adjusted_score is None:
        return SceneReference(label=normalized_label, display_name=normalized_label, notes=f"No {kind} candidate found.")

    has_strong_reason = any(
        "asset id exactly matches" in reason
        or "query matches alias" in reason
        or "token overlap" in reason
        for reason in best_candidate.reasons
    )
    if int(best_candidate.score) < threshold or not has_strong_reason:
        return SceneReference(
            label=normalized_label,
            canonical_id=None,
            display_name=normalized_label,
            status="review",
            entity_kind="individual" if kind == "character" else "environment",
            resolution_score=int(best_candidate.score),
            source_path="",
            notes=f"Low-confidence {kind} match requires review.",
        )

    entry = _load_registry_entry(project_dir, project_slug, kind, best_candidate.canonical_id) or {}
    return _scene_reference_from_registry_entry(
        project_dir=project_dir,
        project_slug=project_slug,
        kind=kind,
        label=label,
        canonical_id=best_candidate.canonical_id,
        entry=entry,
        resolution_score=int(best_candidate.score),
        notes=" | ".join(best_candidate.reasons[:2]),
        chapter_id=chapter_id,
    )


def _resolve_character_reference(project_slug: str, label: str, markdown: str, project_dir: Path, chapter_id: str) -> SceneReference:
    normalized_label = _normalize_scene_label(label)
    direct_match = _resolve_direct_registry_match(
        project_dir=project_dir,
        project_slug=project_slug,
        kind="character",
        label=label,
        chapter_id=chapter_id,
    )
    if direct_match is not None:
        return direct_match
    resolved = _best_fuzzy_candidate(
        project_slug=project_slug,
        project_dir=project_dir,
        kind="character",
        label=label,
        markdown=markdown,
        chapter_id=chapter_id,
    )
    return resolved if resolved is not None else SceneReference(label=normalized_label, display_name=normalized_label, notes="No character candidate found.")


def _resolve_environment_reference(project_slug: str, label: str, markdown: str, project_dir: Path, chapter_id: str) -> SceneReference:
    normalized_label = _normalize_scene_label(label)
    direct_match = _resolve_direct_registry_match(
        project_dir=project_dir,
        project_slug=project_slug,
        kind="environment",
        label=label,
        chapter_id=chapter_id,
    )
    if direct_match is not None:
        return direct_match
    resolved = _best_fuzzy_candidate(
        project_slug=project_slug,
        project_dir=project_dir,
        kind="environment",
        label=label,
        markdown=markdown,
        chapter_id=chapter_id,
    )
    return resolved if resolved is not None else SceneReference(label=normalized_label, display_name=normalized_label, notes="No environment candidate found.")


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
                    action_start=sentence if index == 1 else f"Continue from prior beat: {sentences[index - 2]}",
                    action_end=sentences[index] if index < len(sentences) else sentence,
                    spatial_context=continuity_constraints[min(index - 1, len(continuity_constraints) - 1)] if continuity_constraints else "",
                    blocking_hint=coverage_families[min(index - 1, len(coverage_families) - 1)] if coverage_families else "",
                    environment_subzone="primary scene playing area",
                    continuity_focus=continuity_constraints[min(index - 1, len(continuity_constraints) - 1)] if continuity_constraints else "",
                    coverage_hint=coverage_families[min(index - 1, len(coverage_families) - 1)] if coverage_families else "",
                    coverage_priority="primary story beat",
                    handoff_to_next=sentences[index] if index < len(sentences) else "",
                )
            )
        return beats

    if summary:
        beats.append(SceneBeat(beat_id="BT001", summary=summary, purpose=purpose, action_start=summary, action_end=summary, spatial_context=continuity_constraints[0] if continuity_constraints else "", blocking_hint=coverage_families[0] if coverage_families else "", environment_subzone="primary scene playing area", continuity_focus=continuity_constraints[0] if continuity_constraints else "", coverage_hint=coverage_families[0] if coverage_families else "", coverage_priority="primary story beat"))
    if emotional_arc:
        beats.append(SceneBeat(beat_id="BT002", summary=f"Carry the emotional arc through: {emotional_arc}.", action_start="Continue the established scene action.", action_end=f"Land the emotional shift: {emotional_arc}.", spatial_context=continuity_constraints[1] if len(continuity_constraints) > 1 else "", blocking_hint=coverage_families[1] if len(coverage_families) > 1 else "", environment_subzone="primary scene playing area", continuity_focus=continuity_constraints[1] if len(continuity_constraints) > 1 else "", coverage_hint=coverage_families[1] if len(coverage_families) > 1 else "", coverage_priority="emotional transition"))
    if not beats:
        beats.append(SceneBeat(beat_id="BT001", summary=f"Establish the production intent for {scene_id}.", purpose=purpose, action_start="Scene opens in the established location.", action_end="Primary scene business becomes readable.", environment_subzone="primary scene playing area", coverage_priority="establishing beat"))
    if len(beats) == 1:
        beats.append(SceneBeat(beat_id="BT002", summary="Escalate the scene tension and staging clearly.", action_start="Continue from the opening scene condition.", action_end="Escalation becomes visually explicit.", spatial_context=continuity_constraints[0] if continuity_constraints else "", blocking_hint=coverage_families[0] if coverage_families else "", environment_subzone="primary scene playing area", continuity_focus=continuity_constraints[0] if continuity_constraints else "", coverage_hint=coverage_families[0] if coverage_families else "", coverage_priority="escalation beat"))
    if len(beats) == 2:
        beats.append(SceneBeat(beat_id="BT003", summary="Land the scene consequence or transition cleanly.", action_start="Continue the established scene action toward consequence.", action_end="Arrive at the scene's transition point.", spatial_context=continuity_constraints[-1] if continuity_constraints else "", blocking_hint=coverage_families[-1] if coverage_families else "", environment_subzone="primary scene playing area", continuity_focus=continuity_constraints[-1] if continuity_constraints else "", coverage_hint=coverage_families[-1] if coverage_families else "", coverage_priority="transition beat"))
    return beats[:4]


def _derive_scene_staging(
    *,
    scene_id: str,
    summary: str,
    purpose: str,
    emotional_arc: str,
    continuity_constraints: list[str],
    beats: list[SceneBeat],
) -> dict[str, Any]:
    scene_start_state = _first_nonempty(summary, purpose, fallback=f"{scene_id} opens with the primary dramatic situation already in motion.")
    scene_end_state = _first_nonempty(beats[-1].action_end if beats else "", emotional_arc, fallback="The scene resolves into the next dramatic transition point.")
    dominant_action_line = _first_nonempty(summary, purpose, fallback="Scene action advances the chapter's immediate dramatic objective.")
    scene_spatial_layout = continuity_constraints[:3] or ["Use the established environment scale and architecture to anchor subject placement."]
    character_spatial_map = ["Primary subject placement should remain readable against the main environment anchor."]
    environment_subzones = ["primary scene playing area"]
    entry_vectors = ["Subjects inherit entry logic from the prior scene or chapter transition."]
    exit_vectors = ["Subjects exit or hand off toward the next story beat."]
    beat_transition_map = [f"{beat.beat_id}: {beat.action_start or beat.summary} -> {beat.action_end or beat.summary}" for beat in beats]
    return {
        "scene_start_state": scene_start_state,
        "scene_end_state": scene_end_state,
        "dominant_action_line": dominant_action_line,
        "scene_spatial_layout": scene_spatial_layout,
        "character_spatial_map": character_spatial_map,
        "environment_subzones": environment_subzones,
        "entry_vectors": entry_vectors,
        "exit_vectors": exit_vectors,
        "beat_transition_map": beat_transition_map,
    }


def _default_primary_subject_seed(summary: str) -> str:
    lowered = summary.lower()
    if "narrator" in lowered:
        return "The Narrator"
    if "john carter" in lowered:
        return "John Carter"
    if "chieftain" in lowered:
        return "The Chieftain"
    if "tars tarkas" in lowered:
        return "Tars Tarkas"
    if "martian warrior" in lowered:
        return "Martian Warrior"
    return "primary scene subject"


def _default_subject_visibility(subject_seed: str) -> str:
    if subject_seed.strip().lower() == "the narrator":
        return "off_screen_voice"
    return "on_screen"


def _default_narration_mode(subject_seed: str) -> str:
    if subject_seed.strip().lower() == "the narrator":
        return "voiceover_off_screen"
    return "none"


def _default_shot_seed_enums(coverage_priority: str, beat_summary: str) -> dict[str, str]:
    priority = coverage_priority.strip().lower()
    summary = beat_summary.strip().lower()
    if "transition" in priority:
        return {
            "shot_size": "medium",
            "camera_angle": "eye_level",
            "lens_family": "normal",
            "camera_motion": "locked_off",
            "zoom_behavior": "none",
            "focus_strategy": "deep_focus",
            "lighting_style": "hard_directional",
            "primary_subject_angle": "front_three_quarter_left",
        }
    if "emotion" in priority or "reaction" in summary:
        return {
            "shot_size": "close_up",
            "camera_angle": "eye_level",
            "lens_family": "portrait",
            "camera_motion": "push_in",
            "zoom_behavior": "subtle_in",
            "focus_strategy": "shallow_subject",
            "lighting_style": "hard_directional",
            "primary_subject_angle": "front_three_quarter_left",
        }
    if "detail" in summary or "insert" in summary:
        return {
            "shot_size": "insert_detail",
            "camera_angle": "eye_level",
            "lens_family": "portrait",
            "camera_motion": "locked_off",
            "zoom_behavior": "none",
            "focus_strategy": "shallow_subject",
            "lighting_style": "hard_directional",
            "primary_subject_angle": "",
        }
    return {
        "shot_size": "medium",
        "camera_angle": "eye_level",
        "lens_family": "normal",
        "camera_motion": "locked_off",
        "zoom_behavior": "none",
        "focus_strategy": "deep_focus",
        "lighting_style": "hard_directional",
        "primary_subject_angle": "front_three_quarter_left",
    }


def _normalize_fragment(text: str, *, limit: int = 120) -> str:
    collapsed = " ".join(str(text or "").split()).strip(" ,;")
    if not collapsed:
        return ""
    if len(collapsed) <= limit:
        return collapsed
    return collapsed[: limit - 3].rstrip(" ,;") + "..."


def _scene_short_description(summary: str, purpose: str, emotional_arc: str) -> str:
    return _normalize_fragment(
        _first_nonempty(
            summary,
            purpose,
            emotional_arc,
            fallback="story scene with readable character hierarchy and environment context",
        ),
        limit=150,
    )


def _scene_scale_story_point(summary: str, purpose: str, evidence_summary: list[str]) -> str:
    text = " ".join([summary, purpose, *evidence_summary]).lower()
    if any(term in text for term in ["giant", "towering", "enormous", "huge", "dais", "small beside", "scale mismatch", "human-sized"]):
        if "chair" in text or "desk" in text or "furniture" in text:
            return "human-scale furnishings emphasize the mismatch beside larger bodies"
        if "dais" in text or "rostrum" in text:
            return "raised ceremonial architecture reinforces scale and status hierarchy"
        return "subject scale contrast should remain visually obvious in the frame"
    return ""


def _scene_required_anchor_catalog(
    scene_spatial_layout: list[str],
    environment_subzones: list[str],
    evidence_summary: list[str],
) -> list[str]:
    anchors = _coerce_string_list(environment_subzones, scene_spatial_layout)
    text = " ".join(evidence_summary).lower()
    heuristic_terms = [
        ("dais", "raised dais"),
        ("rostrum", "central rostrum"),
        ("gallery", "gallery wall"),
        ("throne", "authority seat"),
        ("chair", "human-scale carved chair"),
        ("desk", "human-scale carved desk"),
        ("mural", "painted mural wall"),
        ("bar", "window bar"),
        ("threshold", "scene threshold"),
        ("door", "entry doorway"),
    ]
    for term, label in heuristic_terms:
        if term in text:
            anchors.append(label)
    return _coerce_string_list(anchors)[:5]


def _planned_shot_anchor(beat: SceneBeat, scene_anchors: list[str]) -> str:
    text = " ".join(
        item
        for item in [beat.environment_subzone, beat.spatial_context, beat.blocking_hint, beat.summary]
        if item
    ).lower()
    for anchor in scene_anchors:
        if anchor and any(token in text for token in anchor.lower().split()):
            return anchor
    if beat.environment_subzone:
        return _normalize_fragment(beat.environment_subzone, limit=80)
    if scene_anchors:
        return scene_anchors[0]
    return ""


def _planned_shot_scale_proof_detail(beat: SceneBeat, scene_scale_story_point: str, scene_anchors: list[str]) -> str:
    text = " ".join(item for item in [beat.summary, beat.spatial_context, beat.blocking_hint, scene_scale_story_point] if item).lower()
    if "chair" in text or "desk" in text or "furniture" in text:
        return "keep one oversized body beside human-scale furniture"
    if "dais" in text or "rostrum" in text:
        return "preserve the lower-floor versus raised-platform hierarchy"
    if scene_scale_story_point:
        return _normalize_fragment(scene_scale_story_point, limit=100)
    if scene_anchors:
        return f"keep {scene_anchors[0]} readable as the scale anchor"
    return ""


def _derive_planned_shots(beats: list[SceneBeat]) -> list[PlannedShotSeed]:
    planned: list[PlannedShotSeed] = []
    scene_anchors = _scene_required_anchor_catalog(
        [beat.spatial_context for beat in beats if beat.spatial_context],
        [beat.environment_subzone for beat in beats if beat.environment_subzone],
        [beat.summary for beat in beats],
    )
    scene_scale_story_point = _scene_scale_story_point(
        " ".join(beat.summary for beat in beats),
        " ".join(beat.purpose for beat in beats),
        [beat.spatial_context for beat in beats if beat.spatial_context],
    )
    for index, beat in enumerate(beats, start=1):
        primary_subject_seed = _default_primary_subject_seed(beat.summary)
        enums = _default_shot_seed_enums(beat.coverage_priority, beat.summary)
        planned.append(
            PlannedShotSeed(
                planned_shot_id=f"SH{index:03d}",
                beat_id=beat.beat_id,
                narrative_function=beat.coverage_priority or "story beat",
                planned_shot_moment_summary=_normalize_fragment(
                    _first_nonempty(beat.summary, beat.action_start, beat.action_end, fallback="visible story beat"),
                    limit=110,
                ),
                primary_subject_seed=primary_subject_seed,
                secondary_subjects_seed=list(beat.passive_subjects),
                subject_visibility=_default_subject_visibility(primary_subject_seed),
                narration_mode=_default_narration_mode(primary_subject_seed),
                environment_subzone=beat.environment_subzone or "primary scene playing area",
                planned_shot_required_anchor_1=_planned_shot_anchor(beat, scene_anchors),
                planned_shot_scale_proof_detail=_planned_shot_scale_proof_detail(beat, scene_scale_story_point, scene_anchors),
                start_state_seed=beat.action_start or beat.summary,
                end_state_seed=beat.action_end or beat.summary,
                action_seed=beat.summary,
                blocking_seed=_coerce_string_list(beat.blocking_hint, beat.spatial_context),
                shot_size=enums["shot_size"],
                camera_angle=enums["camera_angle"],
                lens_family=enums["lens_family"],
                camera_motion=enums["camera_motion"],
                zoom_behavior=enums["zoom_behavior"],
                focus_strategy=enums["focus_strategy"],
                lighting_style=enums["lighting_style"],
                primary_subject_angle=enums["primary_subject_angle"],
            )
        )
    return planned


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
        "## Scene Short Description",
        "",
        contract.scene_short_description or "(none)",
        "",
        "## Scene Primary Scale Story Point",
        "",
        contract.scene_primary_scale_story_point or "(none)",
        "",
        "## Scene Required Anchor Catalog",
        "",
    ]
    if contract.scene_required_anchor_catalog:
        lines.extend([f"- {item}" for item in contract.scene_required_anchor_catalog])
    else:
        lines.append("- (none)")

    lines.extend([
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
        "## Scene Start State",
        "",
        contract.scene_start_state or "(none)",
        "",
        "## Scene End State",
        "",
        contract.scene_end_state or "(none)",
        "",
        "## Dominant Action Line",
        "",
        contract.dominant_action_line or "(none)",
        "",
        "## Scene Spatial Layout",
        "",
    ])
    if contract.scene_spatial_layout:
        lines.extend([f"- {item}" for item in contract.scene_spatial_layout])
    else:
        lines.append("- (none)")

    lines.extend(["", "## Character Spatial Map", ""])
    if contract.character_spatial_map:
        lines.extend([f"- {item}" for item in contract.character_spatial_map])
    else:
        lines.append("- (none)")

    lines.extend(["", "## Environment Subzones", ""])
    if contract.environment_subzones:
        lines.extend([f"- {item}" for item in contract.environment_subzones])
    else:
        lines.append("- (none)")

    lines.extend([
        "",
        "## Required Cast",
        "",
    ])
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
        if beat.action_start:
            bits.append(f"start: {beat.action_start}")
        if beat.action_end:
            bits.append(f"end: {beat.action_end}")
        if beat.spatial_context:
            bits.append(f"space: {beat.spatial_context}")
        if beat.blocking_hint:
            bits.append(f"blocking: {beat.blocking_hint}")
        if beat.environment_subzone:
            bits.append(f"subzone: {beat.environment_subzone}")
        if beat.continuity_focus:
            bits.append(f"continuity: {beat.continuity_focus}")
        if beat.coverage_hint:
            bits.append(f"coverage: {beat.coverage_hint}")
        if beat.coverage_priority:
            bits.append(f"priority: {beat.coverage_priority}")
        if beat.handoff_to_next:
            bits.append(f"handoff: {beat.handoff_to_next}")
        lines.append(f"- {beat.beat_id}: " + " | ".join(bits))
    if not contract.beat_list:
        lines.append("- (none)")

    lines.extend(["", "## Planned Shots", ""])
    for planned_shot in contract.planned_shots:
        bits = [
            f"beat={planned_shot.beat_id}",
            f"function={planned_shot.narrative_function or 'story beat'}",
            f"primary={planned_shot.primary_subject_seed or '(none)'}",
            f"visibility={planned_shot.subject_visibility or '(none)'}",
            f"narration={planned_shot.narration_mode or '(none)'}",
            f"subzone={planned_shot.environment_subzone or '(none)'}",
            f"moment={planned_shot.planned_shot_moment_summary or '(none)'}",
            f"anchor1={planned_shot.planned_shot_required_anchor_1 or '(none)'}",
            f"scale_proof={planned_shot.planned_shot_scale_proof_detail or '(none)'}",
            f"start={planned_shot.start_state_seed or '(none)'}",
            f"end={planned_shot.end_state_seed or '(none)'}",
            f"action={planned_shot.action_seed or '(none)'}",
            f"shot_size={planned_shot.shot_size or '(none)'}",
            f"camera_angle={planned_shot.camera_angle or '(none)'}",
            f"lens={planned_shot.lens_family or '(none)'}",
            f"motion={planned_shot.camera_motion or '(none)'}",
            f"zoom={planned_shot.zoom_behavior or '(none)'}",
            f"focus={planned_shot.focus_strategy or '(none)'}",
            f"lighting={planned_shot.lighting_style or '(none)'}",
            f"subject_angle={planned_shot.primary_subject_angle or '(none)'}",
        ]
        lines.append(f"- {planned_shot.planned_shot_id}: " + " | ".join(bits))
    if not contract.planned_shots:
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


def _parse_scene_contract_packet(text: str, scene_id: str, chapter_id: str, fallback: dict[str, Any]) -> dict[str, Any]:
    packet = parse_packet_document(text, expected_task="scene_contract_synthesis")
    if not packet.records:
        raise ValueError("Scene contract response did not contain a scene contract record.")
    record = packet.records[0]
    sections = record.sections
    production_scalars, production_lists, production_freeform = _parse_section_markdown(sections.get("production_markdown", ""))
    _, beat_lists, beat_freeform = _parse_section_markdown(sections.get("beat_markdown", ""))
    staging_scalars, staging_lists, _ = _parse_section_markdown(sections.get("scene_staging_markdown", ""))
    _, planned_shot_lists, planned_shot_freeform = _parse_section_markdown(sections.get("planned_shots_markdown", ""))
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
        "scene_short_description": _first_nonempty(staging_scalars.get("scene_short_description"), fallback.get("scene_short_description"), fallback=""),
        "scene_primary_scale_story_point": _first_nonempty(
            staging_scalars.get("scene_primary_scale_story_point"),
            fallback.get("scene_primary_scale_story_point"),
            fallback="",
        ),
        "scene_required_anchor_catalog": staging_lists.get("scene_required_anchor_catalog", []) or list(fallback.get("scene_required_anchor_catalog", [])),
        "scene_start_state": _first_nonempty(staging_scalars.get("scene_start_state"), fallback.get("scene_start_state"), fallback=""),
        "scene_end_state": _first_nonempty(staging_scalars.get("scene_end_state"), fallback.get("scene_end_state"), fallback=""),
        "dominant_action_line": _first_nonempty(staging_scalars.get("dominant_action_line"), fallback.get("dominant_action_line"), fallback=""),
        "scene_spatial_layout": staging_lists.get("scene_spatial_layout", []) or list(fallback.get("scene_spatial_layout", [])),
        "character_spatial_map": staging_lists.get("character_spatial_map", []) or list(fallback.get("character_spatial_map", [])),
        "environment_subzones": staging_lists.get("environment_subzones", []) or list(fallback.get("environment_subzones", [])),
        "entry_vectors": staging_lists.get("entry_vectors", []) or list(fallback.get("entry_vectors", [])),
        "exit_vectors": staging_lists.get("exit_vectors", []) or list(fallback.get("exit_vectors", [])),
        "beat_transition_map": staging_lists.get("beat_transition_map", []) or list(fallback.get("beat_transition_map", [])),
        "planned_shot_overrides": planned_shot_lists.get("planned_shot_list", []) or planned_shot_freeform,
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
    scene_staging = _derive_scene_staging(
        scene_id=scene_id,
        summary=summary,
        purpose=purpose,
        emotional_arc=emotional_arc,
        continuity_constraints=continuity_constraints,
        beats=beats,
    )
    planned_shots = _derive_planned_shots(beats)
    scene_short_description = _scene_short_description(summary, purpose, emotional_arc)
    scene_primary_scale_story_point = _scene_scale_story_point(summary, purpose, evidence_summary)
    scene_required_anchor_catalog = _scene_required_anchor_catalog(
        list(scene_staging.get("scene_spatial_layout", [])),
        list(scene_staging.get("environment_subzones", [])),
        evidence_summary,
    )
    for item in planned_shots:
        if not item.planned_shot_required_anchor_1:
            item.planned_shot_required_anchor_1 = scene_required_anchor_catalog[0] if scene_required_anchor_catalog else ""
        if not item.planned_shot_scale_proof_detail:
            item.planned_shot_scale_proof_detail = scene_primary_scale_story_point
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
        "scene_short_description": scene_short_description,
        "scene_primary_scale_story_point": scene_primary_scale_story_point,
        "scene_required_anchor_catalog": scene_required_anchor_catalog,
        "storyboard_markdown": storyboard_markdown,
        "beat_overrides": [beat.to_dict() for beat in beats],
        "planned_shot_overrides": [item.to_dict() for item in planned_shots],
        "continuity_overrides": continuity_constraints,
        "coverage_overrides": coverage_families,
        "beats": beats,
        "planned_shots": planned_shots,
        **scene_staging,
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
            [_resolve_character_reference(project_slug, label, scene_markdown, project_dir, chapter_id) for label in raw_characters]
        )
        environment_refs = _dedupe_scene_references(
            [_resolve_environment_reference(project_slug, label, scene_markdown, project_dir, chapter_id) for label in raw_environments]
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
            "schema_version": SCENE_CONTRACT_SCHEMA_VERSION,
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
                scene_short_description=existing.get("scene_short_description", ""),
                scene_primary_scale_story_point=existing.get("scene_primary_scale_story_point", ""),
                scene_required_anchor_catalog=existing.get("scene_required_anchor_catalog", []),
                scene_start_state=existing.get("scene_start_state", ""),
                scene_end_state=existing.get("scene_end_state", ""),
                dominant_action_line=existing.get("dominant_action_line", ""),
                scene_spatial_layout=existing.get("scene_spatial_layout", []),
                character_spatial_map=existing.get("character_spatial_map", []),
                environment_subzones=existing.get("environment_subzones", []),
                entry_vectors=existing.get("entry_vectors", []),
                exit_vectors=existing.get("exit_vectors", []),
                beat_transition_map=existing.get("beat_transition_map", []),
                characters_required=[SceneReference(**item) for item in existing.get("characters_required", []) if isinstance(item, dict)],
                environments_required=[SceneReference(**item) for item in existing.get("environments_required", []) if isinstance(item, dict)],
                continuity_constraints=existing.get("continuity_constraints", []),
                visual_coverage_families=existing.get("visual_coverage_families", []),
                beat_list=[SceneBeat(**item) for item in existing.get("beat_list", []) if isinstance(item, dict)],
                planned_shots=[PlannedShotSeed(**item) for item in existing.get("planned_shots", []) if isinstance(item, dict)],
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
                    scene_short_description=existing.get("scene_short_description", ""),
                    scene_primary_scale_story_point=existing.get("scene_primary_scale_story_point", ""),
                    scene_required_anchor_catalog=existing.get("scene_required_anchor_catalog", []),
                    scene_start_state=existing.get("scene_start_state", ""),
                    scene_end_state=existing.get("scene_end_state", ""),
                    dominant_action_line=existing.get("dominant_action_line", ""),
                    scene_spatial_layout=existing.get("scene_spatial_layout", []),
                    character_spatial_map=existing.get("character_spatial_map", []),
                    environment_subzones=existing.get("environment_subzones", []),
                    entry_vectors=existing.get("entry_vectors", []),
                    exit_vectors=existing.get("exit_vectors", []),
                    beat_transition_map=existing.get("beat_transition_map", []),
                    characters_required=[SceneReference(**item) for item in existing.get("characters_required", []) if isinstance(item, dict)],
                    environments_required=[SceneReference(**item) for item in existing.get("environments_required", []) if isinstance(item, dict)],
                    continuity_constraints=existing.get("continuity_constraints", []),
                    visual_coverage_families=existing.get("visual_coverage_families", []),
                    beat_list=[SceneBeat(**item) for item in existing.get("beat_list", []) if isinstance(item, dict)],
                    planned_shots=[PlannedShotSeed(**item) for item in existing.get("planned_shots", []) if isinstance(item, dict)],
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
                fallback_payload=fallback_payload,
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
        scene_short_description = _first_nonempty(merged.get("scene_short_description"), fallback_payload.get("scene_short_description"), fallback="")
        scene_primary_scale_story_point = _first_nonempty(
            merged.get("scene_primary_scale_story_point"),
            fallback_payload.get("scene_primary_scale_story_point"),
            fallback="",
        )
        scene_required_anchor_catalog = _coerce_string_list(merged.get("scene_required_anchor_catalog", [])) or list(
            fallback_payload.get("scene_required_anchor_catalog", [])
        )
        storyboard_markdown = _first_nonempty(merged.get("storyboard_markdown"), fallback_payload["storyboard_markdown"], fallback="")
        scene_start_state = _first_nonempty(merged.get("scene_start_state"), fallback_payload.get("scene_start_state"), fallback="")
        scene_end_state = _first_nonempty(merged.get("scene_end_state"), fallback_payload.get("scene_end_state"), fallback="")
        dominant_action_line = _first_nonempty(merged.get("dominant_action_line"), fallback_payload.get("dominant_action_line"), fallback="")
        scene_spatial_layout = _coerce_string_list(merged.get("scene_spatial_layout", [])) or list(fallback_payload.get("scene_spatial_layout", []))
        character_spatial_map = _coerce_string_list(merged.get("character_spatial_map", [])) or list(fallback_payload.get("character_spatial_map", []))
        environment_subzones = _coerce_string_list(merged.get("environment_subzones", [])) or list(fallback_payload.get("environment_subzones", []))
        entry_vectors = _coerce_string_list(merged.get("entry_vectors", [])) or list(fallback_payload.get("entry_vectors", []))
        exit_vectors = _coerce_string_list(merged.get("exit_vectors", [])) or list(fallback_payload.get("exit_vectors", []))
        beat_transition_map = _coerce_string_list(merged.get("beat_transition_map", [])) or list(fallback_payload.get("beat_transition_map", []))
        planned_shots = _coerce_planned_shots(merged.get("planned_shot_overrides", []), fallback_shots=fallback_payload["planned_shots"])

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
            scene_short_description=scene_short_description,
            scene_primary_scale_story_point=scene_primary_scale_story_point,
            scene_required_anchor_catalog=scene_required_anchor_catalog,
            scene_start_state=scene_start_state,
            scene_end_state=scene_end_state,
            dominant_action_line=dominant_action_line,
            scene_spatial_layout=scene_spatial_layout,
            character_spatial_map=character_spatial_map,
            environment_subzones=environment_subzones,
            entry_vectors=entry_vectors,
            exit_vectors=exit_vectors,
            beat_transition_map=beat_transition_map,
            characters_required=character_refs,
            environments_required=environment_refs,
            continuity_constraints=continuity_constraints,
            visual_coverage_families=coverage_families,
            beat_list=beats,
            planned_shots=planned_shots,
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
        contract.planned_shots = contract.planned_shots or fallback_payload["planned_shots"]

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
                        action_start=_first_nonempty(item.get("action_start"), item.get("start"), fallback=""),
                        action_end=_first_nonempty(item.get("action_end"), item.get("end"), fallback=""),
                        active_subjects=_coerce_string_list(item.get("active_subjects", [])),
                        passive_subjects=_coerce_string_list(item.get("passive_subjects", [])),
                        spatial_context=_first_nonempty(item.get("spatial_context"), item.get("space"), fallback=""),
                        blocking_hint=_first_nonempty(item.get("blocking_hint"), item.get("blocking"), fallback=""),
                        environment_subzone=_first_nonempty(item.get("environment_subzone"), item.get("subzone"), fallback=""),
                        continuity_focus=_first_nonempty(item.get("continuity_focus"), item.get("continuity"), fallback=""),
                        coverage_hint=_first_nonempty(item.get("coverage_hint"), fallback=""),
                        coverage_priority=_first_nonempty(item.get("coverage_priority"), item.get("priority"), fallback=""),
                        handoff_to_next=_first_nonempty(item.get("handoff_to_next"), item.get("handoff"), fallback=""),
                    )
                )
            elif isinstance(item, str):
                beat_id = f"BT{index:03d}"
                raw = item.strip()
                match = re.match(r"^\s*(BT\d{3})\s*:\s*(.*)$", raw, re.IGNORECASE)
                if match:
                    beat_id = match.group(1).upper()
                    raw = match.group(2).strip()
                chunks = [chunk.strip() for chunk in raw.split("||") if chunk.strip()]
                summary = chunks[0] if chunks else raw
                fields: dict[str, str] = {}
                for chunk in chunks[1:]:
                    if "=" not in chunk:
                        continue
                    key, value = chunk.split("=", 1)
                    fields[_normalize_key(key)] = value.strip()
                beats.append(
                    SceneBeat(
                        beat_id=beat_id,
                        summary=summary or item.strip(),
                        purpose=_first_nonempty(fields.get("purpose"), fallback=""),
                        action_start=_first_nonempty(fields.get("action_start"), fields.get("start"), fallback=""),
                        action_end=_first_nonempty(fields.get("action_end"), fields.get("end"), fallback=""),
                        active_subjects=_coerce_string_list(fields.get("active_subjects", "")),
                        passive_subjects=_coerce_string_list(fields.get("passive_subjects", "")),
                        spatial_context=_first_nonempty(fields.get("spatial_context"), fields.get("space"), fallback=""),
                        blocking_hint=_first_nonempty(fields.get("blocking_hint"), fields.get("blocking"), fallback=""),
                        environment_subzone=_first_nonempty(fields.get("environment_subzone"), fields.get("subzone"), fallback=""),
                        continuity_focus=_first_nonempty(fields.get("continuity_focus"), fields.get("continuity"), fallback=""),
                        coverage_hint=_first_nonempty(fields.get("coverage_hint"), fields.get("coverage"), fallback=""),
                        coverage_priority=_first_nonempty(fields.get("coverage_priority"), fields.get("priority"), fallback=""),
                        handoff_to_next=_first_nonempty(fields.get("handoff_to_next"), fields.get("handoff"), fallback=""),
                    )
                )
    if beats:
        return beats
    return fallback_beats


def _coerce_planned_shots(raw_planned_shots: Any, *, fallback_shots: list[PlannedShotSeed]) -> list[PlannedShotSeed]:
    planned: list[PlannedShotSeed] = []
    if isinstance(raw_planned_shots, list):
        for index, item in enumerate(raw_planned_shots, start=1):
            if isinstance(item, PlannedShotSeed):
                planned.append(item)
                continue
            if isinstance(item, dict):
                planned.append(
                    PlannedShotSeed(
                        planned_shot_id=_first_nonempty(item.get("planned_shot_id"), item.get("shot_id"), fallback=f"SH{index:03d}"),
                        beat_id=_first_nonempty(item.get("beat_id"), fallback=f"BT{index:03d}"),
                        narrative_function=_first_nonempty(item.get("narrative_function"), item.get("function"), fallback=""),
                        planned_shot_moment_summary=_first_nonempty(item.get("planned_shot_moment_summary"), item.get("moment"), fallback=""),
                        primary_subject_seed=_first_nonempty(item.get("primary_subject_seed"), item.get("primary_subject"), fallback=""),
                        secondary_subjects_seed=_coerce_string_list(item.get("secondary_subjects_seed", []), item.get("secondary_subjects", [])),
                        subject_visibility=_first_nonempty(item.get("subject_visibility"), fallback=""),
                        narration_mode=_first_nonempty(item.get("narration_mode"), fallback=""),
                        environment_subzone=_first_nonempty(item.get("environment_subzone"), item.get("subzone"), fallback=""),
                        planned_shot_required_anchor_1=_first_nonempty(
                            item.get("planned_shot_required_anchor_1"),
                            item.get("required_anchor_1"),
                            item.get("anchor1"),
                            fallback="",
                        ),
                        planned_shot_scale_proof_detail=_first_nonempty(
                            item.get("planned_shot_scale_proof_detail"),
                            item.get("required_scale_proof_detail"),
                            item.get("scale_proof"),
                            fallback="",
                        ),
                        start_state_seed=_first_nonempty(item.get("start_state_seed"), item.get("start_state"), fallback=""),
                        end_state_seed=_first_nonempty(item.get("end_state_seed"), item.get("end_state"), fallback=""),
                        action_seed=_first_nonempty(item.get("action_seed"), item.get("action"), fallback=""),
                        blocking_seed=_coerce_string_list(item.get("blocking_seed", []), item.get("blocking", "")),
                        shot_size=_first_nonempty(item.get("shot_size"), fallback=""),
                        camera_angle=_first_nonempty(item.get("camera_angle"), fallback=""),
                        lens_family=_first_nonempty(item.get("lens_family"), fallback=""),
                        camera_motion=_first_nonempty(item.get("camera_motion"), fallback=""),
                        zoom_behavior=_first_nonempty(item.get("zoom_behavior"), fallback=""),
                        focus_strategy=_first_nonempty(item.get("focus_strategy"), fallback=""),
                        lighting_style=_first_nonempty(item.get("lighting_style"), fallback=""),
                        primary_subject_angle=_first_nonempty(item.get("primary_subject_angle"), fallback=""),
                    )
                )
            elif isinstance(item, str):
                raw = item.strip()
                match = re.match(r"^\s*(SH\d{3})\s*:\s*(.*)$", raw, re.IGNORECASE)
                shot_id = f"SH{index:03d}"
                if match:
                    shot_id = match.group(1).upper()
                    raw = match.group(2).strip()
                chunks = [chunk.strip() for chunk in raw.split("||") if chunk.strip()]
                fields: dict[str, str] = {}
                for chunk in chunks:
                    if "=" not in chunk:
                        continue
                    key, value = chunk.split("=", 1)
                    fields[_normalize_key(key)] = value.strip()
                planned.append(
                    PlannedShotSeed(
                        planned_shot_id=shot_id,
                        beat_id=_first_nonempty(fields.get("beat"), fields.get("beat_id"), fallback=f"BT{index:03d}"),
                        narrative_function=_first_nonempty(fields.get("function"), fields.get("narrative_function"), fallback=""),
                        planned_shot_moment_summary=_first_nonempty(fields.get("moment"), fields.get("planned_shot_moment_summary"), fallback=""),
                        primary_subject_seed=_first_nonempty(fields.get("primary"), fields.get("primary_subject_seed"), fallback=""),
                        secondary_subjects_seed=_coerce_string_list(fields.get("secondary"), fields.get("secondary_subjects_seed")),
                        subject_visibility=_first_nonempty(fields.get("visibility"), fields.get("subject_visibility"), fallback=""),
                        narration_mode=_first_nonempty(fields.get("narration"), fields.get("narration_mode"), fallback=""),
                        environment_subzone=_first_nonempty(fields.get("subzone"), fields.get("environment_subzone"), fallback=""),
                        planned_shot_required_anchor_1=_first_nonempty(
                            fields.get("anchor1"),
                            fields.get("required_anchor_1"),
                            fields.get("planned_shot_required_anchor_1"),
                            fallback="",
                        ),
                        planned_shot_scale_proof_detail=_first_nonempty(
                            fields.get("scale_proof"),
                            fields.get("required_scale_proof_detail"),
                            fields.get("planned_shot_scale_proof_detail"),
                            fallback="",
                        ),
                        start_state_seed=_first_nonempty(fields.get("start"), fields.get("start_state_seed"), fallback=""),
                        end_state_seed=_first_nonempty(fields.get("end"), fields.get("end_state_seed"), fallback=""),
                        action_seed=_first_nonempty(fields.get("action"), fields.get("action_seed"), fallback=""),
                        blocking_seed=_coerce_string_list(fields.get("blocking"), fields.get("blocking_seed")),
                        shot_size=_first_nonempty(fields.get("shot_size"), fallback=""),
                        camera_angle=_first_nonempty(fields.get("camera_angle"), fallback=""),
                        lens_family=_first_nonempty(fields.get("lens"), fields.get("lens_family"), fallback=""),
                        camera_motion=_first_nonempty(fields.get("motion"), fields.get("camera_motion"), fallback=""),
                        zoom_behavior=_first_nonempty(fields.get("zoom"), fields.get("zoom_behavior"), fallback=""),
                        focus_strategy=_first_nonempty(fields.get("focus"), fields.get("focus_strategy"), fallback=""),
                        lighting_style=_first_nonempty(fields.get("lighting"), fields.get("lighting_style"), fallback=""),
                        primary_subject_angle=_first_nonempty(fields.get("subject_angle"), fields.get("primary_subject_angle"), fallback=""),
                    )
                )
    if planned:
        return planned
    return fallback_shots


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
    fallback_payload: dict[str, Any],
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
5. prompt-ready visual fragments rather than abstract summaries

STYLE RULES:
- prefer short visible clauses
- no markdown inside field values
- no generic filler like "primary scene playing area" or "maintain readability"
- if a scale relationship matters, make it explicit
- if a shot needs an anchor, choose a concrete object, structure, or subzone

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

[[SECTION scene_staging_markdown]]
scene_short_description: <one short visual line, 8-20 words, no names required>
scene_primary_scale_story_point: <one short scale or hierarchy note>
scene_required_anchor_catalog:
- anchor 1
- anchor 2
scene_start_state: <how the scene begins visually and dramatically>
scene_end_state: <how the scene ends visually and dramatically>
dominant_action_line: <main action thread of the scene>
scene_spatial_layout:
- layout note 1
- layout note 2
character_spatial_map:
- subject placement note 1
- subject placement note 2
environment_subzones:
- subzone 1
- subzone 2
entry_vectors:
- entry path 1
exit_vectors:
- exit path 1
beat_transition_map:
- BT001 -> BT002: <transition>
- BT002 -> BT003: <transition>
[[/SECTION]]

[[SECTION planned_shots_markdown]]
planned_shot_list:
- SH001: beat=BT001 || function=<story function> || moment=<visible shot moment summary> || primary=<primary subject label> || secondary=<secondary label 1, secondary label 2> || visibility=<on_screen|partial|silhouette|off_screen_voice|implied_only> || narration=<none|voiceover_off_screen|in_scene_speaker|internal_monologue> || subzone=<environment subzone> || anchor1=<required environment anchor> || scale_proof=<required scale proof detail> || start=<specific shot start state> || end=<specific shot end state> || action=<specific shot action> || blocking=<blocking seed> || shot_size=<extreme_wide|wide|full|medium_full|medium|medium_close|close_up|extreme_close_up|insert_detail> || camera_angle=<eye_level|low_angle|high_angle|overhead|dutch> || lens=<ultra_wide|wide|normal|portrait|telephoto> || motion=<locked_off|pan|tilt|push_in|pull_back|track|crane|handheld> || zoom=<none|subtle_in|subtle_out|strong_in|strong_out> || focus=<deep_focus|shallow_subject|rack_focus|environment_priority> || lighting=<soft_even|hard_directional|high_contrast_ceremonial|diffuse_ambient|backlit|torch_firelight|low_key_night> || subject_angle=<front|front_three_quarter_left|front_three_quarter_right|profile_left|profile_right|rear_three_quarter_left|rear_three_quarter_right|back>
- SH002: beat=BT002 || function=<...> || moment=<...> || primary=<...> || visibility=<...> || narration=<...> || subzone=<...> || anchor1=<...> || scale_proof=<...> || start=<...> || end=<...> || action=<...> || blocking=<...> || shot_size=<...> || camera_angle=<...> || lens=<...> || motion=<...> || zoom=<...> || focus=<...> || lighting=<...> || subject_angle=<...>
[[/SECTION]]

[[SECTION beat_markdown]]
beat_list:
- BT001: <summary> || action_start=<how the beat begins> || action_end=<how the beat ends> || active_subjects=<subject A, subject B> || passive_subjects=<subject C> || spatial_context=<where the action happens> || blocking_hint=<where people are staged> || environment_subzone=<specific subzone> || continuity=<continuity focus> || coverage=<coverage hint> || priority=<coverage priority> || handoff=<what the next beat inherits>
- BT002: <summary> || action_start=<...> || action_end=<...> || active_subjects=<...> || passive_subjects=<...> || spatial_context=<...> || blocking_hint=<...> || environment_subzone=<...> || continuity=<...> || coverage=<...> || priority=<...> || handoff=<...>
- BT003: <summary> || action_start=<...> || action_end=<...> || active_subjects=<...> || passive_subjects=<...> || spatial_context=<...> || blocking_hint=<...> || environment_subzone=<...> || continuity=<...> || coverage=<...> || priority=<...> || handoff=<...>
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
        _, beat_lists, beat_freeform = _parse_section_markdown(record.sections.get("beat_markdown", ""))
        staging_scalars, staging_lists, _ = _parse_section_markdown(record.sections.get("scene_staging_markdown", ""))
        _, planned_shot_lists, planned_shot_freeform = _parse_section_markdown(record.sections.get("planned_shots_markdown", ""))
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
            "scene_short_description": _first_nonempty(staging_scalars.get("scene_short_description"), fallback=fallback_payload.get("scene_short_description", "")),
            "scene_primary_scale_story_point": _first_nonempty(
                staging_scalars.get("scene_primary_scale_story_point"),
                fallback=fallback_payload.get("scene_primary_scale_story_point", ""),
            ),
            "scene_required_anchor_catalog": staging_lists.get("scene_required_anchor_catalog", []) or list(
                fallback_payload.get("scene_required_anchor_catalog", [])
            ),
            "scene_start_state": _first_nonempty(staging_scalars.get("scene_start_state"), fallback=fallback_payload.get("scene_start_state", "")),
            "scene_end_state": _first_nonempty(staging_scalars.get("scene_end_state"), fallback=fallback_payload.get("scene_end_state", "")),
            "dominant_action_line": _first_nonempty(staging_scalars.get("dominant_action_line"), fallback=fallback_payload.get("dominant_action_line", "")),
            "scene_spatial_layout": staging_lists.get("scene_spatial_layout", []) or list(fallback_payload.get("scene_spatial_layout", [])),
            "character_spatial_map": staging_lists.get("character_spatial_map", []) or list(fallback_payload.get("character_spatial_map", [])),
            "environment_subzones": staging_lists.get("environment_subzones", []) or list(fallback_payload.get("environment_subzones", [])),
            "entry_vectors": staging_lists.get("entry_vectors", []) or list(fallback_payload.get("entry_vectors", [])),
            "exit_vectors": staging_lists.get("exit_vectors", []) or list(fallback_payload.get("exit_vectors", [])),
            "beat_transition_map": staging_lists.get("beat_transition_map", []) or list(fallback_payload.get("beat_transition_map", [])),
            "planned_shot_overrides": planned_shot_lists.get("planned_shot_list", []) or planned_shot_freeform or list(fallback_payload.get("planned_shots", [])),
        }
    except Exception:
        return None
