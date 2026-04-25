from __future__ import annotations

from pathlib import Path
from typing import Any

from .chapter_selection import any_chapter_matches, parse_chapter_selector
from .core.json_io import read_json
from .environment_bible import _is_film_facing_environment
from .prompt_boosters import apply_booster_bundles
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
ENVIRONMENT_VALIDATION_SLICE_LIMIT = 2
ENVIRONMENT_VALIDATION_SLICE_STAGES = {
    "establishing": {"establishing_wide"},
    "spatial": {"medium_spatial"},
    "supporting": {"detail_focus", "lighting_variant", "time_of_day", "interior_layout", "exterior_geography"},
}

REQUIRED_ENVIRONMENT_REFERENCE_INPUTS = {"subject_kind", "subject_id", "source_artifact_ids", "reference_mode", "variant_name", "reuse_policy"}
OPTIONAL_BUT_RECOMMENDED_ENVIRONMENT_INPUTS = {"display_name", "layout_descriptor", "scale_descriptor", "architecture_descriptor", "landmark_descriptor", "lighting_descriptor", "mood_descriptor", "locked_fields"}


def run_environment_reference_planning(project_slug: str, *, force: bool = False, variants: list[str] | None = None, limit: int | None = None, test_slice: bool = False) -> ReferencePhaseSummary:
    project_dir = create_project(project_slug)
    environment_bibles = _load_environment_bibles(project_dir)
    selected_variants = _selected_variants(variants, test_slice=test_slice)
    existing = [] if force else load_reference_queue(project_dir, "environment")
    existing_by_key = {(str(e.get("asset_id", "")).strip().lower(), str(e.get("variant_key", "")).strip().lower()): e for e in existing}
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
                entry = existing_by_key[key]
                if test_slice:
                    entry["validation_slice"] = True
                    entry["validation_slice_stage"] = _validation_slice_stage_for_variant(variant)
                entries.append(entry)
                continue
            path = prompt_package_path(project_dir, "environment", environment_id, variant)
            blocking_warnings = validate_prompt_package(path, REQUIRED_ENVIRONMENT_REFERENCE_INPUTS)
            recommended_warnings = _recommended_input_warnings(path)
            prompt_warnings = blocking_warnings + recommended_warnings
            
            request = make_reference_request(asset_kind="environment", asset_id=environment_id, variant_key=variant, prompt_path=path, priority=priority, warnings=prompt_warnings)
            request["status"] = "blocked" if blocking_warnings else "prepared"
            request["blocking_warnings"] = blocking_warnings
            request["recommended_warnings"] = recommended_warnings
            request["generation_stage"] = _generation_stage_for_variant(variant)
            request["generation_workflow_id"] = _workflow_for_variant(variant)
            if test_slice:
                request["validation_slice"] = True
                request["validation_slice_stage"] = _validation_slice_stage_for_variant(variant)
            if variant == "medium_spatial":
                request.setdefault("review_notes", []).append("Validation order: derive spatial reference from an approved locked establishing reference when available.")
            if variant not in ENVIRONMENT_MASTER_VARIANTS:
                request.setdefault("review_notes", []).append(f"Requires an approved locked {ENVIRONMENT_PRIMARY_MASTER_VARIANT} environment reference before generation.")
            entries.append(request)
            if blocking_warnings:
                warnings.append(f"{environment_id}/{variant} (BLOCKING): " + "; ".join(blocking_warnings))
            if recommended_warnings:
                warnings.append(f"{environment_id}/{variant} (RECOMMENDED): " + "; ".join(recommended_warnings))

    if test_slice:
        entries = _apply_validation_slice_caps(entries)
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
    test_slice: bool = False,
    chapters: str | None = None,
    prompt_variant_id: str = "raw",
    booster_bundle_ids: list[str] | None = None,
) -> ReferencePhaseSummary:
    project_dir = create_project(project_slug)
    queue = load_reference_queue(project_dir, "environment")
    selected_variants = {v.strip().lower() for v in variants or [] if v.strip()}
    selected_ids = {e.strip().lower() for e in environment_ids or [] if e.strip()}
    selected_chapters = set(parse_chapter_selector(chapters))
    eligible: list[dict[str, Any]] = []
    warnings: list[str] = []
    written: list[str] = []

    if test_slice:
        eligible = _prompt_prepared_entries(project_dir, "environment", selected_variants, selected_ids)
        if selected_chapters:
            eligible = [e for e in eligible if any_chapter_matches(e.get("chapter_mentions", []), selected_chapters)]

    if not eligible:
        for entry in queue:
            environment_id = str(entry.get("asset_id", "")).strip().lower()
            variant = str(entry.get("variant_key", "")).strip().lower()
            if selected_ids and environment_id not in selected_ids:
                continue
            if selected_variants and variant not in selected_variants:
                continue
            if selected_chapters and not any_chapter_matches(entry.get("chapter_mentions", []), selected_chapters):
                continue
            status = str(entry.get("status", "")).strip().lower()
            if status in {"approved", "locked"}:
                continue
            if status == "blocked" and not test_slice:
                continue
            
            # Recommended warnings should not block generation
            blocking = entry.get("blocking_warnings", [])
            if blocking and not test_slice:
                continue
                
            eligible.append(entry)

    if test_slice:
        if selected_chapters:
            environment_bibles = _load_environment_bibles(project_dir)
            eligible = _rank_environment_entries(eligible, environment_bibles, selected_chapters)
            slice_limit = limit if limit is not None else 2
            eligible = eligible[:slice_limit]
        else:
            eligible = _apply_validation_slice_caps(eligible)
            if limit is not None:
                eligible = eligible[:limit]
                
    selected_entries = eligible if (test_slice and selected_chapters) else (eligible if limit is None else eligible[:limit])
    for entry in selected_entries:
        environment_id = str(entry.get("asset_id", "")).strip().lower()
        variant = str(entry.get("variant_key", "")).strip().lower()
        source_ref = _source_reference_for_variant(project_dir, environment_id, variant)
        if _requires_source_reference(variant) and not source_ref:
            note = _missing_gate_note(environment_id, variant)
            warnings.append(note)
            entry.setdefault("review_notes", []).append(note)
            entry["status"] = "blocked"
            continue
        actual_workflow_id = workflow_id or _workflow_for_variant(variant, has_source=bool(source_ref))
        stage = _generation_stage_for_variant(variant, has_source=bool(source_ref))
        try:
            generation_prompt_path = _write_generation_prompt_package(
                project_dir,
                entry,
                workflow_id=actual_workflow_id,
                source_ref=source_ref,
                prompt_variant_id=prompt_variant_id,
                booster_bundle_ids=booster_bundle_ids,
            )
            ref_args = [f"image1={source_ref}"] if source_ref else []
            summary = run_still(project_slug=project_slug, stage=stage, prompt_file=str(generation_prompt_path), workflow_id=actual_workflow_id, asset_id=environment_id, ref_args=ref_args, seed=seed, execute=execute)
        except Exception as exc:
            warnings.append(f"{environment_id}/{variant}: generation preparation failed: {exc}")
            continue
        entry["prompt_variant_id"] = prompt_variant_id
        entry["booster_bundle_ids"] = [bid for bid in (booster_bundle_ids or []) if str(bid).strip()]
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
                candidate_summary = register_environment_reference_candidate(project_slug, environment_id=environment_id, variant=variant, image_path=output_file)
                written.extend(candidate_summary.written_files)
    queue_to_write = eligible if test_slice and eligible else queue
    written.extend(write_reference_queue(project_dir, "environment", queue_to_write))
    return summarize_reference_phase(project_slug, "environment", project_dir, warnings=warnings, written_files=written)


