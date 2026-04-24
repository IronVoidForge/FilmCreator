from __future__ import annotations

from pathlib import Path
from typing import Any

from .character_bible import _is_film_facing_character
from .core.json_io import read_json
from .reference_assets import (
    CHARACTER_DEFAULT_VARIANTS,
    ReferencePhaseSummary,
    approve_reference_candidate,
    load_reference_queue,
    make_reference_request,
    prompt_package_path,
    reference_root,
    register_reference_candidate,
    reject_reference_candidate,
    lock_reference_candidate,
    summarize_reference_phase,
    validate_prompt_package,
    write_reference_queue,
)
from .scaffold import create_project

REQUIRED_CHARACTER_REFERENCE_INPUTS = {
    "subject_kind",
    "subject_id",
    "source_artifact_ids",
    "reference_mode",
    "variant_name",
    "reuse_policy",
}

OPTIONAL_BUT_RECOMMENDED_CHARACTER_INPUTS = {
    "display_name",
    "identity_descriptor",
    "body_descriptor",
    "face_descriptor",
    "costume_descriptor",
    "posture_descriptor",
    "expression_descriptor",
    "locked_fields",
}


def run_character_reference_planning(
    project_slug: str,
    *,
    force: bool = False,
    variants: list[str] | None = None,
    limit: int | None = None,
) -> ReferencePhaseSummary:
    project_dir = create_project(project_slug)
    character_bibles = _load_character_bibles(project_dir)
    selected_variants = [variant.strip().lower() for variant in (variants or CHARACTER_DEFAULT_VARIANTS) if variant.strip()]
    existing = [] if force else load_reference_queue(project_dir, "character")
    existing_by_key = {
        (str(entry.get("asset_id", "")).strip().lower(), str(entry.get("variant_key", "")).strip().lower()): entry
        for entry in existing
    }
    entries: list[dict[str, Any]] = []
    warnings: list[str] = []
    written: list[str] = []
    planned_assets = 0

    for character_id, bible in sorted(character_bibles.items()):
        if limit is not None and planned_assets >= limit:
            break
        if not _should_plan_character(bible):
            continue
        planned_assets += 1
        priority = _character_priority(bible)
        for variant in selected_variants:
            key = (character_id, variant)
            if key in existing_by_key:
                entries.append(existing_by_key[key])
                continue
            path = prompt_package_path(project_dir, "character", character_id, variant)
            prompt_warnings = validate_prompt_package(path, REQUIRED_CHARACTER_REFERENCE_INPUTS)
            prompt_warnings.extend(_recommended_input_warnings(path))
            request = make_reference_request(
                asset_kind="character",
                asset_id=character_id,
                variant_key=variant,
                prompt_path=path,
                priority=priority,
                warnings=prompt_warnings,
            )
            entries.append(request)
            if prompt_warnings:
                warnings.append(f"{character_id}/{variant}: " + "; ".join(prompt_warnings))

    written.extend(write_reference_queue(project_dir, "character", entries))
    return summarize_reference_phase(project_slug, "character", project_dir, warnings=warnings, written_files=written)


def register_character_reference_candidate(
    project_slug: str,
    *,
    character_id: str,
    variant: str,
    image_path: str,
) -> ReferencePhaseSummary:
    return register_reference_candidate(
        project_slug,
        asset_kind="character",
        asset_id=character_id,
        variant_key=variant,
        image_path=image_path,
    )


def approve_character_reference_candidate(project_slug: str, *, candidate_id: str) -> ReferencePhaseSummary:
    return approve_reference_candidate(project_slug, asset_kind="character", candidate_id=candidate_id)


def reject_character_reference_candidate(project_slug: str, *, candidate_id: str, reason: str) -> ReferencePhaseSummary:
    return reject_reference_candidate(project_slug, asset_kind="character", candidate_id=candidate_id, reason=reason)


def lock_character_reference_candidate(project_slug: str, *, candidate_id: str) -> ReferencePhaseSummary:
    return lock_reference_candidate(project_slug, asset_kind="character", candidate_id=candidate_id)


def _load_character_bibles(project_dir: Path) -> dict[str, dict[str, Any]]:
    records: dict[str, dict[str, Any]] = {}
    root = project_dir / "02_story_analysis" / "bibles" / "characters"
    paths = sorted(path for path in root.glob("CHAR_*.json") if path.is_file()) if root.exists() else []
    if not paths:
        fallback = project_dir / "02_story_analysis" / "world" / "global" / "CHARACTER_REGISTRY_GLOBAL.json"
        paths = [fallback] if fallback.exists() else []
    for path in paths:
        payload = read_json(path)
        if not isinstance(payload, dict):
            continue
        if path.name.startswith("CHARACTER_REGISTRY_GLOBAL"):
            for character_id, entry in payload.items():
                if not isinstance(entry, dict):
                    continue
                normalized_id = str(entry.get("canonical_id", character_id)).strip().lower()
                if not normalized_id:
                    continue
                record = dict(entry)
                record.setdefault("character_id", normalized_id)
                record.setdefault("display_name", str(entry.get("display_name", normalized_id)).strip() or normalized_id)
                records[normalized_id] = record
            continue
        character_id = str(payload.get("character_id", payload.get("canonical_id", ""))).strip().lower()
        if character_id:
            payload = dict(payload)
            payload.setdefault("character_id", character_id)
            payload.setdefault("display_name", str(payload.get("display_name", character_id)).strip() or character_id)
            records[character_id] = payload
    return records


def _should_plan_character(bible: dict[str, Any]) -> bool:
    character_id = str(bible.get("character_id", "")).strip().lower()
    if not character_id:
        return False
    status = str(bible.get("status", "canonical")).strip().lower()
    if status not in {"", "canonical"}:
        return False
    try:
        return _is_film_facing_character({"status": status, "entity_kind": str(bible.get("entity_kind", "individual")).strip().lower()}, bible)
    except Exception:
        return True


def _character_priority(bible: dict[str, Any]) -> str:
    role = " ".join(str(value).lower() for value in [bible.get("role", ""), bible.get("narrative_role", ""), bible.get("story_role", "")])
    if any(term in role for term in ["protagonist", "lead", "major", "main", "primary"]):
        return "high"
    if any(term in role for term in ["supporting", "recurring", "secondary"]):
        return "medium"
    return "normal"


def _recommended_input_warnings(path: Path) -> list[str]:
    if not path.exists():
        return []
    try:
        from .prompt_package import parse_prompt_package

        package = parse_prompt_package(path)
    except Exception:
        return []
    missing = sorted(key for key in OPTIONAL_BUT_RECOMMENDED_CHARACTER_INPUTS if not str(package.inputs.get(key, "")).strip())
    return [f"recommended input `{key}` is missing" for key in missing]
