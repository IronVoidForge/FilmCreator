from __future__ import annotations

from pathlib import Path
from typing import Any

from .core.json_io import read_json
from .environment_bible import _is_film_facing_environment
from .prompt_package import PromptPackage, parse_prompt_package, write_prompt_package
from .reference_assets import (
    ENVIRONMENT_DEFAULT_VARIANTS,
    ReferencePhaseSummary,
    approve_reference_candidate,
    load_approved_manifest,
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
from .runner import run_still
from .scaffold import create_project

ENVIRONMENT_MASTER_VARIANTS = {"establishing_wide", "medium_spatial"}
ENVIRONMENT_PRIMARY_MASTER_VARIANT = "establishing_wide"
ENVIRONMENT_T2I_WORKFLOW_ID = "still.t2i.klein.distilled"
ENVIRONMENT_VARIANT_WORKFLOW_ID = "still.reference_variant.single_ref.klein.distilled"

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


def run_environment_reference_planning(
    project_slug: str,
    *,
    force: bool = False,
    variants: list[str] | None = None,
    limit: int | None = None,
) -> ReferencePhaseSummary:
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
    planned_assets = 0

    for environment_id, bible in sorted(environment_bibles.items()):
        if limit is not None and planned_assets >= limit:
            break
        if not _should_plan_environment(bible):
            continue
        planned_assets += 1
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
            request["generation_stage"] = _generation_stage_for_variant(variant)
            request["generation_workflow_id"] = _workflow_for_variant(variant)
            if variant not in ENVIRONMENT_MASTER_VARIANTS:
                request.setdefault("review_notes", []).append(
                    f"Requires an approved locked {ENVIRONMENT_PRIMARY_MASTER_VARIANT} environment reference before generation."
                )
            entries.append(request)
            if prompt_warnings:
                warnings.append(f"{environment_id}/{variant}: " + "; ".join(prompt_warnings))

    written.extend(write_reference_queue(project_dir, "environment", entries))
    return summarize_reference_phase(project_slug, "environment", project_dir, warnings=warnings, written_files=written)


def run_environment_reference_generation(
    project_slug: str,
    *,
    limit: int | None = None,
    variants: list[str] | None = None,
    environment_ids: list[str] | None = None,
    execute: bool = False,
    seed: int | None = None,
    workflow_id: str | None = None,
) -> ReferencePhaseSummary:
    project_dir = create_project(project_slug)
    queue = load_reference_queue(project_dir, "environment")
    selected_variants = {variant.strip().lower() for variant in variants or [] if variant.strip()}
    selected_ids = {environment_id.strip().lower() for environment_id in environment_ids or [] if environment_id.strip()}
    eligible: list[dict[str, Any]] = []
    warnings: list[str] = []
    written: list[str] = []

    for entry in queue:
        environment_id = str(entry.get("asset_id", "")).strip().lower()
        variant = str(entry.get("variant_key", "")).strip().lower()
        if selected_ids and environment_id not in selected_ids:
            continue
        if selected_variants and variant not in selected_variants:
            continue
        if str(entry.get("status", "")).strip().lower() in {"blocked", "approved", "locked"}:
            continue
        if entry.get("warnings"):
            continue
        eligible.append(entry)

    selected_entries = eligible if limit is None else eligible[:limit]
    for entry in selected_entries:
        environment_id = str(entry.get("asset_id", "")).strip().lower()
        variant = str(entry.get("variant_key", "")).strip().lower()
        source_ref = _locked_master_reference(project_dir, environment_id) if variant not in ENVIRONMENT_MASTER_VARIANTS else ""
        if variant not in ENVIRONMENT_MASTER_VARIANTS and not source_ref:
            note = f"{environment_id}/{variant}: missing locked master reference; generate, approve, and lock {ENVIRONMENT_PRIMARY_MASTER_VARIANT} first."
            warnings.append(note)
            entry.setdefault("review_notes", []).append(note)
            entry["status"] = "blocked"
            continue

        actual_workflow_id = workflow_id or _workflow_for_variant(variant)
        stage = _generation_stage_for_variant(variant)
        try:
            generation_prompt_path = _write_generation_prompt_package(project_dir, entry, workflow_id=actual_workflow_id, source_ref=source_ref)
            ref_args = [f"source_frame={source_ref}"] if source_ref else []
            summary = run_still(
                project_slug=project_slug,
                stage=stage,
                prompt_file=str(generation_prompt_path),
                workflow_id=actual_workflow_id,
                asset_id=environment_id,
                ref_args=ref_args,
                seed=seed,
                execute=execute,
            )
        except Exception as exc:
            warnings.append(f"{environment_id}/{variant}: generation preparation failed: {exc}")
            continue

        entry["generation_stage"] = stage
        entry["generation_workflow_id"] = actual_workflow_id
        entry["source_reference_image"] = source_ref
        entry["last_run_manifest"] = str(summary.manifest_path)
        entry["last_patched_workflow"] = str(summary.patched_workflow_path)
        entry["generation_ready"] = bool(summary.execution_ready)
        entry["generation_requested_execute"] = bool(summary.execute_requested)
        entry["status"] = "generated" if execute and summary.execution_ready else "prepared"
        if summary.blockers:
            entry.setdefault("review_notes", []).extend(summary.blockers)
        if summary.warnings:
            entry.setdefault("review_notes", []).extend(summary.warnings)
        if execute:
            for output_file in _manifest_output_files(summary.manifest_path):
                candidate_summary = register_environment_reference_candidate(
                    project_slug,
                    environment_id=environment_id,
                    variant=variant,
                    image_path=output_file,
                )
                written.extend(candidate_summary.written_files)

    written.extend(write_reference_queue(project_dir, "environment", queue))
    return summarize_reference_phase(project_slug, "environment", project_dir, warnings=warnings, written_files=written)


def register_environment_reference_candidate(project_slug: str, *, environment_id: str, variant: str, image_path: str) -> ReferencePhaseSummary:
    return register_reference_candidate(project_slug, asset_kind="environment", asset_id=environment_id, variant_key=variant, image_path=image_path)


def approve_environment_reference_candidate(project_slug: str, *, candidate_id: str) -> ReferencePhaseSummary:
    return approve_reference_candidate(project_slug, asset_kind="environment", candidate_id=candidate_id)


def reject_environment_reference_candidate(project_slug: str, *, candidate_id: str, reason: str) -> ReferencePhaseSummary:
    return reject_reference_candidate(project_slug, asset_kind="environment", candidate_id=candidate_id, reason=reason)


def lock_environment_reference_candidate(project_slug: str, *, candidate_id: str) -> ReferencePhaseSummary:
    return lock_reference_candidate(project_slug, asset_kind="environment", candidate_id=candidate_id)


def _generation_stage_for_variant(variant: str) -> str:
    return "environment_reference" if variant in ENVIRONMENT_MASTER_VARIANTS else "environment_reference_variant"


def _workflow_for_variant(variant: str) -> str:
    return ENVIRONMENT_T2I_WORKFLOW_ID if variant in ENVIRONMENT_MASTER_VARIANTS else ENVIRONMENT_VARIANT_WORKFLOW_ID


def _locked_master_reference(project_dir: Path, environment_id: str) -> str:
    approved = load_approved_manifest(project_dir, "environment")
    for entry in approved:
        if str(entry.get("asset_id", "")).strip().lower() != environment_id.strip().lower():
            continue
        if not entry.get("locked"):
            return ""
        return str(entry.get("canonical_reference_image", "")).strip()
    return ""


def _write_generation_prompt_package(project_dir: Path, entry: dict[str, Any], *, workflow_id: str, source_ref: str) -> Path:
    original_path = Path(str(entry.get("prompt_package_path", "")))
    package = parse_prompt_package(original_path)
    repair_notes = package.repair_notes_markdown
    if source_ref:
        extra_note = f"- Use source_frame as locked environment reference: {source_ref}"
        repair_notes = (repair_notes + "\n" + extra_note).strip() if repair_notes else extra_note
    generated = PromptPackage(
        path=package.path,
        title=package.title,
        prompt_id=package.prompt_id,
        purpose=package.purpose,
        workflow_type=workflow_id,
        positive_prompt=package.positive_prompt,
        negative_prompt=package.negative_prompt,
        inputs_markdown=package.inputs_markdown,
        continuity_notes_markdown=package.continuity_notes_markdown,
        sources_markdown=package.sources_markdown,
        repair_notes_markdown=repair_notes,
    )
    asset_id = str(entry.get("asset_id", "")).strip().lower()
    variant = str(entry.get("variant_key", "")).strip().lower()
    safe_workflow = workflow_id.replace("/", "_")
    output_path = project_dir / "03_reference_assets" / "environments" / asset_id / "generation_prompts" / f"{variant}_{safe_workflow}_prompt.md"
    write_prompt_package(output_path, generated)
    return output_path


def _manifest_output_files(manifest_path: Path) -> list[str]:
    if not manifest_path.exists():
        return []
    payload = read_json(manifest_path)
    if not isinstance(payload, dict):
        return []
    output_files = payload.get("output_files", [])
    if not isinstance(output_files, list):
        return []
    return [str(path) for path in output_files if str(path).strip()]


def _load_environment_bibles(project_dir: Path) -> dict[str, dict[str, Any]]:
    records: dict[str, dict[str, Any]] = {}
    root = project_dir / "02_story_analysis" / "bibles" / "environments"
    paths = sorted(path for path in root.glob("ENV_*.json") if path.is_file()) if root.exists() else []
    if not paths:
        fallback = project_dir / "02_story_analysis" / "world" / "global" / "ENVIRONMENT_REGISTRY_GLOBAL.json"
        paths = [fallback] if fallback.exists() else []
    for path in paths:
        payload = read_json(path)
        if isinstance(payload, dict):
            if path.name.startswith("ENVIRONMENT_REGISTRY_GLOBAL"):
                for env_id, entry in payload.items():
                    if not isinstance(entry, dict):
                        continue
                    normalized_id = str(entry.get("canonical_id", env_id)).strip().lower()
                    if not normalized_id:
                        continue
                    record = dict(entry)
                    record.setdefault("environment_id", normalized_id)
                    record.setdefault("display_name", str(entry.get("display_name", normalized_id)).strip() or normalized_id)
                    records[normalized_id] = record
                continue
            env_id = str(payload.get("environment_id", payload.get("canonical_id", ""))).strip().lower()
            if env_id:
                payload = dict(payload)
                payload.setdefault("environment_id", env_id)
                payload.setdefault("display_name", str(payload.get("display_name", env_id)).strip() or env_id)
                records[env_id] = payload
    return records


def _should_plan_environment(bible: dict[str, Any]) -> bool:
    env_id = str(bible.get("environment_id", "")).strip().lower()
    if not env_id:
        return False
    try:
        return _is_film_facing_environment({"status": str(bible.get("status", "canonical")).strip().lower(), "entity_kind": str(bible.get("entity_kind", "environment")).strip().lower()}, bible)
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
        package = parse_prompt_package(path)
    except Exception:
        return []
    return [f"recommended input `{k}` missing" for k in OPTIONAL_BUT_RECOMMENDED_ENVIRONMENT_INPUTS if not str(package.inputs.get(k, "")).strip()]
