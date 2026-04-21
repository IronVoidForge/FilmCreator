from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import stat
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

from .book_librarian import search_book_index, search_chapter_context
from .core.json_io import read_json, write_json
from .features.authoring.packet_parser import parse_packet_document
from .lmstudio_client import LMStudioClient
from .scaffold import create_project
from .settings import load_runtime_settings


DESCRIPTOR_ROOT = Path("02_story_analysis") / "descriptors"

CHARACTER_ENTITY_TYPE = "character"
ENVIRONMENT_ENTITY_TYPE = "environment"
SCENE_ENTITY_TYPE = "scene"
SHOT_ENTITY_TYPE = "shot"
KEY_ITEM_ENTITY_TYPE = "key_item"

EXPLICIT_ORIGINS = {"bible", "contract", "shot_package", "scene_contract", "registry_entry", "book_index", "llm_supported"}
INFERRED_ORIGINS = {"llm", "llm_generated", "heuristic", "book_window"}

CHARACTER_FIELD_ORDER = [
    "sex",
    "age_range",
    "height",
    "build",
    "skin_tone",
    "hair_color",
    "hair_style",
    "eye_color",
    "face_shape",
    "facial_hair",
    "distinctive_features",
    "costume_layers",
    "costume_materials",
    "costume_signature",
    "silhouette_notes",
    "recurring_accessories",
    "posture",
    "expression_tendency",
    "physical_presence_notes",
    "voice_or_presence_notes",
]

ENVIRONMENT_FIELD_ORDER = [
    "environment_type",
    "layout",
    "scale",
    "geography",
    "architecture",
    "pathways",
    "camera_friendly_landmarks",
    "materials",
    "lighting",
    "mood",
    "weather_or_atmosphere",
    "recurring_anchors",
    "foreground_midground_background",
    "depth_cues",
]

SCENE_FIELD_ORDER = [
    "action_summary",
    "emotional_beat",
    "participants",
    "key_items",
    "location_requirements",
    "camera_intent",
    "start_state",
    "end_state",
    "movement_notes",
    "transition_notes",
    "dialogue_relevance",
]

SHOT_FIELD_ORDER = [
    "shot_type",
    "previous_shot_id",
    "next_shot_id",
    "angle",
    "framing",
    "lens_family",
    "distance",
    "camera_height",
    "camera_motion",
    "zoom_behavior",
    "focus_target",
    "perspective_notes",
    "primary_subject",
    "secondary_subjects",
    "subject_positions",
    "pose_notes",
    "gaze_direction",
    "interaction_notes",
    "environment_id",
    "environment_label",
    "spatial_continuity",
    "background_layers",
    "foreground_elements",
    "midground_elements",
    "depth_cues",
    "start_state",
    "end_state",
    "movement_notes",
    "continuity_constraints",
    "keyframe_intent",
    "image_to_image_intent",
]

KEY_ITEM_FIELD_ORDER = [
    "item_kind",
    "shape",
    "scale",
    "materials",
    "color_palette",
    "ornamentation",
    "condition_or_wear",
    "holder_or_user_notes",
    "iconic_features",
    "symbolic_role",
]

KEY_ITEM_PATTERNS: list[tuple[str, str]] = [
    (r"\b(?:the\s+)?one\s+ring\b", "ring"),
    (r"\b(?:the\s+)?ring\b", "ring"),
    (r"\b(?:the\s+)?sword\b", "sword"),
    (r"\b(?:the\s+)?blade\b", "sword"),
    (r"\b(?:the\s+)?dagger\b", "dagger"),
    (r"\b(?:the\s+)?spear\b", "spear"),
    (r"\b(?:the\s+)?staff\b", "staff"),
    (r"\b(?:the\s+)?armor(?:\s+set)?\b", "armor set"),
    (r"\b(?:the\s+)?armour(?:\s+set)?\b", "armor set"),
    (r"\b(?:the\s+)?shield\b", "shield"),
    (r"\b(?:the\s+)?amulet\b", "amulet"),
    (r"\b(?:the\s+)?talisman\b", "talisman"),
    (r"\b(?:the\s+)?relic\b", "relic"),
    (r"\b(?:the\s+)?crown\b", "crown"),
    (r"\b(?:the\s+)?helmet\b", "helmet"),
    (r"\b(?:the\s+)?mask\b", "mask"),
    (r"\b(?:the\s+)?pendant\b", "pendant"),
    (r"\b(?:the\s+)?sigil\b", "sigil"),
    (r"\b(?:the\s+)?emblem\b", "emblem"),
    (r"\b(?:the\s+)?banner\b", "banner"),
    (r"\b(?:the\s+)?device\b", "device"),
    (r"\b(?:the\s+)?book\b", "book"),
    (r"\b(?:the\s+)?scroll\b", "scroll"),
    (r"\b(?:the\s+)?map\b", "map"),
    (r"\b(?:the\s+)?key\b", "key"),
]


@dataclass
class DescriptorMetadata:
    artifact_id: str
    artifact_type: str = "descriptor"
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
class DescriptorRecord:
    descriptor_id: str
    canonical_id: str
    display_name: str
    entity_type: str
    status: str = "canonical"
    field_values: dict[str, Any] = field(default_factory=dict)
    supported_field_values: dict[str, Any] = field(default_factory=dict)
    generated_field_values: dict[str, Any] = field(default_factory=dict)
    field_states: dict[str, str] = field(default_factory=dict)
    supported_field_states: dict[str, str] = field(default_factory=dict)
    generated_field_states: dict[str, str] = field(default_factory=dict)
    field_sources: dict[str, list[dict[str, Any]]] = field(default_factory=dict)
    supported_field_sources: dict[str, list[dict[str, Any]]] = field(default_factory=dict)
    generated_field_sources: dict[str, list[dict[str, Any]]] = field(default_factory=dict)
    field_confidence: dict[str, str] = field(default_factory=dict)
    supported_field_confidence: dict[str, str] = field(default_factory=dict)
    generated_field_confidence: dict[str, str] = field(default_factory=dict)
    field_origin: dict[str, str] = field(default_factory=dict)
    supported_field_origin: dict[str, str] = field(default_factory=dict)
    generated_field_origin: dict[str, str] = field(default_factory=dict)
    chapter_mentions: list[str] = field(default_factory=list)
    scene_mentions: list[str] = field(default_factory=list)
    shot_mentions: list[str] = field(default_factory=list)
    evidence_refs: list[dict[str, Any]] = field(default_factory=list)
    evidence_summary: list[str] = field(default_factory=list)
    inferred_fields: list[str] = field(default_factory=list)
    review_flags: list[str] = field(default_factory=list)
    related_assets: list[dict[str, Any]] = field(default_factory=list)
    metadata: DescriptorMetadata | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "descriptor_id": self.descriptor_id,
            "canonical_id": self.canonical_id,
            "display_name": self.display_name,
            "entity_type": self.entity_type,
            "status": self.status,
            "field_values": self.field_values,
            "supported_field_values": self.supported_field_values,
            "generated_field_values": self.generated_field_values,
            "field_states": self.field_states,
            "supported_field_states": self.supported_field_states,
            "generated_field_states": self.generated_field_states,
            "field_sources": self.field_sources,
            "supported_field_sources": self.supported_field_sources,
            "generated_field_sources": self.generated_field_sources,
            "field_confidence": self.field_confidence,
            "supported_field_confidence": self.supported_field_confidence,
            "generated_field_confidence": self.generated_field_confidence,
            "field_origin": self.field_origin,
            "supported_field_origin": self.supported_field_origin,
            "generated_field_origin": self.generated_field_origin,
            "chapter_mentions": self.chapter_mentions,
            "scene_mentions": self.scene_mentions,
            "shot_mentions": self.shot_mentions,
            "evidence_refs": self.evidence_refs,
            "evidence_summary": self.evidence_summary,
            "inferred_fields": self.inferred_fields,
            "review_flags": self.review_flags,
            "related_assets": self.related_assets,
            "metadata": self.metadata.to_dict() if self.metadata else None,
        }


@dataclass(frozen=True)
class DescriptorEnrichmentSummary:
    project_slug: str
    total_entries: int
    synthesized_count: int
    reused_count: int
    review_queue_count: int
    written_files: list[str]
    warnings: list[str]

    def to_dict(self) -> dict[str, Any]:
        return {
            "project_slug": self.project_slug,
            "total_entries": self.total_entries,
            "synthesized_count": self.synthesized_count,
            "reused_count": self.reused_count,
            "review_queue_count": self.review_queue_count,
            "written_files": self.written_files,
            "warnings": self.warnings,
        }


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _fingerprint(data: Any) -> str:
    raw = json.dumps(data, sort_keys=True, ensure_ascii=False)
    return hashlib.sha1(raw.encode("utf-8")).hexdigest()


def _descriptor_root(project_dir: Path) -> Path:
    return project_dir / DESCRIPTOR_ROOT


