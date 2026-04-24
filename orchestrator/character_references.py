from __future__ import annotations

from pathlib import Path
from typing import Any

from .character_bible import _is_film_facing_character
from .core.json_io import read_json
from .prompt_package import PromptPackage, parse_prompt_package, write_prompt_package
from .reference_assets import (
    CHARACTER_DEFAULT_VARIANTS,
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

CHARACTER_MASTER_VARIANTS = {"full_body_neutral", "bust_portrait"}
CHARACTER_PRIMARY_MASTER_VARIANT = "full_body_neutral"
CHARACTER_T2I_WORKFLOW_ID = "still.t2i.klein.distilled"
CHARACTER_VARIANT_WORKFLOW_ID = "still.reference_variant.single_ref.klein.distilled"

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
            request["generation_stage"] = _generation_stage_for_variant(variant)
            request["generation_workflow_id"] = _workflow_for_variant(variant)
            if variant not in CHARACTER_MASTER_VARIANTS:
                request.setdefault("review_notes", []).append(
                    f"Requires an approved locked {CHARACTER_PRIMARY_MASTER_VARIANT} character reference before generation."
                )
            entries.append(request)
            if prompt_warnings:
                warnings.append(f"{character_id}/{variant}: " + "; ".join(prompt_warnings))

    written.extend(write_reference_queue(project_dir, "character", entries))
    return summarize_reference_phase(project_slug, "character", project_dir, warnings=warnings, written_files=written)


def run_character_reference_generation(
    project_slug: str,
    *,
    limit: int | None = None,
    variants: list[str] | None = None,
    character_ids: list[str] | None = None,
    execute: bool = False,
    seed: int | None = None,
    workflow_id: str | None = None,
) -> ReferencePhaseSummary:
    project_dir = create_project(project_slug)
    queue = load_reference_queue(project_dir, "character")
    selected_variants = {variant.strip().lower() for variant in variants or [] if variant.strip()}
    selected_ids = {character_id.strip().lower() for character_id in character_ids or [] if character_id.strip()}
    eligible: list[dict[str, Any]] = []
    warnings: list[str] = []
    written: list[str] = []

    for entry in queue:
        character_id = str(entry.get("asset_id", "")).strip().lower()
        variant = str(entry.get("variant_key", "")).strip().lower()
        if selected_ids and character_id not in selected_ids:
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
        character_id = str(entry.get("asset_id", "")).strip().lower()
        variant = str(entry.get("variant_key", "")).strip().lower()
        source_ref = _locked_master_reference(project_dir, character_id) if variant not in CHARACTER_MASTER_VARIANTS else ""
        if variant not in CHARACTER_MASTER_VARIANTS and not source_ref:
            note = f"{character_id}/{variant}: missing locked master reference; generate, approve, and lock {CHARACTER_PRIMARY_MASTER_VARIANT} first."
            warnings.append(note)
            entry.setdefault("review_notes", []).append(note)
            entry["status"] = "blocked"
            continue

        actual_workflow_id = workflow_id or _workflow_for_variant(variant)
        stage = _generation_stage_for_variant(variant)
        try:
            generation_prompt_path = _write_generation_prompt_package(
                project_dir,
                entry,
                workflow_id=actual_workflow_id,
                source_ref=source_ref,
            )
            ref_args = [f"source_frame={source_ref}"] if source_ref else []
            summary = run_still(
                project_slug=project_slug,
                stage=stage,
                prompt_file=str(generation_prompt_path),
                workflow_id=actual_workflow_id,
                asset_id=character_id,
                ref_args=ref_args,
                seed=seed,
                execute=execute,
            )
        except Exception as exc:
            warnings.append(f"{character_id}/{variant}: generation preparation failed: {exc}")
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
                candidate_summary = register_character_reference_candidate(
                    project_slug,
                    character_id=character_id,
                    variant=variant,
                    image_path=output_file,
                )
                written.extend(candidate_summary.written_files)

    written.extend(write_reference_queue(project_dir, "character", queue))
    return summarize_reference_phase(project_slug, "character", project_dir, warnings=warnings, written_files=written)


def register_character_reference_candidate(project_slug: str, *, character_id: str, variant: str, image_path: str) -> ReferencePhaseSummary:
    return register_reference_candidate(project_slug, asset_kind="character", asset_id=character_id, variant_key=variant, image_path=image_path)


def approve_character_reference_candidate(project_slug: str, *, candidate_id: str) -> ReferencePhaseSummary:
    return approve_reference_candidate(project_slug, asset_kind="character", candidate_id=candidate_id)


def reject_character_reference_candidate(project_slug: str, *, candidate_id: str, reason: str) -> ReferencePhaseSummary:
    return reject_reference_candidate(project_slug, asset_kind="character", candidate_id=candidate_id, reason=reason)


def lock_character_reference_candidate(project_slug: str, *, candidate_id: str) -> ReferencePhaseSummary:
    return lock_reference_candidate(project_slug, asset_kind="character", candidate_id=candidate_id)


def _generation_stage_for_variant(variant: str) -> str:
    return "character_reference" if variant in CHARACTER_MASTER_VARIANTS else "character_reference_variant"


def _workflow_for_variant(variant: str) -> str:
    return CHARACTER_T2I_WORKFLOW_ID if variant in CHARACTER_MASTER_VARIANTS else CHARACTER_VARIANT_WORKFLOW_ID


def _locked_master_reference(project_dir: Path, character_id: str) -> str:
    approved = load_approved_manifest(project_dir, "character")
    for entry in approved:
        if str(entry.get("asset_id", "")).strip().lower() != character_id.strip().lower():
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
        extra_note = f"- Use source_frame as locked identity reference: {source_ref}"
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
    output_path = project_dir / "03_reference_assets" / "characters" / asset_id / "generation_prompts" / f"{variant}_{safe_workflow}_prompt.md"
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
            for character_id, record in payload.items():
                if not isinstance(record, dict):
                    continue
                normalized_id = str(record.get("canonical_id", character_id)).strip().lower()
                if normalized_id:
                    item = dict(record)
                    item.setdefault("character_id", normalized_id)
                    item.setdefault("display_name", str(record.get("display_name", normalized_id)).strip() or normalized_id)
                    records[normalized_id] = item
            continue
        character_id = str(payload.get("character_id", payload.get("canonical_id", ""))).strip().lower()
        if character_id:
            item = dict(payload)
            item.setdefault("character_id", character_id)
            item.setdefault("display_name", str(payload.get("display_name", character_id)).strip() or character_id)
            records[character_id] = item
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
        package = parse_prompt_package(path)
    except Exception:
        return []
    missing = sorted(key for key in OPTIONAL_BUT_RECOMMENDED_CHARACTER_INPUTS if not str(package.inputs.get(key, "")).strip())
    return [f"recommended input `{key}` is missing" for key in missing]
