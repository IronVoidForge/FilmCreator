from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .core.json_io import read_json, write_json
from .features.authoring.packet_parser import parse_packet_document
from .lmstudio_client import LMStudioClient
from .scaffold import create_project
from .settings import load_runtime_settings


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
    previous_shot_id: str = ""
    next_shot_id: str = ""
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
            "shot_title": self.shot_title,
            "shot_type": self.shot_type,
            "camera_description": self.camera_description,
            "composition": self.composition,
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


def _clean_label(value: object, *, fallback: str) -> str:
    if isinstance(value, str):
        cleaned = value.strip()
        if cleaned and cleaned.lower() not in {"none", "(none)", "n/a"}:
            return cleaned
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
            parts = [part.strip() for part in re.split(r",|\n", stripped) if part.strip()]
            if parts:
                items.extend(parts)
            else:
                items.append(stripped)

    seen: set[str] = set()
    deduped: list[str] = []
    for item in items:
        if item not in seen:
            seen.add(item)
            deduped.append(item)
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


def _normalize_asset_label(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", value.strip().lower()).strip("_")


def _scene_contract_root(project_dir: Path) -> Path:
    return project_dir / "02_story_analysis" / "contracts" / "scenes"


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
    normalized_text = _normalize_asset_label(text)
    if not normalized_text:
        return None
    for ref in refs:
        candidates = [
            _normalize_asset_label(str(ref.get("label", ""))),
            _normalize_asset_label(str(ref.get("display_name", ""))),
            _normalize_asset_label(str(ref.get("canonical_id", ""))),
        ]
        if normalized_text in candidates or any(candidate and candidate in normalized_text for candidate in candidates):
            return ref
    return None


def _select_environment_ref(scene_contract: dict[str, Any], project_dir: Path) -> ShotReference:
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
        canonical_id = str(raw_ref.get("canonical_id") or "").strip()
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
        canonical_id = str(raw_ref.get("canonical_id") or "").strip() or None
        bible = _load_environment_bible(project_dir, canonical_id) if canonical_id else None
        return ShotReference(
            label=str(raw_ref.get("label", "environment")),
            canonical_id=canonical_id,
            display_name=_first_nonempty(str((bible or {}).get("display_name", "")), str(raw_ref.get("display_name", "")), fallback=str(raw_ref.get("label", "environment"))),
            status=str(raw_ref.get("status", (bible or {}).get("status", "review"))),
            entity_kind=str(raw_ref.get("entity_kind", (bible or {}).get("entity_kind", "environment"))),
            source_path=str(raw_ref.get("source_path", "")),
            notes=str(raw_ref.get("notes", "")),
        )

    return ShotReference(label="environment", display_name="environment", status="review", entity_kind="environment")


def _build_character_reference(project_dir: Path, raw_ref: dict[str, Any]) -> ShotReference:
    canonical_id = str(raw_ref.get("canonical_id") or "").strip() or None
    bible = _load_character_bible(project_dir, canonical_id) if canonical_id else None
    display_name = _first_nonempty(
        str((bible or {}).get("display_name", "")),
        str(raw_ref.get("display_name", "")),
        fallback=str(raw_ref.get("label", canonical_id or "")),
    )
    return ShotReference(
        label=str(raw_ref.get("label", display_name)),
        canonical_id=canonical_id,
        display_name=display_name,
        status=str(raw_ref.get("status", (bible or {}).get("status", "review"))),
        entity_kind=str(raw_ref.get("entity_kind", (bible or {}).get("entity_kind", "individual"))),
        resolution_score=int(raw_ref.get("resolution_score")) if str(raw_ref.get("resolution_score", "")).isdigit() else raw_ref.get("resolution_score"),
        source_path=str(raw_ref.get("source_path", "")),
        notes=str(raw_ref.get("notes", "")),
    )


def _selected_characters(scene_contract: dict[str, Any], project_dir: Path, beat_summary: str, shot_order: int) -> list[ShotReference]:
    raw_refs = scene_contract.get("characters_required", [])
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


def _shot_type_from_beat(scene_contract: dict[str, Any], beat_summary: str, shot_order: int) -> str:
    text = f"{scene_contract.get('visual_coverage_families', [])} {beat_summary}".lower()
    if shot_order == 1 and any(term in text for term in ["wide", "establish", "aerial", "opening", "overview"]):
        return "establishing_wide"
    if any(term in text for term in ["crash", "battle", "attack", "fight", "chase", "charge", "action"]):
        return "action"
    if any(term in text for term in ["reaction", "respond", "reveal", "realize", "recognize"]):
        return "reaction_closeup"
    if any(term in text for term in ["insert", "detail", "prop", "object", "hand"]):
        return "insert_detail"
    if any(term in text for term in ["over-the-shoulder", "over the shoulder", "dialogue", "conversation"]):
        return "over_the_shoulder"
    if shot_order == len(scene_contract.get("beat_list", []) or []):
        return "closing_reaction"
    return "medium"


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
    cast = ", ".join(ref.display_name for ref in characters[:3]) or "scene cast"
    env = environment.display_name or environment.label
    if shot_type == "establishing_wide":
        return f"Wide composition across {env} with {cast} placed for immediate spatial orientation."
    if shot_type == "action":
        return f"Dynamic composition in {env} with {cast} crossing the frame and maintaining readable movement."
    if shot_type == "reaction_closeup":
        return f"Intimate composition that isolates {cast} against {env} to capture the beat's emotional turn."
    if shot_type == "insert_detail":
        return f"Detail composition centered on the key physical action or prop inside {env}."
    if shot_type == "over_the_shoulder":
        return f"Over-the-shoulder composition in {env} with {cast} sharing the frame for dialogue or tension."
    if shot_type == "closing_reaction":
        return f"Closing composition in {env} that emphasizes the consequence of {beat_summary.lower()}."
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
) -> str:
    cast = ", ".join(ref.display_name or ref.label for ref in characters[:3]) or "none"
    env = environment.display_name or environment.label
    return _compact_snippet(
        f"{shot_title}. {shot_type}. {camera_description} {composition} Cast: {cast}. Environment: {env}. Beat: {beat_summary}",
        limit=320,
    )


