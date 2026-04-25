from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .common import ensure_dir, read_json, write_json
from .scaffold import create_project

NULL_STRINGS = {
    "",
    "unknown",
    "none",
    "n/a",
    "na",
    "null",
    "tbd",
    "todo",
    "not available",
    "not specified",
}


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _fingerprint_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _fingerprint_payload(payload: Any) -> str:
    return hashlib.sha256(json.dumps(payload, sort_keys=True, ensure_ascii=False).encode("utf-8")).hexdigest()


def _clamp(value: float, lower: float = 0.0, upper: float = 100.0) -> int:
    return int(round(max(lower, min(upper, value))))


def _is_meaningful_string(value: Any) -> bool:
    if not isinstance(value, str):
        return False
    text = value.strip()
    if not text:
        return False
    if text.lower() in NULL_STRINGS:
        return False
    return True


def _presence_score(value: Any) -> float:
    if value is None:
        return 0.0
    if isinstance(value, str):
        return 1.0 if _is_meaningful_string(value) else 0.0
    if isinstance(value, bool):
        return 1.0 if value else 0.0
    if isinstance(value, (int, float)):
        return 1.0
    if isinstance(value, list):
        if not value:
            return 0.0
        return sum(_presence_score(item) for item in value) / len(value)
    if isinstance(value, dict):
        if not value:
            return 0.0
        return sum(_presence_score(item) for item in value.values()) / len(value)
    return 0.0


def _weighted_presence(payload: dict[str, Any], weights: dict[str, float]) -> int:
    total_weight = sum(weights.values()) or 1.0
    score = 0.0
    for key, weight in weights.items():
        score += _presence_score(payload.get(key)) * weight
    return _clamp((score / total_weight) * 100.0)


def _count_unknown_like(value: Any) -> int:
    if value is None:
        return 1
    if isinstance(value, str):
        text = value.strip().lower()
        return 1 if (not text or text in NULL_STRINGS or "unknown" in text or "unresolved" in text) else 0
    if isinstance(value, list):
        if not value:
            return 1
        return sum(_count_unknown_like(item) for item in value)
    if isinstance(value, dict):
        if not value:
            return 1
        return sum(_count_unknown_like(item) for item in value.values())
    return 0


def _count_review_flags(payload: dict[str, Any]) -> int:
    review_flags = payload.get("review_flags")
    if isinstance(review_flags, list):
        return len(review_flags)
    if isinstance(review_flags, dict):
        return sum(1 for value in review_flags.values() if value)
    return 0


def _count_evidence_refs(payload: dict[str, Any]) -> int:
    refs = payload.get("evidence_refs")
    if isinstance(refs, list):
        return len(refs)
    return 0


def _count_mentions(payload: dict[str, Any], key: str) -> int:
    mentions = payload.get(key)
    if isinstance(mentions, list):
        return len(mentions)
    return 0


def _has_locked_fields(payload: dict[str, Any]) -> bool:
    metadata = payload.get("metadata")
    if isinstance(metadata, dict):
        lock_status = str(metadata.get("lock_status", "")).strip().lower()
        if lock_status in {"locked", "approved", "final"}:
            return True
        if metadata.get("locked") is True:
            return True
        locked_fields = metadata.get("locked_fields")
        if isinstance(locked_fields, dict) and any(bool(value) for value in locked_fields.values()):
            return True
    for key in ("locked", "approved", "final"):
        if payload.get(key) is True:
            return True
    status = str(payload.get("status", "")).strip().lower()
    return status in {"locked", "approved", "final"}


def _summarize_notes(notes: list[str]) -> str:
    if not notes:
        return ""
    return "; ".join(notes[:4])


def _dialogue_artifact_identity(artifact_path: Path, payload: Any) -> tuple[str, str]:
    if isinstance(payload, dict):
        for key in ("chapter_id", "scene_id", "shot_id", "dialogue_id", "title"):
            value = payload.get(key)
            if _is_meaningful_string(value):
                artifact_id = str(value).strip()
                return artifact_id, artifact_id
    name = artifact_path.name.upper()
    if name == "DIALOGUE.JSON":
        shot_id = artifact_path.parent.name.strip()
        scene_id = artifact_path.parent.parent.name.strip() if artifact_path.parent.parent else ""
        if scene_id and shot_id:
            artifact_id = f"{scene_id}/{shot_id}"
        else:
            artifact_id = shot_id or artifact_path.stem
        return artifact_id, artifact_id
    if name == "DIALOGUE_INDEX.JSON":
        artifact_id = artifact_path.parent.name.strip() or artifact_path.stem
        return artifact_id, artifact_id
    return artifact_path.stem, artifact_path.stem


def _dialogue_event_list(payload: Any) -> list[dict[str, Any]]:
    if isinstance(payload, dict):
        events = payload.get("dialogue_events")
        if isinstance(events, list):
            return [item for item in events if isinstance(item, dict)]
        return []
    if isinstance(payload, list):
        return [item for item in payload if isinstance(item, dict)]
    return []


@dataclass(frozen=True)
class QualityGradeRecord:
    family: str
    entity_type: str
    artifact_id: str
    display_name: str
    artifact_path: str
    markdown_path: str = ""
    source_fingerprint: str = ""
    quality_score_10: int = 0
    grade_band: str = "F"
    completeness_score: int = 0
    evidence_support_score: int = 0
    consistency_score: int = 0
    prompt_readiness_score: int = 0
    inference_load_score: int = 0
    review_status: str = "review"
    rerun_recommended: bool = False
    rerun_scope: str = ""
    rerun_stage: str = ""
    rerun_reason: list[str] = field(default_factory=list)
    dependency_refs: list[str] = field(default_factory=list)
    evidence_refs: list[dict[str, Any]] = field(default_factory=list)
    chapter_mentions: list[str] = field(default_factory=list)
    lock_status: str = "unlocked"
    notes: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "family": self.family,
            "entity_type": self.entity_type,
            "artifact_id": self.artifact_id,
            "display_name": self.display_name,
            "artifact_path": self.artifact_path,
            "markdown_path": self.markdown_path,
            "source_fingerprint": self.source_fingerprint,
            "quality_score_10": self.quality_score_10,
            "grade_band": self.grade_band,
            "completeness_score": self.completeness_score,
            "evidence_support_score": self.evidence_support_score,
            "consistency_score": self.consistency_score,
            "prompt_readiness_score": self.prompt_readiness_score,
            "inference_load_score": self.inference_load_score,
            "review_status": self.review_status,
            "rerun_recommended": self.rerun_recommended,
            "rerun_scope": self.rerun_scope,
            "rerun_stage": self.rerun_stage,
            "rerun_reason": self.rerun_reason,
            "dependency_refs": self.dependency_refs,
            "evidence_refs": self.evidence_refs,
            "chapter_mentions": self.chapter_mentions,
            "lock_status": self.lock_status,
            "notes": self.notes,
        }


