from __future__ import annotations

from pathlib import Path
from typing import Any

from .core.json_io import read_json
from .environment_bible import _is_film_facing_environment
from .reference_assets import (
    ENVIRONMENT_DEFAULT_VARIANTS,
    ReferencePhaseSummary,
    approve_reference_candidate,
    load_reference_queue,
    make_reference_request,
    prompt_package_path,
    register_reference_candidate,
    reject_reference_candidate,
    lock_reference_candidate,
    summarize_reference_phase,
    validate_prompt_package,
    write_reference_queue,
)
from .scaffold import create_project

REQUIRED_ENVIRONMENT_REFERENCE_INPUTS = {
    "subject_kind",
    "subject_id",
    "source_artifact_ids",
    "reference_mode",
    "variant_name",
    "reuse_policy",
}

OPTIONAL_BUT_RECOMMENDED_ENVIRONMENT_INPUTS = {
    "display_name",
    "layout_descriptor",
    "scale_descriptor",
    "architecture_descriptor",
    "landmark_descriptor",
    "lighting_descriptor",
    "mood_descriptor",
    "locked_fields",
}


def run_environment_reference_planning(project_slug: str, *, force: bool = False, variants: list[str] | None = None, limit: int | None = None) -> ReferencePhaseSummary:
    project_dir = create_project(project_slug)
    environment_bibles = _load_environment_bibles(project_dir)
    selected_variants = [variant.strip().lower() for variant in (variants or ENVIRONMENT_DEFAULT_VARIANTS) if variant.strip()]
    existing = [] if force else load_reference_queue(project_dir, "environment")
    existing_by_key = {
        (str(entry.get("asset_id", "")).strip().lower(), str(entry.get("variant_key", "")).strip().lower()): entry
        for entry in existing
    }
    entries: list[dict[str, Any]] = []
    warnings: list[str] = []
    written: list[str] = []

    for environment_id, bible in sorted(environment_bibles.items()):
        if not _should_plan_environment(bible):
            continue
        priority = _environment_priority(bible)
        for variant in selected_variants:
            key = (environment_id, variant)
            if key in existing_by_key:
                entries.append(existing_by_key[key])
                continue
            path = prompt_package_path(project_dir, "environment", environment_id, variant)
            prompt_warnings = validate_prompt_package(path, REQUIRED_ENVIRONMENT_REFERENCE_INPUTS)
            prompt_warnings.extend(_recommended_input_warnings(path))
            request = make_reference_request(
                asset_kind="environment",
                asset_id=environment_id,
                variant_key=variant,
                prompt_path=path,
                priority=priority,
                warnings=prompt_warnings,
            )
            entries.append(request)

    written.extend(write_reference_queue(project_dir, "environment", entries))
    return summarize_reference_phase(project_slug, "environment", project_dir, warnings=warnings, written_files=written)


def register_environment_reference_candidate(project_slug: str, *, environment_id: str, variant: str, image_path: str) -> ReferencePhaseSummary:
    return register_reference_candidate(project_slug, asset_kind="environment", asset_id=environment_id, variant_key=variant, image_path=image_path)


def approve_environment_reference_candidate(project_slug: str, *, candidate_id: str) -> ReferencePhaseSummary:
    return approve_reference_candidate(project_slug, asset_kind="environment", candidate_id=candidate_id)


def reject_environment_reference_candidate(project_slug: str, *, candidate_id: str, reason: str) -> ReferencePhaseSummary:
    return reject_reference_candidate(project_slug, asset_kind="environment", candidate_id=candidate_id, reason=reason)


def lock_environment_reference_candidate(project_slug: str, *, candidate_id: str) -> ReferencePhaseSummary:
    return lock_reference_candidate(project_slug, asset_kind="environment", candidate_id=candidate_id)


def _load_environment_bibles(project_dir: Path) -> dict[str, dict[str, Any]]:
    root = project_dir / "02_story_analysis" / "bibles" / "environments"
    if not root.exists():
        return {}
    records: dict[str, dict[str, Any]] = {}
    for path in sorted(root.glob("ENV_*.json")):
        payload = read_json(path)
        if isinstance(payload, dict):
            env_id = str(payload.get("environment_id", "")).strip().lower()
            if env_id:
                records[env_id] = payload
    return records


def _should_plan_environment(bible: dict[str, Any]) -> bool:
    env_id = str(bible.get("environment_id", "")).strip().lower()
    if not env_id:
        return False
    try:
        return _is_film_facing_environment({"canonical_id": env_id}, bible)
    except Exception:
        return True


def _environment_priority(bible: dict[str, Any]) -> str:
    role = " ".join(str(v).lower() for v in [bible.get("role", ""), bible.get("narrative_role", "")])
    if "main" in role or "primary" in role:
        return "high"
    if "secondary" in role:
        return "medium"
    return "normal"


def _recommended_input_warnings(path: Path) -> list[str]:
    try:
        from .prompt_package import parse_prompt_package
        package = parse_prompt_package(path)
    except Exception:
        return []
    return [f"recommended input `{k}` missing" for k in OPTIONAL_BUT_RECOMMENDED_ENVIRONMENT_INPUTS if not str(package.inputs.get(k, "")).strip()]