def _shot_title_from_beat(shot_type: str, beat_summary: str, shot_order: int) -> str:
    snippet = _compact_snippet(beat_summary, limit=54)
    if snippet:
        return f"{shot_type.replace('_', ' ').title()} {shot_order}: {snippet}"
    return f"{shot_type.replace('_', ' ').title()} {shot_order}"


def _build_shot_blueprints(scene_contract: dict[str, Any], project_dir: Path) -> list[dict[str, Any]]:
    beats = scene_contract.get("beat_list", [])
    if not isinstance(beats, list) or not beats:
        beats = [{"beat_id": "BT001", "summary": scene_contract.get("summary", "") or scene_contract.get("production_intent", "") or scene_contract.get("scene_title", "")}]

    environment = _select_environment_ref(scene_contract, project_dir)
    blueprints: list[dict[str, Any]] = []
    for index, raw_beat in enumerate(beats, start=1):
        beat_id = f"BT{index:03d}"
        beat_summary = ""
        if isinstance(raw_beat, dict):
            beat_id = str(raw_beat.get("beat_id", beat_id)).strip().upper() or beat_id
            beat_summary = _first_nonempty(
                str(raw_beat.get("summary", "")),
                str(raw_beat.get("markdown", "")),
                fallback="",
            )
        elif isinstance(raw_beat, str):
            beat_summary = raw_beat.strip()
        shot_type = _shot_type_from_beat(scene_contract, beat_summary, index)
        characters = _selected_characters(scene_contract, project_dir, beat_summary, index)
        camera_description = _camera_description(shot_type, beat_summary)
        composition = _composition_description(shot_type, characters, environment, beat_summary)
        shot_title = _shot_title_from_beat(shot_type, beat_summary, index)
        prompt_seed = _prompt_seed(
            shot_title=shot_title,
            shot_type=shot_type,
            camera_description=camera_description,
            composition=composition,
            characters=characters,
            environment=environment,
            beat_summary=beat_summary,
        )
        continuity_constraints = _coerce_string_list(
            scene_contract.get("continuity_constraints", []),
            beat_summary,
            scene_contract.get("unresolved_questions", []),
        )
        blueprints.append(
            {
                "shot_id": f"SH{index:03d}",
                "shot_order": index,
                "beat_ids": [beat_id],
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
    return blueprints


def _load_shot_planning_evidence(
    *,
    project_dir: Path,
    scene_contract: dict[str, Any],
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
        *[_compact_snippet(str(item), limit=220) for item in _coerce_string_list(scene_contract.get("visual_coverage_families", []))[:4]],
        *[_compact_snippet(str(item), limit=220) for item in _coerce_string_list(scene_contract.get("continuity_constraints", []))[:4]],
    ]
    scene_evidence = [item for item in scene_evidence if item]

    fingerprint_payload = {
        "scene_contract": scene_contract,
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
shot_type: <shot type>
camera_description: <camera note>
composition: <composition note>
characters_in_frame:
- john_carter
- tars_tarkas
environment: <environment reference or label>
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
                    "shot_title": _first_nonempty(scalars.get("shot_title"), fallback=""),
                    "shot_type": _first_nonempty(scalars.get("shot_type"), fallback=""),
                    "camera_description": _first_nonempty(scalars.get("camera_description"), fallback=""),
                    "composition": _first_nonempty(scalars.get("composition"), fallback=""),
                    "characters_in_frame": _coerce_string_list(lists.get("characters_in_frame"), scalars.get("characters_in_frame")),
                    "environment": _first_nonempty(scalars.get("environment"), fallback=""),
                    "continuity_constraints": _coerce_string_list(lists.get("continuity_constraints"), scalars.get("continuity_constraints")),
                    "prompt_seed": _first_nonempty(scalars.get("prompt_seed"), freeform[0] if freeform else None, fallback=""),
                    "shot_notes": _first_nonempty(scalars.get("shot_notes"), fallback=""),
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
        "shot_title": str(payload.get("shot_title", "")),
        "shot_type": str(payload.get("shot_type", "")),
        "camera_description": str(payload.get("camera_description", "")),
        "composition": str(payload.get("composition", "")),
        "beat_ids": _coerce_string_list(payload.get("beat_ids", [])),
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
        "",
        "## Camera",
        "",
        package.camera_description or "(none)",
        "",
        "## Composition",
        "",
        package.composition or "(none)",
        "",
        "## Characters",
        "",
    ]
    if characters:
        lines.extend([f"- {ref.display_name or ref.label} (`{ref.canonical_id or ref.label}`)" for ref in characters])
    else:
        lines.append("- (none)")
    lines.extend(
        [
            "",
            "## Environment",
            "",
            f"- {environment.display_name or environment.label} (`{environment.canonical_id or environment.label}`)",
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
            f"(type={record.shot_type}, beat_ids={', '.join(record.beat_ids) or '(none)'}, cast={len(record.characters_in_frame)}, env={env_name}, "
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
            f"(type={record.shot_type}, cast={len(record.characters_in_frame)}, env={record.environment.display_name if record.environment else '(none)'}, "
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
) -> ShotPlanningSummary:
    project_dir = create_project(project_slug)
    scene_contract_files = _scene_contract_files(project_dir)

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

    for scene_index, scene_contract_path in enumerate(scene_contract_files, start=1):
        scene_started_at = time.perf_counter()
        scene_contract = _load_json_file(scene_contract_path)
        scene_id = str(scene_contract.get("scene_id", "")).strip().upper() or scene_contract_path.stem.upper()
        chapter_id = str(scene_contract.get("chapter_id", "")).strip().upper() or _chapter_id_from_scene_id(scene_id)
        scene_title = _scene_contract_to_scene_title(scene_contract)
        scene_dir = output_root / chapter_id / scene_id
        scene_dir.mkdir(parents=True, exist_ok=True)
        print(f"[shot-planner] {scene_index}/{total_scenes} starting {scene_id}...")

        shot_blueprints = _build_shot_blueprints(scene_contract, project_dir)
        evidence = _load_shot_planning_evidence(
            project_dir=project_dir,
            scene_contract=scene_contract,
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
            base_path = scene_dir / shot_id
            existing = read_json(base_path.with_suffix(".json")) if base_path.with_suffix(".json").exists() else None
            metadata = _shot_package_metadata(existing, artifact_id=f"{scene_id}_{shot_id}_SHOT_PACKAGE", fp=fp)

            if existing and not force:
                old_meta = existing.get("metadata") or {}
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
            environment_ref = ShotReference(
                label=_clean_label(environment_payload.get("label"), fallback="environment"),
                canonical_id=(str(environment_payload.get("canonical_id", "")).strip() or None),
                display_name=_clean_label(
                    environment_payload.get("display_name"),
                    fallback=_clean_label(environment_payload.get("label"), fallback="environment"),
                ),
                status=str(environment_payload.get("status", "review")),
                entity_kind=str(environment_payload.get("entity_kind", "environment")),
                resolution_score=environment_payload.get("resolution_score"),
                source_path=str(environment_payload.get("source_path", "")),
                notes=str(environment_payload.get("notes", "")),
            )
            character_payloads = merged.get("characters_in_frame", [])
            character_refs = [ShotReference(**item) for item in character_payloads if isinstance(item, dict)]

            package = ShotPackage(
                shot_id=shot_id,
                scene_id=scene_id,
                chapter_id=chapter_id,
                shot_order=int(merged.get("shot_order", len(scene_shots) + 1) or len(scene_shots) + 1),
                shot_title=_first_nonempty(merged.get("shot_title"), fallback=f"{scene_title} {shot_id}"),
                shot_type=_first_nonempty(merged.get("shot_type"), fallback="medium"),
                camera_description=_first_nonempty(merged.get("camera_description"), fallback="Stable readable framing."),
                composition=_first_nonempty(merged.get("composition"), fallback="Readable composition."),
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
                composition=package.composition,
                characters=package.characters_in_frame,
                environment=package.environment or environment_ref,
                beat_summary=_first_nonempty(scene_contract.get("summary", ""), scene_contract.get("production_intent", ""), fallback=""),
            )
            package.shot_notes = package.shot_notes or _compact_snippet(str(scene_contract.get("summary", "")), limit=220)

            _write_shot_package_files(base_path, package)
            scene_written_files.extend([str(base_path.with_suffix(".json")), str(base_path.with_suffix(".md"))])
            written_files.extend([str(base_path.with_suffix(".json")), str(base_path.with_suffix(".md"))])
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
    return ShotPackage(
        shot_id=str(existing.get("shot_id", "")),
        scene_id=str(existing.get("scene_id", "")),
        chapter_id=str(existing.get("chapter_id", "")),
        shot_order=int(existing.get("shot_order", 0) or 0),
        shot_title=str(existing.get("shot_title", "")),
        shot_type=str(existing.get("shot_type", "")),
        camera_description=str(existing.get("camera_description", "")),
        composition=str(existing.get("composition", "")),
        characters_in_frame=[ShotReference(**item) for item in existing.get("characters_in_frame", []) if isinstance(item, dict)],
        environment=ShotReference(**environment_payload) if environment_payload else None,
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
    queue.append(
        {
            "shot_id": package.shot_id,
            "scene_id": package.scene_id,
            "issues": issues,
        }
    )