@dataclass(frozen=True)
class QualityFamilySummary:
    family: str
    entity_type: str
    title: str
    count: int
    average_quality_score_10: int
    average_completeness: int
    average_evidence_support: int
    average_consistency: int
    average_prompt_readiness: int
    average_inference_load: int
    grade_counts: dict[str, int]
    rerun_count: int

    def to_dict(self) -> dict[str, Any]:
        return {
            "family": self.family,
            "entity_type": self.entity_type,
            "title": self.title,
            "count": self.count,
            "average_quality_score_10": self.average_quality_score_10,
            "average_completeness": self.average_completeness,
            "average_evidence_support": self.average_evidence_support,
            "average_consistency": self.average_consistency,
            "average_prompt_readiness": self.average_prompt_readiness,
            "average_inference_load": self.average_inference_load,
            "grade_counts": self.grade_counts,
            "rerun_count": self.rerun_count,
        }


@dataclass(frozen=True)
class QualityGradingSummary:
    project_slug: str
    generated_at_utc: str
    total_records: int
    family_summaries: list[QualityFamilySummary]
    records: list[QualityGradeRecord]
    rerun_queue: list[dict[str, Any]]
    written_files: list[str]
    warnings: list[str]

    def to_dict(self) -> dict[str, Any]:
        return {
            "project_slug": self.project_slug,
            "generated_at_utc": self.generated_at_utc,
            "total_records": self.total_records,
            "family_summaries": [summary.to_dict() for summary in self.family_summaries],
            "records": [record.to_dict() for record in self.records],
            "rerun_queue": self.rerun_queue,
            "written_files": self.written_files,
            "warnings": self.warnings,
        }


@dataclass(frozen=True)
class _FamilySpec:
    family: str
    entity_type: str
    title: str
    glob_patterns: list[str]
    rerun_stage: str
    rerun_scope: str
    dependencies: list[str]


FAMILY_SPECS: list[_FamilySpec] = [
    _FamilySpec(
        family="character_bible",
        entity_type="character",
        title="Character Bibles",
        glob_patterns=["02_story_analysis/bibles/characters/*.json"],
        rerun_stage="synthesize-character-bibles",
        rerun_scope="character_family",
        dependencies=["chapter_analysis", "identity_refinement"],
    ),
    _FamilySpec(
        family="environment_bible",
        entity_type="environment",
        title="Environment Bibles",
        glob_patterns=["02_story_analysis/bibles/environments/*.json"],
        rerun_stage="synthesize-environment-bibles",
        rerun_scope="environment_family",
        dependencies=["chapter_analysis", "identity_refinement"],
    ),
    _FamilySpec(
        family="scene_contract",
        entity_type="scene",
        title="Scene Contracts",
        glob_patterns=["02_story_analysis/contracts/scenes/**/*.json"],
        rerun_stage="synthesize-scene-contracts",
        rerun_scope="scene_family",
        dependencies=["character_bible", "environment_bible"],
    ),
    _FamilySpec(
        family="shot_package",
        entity_type="shot",
        title="Shot Packages",
        glob_patterns=["02_story_analysis/contracts/shots/**/*.json"],
        rerun_stage="synthesize-shot-packages",
        rerun_scope="shot_family",
        dependencies=["scene_contract", "character_bible", "environment_bible"],
    ),
    _FamilySpec(
        family="dialogue_timeline",
        entity_type="dialogue",
        title="Dialogue Timelines",
        glob_patterns=[
            "02_story_analysis/timelines/**/*.json",
            "02_story_analysis/contracts/shots/**/*DIALOGUE*.json",
        ],
        rerun_stage="synthesize-dialogue-timeline",
        rerun_scope="dialogue_family",
        dependencies=["shot_package", "scene_contract"],
    ),
    _FamilySpec(
        family="descriptor",
        entity_type="descriptor",
        title="Descriptor Records",
        glob_patterns=["02_story_analysis/descriptors/**/*.json"],
        rerun_stage="synthesize-descriptor-enrichment",
        rerun_scope="descriptor_family",
        dependencies=["character_bible", "environment_bible", "scene_contract", "shot_package"],
    ),
    _FamilySpec(
        family="prompt_package",
        entity_type="prompt",
        title="Prompt Packages",
        glob_patterns=["03_prompt_packages/prepared/**/*_prompt.md"],
        rerun_stage="synthesize-prompt-preparation",
        rerun_scope="prompt_family",
        dependencies=["character_bible", "environment_bible", "scene_contract", "shot_package", "descriptor"],
    ),
]


