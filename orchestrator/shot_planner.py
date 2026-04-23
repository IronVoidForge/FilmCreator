from __future__ import annotations

import hashlib
import json
import re
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .chapter_selection import chapter_matches, parse_chapter_selector
from .core.json_io import read_json, write_json
from .features.authoring.packet_parser import parse_packet_document
from .lmstudio_client import LMStudioClient
from .scaffold import create_project
from .settings import load_runtime_settings

SHOT_PLANNER_SCHEMA_VERSION = "2026-04-23-shot-planner-v5"

SHOT_SIZE_ENUM = {"extreme_wide", "wide", "full", "medium_full", "medium", "medium_close", "close_up", "extreme_close_up", "insert_detail"}
CAMERA_ANGLE_ENUM = {"eye_level", "low_angle", "high_angle", "overhead", "dutch"}
LENS_FAMILY_ENUM = {"ultra_wide", "wide", "normal", "portrait", "telephoto"}
CAMERA_MOTION_ENUM = {"locked_off", "pan", "tilt", "push_in", "pull_back", "track", "crane", "handheld"}
ZOOM_BEHAVIOR_ENUM = {"none", "subtle_in", "subtle_out", "strong_in", "strong_out"}
FOCUS_STRATEGY_ENUM = {"deep_focus", "shallow_subject", "rack_focus", "environment_priority"}
LIGHTING_STYLE_ENUM = {"soft_even", "hard_directional", "high_contrast_ceremonial", "diffuse_ambient", "backlit", "torch_firelight", "low_key_night"}
SUBJECT_VISIBILITY_ENUM = {"on_screen", "partial", "silhouette", "off_screen_voice", "implied_only"}
NARRATION_MODE_ENUM = {"none", "voiceover_off_screen", "in_scene_speaker", "internal_monologue"}
PRIMARY_SUBJECT_ANGLE_ENUM = {"front", "front_three_quarter_left", "front_three_quarter_right", "profile_left", "profile_right", "rear_three_quarter_left", "rear_three_quarter_right", "back"}

CLOSE_SHOT_SIZES = {"extreme_close_up", "close_up", "medium_close"}
WIDE_SHOT_SIZES = {"extreme_wide", "wide"}


@dataclass
class ShotReference:
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
class ShotPackageMetadata:
    artifact_id: str
    artifact_type: str = "shot_package"
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
class ShotPackage:
    shot_id: str
    scene_id: str
    chapter_id: str
    shot_order: int
    shot_title: str
    shot_type: str
    camera_description: str
    composition: str
    target_seconds: float = 5.0
    previous_shot_id: str = ""
    next_shot_id: str = ""
    primary_subject: str = ""
    secondary_subjects: list[str] = field(default_factory=list)
    shot_moment_summary: str = ""
    start_state: str = ""
    end_state: str = ""
    action_during_shot: str = ""
    action_continues_from: str = ""
    action_hands_off_to: str = ""
    shot_size: str = ""
    camera_angle: str = ""
    lens_family: str = ""
    camera_motion: str = ""
    zoom_behavior: str = ""
    focus_strategy: str = ""
    lighting_style: str = ""
    subject_visibility: str = ""
    narration_mode: str = ""
    primary_subject_angle: str = ""
    visible_primary_subject_id: str = ""
    visible_secondary_subject_ids: list[str] = field(default_factory=list)
    primary_subject_frame_position: str = ""
    primary_subject_scale_relation: str = ""
    primary_subject_facing_direction: str = ""
    primary_subject_pose_description: str = ""
    subject_relation_summary: str = ""
    required_environment_anchor_1: str = ""
    required_scale_proof_detail: str = ""
    camera_package_description: str = ""
    subject_blocking: list[str] = field(default_factory=list)
    camera_relative_positions: list[str] = field(default_factory=list)
    gaze_directions: list[str] = field(default_factory=list)
    environment_subzone: str = ""
    key_visible_environment_features: list[str] = field(default_factory=list)
    continuity_from_previous_shot: str = ""
    continuity_to_next_shot: str = ""
    pose_anchor_frame: str = ""
    pose_end_frame: str = ""
    characters_in_frame: list[ShotReference] = field(default_factory=list)
    environment: ShotReference | None = None
    beat_ids: list[str] = field(default_factory=list)
    continuity_constraints: list[str] = field(default_factory=list)
    prompt_seed: str = ""
    shot_notes: str = ""
    evidence_refs: list[dict[str, Any]] = field(default_factory=list)
    evidence_summary: list[str] = field(default_factory=list)
    metadata: ShotPackageMetadata | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "shot_id": self.shot_id,
            "scene_id": self.scene_id,
            "chapter_id": self.chapter_id,
            "shot_order": self.shot_order,
            "previous_shot_id": self.previous_shot_id,
            "next_shot_id": self.next_shot_id,
            "primary_subject": self.primary_subject,
            "secondary_subjects": self.secondary_subjects,
            "shot_moment_summary": self.shot_moment_summary,
            "start_state": self.start_state,
            "end_state": self.end_state,
            "action_during_shot": self.action_during_shot,
            "action_continues_from": self.action_continues_from,
            "action_hands_off_to": self.action_hands_off_to,
            "shot_size": self.shot_size,
            "camera_angle": self.camera_angle,
            "lens_family": self.lens_family,
            "camera_motion": self.camera_motion,
            "zoom_behavior": self.zoom_behavior,
            "focus_strategy": self.focus_strategy,
            "lighting_style": self.lighting_style,
            "subject_visibility": self.subject_visibility,
            "narration_mode": self.narration_mode,
            "primary_subject_angle": self.primary_subject_angle,
            "visible_primary_subject_id": self.visible_primary_subject_id,
            "visible_secondary_subject_ids": self.visible_secondary_subject_ids,
            "primary_subject_frame_position": self.primary_subject_frame_position,
            "primary_subject_scale_relation": self.primary_subject_scale_relation,
            "primary_subject_facing_direction": self.primary_subject_facing_direction,
            "primary_subject_pose_description": self.primary_subject_pose_description,
            "subject_relation_summary": self.subject_relation_summary,
            "required_environment_anchor_1": self.required_environment_anchor_1,
            "required_scale_proof_detail": self.required_scale_proof_detail,
            "camera_package_description": self.camera_package_description,
            "subject_blocking": self.subject_blocking,
            "camera_relative_positions": self.camera_relative_positions,
            "gaze_directions": self.gaze_directions,
            "environment_subzone": self.environment_subzone,
            "key_visible_environment_features": self.key_visible_environment_features,
            "continuity_from_previous_shot": self.continuity_from_previous_shot,
            "continuity_to_next_shot": self.continuity_to_next_shot,
            "pose_anchor_frame": self.pose_anchor_frame,
            "pose_end_frame": self.pose_end_frame,
            "shot_title": self.shot_title,
            "shot_type": self.shot_type,
            "camera_description": self.camera_description,
            "composition": self.composition,
            "target_seconds": self.target_seconds,
            "characters_in_frame": [item.to_dict() for item in self.characters_in_frame],
            "environment": self.environment.to_dict() if self.environment else None,
            "beat_ids": self.beat_ids,
            "continuity_constraints": self.continuity_constraints,
            "prompt_seed": self.prompt_seed,
            "shot_notes": self.shot_notes,
            "evidence_refs": self.evidence_refs,
            "evidence_summary": self.evidence_summary,
            "metadata": self.metadata.to_dict() if self.metadata else None,
        }


@dataclass(frozen=True)
class ShotPlanningSummary:
    project_slug: str
    total_scene_entries: int
    total_shot_entries: int
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
            "total_shot_entries": self.total_shot_entries,
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


def _coerce_float(*values: object, fallback: float = 0.0) -> float:
    for value in values:
        if value is None:
            continue
        try:
            if isinstance(value, str):
                stripped = value.strip()
                if not stripped:
                    continue
                return float(stripped)
            return float(value)
        except (TypeError, ValueError):
            continue
    return fallback


def _clean_label(value: object, *, fallback: str) -> str:
    if isinstance(value, str):
        cleaned = value.strip()
        if cleaned and cleaned.lower() not in {"none", "(none)", "n/a", "null", "[]", "[ ]", "{}", "{ }"}:
            return cleaned
    return fallback


def _is_placeholder_text(value: object) -> bool:
    if value is None:
        return True
    text = str(value).strip()
    if not text:
        return True
    normalized = text.lower()
    return normalized in {
        "none",
        "(none)",
        "n/a",
        "null",
        "[]",
        "[ ]",
        "{}",
        "{ }",
        "unknown",
        "(unknown)",
    }