def _normalize_id(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", value.strip().lower()).strip("_")


def _normalize_text(value: str) -> str:
    return " ".join(value.split()).strip()


def _compact(text: str, *, limit: int = 220) -> str:
    collapsed = _normalize_text(text)
    if len(collapsed) <= limit:
        return collapsed
    return collapsed[: limit - 3].rstrip() + "..."


def _looks_like_metadata_summary(text: str) -> bool:
    normalized = " ".join(text.lower().split())
    metadata_markers = [
        "resolved known",
        "no competing canonical alias",
        "kept extracted asset id",
        "canonical id",
        "extracted asset id",
        "singular individual entity",
        "registry fallback",
        "alias detected",
    ]
    return any(marker in normalized for marker in metadata_markers)


def _clean_visual_summary(text: Any, *, fallback: str = "unknown", limit: int = 220) -> str:
    if not isinstance(text, str):
        return fallback
    cleaned = _normalize_text(text)
    if not cleaned or _looks_like_metadata_summary(cleaned):
        return fallback
    return _compact(cleaned, limit=limit)


def _first_nonempty(*values: object, fallback: str = "") -> str:
    for value in values:
        if isinstance(value, str) and value.strip():
            return value.strip()
    return fallback


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
            parts = [part.strip() for part in re.split(r",|\n|;", stripped) if part.strip()]
            items.extend(parts or [stripped])
    seen: set[str] = set()
    deduped: list[str] = []
    for item in items:
        if item not in seen:
            seen.add(item)
            deduped.append(item)
    return deduped


def _load_json_file(path: Path) -> dict[str, Any]:
    payload = read_json(path)
    return payload if isinstance(payload, dict) else {}


def _character_bible_paths(project_dir: Path) -> list[Path]:
    root = project_dir / "02_story_analysis" / "bibles" / "characters"
    return sorted(path for path in root.glob("CHAR_*.json") if path.is_file()) if root.exists() else []


def _environment_bible_paths(project_dir: Path) -> list[Path]:
    root = project_dir / "02_story_analysis" / "bibles" / "environments"
    return sorted(path for path in root.glob("ENV_*.json") if path.is_file()) if root.exists() else []


def _scene_contract_paths(project_dir: Path) -> list[Path]:
    root = project_dir / "02_story_analysis" / "contracts" / "scenes"
    return sorted(path for path in root.glob("CH*/CH*_SC*.json") if path.is_file()) if root.exists() else []


def _shot_package_paths(project_dir: Path) -> list[Path]:
    root = project_dir / "02_story_analysis" / "contracts" / "shots"
    return sorted(path for path in root.glob("CH*/CH*_SC*/SHOT_INDEX.json") if path.is_file()) if root.exists() else []


def _load_character_bibles(project_dir: Path) -> dict[str, dict[str, Any]]:
    records: dict[str, dict[str, Any]] = {}
    for path in _character_bible_paths(project_dir):
        payload = _load_json_file(path)
        character_id = str(payload.get("character_id", "")).strip().lower()
        if character_id:
            records[character_id] = payload
    return records


def _load_environment_bibles(project_dir: Path) -> dict[str, dict[str, Any]]:
    records: dict[str, dict[str, Any]] = {}
    for path in _environment_bible_paths(project_dir):
        payload = _load_json_file(path)
        environment_id = str(payload.get("environment_id", "")).strip().lower()
        if environment_id:
            records[environment_id] = payload
    return records


def _load_scene_contracts(project_dir: Path) -> dict[str, dict[str, Any]]:
    records: dict[str, dict[str, Any]] = {}
    for path in _scene_contract_paths(project_dir):
        payload = _load_json_file(path)
        scene_id = str(payload.get("scene_id", "")).strip().upper()
        if scene_id:
            records[scene_id] = payload
    return records


def _load_shot_packages(project_dir: Path) -> list[dict[str, Any]]:
    shots: list[dict[str, Any]] = []
    for path in _shot_package_paths(project_dir):
        payload = read_json(path)
        if not isinstance(payload, list):
            continue
        for item in payload:
            if isinstance(item, dict):
                shots.append(item)
    shots.sort(key=lambda item: (str(item.get("chapter_id", "")), str(item.get("scene_id", "")), int(item.get("shot_order", 0) or 0)))
    return shots


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


def _parse_markdown_section(section_text: str) -> tuple[dict[str, str], dict[str, list[str]], list[str]]:
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
            key = key.strip().lower().replace(" ", "_")
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


def _section_text(packet, section_name: str) -> str:
    return packet.sections.get(section_name, "").strip()


def _load_existing_metadata(existing: dict | None, artifact_id: str, fp: str) -> DescriptorMetadata:
    old_meta = (existing or {}).get("metadata") or {}
    return DescriptorMetadata(
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


def _merge_with_existing(new: dict[str, Any], existing: dict | None, metadata: DescriptorMetadata) -> dict[str, Any]:
    if not existing:
        return new
    merged = dict(new)
    for field_name, locked in metadata.locked_fields.items():
        if locked and field_name in existing:
            merged[field_name] = existing[field_name]
    for field_name, value in metadata.manual_overrides.items():
        merged[field_name] = value
    return merged


def _render_field_section(title: str, fields: list[tuple[str, Any]]) -> list[str]:
    lines = [title, ""]
    for key, value in fields:
        if value is None:
            continue
        if isinstance(value, list):
            if not value:
                continue
            lines.append(f"{key}:")
            for item in value:
                lines.append(f"- {item}")
            continue
        value_str = str(value).strip()
        if not value_str:
            continue
        lines.append(f"{key}: {value_str}")
    if lines[-1] != "":
        lines.append("")
    return lines


def _write_descriptor_markdown(path: Path, record: DescriptorRecord) -> None:
    lines = [
        f"# {record.entity_type.replace('_', ' ').title()} Descriptor: {record.display_name}",
        "",
        f"- descriptor_id: `{record.descriptor_id}`",
        f"- canonical_id: `{record.canonical_id}`",
        f"- status: `{record.status}`",
        f"- entity_type: `{record.entity_type}`",
        "",
        "## Supported Fields",
        "",
    ]
    for field_name in sorted(record.supported_field_values.keys()):
        value = record.supported_field_values[field_name]
        if isinstance(value, list):
            if not value:
                continue
            lines.append(f"- {field_name}:")
            for item in value:
                lines.append(f"  - {item}")
        else:
            value_str = str(value).strip()
            if value_str:
                lines.append(f"- {field_name}: {value_str}")

    lines.extend(["", "## Generated Fields", ""])
    for field_name in sorted(record.generated_field_values.keys()):
        value = record.generated_field_values[field_name]
        if isinstance(value, list):
            if not value:
                continue
            lines.append(f"- {field_name}:")
            for item in value:
                lines.append(f"  - {item}")
        else:
            value_str = str(value).strip()
            if value_str:
                lines.append(f"- {field_name}: {value_str}")

    lines.extend(
        [
            "",
            "## Coverage",
            "",
            f"- chapter_mentions: {', '.join(record.chapter_mentions) if record.chapter_mentions else '(none)'}",
            f"- scene_mentions: {', '.join(record.scene_mentions) if record.scene_mentions else '(none)'}",
            f"- shot_mentions: {', '.join(record.shot_mentions) if record.shot_mentions else '(none)'}",
            "",
            "## Evidence Summary",
            "",
        ]
    )
    if record.evidence_summary:
        lines.extend([f"- {item}" for item in record.evidence_summary])
    else:
        lines.append("- (none)")
    lines.extend(["", "## Review", ""])
    if record.review_flags:
        lines.extend([f"- {item}" for item in record.review_flags])
    else:
        lines.append("- (none)")
    lines.extend(["", "## Metadata", ""])
    if record.metadata:
        lines.extend(
            [
                f"- artifact_id: `{record.metadata.artifact_id}`",
                f"- status: `{record.metadata.status}`",
                f"- source_fingerprint: `{record.metadata.source_fingerprint}`",
                f"- created_at_utc: `{record.metadata.created_at_utc}`",
                f"- updated_at_utc: `{record.metadata.updated_at_utc}`",
            ]
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _write_descriptor_files(base_path: Path, record: DescriptorRecord) -> None:
    write_json(base_path.with_suffix(".json"), record.to_dict())
    _write_descriptor_markdown(base_path.with_suffix(".md"), record)


def _descriptor_index_lines(title: str, records: list[DescriptorRecord]) -> str:
    lines = [f"# {title}", ""]
    if not records:
        lines.append("- No entries.")
        return "\n".join(lines) + "\n"
    for record in sorted(records, key=lambda item: (item.entity_type, item.canonical_id)):
        lines.append(
            f"- `{record.entity_type}:{record.canonical_id}` - {record.display_name} "
            f"(status={record.status}, mentions={len(record.chapter_mentions)}, review={len(record.review_flags)})"
        )
    return "\n".join(lines) + "\n"


def _write_index(path: Path, records: list[DescriptorRecord], *, title: str) -> None:
    path.write_text(_descriptor_index_lines(title, records), encoding="utf-8")


def _write_review_queue(path: Path, queue: list[dict[str, Any]], *, title: str) -> None:
    lines = [f"# {title}", ""]
    if not queue:
        lines.append("- No review items.")
    else:
        grouped: dict[str, list[dict[str, Any]]] = {}
        for item in queue:
            prefix = str(item.get("entity_type", "other")).strip().lower() or "other"
            grouped.setdefault(prefix, []).append(item)
        for group_name in sorted(grouped.keys()):
            lines.append(f"## {group_name.title()}")
            lines.append("")
            for item in grouped[group_name]:
                lines.append(f"- `{item.get('descriptor_id', '')}`")
                for issue in item.get("issues", []):
                    lines.append(f"  - {issue}")
            lines.append("")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _descriptor_field_state(origin: str, value: Any) -> str:
    if value is None:
        return "unknown"
    if isinstance(value, str):
        normalized = value.strip().lower()
        if not normalized or normalized in {"unknown", "none", "(none)", "n/a"}:
            return "unknown"
    if origin in EXPLICIT_ORIGINS:
        return "explicit"
    if origin in INFERRED_ORIGINS:
        return "inferred"
    return "review_needed"


def _descriptor_field_confidence(state: str, value: Any) -> str:
    if state == "explicit":
        return "high"
    if state == "inferred":
        return "medium"
    if state == "review_needed":
        return "low"
    return "low"


def _add_field(
    field_values: dict[str, Any],
    field_states: dict[str, str],
    field_confidence: dict[str, str],
    field_origin: dict[str, str],
    field_sources: dict[str, list[dict[str, Any]]],
    inferred_fields: list[str],
    key: str,
    value: Any,
    *,
    origin: str,
    source_ref: dict[str, Any] | None = None,
) -> None:
    if value is None:
        return
    if isinstance(value, str):
        cleaned = value.strip()
        if not cleaned:
            return
        value = cleaned
    elif isinstance(value, list):
        value = [item.strip() for item in value if isinstance(item, str) and item.strip()]
        if not value:
            return
    field_values[key] = value
    state = _descriptor_field_state(origin, value)
    field_states[key] = state
    field_confidence[key] = _descriptor_field_confidence(state, value)
    field_origin[key] = origin
    if source_ref is not None:
        field_sources.setdefault(key, []).append(source_ref)
    if state == "inferred":
        inferred_fields.append(key)


def _split_descriptor_field_views(
    field_values: dict[str, Any],
    field_origin: dict[str, str],
    field_states: dict[str, str],
    field_confidence: dict[str, str],
    field_sources: dict[str, list[dict[str, Any]]],
) -> tuple[
    dict[str, Any],
    dict[str, Any],
    dict[str, str],
    dict[str, str],
    dict[str, list[dict[str, Any]]],
    dict[str, list[dict[str, Any]]],
    dict[str, str],
    dict[str, str],
    dict[str, str],
    dict[str, str],
]:
    supported_values: dict[str, Any] = {}
    generated_values: dict[str, Any] = {}
    supported_states: dict[str, str] = {}
    generated_states: dict[str, str] = {}
    supported_sources: dict[str, list[dict[str, Any]]] = {}
    generated_sources: dict[str, list[dict[str, Any]]] = {}
    supported_confidence: dict[str, str] = {}
    generated_confidence: dict[str, str] = {}
    supported_origin: dict[str, str] = {}
    generated_origin: dict[str, str] = {}

    for key, value in field_values.items():
        origin = field_origin.get(key, "fallback")
        state = field_states.get(key, _descriptor_field_state(origin, value))
        confidence = field_confidence.get(key, _descriptor_field_confidence(state, value))
        sources = field_sources.get(key, [])
        if value is None or state == "unknown":
            continue
        if origin in EXPLICIT_ORIGINS and state == "explicit":
            supported_values[key] = value
            supported_states[key] = state
            supported_sources[key] = sources
            supported_confidence[key] = confidence
            supported_origin[key] = origin
        elif origin in INFERRED_ORIGINS or origin == "heuristic":
            generated_values[key] = value
            generated_states[key] = state
            generated_sources[key] = sources
            generated_confidence[key] = confidence
            generated_origin[key] = origin
        elif state in {"explicit", "inferred", "review_needed"}:
            supported_values[key] = value
            supported_states[key] = state
            supported_sources[key] = sources
            supported_confidence[key] = confidence
            supported_origin[key] = origin
        else:
            generated_values[key] = value
            generated_states[key] = state
            generated_sources[key] = sources
            generated_confidence[key] = confidence
            generated_origin[key] = origin

    return (
        supported_values,
        generated_values,
        supported_states,
        generated_states,
        supported_sources,
        generated_sources,
        supported_confidence,
        generated_confidence,
        supported_origin,
        generated_origin,
    )


def _chapter_id_from_path(source_path: str) -> str:
    for part in Path(source_path).parts:
        if part.startswith("CH") and len(part) >= 5:
            return part[:5].upper()
    return ""


def _scene_id_from_shot_path(source_path: str) -> str:
    for part in Path(source_path).parts:
        if re.fullmatch(r"CH\d{3}_SC\d{3}", part.upper()):
            return part.upper()
    return ""


def _build_reference_maps(
    scene_contracts: dict[str, dict[str, Any]],
    shot_packages: list[dict[str, Any]],
) -> tuple[dict[str, list[str]], dict[str, list[str]], dict[str, list[str]], dict[str, list[str]]]:
    character_scenes: dict[str, list[str]] = {}
    character_shots: dict[str, list[str]] = {}
    environment_scenes: dict[str, list[str]] = {}
    environment_shots: dict[str, list[str]] = {}

    for scene_id, contract in scene_contracts.items():
        for ref in contract.get("characters_required", []):
            if not isinstance(ref, dict):
                continue
            canonical = str(ref.get("canonical_id", "")).strip().lower()
            if canonical:
                character_scenes.setdefault(canonical, []).append(scene_id)
        for ref in contract.get("environments_required", []):
            if not isinstance(ref, dict):
                continue
            canonical = str(ref.get("canonical_id", "")).strip().lower()
            if canonical:
                environment_scenes.setdefault(canonical, []).append(scene_id)

    for shot in shot_packages:
        scene_id = str(shot.get("scene_id", "")).strip().upper()
        shot_id = str(shot.get("shot_id", "")).strip().upper()
        if not scene_id or not shot_id:
            continue
        for ref in shot.get("characters_in_frame", []):
            if not isinstance(ref, dict):
                continue
            canonical = str(ref.get("canonical_id", "")).strip().lower()
            if canonical:
                character_shots.setdefault(canonical, []).append(f"{scene_id}/{shot_id}")
        env = shot.get("environment")
        if isinstance(env, dict):
            canonical = str(env.get("canonical_id", "")).strip().lower()
            if canonical:
                environment_shots.setdefault(canonical, []).append(f"{scene_id}/{shot_id}")

    return character_scenes, character_shots, environment_scenes, environment_shots


def _collect_character_evidence(
    project_slug: str,
    project_dir: Path,
    char_id: str,
    entry: dict[str, Any],
    bible: dict[str, Any],
    scene_mentions: list[str],
    shot_mentions: list[str],
) -> tuple[list[str], list[dict[str, Any]]]:
    evidence_lines: list[str] = []
    evidence_refs: list[dict[str, Any]] = []
    seen: set[str] = set()

    def add_line(line: str, ref: dict[str, Any]) -> None:
        normalized = _normalize_text(line)
        if not normalized or normalized in seen:
            return
        if len(normalized) > 260:
            normalized = normalized[:257].rstrip() + "..."
        seen.add(normalized)
        evidence_lines.append(normalized)
        evidence_refs.append(ref)

    for value in [
        bible.get("stable_visual_summary", ""),
        bible.get("physical_traits", []),
        bible.get("costume_signature", ""),
        bible.get("personality", ""),
        bible.get("role", ""),
        bible.get("voice_notes", ""),
    ]:
        if isinstance(value, list):
            for item in value:
                if isinstance(item, str) and item.strip() and not _looks_like_metadata_summary(item):
                    add_line(item, {"source": "character_bible", "chapter_id": None, "source_path": None})
        elif isinstance(value, str) and value.strip() and not _looks_like_metadata_summary(value):
            add_line(value, {"source": "character_bible", "chapter_id": None, "source_path": None})

    desc_layers = entry.get("description_layers", {})
    for section_name in ("stable_canonical", "initial_extracted"):
        for item in desc_layers.get(section_name, [])[:3]:
            if isinstance(item, dict):
                summary = str(item.get("summary", "")).strip()
                if summary:
                    add_line(summary, {"source": f"registry_{section_name}", "chapter_id": item.get("chapter_id"), "source_path": item.get("source_path")})
            elif isinstance(item, str) and item.strip():
                add_line(item, {"source": f"registry_{section_name}", "chapter_id": None, "source_path": None})

    for chapter_id in (entry.get("chapter_mentions", []) or [])[:4]:
        chapter_id = str(chapter_id).strip().upper()
        if not chapter_id:
            continue
        for term in _character_query_terms(entry, bible):
            try:
                contexts = search_chapter_context(project_slug, chapter_id, [term], window=1, top_n=2)
            except Exception:
                continue
            for context in contexts:
                snippet = _compact(context.preview or context.text, limit=220)
                if snippet:
                    add_line(
                        f"[{chapter_id} p{context.paragraph_start}-p{context.paragraph_end}] {snippet}",
                        {
                            "source": "book_window",
                            "chapter_id": chapter_id,
                            "source_path": context.chapter_path,
                            "paragraph_start": context.paragraph_start,
                            "paragraph_end": context.paragraph_end,
                        },
                    )
                if len(evidence_lines) >= 8:
                    break
            if len(evidence_lines) >= 8:
                break

    query = " ".join(_character_query_terms(entry, bible)[:3]).strip()
    if query:
        for hit in search_book_index(project_slug, query, top_n=3):
            chapter_id = str(hit.get("chapter_id", "")).strip().upper()
            reasons = ", ".join(str(reason) for reason in hit.get("reasons", [])[:2] if str(reason).strip())
            add_line(
                f"[{chapter_id}] {hit.get('title', '')} ({reasons or 'book index hit'})",
                {"source": "book_index", "chapter_id": chapter_id or None, "source_path": None},
            )

    if not evidence_lines:
        add_line(
            _compact(str(entry.get("resolution_reason", "")) or bible.get("stable_visual_summary", "") or entry.get("display_name", "") or char_id, limit=220),
            {"source": "registry_fallback", "chapter_id": None, "source_path": None},
        )

    return evidence_lines[:8], evidence_refs[:8]


def _character_query_terms(entry: dict[str, Any], bible: dict[str, Any]) -> list[str]:
    terms: list[str] = []
    for value in [entry.get("display_name"), entry.get("canonical_id"), *entry.get("aliases", []), bible.get("display_name"), bible.get("costume_signature"), bible.get("stable_visual_summary")]:
        if isinstance(value, str) and value.strip():
            normalized = _normalize_text(value.replace("_", " "))
            if normalized and normalized not in terms:
                terms.append(normalized)
    for trait in bible.get("physical_traits", []):
        if isinstance(trait, str) and trait.strip() and trait.strip() not in terms:
            terms.append(trait.strip())
    return terms[:5]


def _collect_environment_evidence(
    project_slug: str,
    entry: dict[str, Any],
    bible: dict[str, Any],
) -> tuple[list[str], list[dict[str, Any]]]:
    evidence_lines: list[str] = []
    evidence_refs: list[dict[str, Any]] = []
    seen: set[str] = set()

    def add_line(line: str, ref: dict[str, Any]) -> None:
        normalized = _normalize_text(line)
        if not normalized or normalized in seen:
            return
        if len(normalized) > 260:
            normalized = normalized[:257].rstrip() + "..."
        seen.add(normalized)
        evidence_lines.append(normalized)
        evidence_refs.append(ref)

    for value in [
        bible.get("visual_summary", ""),
        bible.get("layout_notes", ""),
        bible.get("lighting", ""),
        bible.get("mood", ""),
        bible.get("recurring_elements", []),
        bible.get("constraints", []),
    ]:
        if isinstance(value, list):
            for item in value:
                if isinstance(item, str) and item.strip() and not _looks_like_metadata_summary(item):
                    add_line(item, {"source": "environment_bible", "chapter_id": None, "source_path": None})
        elif isinstance(value, str) and value.strip() and not _looks_like_metadata_summary(value):
            add_line(value, {"source": "environment_bible", "chapter_id": None, "source_path": None})

    desc_layers = entry.get("description_layers", {})
    for section_name in ("stable_canonical", "initial_extracted"):
        for item in desc_layers.get(section_name, [])[:3]:
            if isinstance(item, dict):
                summary = str(item.get("summary", "")).strip()
                if summary:
                    add_line(summary, {"source": f"registry_{section_name}", "chapter_id": item.get("chapter_id"), "source_path": item.get("source_path")})
            elif isinstance(item, str) and item.strip():
                add_line(item, {"source": f"registry_{section_name}", "chapter_id": None, "source_path": None})

    for chapter_id in (entry.get("chapter_mentions", []) or [])[:4]:
        chapter_id = str(chapter_id).strip().upper()
        if not chapter_id:
            continue
        for term in _environment_query_terms(entry, bible):
            try:
                contexts = search_chapter_context(project_slug, chapter_id, [term], window=1, top_n=2)
            except Exception:
                continue
            for context in contexts:
                snippet = _compact(context.preview or context.text, limit=220)
                if snippet:
                    add_line(
                        f"[{chapter_id} p{context.paragraph_start}-p{context.paragraph_end}] {snippet}",
                        {
                            "source": "book_window",
                            "chapter_id": chapter_id,
                            "source_path": context.chapter_path,
                            "paragraph_start": context.paragraph_start,
                            "paragraph_end": context.paragraph_end,
                        },
                    )
                if len(evidence_lines) >= 8:
                    break
            if len(evidence_lines) >= 8:
                break

    query = " ".join(_environment_query_terms(entry, bible)[:3]).strip()
    if query:
        for hit in search_book_index(project_slug, query, top_n=3):
            chapter_id = str(hit.get("chapter_id", "")).strip().upper()
            reasons = ", ".join(str(reason) for reason in hit.get("reasons", [])[:2] if str(reason).strip())
            add_line(
                f"[{chapter_id}] {hit.get('title', '')} ({reasons or 'book index hit'})",
                {"source": "book_index", "chapter_id": chapter_id or None, "source_path": None},
            )

    if not evidence_lines:
        add_line(
            _compact(str(entry.get("resolution_reason", "")) or bible.get("visual_summary", "") or entry.get("display_name", "") or entry.get("canonical_id", ""), limit=220),
            {"source": "registry_fallback", "chapter_id": None, "source_path": None},
        )

    return evidence_lines[:8], evidence_refs[:8]


def _environment_query_terms(entry: dict[str, Any], bible: dict[str, Any]) -> list[str]:
    terms: list[str] = []
    for value in [entry.get("display_name"), entry.get("canonical_id"), bible.get("display_name"), bible.get("environment_type"), bible.get("visual_summary"), bible.get("layout_notes")]:
        if isinstance(value, str) and value.strip():
            normalized = _normalize_text(value.replace("_", " "))
            if normalized and normalized not in terms:
                terms.append(normalized)
    for item in bible.get("recurring_elements", []):
        if isinstance(item, str) and item.strip() and item.strip() not in terms:
            terms.append(item.strip())
    return terms[:5]


def _collect_scene_evidence(project_slug: str, scene_id: str, scene_contract: dict[str, Any]) -> tuple[list[str], list[dict[str, Any]]]:
    evidence_lines: list[str] = []
    evidence_refs: list[dict[str, Any]] = []
    seen: set[str] = set()

    def add_line(line: str, ref: dict[str, Any]) -> None:
        normalized = _normalize_text(line)
        if not normalized or normalized in seen:
            return
        if len(normalized) > 260:
            normalized = normalized[:257].rstrip() + "..."
        seen.add(normalized)
        evidence_lines.append(normalized)
        evidence_refs.append(ref)

    for key in ("purpose", "summary", "emotional_arc", "production_intent", "storyboard_markdown"):
        value = scene_contract.get(key, "")
        if isinstance(value, str) and value.strip():
            add_line(value, {"source": "scene_contract", "scene_id": scene_id, "chapter_id": scene_id[:5], "source_path": None})

    for beat in scene_contract.get("beat_list", [])[:4]:
        if not isinstance(beat, dict):
            continue
        summary = str(beat.get("summary", "")).strip()
        if summary:
            add_line(summary, {"source": "scene_contract_beat", "scene_id": scene_id, "chapter_id": scene_id[:5], "source_path": None})

    for item in scene_contract.get("continuity_constraints", [])[:4]:
        if isinstance(item, str) and item.strip():
            add_line(item, {"source": "scene_contract_continuity", "scene_id": scene_id, "chapter_id": scene_id[:5], "source_path": None})

    if scene_contract.get("evidence_summary"):
        for item in scene_contract.get("evidence_summary", [])[:3]:
            if isinstance(item, str) and item.strip():
                add_line(item, {"source": "scene_contract_evidence", "scene_id": scene_id, "chapter_id": scene_id[:5], "source_path": None})

    if not evidence_lines:
        add_line(scene_id, {"source": "scene_fallback", "scene_id": scene_id, "chapter_id": scene_id[:5], "source_path": None})
    return evidence_lines[:8], evidence_refs[:8]


def _collect_shot_evidence(
    project_slug: str,
    shot: dict[str, Any],
    scene_contract: dict[str, Any],
) -> tuple[list[str], list[dict[str, Any]]]:
    evidence_lines: list[str] = []
    evidence_refs: list[dict[str, Any]] = []
    seen: set[str] = set()

    def add_line(line: str, ref: dict[str, Any]) -> None:
        normalized = _normalize_text(line)
        if not normalized or normalized in seen:
            return
        if len(normalized) > 260:
            normalized = normalized[:257].rstrip() + "..."
        seen.add(normalized)
        evidence_lines.append(normalized)
        evidence_refs.append(ref)

    for key in ("shot_title", "shot_type", "camera_description", "composition", "prompt_seed", "shot_notes"):
        value = shot.get(key, "")
        if isinstance(value, str) and value.strip():
            add_line(value, {"source": "shot_package", "scene_id": shot.get("scene_id", ""), "shot_id": shot.get("shot_id", ""), "chapter_id": shot.get("chapter_id", ""), "source_path": None})

    for item in shot.get("continuity_constraints", [])[:4]:
        if isinstance(item, str) and item.strip():
            add_line(item, {"source": "shot_package_continuity", "scene_id": shot.get("scene_id", ""), "shot_id": shot.get("shot_id", ""), "chapter_id": shot.get("chapter_id", ""), "source_path": None})

    for item in shot.get("evidence_summary", [])[:3]:
        if isinstance(item, str) and item.strip():
            add_line(item, {"source": "shot_package_evidence", "scene_id": shot.get("scene_id", ""), "shot_id": shot.get("shot_id", ""), "chapter_id": shot.get("chapter_id", ""), "source_path": None})

    if scene_contract.get("summary"):
        add_line(str(scene_contract.get("summary")), {"source": "scene_contract", "scene_id": shot.get("scene_id", ""), "shot_id": shot.get("shot_id", ""), "chapter_id": shot.get("chapter_id", ""), "source_path": None})

    if not evidence_lines:
        add_line(str(shot.get("shot_id", "")), {"source": "shot_fallback", "scene_id": shot.get("scene_id", ""), "shot_id": shot.get("shot_id", ""), "chapter_id": shot.get("chapter_id", ""), "source_path": None})
    return evidence_lines[:8], evidence_refs[:8]


def _collect_key_item_candidates(scene_contracts: dict[str, dict[str, Any]], shot_packages: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    candidates: dict[str, dict[str, Any]] = {}

    def add_candidate(display_name: str, item_kind: str, source_text: str, ref: dict[str, Any]) -> None:
        normalized = _normalize_id(display_name)
        if not normalized:
            return
        candidate = candidates.setdefault(
            normalized,
            {
                "display_name": display_name.strip(),
                "item_kind": item_kind,
                "chapter_mentions": [],
                "scene_mentions": [],
                "shot_mentions": [],
                "evidence_summary": [],
                "evidence_refs": [],
                "status": "canonical",
            },
        )
        if display_name and len(display_name) > len(candidate["display_name"]):
            candidate["display_name"] = display_name.strip()
        candidate["item_kind"] = item_kind
        if ref.get("chapter_id") and ref["chapter_id"] not in candidate["chapter_mentions"]:
            candidate["chapter_mentions"].append(ref["chapter_id"])
        if ref.get("scene_id") and ref["scene_id"] not in candidate["scene_mentions"]:
            candidate["scene_mentions"].append(ref["scene_id"])
        if ref.get("shot_id"):
            shot_label = f"{ref.get('scene_id', '')}/{ref.get('shot_id', '')}".strip("/")
            if shot_label and shot_label not in candidate["shot_mentions"]:
                candidate["shot_mentions"].append(shot_label)
        snippet = _compact(source_text, limit=220)
        if snippet and snippet not in candidate["evidence_summary"]:
            candidate["evidence_summary"].append(snippet)
        if ref not in candidate["evidence_refs"]:
            candidate["evidence_refs"].append(ref)

    def scan_texts(texts: list[tuple[str, dict[str, Any]]]) -> None:
        for text, ref in texts:
            haystack = text or ""
            for pattern, kind in KEY_ITEM_PATTERNS:
                for match in re.finditer(pattern, haystack, re.IGNORECASE):
                    raw = match.group(0).strip()
                    if not raw:
                        continue
                    add_candidate(raw, kind, haystack[max(0, match.start() - 60): match.end() + 80], ref)

    scene_texts: list[tuple[str, dict[str, Any]]] = []
    for scene_id, contract in scene_contracts.items():
        chapter_id = scene_id[:5]
        for key in ("purpose", "summary", "emotional_arc", "production_intent", "storyboard_markdown"):
            value = contract.get(key, "")
            if isinstance(value, str) and value.strip():
                scene_texts.append((value, {"chapter_id": chapter_id, "scene_id": scene_id, "source": "scene_contract"}))
        for item in contract.get("beat_list", []):
            if isinstance(item, dict):
                summary = str(item.get("summary", "")).strip()
                if summary:
                    scene_texts.append((summary, {"chapter_id": chapter_id, "scene_id": scene_id, "source": "scene_contract_beat"}))
    scan_texts(scene_texts)

    shot_texts: list[tuple[str, dict[str, Any]]] = []
    for shot in shot_packages:
        scene_id = str(shot.get("scene_id", "")).strip().upper()
        chapter_id = str(shot.get("chapter_id", "")).strip().upper() or scene_id[:5]
        shot_id = str(shot.get("shot_id", "")).strip().upper()
        if not scene_id or not shot_id:
            continue
        for key in ("shot_title", "shot_type", "camera_description", "composition", "prompt_seed", "shot_notes"):
            value = shot.get(key, "")
            if isinstance(value, str) and value.strip():
                shot_texts.append((value, {"chapter_id": chapter_id, "scene_id": scene_id, "shot_id": shot_id, "source": "shot_package"}))
    scan_texts(shot_texts)

    if not candidates:
        return {}

    filtered: dict[str, dict[str, Any]] = {}
    for key, candidate in candidates.items():
        mention_count = len(candidate["evidence_refs"])
        if mention_count >= 2 or any(part[:1].isupper() for part in candidate["display_name"].split()):
            filtered[key] = candidate
    return filtered or candidates


def _determine_field_relevance(value: Any) -> str:
    if value is None:
        return "unknown"
    if isinstance(value, str):
        normalized = value.strip().lower()
        if not normalized or normalized in {"unknown", "none", "(none)", "n/a"}:
            return "unknown"
        return "present"
    if isinstance(value, list):
        return "present" if any(isinstance(item, str) and item.strip() for item in value) else "unknown"
    if isinstance(value, dict):
        return "present" if value else "unknown"
    return "present"


def _llm_refine_descriptor(
    *,
    entity_type: str,
    descriptor_id: str,
    canonical_id: str,
    display_name: str,
    status: str,
    base_fields: dict[str, Any],
    evidence_summary: list[str],
    desired_fields: list[str],
) -> dict[str, Any] | None:
    settings = load_runtime_settings()
    client = LMStudioClient(settings)

    system = (
        "You are a descriptor enrichment system for a film pipeline. "
        "Use only the provided evidence. Prefer compact structured markdown. "
        "If evidence directly supports a detail, put it in supported fields. "
        "If you make a careful visual choice to complete the canon, put it in generated fields. "
        "Never place inferred detail in supported fields. "
        "For generated fields, prefer a best-effort visual decision over unknown when canon and evidence make a reasonable choice. "
        "Do not leave generated visual fields empty when a reasonable canon-compatible choice can be made. "
        "Return one tagged FilmCreator markdown packet only. "
        "Do not return JSON."
    )

    desired_field_lines = "\n".join(f"- {field}" for field in desired_fields)
    user = f"""
Enrich the following {entity_type} descriptor using the evidence provided.

Keep the output compact. Favor structured fields over prose.
Use the book, registry, and existing contract evidence for supported fields.
Use careful inference for generated fields when the text does not spell out a visual detail but the canon is still clear.
For generated fields, make a best-effort visual decision from the book evidence and stable context instead of using unknown whenever the canon supports a reasonable choice. Do not leave generated visual fields empty if you can make a canon-compatible choice. Put those values in generated_fields_markdown, keep supported_fields_markdown strictly book-backed, and use review flags for anything still low-confidence or questionable.

DESCRIPTOR:
{json.dumps({
    "descriptor_id": descriptor_id,
    "canonical_id": canonical_id,
    "display_name": display_name,
    "entity_type": entity_type,
    "status": status,
    "base_fields": base_fields,
}, indent=2, ensure_ascii=False)}

EVIDENCE:
{json.dumps(evidence_summary, indent=2, ensure_ascii=False)}

Fields to fill when evidence supports them:
{desired_field_lines}

Return exactly one FilmCreator packet:
[[FILMCREATOR_PACKET]]
task: descriptor_enrichment
version: 1

[[FILMCREATOR_RECORD]]
type: descriptor
artifact_id: {descriptor_id}
canonical_id: {canonical_id}
display_name: {display_name}
entity_type: {entity_type}
status: {status}

[[SECTION supported_fields_markdown]]
field_name: supported field value
field_name:
- list item 1
- list item 2
[[/SECTION]]

[[SECTION generated_fields_markdown]]
field_name: generated field value
field_name:
- list item 1
- list item 2
[[/SECTION]]

[[SECTION coverage_markdown]]
chapter_mentions:
- CH001
scene_mentions:
- CH001_SC001
shot_mentions:
- CH001_SC001/SH001
[[/SECTION]]

[[SECTION review_markdown]]
review_flags:
- low_confidence_field
inferred_fields:
- field_name
[[/SECTION]]

[[SECTION evidence_markdown]]
- evidence line 1
- evidence line 2
[[/SECTION]]

[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
"""

    try:
        response = client.chat_completion(system_prompt=system, user_prompt=user, temperature=0.1)
        packet = parse_packet_document(response, expected_task="descriptor_enrichment")
        if not packet.records:
            return None
        record = packet.records[0]
        supported_scalars, supported_lists, supported_freeform = _parse_markdown_section(_section_text(packet, "supported_fields_markdown"))
        generated_scalars, generated_lists, generated_freeform = _parse_markdown_section(_section_text(packet, "generated_fields_markdown"))
        coverage_scalars, coverage_lists, coverage_freeform = _parse_markdown_section(_section_text(packet, "coverage_markdown"))
        review_scalars, review_lists, review_freeform = _parse_markdown_section(_section_text(packet, "review_markdown"))
        evidence_scalars, evidence_lists, evidence_freeform = _parse_markdown_section(_section_text(packet, "evidence_markdown"))
        supported: dict[str, Any] = {}
        generated: dict[str, Any] = {}
        for field in desired_fields:
            if field in supported_lists and supported_lists[field]:
                supported[field] = supported_lists[field]
            elif field in supported_scalars and supported_scalars[field]:
                supported[field] = supported_scalars[field]
            if field in generated_lists and generated_lists[field]:
                generated[field] = generated_lists[field]
            elif field in generated_scalars and generated_scalars[field]:
                generated[field] = generated_scalars[field]
        merged: dict[str, Any] = {}
        merged.update(supported)
        for key, value in generated.items():
            merged.setdefault(key, value)
        merged["supported_field_values"] = supported
        merged["generated_field_values"] = generated
        merged["chapter_mentions"] = _coerce_string_list(coverage_lists.get("chapter_mentions"), coverage_scalars.get("chapter_mentions"))
        merged["scene_mentions"] = _coerce_string_list(coverage_lists.get("scene_mentions"), coverage_scalars.get("scene_mentions"))
        merged["shot_mentions"] = _coerce_string_list(coverage_lists.get("shot_mentions"), coverage_scalars.get("shot_mentions"))
        merged["review_flags"] = _coerce_string_list(review_lists.get("review_flags"), review_scalars.get("review_flags"), review_freeform)
        merged["inferred_fields"] = _coerce_string_list(review_lists.get("inferred_fields"), review_scalars.get("inferred_fields"))
        merged["evidence_summary"] = _coerce_string_list(evidence_lists.get("evidence_markdown"), evidence_scalars.get("evidence_markdown")) or list(evidence_freeform)
        return merged
    except Exception:
        return None


def _finalize_descriptor(
    *,
    descriptor_id: str,
    canonical_id: str,
    display_name: str,
    entity_type: str,
    status: str,
    field_values: dict[str, Any],
    field_origin: dict[str, str],
    field_sources: dict[str, list[dict[str, Any]]],
    chapter_mentions: list[str],
    scene_mentions: list[str],
    shot_mentions: list[str],
    evidence_refs: list[dict[str, Any]],
    evidence_summary: list[str],
    inferred_fields: list[str],
    review_flags: list[str],
    related_assets: list[dict[str, Any]],
    metadata: DescriptorMetadata,
) -> DescriptorRecord:
    field_states: dict[str, str] = {}
    field_confidence: dict[str, str] = {}
    for key, value in field_values.items():
        origin = field_origin.get(key, "fallback")
        state = _descriptor_field_state(origin, value)
        if key in inferred_fields and state == "explicit":
            state = "inferred"
        if value is None or state == "unknown":
            state = "unknown"
        field_states[key] = state
        field_confidence[key] = _descriptor_field_confidence(state, value)
    (
        supported_field_values,
        generated_field_values,
        supported_field_states,
        generated_field_states,
        supported_field_sources,
        generated_field_sources,
        supported_field_confidence,
        generated_field_confidence,
        supported_field_origin,
        generated_field_origin,
    ) = _split_descriptor_field_views(field_values, field_origin, field_states, field_confidence, field_sources)
    return DescriptorRecord(
        descriptor_id=descriptor_id,
        canonical_id=canonical_id,
        display_name=display_name,
        entity_type=entity_type,
        status=status,
        field_values=field_values,
        supported_field_values=supported_field_values,
        generated_field_values=generated_field_values,
        field_states=field_states,
        supported_field_states=supported_field_states,
        generated_field_states=generated_field_states,
        field_sources=field_sources,
        supported_field_sources=supported_field_sources,
        generated_field_sources=generated_field_sources,
        field_confidence=field_confidence,
        supported_field_confidence=supported_field_confidence,
        generated_field_confidence=generated_field_confidence,
        field_origin=field_origin,
        supported_field_origin=supported_field_origin,
        generated_field_origin=generated_field_origin,
        chapter_mentions=_ordered_unique(chapter_mentions),
        scene_mentions=_ordered_unique(scene_mentions),
        shot_mentions=_ordered_unique(shot_mentions),
        evidence_refs=evidence_refs,
        evidence_summary=evidence_summary[:25],
        inferred_fields=_ordered_unique(inferred_fields),
        review_flags=_ordered_unique(review_flags),
        related_assets=related_assets,
        metadata=metadata,
    )


def _ordered_unique(values: list[str]) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []
    for value in values:
        if value in seen:
            continue
        seen.add(value)
        ordered.append(value)
    return ordered


def _base_character_descriptor(
    project_slug: str,
    project_dir: Path,
    char_id: str,
    entry: dict[str, Any],
    bible: dict[str, Any],
    scene_mentions: list[str],
    shot_mentions: list[str],
    use_llm: bool,
) -> DescriptorRecord:
    evidence_summary, evidence_refs = _collect_character_evidence(project_slug, project_dir, char_id, entry, bible, scene_mentions, shot_mentions)
    base_fields: dict[str, Any] = {}
    field_origin: dict[str, str] = {}
    field_sources: dict[str, list[dict[str, Any]]] = {}
    inferred_fields: list[str] = []
    review_flags: list[str] = []
    related_assets: list[dict[str, Any]] = []

    def set_field(key: str, value: Any, *, origin: str, ref: dict[str, Any] | None = None) -> None:
        _add_field(base_fields, {}, {}, field_origin, field_sources, inferred_fields, key, value, origin=origin, source_ref=ref)

    set_field("sex", bible.get("sex") or entry.get("sex") or "unknown", origin="bible")
    set_field("age_range", bible.get("age_range") or entry.get("age_range") or "unknown", origin="bible")
    set_field("role", bible.get("role") or entry.get("entity_kind") or "unknown", origin="bible")
    set_field("entity_kind", entry.get("entity_kind") or "individual", origin="registry_entry")
    set_field("aliases", _coerce_string_list(bible.get("aliases", []), entry.get("aliases", [])), origin="bible")
    set_field("height", "unknown", origin="fallback")
    set_field("build", "unknown", origin="fallback")
    set_field("skin_tone", "unknown", origin="fallback")
    set_field("hair_color", "unknown", origin="fallback")
    set_field("hair_style", "unknown", origin="fallback")
    set_field("eye_color", "unknown", origin="fallback")
    set_field("face_shape", "unknown", origin="fallback")
    set_field("facial_hair", "unknown", origin="fallback")
    set_field("distinctive_features", _coerce_string_list(bible.get("physical_traits", [])), origin="bible")
    set_field("costume_layers", _coerce_string_list(bible.get("costume_signature", "")), origin="bible")
    set_field("costume_materials", "unknown", origin="fallback")
    set_field("costume_signature", bible.get("costume_signature") or "unknown", origin="bible")
    set_field("silhouette_notes", _clean_visual_summary(bible.get("stable_visual_summary"), fallback="unknown"), origin="bible")
    set_field("recurring_accessories", _coerce_string_list(bible.get("relationship_notes", [])), origin="bible")
    set_field("posture", "unknown", origin="fallback")
    set_field("expression_tendency", "unknown", origin="fallback")
    set_field("physical_presence_notes", _clean_visual_summary(bible.get("stable_visual_summary"), fallback="unknown"), origin="bible")
    set_field("voice_or_presence_notes", _clean_visual_summary(bible.get("voice_notes"), fallback="unknown"), origin="bible")
    set_field("chapter_mentions", _coerce_string_list(entry.get("chapter_mentions", [])), origin="registry_entry")

    llm_payload = None
    if use_llm:
        llm_payload = _llm_refine_descriptor(
            entity_type=CHARACTER_ENTITY_TYPE,
            descriptor_id=f"DESC_CHAR_{char_id}",
            canonical_id=char_id,
            display_name=bible.get("display_name") or entry.get("display_name") or char_id,
            status=entry.get("status", "canonical"),
            base_fields=base_fields,
            evidence_summary=evidence_summary,
            desired_fields=CHARACTER_FIELD_ORDER,
        )

    if llm_payload:
        for field_name, value in (llm_payload.get("supported_field_values") or {}).items():
            if value:
                base_fields[field_name] = value
                field_origin[field_name] = "llm_supported"
        for field_name, value in (llm_payload.get("generated_field_values") or {}).items():
            if value:
                base_fields[field_name] = value
                field_origin[field_name] = "llm_generated"
                if field_name not in inferred_fields:
                    inferred_fields.append(field_name)
        if llm_payload.get("chapter_mentions"):
            base_fields["chapter_mentions"] = llm_payload["chapter_mentions"]
        review_flags.extend(llm_payload.get("review_flags", []))
        evidence_summary = _coerce_string_list(llm_payload.get("evidence_summary", []), evidence_summary)
        related_assets = []

    if not evidence_summary:
        evidence_summary = ["No usable evidence lines were collected."]

    if "unknown" in {str(base_fields.get("height", "")).lower(), str(base_fields.get("hair_color", "")).lower(), str(base_fields.get("eye_color", "")).lower()}:
        review_flags.append("low_confidence_visual_fields")
    if "unknown" in str(base_fields.get("sex", "")).lower():
        review_flags.append("sex_unresolved")

    metadata = DescriptorMetadata(
        artifact_id=f"DESC_CHAR_{char_id}",
        artifact_type="descriptor_character",
        status="generated",
        source_fingerprint=_fingerprint({"entry": entry, "bible": bible, "evidence": evidence_summary, "kind": "character"}),
        created_at_utc=_utc_now(),
        updated_at_utc=_utc_now(),
        upstream_dependencies=[
            {"dependency_type": "character_bible", "dependency_id": char_id, "version": _fingerprint(bible)},
            {"dependency_type": "character_registry_entry", "dependency_id": char_id, "version": _fingerprint(entry)},
        ],
    )
    return _finalize_descriptor(
        descriptor_id=metadata.artifact_id,
        canonical_id=char_id,
        display_name=_first_nonempty(str(bible.get("display_name", "")), str(entry.get("display_name", "")), fallback=char_id),
        entity_type=CHARACTER_ENTITY_TYPE,
        status=entry.get("status", "canonical"),
        field_values=base_fields,
        field_origin=field_origin,
        field_sources=field_sources,
        chapter_mentions=_coerce_string_list(entry.get("chapter_mentions", [])),
        scene_mentions=scene_mentions,
        shot_mentions=shot_mentions,
        evidence_refs=evidence_refs,
        evidence_summary=evidence_summary,
        inferred_fields=inferred_fields,
        review_flags=review_flags,
        related_assets=related_assets,
        metadata=metadata,
    )


def _base_environment_descriptor(
    project_slug: str,
    project_dir: Path,
    env_id: str,
    entry: dict[str, Any],
    bible: dict[str, Any],
    scene_mentions: list[str],
    shot_mentions: list[str],
    use_llm: bool,
) -> DescriptorRecord:
    evidence_summary, evidence_refs = _collect_environment_evidence(project_slug, entry, bible)
    base_fields: dict[str, Any] = {}
    field_origin: dict[str, str] = {}
    field_sources: dict[str, list[dict[str, Any]]] = {}
    inferred_fields: list[str] = []
    review_flags: list[str] = []

    def set_field(key: str, value: Any, *, origin: str, ref: dict[str, Any] | None = None) -> None:
        _add_field(base_fields, {}, {}, field_origin, field_sources, inferred_fields, key, value, origin=origin, source_ref=ref)

    set_field("environment_type", bible.get("environment_type") or entry.get("entity_kind") or "environment", origin="bible")
    set_field("layout", bible.get("layout_notes") or "unknown", origin="bible")
    set_field("scale", "unknown", origin="fallback")
    set_field("geography", "unknown", origin="fallback")
    set_field("architecture", "unknown", origin="fallback")
    set_field("pathways", "unknown", origin="fallback")
    set_field("camera_friendly_landmarks", _coerce_string_list(bible.get("recurring_elements", [])), origin="bible")
    set_field("materials", "unknown", origin="fallback")
    set_field("lighting", bible.get("lighting") or "unknown", origin="bible")
    set_field("mood", bible.get("mood") or "unknown", origin="bible")
    set_field("weather_or_atmosphere", "unknown", origin="fallback")
    set_field("recurring_anchors", _coerce_string_list(bible.get("recurring_elements", [])), origin="bible")
    set_field("foreground_midground_background", "unknown", origin="fallback")
    set_field("depth_cues", "unknown", origin="fallback")
    set_field("chapter_mentions", _coerce_string_list(entry.get("chapter_mentions", [])), origin="registry_entry")

    llm_payload = None
    if use_llm:
        llm_payload = _llm_refine_descriptor(
            entity_type=ENVIRONMENT_ENTITY_TYPE,
            descriptor_id=f"DESC_ENV_{env_id}",
            canonical_id=env_id,
            display_name=bible.get("display_name") or entry.get("display_name") or env_id,
            status=entry.get("status", "canonical"),
            base_fields=base_fields,
            evidence_summary=evidence_summary,
            desired_fields=ENVIRONMENT_FIELD_ORDER,
        )

    if llm_payload:
        for field_name, value in (llm_payload.get("supported_field_values") or {}).items():
            if value:
                base_fields[field_name] = value
                field_origin[field_name] = "llm_supported"
        for field_name, value in (llm_payload.get("generated_field_values") or {}).items():
            if value:
                base_fields[field_name] = value
                field_origin[field_name] = "llm_generated"
                if field_name not in inferred_fields:
                    inferred_fields.append(field_name)
        if llm_payload.get("chapter_mentions"):
            base_fields["chapter_mentions"] = llm_payload["chapter_mentions"]
        review_flags.extend(llm_payload.get("review_flags", []))
        evidence_summary = _coerce_string_list(llm_payload.get("evidence_summary", []), evidence_summary)

    if "unknown" in {str(base_fields.get("layout", "")).lower(), str(base_fields.get("lighting", "")).lower(), str(base_fields.get("mood", "")).lower()}:
        review_flags.append("low_confidence_spatial_fields")

    metadata = DescriptorMetadata(
        artifact_id=f"DESC_ENV_{env_id}",
        artifact_type="descriptor_environment",
        status="generated",
        source_fingerprint=_fingerprint({"entry": entry, "bible": bible, "evidence": evidence_summary, "kind": "environment"}),
        created_at_utc=_utc_now(),
        updated_at_utc=_utc_now(),
        upstream_dependencies=[
            {"dependency_type": "environment_bible", "dependency_id": env_id, "version": _fingerprint(bible)},
            {"dependency_type": "environment_registry_entry", "dependency_id": env_id, "version": _fingerprint(entry)},
        ],
    )
    return _finalize_descriptor(
        descriptor_id=metadata.artifact_id,
        canonical_id=env_id,
        display_name=_first_nonempty(str(bible.get("display_name", "")), str(entry.get("display_name", "")), fallback=env_id),
        entity_type=ENVIRONMENT_ENTITY_TYPE,
        status=entry.get("status", "canonical"),
        field_values=base_fields,
        field_origin=field_origin,
        field_sources=field_sources,
        chapter_mentions=_coerce_string_list(entry.get("chapter_mentions", [])),
        scene_mentions=scene_mentions,
        shot_mentions=shot_mentions,
        evidence_refs=evidence_refs,
        evidence_summary=evidence_summary,
        inferred_fields=inferred_fields,
        review_flags=review_flags,
        related_assets=[],
        metadata=metadata,
    )


def _base_scene_descriptor(
    scene_id: str,
    scene_contract: dict[str, Any],
    shot_mentions: list[str],
    use_llm: bool,
) -> DescriptorRecord:
    evidence_summary, evidence_refs = _collect_scene_evidence("", scene_id, scene_contract)
    base_fields: dict[str, Any] = {}
    field_origin: dict[str, str] = {}
    field_sources: dict[str, list[dict[str, Any]]] = {}
    inferred_fields: list[str] = []
    review_flags: list[str] = []

    def set_field(key: str, value: Any, *, origin: str) -> None:
        _add_field(base_fields, {}, {}, field_origin, field_sources, inferred_fields, key, value, origin=origin)

    set_field("chapter_id", scene_contract.get("chapter_id") or scene_id[:5], origin="scene_contract")
    set_field("scene_title", scene_contract.get("scene_title") or scene_id, origin="scene_contract")
    set_field("action_summary", scene_contract.get("summary") or scene_contract.get("production_intent") or "unknown", origin="scene_contract")
    set_field("emotional_beat", scene_contract.get("emotional_arc") or "unknown", origin="scene_contract")
    set_field("participants", _coerce_string_list([ref.get("display_name", ref.get("label", "")) for ref in scene_contract.get("characters_required", []) if isinstance(ref, dict)]), origin="scene_contract")
    set_field("key_items", "unknown", origin="fallback")
    set_field("location_requirements", _coerce_string_list([ref.get("display_name", ref.get("label", "")) for ref in scene_contract.get("environments_required", []) if isinstance(ref, dict)]), origin="scene_contract")
    camera_intent = "; ".join(_coerce_string_list(scene_contract.get("visual_coverage_families", []))) or "unknown"
    set_field("camera_intent", camera_intent, origin="scene_contract")
    set_field("start_state", "unknown", origin="fallback")
    set_field("end_state", "unknown", origin="fallback")
    set_field("movement_notes", _coerce_string_list(scene_contract.get("continuity_constraints", [])), origin="scene_contract")
    set_field("transition_notes", scene_contract.get("storyboard_markdown") or "unknown", origin="scene_contract")
    set_field("dialogue_relevance", "unknown", origin="fallback")
    set_field("chapter_mentions", [scene_contract.get("chapter_id", scene_id[:5])], origin="scene_contract")

    if use_llm:
        llm_payload = _llm_refine_descriptor(
            entity_type=SCENE_ENTITY_TYPE,
            descriptor_id=f"DESC_{scene_id}",
            canonical_id=scene_id,
            display_name=scene_contract.get("scene_title") or scene_id,
            status=scene_contract.get("metadata", {}).get("status", "generated") if isinstance(scene_contract.get("metadata"), dict) else "generated",
            base_fields=base_fields,
            evidence_summary=evidence_summary,
            desired_fields=SCENE_FIELD_ORDER,
        )
        if llm_payload:
            for field_name, value in (llm_payload.get("supported_field_values") or {}).items():
                if value:
                    base_fields[field_name] = value
                    field_origin[field_name] = "llm_supported"
            for field_name, value in (llm_payload.get("generated_field_values") or {}).items():
                if value:
                    base_fields[field_name] = value
                    field_origin[field_name] = "llm_generated"
                    if field_name not in inferred_fields:
                        inferred_fields.append(field_name)
            if llm_payload.get("chapter_mentions"):
                base_fields["chapter_mentions"] = llm_payload["chapter_mentions"]
            review_flags.extend(llm_payload.get("review_flags", []))
            evidence_summary = _coerce_string_list(llm_payload.get("evidence_summary", []), evidence_summary)

    if not evidence_summary:
        evidence_summary = ["No usable evidence lines were collected."]
    metadata = DescriptorMetadata(
        artifact_id=f"DESC_{scene_id}",
        artifact_type="descriptor_scene",
        status="generated",
        source_fingerprint=_fingerprint({"scene": scene_contract, "evidence": evidence_summary, "kind": "scene"}),
        created_at_utc=_utc_now(),
        updated_at_utc=_utc_now(),
        upstream_dependencies=[{"dependency_type": "scene_contract", "dependency_id": scene_id, "version": _fingerprint(scene_contract)}],
    )
    return _finalize_descriptor(
        descriptor_id=metadata.artifact_id,
        canonical_id=scene_id,
        display_name=_first_nonempty(scene_contract.get("scene_title"), fallback=scene_id),
        entity_type=SCENE_ENTITY_TYPE,
        status="canonical",
        field_values=base_fields,
        field_origin=field_origin,
        field_sources=field_sources,
        chapter_mentions=[scene_contract.get("chapter_id", scene_id[:5])],
        scene_mentions=[scene_id],
        shot_mentions=shot_mentions,
        evidence_refs=evidence_refs,
        evidence_summary=evidence_summary,
        inferred_fields=inferred_fields,
        review_flags=review_flags,
        related_assets=[],
        metadata=metadata,
    )


def _base_shot_descriptor(
    shot: dict[str, Any],
    scene_contract: dict[str, Any],
    use_llm: bool,
) -> DescriptorRecord:
    scene_id = str(shot.get("scene_id", "")).strip().upper()
    shot_id = str(shot.get("shot_id", "")).strip().upper()
    evidence_summary, evidence_refs = _collect_shot_evidence("", shot, scene_contract)
    base_fields: dict[str, Any] = {}
    field_origin: dict[str, str] = {}
    field_sources: dict[str, list[dict[str, Any]]] = {}
    inferred_fields: list[str] = []
    review_flags: list[str] = []

    def set_field(key: str, value: Any, *, origin: str) -> None:
        _add_field(base_fields, {}, {}, field_origin, field_sources, inferred_fields, key, value, origin=origin)

    env_ref = shot.get("environment") if isinstance(shot.get("environment"), dict) else {}
    character_refs = shot.get("characters_in_frame", []) if isinstance(shot.get("characters_in_frame"), list) else []

    set_field("shot_type", shot.get("shot_type") or "medium", origin="shot_package")
    set_field("previous_shot_id", str(shot.get("previous_shot_id", "")).strip().upper() or "none", origin="shot_package")
    set_field("next_shot_id", str(shot.get("next_shot_id", "")).strip().upper() or "none", origin="shot_package")
    set_field("angle", shot.get("shot_type") or "medium", origin="shot_package")
    set_field("framing", shot.get("composition") or "Readable composition.", origin="shot_package")
    set_field("lens_family", "neutral_reference", origin="fallback")
    set_field("distance", "medium", origin="fallback")
    set_field("camera_height", "eye-level", origin="heuristic")
    set_field("camera_motion", shot.get("camera_description") or "stable", origin="shot_package")
    set_field("zoom_behavior", "stable", origin="heuristic")
    set_field("focus_target", _first_nonempty(shot.get("shot_title"), shot.get("prompt_seed"), fallback=shot_id), origin="shot_package")
    set_field("perspective_notes", shot.get("camera_description") or "unknown", origin="shot_package")
    set_field("characters_in_frame", _coerce_string_list([ref.get("display_name", ref.get("label", "")) for ref in character_refs if isinstance(ref, dict)]), origin="shot_package")
    set_field("primary_subject", _first_nonempty(*[ref.get("display_name", ref.get("label", "")) for ref in character_refs if isinstance(ref, dict)], fallback="unknown"), origin="shot_package")
    set_field("secondary_subjects", _coerce_string_list([ref.get("display_name", ref.get("label", "")) for ref in character_refs[1:] if isinstance(ref, dict)]), origin="shot_package")
    set_field("subject_positions", "unknown", origin="fallback")
    set_field("pose_notes", "unknown", origin="fallback")
    set_field("gaze_direction", "unknown", origin="fallback")
    set_field("interaction_notes", _coerce_string_list(shot.get("continuity_constraints", [])), origin="shot_package")
    set_field("environment_id", str(env_ref.get("canonical_id", "")).strip().lower() or "unknown", origin="shot_package")
    set_field("environment_label", _first_nonempty(str(env_ref.get("display_name", "")), str(env_ref.get("label", "")), fallback="unknown"), origin="shot_package")
    set_field("spatial_continuity", shot.get("composition") or "unknown", origin="shot_package")
    set_field("background_layers", "unknown", origin="fallback")
    set_field("foreground_elements", "unknown", origin="fallback")
    set_field("midground_elements", "unknown", origin="fallback")
    set_field("depth_cues", "unknown", origin="fallback")
    set_field("start_state", "unknown", origin="fallback")
    set_field("end_state", "unknown", origin="fallback")
    set_field("movement_notes", shot.get("shot_notes") or "unknown", origin="shot_package")
    set_field("continuity_constraints", _coerce_string_list(shot.get("continuity_constraints", []), scene_contract.get("continuity_constraints", [])), origin="shot_package")
    set_field("keyframe_intent", shot.get("prompt_seed") or "unknown", origin="shot_package")
    set_field("image_to_image_intent", "preserve canonical continuity", origin="heuristic")
    set_field("chapter_mentions", [scene_id[:5]] if scene_id else [], origin="shot_package")

    if use_llm:
        llm_payload = _llm_refine_descriptor(
            entity_type=SHOT_ENTITY_TYPE,
            descriptor_id=f"DESC_{scene_id}_{shot_id}",
            canonical_id=f"{scene_id}_{shot_id}",
            display_name=shot.get("shot_title") or shot_id,
            status="generated",
            base_fields=base_fields,
            evidence_summary=evidence_summary,
            desired_fields=SHOT_FIELD_ORDER,
        )
        if llm_payload:
            for field_name, value in (llm_payload.get("supported_field_values") or {}).items():
                if value:
                    base_fields[field_name] = value
                    field_origin[field_name] = "llm_supported"
            for field_name, value in (llm_payload.get("generated_field_values") or {}).items():
                if value:
                    base_fields[field_name] = value
                    field_origin[field_name] = "llm_generated"
                    if field_name not in inferred_fields:
                        inferred_fields.append(field_name)
            if llm_payload.get("chapter_mentions"):
                base_fields["chapter_mentions"] = llm_payload["chapter_mentions"]
            if llm_payload.get("scene_mentions"):
                base_fields["scene_mentions"] = llm_payload["scene_mentions"]
            if llm_payload.get("shot_mentions"):
                base_fields["shot_mentions"] = llm_payload["shot_mentions"]
            review_flags.extend(llm_payload.get("review_flags", []))
            evidence_summary = _coerce_string_list(llm_payload.get("evidence_summary", []), evidence_summary)

    if "unknown" in {str(base_fields.get("environment_label", "")).lower(), str(base_fields.get("primary_subject", "")).lower()}:
        review_flags.append("thin_shot_subject_context")
    metadata = DescriptorMetadata(
        artifact_id=f"DESC_{scene_id}_{shot_id}",
        artifact_type="descriptor_shot",
        status="generated",
        source_fingerprint=_fingerprint({"shot": shot, "scene": scene_contract, "evidence": evidence_summary, "kind": "shot"}),
        created_at_utc=_utc_now(),
        updated_at_utc=_utc_now(),
        upstream_dependencies=[
            {"dependency_type": "shot_package", "dependency_id": f"{scene_id}/{shot_id}", "version": _fingerprint(shot)},
            {"dependency_type": "scene_contract", "dependency_id": scene_id, "version": _fingerprint(scene_contract)},
        ],
    )
    return _finalize_descriptor(
        descriptor_id=metadata.artifact_id,
        canonical_id=f"{scene_id}_{shot_id}",
        display_name=_first_nonempty(shot.get("shot_title"), fallback=shot_id),
        entity_type=SHOT_ENTITY_TYPE,
        status="canonical",
        field_values=base_fields,
        field_origin=field_origin,
        field_sources=field_sources,
        chapter_mentions=[scene_id[:5]] if scene_id else [],
        scene_mentions=[scene_id] if scene_id else [],
        shot_mentions=[f"{scene_id}/{shot_id}"] if scene_id and shot_id else [],
        evidence_refs=evidence_refs,
        evidence_summary=evidence_summary,
        inferred_fields=inferred_fields,
        review_flags=review_flags,
        related_assets=[],
        metadata=metadata,
    )


def _extract_key_item_mentions(text: str) -> list[tuple[str, str]]:
    mentions: list[tuple[str, str]] = []
    for pattern, kind in KEY_ITEM_PATTERNS:
        for match in re.finditer(pattern, text, re.IGNORECASE):
            raw = match.group(0).strip()
            if raw:
                mentions.append((raw, kind))
    return mentions


def _base_key_item_descriptor(
    item_id: str,
    candidate: dict[str, Any],
    use_llm: bool,
) -> DescriptorRecord:
    evidence_summary = _coerce_string_list(candidate.get("evidence_summary", []))
    evidence_refs = [ref for ref in candidate.get("evidence_refs", []) if isinstance(ref, dict)]
    base_fields: dict[str, Any] = {}
    field_origin: dict[str, str] = {}
    field_sources: dict[str, list[dict[str, Any]]] = {}
    inferred_fields: list[str] = []
    review_flags: list[str] = []

    def set_field(key: str, value: Any, *, origin: str) -> None:
        _add_field(base_fields, {}, {}, field_origin, field_sources, inferred_fields, key, value, origin=origin)

    set_field("item_kind", candidate.get("item_kind") or "artifact", origin="heuristic")
    set_field("shape", "unknown", origin="fallback")
    set_field("scale", "unknown", origin="fallback")
    set_field("materials", "unknown", origin="fallback")
    set_field("color_palette", "unknown", origin="fallback")
    set_field("ornamentation", "unknown", origin="fallback")
    set_field("condition_or_wear", "unknown", origin="fallback")
    set_field("holder_or_user_notes", "unknown", origin="fallback")
    set_field("iconic_features", _coerce_string_list(candidate.get("evidence_summary", []))[:3], origin="heuristic")
    set_field("symbolic_role", "unknown", origin="fallback")
    set_field("chapter_mentions", _coerce_string_list(candidate.get("chapter_mentions", [])), origin="heuristic")

    if use_llm:
        llm_payload = _llm_refine_descriptor(
            entity_type=KEY_ITEM_ENTITY_TYPE,
            descriptor_id=f"DESC_ITEM_{item_id}",
            canonical_id=item_id,
            display_name=candidate.get("display_name") or item_id,
            status=candidate.get("status", "canonical"),
            base_fields=base_fields,
            evidence_summary=evidence_summary,
            desired_fields=KEY_ITEM_FIELD_ORDER,
        )
        if llm_payload:
            for field_name, value in (llm_payload.get("supported_field_values") or {}).items():
                if value:
                    base_fields[field_name] = value
                    field_origin[field_name] = "llm_supported"
            for field_name, value in (llm_payload.get("generated_field_values") or {}).items():
                if value:
                    base_fields[field_name] = value
                    field_origin[field_name] = "llm_generated"
                    if field_name not in inferred_fields:
                        inferred_fields.append(field_name)
            if llm_payload.get("chapter_mentions"):
                base_fields["chapter_mentions"] = llm_payload["chapter_mentions"]
            review_flags.extend(llm_payload.get("review_flags", []))
            evidence_summary = _coerce_string_list(llm_payload.get("evidence_summary", []), evidence_summary)

    metadata = DescriptorMetadata(
        artifact_id=f"DESC_ITEM_{item_id}",
        artifact_type="descriptor_key_item",
        status="generated",
        source_fingerprint=_fingerprint({"candidate": candidate, "evidence": evidence_summary, "kind": "key_item"}),
        created_at_utc=_utc_now(),
        updated_at_utc=_utc_now(),
        upstream_dependencies=[{"dependency_type": "candidate_mentions", "dependency_id": item_id, "version": _fingerprint(candidate)}],
    )
    if len(candidate.get("evidence_refs", [])) < 2:
        review_flags.append("thin_key_item_coverage")
    return _finalize_descriptor(
        descriptor_id=metadata.artifact_id,
        canonical_id=item_id,
        display_name=_first_nonempty(candidate.get("display_name"), fallback=item_id),
        entity_type=KEY_ITEM_ENTITY_TYPE,
        status=candidate.get("status", "canonical"),
        field_values=base_fields,
        field_origin=field_origin,
        field_sources=field_sources,
        chapter_mentions=_coerce_string_list(candidate.get("chapter_mentions", [])),
        scene_mentions=_coerce_string_list(candidate.get("scene_mentions", [])),
        shot_mentions=_coerce_string_list(candidate.get("shot_mentions", [])),
        evidence_refs=evidence_refs,
        evidence_summary=evidence_summary[:25],
        inferred_fields=inferred_fields,
        review_flags=review_flags,
        related_assets=[],
        metadata=metadata,
    )


def _descriptor_output_path(project_dir: Path, record: DescriptorRecord) -> Path:
    root = _descriptor_root(project_dir)
    if record.entity_type == CHARACTER_ENTITY_TYPE:
        return root / "characters" / f"{record.canonical_id}.json"
    if record.entity_type == ENVIRONMENT_ENTITY_TYPE:
        return root / "environments" / f"{record.canonical_id}.json"
    if record.entity_type == SCENE_ENTITY_TYPE:
        return root / "scenes" / f"{record.canonical_id}.json"
    if record.entity_type == SHOT_ENTITY_TYPE:
        parts = record.canonical_id.split("_")
        if len(parts) >= 3:
            scene_id = "_".join(parts[:2])
            shot_id = parts[2]
            return root / "shots" / scene_id[:5] / scene_id / f"{shot_id}.json"
        return root / "shots" / f"{record.canonical_id}.json"
    if record.entity_type == KEY_ITEM_ENTITY_TYPE:
        return root / "key_items" / f"{record.canonical_id}.json"
    return root / "misc" / f"{record.canonical_id}.json"


def _descriptor_base_path(project_dir: Path, record: DescriptorRecord) -> Path:
    return _descriptor_output_path(project_dir, record).with_suffix("")


def _descriptor_from_existing(existing: dict[str, Any], metadata: DescriptorMetadata) -> DescriptorRecord:
    return DescriptorRecord(
        descriptor_id=str(existing.get("descriptor_id", metadata.artifact_id)),
        canonical_id=str(existing.get("canonical_id", "")),
        display_name=str(existing.get("display_name", "")),
        entity_type=str(existing.get("entity_type", "")),
        status=str(existing.get("status", "canonical")),
        field_values=existing.get("field_values", {}),
        supported_field_values=existing.get("supported_field_values", {}),
        generated_field_values=existing.get("generated_field_values", {}),
        field_states=existing.get("field_states", {}),
        supported_field_states=existing.get("supported_field_states", {}),
        generated_field_states=existing.get("generated_field_states", {}),
        field_sources=existing.get("field_sources", {}),
        supported_field_sources=existing.get("supported_field_sources", {}),
        generated_field_sources=existing.get("generated_field_sources", {}),
        field_confidence=existing.get("field_confidence", {}),
        supported_field_confidence=existing.get("supported_field_confidence", {}),
        generated_field_confidence=existing.get("generated_field_confidence", {}),
        field_origin=existing.get("field_origin", {}),
        supported_field_origin=existing.get("supported_field_origin", {}),
        generated_field_origin=existing.get("generated_field_origin", {}),
        chapter_mentions=existing.get("chapter_mentions", []),
        scene_mentions=existing.get("scene_mentions", []),
        shot_mentions=existing.get("shot_mentions", []),
        evidence_refs=existing.get("evidence_refs", []),
        evidence_summary=existing.get("evidence_summary", []),
        inferred_fields=existing.get("inferred_fields", []),
        review_flags=existing.get("review_flags", []),
        related_assets=existing.get("related_assets", []),
        metadata=metadata,
    )


def _descriptor_review_issues(record: DescriptorRecord) -> list[str]:
    issues: list[str] = []
    if record.status != "canonical":
        issues.append(f"status={record.status}")
    if not record.chapter_mentions:
        issues.append("missing chapter coverage")
    if not record.evidence_summary:
        issues.append("missing evidence summary")
    if record.review_flags:
        issues.extend(record.review_flags)
    return issues


def _write_root_indexes(output_root: Path, records: list[DescriptorRecord], review_records: list[DescriptorRecord]) -> None:
    _write_index(output_root / "DESCRIPTOR_INDEX.md", records, title="Descriptor Index")
    write_json(output_root / "DESCRIPTOR_INDEX.json", [record.to_dict() for record in sorted(records, key=lambda item: (item.entity_type, item.canonical_id))])
    _write_index(output_root / "DESCRIPTOR_REVIEW_INDEX.md", review_records, title="Descriptor Review Index")
    write_json(output_root / "DESCRIPTOR_REVIEW_INDEX.json", [record.to_dict() for record in sorted(review_records, key=lambda item: (item.entity_type, item.canonical_id))])


def run_descriptor_enrichment(
    project_slug: str,
    *,
    use_llm: bool = True,
    force: bool = False,
    limit: int | None = None,
    entity_types: list[str] | None = None,
    entity_ids: list[str] | None = None,
) -> DescriptorEnrichmentSummary:
    project_dir = create_project(project_slug)
    output_root = _descriptor_root(project_dir)
    review_dir = output_root / "review"
    output_root.mkdir(parents=True, exist_ok=True)
    review_dir.mkdir(parents=True, exist_ok=True)
    (output_root / "characters").mkdir(parents=True, exist_ok=True)
    (output_root / "environments").mkdir(parents=True, exist_ok=True)
    (output_root / "scenes").mkdir(parents=True, exist_ok=True)
    (output_root / "shots").mkdir(parents=True, exist_ok=True)
    (output_root / "key_items").mkdir(parents=True, exist_ok=True)

    character_bibles = _load_character_bibles(project_dir)
    environment_bibles = _load_environment_bibles(project_dir)
    scene_contracts = _load_scene_contracts(project_dir)
    shot_packages = _load_shot_packages(project_dir)
    character_scene_map, character_shot_map, environment_scene_map, environment_shot_map = _build_reference_maps(scene_contracts, shot_packages)
    key_item_candidates = _collect_key_item_candidates(scene_contracts, shot_packages)

    records: list[DescriptorRecord] = []
    review_records: list[DescriptorRecord] = []
    review_queue: list[dict[str, Any]] = []
    written_files: list[str] = []
    warnings: list[str] = []
    synthesized = 0
    reused = 0
    processed = 0
    stop_processing = False
    selected_types = set(entity_types or [])
    selected_ids = {str(item).strip().lower() for item in (entity_ids or []) if str(item).strip()}

    def matches_entity_id(*candidates: str) -> bool:
        if not selected_ids:
            return True
        normalized = {str(candidate).strip().lower() for candidate in candidates if str(candidate).strip()}
        return bool(normalized & selected_ids)

    def maybe_reuse(base_path: Path, fp: str, builder: Callable[[], DescriptorRecord], *, force: bool) -> DescriptorRecord:
        nonlocal reused, synthesized
        existing = read_json(base_path.with_suffix(".json")) if base_path.with_suffix(".json").exists() else None
        metadata = _load_existing_metadata(existing, artifact_id=base_path.name, fp=fp)
        if existing and not force:
            old_meta = existing.get("metadata") or {}
            if old_meta.get("source_fingerprint") == fp:
                reused += 1
                return _descriptor_from_existing(existing, metadata)
            if old_meta.get("status") == "locked":
                existing["metadata"]["status"] = "stale"
                write_json(base_path.with_suffix(".json"), existing)
                warnings.append(f"Locked descriptor became stale and was not regenerated: {base_path.name}")
                return _descriptor_from_existing(existing, metadata)
        record = builder()
        base_path.parent.mkdir(parents=True, exist_ok=True)
        _write_descriptor_files(base_path, record)
        synthesized += 1
        written_files.extend([str(base_path.with_suffix(".json")), str(base_path.with_suffix(".md"))])
        return record

    if not selected_types or CHARACTER_ENTITY_TYPE in selected_types:
        for char_id, bible in character_bibles.items():
            if stop_processing:
                break
            if not matches_entity_id(char_id, f"char_{char_id}", f"desc_char_{char_id}"):
                continue
            source_entry = character_bibles.get(char_id, bible)
            fp = _fingerprint({"bible": bible, "scene_mentions": character_scene_map.get(char_id, []), "shot_mentions": character_shot_map.get(char_id, []), "kind": "character"})
            base_path = output_root / "characters" / char_id

            def build_character() -> DescriptorRecord:
                return _base_character_descriptor(
                    project_slug=project_slug,
                    project_dir=project_dir,
                    char_id=char_id,
                    entry=source_entry,
                    bible=bible,
                    scene_mentions=character_scene_map.get(char_id, []),
                    shot_mentions=character_shot_map.get(char_id, []),
                    use_llm=use_llm,
                )

            record = maybe_reuse(base_path, fp, build_character, force=force)
            records.append(record)
            processed += 1
            if limit is not None and processed >= limit:
                stop_processing = True
            if record.status != "canonical" or record.review_flags:
                review_records.append(record)
                review_queue.append({"descriptor_id": record.descriptor_id, "entity_type": record.entity_type, "issues": _descriptor_review_issues(record)})

    if not selected_types or ENVIRONMENT_ENTITY_TYPE in selected_types:
        for env_id, bible in environment_bibles.items():
            if stop_processing:
                break
            if not matches_entity_id(env_id, f"env_{env_id}", f"desc_env_{env_id}"):
                continue
            source_entry = environment_bibles.get(env_id, bible)
            fp = _fingerprint({"bible": bible, "scene_mentions": environment_scene_map.get(env_id, []), "shot_mentions": environment_shot_map.get(env_id, []), "kind": "environment"})
            base_path = output_root / "environments" / env_id

            def build_environment() -> DescriptorRecord:
                return _base_environment_descriptor(
                    project_slug=project_slug,
                    project_dir=project_dir,
                    env_id=env_id,
                    entry=source_entry,
                    bible=bible,
                    scene_mentions=environment_scene_map.get(env_id, []),
                    shot_mentions=environment_shot_map.get(env_id, []),
                    use_llm=use_llm,
                )

            record = maybe_reuse(base_path, fp, build_environment, force=force)
            records.append(record)
            processed += 1
            if limit is not None and processed >= limit:
                stop_processing = True
            if record.status != "canonical" or record.review_flags:
                review_records.append(record)
                review_queue.append({"descriptor_id": record.descriptor_id, "entity_type": record.entity_type, "issues": _descriptor_review_issues(record)})

    if not selected_types or SCENE_ENTITY_TYPE in selected_types:
        for scene_id, contract in scene_contracts.items():
            if stop_processing:
                break
            if not matches_entity_id(scene_id, scene_id.lower(), f"desc_{scene_id.lower()}"):
                continue
            fp = _fingerprint({"scene": contract, "kind": "scene"})
            base_path = output_root / "scenes" / scene_id
            shot_mentions = [f"{str(shot.get('scene_id', '')).strip().upper()}/{str(shot.get('shot_id', '')).strip().upper()}" for shot in shot_packages if str(shot.get("scene_id", "")).strip().upper() == scene_id and str(shot.get("shot_id", "")).strip()]

            def build_scene() -> DescriptorRecord:
                return _base_scene_descriptor(scene_id=scene_id, scene_contract=contract, shot_mentions=shot_mentions, use_llm=use_llm)

            record = maybe_reuse(base_path, fp, build_scene, force=force)
            records.append(record)
            processed += 1
            if limit is not None and processed >= limit:
                stop_processing = True
            if record.review_flags:
                review_records.append(record)
                review_queue.append({"descriptor_id": record.descriptor_id, "entity_type": record.entity_type, "issues": _descriptor_review_issues(record)})

    if not selected_types or SHOT_ENTITY_TYPE in selected_types:
        for shot in shot_packages:
            if stop_processing:
                break
            scene_id = str(shot.get("scene_id", "")).strip().upper()
            shot_id = str(shot.get("shot_id", "")).strip().upper()
            if not scene_id or not shot_id:
                continue
            if not matches_entity_id(shot_id, f"{scene_id}/{shot_id}", f"{scene_id}_{shot_id}", f"desc_{scene_id}_{shot_id}"):
                continue
            scene_contract = scene_contracts.get(scene_id, {})
            fp = _fingerprint({"shot": shot, "scene": scene_contract, "kind": "shot"})
            chapter_id = scene_id[:5]
            base_path = output_root / "shots" / chapter_id / scene_id / shot_id

            def build_shot() -> DescriptorRecord:
                return _base_shot_descriptor(shot=shot, scene_contract=scene_contract, use_llm=use_llm)

            record = maybe_reuse(base_path, fp, build_shot, force=force)
            records.append(record)
            processed += 1
            if limit is not None and processed >= limit:
                stop_processing = True
            if record.review_flags:
                review_records.append(record)
                review_queue.append({"descriptor_id": record.descriptor_id, "entity_type": record.entity_type, "issues": _descriptor_review_issues(record)})
            if stop_processing:
                break

    if not selected_types or KEY_ITEM_ENTITY_TYPE in selected_types:
        for item_id, candidate in key_item_candidates.items():
            if stop_processing:
                break
            if not matches_entity_id(item_id, f"item_{item_id}", f"desc_item_{item_id}"):
                continue
            fp = _fingerprint({"candidate": candidate, "kind": "key_item"})
            base_path = output_root / "key_items" / item_id

            def build_item() -> DescriptorRecord:
                return _base_key_item_descriptor(item_id=item_id, candidate=candidate, use_llm=use_llm)

            record = maybe_reuse(base_path, fp, build_item, force=force)
            records.append(record)
            processed += 1
            if limit is not None and processed >= limit:
                stop_processing = True
            if record.review_flags:
                review_records.append(record)
                review_queue.append({"descriptor_id": record.descriptor_id, "entity_type": record.entity_type, "issues": _descriptor_review_issues(record)})

    review_queue_path = review_dir / "DESCRIPTOR_REVIEW_QUEUE.md"
    review_queue_json = review_dir / "DESCRIPTOR_REVIEW_QUEUE.json"
    _write_review_queue(review_queue_path, review_queue, title="Descriptor Review Queue")
    write_json(review_queue_json, review_queue)
    _write_root_indexes(output_root, [record for record in records if record.status == "canonical" and not record.review_flags], review_records)

    written_files.extend(
        [
            str(review_queue_path),
            str(review_queue_json),
            str(output_root / "DESCRIPTOR_INDEX.md"),
            str(output_root / "DESCRIPTOR_INDEX.json"),
            str(output_root / "DESCRIPTOR_REVIEW_INDEX.md"),
            str(output_root / "DESCRIPTOR_REVIEW_INDEX.json"),
        ]
    )

    return DescriptorEnrichmentSummary(
        project_slug=project_slug,
        total_entries=len(records),
        synthesized_count=synthesized,
        reused_count=reused,
        review_queue_count=len(review_queue),
        written_files=written_files,
        warnings=warnings,
    )


@dataclass(frozen=True)
class DescriptorResetSummary:
    project_slug: str
    removed_paths: list[str]
    warnings: list[str]

    def to_dict(self) -> dict[str, Any]:
        return {
            "project_slug": self.project_slug,
            "removed_paths": self.removed_paths,
            "warnings": self.warnings,
        }


def clear_descriptor_artifacts(
    project_slug: str,
    *,
    include_prompt_packages: bool = True,
) -> DescriptorResetSummary:
    project_dir = create_project(project_slug)
    project_root = project_dir.resolve()
    removed_paths: list[str] = []
    warnings: list[str] = []

    targets = [
        project_dir / "02_story_analysis" / "descriptors",
    ]
    if include_prompt_packages:
        targets.append(project_dir / "03_prompt_packages" / "prepared")

    def on_rm_error(func: Callable[..., Any], path: str, exc_info: tuple[Any, Any, Any]) -> None:
        try:
            os.chmod(path, stat.S_IWRITE)
            func(path)
        except Exception as exc:
            warnings.append(f"Failed to remove {path}: {exc}")

    for target in targets:
        resolved = target.resolve()
        if project_root not in resolved.parents and resolved != project_root:
            warnings.append(f"Skipped unsafe target: {resolved}")
            continue
        if target.exists():
            shutil.rmtree(target, onerror=on_rm_error)
            if not target.exists():
                removed_paths.append(str(target))
            else:
                warnings.append(f"Target still exists after cleanup attempt: {target}")

    return DescriptorResetSummary(
        project_slug=project_slug,
        removed_paths=removed_paths,
        warnings=warnings,
    )