def _iter_family_paths(project_dir: Path, spec: _FamilySpec) -> list[Path]:
    paths: list[Path] = []
    for pattern in spec.glob_patterns:
        for path in project_dir.glob(pattern):
            if path.is_dir():
                continue
            name = path.name.upper()
            parts = {part.upper() for part in path.parts}
            if "REVIEW" in parts or path.parent.name.lower() == "review":
                continue
            if "INDEX" in name and spec.family != "prompt_package":
                continue
            if spec.family == "prompt_package":
                if not path.name.endswith("_prompt.md"):
                    continue
                if "INDEX" in name or "REVIEW" in name:
                    continue
            elif spec.family == "shot_package":
                if not re.fullmatch(r"SH\d+\.json", path.name, flags=re.IGNORECASE):
                    continue
            elif spec.family == "scene_contract":
                if not re.fullmatch(r"CH\d+_SC\d+\.json", path.name, flags=re.IGNORECASE):
                    continue
            elif spec.family in {"character_bible", "environment_bible"}:
                if not path.name.lower().startswith(("char_", "env_")):
                    continue
            elif spec.family == "dialogue_timeline":
                if not (
                    path.name.endswith("_DIALOGUE_TIMELINE.json")
                    or path.name in {"dialogue_timeline.json", "edit_timeline.json", "DIALOGUE_INDEX.json", "DIALOGUE.json"}
                ):
                    continue
            elif spec.family == "descriptor":
                if "INDEX" in name or "REVIEW" in name:
                    continue
            paths.append(path)
    unique_paths = sorted({path.resolve() for path in paths}, key=lambda item: str(item).lower())
    return unique_paths


def _band_from_score(score: int) -> str:
    if score >= 90:
        return "A"
    if score >= 75:
        return "B"
    if score >= 60:
        return "C"
    if score >= 45:
        return "D"
    return "F"


def _score_10_from_score(score: int) -> int:
    if score <= 0:
        return 0
    return max(1, min(10, round(score / 10)))


def _grader_character(payload: dict[str, Any]) -> tuple[int, int, int, int, int, list[str]]:
    completeness = _weighted_presence(
        payload,
        {
            "role": 8,
            "stable_visual_summary": 18,
            "costume_signature": 12,
            "physical_traits": 15,
            "personality": 10,
            "voice_notes": 8,
            "relationship_notes": 6,
            "continuity_constraints": 8,
            "chapter_mentions": 10,
            "evidence_refs": 5,
        },
    )
    evidence_support = _clamp(
        min(100.0, _count_evidence_refs(payload) * 14 + _count_mentions(payload, "chapter_mentions") * 6 + (10 if _is_meaningful_string(payload.get("first_seen_chapter")) else 0) + (10 if _is_meaningful_string(payload.get("last_seen_chapter")) else 0))
    )
    unknown_count = sum(
        _count_unknown_like(payload.get(key))
        for key in ("stable_visual_summary", "costume_signature", "physical_traits", "personality", "voice_notes", "relationship_notes", "continuity_constraints")
    )
    inference_load = _clamp(unknown_count * 15 + _count_review_flags(payload) * 8)
    consistency = _clamp(100.0 - len(payload.get("unresolved_ambiguities", [])) * 12 - _count_review_flags(payload) * 6)
    prompt_readiness = _clamp(completeness * 0.55 + evidence_support * 0.2 + (100 - inference_load) * 0.25)
    notes = []
    if _count_unknown_like(payload.get("stable_visual_summary")):
        notes.append("stable_visual_summary is unresolved")
    if _count_unknown_like(payload.get("costume_signature")):
        notes.append("costume_signature is thin")
    if _count_unknown_like(payload.get("physical_traits")):
        notes.append("physical_traits are thin")
    if _count_review_flags(payload):
        notes.append("review flags present")
    if len(payload.get("unresolved_ambiguities", [])) > 0:
        notes.append(f"{len(payload.get('unresolved_ambiguities', []))} unresolved ambiguities")
    return completeness, evidence_support, consistency, prompt_readiness, inference_load, notes


def _focus_fields_from_notes(family: str, notes: list[str]) -> list[str]:
    mapping = {
        "character_bible": {
            "stable_visual_summary": "stable_visual_summary is unresolved",
            "costume_signature": "costume_signature is thin",
            "physical_traits": "physical_traits are thin",
            "personality": "personality is thin",
            "voice_notes": "voice_notes are thin",
            "relationship_notes": "relationship_notes are thin",
        },
        "environment_bible": {
            "visual_summary": "visual_summary is unresolved",
            "layout_notes": "layout_notes are thin",
            "lighting": "lighting is thin",
            "mood": "mood is thin",
        },
        "scene_contract": {
            "production_intent": "production_intent is thin",
            "summary": "summary is thin",
            "unresolved_questions": "unresolved questions present",
        },
        "shot_package": {
            "environment": "environment resolution is thin",
            "prompt_seed": "prompt_seed is thin",
            "target_seconds": "target_seconds missing",
        },
        "descriptor": {
            "generated_field_values": "generated fields remain thin",
            "field_values": "descriptor is incomplete",
        },
        "prompt_package": {
            "source_artifact_ids": "reference ids are missing",
            "reference_asset_ids": "reference ids are missing",
            "unknown": "placeholder language present",
        },
    }
    field_map = mapping.get(family, {})
    focus = []
    for field_name, needle in field_map.items():
        if any(needle in note for note in notes):
            focus.append(field_name)
    return sorted(dict.fromkeys(focus))


def _grader_environment(payload: dict[str, Any]) -> tuple[int, int, int, int, int, list[str]]:
    completeness = _weighted_presence(
        payload,
        {
            "visual_summary": 18,
            "layout_notes": 16,
            "lighting": 10,
            "mood": 10,
            "recurring_elements": 12,
            "constraints": 10,
            "chapter_mentions": 10,
            "evidence_refs": 8,
            "environment_type": 6,
        },
    )
    evidence_support = _clamp(
        min(100.0, _count_evidence_refs(payload) * 14 + _count_mentions(payload, "chapter_mentions") * 8 + (10 if _is_meaningful_string(payload.get("first_seen_chapter")) else 0) + (10 if _is_meaningful_string(payload.get("last_seen_chapter")) else 0))
    )
    unknown_count = sum(
        _count_unknown_like(payload.get(key))
        for key in ("visual_summary", "layout_notes", "lighting", "mood", "recurring_elements", "constraints")
    )
    inference_load = _clamp(unknown_count * 15 + _count_review_flags(payload) * 8)
    consistency = _clamp(100.0 - len(payload.get("unresolved_ambiguities", [])) * 12 - _count_review_flags(payload) * 6)
    prompt_readiness = _clamp(completeness * 0.6 + evidence_support * 0.2 + (100 - inference_load) * 0.2)
    notes = []
    if _count_unknown_like(payload.get("visual_summary")):
        notes.append("visual_summary is unresolved")
    if _count_unknown_like(payload.get("layout_notes")):
        notes.append("layout_notes are thin")
    if _count_review_flags(payload):
        notes.append("review flags present")
    if len(payload.get("unresolved_ambiguities", [])) > 0:
        notes.append(f"{len(payload.get('unresolved_ambiguities', []))} unresolved ambiguities")
    return completeness, evidence_support, consistency, prompt_readiness, inference_load, notes