def _normalize_match_key(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", value.strip().lower()).strip("_")


def _label_variants(value: str) -> list[str]:
    raw = str(value or "").strip()
    if not raw:
        return []
    variants: list[str] = []

    def add_variant(text: str) -> None:
        normalized = _normalize_match_key(text)
        if normalized and normalized not in variants:
            variants.append(normalized)

    cleaned = re.sub(r"\[\[|\]\]", "", raw)
    add_variant(cleaned)
    parenthetical = re.sub(r"\([^)]*\)", " ", cleaned)
    add_variant(parenthetical)
    article_stripped = re.sub(r"^(the|a|an)\s+", "", parenthetical.strip(), flags=re.IGNORECASE)
    add_variant(article_stripped)
    title_stripped = re.sub(
        r"^(captain|capt\.?|general|gen\.?|major|maj\.?|colonel|col\.?|lieutenant|lt\.?|sergeant|sgt\.?|doctor|dr\.?|mr\.?|mrs\.?|ms\.?|miss|the)\s+",
        "",
        article_stripped.strip(),
        flags=re.IGNORECASE,
    )
    add_variant(title_stripped)
    descriptor_stripped = re.sub(
        r"\b(younger|elderly|older|deceased|dead|corpse|body|wounded|injured|late)\b",
        " ",
        title_stripped,
        flags=re.IGNORECASE,
    )
    add_variant(descriptor_stripped)
    return variants


def _meaningful_tokens(value: str) -> set[str]:
    stopwords = {
        "the",
        "and",
        "for",
        "with",
        "from",
        "into",
        "near",
        "site",
        "scene",
        "area",
        "space",
        "place",
        "through",
        "under",
        "over",
        "within",
        "floor",
    }
    return {
        token
        for token in re.findall(r"[a-z0-9]+", str(value or "").lower())
        if len(token) > 2 and token not in stopwords and not token.isdigit()
    }


def _best_display_label(ref: "ShotReference") -> str:
    return _first_nonempty(ref.display_name, ref.label, fallback="")


def _looks_like_scale_relation(value: str) -> bool:
    text = " ".join(str(value or "").lower().split())
    if not text:
        return False
    scale_terms = {
        "scale",
        "size",
        "larger",
        "smaller",
        "towering",
        "huge",
        "enormous",
        "tiny",
        "width",
        "height",
        "distance",
        "crowd",
        "lone",
        "body",
        "furniture",
        "trail",
        "cliff",
        "dais",
        "platform",
        "versus",
        "against",
        "beside",
        "relative",
    }
    return any(term in text for term in scale_terms)


def _looks_like_environment_anchor(value: str) -> bool:
    text = " ".join(str(value or "").lower().split())
    if not text or _is_placeholder_text(text):
        return False
    if any(term in text for term in ["eye", "eyes", "face", "skin", "wrinkle", "wrinkles", "mouth", "breath", "blink", "blink", "expression"]):
        return False
    anchor_terms = {
        "trail",
        "valley",
        "plateau",
        "camp",
        "canyon",
        "gorge",
        "cave",
        "void",
        "sky",
        "star",
        "mountain",
        "landscape",
        "dais",
        "rostrum",
        "chair",
        "desk",
        "furniture",
        "gallery",
        "wall",
        "mural",
        "threshold",
        "door",
        "quartz",
        "vein",
        "bar",
    }
    return any(term in text for term in anchor_terms)


def _coerce_string_list(*values: object) -> list[str]:
    items: list[str] = []
    for value in values:
        if value is None:
            continue
        if isinstance(value, list):
            for item in value:
                if not isinstance(item, str):
                    continue
                stripped = item.strip()
                if _is_placeholder_text(stripped):
                    continue
                items.append(stripped)
        elif isinstance(value, str):
            stripped = value.strip()
            if _is_placeholder_text(stripped):
                continue
            parts = [part.strip() for part in re.split(r",|\n", stripped) if part.strip()]
            if parts:
                items.extend(part for part in parts if not _is_placeholder_text(part))
            else:
                items.append(stripped)

    seen: set[str] = set()
    deduped: list[str] = []
    for item in items:
        if item not in seen:
            seen.add(item)
            deduped.append(item)
    return deduped


def _estimate_shot_seconds(shot_type: str, shot_order: int, total_shots: int) -> float:
    shot_type_normalized = (shot_type or "").strip().lower()
    if shot_type_normalized in {"establishing", "wide", "opening"}:
        seconds = 6.0
    elif shot_type_normalized in {"closeup", "close-up", "reaction", "closing_reaction"}:
        seconds = 4.5
    elif shot_type_normalized in {"tracking", "moving", "action", "dynamic"}:
        seconds = 5.5
    elif shot_type_normalized in {"generic", "shot"}:
        seconds = 5.0
    else:
        seconds = 5.0

    if total_shots <= 3:
        seconds += 0.3
    elif total_shots >= 6:
        seconds -= 0.2

    if shot_order == 1:
        seconds += 0.2
    elif shot_order == total_shots:
        seconds -= 0.2

    return max(4.0, min(10.0, round(seconds, 1)))


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


def _normalize_asset_label(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", value.strip().lower()).strip("_")


def _scene_contract_root(project_dir: Path) -> Path:
    return project_dir / "02_story_analysis" / "contracts" / "scenes"


def _scene_binding_root(project_dir: Path) -> Path:
    return project_dir / "02_story_analysis" / "contracts" / "scene_bindings"


def _shot_package_root(project_dir: Path) -> Path:
    return project_dir / "02_story_analysis" / "contracts" / "shots"


def _scene_contract_files(project_dir: Path) -> list[Path]:
    root = _scene_contract_root(project_dir)
    if not root.exists():
        return []
    return sorted(path for path in root.glob("CH*/CH*_SC*.json") if path.is_file())


def _load_json_file(path: Path) -> dict[str, Any]:
    payload = read_json(path)
    return payload if isinstance(payload, dict) else {}


def _scene_binding_path(project_dir: Path, scene_id: str) -> Path:
    chapter_id = _chapter_id_from_scene_id(scene_id)
    return _scene_binding_root(project_dir) / chapter_id / f"{scene_id}_BINDINGS.json"


def _load_scene_binding(project_dir: Path, scene_id: str) -> dict[str, Any]:
    path = _scene_binding_path(project_dir, scene_id)
    return _load_json_file(path) if path.exists() else {}


def _load_character_bible(project_dir: Path, canonical_id: str) -> dict[str, Any] | None:
    path = project_dir / "02_story_analysis" / "bibles" / "characters" / f"CHAR_{canonical_id}.json"
    if not path.exists():
        return None
    return _load_json_file(path)


def _load_environment_bible(project_dir: Path, canonical_id: str) -> dict[str, Any] | None:
    path = project_dir / "02_story_analysis" / "bibles" / "environments" / f"ENV_{canonical_id}.json"
    if not path.exists():
        return None
    return _load_json_file(path)


def _normalize_optional_canonical_id(value: Any) -> str | None:
    text = str(value or "").strip()
    if not text or text.lower() in {"none", "null", "(none)"}:
        return None
    return text


def _chapter_id_from_scene_id(scene_id: str) -> str:
    return scene_id[:5]


def _scene_contract_to_scene_title(scene_contract: dict[str, Any]) -> str:
    return _first_nonempty(
        scene_contract.get("scene_title"),
        scene_contract.get("production_intent"),
        scene_contract.get("summary"),
        fallback=str(scene_contract.get("scene_id", "")),
    )


def _find_ref_by_label(refs: list[dict[str, Any]], text: str) -> dict[str, Any] | None:
    text_variants = _label_variants(text)
    if not text_variants:
        return None
    for ref in refs:
        candidates: set[str] = set()
        for field_name in ("label", "display_name", "canonical_id"):
            for variant in _label_variants(str(ref.get(field_name, ""))):
                candidates.add(variant)
        if any(variant in candidates for variant in text_variants):
            return ref
    return None


def _binding_ref_to_shot_reference(raw_ref: dict[str, Any], project_dir: Path, *, kind: str) -> ShotReference:
    canonical_id = _normalize_optional_canonical_id(raw_ref.get("canonical_id"))
    if kind == "character":
        bible = _load_character_bible(project_dir, canonical_id) if canonical_id else None
        fallback_entity_kind = "individual"
    else:
        bible = _load_environment_bible(project_dir, canonical_id) if canonical_id else None
        fallback_entity_kind = "environment"
    source_path = str(raw_ref.get("source_path", ""))
    if not canonical_id:
        source_path = ""
    return ShotReference(
        label=str(raw_ref.get("label", canonical_id or "")),
        canonical_id=canonical_id,
        display_name=_first_nonempty(str((bible or {}).get("display_name", "")), str(raw_ref.get("display_name", "")), fallback=str(raw_ref.get("label", canonical_id or ""))),
        status=str(raw_ref.get("status", (bible or {}).get("status", "review"))),
        entity_kind=str(raw_ref.get("entity_kind", (bible or {}).get("entity_kind", fallback_entity_kind))),
        resolution_score=int(raw_ref.get("resolution_score")) if str(raw_ref.get("resolution_score", "")).isdigit() else raw_ref.get("resolution_score"),
        source_path=source_path,
        notes=str(raw_ref.get("notes", "")),
    )


def _environment_override_for_beat(scene_binding: dict[str, Any], beat_id: str) -> dict[str, Any] | None:
    overrides = scene_binding.get("beat_environment_overrides", [])
    if not isinstance(overrides, list) or not beat_id:
        return None
    for item in overrides:
        if not isinstance(item, dict):
            continue
        if str(item.get("beat_id", "")).strip().upper() == beat_id.upper() and isinstance(item.get("environment"), dict):
            return item.get("environment")
    return None


def _load_local_environment_entries(project_dir: Path, chapter_id: str) -> dict[str, dict[str, Any]]:
    path = project_dir / "02_story_analysis" / "world" / "local" / f"{chapter_id.upper()}_ENVIRONMENT_REGISTRY.json"
    if not path.exists():
        return {}
    payload = read_json(path)
    if not isinstance(payload, dict):
        return {}
    return {canonical_id: entry for canonical_id, entry in payload.items() if isinstance(canonical_id, str) and isinstance(entry, dict)}


def _local_environment_from_hint(
    scene_contract: dict[str, Any],
    project_dir: Path,
    *,
    beat_id: str,
    subzone_hint: str,
) -> ShotReference | None:
    chapter_id = str(scene_contract.get("chapter_id", "")).strip().upper()
    if not chapter_id:
        return None

    hints: list[str] = [subzone_hint]
    for item in scene_contract.get("beat_list", []):
        if not isinstance(item, dict):
            continue
        if str(item.get("beat_id", "")).strip().upper() != beat_id.upper():
            continue
        hints.extend(
            [
                str(item.get("environment_subzone", "")),
                str(item.get("spatial_context", "")),
                str(item.get("summary", "")),
            ]
        )
        break
    hint_text = " ".join(text for text in hints if str(text).strip())
    hint_tokens = _meaningful_tokens(hint_text)
    if not hint_tokens:
        return None

    best_ref: ShotReference | None = None
    best_score = 0
    for canonical_id, entry in _load_local_environment_entries(project_dir, chapter_id).items():
        entry_tokens = _meaningful_tokens(canonical_id.replace("_", " "))
        entry_tokens |= _meaningful_tokens(str(entry.get("display_name", "")))
        for alias in entry.get("aliases", []):
            if isinstance(alias, str):
                entry_tokens |= _meaningful_tokens(alias)
        for source_path in entry.get("sources", []):
            if isinstance(source_path, str):
                entry_tokens |= _meaningful_tokens(Path(source_path).stem.replace("_", " "))
        overlap = len(hint_tokens & entry_tokens)
        score = overlap * 12
        normalized_hint = _normalize_match_key(hint_text)
        canonical_key = _normalize_match_key(canonical_id)
        if canonical_key and canonical_key in normalized_hint:
            score += 20
        if {"plateau", "camp"} <= hint_tokens and {"plateau", "camp"} <= entry_tokens:
            score += 20
        if {"valley", "floor"} <= hint_tokens and {"gold", "vein"} & entry_tokens:
            score += 8
        if {"void", "space"} & hint_tokens and {"void", "space"} & entry_tokens:
            score += 20
        if score > best_score:
            best_score = score
            best_ref = _binding_ref_to_shot_reference(
                {
                    "label": str(entry.get("display_name", canonical_id)),
                    "canonical_id": canonical_id,
                    "display_name": str(entry.get("display_name", canonical_id)),
                    "status": str(entry.get("status", "canonical")),
                    "entity_kind": str(entry.get("entity_kind", "environment")),
                    "source_path": (entry.get("sources", []) or [""])[0],
                    "notes": f"Chapter-local beat subzone match for '{subzone_hint or beat_id}'.",
                },
                project_dir,
                kind="environment",
            )
    return best_ref if best_ref and best_score >= 20 else None


def _select_scene_contract_environment_for_beat(
    scene_contract: dict[str, Any],
    project_dir: Path,
    beat_id: str,
) -> ShotReference | None:
    environment_refs = scene_contract.get("environments_required", [])
    if not isinstance(environment_refs, list):
        return None
    canonical_refs: list[ShotReference] = []
    for raw_ref in environment_refs:
        if not isinstance(raw_ref, dict):
            continue
        canonical_id = _normalize_optional_canonical_id(raw_ref.get("canonical_id"))
        status = str(raw_ref.get("status", "review"))
        if canonical_id and status == "canonical":
            canonical_refs.append(_binding_ref_to_shot_reference(raw_ref, project_dir, kind="environment"))
    if len(canonical_refs) < 2 or not beat_id:
        return None

    beat_payload: dict[str, Any] | None = None
    for item in scene_contract.get("beat_list", []):
        if not isinstance(item, dict):
            continue
        if str(item.get("beat_id", "")).strip().upper() == beat_id.upper():
            beat_payload = item
            break
    if beat_payload is None:
        return None

    beat_text = " ".join(
        str(item)
        for item in [
            beat_payload.get("summary", ""),
            beat_payload.get("spatial_context", ""),
            beat_payload.get("environment_subzone", ""),
            beat_payload.get("blocking_hint", ""),
            beat_payload.get("coverage_hint", ""),
        ]
        if str(item).strip()
    )
    beat_tokens = _meaningful_tokens(beat_text)
    if not beat_tokens:
        return None

    best_ref: ShotReference | None = None
    best_score = 0
    for ref in canonical_refs:
        ref_tokens = _meaningful_tokens(ref.label) | _meaningful_tokens(ref.display_name) | _meaningful_tokens(ref.canonical_id or "")
        source_name = Path(ref.source_path).stem.replace("_", " ")
        ref_tokens |= _meaningful_tokens(source_name)
        overlap = len(beat_tokens & ref_tokens)
        score = overlap * 12
        beat_key = _normalize_match_key(beat_text)
        if ref.canonical_id and _normalize_match_key(ref.canonical_id) in beat_key:
            score += 20
        if ref.display_name and _normalize_match_key(ref.display_name) in beat_key:
            score += 16
        if score > best_score:
            best_score = score
            best_ref = ref
    return best_ref if best_ref and best_score >= 18 else None


def _select_environment_ref(
    scene_contract: dict[str, Any],
    project_dir: Path,
    scene_binding: dict[str, Any] | None = None,
    beat_id: str = "",
    subzone_hint: str = "",
) -> ShotReference:
    if isinstance(scene_binding, dict) and scene_binding:
        override = _environment_override_for_beat(scene_binding, beat_id)
        if isinstance(override, dict):
            return _binding_ref_to_shot_reference(override, project_dir, kind="environment")
        local_override = _local_environment_from_hint(scene_contract, project_dir, beat_id=beat_id, subzone_hint=subzone_hint)
        if local_override is not None:
            return local_override
        resolved_environment = scene_binding.get("resolved_environment")
        if isinstance(resolved_environment, dict):
            return _binding_ref_to_shot_reference(resolved_environment, project_dir, kind="environment")

    local_override = _local_environment_from_hint(scene_contract, project_dir, beat_id=beat_id, subzone_hint=subzone_hint)
    if local_override is not None:
        return local_override

    contract_override = _select_scene_contract_environment_for_beat(scene_contract, project_dir, beat_id)
    if contract_override is not None:
        return contract_override

    environment_refs = scene_contract.get("environments_required", [])
    if not isinstance(environment_refs, list) or not environment_refs:
        return ShotReference(
            label="scene_environment",
            display_name=_scene_contract_to_scene_title(scene_contract),
            status="review",
            entity_kind="environment",
            notes="Scene contract did not provide an environment reference.",
        )

    for raw_ref in environment_refs:
        if not isinstance(raw_ref, dict):
            continue
        canonical_id = _normalize_optional_canonical_id(raw_ref.get("canonical_id")) or ""
        bible = _load_environment_bible(project_dir, canonical_id) if canonical_id else None
        status = str(raw_ref.get("status") or (bible or {}).get("status", "review"))
        entity_kind = str(raw_ref.get("entity_kind") or (bible or {}).get("entity_kind", "environment"))
        if canonical_id and status == "canonical":
            return ShotReference(
                label=str(raw_ref.get("label", canonical_id)),
                canonical_id=canonical_id,
                display_name=_first_nonempty(str((bible or {}).get("display_name", "")), str(raw_ref.get("display_name", "")), fallback=canonical_id),
                status=status,
                entity_kind=entity_kind,
                source_path=str(raw_ref.get("source_path", "")),
                notes=str(raw_ref.get("notes", "")),
            )

    raw_ref = environment_refs[0]
    if isinstance(raw_ref, dict):
        canonical_id = _normalize_optional_canonical_id(raw_ref.get("canonical_id"))
        bible = _load_environment_bible(project_dir, canonical_id) if canonical_id else None
        source_path = str(raw_ref.get("source_path", ""))
        if canonical_id is None:
            source_path = ""
        return ShotReference(
            label=str(raw_ref.get("label", "environment")),
            canonical_id=canonical_id,
            display_name=_first_nonempty(str((bible or {}).get("display_name", "")), str(raw_ref.get("display_name", "")), fallback=str(raw_ref.get("label", "environment"))),
            status=str(raw_ref.get("status", (bible or {}).get("status", "review"))),
            entity_kind=str(raw_ref.get("entity_kind", (bible or {}).get("entity_kind", "environment"))),
            source_path=source_path,
            notes=str(raw_ref.get("notes", "")),
        )

    return ShotReference(label="environment", display_name="environment", status="review", entity_kind="environment")


def _build_character_reference(project_dir: Path, raw_ref: dict[str, Any]) -> ShotReference:
    canonical_id = _normalize_optional_canonical_id(raw_ref.get("canonical_id"))
    bible = _load_character_bible(project_dir, canonical_id) if canonical_id else None
    display_name = _first_nonempty(
        str((bible or {}).get("display_name", "")),
        "" if _is_placeholder_text(raw_ref.get("display_name")) else str(raw_ref.get("display_name", "")),
        fallback="" if _is_placeholder_text(raw_ref.get("label")) else str(raw_ref.get("label", canonical_id or "")),
    )
    return ShotReference(
        label="" if _is_placeholder_text(raw_ref.get("label")) else str(raw_ref.get("label", display_name)),
        canonical_id=canonical_id,
        display_name=display_name,
        status=str(raw_ref.get("status", (bible or {}).get("status", "review"))),
        entity_kind=str(raw_ref.get("entity_kind", (bible or {}).get("entity_kind", "individual"))),
        resolution_score=int(raw_ref.get("resolution_score")) if str(raw_ref.get("resolution_score", "")).isdigit() else raw_ref.get("resolution_score"),
        source_path="" if not canonical_id else str(raw_ref.get("source_path", "")),
        notes=str(raw_ref.get("notes", "")),
    )


def _selected_characters(
    scene_contract: dict[str, Any],
    project_dir: Path,
    beat_summary: str,
    shot_order: int,
    scene_binding: dict[str, Any] | None = None,
    subject_hints: list[str] | None = None,
) -> list[ShotReference]:
    raw_refs = scene_contract.get("characters_required", [])
    if isinstance(scene_binding, dict) and isinstance(scene_binding.get("resolved_characters"), list) and scene_binding.get("resolved_characters"):
        raw_refs = scene_binding.get("resolved_characters", [])
    if not isinstance(raw_refs, list):
        raw_refs = []
    references = [_build_character_reference(project_dir, raw_ref) for raw_ref in raw_refs if isinstance(raw_ref, dict)]

    if not references:
        return [
            ShotReference(
                label="scene_character",
                display_name="scene_character",
                status="review",
                entity_kind="individual",
                notes="Scene contract did not provide a character reference.",
            )
        ]

    matched: list[ShotReference] = []
    for token in subject_hints or []:
        ref = _find_ref_by_label([ref.to_dict() for ref in references], token)
        if ref is not None:
            matched.append(_build_character_reference(project_dir, ref))
    for token in re.split(r"[,;/]", beat_summary):
        ref = _find_ref_by_label([ref.to_dict() for ref in references], token)
        if ref is not None:
            matched.append(_build_character_reference(project_dir, ref))

    if matched:
        return _dedupe_shot_references(matched[:3])

    canonical = [ref for ref in references if ref.status == "canonical" and ref.canonical_id]
    if shot_order == 1:
        return _dedupe_shot_references(canonical[:3] or references[:2])

    if shot_order == len(scene_contract.get("beat_list", []) or []):
        return _dedupe_shot_references(canonical[:2] or references[:2])

    if len(canonical) >= 2:
        return _dedupe_shot_references(canonical[:2])
    return _dedupe_shot_references(references[:2])


def _dedupe_shot_references(refs: list[ShotReference]) -> list[ShotReference]:
    deduped: list[ShotReference] = []
    seen: set[tuple[str, str, str]] = set()
    for ref in refs:
        key = (
            ref.canonical_id or "",
            ref.display_name.lower(),
            ref.label.lower(),
        )
        if key in seen:
            continue
        seen.add(key)
        deduped.append(ref)
    return deduped


def _subject_variants(value: str) -> set[str]:
    return set(_label_variants(value))


def _is_collective_reference(ref: ShotReference) -> bool:
    label_text = " ".join([ref.label, ref.display_name, ref.canonical_id or ""]).lower()
    if ref.entity_kind.strip().lower() in {"collective", "group"}:
        return True
    return any(term in label_text for term in ["warriors", "guards", "soldiers", "court", "crowd", "mob", "people"])


def _visible_secondary_subject_labels(primary_subject: str, characters: list[ShotReference]) -> list[str]:
    primary_variants = _subject_variants(primary_subject)
    labels: list[str] = []
    for ref in characters:
        ref_variants = _subject_variants(ref.canonical_id or "") | _subject_variants(ref.label) | _subject_variants(ref.display_name)
        if primary_variants and primary_variants & ref_variants:
            continue
        label = _best_display_label(ref) or ref.canonical_id or ref.label
        if label:
            labels.append(label)
    return _ordered_unique(labels)[:3]


def _filter_visible_characters(
    *,
    characters: list[ShotReference],
    primary_subject: str,
    secondary_subjects: list[str],
    beat_payload: dict[str, Any],
    shot_size: str,
    shot_type: str,
    subject_visibility: str,
) -> list[ShotReference]:
    if not characters:
        return characters

    intimate_frame = shot_size in CLOSE_SHOT_SIZES or shot_type in {"reaction_closeup", "closing_reaction", "insert_detail"}
    primary_variants = _subject_variants(primary_subject)
    secondary_variants: set[str] = set()
    for item in secondary_subjects:
        secondary_variants.update(_subject_variants(item))

    primary_ref: ShotReference | None = None
    others: list[ShotReference] = []
    for ref in characters:
        ref_variants = _subject_variants(ref.canonical_id or "") | _subject_variants(ref.label) | _subject_variants(ref.display_name)
        if primary_ref is None and primary_variants and primary_variants & ref_variants:
            primary_ref = ref
            continue
        others.append(ref)
    if primary_ref is None:
        primary_ref = characters[0]
        others = characters[1:]

    if subject_visibility == "off_screen_voice":
        return [primary_ref]

    beat_text = " ".join(
        str(item)
        for item in [
            beat_payload.get("summary", ""),
            beat_payload.get("action_start", ""),
            beat_payload.get("action_end", ""),
            beat_payload.get("blocking_hint", ""),
        ]
        if str(item).strip()
    ).lower()
    body_reveal = any(term in beat_text for term in ["body", "corpse", "deceased", "dead", "grief", "horror", "discover", "discovery"])
    max_visible = 1 if shot_size == "insert_detail" else 2 if intimate_frame else 3

    kept: list[ShotReference] = [primary_ref]
    for ref in others:
        if len(kept) >= max_visible:
            break
        ref_variants = _subject_variants(ref.canonical_id or "") | _subject_variants(ref.label) | _subject_variants(ref.display_name)
        matches_secondary = bool(secondary_variants & ref_variants) if secondary_variants else False
        is_collective = _is_collective_reference(ref)

        if intimate_frame:
            if body_reveal and is_collective:
                continue
            if is_collective and not matches_secondary:
                continue
            if not matches_secondary and len(kept) >= 2:
                continue
        kept.append(ref)

    return _dedupe_shot_references(kept)


def _shot_type_from_beat(scene_contract: dict[str, Any], beat_payload: dict[str, Any], shot_order: int) -> str:
    text = " ".join(
        str(item)
        for item in [
            beat_payload.get("summary", ""),
            beat_payload.get("action_start", ""),
            beat_payload.get("action_end", ""),
            beat_payload.get("coverage_hint", ""),
            beat_payload.get("coverage_priority", ""),
            beat_payload.get("blocking_hint", ""),
        ]
        if str(item).strip()
    ).lower()
    coverage_text = " ".join(str(item) for item in scene_contract.get("visual_coverage_families", []) if str(item).strip()).lower()
    if shot_order == 1 and any(term in f"{text} {coverage_text}" for term in ["wide", "establish", "aerial", "opening", "overview"]):
        return "establishing_wide"
    if any(term in text for term in ["insert", "detail", "prop", "object", "hand"]):
        return "insert_detail"
    if any(term in text for term in ["over-the-shoulder", "over the shoulder", "dialogue", "conversation"]):
        return "over_the_shoulder"
    if any(term in text for term in ["lift", "lifting", "carry", "carrying", "retrieve", "retrieval", "kneel", "kneeling", "hoist", "drag", "struggle"]):
        return "medium"
    if any(term in text for term in ["reaction", "respond", "reveal", "realize", "recognize", "discover", "discovery", "grief", "corpse", "body", "dead", "deceased", "stare", "frozen", "horror"]):
        return "reaction_closeup"
    if any(term in text for term in ["crash", "battle", "attack", "fight", "chase", "charge", "action", "pursuit", "flee", "flight", "run", "running", "pursuing", "ambush", "skirmish"]):
        return "action"
    if shot_order == len(scene_contract.get("beat_list", []) or []):
        return "closing_reaction"
    return "medium"


def _resolved_shot_type(
    scene_contract: dict[str, Any],
    beat_payload: dict[str, Any],
    planned_shot: dict[str, Any],
    shot_order: int,
    shot_size: str,
) -> str:
    text = " ".join(
        str(item)
        for item in [
            beat_payload.get("summary", ""),
            beat_payload.get("action_start", ""),
            beat_payload.get("action_end", ""),
            beat_payload.get("coverage_hint", ""),
            beat_payload.get("coverage_priority", ""),
            beat_payload.get("blocking_hint", ""),
            planned_shot.get("narrative_function", ""),
            planned_shot.get("planned_shot_moment_summary", ""),
        ]
        if str(item).strip()
    ).lower()

    if shot_size == "insert_detail" or any(term in text for term in ["insert", "detail", "prop", "object", "hand"]):
        return "insert_detail"
    if any(term in text for term in ["over-the-shoulder", "over the shoulder", "dialogue", "conversation", "exchange"]):
        return "over_the_shoulder"

    action_terms = ["battle", "attack", "fight", "chase", "charge", "pursuit", "flee", "flight", "run", "running", "ambush", "skirmish"]
    reaction_terms = ["reaction", "respond", "reveal", "realize", "recognize", "discover", "discovery", "grief", "corpse", "body", "dead", "deceased", "stare", "frozen", "horror"]
    physical_terms = ["lift", "lifting", "carry", "carrying", "retrieve", "retrieval", "kneel", "kneeling", "hoist", "drag", "struggle"]

    if shot_size in WIDE_SHOT_SIZES:
        if any(term in text for term in action_terms):
            return "action"
        return "establishing_wide"
    if shot_size in CLOSE_SHOT_SIZES:
        return "reaction_closeup"
    if any(term in text for term in action_terms):
        return "action"
    if any(term in text for term in physical_terms):
        return "medium"
    if shot_order == len(scene_contract.get("beat_list", []) or []) and any(term in text for term in reaction_terms):
        return "closing_reaction"
    if any(term in text for term in reaction_terms):
        return "medium"
    return _shot_type_from_beat(scene_contract, beat_payload, shot_order)


def _camera_description(shot_type: str, beat_summary: str) -> str:
    mapping = {
        "establishing_wide": "Wide establishing frame with a steady or lightly drifting camera.",
        "action": "Active camera with tracking energy and clear spatial orientation.",
        "reaction_closeup": "Close framing that isolates reaction and emotional emphasis.",
        "insert_detail": "Tight detail framing focused on a single visual object or gesture.",
        "over_the_shoulder": "Shoulder-level conversational framing with visible foreground presence.",
        "closing_reaction": "Controlled closing frame that lands the consequence of the beat.",
        "medium": "Stable medium framing that keeps action and character readable.",
    }
    return mapping.get(shot_type, "Stable readable framing built from the beat requirement.")


def _composition_description(shot_type: str, characters: list[ShotReference], environment: ShotReference, beat_summary: str) -> str:
    cast = ", ".join(_best_display_label(ref) for ref in characters[:3] if _best_display_label(ref)) or "scene cast"
    env = environment.display_name or environment.label
    beat_text = beat_summary.lower()
    if shot_type == "establishing_wide":
        return f"Wide composition across {env} with {cast} placed for immediate spatial orientation."
    if shot_type == "action":
        return f"Dynamic composition in {env} with clear pursuit vectors and readable movement for {cast}."
    if shot_type == "reaction_closeup":
        if any(term in beat_text for term in ["body", "corpse", "deceased", "dead"]):
            return f"Intimate composition that holds {cast} against {env} while preserving the fallen-body reveal."
        return f"Intimate composition that isolates {cast} against {env} to capture the beat's emotional turn."
    if shot_type == "insert_detail":
        return f"Detail composition centered on the key physical action or prop inside {env}."
    if shot_type == "over_the_shoulder":
        return f"Over-the-shoulder composition in {env} with {cast} sharing the frame for dialogue or tension."
    if shot_type == "closing_reaction":
        return f"Closing composition in {env} that emphasizes the consequence of {beat_summary.lower()}."
    if any(term in beat_text for term in ["lift", "carry", "retrieval", "struggle", "hoist", "drag"]):
        return f"Readable medium composition in {env} that keeps {cast} together so the physical effort stays obvious."
    return f"Readable medium composition in {env} featuring {cast}."


def _prompt_seed(
    *,
    shot_title: str,
    shot_type: str,
    camera_description: str,
    composition: str,
    characters: list[ShotReference],
    environment: ShotReference,
    beat_summary: str,
    shot_size: str,
    camera_angle: str,
    lens_family: str,
    camera_motion: str,
    zoom_behavior: str,
    focus_strategy: str,
    lighting_style: str,
    subject_visibility: str,
    primary_subject_angle: str,
) -> str:
    cast = ", ".join(ref.display_name or ref.label for ref in characters[:3]) or "none"
    env = environment.display_name or environment.label
    return _compact_snippet(
        f"{shot_title}. {shot_type}. size={shot_size}. angle={camera_angle}. lens={lens_family}. motion={camera_motion}. zoom={zoom_behavior}. focus={focus_strategy}. lighting={lighting_style}. visibility={subject_visibility}. subject_angle={primary_subject_angle}. {camera_description} {composition} Cast: {cast}. Environment: {env}. Beat: {beat_summary}",
        limit=320,
    )


def _coerce_scene_beat(raw_beat: dict[str, Any], beat_summary: str) -> dict[str, Any]:
    return {
        "summary": beat_summary,
        "action_start": _first_nonempty(str(raw_beat.get("action_start", "")), str(raw_beat.get("start", "")), fallback=beat_summary),
        "action_end": _first_nonempty(str(raw_beat.get("action_end", "")), str(raw_beat.get("end", "")), fallback=beat_summary),
        "active_subjects": _coerce_string_list(raw_beat.get("active_subjects", [])),
        "passive_subjects": _coerce_string_list(raw_beat.get("passive_subjects", [])),
        "spatial_context": _first_nonempty(str(raw_beat.get("spatial_context", "")), str(raw_beat.get("continuity_focus", "")), fallback=""),
        "blocking_hint": _first_nonempty(str(raw_beat.get("blocking_hint", "")), str(raw_beat.get("coverage_hint", "")), fallback=""),
        "environment_subzone": _first_nonempty(str(raw_beat.get("environment_subzone", "")), fallback=""),
        "coverage_priority": _first_nonempty(str(raw_beat.get("coverage_priority", "")), fallback=""),
        "handoff_to_next": _first_nonempty(str(raw_beat.get("handoff_to_next", "")), fallback=""),
    }


def _shot_subject_blocking(scene_contract: dict[str, Any], beat_payload: dict[str, Any], characters: list[ShotReference]) -> list[str]:
    blocking: list[str] = []
    if beat_payload.get("blocking_hint"):
        blocking.append(str(beat_payload["blocking_hint"]))
    if beat_payload.get("spatial_context"):
        blocking.append(str(beat_payload["spatial_context"]))
    for ref in characters[:3]:
        label = ref.display_name or ref.label
        if label:
            blocking.append(f"{label} remains readable within the active playing space.")
    return _ordered_unique([item for item in blocking if item])[:4]


def _camera_relative_positions(characters: list[ShotReference], environment: ShotReference, beat_payload: dict[str, Any]) -> list[str]:
    positions: list[str] = []
    subzone = str(beat_payload.get("environment_subzone", "")).strip()
    if subzone:
        positions.append(f"Camera anchors the action inside the {subzone}.")
    env_name = environment.display_name or environment.label
    if env_name:
        positions.append(f"Background depth should keep {env_name} legible as the location anchor.")
    for index, ref in enumerate(characters[:2], start=1):
        label = ref.display_name or ref.label
        positions.append(f"Subject {index}: {label} remains visually readable against the environment scale.")
    return positions[:4]


def _visible_environment_features(environment: ShotReference, beat_payload: dict[str, Any]) -> list[str]:
    features: list[str] = []
    subzone = str(beat_payload.get("environment_subzone", "")).strip()
    if subzone:
        features.append(subzone)
    notes = str(environment.notes or "").strip()
    if notes:
        features.append(_compact_snippet(notes, limit=120))
    return _ordered_unique([item for item in features if item])[:3]


def _normalize_enum(value: Any, allowed: set[str], fallback: str = "") -> str:
    normalized = str(value or "").strip().lower()
    return normalized if normalized in allowed else fallback


def _default_primary_subject_angle(primary_subject: str, shot_size: str, subject_visibility: str) -> str:
    if subject_visibility == "off_screen_voice" or shot_size == "insert_detail":
        return ""
    if primary_subject.strip().lower() == "the narrator":
        return ""
    return "front_three_quarter_left"


def _angle_to_facing_direction(primary_subject_angle: str, subject_visibility: str) -> str:
    if subject_visibility == "off_screen_voice":
        return "off-screen voice only"
    mapping = {
        "front": "facing directly toward camera",
        "front_three_quarter_left": "front three-quarter left toward the scene action",
        "front_three_quarter_right": "front three-quarter right toward the scene action",
        "profile_left": "profile left toward the scene action",
        "profile_right": "profile right toward the scene action",
        "rear_three_quarter_left": "rear three-quarter left away from camera",
        "rear_three_quarter_right": "rear three-quarter right away from camera",
        "back": "back to camera with head turned toward the action",
    }
    return mapping.get(primary_subject_angle, "angled toward the scene action")


def _camera_package_description(
    shot_size: str,
    camera_angle: str,
    lens_family: str,
    camera_motion: str,
    zoom_behavior: str,
    focus_strategy: str,
    lighting_style: str,
) -> str:
    parts = [
        shot_size.replace("_", "-") if shot_size else "",
        camera_angle.replace("_", " ") if camera_angle else "",
        f"{lens_family.replace('_', '-')} lens" if lens_family else "",
        camera_motion.replace("_", " ") if camera_motion else "",
        f"zoom {zoom_behavior.replace('_', ' ')}" if zoom_behavior and zoom_behavior != "none" else "",
        focus_strategy.replace("_", " ") if focus_strategy else "",
        lighting_style.replace("_", " ") if lighting_style else "",
    ]
    return _compact_snippet(", ".join(part for part in parts if part), limit=180)


def _visible_primary_subject_id(primary_subject: str, characters: list[ShotReference], subject_visibility: str) -> str:
    if subject_visibility == "off_screen_voice" or primary_subject.strip().lower() == "the narrator":
        for ref in characters:
            canonical_id = (ref.canonical_id or "").strip()
            if canonical_id:
                return canonical_id
        return ""
    primary_variants = _label_variants(primary_subject)
    for ref in characters:
        canonical_id = (ref.canonical_id or "").strip()
        ref_variants = set(_label_variants(ref.canonical_id or "")) | set(_label_variants(ref.label)) | set(_label_variants(ref.display_name))
        if canonical_id and any(variant in ref_variants for variant in primary_variants):
            return canonical_id
    for ref in characters:
        canonical_id = (ref.canonical_id or "").strip()
        if canonical_id:
            return canonical_id
    return ""


def _visible_secondary_subject_ids(primary_subject_id: str, characters: list[ShotReference]) -> list[str]:
    secondary: list[str] = []
    for ref in characters:
        canonical_id = (ref.canonical_id or "").strip()
        if not canonical_id or canonical_id == primary_subject_id:
            continue
        secondary.append(canonical_id)
    return _ordered_unique(secondary)[:3]


def _primary_subject_frame_position(
    shot_size: str,
    environment_subzone: str,
    subject_visibility: str,
    shot_order: int,
) -> str:
    if subject_visibility == "off_screen_voice":
        return "off-screen voice with no visible body"
    subzone = environment_subzone or "active playing area"
    if shot_size in {"extreme_wide", "wide"}:
        return f"midground inside {subzone}"
    if shot_size in {"medium_close", "close_up", "extreme_close_up"}:
        return f"foreground inside {subzone}"
    if shot_order == 1:
        return f"foreground entry line within {subzone}"
    return f"foreground right within {subzone}"


def _primary_subject_scale_relation(
    scene_contract: dict[str, Any],
    planned_shot: dict[str, Any],
    environment: ShotReference,
) -> str:
    for candidate in (
        str(planned_shot.get("planned_shot_scale_proof_detail", "")),
        str(scene_contract.get("scene_primary_scale_story_point", "")),
        str(environment.notes or ""),
    ):
        if _looks_like_scale_relation(candidate):
            return candidate.strip()
    return "preserve readable body-to-environment scale in frame"


def _environment_anchor(
    planned_shot: dict[str, Any],
    visible_environment_features: list[str],
    subzone: str,
) -> str:
    for candidate in (
        str(planned_shot.get("planned_shot_required_anchor_1", "")),
        visible_environment_features[0] if visible_environment_features else "",
        subzone,
    ):
        if _looks_like_environment_anchor(candidate):
            return candidate.strip()
    return subzone.strip() or (visible_environment_features[0].strip() if visible_environment_features else "")


def _scale_proof_detail(
    planned_shot: dict[str, Any],
    primary_subject_scale_relation: str,
) -> str:
    for candidate in (
        str(planned_shot.get("planned_shot_scale_proof_detail", "")),
        primary_subject_scale_relation,
    ):
        if _looks_like_scale_relation(candidate):
            return candidate.strip()
    return primary_subject_scale_relation.strip()


def _subject_relation_summary(primary_subject: str, secondary_subjects: list[str], subject_visibility: str) -> str:
    if subject_visibility == "off_screen_voice":
        return "visible bodies should carry the scene while narration remains off-screen"
    if secondary_subjects:
        return f"{primary_subject} plays against {', '.join(secondary_subjects[:2])} in the same frame"
    return f"{primary_subject} carries the frame alone"


def _default_shot_enums(shot_type: str, primary_subject: str) -> dict[str, str]:
    shot_type_normalized = shot_type.strip().lower()
    if shot_type_normalized == "insert_detail":
        shot_size = "insert_detail"
        lens_family = "portrait"
        focus_strategy = "shallow_subject"
        camera_motion = "locked_off"
        zoom_behavior = "none"
        camera_angle = "eye_level"
    elif shot_type_normalized in {"closing_reaction", "close_up", "reaction_closeup"}:
        shot_size = "close_up"
        lens_family = "portrait"
        focus_strategy = "shallow_subject"
        camera_motion = "push_in"
        zoom_behavior = "subtle_in"
        camera_angle = "eye_level"
    elif shot_type_normalized in {"wide", "establishing", "establishing_wide"}:
        shot_size = "wide"
        lens_family = "wide"
        focus_strategy = "deep_focus"
        camera_motion = "locked_off"
        zoom_behavior = "none"
        camera_angle = "eye_level"
    else:
        shot_size = "medium"
        lens_family = "normal"
        focus_strategy = "deep_focus"
        camera_motion = "locked_off"
        zoom_behavior = "none"
        camera_angle = "eye_level"
    subject_visibility = "off_screen_voice" if primary_subject.strip().lower() == "the narrator" else "on_screen"
    return {
        "shot_size": shot_size,
        "camera_angle": camera_angle,
        "lens_family": lens_family,
        "camera_motion": camera_motion,
        "zoom_behavior": zoom_behavior,
        "focus_strategy": focus_strategy,
        "lighting_style": "hard_directional",
        "subject_visibility": subject_visibility,
        "narration_mode": "voiceover_off_screen" if subject_visibility == "off_screen_voice" else "none",
        "primary_subject_angle": _default_primary_subject_angle(primary_subject, shot_size, subject_visibility),
    }


def _scene_planned_shot_map(scene_contract: dict[str, Any]) -> dict[str, dict[str, Any]]:
    mapping: dict[str, dict[str, Any]] = {}
    for item in scene_contract.get("planned_shots", []):
        if not isinstance(item, dict):
            continue
        shot_id = str(item.get("planned_shot_id", item.get("shot_id", ""))).strip().upper()
        if shot_id:
            mapping[shot_id] = item
    return mapping


def _shot_title_from_beat(shot_type: str, beat_summary: str, shot_order: int) -> str:
    snippet = _compact_snippet(beat_summary, limit=54)
    if snippet:
        return f"{shot_type.replace('_', ' ').title()} {shot_order}: {snippet}"
    return f"{shot_type.replace('_', ' ').title()} {shot_order}"


def _build_shot_blueprints(scene_contract: dict[str, Any], project_dir: Path, scene_binding: dict[str, Any] | None = None) -> list[dict[str, Any]]:
    beats = scene_contract.get("beat_list", [])
    if not isinstance(beats, list) or not beats:
        beats = [{"beat_id": "BT001", "summary": scene_contract.get("summary", "") or scene_contract.get("production_intent", "") or scene_contract.get("scene_title", "")}]
    blueprints: list[dict[str, Any]] = []
    previous_end_state = _first_nonempty(str(scene_contract.get("scene_start_state", "")), str(scene_contract.get("summary", "")), fallback="")
    planned_shots = _scene_planned_shot_map(scene_contract)
    for index, raw_beat in enumerate(beats, start=1):
        beat_id = f"BT{index:03d}"
        shot_id = f"SH{index:03d}"
        beat_summary = ""
        beat_payload: dict[str, Any] = {
            "summary": "",
            "action_start": "",
            "action_end": "",
            "active_subjects": [],
            "passive_subjects": [],
            "spatial_context": "",
            "blocking_hint": "",
            "environment_subzone": "",
            "coverage_priority": "",
            "handoff_to_next": "",
        }
        if isinstance(raw_beat, dict):
            beat_id = str(raw_beat.get("beat_id", beat_id)).strip().upper() or beat_id
            beat_summary = _first_nonempty(
                str(raw_beat.get("summary", "")),
                str(raw_beat.get("markdown", "")),
                fallback="",
            )
            beat_payload = _coerce_scene_beat(raw_beat, beat_summary)
        elif isinstance(raw_beat, str):
            beat_summary = raw_beat.strip()
            beat_payload["summary"] = beat_summary
            beat_payload["action_start"] = beat_summary
            beat_payload["action_end"] = beat_summary
        planned_shot = planned_shots.get(shot_id, {})
        environment = _select_environment_ref(
            scene_contract,
            project_dir,
            scene_binding=scene_binding,
            beat_id=beat_id,
            subzone_hint=_first_nonempty(str(planned_shot.get("environment_subzone", "")), str(beat_payload.get("environment_subzone", "")), fallback=""),
        )
        provisional_shot_type = _shot_type_from_beat(scene_contract, beat_payload, index)
        subject_hints = _coerce_string_list(
            planned_shot.get("primary_subject_seed", ""),
            planned_shot.get("secondary_subjects_seed", []),
            beat_payload.get("active_subjects", []),
            beat_payload.get("passive_subjects", []),
        )
        candidate_characters = _selected_characters(
            scene_contract,
            project_dir,
            beat_summary,
            index,
            scene_binding=scene_binding,
            subject_hints=subject_hints,
        )
        continuity_constraints = _coerce_string_list(
            scene_contract.get("continuity_constraints", []),
            beat_summary,
            scene_contract.get("unresolved_questions", []),
        )
        primary_subject = _first_nonempty(
            str(planned_shot.get("primary_subject_seed", "")),
            beat_payload["active_subjects"][0] if beat_payload["active_subjects"] else "",
            _first_nonempty(candidate_characters[0].display_name if candidate_characters else "", candidate_characters[0].label if candidate_characters else "", fallback="scene subject"),
        )
        secondary_subject_hints = _coerce_string_list(planned_shot.get("secondary_subjects_seed", []), beat_payload.get("passive_subjects", []))
        provisional_enums = _default_shot_enums(provisional_shot_type, primary_subject)
        shot_size = _normalize_enum(planned_shot.get("shot_size"), SHOT_SIZE_ENUM, fallback=provisional_enums["shot_size"])
        shot_type = _resolved_shot_type(scene_contract, beat_payload, planned_shot, index, shot_size)
        enums = _default_shot_enums(shot_type, primary_subject)
        camera_angle = _normalize_enum(planned_shot.get("camera_angle"), CAMERA_ANGLE_ENUM, fallback=enums["camera_angle"])
        lens_family = _normalize_enum(planned_shot.get("lens_family"), LENS_FAMILY_ENUM, fallback=enums["lens_family"])
        camera_motion = _normalize_enum(planned_shot.get("camera_motion"), CAMERA_MOTION_ENUM, fallback=enums["camera_motion"])
        zoom_behavior = _normalize_enum(planned_shot.get("zoom_behavior"), ZOOM_BEHAVIOR_ENUM, fallback=enums["zoom_behavior"])
        focus_strategy = _normalize_enum(planned_shot.get("focus_strategy"), FOCUS_STRATEGY_ENUM, fallback=enums["focus_strategy"])
        lighting_style = _normalize_enum(planned_shot.get("lighting_style"), LIGHTING_STYLE_ENUM, fallback=enums["lighting_style"])
        subject_visibility = _normalize_enum(planned_shot.get("subject_visibility"), SUBJECT_VISIBILITY_ENUM, fallback=enums["subject_visibility"])
        narration_mode = _normalize_enum(planned_shot.get("narration_mode"), NARRATION_MODE_ENUM, fallback=enums["narration_mode"])
        primary_subject_angle = _normalize_enum(planned_shot.get("primary_subject_angle"), PRIMARY_SUBJECT_ANGLE_ENUM, fallback=enums["primary_subject_angle"])
        characters = _filter_visible_characters(
            characters=candidate_characters,
            primary_subject=primary_subject,
            secondary_subjects=secondary_subject_hints,
            beat_payload=beat_payload,
            shot_size=shot_size,
            shot_type=shot_type,
            subject_visibility=subject_visibility,
        )
        secondary_subjects = _visible_secondary_subject_labels(primary_subject, characters)
        camera_description = _camera_description(shot_type, beat_summary)
        composition = _composition_description(shot_type, characters, environment, beat_summary)
        shot_title = _shot_title_from_beat(shot_type, beat_summary, index)
        start_state = _first_nonempty(str(planned_shot.get("start_state_seed", "")), str(beat_payload.get("action_start", "")), previous_end_state, beat_summary, fallback=beat_summary)
        end_state = _first_nonempty(str(planned_shot.get("end_state_seed", "")), str(beat_payload.get("action_end", "")), beat_summary, fallback=start_state)
        action_continues_from = previous_end_state if index > 1 else _first_nonempty(str(scene_contract.get("scene_start_state", "")), beat_summary, fallback="")
        action_hands_off_to = _first_nonempty(str(beat_payload.get("handoff_to_next", "")), end_state, fallback="")
        action_during_shot = _first_nonempty(str(planned_shot.get("action_seed", "")), beat_summary, fallback=beat_summary)
        subject_blocking = _shot_subject_blocking(scene_contract, beat_payload, characters)
        subject_blocking = _ordered_unique(_coerce_string_list(planned_shot.get("blocking_seed", []), subject_blocking))
        camera_positions = _camera_relative_positions(characters, environment, beat_payload)
        subzone = _first_nonempty(str(planned_shot.get("environment_subzone", "")), str(beat_payload.get("environment_subzone", "")), *scene_contract.get("environment_subzones", []), fallback="")
        visible_environment_features = _visible_environment_features(environment, beat_payload)
        visible_primary_subject_id = _visible_primary_subject_id(primary_subject, characters, subject_visibility)
        visible_secondary_subject_ids = _visible_secondary_subject_ids(visible_primary_subject_id, characters)
        primary_subject_frame_position = _primary_subject_frame_position(shot_size, subzone, subject_visibility, index)
        primary_subject_scale_relation = _primary_subject_scale_relation(scene_contract, planned_shot, environment)
        primary_subject_facing_direction = _angle_to_facing_direction(primary_subject_angle, subject_visibility)
        primary_subject_pose_description = _first_nonempty(start_state, action_during_shot, fallback="")
        subject_relation_summary = _subject_relation_summary(primary_subject, secondary_subjects, subject_visibility)
        required_environment_anchor_1 = _environment_anchor(planned_shot, visible_environment_features, subzone)
        required_scale_proof_detail = _scale_proof_detail(planned_shot, primary_subject_scale_relation)
        camera_package_description = _camera_package_description(
            shot_size,
            camera_angle,
            lens_family,
            camera_motion,
            zoom_behavior,
            focus_strategy,
            lighting_style,
        )
        prompt_seed = _prompt_seed(
            shot_title=shot_title,
            shot_type=shot_type,
            camera_description=camera_description,
            composition=composition,
            characters=characters,
            environment=environment,
            beat_summary=beat_summary,
            shot_size=shot_size,
            camera_angle=camera_angle,
            lens_family=lens_family,
            camera_motion=camera_motion,
            zoom_behavior=zoom_behavior,
            focus_strategy=focus_strategy,
            lighting_style=lighting_style,
            subject_visibility=subject_visibility,
            primary_subject_angle=primary_subject_angle or "unspecified",
        )
        blueprints.append(
            {
                "shot_id": shot_id,
                "shot_order": index,
                "beat_ids": [beat_id],
                "shot_moment_summary": _first_nonempty(
                    str(planned_shot.get("planned_shot_moment_summary", "")),
                    beat_summary,
                    fallback="",
                ),
                "primary_subject": primary_subject,
                "secondary_subjects": secondary_subjects,
                "start_state": start_state,
                "end_state": end_state,
                "action_during_shot": action_during_shot,
                "action_continues_from": action_continues_from,
                "action_hands_off_to": action_hands_off_to,
                "shot_size": shot_size,
                "camera_angle": camera_angle,
                "lens_family": lens_family,
                "camera_motion": camera_motion,
                "zoom_behavior": zoom_behavior,
                "focus_strategy": focus_strategy,
                "lighting_style": lighting_style,
                "subject_visibility": subject_visibility,
                "narration_mode": narration_mode,
                "primary_subject_angle": primary_subject_angle,
                "visible_primary_subject_id": visible_primary_subject_id,
                "visible_secondary_subject_ids": visible_secondary_subject_ids,
                "primary_subject_frame_position": primary_subject_frame_position,
                "primary_subject_scale_relation": primary_subject_scale_relation,
                "primary_subject_facing_direction": primary_subject_facing_direction,
                "primary_subject_pose_description": primary_subject_pose_description,
                "subject_relation_summary": subject_relation_summary,
                "required_environment_anchor_1": required_environment_anchor_1,
                "required_scale_proof_detail": required_scale_proof_detail,
                "camera_package_description": camera_package_description,
                "subject_blocking": subject_blocking,
                "camera_relative_positions": camera_positions,
                "gaze_directions": [f"{primary_subject} focuses toward the active scene action."] if primary_subject else [],
                "environment_subzone": subzone,
                "key_visible_environment_features": visible_environment_features,
                "continuity_from_previous_shot": action_continues_from,
                "continuity_to_next_shot": action_hands_off_to,
                "pose_anchor_frame": start_state,
                "pose_end_frame": end_state,
                "shot_title": shot_title,
                "shot_type": shot_type,
                "camera_description": camera_description,
                "composition": composition,
                "characters_in_frame": [ref.to_dict() for ref in characters],
                "environment": environment.to_dict(),
                "continuity_constraints": continuity_constraints[:6],
                "prompt_seed": prompt_seed,
                "shot_notes": _compact_snippet(beat_summary or scene_contract.get("summary", ""), limit=220),
            }
        )
        previous_end_state = end_state
    return blueprints


def _load_shot_planning_evidence(
    *,
    project_dir: Path,
    scene_contract: dict[str, Any],
    scene_binding: dict[str, Any] | None,
    shot_blueprints: list[dict[str, Any]],
) -> dict[str, Any]:
    character_refs = scene_contract.get("characters_required", [])
    environment_refs = scene_contract.get("environments_required", [])
    selected_character_ids = [
        str(ref.get("canonical_id", "")).strip()
        for blueprint in shot_blueprints
        for ref in blueprint.get("characters_in_frame", [])
        if isinstance(ref, dict) and str(ref.get("canonical_id", "")).strip()
    ]
    selected_environment_ids = [
        str(blueprint.get("environment", {}).get("canonical_id", "")).strip()
        for blueprint in shot_blueprints
        if isinstance(blueprint.get("environment"), dict) and str(blueprint.get("environment", {}).get("canonical_id", "")).strip()
    ]

    character_evidence: list[str] = []
    environment_evidence: list[str] = []
    character_fingerprints: list[str] = []
    environment_fingerprints: list[str] = []

    for canonical_id in _ordered_unique(selected_character_ids)[:3]:
        bible = _load_character_bible(project_dir, canonical_id)
        if not bible:
            continue
        meta = bible.get("metadata", {}) if isinstance(bible.get("metadata"), dict) else {}
        if isinstance(meta.get("source_fingerprint"), str):
            character_fingerprints.append(meta["source_fingerprint"])
        line = _compact_snippet(
            " | ".join(
                part
                for part in [
                    str(bible.get("display_name", "")),
                    str(bible.get("stable_visual_summary", "")),
                    str(bible.get("costume_signature", "")),
                    str(bible.get("personality", "")),
                ]
                if part.strip()
            ),
            limit=260,
        )
        if line:
            character_evidence.append(line)

    for canonical_id in _ordered_unique(selected_environment_ids)[:2]:
        bible = _load_environment_bible(project_dir, canonical_id)
        if not bible:
            continue
        meta = bible.get("metadata", {}) if isinstance(bible.get("metadata"), dict) else {}
        if isinstance(meta.get("source_fingerprint"), str):
            environment_fingerprints.append(meta["source_fingerprint"])
        line = _compact_snippet(
            " | ".join(
                part
                for part in [
                    str(bible.get("display_name", "")),
                    str(bible.get("visual_summary", "")),
                    str(bible.get("layout_notes", "")),
                    str(bible.get("lighting", "")),
                    str(bible.get("mood", "")),
                ]
                if part.strip()
            ),
            limit=260,
        )
        if line:
            environment_evidence.append(line)

    scene_evidence = [
        _compact_snippet(str(scene_contract.get("production_intent", "")), limit=260),
        _compact_snippet(str(scene_contract.get("summary", "")), limit=260),
        _compact_snippet(str(scene_contract.get("emotional_arc", "")), limit=220),
        _compact_snippet(str(scene_contract.get("scene_start_state", "")), limit=220),
        _compact_snippet(str(scene_contract.get("scene_end_state", "")), limit=220),
        _compact_snippet(str(scene_contract.get("dominant_action_line", "")), limit=220),
        *[_compact_snippet(str(item), limit=220) for item in _coerce_string_list(scene_contract.get("visual_coverage_families", []))[:4]],
        *[_compact_snippet(str(item), limit=220) for item in _coerce_string_list(scene_contract.get("continuity_constraints", []))[:4]],
        *[_compact_snippet(str(item), limit=220) for item in _coerce_string_list(scene_contract.get("scene_spatial_layout", []))[:3]],
        *[_compact_snippet(str(item), limit=220) for item in _coerce_string_list(scene_contract.get("character_spatial_map", []))[:3]],
    ]
    scene_evidence = [item for item in scene_evidence if item]

    fingerprint_payload = {
        "schema_version": SHOT_PLANNER_SCHEMA_VERSION,
        "scene_contract": scene_contract,
        "scene_binding": scene_binding or {},
        "shot_blueprints": shot_blueprints,
        "character_fingerprints": _ordered_unique(character_fingerprints),
        "environment_fingerprints": _ordered_unique(environment_fingerprints),
    }

    return {
        "scene_evidence": scene_evidence[:6],
        "character_evidence": character_evidence[:3],
        "environment_evidence": environment_evidence[:2],
        "fingerprint_payload": fingerprint_payload,
    }


def _llm_synthesis(
    *,
    project_slug: str,
    scene_contract: dict[str, Any],
    shot_blueprints: list[dict[str, Any]],
    evidence: dict[str, Any],
) -> list[dict[str, Any]] | None:
    settings = load_runtime_settings()
    client = LMStudioClient(settings)

    system = (
        "You are a film shot planning system. "
        "Use only the provided evidence. Preserve shot order, keep the plan compact, and avoid inventing unsupported details. "
        "Return one tagged FilmCreator markdown packet only. Do not return JSON."
    )

    user = f"""
Create generation-ready shot packages from the provided scene contract and shot blueprints.

PRIORITIES:
1. keep the shot order stable
2. tighten camera and composition language
3. keep each shot compact and production-usable
4. preserve continuity constraints and character/environment grounding
5. make start state, end state, blocking, and action handoff explicit enough to stage a frame
6. return prompt-ready visual fragments, not generic summaries

STYLE RULES:
- prefer short visual clauses over abstract commentary
- do not write filler like "maintain readability" or "continue the established action"
- choose one concrete environment anchor when possible
- if scale matters, describe the scale proof explicitly

PROJECT:
{project_slug}

SCENE CONTRACT:
{json.dumps(scene_contract, indent=2, ensure_ascii=False)}

SCENE EVIDENCE:
{json.dumps(evidence["scene_evidence"], indent=2, ensure_ascii=False)}

CHARACTER EVIDENCE:
{json.dumps(evidence["character_evidence"], indent=2, ensure_ascii=False)}

ENVIRONMENT EVIDENCE:
{json.dumps(evidence["environment_evidence"], indent=2, ensure_ascii=False)}

BLUEPRINTS:
{json.dumps(shot_blueprints, indent=2, ensure_ascii=False)}

Return exactly one FilmCreator packet in this structure:
[[FILMCREATOR_PACKET]]
task: shot_planning
version: 1

[[FILMCREATOR_RECORD]]
type: shot
artifact_id: CH024_SC001_SH001_SHOT_PACKAGE
shot_id: SH001
shot_order: 1
scene_id: CH024_SC001
chapter_id: CH024
status: generated
entity_kind: shot

[[SECTION shot_markdown]]
shot_title: <short shot title>
shot_order: 1
beat_ids:
- BT001
primary_subject: <main subject driving the shot>
secondary_subjects:
- subject 2
- subject 3
shot_moment_summary: <short visible frame summary>
start_state: <explicit visual/action state at the start of the shot>
end_state: <explicit visual/action state at the end of the shot>
action_during_shot: <what the shot is actively covering>
action_continues_from: <what visual/action state this inherits>
action_hands_off_to: <what the next shot should inherit>
shot_type: <shot type>
shot_size: <extreme_wide|wide|full|medium_full|medium|medium_close|close_up|extreme_close_up|insert_detail>
camera_angle: <eye_level|low_angle|high_angle|overhead|dutch>
lens_family: <ultra_wide|wide|normal|portrait|telephoto>
camera_motion: <locked_off|pan|tilt|push_in|pull_back|track|crane|handheld>
zoom_behavior: <none|subtle_in|subtle_out|strong_in|strong_out>
focus_strategy: <deep_focus|shallow_subject|rack_focus|environment_priority>
lighting_style: <soft_even|hard_directional|high_contrast_ceremonial|diffuse_ambient|backlit|torch_firelight|low_key_night>
subject_visibility: <on_screen|partial|silhouette|off_screen_voice|implied_only>
narration_mode: <none|voiceover_off_screen|in_scene_speaker|internal_monologue>
primary_subject_angle: <front|front_three_quarter_left|front_three_quarter_right|profile_left|profile_right|rear_three_quarter_left|rear_three_quarter_right|back>
visible_primary_subject_id: <canonical id or visible role token>
visible_secondary_subject_ids:
- canonical id
primary_subject_frame_position: <short frame placement clause>
primary_subject_scale_relation: <short scale relation clause>
primary_subject_facing_direction: <short facing direction clause>
primary_subject_pose_description: <short pose clause>
subject_relation_summary: <short relation clause>
required_environment_anchor_1: <short required anchor clause>
required_scale_proof_detail: <short scale proof clause>
camera_package_description: <single compact camera package clause>
camera_description: <camera note>
composition: <composition note>
characters_in_frame:
- john_carter
- tars_tarkas
environment: <environment reference or label>
environment_subzone: <specific playable subzone inside the environment>
subject_blocking:
- character placement note
- staging note
camera_relative_positions:
- camera/subject relation note
gaze_directions:
- eyeline note
key_visible_environment_features:
- visible set anchor
continuity_from_previous_shot: <specific state inherited from previous shot or scene start>
continuity_to_next_shot: <specific state handed off to the next shot>
pose_anchor_frame: <clear pose description for image generation>
pose_end_frame: <clear ending pose description for continuity>
continuity_constraints:
- constraint 1
- constraint 2
prompt_seed: <short generation prompt seed>
shot_notes: <optional short note>
[[/SECTION]]

[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
"""

    try:
        response = client.chat_completion(system_prompt=system, user_prompt=user, temperature=0.1)
        packet = parse_packet_document(response, expected_task="shot_planning")
        records = []
        for record in packet.records:
            if record.fields.get("type") != "shot":
                continue
            shot_markdown = record.sections.get("shot_markdown", "")
            parsed = _parse_markdown_section(shot_markdown)
            scalars, lists, freeform = parsed
            records.append(
                {
                    "shot_id": _first_nonempty(record.fields.get("shot_id"), fallback=""),
                    "shot_order": int(record.fields.get("shot_order", "0") or "0") if str(record.fields.get("shot_order", "")).isdigit() else None,
                    "beat_ids": _coerce_string_list(lists.get("beat_ids"), scalars.get("beat_ids")),
                    "primary_subject": _first_nonempty(scalars.get("primary_subject"), fallback=""),
                    "secondary_subjects": _coerce_string_list(lists.get("secondary_subjects"), scalars.get("secondary_subjects")),
                    "shot_moment_summary": _first_nonempty(scalars.get("shot_moment_summary"), fallback=""),
                    "start_state": _first_nonempty(scalars.get("start_state"), fallback=""),
                    "end_state": _first_nonempty(scalars.get("end_state"), fallback=""),
                    "action_during_shot": _first_nonempty(scalars.get("action_during_shot"), fallback=""),
                    "action_continues_from": _first_nonempty(scalars.get("action_continues_from"), fallback=""),
                    "action_hands_off_to": _first_nonempty(scalars.get("action_hands_off_to"), fallback=""),
                    "shot_title": _first_nonempty(scalars.get("shot_title"), fallback=""),
                    "shot_type": _first_nonempty(scalars.get("shot_type"), fallback=""),
                    "shot_size": _first_nonempty(scalars.get("shot_size"), fallback=""),
                    "camera_angle": _first_nonempty(scalars.get("camera_angle"), fallback=""),
                    "lens_family": _first_nonempty(scalars.get("lens_family"), fallback=""),
                    "camera_motion": _first_nonempty(scalars.get("camera_motion"), fallback=""),
                    "zoom_behavior": _first_nonempty(scalars.get("zoom_behavior"), fallback=""),
                    "focus_strategy": _first_nonempty(scalars.get("focus_strategy"), fallback=""),
                    "lighting_style": _first_nonempty(scalars.get("lighting_style"), fallback=""),
                    "subject_visibility": _first_nonempty(scalars.get("subject_visibility"), fallback=""),
                    "narration_mode": _first_nonempty(scalars.get("narration_mode"), fallback=""),
                    "primary_subject_angle": _first_nonempty(scalars.get("primary_subject_angle"), fallback=""),
                    "visible_primary_subject_id": _first_nonempty(scalars.get("visible_primary_subject_id"), fallback=""),
                    "visible_secondary_subject_ids": _coerce_string_list(lists.get("visible_secondary_subject_ids"), scalars.get("visible_secondary_subject_ids")),
                    "primary_subject_frame_position": _first_nonempty(scalars.get("primary_subject_frame_position"), fallback=""),
                    "primary_subject_scale_relation": _first_nonempty(scalars.get("primary_subject_scale_relation"), fallback=""),
                    "primary_subject_facing_direction": _first_nonempty(scalars.get("primary_subject_facing_direction"), fallback=""),
                    "primary_subject_pose_description": _first_nonempty(scalars.get("primary_subject_pose_description"), fallback=""),
                    "subject_relation_summary": _first_nonempty(scalars.get("subject_relation_summary"), fallback=""),
                    "required_environment_anchor_1": _first_nonempty(scalars.get("required_environment_anchor_1"), fallback=""),
                    "required_scale_proof_detail": _first_nonempty(scalars.get("required_scale_proof_detail"), fallback=""),
                    "camera_package_description": _first_nonempty(scalars.get("camera_package_description"), fallback=""),
                    "camera_description": _first_nonempty(scalars.get("camera_description"), fallback=""),
                    "composition": _first_nonempty(scalars.get("composition"), fallback=""),
                    "characters_in_frame": _coerce_string_list(lists.get("characters_in_frame"), scalars.get("characters_in_frame")),
                    "environment": _first_nonempty(scalars.get("environment"), fallback=""),
                    "environment_subzone": _first_nonempty(scalars.get("environment_subzone"), fallback=""),
                    "subject_blocking": _coerce_string_list(lists.get("subject_blocking"), scalars.get("subject_blocking")),
                    "camera_relative_positions": _coerce_string_list(lists.get("camera_relative_positions"), scalars.get("camera_relative_positions")),
                    "gaze_directions": _coerce_string_list(lists.get("gaze_directions"), scalars.get("gaze_directions")),
                    "key_visible_environment_features": _coerce_string_list(lists.get("key_visible_environment_features"), scalars.get("key_visible_environment_features")),
                    "continuity_from_previous_shot": _first_nonempty(scalars.get("continuity_from_previous_shot"), fallback=""),
                    "continuity_to_next_shot": _first_nonempty(scalars.get("continuity_to_next_shot"), fallback=""),
                    "pose_anchor_frame": _first_nonempty(scalars.get("pose_anchor_frame"), fallback=""),
                    "pose_end_frame": _first_nonempty(scalars.get("pose_end_frame"), fallback=""),
                    "continuity_constraints": _coerce_string_list(lists.get("continuity_constraints"), scalars.get("continuity_constraints")),
                    "prompt_seed": _first_nonempty(scalars.get("prompt_seed"), freeform[0] if freeform else None, fallback=""),
                    "shot_notes": _first_nonempty(scalars.get("shot_notes"), fallback=""),
                    "target_seconds": _coerce_float(scalars.get("target_seconds"), scalars.get("estimated_seconds"), fallback=0.0) or None,
                }
            )
        if not records:
            return None
        return records
    except Exception:
        return None


def _parse_shot_plan_blueprint(payload: dict[str, Any]) -> dict[str, Any]:
    return {
        "shot_id": str(payload.get("shot_id", "")),
        "shot_order": int(payload.get("shot_order", 0) or 0),
        "primary_subject": str(payload.get("primary_subject", "")),
        "secondary_subjects": _coerce_string_list(payload.get("secondary_subjects", [])),
        "shot_moment_summary": str(payload.get("shot_moment_summary", "")),
        "start_state": str(payload.get("start_state", "")),
        "end_state": str(payload.get("end_state", "")),
        "action_during_shot": str(payload.get("action_during_shot", "")),
        "action_continues_from": str(payload.get("action_continues_from", "")),
        "action_hands_off_to": str(payload.get("action_hands_off_to", "")),
        "shot_title": str(payload.get("shot_title", "")),
        "shot_type": str(payload.get("shot_type", "")),
        "shot_size": str(payload.get("shot_size", "")),
        "camera_angle": str(payload.get("camera_angle", "")),
        "lens_family": str(payload.get("lens_family", "")),
        "camera_motion": str(payload.get("camera_motion", "")),
        "zoom_behavior": str(payload.get("zoom_behavior", "")),
        "focus_strategy": str(payload.get("focus_strategy", "")),
        "lighting_style": str(payload.get("lighting_style", "")),
        "subject_visibility": str(payload.get("subject_visibility", "")),
        "narration_mode": str(payload.get("narration_mode", "")),
        "primary_subject_angle": str(payload.get("primary_subject_angle", "")),
        "visible_primary_subject_id": str(payload.get("visible_primary_subject_id", "")),
        "visible_secondary_subject_ids": _coerce_string_list(payload.get("visible_secondary_subject_ids", [])),
        "primary_subject_frame_position": str(payload.get("primary_subject_frame_position", "")),
        "primary_subject_scale_relation": str(payload.get("primary_subject_scale_relation", "")),
        "primary_subject_facing_direction": str(payload.get("primary_subject_facing_direction", "")),
        "primary_subject_pose_description": str(payload.get("primary_subject_pose_description", "")),
        "subject_relation_summary": str(payload.get("subject_relation_summary", "")),
        "required_environment_anchor_1": str(payload.get("required_environment_anchor_1", "")),
        "required_scale_proof_detail": str(payload.get("required_scale_proof_detail", "")),
        "camera_package_description": str(payload.get("camera_package_description", "")),
        "camera_description": str(payload.get("camera_description", "")),
        "composition": str(payload.get("composition", "")),
        "target_seconds": _coerce_float(payload.get("target_seconds"), payload.get("estimated_seconds"), fallback=0.0) or None,
        "beat_ids": _coerce_string_list(payload.get("beat_ids", [])),
        "subject_blocking": _coerce_string_list(payload.get("subject_blocking", [])),
        "camera_relative_positions": _coerce_string_list(payload.get("camera_relative_positions", [])),
        "gaze_directions": _coerce_string_list(payload.get("gaze_directions", [])),
        "environment_subzone": str(payload.get("environment_subzone", "")),
        "key_visible_environment_features": _coerce_string_list(payload.get("key_visible_environment_features", [])),
        "continuity_from_previous_shot": str(payload.get("continuity_from_previous_shot", "")),
        "continuity_to_next_shot": str(payload.get("continuity_to_next_shot", "")),
        "pose_anchor_frame": str(payload.get("pose_anchor_frame", "")),
        "pose_end_frame": str(payload.get("pose_end_frame", "")),
        "characters_in_frame": [item for item in payload.get("characters_in_frame", []) if isinstance(item, dict)],
        "environment": payload.get("environment", {}) if isinstance(payload.get("environment"), dict) else {},
        "continuity_constraints": _coerce_string_list(payload.get("continuity_constraints", [])),
        "prompt_seed": str(payload.get("prompt_seed", "")),
        "shot_notes": str(payload.get("shot_notes", "")),
    }


def _shot_package_metadata(existing: dict | None, artifact_id: str, fp: str) -> ShotPackageMetadata:
    old_meta = (existing or {}).get("metadata") or {}
    return ShotPackageMetadata(
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


def _merge_with_existing(new: dict[str, Any], existing: dict | None, metadata: ShotPackageMetadata) -> dict[str, Any]:
    if not existing:
        return new

    merged = dict(new)
    for field_name, locked in metadata.locked_fields.items():
        if locked and field_name in existing:
            merged[field_name] = existing[field_name]

    for field_name, value in metadata.manual_overrides.items():
        merged[field_name] = value

    return merged


def _is_film_facing_shot(package: ShotPackage) -> bool:
    if not package.prompt_seed or len(package.prompt_seed) < 40:
        return False
    if package.shot_type in {"shot", "generic"}:
        return False
    if not package.camera_description or not package.composition:
        return False
    return True


def _shot_needs_review(package: ShotPackage) -> bool:
    if package.environment is None or package.environment.status != "canonical" or not package.environment.canonical_id:
        return True
    unresolved_cast = [ref for ref in package.characters_in_frame if ref.status not in {"canonical", "group"} or not ref.canonical_id]
    if unresolved_cast:
        return True
    if package.shot_type in {"shot", "generic"}:
        return True
    if not package.prompt_seed or len(package.prompt_seed) < 40:
        return True
    if not all(
        [
            package.shot_size,
            package.camera_angle,
            package.lens_family,
            package.camera_motion,
            package.focus_strategy,
            package.lighting_style,
            package.subject_visibility,
            package.narration_mode,
        ]
    ):
        return True
    if not all(
        [
            package.visible_primary_subject_id,
            package.primary_subject_frame_position,
            package.primary_subject_scale_relation,
            package.primary_subject_facing_direction or package.subject_visibility == "off_screen_voice",
            package.primary_subject_pose_description,
            package.required_environment_anchor_1,
            package.camera_package_description,
        ]
    ):
        return True
    normalized_primary = package.primary_subject.strip().lower()
    if normalized_primary == "the narrator" and (
        package.subject_visibility != "off_screen_voice" or package.narration_mode != "voiceover_off_screen"
    ):
        return True
    placeholder_markers = {
        "primary scene playing area",
        "continue the established scene action.",
        "arrive at the scene's transition point.",
        "[]",
        "subject remains readable",
    }
    text_fields = [
        package.start_state,
        package.end_state,
        package.action_during_shot,
        package.action_continues_from,
        package.action_hands_off_to,
        package.pose_anchor_frame,
        package.pose_end_frame,
        package.environment_subzone,
        package.primary_subject_frame_position,
        package.primary_subject_scale_relation,
        package.subject_relation_summary,
        package.required_environment_anchor_1,
    ]
    normalized_texts = [" ".join(text.lower().split()) for text in text_fields if isinstance(text, str) and text.strip()]
    if any(any(marker in text for marker in placeholder_markers) for text in normalized_texts):
        return True
    repeated = {text for text in normalized_texts if normalized_texts.count(text) >= 4}
    if repeated:
        return True
    return False


def _render_shot_package_markdown(package: ShotPackage) -> str:
    characters = package.characters_in_frame or []
    environment = package.environment or ShotReference(label="environment", display_name="environment", status="review", entity_kind="environment")
    lines = [
        f"# Shot Package: {package.shot_title}",
        "",
        f"- shot_id: `{package.shot_id}`",
        f"- scene_id: `{package.scene_id}`",
        f"- chapter_id: `{package.chapter_id}`",
        f"- shot_order: `{package.shot_order}`",
        f"- previous_shot_id: `{package.previous_shot_id or '(none)'}`",
        f"- next_shot_id: `{package.next_shot_id or '(none)'}`",
        f"- shot_type: `{package.shot_type}`",
        f"- shot_size: `{package.shot_size or '(none)'}`",
        f"- camera_angle: `{package.camera_angle or '(none)'}`",
        f"- lens_family: `{package.lens_family or '(none)'}`",
        f"- camera_motion: `{package.camera_motion or '(none)'}`",
        f"- zoom_behavior: `{package.zoom_behavior or '(none)'}`",
        f"- focus_strategy: `{package.focus_strategy or '(none)'}`",
        f"- lighting_style: `{package.lighting_style or '(none)'}`",
        f"- subject_visibility: `{package.subject_visibility or '(none)'}`",
        f"- narration_mode: `{package.narration_mode or '(none)'}`",
        f"- primary_subject_angle: `{package.primary_subject_angle or '(none)'}`",
        f"- visible_primary_subject_id: `{package.visible_primary_subject_id or '(none)'}`",
        f"- target_seconds: `{package.target_seconds}`",
        "",
        "## Camera",
        "",
        package.camera_description or "(none)",
        "",
        "## Prompt Variables",
        "",
        f"- primary_subject_frame_position: {package.primary_subject_frame_position or '(none)'}",
        f"- primary_subject_scale_relation: {package.primary_subject_scale_relation or '(none)'}",
        f"- primary_subject_facing_direction: {package.primary_subject_facing_direction or '(none)'}",
        f"- primary_subject_pose_description: {package.primary_subject_pose_description or '(none)'}",
        f"- subject_relation_summary: {package.subject_relation_summary or '(none)'}",
        f"- required_environment_anchor_1: {package.required_environment_anchor_1 or '(none)'}",
        f"- required_scale_proof_detail: {package.required_scale_proof_detail or '(none)'}",
        f"- camera_package_description: {package.camera_package_description or '(none)'}",
        "",
        "## Composition",
        "",
        package.composition or "(none)",
        "",
        "## Action State",
        "",
        f"- primary_subject: {package.primary_subject or '(none)'}",
        f"- shot_moment_summary: {package.shot_moment_summary or '(none)'}",
        f"- start_state: {package.start_state or '(none)'}",
        f"- end_state: {package.end_state or '(none)'}",
        f"- action_during_shot: {package.action_during_shot or '(none)'}",
        f"- action_continues_from: {package.action_continues_from or '(none)'}",
        f"- action_hands_off_to: {package.action_hands_off_to or '(none)'}",
        "",
        "## Blocking",
        "",
    ]
    if package.subject_blocking:
        lines.extend([f"- {item}" for item in package.subject_blocking])
    else:
        lines.append("- (none)")
    lines.extend(
        [
            "",
            "## Camera Relation",
            "",
        ]
    )
    if package.camera_relative_positions:
        lines.extend([f"- {item}" for item in package.camera_relative_positions])
    else:
        lines.append("- (none)")
    lines.extend(
        [
            "",
            "## Posing",
            "",
            f"- pose_anchor_frame: {package.pose_anchor_frame or '(none)' }",
            f"- pose_end_frame: {package.pose_end_frame or '(none)' }",
            "",
        "## Characters",
        "",
        ]
    )
    if characters:
        lines.extend([f"- {ref.display_name or ref.label} (`{ref.canonical_id or ref.label}`)" for ref in characters])
    else:
        lines.append("- (none)")
    if package.visible_secondary_subject_ids:
        lines.extend(["", "### Visible Secondary Subject IDs", ""])
        lines.extend([f"- `{item}`" for item in package.visible_secondary_subject_ids])
    lines.extend(
        [
            "",
            "## Environment",
            "",
            f"- {environment.display_name or environment.label} (`{environment.canonical_id or environment.label}`)",
            f"- subzone: {package.environment_subzone or '(none)' }",
            "",
            "## Continuity",
            "",
        ]
    )
    if package.continuity_constraints:
        lines.extend([f"- {item}" for item in package.continuity_constraints])
    else:
        lines.append("- (none)")
    lines.extend(
        [
            "",
            "## Prompt Seed",
            "",
            package.prompt_seed or "(none)",
            "",
            "## Evidence Summary",
            "",
        ]
    )
    if package.evidence_summary:
        lines.extend([f"- {item}" for item in package.evidence_summary])
    else:
        lines.append("- (none)")
    lines.extend(["", "## Metadata", ""])
    if package.metadata:
        lines.extend(
            [
                f"- artifact_id: `{package.metadata.artifact_id}`",
                f"- status: `{package.metadata.status}`",
                f"- source_fingerprint: `{package.metadata.source_fingerprint}`",
                f"- created_at_utc: `{package.metadata.created_at_utc}`",
                f"- updated_at_utc: `{package.metadata.updated_at_utc}`",
            ]
        )
    return "\n".join(lines) + "\n"


def _write_shot_package_files(base_path: Path, package: ShotPackage) -> None:
    write_json(base_path.with_suffix(".json"), package.to_dict())
    base_path.with_suffix(".md").write_text(_render_shot_package_markdown(package), encoding="utf-8")


def _apply_shot_lineage(records: list[ShotPackage]) -> None:
    ordered = sorted(records, key=lambda item: item.shot_order)
    for index, record in enumerate(ordered):
        record.previous_shot_id = ordered[index - 1].shot_id if index > 0 else ""
        record.next_shot_id = ordered[index + 1].shot_id if index + 1 < len(ordered) else ""


def _render_scene_shot_index(records: list[ShotPackage]) -> str:
    lines = ["# Shot Index", ""]
    if not records:
        lines.append("- No shot packages.")
        return "\n".join(lines) + "\n"
    for record in sorted(records, key=lambda item: item.shot_order):
        env_name = record.environment.display_name if record.environment else "(none)"
        lines.append(
            f"- `{record.shot_id}` - {record.shot_title} "
            f"(type={record.shot_type}, target={record.target_seconds:.1f}s, beat_ids={', '.join(record.beat_ids) or '(none)'}, cast={len(record.characters_in_frame)}, env={env_name}, "
            f"prev={record.previous_shot_id or '(none)'}, next={record.next_shot_id or '(none)'})"
        )
    return "\n".join(lines) + "\n"


def _render_shot_package_index(records: list[ShotPackage]) -> str:
    lines = ["# Shot Package Index", ""]
    if not records:
        lines.append("- No shot packages.")
        return "\n".join(lines) + "\n"
    for record in sorted(records, key=lambda item: (item.scene_id, item.shot_order, item.shot_id)):
        lines.append(
            f"- `{record.scene_id}/{record.shot_id}` - {record.shot_title} "
            f"(type={record.shot_type}, target={record.target_seconds:.1f}s, cast={len(record.characters_in_frame)}, env={record.environment.display_name if record.environment else '(none)'}, "
            f"prev={record.previous_shot_id or '(none)'}, next={record.next_shot_id or '(none)'})"
        )
    return "\n".join(lines) + "\n"


def _render_shot_package_review_index(records: list[ShotPackage]) -> str:
    lines = ["# Shot Package Review Index", ""]
    if not records:
        lines.append("- No review entries.")
        return "\n".join(lines) + "\n"
    for record in sorted(records, key=lambda item: (item.scene_id, item.shot_order, item.shot_id)):
        flags: list[str] = []
        if record.environment is None or record.environment.status != "canonical" or not record.environment.canonical_id:
            flags.append("environment_review")
        unresolved_cast = [ref for ref in record.characters_in_frame if ref.status not in {"canonical", "group"} or not ref.canonical_id]
        if unresolved_cast:
            flags.append(f"cast_review={len(unresolved_cast)}")
        if record.shot_type in {"medium", "shot", "generic"}:
            flags.append(f"shot_type={record.shot_type}")
        if not record.prompt_seed or len(record.prompt_seed) < 40:
            flags.append("thin_prompt")
        flags.append(f"target={record.target_seconds:.1f}s")
        lines.append(f"- `{record.scene_id}/{record.shot_id}` - {record.shot_title} ({', '.join(flags) if flags else 'review'})")
    return "\n".join(lines) + "\n"


def _render_review_queue_markdown(queue: list[dict[str, Any]]) -> str:
    lines = ["# Shot Package Review Queue", ""]
    if not queue:
        lines.append("- No shot review items.")
        return "\n".join(lines) + "\n"
    for item in queue:
        lines.append(f"- `{item.get('shot_id')}` / `{item.get('scene_id')}`")
        for issue in item.get("issues", []):
            lines.append(f"  - {issue}")
    return "\n".join(lines) + "\n"


def _ordered_unique(values: list[str]) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []
    for value in values:
        if value in seen:
            continue
        seen.add(value)
        ordered.append(value)
    return ordered


def run_shot_planning(
    project_slug: str,
    *,
    use_llm: bool = True,
    force: bool = False,
    chapters: str | None = None,
    run_tracker: "DownstreamRunTracker | None" = None,
) -> ShotPlanningSummary:
    project_dir = create_project(project_slug)
    selected_chapters = set(parse_chapter_selector(chapters))
    scene_contract_files = [
        path for path in _scene_contract_files(project_dir) if chapter_matches(path.parent.name or path.stem[:5], selected_chapters)
    ]

    output_root = _shot_package_root(project_dir)
    review_dir = output_root / "review"
    output_root.mkdir(parents=True, exist_ok=True)
    review_dir.mkdir(parents=True, exist_ok=True)

    synthesized = 0
    reused = 0
    stale_locked = 0
    review_queue: list[dict[str, Any]] = []
    written_files: list[str] = []
    warnings: list[str] = []
    shot_records: list[ShotPackage] = []
    review_records: list[ShotPackage] = []
    total_scenes = len(scene_contract_files)
    phase_name = "shot_packages"
    if run_tracker is not None:
        run_tracker.set_phase_total(phase_name, total_scenes)

    for scene_index, scene_contract_path in enumerate(scene_contract_files, start=1):
        scene_started_at = time.perf_counter()
        scene_contract = _load_json_file(scene_contract_path)
        scene_id = str(scene_contract.get("scene_id", "")).strip().upper() or scene_contract_path.stem.upper()
        chapter_id = str(scene_contract.get("chapter_id", "")).strip().upper() or _chapter_id_from_scene_id(scene_id)
        scene_title = _scene_contract_to_scene_title(scene_contract)
        scene_binding = _load_scene_binding(project_dir, scene_id)
        scene_dir = output_root / chapter_id / scene_id
        scene_dir.mkdir(parents=True, exist_ok=True)
        print(f"[shot-planner] {scene_index}/{total_scenes} starting {scene_id}...")

        shot_blueprints = _build_shot_blueprints(scene_contract, project_dir, scene_binding=scene_binding)
        evidence = _load_shot_planning_evidence(
            project_dir=project_dir,
            scene_contract=scene_contract,
            scene_binding=scene_binding,
            shot_blueprints=shot_blueprints,
        )
        fp = _fingerprint(evidence["fingerprint_payload"])

        scene_shots: list[ShotPackage] = []
        scene_review_shots: list[ShotPackage] = []
        scene_written_files: list[str] = []
        total_shots = len(shot_blueprints)

        for shot_index, blueprint in enumerate(shot_blueprints, start=1):
            shot_id = str(blueprint.get("shot_id", "")).strip().upper()
            if not shot_id:
                continue
            shot_started_at = time.perf_counter()
            print(f"[shot-planner] {scene_index}/{total_scenes} {shot_index}/{total_shots} starting {scene_id}/{shot_id}...")
            estimated_seconds = _estimate_shot_seconds(str(blueprint.get("shot_type", "")), shot_index, total_shots)
            base_path = scene_dir / shot_id
            existing = read_json(base_path.with_suffix(".json")) if base_path.with_suffix(".json").exists() else None
            metadata = _shot_package_metadata(existing, artifact_id=f"{scene_id}_{shot_id}_SHOT_PACKAGE", fp=fp)
            item_id = f"{scene_id}/{shot_id}"
            old_meta = existing.get("metadata") or {} if isinstance(existing, dict) else {}

            if existing and old_meta.get("status") == "locked" and not (run_tracker is not None and run_tracker.is_item_completed(phase_name, item_id, fp)):
                stale_locked += 1
                existing["metadata"]["status"] = "stale"
                write_json(base_path.with_suffix(".json"), existing)
                warnings.append(f"Locked shot package became stale and was not regenerated: {scene_id}/{shot_id}")
                elapsed = round(time.perf_counter() - shot_started_at, 1)
                print(f"[shot-planner] {scene_index}/{total_scenes} {shot_index}/{total_shots} finished {scene_id}/{shot_id} (stale locked) in {elapsed}s")
                continue

            if run_tracker is not None and run_tracker.is_item_completed(phase_name, item_id, fp) and existing:
                reused += 1
                package = _package_from_existing(existing, metadata)
                shot_records.append(package)
                scene_shots.append(package)
                if _shot_needs_review(package):
                    review_records.append(package)
                    scene_review_shots.append(package)
                    _append_shot_review_item(review_queue, package)
                elapsed = round(time.perf_counter() - shot_started_at, 1)
                print(f"[shot-planner] {scene_index}/{total_scenes} {shot_index}/{total_shots} finished {scene_id}/{shot_id} (resumed) in {elapsed}s")
                continue

            if existing and not force and run_tracker is None:
                if old_meta.get("source_fingerprint") == fp:
                    reused += 1
                    package = _package_from_existing(existing, metadata)
                    shot_records.append(package)
                    scene_shots.append(package)
                    if _shot_needs_review(package):
                        review_records.append(package)
                        scene_review_shots.append(package)
                        _append_shot_review_item(review_queue, package)
                    elapsed = round(time.perf_counter() - shot_started_at, 1)
                    print(f"[shot-planner] {scene_index}/{total_scenes} {shot_index}/{total_shots} finished {scene_id}/{shot_id} (reused) in {elapsed}s")
                    continue

                if old_meta.get("status") == "locked":
                    stale_locked += 1
                    existing["metadata"]["status"] = "stale"
                    write_json(base_path.with_suffix(".json"), existing)
                    warnings.append(f"Locked shot package became stale and was not regenerated: {scene_id}/{shot_id}")
                    elapsed = round(time.perf_counter() - shot_started_at, 1)
                    print(f"[shot-planner] {scene_index}/{total_scenes} {shot_index}/{total_shots} finished {scene_id}/{shot_id} (stale locked) in {elapsed}s")
                    continue

            synthesized_payload = _llm_synthesis(
                project_slug=project_slug,
                scene_contract=scene_contract,
                shot_blueprints=shot_blueprints,
                evidence=evidence,
            ) if use_llm else None
            if not synthesized_payload:
                synthesized_payload = shot_blueprints
                if use_llm:
                    warnings.append(f"LLM synthesis failed or returned invalid packet for {scene_id}; used deterministic fallback.")

            if len(synthesized_payload) != len(shot_blueprints):
                synthesized_payload = shot_blueprints
                warnings.append(f"Shot planning for {scene_id} did not preserve blueprint count; used deterministic fallback.")

            blueprint_payload = _parse_shot_plan_blueprint(next((item for item in synthesized_payload if item.get("shot_id") == shot_id), blueprint))
            if not blueprint_payload.get("shot_order"):
                blueprint_payload["shot_order"] = int(blueprint.get("shot_order", 0) or 0)
            if not blueprint_payload.get("shot_title"):
                blueprint_payload["shot_title"] = str(blueprint.get("shot_title", ""))
            if not blueprint_payload.get("shot_type"):
                blueprint_payload["shot_type"] = str(blueprint.get("shot_type", "medium"))
            for key in [
                "shot_moment_summary",
                "primary_subject",
                "start_state",
                "end_state",
                "action_during_shot",
                "action_continues_from",
                "action_hands_off_to",
                "shot_size",
                "camera_angle",
                "lens_family",
                "camera_motion",
                "zoom_behavior",
                "focus_strategy",
                "lighting_style",
                "subject_visibility",
                "narration_mode",
                "primary_subject_angle",
                "visible_primary_subject_id",
                "primary_subject_frame_position",
                "primary_subject_scale_relation",
                "primary_subject_facing_direction",
                "primary_subject_pose_description",
                "subject_relation_summary",
                "required_environment_anchor_1",
                "required_scale_proof_detail",
                "camera_package_description",
                "environment_subzone",
                "continuity_from_previous_shot",
                "continuity_to_next_shot",
                "pose_anchor_frame",
                "pose_end_frame",
            ]:
                if not blueprint_payload.get(key):
                    blueprint_payload[key] = str(blueprint.get(key, ""))
            for key in [
                "secondary_subjects",
                "visible_secondary_subject_ids",
                "subject_blocking",
                "camera_relative_positions",
                "gaze_directions",
                "key_visible_environment_features",
            ]:
                if not blueprint_payload.get(key):
                    blueprint_payload[key] = _coerce_string_list(blueprint.get(key, []))
            if not blueprint_payload.get("camera_description"):
                blueprint_payload["camera_description"] = str(blueprint.get("camera_description", ""))
            if not blueprint_payload.get("composition"):
                blueprint_payload["composition"] = str(blueprint.get("composition", ""))
            if not blueprint_payload.get("prompt_seed"):
                blueprint_payload["prompt_seed"] = str(blueprint.get("prompt_seed", ""))
            if not blueprint_payload.get("shot_notes"):
                blueprint_payload["shot_notes"] = str(blueprint.get("shot_notes", ""))
            if not blueprint_payload.get("beat_ids"):
                blueprint_payload["beat_ids"] = _coerce_string_list(blueprint.get("beat_ids", []))
            if not blueprint_payload.get("continuity_constraints"):
                blueprint_payload["continuity_constraints"] = _coerce_string_list(blueprint.get("continuity_constraints", []))
            if not blueprint_payload.get("characters_in_frame"):
                blueprint_payload["characters_in_frame"] = [item for item in blueprint.get("characters_in_frame", []) if isinstance(item, dict)]
            if not blueprint_payload.get("environment") and isinstance(blueprint.get("environment"), dict):
                blueprint_payload["environment"] = blueprint.get("environment", {})
            merged = _merge_with_existing(blueprint_payload, existing, metadata)

            metadata.upstream_dependencies = [
                {
                    "dependency_type": "scene_contract",
                    "dependency_id": scene_id,
                    "version": _fingerprint(scene_contract),
                },
                {
                    "dependency_type": "scene_binding",
                    "dependency_id": scene_id,
                    "version": _fingerprint(scene_binding or {}),
                },
                {
                    "dependency_type": "shot_blueprints",
                    "dependency_id": scene_id,
                    "version": _fingerprint(shot_blueprints),
                },
            ]
            metadata.revision_history.append(
                {
                    "timestamp_utc": _utc_now(),
                    "action": "synthesized",
                    "source_fingerprint": fp,
                }
            )

            environment_payload = merged.get("environment", {}) if isinstance(merged.get("environment"), dict) else {}
            environment_canonical_id = str(environment_payload.get("canonical_id", "")).strip()
            if environment_canonical_id.lower() in {"none", "null", "(none)"}:
                environment_canonical_id = ""
            environment_status = str(environment_payload.get("status", "review"))
            environment_source_path = str(environment_payload.get("source_path", ""))
            if not environment_canonical_id or environment_status != "canonical":
                environment_source_path = ""
            environment_ref = ShotReference(
                label=_clean_label(environment_payload.get("label"), fallback="environment"),
                canonical_id=(environment_canonical_id or None),
                display_name=_clean_label(
                    environment_payload.get("display_name"),
                    fallback=_clean_label(environment_payload.get("label"), fallback="environment"),
                ),
                status=environment_status,
                entity_kind=str(environment_payload.get("entity_kind", "environment")),
                resolution_score=environment_payload.get("resolution_score"),
                source_path=environment_source_path,
                notes=str(environment_payload.get("notes", "")),
            )
            character_payloads = merged.get("characters_in_frame", [])
            character_refs = [ShotReference(**item) for item in character_payloads if isinstance(item, dict)]

            package = ShotPackage(
                shot_id=shot_id,
                scene_id=scene_id,
                chapter_id=chapter_id,
                shot_order=int(merged.get("shot_order", len(scene_shots) + 1) or len(scene_shots) + 1),
                primary_subject=_first_nonempty(merged.get("primary_subject"), fallback=""),
                secondary_subjects=_coerce_string_list(merged.get("secondary_subjects", [])),
                shot_moment_summary=_first_nonempty(merged.get("shot_moment_summary"), fallback=""),
                start_state=_first_nonempty(merged.get("start_state"), fallback=""),
                end_state=_first_nonempty(merged.get("end_state"), fallback=""),
                action_during_shot=_first_nonempty(merged.get("action_during_shot"), fallback=""),
                action_continues_from=_first_nonempty(merged.get("action_continues_from"), fallback=""),
                action_hands_off_to=_first_nonempty(merged.get("action_hands_off_to"), fallback=""),
                shot_size=_normalize_enum(
                    merged.get("shot_size"),
                    SHOT_SIZE_ENUM,
                    fallback=_normalize_enum(blueprint.get("shot_size"), SHOT_SIZE_ENUM, fallback="medium"),
                ),
                camera_angle=_normalize_enum(
                    merged.get("camera_angle"),
                    CAMERA_ANGLE_ENUM,
                    fallback=_normalize_enum(blueprint.get("camera_angle"), CAMERA_ANGLE_ENUM, fallback="eye_level"),
                ),
                lens_family=_normalize_enum(
                    merged.get("lens_family"),
                    LENS_FAMILY_ENUM,
                    fallback=_normalize_enum(blueprint.get("lens_family"), LENS_FAMILY_ENUM, fallback="normal"),
                ),
                camera_motion=_normalize_enum(
                    merged.get("camera_motion"),
                    CAMERA_MOTION_ENUM,
                    fallback=_normalize_enum(blueprint.get("camera_motion"), CAMERA_MOTION_ENUM, fallback="locked_off"),
                ),
                zoom_behavior=_normalize_enum(
                    merged.get("zoom_behavior"),
                    ZOOM_BEHAVIOR_ENUM,
                    fallback=_normalize_enum(blueprint.get("zoom_behavior"), ZOOM_BEHAVIOR_ENUM, fallback="none"),
                ),
                focus_strategy=_normalize_enum(
                    merged.get("focus_strategy"),
                    FOCUS_STRATEGY_ENUM,
                    fallback=_normalize_enum(blueprint.get("focus_strategy"), FOCUS_STRATEGY_ENUM, fallback="deep_focus"),
                ),
                lighting_style=_normalize_enum(
                    merged.get("lighting_style"),
                    LIGHTING_STYLE_ENUM,
                    fallback=_normalize_enum(blueprint.get("lighting_style"), LIGHTING_STYLE_ENUM, fallback="hard_directional"),
                ),
                subject_visibility=_normalize_enum(
                    merged.get("subject_visibility"),
                    SUBJECT_VISIBILITY_ENUM,
                    fallback=_normalize_enum(blueprint.get("subject_visibility"), SUBJECT_VISIBILITY_ENUM, fallback="on_screen"),
                ),
                narration_mode=_normalize_enum(
                    merged.get("narration_mode"),
                    NARRATION_MODE_ENUM,
                    fallback=_normalize_enum(blueprint.get("narration_mode"), NARRATION_MODE_ENUM, fallback="none"),
                ),
                primary_subject_angle=_normalize_enum(
                    merged.get("primary_subject_angle"),
                    PRIMARY_SUBJECT_ANGLE_ENUM,
                    fallback=_normalize_enum(blueprint.get("primary_subject_angle"), PRIMARY_SUBJECT_ANGLE_ENUM, fallback=""),
                ),
                visible_primary_subject_id=_first_nonempty(merged.get("visible_primary_subject_id"), fallback=""),
                visible_secondary_subject_ids=_coerce_string_list(merged.get("visible_secondary_subject_ids", [])),
                primary_subject_frame_position=_first_nonempty(merged.get("primary_subject_frame_position"), fallback=""),
                primary_subject_scale_relation=_first_nonempty(merged.get("primary_subject_scale_relation"), fallback=""),
                primary_subject_facing_direction=_first_nonempty(merged.get("primary_subject_facing_direction"), fallback=""),
                primary_subject_pose_description=_first_nonempty(merged.get("primary_subject_pose_description"), fallback=""),
                subject_relation_summary=_first_nonempty(merged.get("subject_relation_summary"), fallback=""),
                required_environment_anchor_1=_first_nonempty(merged.get("required_environment_anchor_1"), fallback=""),
                required_scale_proof_detail=_first_nonempty(merged.get("required_scale_proof_detail"), fallback=""),
                camera_package_description=_first_nonempty(merged.get("camera_package_description"), fallback=""),
                shot_title=_first_nonempty(merged.get("shot_title"), fallback=f"{scene_title} {shot_id}"),
                shot_type=_first_nonempty(merged.get("shot_type"), fallback="medium"),
                camera_description=_first_nonempty(merged.get("camera_description"), fallback="Stable readable framing."),
                composition=_first_nonempty(merged.get("composition"), fallback="Readable composition."),
                target_seconds=_coerce_float(merged.get("target_seconds"), estimated_seconds, fallback=estimated_seconds or 5.0),
                subject_blocking=_coerce_string_list(merged.get("subject_blocking", [])),
                camera_relative_positions=_coerce_string_list(merged.get("camera_relative_positions", [])),
                gaze_directions=_coerce_string_list(merged.get("gaze_directions", [])),
                environment_subzone=_first_nonempty(merged.get("environment_subzone"), fallback=""),
                key_visible_environment_features=_coerce_string_list(merged.get("key_visible_environment_features", [])),
                continuity_from_previous_shot=_first_nonempty(merged.get("continuity_from_previous_shot"), fallback=""),
                continuity_to_next_shot=_first_nonempty(merged.get("continuity_to_next_shot"), fallback=""),
                pose_anchor_frame=_first_nonempty(merged.get("pose_anchor_frame"), fallback=""),
                pose_end_frame=_first_nonempty(merged.get("pose_end_frame"), fallback=""),
                characters_in_frame=character_refs,
                environment=environment_ref,
                beat_ids=_coerce_string_list(merged.get("beat_ids", [])) or [shot_id.replace("SH", "BT")],
                continuity_constraints=_coerce_string_list(merged.get("continuity_constraints", [])),
                prompt_seed=_first_nonempty(merged.get("prompt_seed"), fallback=""),
                shot_notes=_first_nonempty(merged.get("shot_notes"), fallback=""),
                evidence_refs=[
                    {
                        "source": "scene_contract",
                        "scene_id": scene_id,
                    },
                    *scene_contract.get("evidence_refs", []),
                ],
                evidence_summary=[
                    *evidence["scene_evidence"],
                    *evidence["character_evidence"],
                    *evidence["environment_evidence"],
                ],
                metadata=metadata,
            )

            package.prompt_seed = package.prompt_seed or _prompt_seed(
                shot_title=package.shot_title,
                shot_type=package.shot_type,
                camera_description=package.camera_description,
                composition=" ".join(
                    item
                    for item in [
                        package.composition,
                        package.start_state,
                        package.end_state,
                        " ".join(package.subject_blocking),
                        package.environment_subzone,
                    ]
                    if item
                ),
                characters=package.characters_in_frame,
                environment=package.environment or environment_ref,
                beat_summary=" ".join(item for item in [package.action_during_shot, package.continuity_to_next_shot] if item) or _first_nonempty(scene_contract.get("summary", ""), scene_contract.get("production_intent", ""), fallback=""),
                shot_size=package.shot_size,
                camera_angle=package.camera_angle,
                lens_family=package.lens_family,
                camera_motion=package.camera_motion,
                zoom_behavior=package.zoom_behavior,
                focus_strategy=package.focus_strategy,
                lighting_style=package.lighting_style,
                subject_visibility=package.subject_visibility,
                primary_subject_angle=package.primary_subject_angle or "unspecified",
            )
            package.visible_primary_subject_id = package.visible_primary_subject_id or _visible_primary_subject_id(
                package.primary_subject,
                package.characters_in_frame,
                package.subject_visibility,
            )
            package.visible_secondary_subject_ids = package.visible_secondary_subject_ids or _visible_secondary_subject_ids(
                package.visible_primary_subject_id,
                package.characters_in_frame,
            )
            package.primary_subject_frame_position = package.primary_subject_frame_position or _primary_subject_frame_position(
                package.shot_size,
                package.environment_subzone,
                package.subject_visibility,
                package.shot_order,
            )
            package.primary_subject_scale_relation = package.primary_subject_scale_relation or _primary_subject_scale_relation(
                scene_contract,
                blueprint,
                package.environment or environment_ref,
            )
            package.primary_subject_facing_direction = package.primary_subject_facing_direction or _angle_to_facing_direction(
                package.primary_subject_angle,
                package.subject_visibility,
            )
            package.primary_subject_pose_description = package.primary_subject_pose_description or _first_nonempty(
                package.pose_anchor_frame,
                package.start_state,
                package.action_during_shot,
                fallback="",
            )
            package.subject_relation_summary = package.subject_relation_summary or _subject_relation_summary(
                package.primary_subject,
                package.secondary_subjects,
                package.subject_visibility,
            )
            package.required_environment_anchor_1 = package.required_environment_anchor_1 or _first_nonempty(
                package.key_visible_environment_features[0] if package.key_visible_environment_features else "",
                package.environment_subzone,
                fallback="",
            )
            package.required_scale_proof_detail = package.required_scale_proof_detail or package.primary_subject_scale_relation
            package.camera_package_description = package.camera_package_description or _camera_package_description(
                package.shot_size,
                package.camera_angle,
                package.lens_family,
                package.camera_motion,
                package.zoom_behavior,
                package.focus_strategy,
                package.lighting_style,
            )
            package.shot_notes = package.shot_notes or _compact_snippet(str(scene_contract.get("summary", "")), limit=220)

            _write_shot_package_files(base_path, package)
            scene_written_files.extend([str(base_path.with_suffix(".json")), str(base_path.with_suffix(".md"))])
            written_files.extend([str(base_path.with_suffix(".json")), str(base_path.with_suffix(".md"))])
            if run_tracker is not None:
                run_tracker.mark_item_completed(
                    phase_name,
                    item_id,
                    fp,
                    outputs=[str(base_path.with_suffix(".json")), str(base_path.with_suffix(".md"))],
                )
            synthesized += 1
            shot_records.append(package)
            scene_shots.append(package)

            if _shot_needs_review(package):
                review_records.append(package)
                scene_review_shots.append(package)
                _append_shot_review_item(review_queue, package)

            elapsed = round(time.perf_counter() - shot_started_at, 1)
            mode = "synthesized" if synthesized_payload else "generated"
            print(f"[shot-planner] {scene_index}/{total_scenes} {shot_index}/{total_shots} finished {scene_id}/{shot_id} ({mode}) in {elapsed}s")

        _apply_shot_lineage(scene_shots)
        for package in scene_shots:
            base_path = scene_dir / package.shot_id / package.shot_id
            _write_shot_package_files(base_path, package)

        scene_index_path = scene_dir / "SHOT_INDEX.md"
        write_json(scene_dir / "SHOT_INDEX.json", [package.to_dict() for package in sorted(scene_shots, key=lambda item: item.shot_order)])
        scene_index_path.write_text(_render_scene_shot_index(scene_shots), encoding="utf-8")
        written_files.extend([str(scene_dir / "SHOT_INDEX.json"), str(scene_index_path)])
        if scene_review_shots:
            review_path = scene_dir / "SHOT_REVIEW_INDEX.md"
            review_path.write_text(_render_scene_shot_index(scene_review_shots), encoding="utf-8")
            written_files.append(str(review_path))

        scene_elapsed = round(time.perf_counter() - scene_started_at, 1)
        print(f"[shot-planner] {scene_index}/{total_scenes} finished {scene_id} in {scene_elapsed}s")

    write_json(review_dir / "SHOT_PACKAGE_REVIEW_QUEUE.json", review_queue)
    (review_dir / "SHOT_PACKAGE_REVIEW_QUEUE.md").write_text(_render_review_queue_markdown(review_queue), encoding="utf-8")

    main_records = [record for record in shot_records if _is_film_facing_shot(record)]
    write_json(
        output_root / "SHOT_PACKAGE_INDEX.json",
        [record.to_dict() for record in sorted(main_records, key=lambda item: (item.scene_id, item.shot_order, item.shot_id))],
    )
    (output_root / "SHOT_PACKAGE_INDEX.md").write_text(_render_shot_package_index(main_records), encoding="utf-8")
    write_json(
        output_root / "SHOT_PACKAGE_REVIEW_INDEX.json",
        [record.to_dict() for record in sorted(review_records, key=lambda item: (item.scene_id, item.shot_order, item.shot_id))],
    )
    (output_root / "SHOT_PACKAGE_REVIEW_INDEX.md").write_text(_render_shot_package_review_index(review_records), encoding="utf-8")

    written_files.extend(
        [
            str(review_dir / "SHOT_PACKAGE_REVIEW_QUEUE.json"),
            str(review_dir / "SHOT_PACKAGE_REVIEW_QUEUE.md"),
            str(output_root / "SHOT_PACKAGE_INDEX.json"),
            str(output_root / "SHOT_PACKAGE_INDEX.md"),
            str(output_root / "SHOT_PACKAGE_REVIEW_INDEX.json"),
            str(output_root / "SHOT_PACKAGE_REVIEW_INDEX.md"),
        ]
    )

    return ShotPlanningSummary(
        project_slug=project_slug,
        total_scene_entries=len(scene_contract_files),
        total_shot_entries=len(shot_records),
        synthesized_count=synthesized,
        reused_count=reused,
        stale_locked_count=stale_locked,
        review_queue_count=len(review_queue),
        written_files=written_files,
        warnings=warnings,
    )


def _package_from_existing(existing: dict[str, Any], metadata: ShotPackageMetadata) -> ShotPackage:
    environment_payload = existing.get("environment", {}) if isinstance(existing.get("environment"), dict) else {}
    environment_canonical_id = _normalize_optional_canonical_id(environment_payload.get("canonical_id"))
    environment_status = str(environment_payload.get("status", "review"))
    environment_source_path = str(environment_payload.get("source_path", ""))
    if not environment_canonical_id or environment_status != "canonical":
        environment_source_path = ""
    return ShotPackage(
        shot_id=str(existing.get("shot_id", "")),
        scene_id=str(existing.get("scene_id", "")),
        chapter_id=str(existing.get("chapter_id", "")),
        shot_order=int(existing.get("shot_order", 0) or 0),
        primary_subject=str(existing.get("primary_subject", "")),
        secondary_subjects=_coerce_string_list(existing.get("secondary_subjects", [])),
        shot_moment_summary=str(existing.get("shot_moment_summary", "")),
        start_state=str(existing.get("start_state", "")),
        end_state=str(existing.get("end_state", "")),
        action_during_shot=str(existing.get("action_during_shot", "")),
        action_continues_from=str(existing.get("action_continues_from", "")),
        action_hands_off_to=str(existing.get("action_hands_off_to", "")),
        shot_size=_normalize_enum(existing.get("shot_size"), SHOT_SIZE_ENUM, fallback=""),
        camera_angle=_normalize_enum(existing.get("camera_angle"), CAMERA_ANGLE_ENUM, fallback=""),
        lens_family=_normalize_enum(existing.get("lens_family"), LENS_FAMILY_ENUM, fallback=""),
        camera_motion=_normalize_enum(existing.get("camera_motion"), CAMERA_MOTION_ENUM, fallback=""),
        zoom_behavior=_normalize_enum(existing.get("zoom_behavior"), ZOOM_BEHAVIOR_ENUM, fallback=""),
        focus_strategy=_normalize_enum(existing.get("focus_strategy"), FOCUS_STRATEGY_ENUM, fallback=""),
        lighting_style=_normalize_enum(existing.get("lighting_style"), LIGHTING_STYLE_ENUM, fallback=""),
        subject_visibility=_normalize_enum(existing.get("subject_visibility"), SUBJECT_VISIBILITY_ENUM, fallback=""),
        narration_mode=_normalize_enum(existing.get("narration_mode"), NARRATION_MODE_ENUM, fallback=""),
        primary_subject_angle=_normalize_enum(existing.get("primary_subject_angle"), PRIMARY_SUBJECT_ANGLE_ENUM, fallback=""),
        visible_primary_subject_id=str(existing.get("visible_primary_subject_id", "")),
        visible_secondary_subject_ids=_coerce_string_list(existing.get("visible_secondary_subject_ids", [])),
        primary_subject_frame_position=str(existing.get("primary_subject_frame_position", "")),
        primary_subject_scale_relation=str(existing.get("primary_subject_scale_relation", "")),
        primary_subject_facing_direction=str(existing.get("primary_subject_facing_direction", "")),
        primary_subject_pose_description=str(existing.get("primary_subject_pose_description", "")),
        subject_relation_summary=str(existing.get("subject_relation_summary", "")),
        required_environment_anchor_1=str(existing.get("required_environment_anchor_1", "")),
        required_scale_proof_detail=str(existing.get("required_scale_proof_detail", "")),
        camera_package_description=str(existing.get("camera_package_description", "")),
        shot_title=str(existing.get("shot_title", "")),
        shot_type=str(existing.get("shot_type", "")),
        camera_description=str(existing.get("camera_description", "")),
        composition=str(existing.get("composition", "")),
        target_seconds=_coerce_float(existing.get("target_seconds"), fallback=5.0),
        subject_blocking=_coerce_string_list(existing.get("subject_blocking", [])),
        camera_relative_positions=_coerce_string_list(existing.get("camera_relative_positions", [])),
        gaze_directions=_coerce_string_list(existing.get("gaze_directions", [])),
        environment_subzone=str(existing.get("environment_subzone", "")),
        key_visible_environment_features=_coerce_string_list(existing.get("key_visible_environment_features", [])),
        continuity_from_previous_shot=str(existing.get("continuity_from_previous_shot", "")),
        continuity_to_next_shot=str(existing.get("continuity_to_next_shot", "")),
        pose_anchor_frame=str(existing.get("pose_anchor_frame", "")),
        pose_end_frame=str(existing.get("pose_end_frame", "")),
        characters_in_frame=[ShotReference(**item) for item in existing.get("characters_in_frame", []) if isinstance(item, dict)],
        environment=ShotReference(
            label=str(environment_payload.get("label", "environment")),
            canonical_id=environment_canonical_id,
            display_name=str(environment_payload.get("display_name", "")),
            status=environment_status,
            entity_kind=str(environment_payload.get("entity_kind", "environment")),
            resolution_score=environment_payload.get("resolution_score"),
            source_path=environment_source_path,
            notes=str(environment_payload.get("notes", "")),
        ) if environment_payload else None,
        beat_ids=_coerce_string_list(existing.get("beat_ids", [])),
        continuity_constraints=_coerce_string_list(existing.get("continuity_constraints", [])),
        prompt_seed=str(existing.get("prompt_seed", "")),
        shot_notes=str(existing.get("shot_notes", "")),
        evidence_refs=existing.get("evidence_refs", []),
        evidence_summary=existing.get("evidence_summary", []),
        metadata=metadata,
    )


def _append_shot_review_item(queue: list[dict[str, Any]], package: ShotPackage) -> None:
    issues: list[str] = []
    if package.environment is None or package.environment.status != "canonical" or not package.environment.canonical_id:
        issues.append(f"Resolve environment for {package.shot_id}.")
    unresolved_cast = [ref for ref in package.characters_in_frame if ref.status not in {"canonical", "group"} or not ref.canonical_id]
    if unresolved_cast:
        issues.append(f"{len(unresolved_cast)} cast reference(s) need review.")
    if package.shot_type in {"shot", "generic"}:
        issues.append(f"Shot type is generic: {package.shot_type}.")
    if not package.prompt_seed or len(package.prompt_seed) < 40:
        issues.append("Prompt seed is thin.")
    if not package.start_state or not package.end_state:
        issues.append("Missing explicit start/end state.")
    if not package.action_during_shot:
        issues.append("Missing explicit action during shot.")
    if not package.subject_blocking:
        issues.append("Missing subject blocking.")
    if not package.environment_subzone:
        issues.append("Missing environment subzone.")
    queue.append(
        {
            "shot_id": package.shot_id,
            "scene_id": package.scene_id,
            "issues": issues,
        }
    )