def register_environment_reference_candidate(project_slug: str, *, environment_id: str, variant: str, image_path: str) -> ReferencePhaseSummary:
    return register_reference_candidate(project_slug, asset_kind="environment", asset_id=environment_id, variant_key=variant, image_path=image_path)

def approve_environment_reference_candidate(project_slug: str, *, candidate_id: str) -> ReferencePhaseSummary:
    return approve_reference_candidate(project_slug, asset_kind="environment", candidate_id=candidate_id)

def reject_environment_reference_candidate(project_slug: str, *, candidate_id: str, reason: str) -> ReferencePhaseSummary:
    return reject_reference_candidate(project_slug, asset_kind="environment", candidate_id=candidate_id, reason=reason)

def lock_environment_reference_candidate(project_slug: str, *, candidate_id: str) -> ReferencePhaseSummary:
    return lock_reference_candidate(project_slug, asset_kind="environment", candidate_id=candidate_id)


def _selected_variants(variants: list[str] | None, *, test_slice: bool) -> list[str]:
    if variants:
        return [v.strip().lower() for v in variants if v.strip()]
    if test_slice:
        return ["establishing_wide", "medium_spatial", "detail_focus"]
    return [v.strip().lower() for v in ENVIRONMENT_DEFAULT_VARIANTS if v.strip()]