def _grader_scene(payload: dict[str, Any]) -> tuple[int, int, int, int, int, list[str]]:
    completeness = _weighted_presence(
        payload,
        {
            "summary": 16,
            "production_intent": 16,
            "emotional_arc": 10,
            "purpose": 8,
            "continuity_constraints": 10,
            "characters_required": 10,
            "environments_required": 10,
            "beat_list": 10,
            "evidence_refs": 5,
            "storyboard_markdown": 5,
            "visual_coverage_families": 5,
        },
    )
    evidence_support = _clamp(
        min(100.0, _count_evidence_refs(payload) * 12 + _count_mentions(payload, "characters_required") * 6 + _count_mentions(payload, "environments_required") * 6 + len(payload.get("beat_list", [])) * 3)
    )
    unknown_count = sum(_count_unknown_like(payload.get(key)) for key in ("summary", "production_intent", "emotional_arc", "purpose"))
    inference_load = _clamp(unknown_count * 18 + len(payload.get("unresolved_questions", [])) * 10 + _count_review_flags(payload) * 8)
    consistency = _clamp(100.0 - len(payload.get("unresolved_questions", [])) * 12 - _count_review_flags(payload) * 6)
    prompt_readiness = _clamp(completeness * 0.45 + evidence_support * 0.25 + (100 - inference_load) * 0.3)
    notes = []
    if _count_unknown_like(payload.get("production_intent")):
        notes.append("production_intent is thin")
    if len(payload.get("unresolved_questions", [])) > 0:
        notes.append(f"{len(payload.get('unresolved_questions', []))} unresolved questions")
    if _count_review_flags(payload):
        notes.append("review flags present")
    return completeness, evidence_support, consistency, prompt_readiness, inference_load, notes


def _grader_shot(payload: dict[str, Any]) -> tuple[int, int, int, int, int, list[str]]:
    completeness = _weighted_presence(
        payload,
        {
            "shot_title": 10,
            "shot_type": 10,
            "camera_description": 12,
            "composition": 12,
            "environment": 10,
            "characters_in_frame": 10,
            "continuity_constraints": 10,
            "prompt_seed": 10,
            "shot_notes": 10,
            "evidence_refs": 5,
            "target_seconds": 5,
            "previous_shot_id": 3,
            "next_shot_id": 3,
        },
    )
    evidence_support = _clamp(
        min(100.0, _count_evidence_refs(payload) * 12 + _count_mentions(payload, "characters_in_frame") * 5 + (5 if _is_meaningful_string(payload.get("environment")) else 0) + (5 if _is_meaningful_string(payload.get("prompt_seed")) else 0))
    )
    unknown_count = sum(_count_unknown_like(payload.get(key)) for key in ("shot_title", "camera_description", "composition", "environment", "shot_notes", "prompt_seed"))
    inference_load = _clamp(unknown_count * 15 + len(payload.get("continuity_constraints", [])) * 2 + _count_review_flags(payload) * 8)
    consistency = _clamp(100.0 - _count_review_flags(payload) * 6 - (10 if not _is_meaningful_string(payload.get("environment")) else 0))
    prompt_readiness = _clamp(completeness * 0.4 + evidence_support * 0.25 + (100 - inference_load) * 0.35)
    notes = []
    if _count_unknown_like(payload.get("environment")):
        notes.append("environment resolution is thin")
    if _count_unknown_like(payload.get("prompt_seed")):
        notes.append("prompt_seed is thin")
    if payload.get("target_seconds") in (None, "", 0):
        notes.append("target_seconds missing")
    if _count_review_flags(payload):
        notes.append("review flags present")
    return completeness, evidence_support, consistency, prompt_readiness, inference_load, notes


def _is_silent_dialogue(payload: dict[str, Any]) -> bool:
    """Check if dialogue is explicitly marked as silent/no dialogue expected."""
    if isinstance(payload, dict):
        if payload.get("no_dialogue_expected") is True:
            return True
        metadata = payload.get("metadata")
        if isinstance(metadata, dict) and metadata.get("no_dialogue_expected") is True:
            return True
    return False


def _grader_dialogue(payload: dict[str, Any], *, artifact_path: Path) -> tuple[int, int, int, int, int, list[str]]:
    events = _dialogue_event_list(payload)
    is_silent = _is_silent_dialogue(payload)
    
    if isinstance(payload, list) or (isinstance(payload, dict) and "dialogue_events" in payload):
        payload_dict = payload if isinstance(payload, dict) else {}
        scene_bindings = payload_dict.get("scene_bindings") if isinstance(payload_dict.get("scene_bindings"), list) else []
        completeness = _clamp(min(100.0, len(events) * 10 + len(scene_bindings) * 8 + (10 if _is_meaningful_string(payload_dict.get("chapter_id")) else 0) + (10 if _is_meaningful_string(payload_dict.get("source_path")) else 0)))
        unresolved = sum(1 for event in events if isinstance(event, dict) and event.get("speaker", {}).get("status") == "unresolved")
        evidence_support = _clamp(min(100.0, len(events) * 10 + len(scene_bindings) * 8 + (10 if _is_meaningful_string(payload_dict.get("source_fingerprint")) else 0)))
        consistency = _clamp(100.0 - unresolved * 8)
        prompt_readiness = _clamp(completeness * 0.45 + evidence_support * 0.25 + consistency * 0.3)
        inference_load = _clamp(unresolved * 10 + (_count_review_flags(payload_dict) if isinstance(payload, dict) else 0) * 8)
        notes = []
        if unresolved:
            notes.append(f"{unresolved} unresolved speakers")
        if not events and not is_silent:
            notes.append("no dialogue events")
        return completeness, evidence_support, consistency, prompt_readiness, inference_load, notes

    if "chapters" in payload and isinstance(payload.get("chapters"), list):
        chapters = payload.get("chapters", [])
        completeness = _clamp(min(100.0, len(chapters) * 18 + (10 if _is_meaningful_string(payload.get("project_slug")) else 0)))
        total_events = sum(int(ch.get("dialogue_events", 0)) for ch in chapters if isinstance(ch, dict))
        unresolved = sum(int(ch.get("unresolved_speakers", 0)) for ch in chapters if isinstance(ch, dict))
        evidence_support = _clamp(min(100.0, total_events * 2 + len(chapters) * 10))
        consistency = _clamp(100.0 - unresolved * 5)
        prompt_readiness = _clamp(completeness * 0.35 + evidence_support * 0.35 + consistency * 0.3)
        inference_load = _clamp(unresolved * 8 + _count_review_flags(payload) * 6)
        notes = []
        if unresolved:
            notes.append(f"{unresolved} unresolved speakers")
        return completeness, evidence_support, consistency, prompt_readiness, inference_load, notes

    if artifact_path.name.endswith("_DIALOGUE_TIMELINE.json"):
        events = _dialogue_event_list(payload)
        payload_dict = payload if isinstance(payload, dict) else {}
        scene_bindings = payload_dict.get("scene_bindings") if isinstance(payload_dict.get("scene_bindings"), list) else []
        completeness = _clamp(min(100.0, len(events) * 12 + len(scene_bindings) * 10))
        unresolved = len([event for event in events if isinstance(event, dict) and event.get("speaker", {}).get("status") == "unresolved"])
        evidence_support = _clamp(min(100.0, len(events) * 10 + len(scene_bindings) * 8))
        consistency = _clamp(100.0 - unresolved * 8)
        prompt_readiness = _clamp(completeness * 0.45 + evidence_support * 0.25 + consistency * 0.3)
        inference_load = _clamp(unresolved * 10)
        notes = []
        if unresolved:
            notes.append(f"{unresolved} unresolved speakers")
        return completeness, evidence_support, consistency, prompt_readiness, inference_load, notes

    completeness = _weighted_presence(payload, {"project_slug": 20, "chapter_count": 20, "dialogue_event_count": 20, "chapter_summaries": 20, "dialogue_events": 20})
    evidence_support = _clamp(min(100.0, _count_mentions(payload, "chapter_summaries") * 5 + _count_mentions(payload, "dialogue_events") * 2))
    consistency = _clamp(100.0 - _count_review_flags(payload) * 5)
    prompt_readiness = _clamp(completeness * 0.5 + evidence_support * 0.2 + consistency * 0.3)
    inference_load = _clamp(_count_review_flags(payload) * 5)
    notes = []
    return completeness, evidence_support, consistency, prompt_readiness, inference_load, notes


def _grader_descriptor(payload: dict[str, Any]) -> tuple[int, int, int, int, int, list[str]]:
    completeness = _weighted_presence(
        payload,
        {
            "canonical_id": 8,
            "display_name": 8,
            "entity_type": 8,
            "status": 6,
            "field_values": 20,
            "supported_field_values": 12,
            "generated_field_values": 12,
            "field_states": 12,
            "evidence_refs": 8,
            "chapter_mentions": 6,
            "scene_mentions": 6,
            "shot_mentions": 4,
            "review_flags": 4,
        },
    )
    evidence_support = _clamp(min(100.0, _count_evidence_refs(payload) * 12 + _count_mentions(payload, "chapter_mentions") * 4 + _count_mentions(payload, "scene_mentions") * 3 + _count_mentions(payload, "shot_mentions") * 2))
    inference_load = _clamp(_count_unknown_like(payload.get("generated_field_values")) * 8 + _count_review_flags(payload) * 6)
    consistency = _clamp(100.0 - _count_review_flags(payload) * 5 - (10 if str(payload.get("status", "")).strip().lower() in {"review_needed", "unresolved"} else 0))
    prompt_readiness = _clamp(completeness * 0.45 + evidence_support * 0.25 + (100 - inference_load) * 0.3)
    notes = []
    if _count_review_flags(payload):
        notes.append("review flags present")
    if _count_unknown_like(payload.get("generated_field_values")):
        notes.append("generated fields remain thin")
    return completeness, evidence_support, consistency, prompt_readiness, inference_load, notes


def _has_prompt_semantic_issue(text: str) -> tuple[bool, list[str]]:
    """Check for semantic issues that should cap grade below A."""
    issues = []
    text_lower = text.lower()
    
    if "missing the required subject anchor" in text_lower or "missing required subject anchor" in text_lower:
        issues.append("Prompt body is missing the required subject anchor")
    
    if "reference conflict" in text_lower:
        issues.append("reference conflict exists")
    
    if "image1" in text_lower and "subject contradicts" in text_lower:
        issues.append("image1 subject contradicts visible primary subject")
    
    if "visible subject exists" in text_lower and "positive prompt omits" in text_lower:
        issues.append("visible subject exists but positive prompt omits it")
    
    if "shot negatives" in text_lower and "missing fallback" in text_lower:
        issues.append("shot negatives are missing fallback terms")
    
    env_markers = ["architecture", "lighting", "mood", "scale"]
    if "environment" in text_lower:
        missing_env = [m for m in env_markers if m not in text_lower]
        if len(missing_env) >= 2:
            issues.append(f"environment prompt missing {', '.join(missing_env[:2])} descriptors")
    
    if "character" in text_lower:
        if "body_descriptor" not in text_lower and "locked_fields" not in text_lower and "fallback repair" not in text_lower:
            issues.append("character prompt missing body_descriptor or locked_fields and no fallback repair")
    
    return len(issues) > 0, issues