def _validation_slice_stage_for_variant(variant: str) -> str:
    for stage, variants in ENVIRONMENT_VALIDATION_SLICE_STAGES.items():
        if variant in variants:
            return stage
    return "supporting"


def _apply_validation_slice_caps(entries: list[dict[str, Any]]) -> list[dict[str, Any]]:
    counts = {"establishing": 0, "spatial": 0, "supporting": 0}
    capped: list[dict[str, Any]] = []
    for entry in entries:
        stage = str(entry.get("validation_slice_stage") or _validation_slice_stage_for_variant(str(entry.get("variant_key", ""))))
        if stage not in counts:
            stage = "supporting"
        if counts[stage] >= ENVIRONMENT_VALIDATION_SLICE_LIMIT:
            continue
        counts[stage] += 1
        entry["validation_slice"] = True
        entry["validation_slice_stage"] = stage
        capped.append(entry)
    return capped


def _generation_stage_for_variant(variant: str, *, has_source: bool = False) -> str:
    return "environment_reference_variant" if has_source else "environment_reference"


def _workflow_for_variant(variant: str, *, has_source: bool = False) -> str:
    return ENVIRONMENT_VARIANT_WORKFLOW_ID if has_source else ENVIRONMENT_T2I_WORKFLOW_ID


def _requires_source_reference(variant: str) -> bool:
    return variant not in {"establishing_wide"}


def _source_reference_for_variant(project_dir: Path, environment_id: str, variant: str) -> str:
    if variant == "medium_spatial":
        return _locked_reference_for_variant(project_dir, environment_id, "establishing_wide")
    if variant == "establishing_wide":
        return ""
    return _locked_reference_for_variant(project_dir, environment_id, "medium_spatial") or _locked_master_reference(project_dir, environment_id)


def _missing_gate_note(environment_id: str, variant: str) -> str:
    if variant == "medium_spatial":
        return f"{environment_id}/{variant}: missing locked establishing_wide reference; generate, approve, and lock establishing first."
    return f"{environment_id}/{variant}: missing locked medium_spatial reference; generate, approve, and lock spatial reference first."


def _locked_master_reference(project_dir: Path, environment_id: str) -> str:
    approved = load_approved_manifest(project_dir, "environment")
    for entry in approved:
        if str(entry.get("asset_id", "")).strip().lower() != environment_id.strip().lower():
            continue
        if not entry.get("locked"):
            return ""
        return str(entry.get("canonical_reference_image", "")).strip()
    return ""


def _locked_reference_for_variant(project_dir: Path, environment_id: str, variant: str) -> str:
    approved = load_approved_manifest(project_dir, "environment")
    for entry in approved:
        if str(entry.get("asset_id", "")).strip().lower() != environment_id.strip().lower() or not entry.get("locked"):
            continue
        if variant == ENVIRONMENT_PRIMARY_MASTER_VARIANT:
            return str(entry.get("canonical_reference_image", "")).strip()
        supporting = entry.get("supporting_references", {})
        if isinstance(supporting, dict):
            return str(supporting.get(variant, "")).strip()
    return ""