def _grader_prompt_package(text: str) -> tuple[int, int, int, int, int, list[str]]:
    lines = text.splitlines()
    sections = sum(1 for line in lines if line.startswith("#"))
    ref_hits = sum(1 for token in ("reference", "source_artifact_ids", "reference_asset_ids", "continuity", "shot_lineage_ids", "prompt", "negative") if token.lower() in text.lower())
    completeness = _clamp(min(100.0, len(text) / 20 + sections * 12 + ref_hits * 5))
    evidence_support = _clamp(min(100.0, ref_hits * 12 + (15 if "source_artifact_ids" in text.lower() else 0) + (15 if "reference_asset_ids" in text.lower() else 0)))
    unknown_like = sum(text.lower().count(marker) for marker in ("unknown", "no notes available", "todo", "tbd"))
    inference_load = _clamp(min(100.0, unknown_like * 15))
    length_score = 100 if 250 <= len(text) <= 4000 else _clamp(max(0.0, 100.0 - abs(len(text) - 1200) / 20))
    prompt_readiness = _clamp(completeness * 0.35 + evidence_support * 0.25 + length_score * 0.4)
    consistency = _clamp(100.0 - unknown_like * 12)
    notes = []
    if "source_artifact_ids" not in text.lower() and "reference_asset_ids" not in text.lower():
        notes.append("reference ids are missing")
    if unknown_like:
        notes.append("placeholder language present")
    
    has_semantic_issue, semantic_issues = _has_prompt_semantic_issue(text)
    if has_semantic_issue:
        notes.extend(semantic_issues)
    
    return completeness, evidence_support, consistency, prompt_readiness, inference_load, notes


def _family_records(project_dir: Path, spec: _FamilySpec) -> list[Path]:
    return _iter_family_paths(project_dir, spec)


def _make_grade_record(
    *,
    family: _FamilySpec,
    artifact_path: Path,
    payload: Any,
    markdown_path: Path | None = None,
) -> QualityGradeRecord:
    if isinstance(payload, dict):
        artifact_id = ""
        display_name = ""
        for key in ("character_id", "environment_id", "scene_id", "shot_id", "descriptor_id", "project_slug", "chapter_id", "title"):
            value = payload.get(key)
            if _is_meaningful_string(value):
                artifact_id = str(value).strip()
                break
        if not artifact_id:
            artifact_id = artifact_path.stem
        display_name = str(payload.get("display_name", "")) if _is_meaningful_string(payload.get("display_name")) else artifact_id
    elif family.family == "dialogue_timeline" and isinstance(payload, list):
        artifact_id, display_name = _dialogue_artifact_identity(artifact_path, payload)
    else:
        artifact_id = artifact_path.stem
        display_name = artifact_id

    if family.family == "character_bible" and isinstance(payload, dict):
        completeness, evidence_support, consistency, prompt_readiness, inference_load, notes = _grader_character(payload)
        chapter_mentions = [str(item) for item in payload.get("chapter_mentions", []) if _is_meaningful_string(item)]
    elif family.family == "environment_bible" and isinstance(payload, dict):
        completeness, evidence_support, consistency, prompt_readiness, inference_load, notes = _grader_environment(payload)
        chapter_mentions = [str(item) for item in payload.get("chapter_mentions", []) if _is_meaningful_string(item)]
    elif family.family == "scene_contract" and isinstance(payload, dict):
        completeness, evidence_support, consistency, prompt_readiness, inference_load, notes = _grader_scene(payload)
        chapter_mentions = [str(payload.get("chapter_id", ""))] if _is_meaningful_string(payload.get("chapter_id")) else []
    elif family.family == "shot_package" and isinstance(payload, dict):
        completeness, evidence_support, consistency, prompt_readiness, inference_load, notes = _grader_shot(payload)
        chapter_mentions = [str(payload.get("chapter_id", ""))] if _is_meaningful_string(payload.get("chapter_id")) else []
    elif family.family == "dialogue_timeline" and isinstance(payload, (dict, list)):
        completeness, evidence_support, consistency, prompt_readiness, inference_load, notes = _grader_dialogue(payload, artifact_path=artifact_path)
        if isinstance(payload, dict):
            chapter_mentions = [str(payload.get("chapter_id", ""))] if _is_meaningful_string(payload.get("chapter_id")) else []
        else:
            chapter_id = artifact_path.parent.parent.name[:5].upper() if artifact_path.parent.parent else ""
            chapter_mentions = [chapter_id] if chapter_id.startswith("CH") else []
    elif family.family == "descriptor" and isinstance(payload, dict):
        completeness, evidence_support, consistency, prompt_readiness, inference_load, notes = _grader_descriptor(payload)
        chapter_mentions = [str(item) for item in payload.get("chapter_mentions", []) if _is_meaningful_string(item)]
    elif family.family == "prompt_package" and isinstance(payload, str):
        completeness, evidence_support, consistency, prompt_readiness, inference_load, notes = _grader_prompt_package(payload)
        chapter_mentions = []
    else:
        completeness, evidence_support, consistency, prompt_readiness, inference_load, notes = 0, 0, 0, 0, 100, ["unrecognized artifact shape"]
        chapter_mentions = []

    if isinstance(payload, (dict, list)):
        fingerprint = _fingerprint_payload(payload)
        evidence_refs = payload.get("evidence_refs") if isinstance(payload, dict) and isinstance(payload.get("evidence_refs"), list) else []
    else:
        fingerprint = _fingerprint_text(payload)
        evidence_refs = []

    average = round((completeness + evidence_support + consistency + prompt_readiness + (100 - inference_load)) / 5)
    quality_score_10 = _score_10_from_score(average)
    grade_band = _band_from_score(average)
    locked = _has_locked_fields(payload) if isinstance(payload, dict) else False
    rerun_recommended = not locked and quality_score_10 <= 6
    reason_bits = list(notes)
    
    # Apply prompt package semantic caps
    if family.family == "prompt_package" and isinstance(payload, str):
        has_semantic_issue, semantic_issues = _has_prompt_semantic_issue(payload)
        if has_semantic_issue or prompt_readiness < 80:
            if grade_band == "A":
                grade_band = "C"
                quality_score_10 = min(quality_score_10, 7)
            rerun_recommended = True
            if has_semantic_issue:
                reason_bits.append("semantic prompt assembly issue")
            if prompt_readiness < 80:
                reason_bits.append(f"prompt readiness {prompt_readiness} below threshold 80")
    
    # Apply dialogue silent mode logic
    if family.family == "dialogue_timeline" and isinstance(payload, (dict, list)):
        events = _dialogue_event_list(payload)
        is_silent = _is_silent_dialogue(payload)
        if not events and is_silent:
            # Silent dialogue with no events is acceptable
            rerun_recommended = False
            reason_bits = []
        elif not events and not is_silent:
            # Expected dialogue but no events - should rerun
            rerun_recommended = True
            if "no dialogue events" not in reason_bits:
                reason_bits.append("expected dialogue but no events generated")
    
    # Add general rerun reasons for non-special families
    if family.family not in {"prompt_package", "dialogue_timeline"}:
        if grade_band == "C":
            reason_bits.append("borderline completeness")
        elif grade_band in {"D", "F"}:
            reason_bits.append("low completeness or evidence coverage")
    
    review_status = "locked" if locked else ("rerun" if rerun_recommended else "ok")
    rerun_reason = reason_bits
    dependency_refs = list(family.dependencies)

    return QualityGradeRecord(
        family=family.family,
        entity_type=family.entity_type,
        artifact_id=artifact_id,
        display_name=display_name,
        artifact_path=str(artifact_path),
        markdown_path=str(markdown_path) if markdown_path else "",
        source_fingerprint=fingerprint,
        quality_score_10=quality_score_10,
        grade_band=grade_band,
        completeness_score=completeness,
        evidence_support_score=evidence_support,
        consistency_score=consistency,
        prompt_readiness_score=prompt_readiness,
        inference_load_score=inference_load,
        review_status=review_status,
        rerun_recommended=rerun_recommended,
        rerun_scope=family.rerun_scope if rerun_recommended else "",
        rerun_stage="run-prompt-preparation" if (family.family == "prompt_package" and rerun_recommended) else (family.rerun_stage if rerun_recommended else ""),
        rerun_reason=rerun_reason,
        dependency_refs=dependency_refs,
        evidence_refs=evidence_refs if isinstance(evidence_refs, list) else [],
        chapter_mentions=chapter_mentions,
        lock_status="locked" if locked else "unlocked",
        notes=notes,
    )


def _render_grade_index_markdown(summary: QualityGradingSummary) -> str:
    lines: list[str] = []
    lines.append("# Quality Grade Index")
    lines.append("")
    lines.append(f"- Project: `{summary.project_slug}`")
    lines.append(f"- Generated: `{summary.generated_at_utc}`")
    lines.append(f"- Records: `{summary.total_records}`")
    lines.append("")
    lines.append("## Family Summary")
    lines.append("")
    lines.append("| Family | Count | Avg Score | Avg Comp | Avg Evidence | Avg Consistency | Avg Prompt | Avg Inference | Reruns |")
    lines.append("| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |")
    for family in sorted(summary.family_summaries, key=lambda item: item.family):
        lines.append(
            f"| {family.title} | {family.count} | {family.average_quality_score_10} | {family.average_completeness} | {family.average_evidence_support} | {family.average_consistency} | {family.average_prompt_readiness} | {family.average_inference_load} | {family.rerun_count} |"
        )
    lines.append("")
    lines.append("## Top Records")
    lines.append("")
    lines.append("| Score | Grade | Family | Artifact | Comp | Evidence | Prompt | Inference | Rerun | Notes |")
    lines.append("| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- |")
    for record in sorted(summary.records, key=lambda item: (item.quality_score_10, item.completeness_score, item.evidence_support_score), reverse=True):
        notes = _summarize_notes(record.notes or record.rerun_reason)
        lines.append(
            f"| {record.quality_score_10} | {record.grade_band} | {record.family} | {record.artifact_id} | {record.completeness_score} | {record.evidence_support_score} | {record.prompt_readiness_score} | {record.inference_load_score} | {record.rerun_stage or '-'} | {notes or '-'} |"
        )
    return "\n".join(lines) + "\n"


def _render_rerun_queue_markdown(summary: QualityGradingSummary) -> str:
    lines: list[str] = []
    lines.append("# Quality Rerun Queue")
    lines.append("")
    lines.append(f"- Project: `{summary.project_slug}`")
    lines.append(f"- Generated: `{summary.generated_at_utc}`")
    lines.append(f"- Rerun items: `{len(summary.rerun_queue)}`")
    lines.append("")
    if not summary.rerun_queue:
        lines.append("- No reruns recommended.")
        return "\n".join(lines) + "\n"
    lines.append("| Family | Artifact | Stage | Scope | Reason |")
    lines.append("| --- | --- | --- | --- | --- |")
    for item in summary.rerun_queue:
        reason = "; ".join(item.get("reason", [])[:3]) if isinstance(item.get("reason"), list) else str(item.get("reason", ""))
        lines.append(
            f"| {item.get('family', '')} | {item.get('artifact_id', '')} | {item.get('rerun_stage', '')} | {item.get('rerun_scope', '')} | {reason or '-'} |"
        )
    return "\n".join(lines) + "\n"