def _write_generation_prompt_package(
    project_dir: Path,
    entry: dict[str, Any],
    *,
    workflow_id: str,
    source_ref: str,
    prompt_variant_id: str = "raw",
    booster_bundle_ids: list[str] | None = None,
) -> Path:
    package = parse_prompt_package(Path(str(entry.get("prompt_package_path", ""))))
    repair_notes = package.repair_notes_markdown
    positive_prompt = package.positive_prompt
    negative_prompt = package.negative_prompt
    if source_ref:
        image_instruction = "Use image1 as the locked spatial reference."
        positive_prompt = _prepend_prompt_instruction(package.positive_prompt, image_instruction)
        extra_note = f"- Use image1 as locked environment reference: {source_ref}"
        repair_notes = (repair_notes + "\n" + extra_note).strip() if repair_notes else extra_note

    boosted_positive, boosted_negative, booster_meta = apply_booster_bundles(
        positive_prompt,
        negative_prompt,
        prompt_variant_id=prompt_variant_id,
        bundle_ids=booster_bundle_ids,
    )
    if booster_meta.get("booster_bundle_ids"):
        summary_line = "- Prompt boosters: variant={variant} bundles={bundles}".format(
            variant=str(booster_meta.get("prompt_variant_id", "raw")),
            bundles=", ".join(str(b) for b in booster_meta.get("booster_bundle_ids", [])),
        )
        repair_notes = (repair_notes + "\n" + summary_line).strip() if repair_notes else summary_line

    entry["prompt_variant_id"] = str(booster_meta.get("prompt_variant_id", prompt_variant_id or "raw"))
    entry["booster_bundle_ids"] = list(booster_meta.get("booster_bundle_ids", []))
    entry["missing_booster_bundle_ids"] = list(booster_meta.get("missing_booster_bundle_ids", []))
    entry["positive_boosters"] = list(booster_meta.get("positive_boosters", []))
    entry["negative_boosters"] = list(booster_meta.get("negative_boosters", []))

    generated = PromptPackage(
        path=package.path,
        title=package.title,
        prompt_id=package.prompt_id,
        purpose=package.purpose,
        workflow_type=workflow_id,
        positive_prompt=boosted_positive,
        negative_prompt=boosted_negative,
        inputs_markdown=package.inputs_markdown,
        continuity_notes_markdown=package.continuity_notes_markdown,
        sources_markdown=package.sources_markdown,
        repair_notes_markdown=repair_notes,
    )
    asset_id = str(entry.get("asset_id", "")).strip().lower()
    variant = str(entry.get("variant_key", "")).strip().lower()
    output_path = project_dir / "03_reference_assets" / "environments" / asset_id / "generation_prompts" / f"{variant}_{workflow_id.replace('/', '_')}_prompt.md"
    write_prompt_package(output_path, generated)
    return output_path


def _manifest_output_files(manifest_path: Path) -> list[str]:
    if not manifest_path.exists():
        return []
    payload = read_json(manifest_path)
    return [str(p) for p in payload.get("output_files", []) if str(p).strip()] if isinstance(payload, dict) and isinstance(payload.get("output_files", []), list) else []


def _prepend_prompt_instruction(prompt: str, instruction: str) -> str:
    prompt = str(prompt).strip()
    instruction = str(instruction).strip()
    if not instruction:
        return prompt
    if not prompt:
        return instruction
    if instruction.lower() in prompt.lower():
        return prompt
    return f"{instruction} {prompt}".strip()


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
                    if isinstance(entry, dict):
                        normalized_id = str(entry.get("canonical_id", env_id)).strip().lower()
                        if normalized_id:
                            record = dict(entry); record.setdefault("environment_id", normalized_id); record.setdefault("display_name", str(entry.get("display_name", normalized_id)).strip() or normalized_id); records[normalized_id] = record
                continue
            env_id = str(payload.get("environment_id", payload.get("canonical_id", ""))).strip().lower()
            if env_id:
                item = dict(payload); item.setdefault("environment_id", env_id); item.setdefault("display_name", str(payload.get("display_name", env_id)).strip() or env_id); records[env_id] = item
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
    if "main" in role or "primary" in role: return "high"
    if "secondary" in role: return "medium"
    return "normal"


def _recommended_input_warnings(path: Path) -> list[str]:
    try: package = parse_prompt_package(path)
    except Exception: return []
    return [f"recommended input `{k}` missing" for k in OPTIONAL_BUT_RECOMMENDED_ENVIRONMENT_INPUTS if not str(package.inputs.get(k, "")).strip()]


def _prompt_prepared_entries(
    project_dir: Path,
    subject_kind: str,
    selected_variants: set[str],
    selected_ids: set[str],
) -> list[dict[str, Any]]:
    index_path = project_dir / "03_prompt_packages" / "prepared" / "PROMPT_PREPARATION_INDEX.json"
    if not index_path.exists():
        return []
    payload = read_json(index_path)
    if not isinstance(payload, list):
        return []
    entries: list[dict[str, Any]] = []
    for item in payload:
        if not isinstance(item, dict):
            continue
        if str(item.get("subject_kind", "")).strip().lower() != subject_kind:
            continue
        if str(item.get("status", "")).strip().lower() != "canonical":
            continue
        asset_id = str(item.get("subject_id", "")).strip().lower()
        variant = str(item.get("variant_name", "")).strip().lower()
        if not asset_id or not variant:
            continue
        if selected_ids and asset_id not in selected_ids:
            continue
        if selected_variants and variant not in selected_variants:
            continue
        prompt_path = Path(str(item.get("path", "")))
        if not prompt_path.exists():
            continue
        
        blocking_warnings = validate_prompt_package(prompt_path, REQUIRED_ENVIRONMENT_REFERENCE_INPUTS)
        recommended_warnings = _recommended_input_warnings(prompt_path)
        warnings = blocking_warnings + recommended_warnings
        
        entries.append(
            {
                "schema_version": "2026-04-23-reference-assets-v1",
                "reference_request_id": f"{asset_id}_{variant}",
                "asset_kind": subject_kind,
                "asset_id": asset_id,
                "variant_key": variant,
                "prompt_package_path": str(prompt_path),
                "status": "prepared" if not blocking_warnings else "blocked",
                "approval_state": "unreviewed",
                "locked": False,
                "priority": "normal",
                "candidate_ids": [],
                "selected_candidate_id": "",
                "review_notes": [],
                "blocking_warnings": blocking_warnings,
                "recommended_warnings": recommended_warnings,
                "warnings": warnings,
                "chapter_mentions": list(item.get("chapter_mentions", [])),
                "updated_at": "",
                "generation_stage": _generation_stage_for_variant(variant),
                "generation_workflow_id": _workflow_for_variant(variant),
            }
        )
    return entries


def _rank_environment_entries(entries: list[dict[str, Any]], environment_bibles: dict[str, dict[str, Any]], selected_chapters: set[str]) -> list[dict[str, Any]]:
    def score_entry(entry: dict[str, Any]) -> tuple[int, ...]:
        env_id = str(entry.get("asset_id", "")).strip().lower()
        bible = environment_bibles.get(env_id, {})
        
        # 1. Chapter match (already filtered, but for consistency)
        chapter_match = 1 if any_chapter_matches(entry.get("chapter_mentions", []), selected_chapters) else 0
        
        # 2. Bound to scenes/shots in selected chapters (approximated by chapter_mentions in prompt-prep)
        # 3. Landmark specificity
        landmark = str(bible.get("landmark_descriptor", "")).strip().lower()
        has_landmark = 1 if landmark and "none" not in landmark and "unknown" not in landmark else 0
        
        # 4. Descriptor completeness / fewer warnings
        warning_score = -len(entry.get("warnings", []))
        
        # 5. Recurrence in selected chapters
        mentions = entry.get("chapter_mentions", [])
        recurrence = len([m for m in mentions if m in selected_chapters])
        
        # 6. Stable ID and non-placeholder name
        display_name = str(bible.get("display_name", "")).strip().lower()
        has_good_name = 1 if display_name and "environment" not in display_name and "unknown" not in display_name else 0
        
        priority_map = {"high": 2, "medium": 1, "normal": 0}
        priority_score = priority_map.get(_environment_priority(bible), 0)
        
        return (chapter_match, priority_score, has_landmark, recurrence, warning_score, has_good_name)

    return sorted(entries, key=score_entry, reverse=True)