def _family_summary(records: list[QualityGradeRecord], spec: _FamilySpec) -> QualityFamilySummary:
    family_records = [record for record in records if record.family == spec.family]
    count = len(family_records)
    if not count:
        return QualityFamilySummary(
            family=spec.family,
            entity_type=spec.entity_type,
            title=spec.title,
            count=0,
            average_quality_score_10=0,
            average_completeness=0,
            average_evidence_support=0,
            average_consistency=0,
            average_prompt_readiness=0,
            average_inference_load=0,
            grade_counts={},
            rerun_count=0,
        )
    grade_counts: dict[str, int] = {}
    for record in family_records:
        grade_counts[record.grade_band] = grade_counts.get(record.grade_band, 0) + 1
    return QualityFamilySummary(
        family=spec.family,
        entity_type=spec.entity_type,
        title=spec.title,
        count=count,
        average_quality_score_10=round(sum(record.quality_score_10 for record in family_records) / count),
        average_completeness=round(sum(record.completeness_score for record in family_records) / count),
        average_evidence_support=round(sum(record.evidence_support_score for record in family_records) / count),
        average_consistency=round(sum(record.consistency_score for record in family_records) / count),
        average_prompt_readiness=round(sum(record.prompt_readiness_score for record in family_records) / count),
        average_inference_load=round(sum(record.inference_load_score for record in family_records) / count),
        grade_counts=dict(sorted(grade_counts.items())),
        rerun_count=sum(1 for record in family_records if record.rerun_recommended),
    )


def _build_rerun_queue(records: list[QualityGradeRecord]) -> list[dict[str, Any]]:
    rerun_queue = []
    for record in sorted([item for item in records if item.rerun_recommended], key=lambda item: (item.quality_score_10, item.completeness_score, item.evidence_support_score)):
        rerun_queue.append(
            {
                "family": record.family,
                "entity_type": record.entity_type,
                "artifact_id": record.artifact_id,
                "display_name": record.display_name,
                "artifact_path": record.artifact_path,
                "markdown_path": record.markdown_path,
                "quality_score_10": record.quality_score_10,
                "grade_band": record.grade_band,
                "completeness_score": record.completeness_score,
                "evidence_support_score": record.evidence_support_score,
                "consistency_score": record.consistency_score,
                "prompt_readiness_score": record.prompt_readiness_score,
                "inference_load_score": record.inference_load_score,
                "rerun_stage": record.rerun_stage,
                "rerun_scope": record.rerun_scope,
                "reason": record.rerun_reason,
                "focus_fields": _focus_fields_from_notes(record.family, record.rerun_reason),
                "dependency_refs": record.dependency_refs,
                "lock_status": record.lock_status,
            }
        )
    return rerun_queue


def run_quality_grading(
    project_slug: str,
    *,
    families: list[str] | None = None,
) -> QualityGradingSummary:
    project_dir = create_project(project_slug)
    project_dir = project_dir.resolve()
    output_root = project_dir / "02_story_analysis" / "grading"
    review_root = output_root / "review"
    ensure_dir(output_root)
    ensure_dir(review_root)

    selected_families = {family.lower() for family in families} if families else None
    warnings: list[str] = []
    records: list[QualityGradeRecord] = []
    written_files: list[str] = []

    for spec in FAMILY_SPECS:
        if selected_families and spec.entity_type not in selected_families and spec.family not in selected_families:
            continue
        paths = _family_records(project_dir, spec)
        for path in paths:
            try:
                if spec.family == "prompt_package":
                    payload = path.read_text(encoding="utf-8")
                    markdown_path = path
                else:
                    payload = read_json(path)
                    markdown_path = path.with_suffix(".md") if path.with_suffix(".md").exists() else None
                record = _make_grade_record(family=spec, artifact_path=path, payload=payload, markdown_path=markdown_path)
                records.append(record)
            except Exception as exc:  # noqa: BLE001
                warnings.append(f"{path}: {exc}")
                records.append(
                    QualityGradeRecord(
                        family=spec.family,
                        entity_type=spec.entity_type,
                        artifact_id=path.stem,
                        display_name=path.stem,
                        artifact_path=str(path),
                        markdown_path=str(path.with_suffix(".md")) if path.with_suffix(".md").exists() else "",
                        grade_band="F",
                        completeness_score=0,
                        evidence_support_score=0,
                        consistency_score=0,
                        prompt_readiness_score=0,
                        inference_load_score=100,
                        review_status="rerun",
                        rerun_recommended=True,
                        rerun_scope=spec.rerun_scope,
                        rerun_stage=spec.rerun_stage,
                        rerun_reason=[str(exc)],
                        dependency_refs=list(spec.dependencies),
                        notes=[str(exc)],
                    )
                )

    deduped_records: dict[tuple[str, str, str], QualityGradeRecord] = {}
    for record in records:
        key = (record.family, record.artifact_id, record.source_fingerprint or record.artifact_path)
        existing = deduped_records.get(key)
        if existing is None or len(record.artifact_path) < len(existing.artifact_path):
            deduped_records[key] = record
    records = list(deduped_records.values())

    family_summaries = [_family_summary(records, spec) for spec in FAMILY_SPECS if not selected_families or spec.entity_type in selected_families or spec.family in selected_families]
    rerun_queue = _build_rerun_queue(records)

    index_json = output_root / "QUALITY_GRADE_INDEX.json"
    index_md = output_root / "QUALITY_GRADE_INDEX.md"
    rerun_json = review_root / "QUALITY_RERUN_QUEUE.json"
    rerun_md = review_root / "QUALITY_RERUN_QUEUE.md"

    written_files.extend([str(index_json), str(index_md), str(rerun_json), str(rerun_md)])

    summary = QualityGradingSummary(
        project_slug=project_slug,
        generated_at_utc=_utc_now(),
        total_records=len(records),
        family_summaries=family_summaries,
        records=records,
        rerun_queue=rerun_queue,
        written_files=written_files,
        warnings=warnings,
    )

    write_json(index_json, summary.to_dict())
    index_md.write_text(_render_grade_index_markdown(summary), encoding="utf-8")
    write_json(rerun_json, rerun_queue)
    rerun_md.write_text(_render_rerun_queue_markdown(summary), encoding="utf-8")

    return QualityGradingSummary(
        project_slug=summary.project_slug,
        generated_at_utc=summary.generated_at_utc,
        total_records=summary.total_records,
        family_summaries=summary.family_summaries,
        records=summary.records,
        rerun_queue=summary.rerun_queue,
        written_files=written_files,
        warnings=warnings,
    )
