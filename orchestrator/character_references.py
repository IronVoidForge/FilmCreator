from __future__ import annotations

from pathlib import Path
from typing import Any

from .character_bible import _is_film_facing_character
from .chapter_selection import any_chapter_matches, parse_chapter_selector
from .core.json_io import read_json
from .prompt_package import PromptPackage, parse_prompt_package, write_prompt_package, _split_sections
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
from .core.json_io import read_json

CHARACTER_MASTER_VARIANTS = {"full_body_neutral", "bust_portrait"}
CHARACTER_PRIMARY_MASTER_VARIANT = "full_body_neutral"
CHARACTER_T2I_WORKFLOW_ID = "still.t2i.klein.distilled"
CHARACTER_VARIANT_WORKFLOW_ID = "still.reference_variant.single_ref.klein.distilled"
CHARACTER_VALIDATION_SLICE_LIMIT = 2
CHARACTER_VALIDATION_SLICE_STAGES = {
    "portrait": {"bust_portrait"},
    "full_body": {"full_body_neutral"},
    "supporting": {"profile_view", "three_quarter_view", "front_view", "back_view", "action_pose", "expression_sheet"},
}

REQUIRED_CHARACTER_REFERENCE_INPUTS = {"subject_kind", "subject_id", "source_artifact_ids", "reference_mode", "variant_name", "reuse_policy"}
OPTIONAL_BUT_RECOMMENDED_CHARACTER_INPUTS = {"display_name", "identity_descriptor", "body_descriptor", "face_descriptor", "costume_descriptor", "posture_descriptor", "expression_descriptor", "locked_fields"}


def run_character_reference_planning(project_slug: str, *, force: bool = False, variants: list[str] | None = None, limit: int | None = None, test_slice: bool = False) -> ReferencePhaseSummary:
    project_dir = create_project(project_slug)
    character_bibles = _load_character_bibles(project_dir)
    selected_variants = _selected_variants(variants, test_slice=test_slice)
    existing = [] if force else load_reference_queue(project_dir, "character")
    existing_by_key = {(str(e.get("asset_id", "")).strip().lower(), str(e.get("variant_key", "")).strip().lower()): e for e in existing}
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
                entry = existing_by_key[key]
                if test_slice:
                    entry["validation_slice"] = True
                    entry["validation_slice_stage"] = _validation_slice_stage_for_variant(variant)
                entries.append(entry)
                continue
            path = prompt_package_path(project_dir, "character", character_id, variant)
            blocking_warnings = validate_prompt_package(path, REQUIRED_CHARACTER_REFERENCE_INPUTS)
            recommended_warnings = _recommended_input_warnings(path)
            prompt_warnings = blocking_warnings + recommended_warnings
            
            identity_review_required = _is_character_identity_review_required(project_dir, character_id)
            
            request = make_reference_request(asset_kind="character", asset_id=character_id, variant_key=variant, prompt_path=path, priority=priority, warnings=prompt_warnings)
            request["status"] = "blocked" if blocking_warnings else "prepared"
            request["blocking_warnings"] = blocking_warnings
            request["recommended_warnings"] = recommended_warnings
            request["identity_review_required"] = identity_review_required
            request["generation_stage"] = _generation_stage_for_variant(variant)
            request["generation_workflow_id"] = _workflow_for_variant(variant)
            if test_slice:
                request["validation_slice"] = True
                request["validation_slice_stage"] = _validation_slice_stage_for_variant(variant)
            if variant == "full_body_neutral":
                request.setdefault("review_notes", []).append("Validation order: derive full-body from an approved locked bust/portrait reference when available.")
            if variant not in CHARACTER_MASTER_VARIANTS:
                request.setdefault("review_notes", []).append(f"Requires an approved locked {CHARACTER_PRIMARY_MASTER_VARIANT} character reference before generation.")
            entries.append(request)
            if blocking_warnings:
                warnings.append(f"{character_id}/{variant} (BLOCKING): " + "; ".join(blocking_warnings))
            if recommended_warnings:
                warnings.append(f"{character_id}/{variant} (RECOMMENDED): " + "; ".join(recommended_warnings))

    if test_slice:
        entries = _apply_validation_slice_caps(entries)
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
    test_slice: bool = False,
    chapters: str | None = None,
    prompt_variant_id: str = "raw",
    booster_bundle_ids: list[str] | None = None,
    include_unresolved_identities: bool = False,
) -> ReferencePhaseSummary:
    project_dir = create_project(project_slug)
    selected_variants = {v.strip().lower() for v in variants or [] if v.strip()}
    selected_ids = {c.strip().lower() for c in character_ids or [] if c.strip()}
    selected_chapters = set(parse_chapter_selector(chapters))
    queue = load_reference_queue(project_dir, "character")
    eligible: list[dict[str, Any]] = []
    warnings: list[str] = []
    written: list[str] = []

    if test_slice:
        eligible = _prompt_prepared_entries(project_dir, "character", selected_variants, selected_ids)
        if selected_chapters:
            eligible = [e for e in eligible if any_chapter_matches(e.get("chapter_mentions", []), selected_chapters)]

    if not eligible:
        for entry in queue:
            character_id = str(entry.get("asset_id", "")).strip().lower()
            variant = str(entry.get("variant_key", "")).strip().lower()
            if selected_ids and character_id not in selected_ids:
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
            
            # Unresolved identity guard
            if entry.get("identity_review_required") and not include_unresolved_identities:
                continue
                
            prompt_path = Path(str(entry.get("prompt_package_path", "")))
            if not prompt_path.exists():
                continue
            eligible.append(entry)

    if not eligible and test_slice:
        eligible = _fallback_prompt_prepared_entries(project_dir, "character", selected_variants, selected_ids)
        if selected_chapters:
            eligible = [e for e in eligible if any_chapter_matches(e.get("chapter_mentions", []), selected_chapters)]

    if test_slice:
        # Also filter out unresolved identities from test-slice by default
        if not include_unresolved_identities:
            eligible = [e for e in eligible if not e.get("identity_review_required")]
        
        if selected_chapters:
            character_bibles = _load_character_bibles(project_dir)
            eligible = _rank_character_entries(eligible, character_bibles, selected_chapters)
            slice_limit = limit if limit is not None else 2
            eligible = eligible[:slice_limit]
        else:
            eligible = _apply_validation_slice_caps(eligible)
            if limit is not None:
                eligible = eligible[:limit]
        
    selected_entries = eligible if (test_slice and selected_chapters) else (eligible if limit is None else eligible[:limit])
    for entry in selected_entries:
        character_id = str(entry.get("asset_id", "")).strip().lower()
        variant = str(entry.get("variant_key", "")).strip().lower()
        source_ref = _source_reference_for_variant(project_dir, character_id, variant)
        if _requires_source_reference(variant) and not source_ref:
            note = _missing_gate_note(character_id, variant)
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
            summary = run_still(project_slug=project_slug, stage=stage, prompt_file=str(generation_prompt_path), workflow_id=actual_workflow_id, asset_id=character_id, ref_args=ref_args, seed=seed, execute=execute)
        except Exception as exc:
            warnings.append(f"{character_id}/{variant}: generation preparation failed: {exc}")
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
                candidate_summary = register_character_reference_candidate(project_slug, character_id=character_id, variant=variant, image_path=output_file)
                written.extend(candidate_summary.written_files)
    queue_to_write = eligible if test_slice and eligible else queue
    written.extend(write_reference_queue(project_dir, "character", queue_to_write))
    return summarize_reference_phase(project_slug, "character", project_dir, warnings=warnings, written_files=written)


def register_character_reference_candidate(project_slug: str, *, character_id: str, variant: str, image_path: str) -> ReferencePhaseSummary:
    return register_reference_candidate(project_slug, asset_kind="character", asset_id=character_id, variant_key=variant, image_path=image_path)

def approve_character_reference_candidate(project_slug: str, *, candidate_id: str) -> ReferencePhaseSummary:
    return approve_reference_candidate(project_slug, asset_kind="character", candidate_id=candidate_id)

def reject_character_reference_candidate(project_slug: str, *, candidate_id: str, reason: str) -> ReferencePhaseSummary:
    return reject_reference_candidate(project_slug, asset_kind="character", candidate_id=candidate_id, reason=reason)

def lock_character_reference_candidate(project_slug: str, *, candidate_id: str) -> ReferencePhaseSummary:
    return lock_reference_candidate(project_slug, asset_kind="character", candidate_id=candidate_id)


def _selected_variants(variants: list[str] | None, *, test_slice: bool) -> list[str]:
    if variants:
        return [v.strip().lower() for v in variants if v.strip()]
    if test_slice:
        return ["bust_portrait", "full_body_neutral", "profile_view"]
    return [v.strip().lower() for v in CHARACTER_DEFAULT_VARIANTS if v.strip()]


def _validation_slice_stage_for_variant(variant: str) -> str:
    for stage, variants in CHARACTER_VALIDATION_SLICE_STAGES.items():
        if variant in variants:
            return stage
    return "supporting"


def _apply_validation_slice_caps(entries: list[dict[str, Any]]) -> list[dict[str, Any]]:
    counts = {"portrait": 0, "full_body": 0, "supporting": 0}
    capped: list[dict[str, Any]] = []
    for entry in entries:
        stage = str(entry.get("validation_slice_stage") or _validation_slice_stage_for_variant(str(entry.get("variant_key", ""))))
        if stage not in counts:
            stage = "supporting"
        if counts[stage] >= CHARACTER_VALIDATION_SLICE_LIMIT:
            continue
        counts[stage] += 1
        entry["validation_slice"] = True
        entry["validation_slice_stage"] = stage
        capped.append(entry)
    return capped


def _generation_stage_for_variant(variant: str, *, has_source: bool = False) -> str:
    return "character_reference_variant" if has_source else "character_reference"


def _workflow_for_variant(variant: str, *, has_source: bool = False) -> str:
    return CHARACTER_VARIANT_WORKFLOW_ID if has_source else CHARACTER_T2I_WORKFLOW_ID


def _requires_source_reference(variant: str) -> bool:
    return variant not in {"bust_portrait"}


def _source_reference_for_variant(project_dir: Path, character_id: str, variant: str) -> str:
    if variant == "full_body_neutral":
        return _locked_reference_for_variant(project_dir, character_id, "bust_portrait")
    if variant == "bust_portrait":
        return ""
    return _locked_reference_for_variant(project_dir, character_id, "full_body_neutral") or _locked_master_reference(project_dir, character_id)


def _missing_gate_note(character_id: str, variant: str) -> str:
    if variant == "full_body_neutral":
        return f"{character_id}/{variant}: missing locked bust_portrait reference; generate, approve, and lock portrait first."
    return f"{character_id}/{variant}: missing locked full_body_neutral reference; generate, approve, and lock full-body first."


def _locked_master_reference(project_dir: Path, character_id: str) -> str:
    approved = load_approved_manifest(project_dir, "character")
    for entry in approved:
        if str(entry.get("asset_id", "")).strip().lower() != character_id.strip().lower():
            continue
        if not entry.get("locked"):
            return ""
        return str(entry.get("canonical_reference_image", "")).strip()
    return ""


def _locked_reference_for_variant(project_dir: Path, character_id: str, variant: str) -> str:
    approved = load_approved_manifest(project_dir, "character")
    for entry in approved:
        if str(entry.get("asset_id", "")).strip().lower() != character_id.strip().lower() or not entry.get("locked"):
            continue
        if variant == CHARACTER_PRIMARY_MASTER_VARIANT:
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
        image_instruction = "Use image1 as the locked identity reference."
        positive_prompt = _prepend_prompt_instruction(package.positive_prompt, image_instruction)
        extra_note = f"- Use image1 as locked identity reference: {source_ref}"
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
    output_path = project_dir / "03_reference_assets" / "characters" / asset_id / "generation_prompts" / f"{variant}_{workflow_id.replace('/', '_')}_prompt.md"
    write_prompt_package(output_path, generated)
    return output_path


def _manifest_output_files(manifest_path: Path) -> list[str]:
    if not manifest_path.exists():
        return []
    payload = read_json(manifest_path)
    return [str(p) for p in payload.get("output_files", []) if str(p).strip()] if isinstance(payload, dict) and isinstance(payload.get("output_files", []), list) else []


def _fallback_prompt_prepared_entries(
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
        entries.append(
            {
                "schema_version": "2026-04-23-reference-assets-v1",
                "reference_request_id": f"{asset_id}_{variant}",
                "asset_kind": subject_kind,
                "asset_id": asset_id,
                "variant_key": variant,
                "prompt_package_path": str(prompt_path),
                "status": "prepared",
                "approval_state": "unreviewed",
                "locked": False,
                "priority": "normal",
                "candidate_ids": [],
                "selected_candidate_id": "",
                "review_notes": [],
                "warnings": [],
                "updated_at": "",
                "generation_stage": _generation_stage_for_variant(variant),
                "generation_workflow_id": _workflow_for_variant(variant),
            }
        )
    return entries


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
        
        blocking_warnings = validate_prompt_package(prompt_path, REQUIRED_CHARACTER_REFERENCE_INPUTS)
        recommended_warnings = _recommended_input_warnings(prompt_path)
        warnings = blocking_warnings + recommended_warnings
        
        identity_review_required = False
        if subject_kind == "character":
            identity_review_required = _is_character_identity_review_required(project_dir, asset_id)
            
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
                "identity_review_required": identity_review_required,
                "chapter_mentions": list(item.get("chapter_mentions", [])),
                "updated_at": "",
                "generation_stage": _generation_stage_for_variant(variant),
                "generation_workflow_id": _workflow_for_variant(variant),
            }
        )
    return entries


def _is_character_identity_review_required(project_dir: Path, character_id: str) -> bool:
    path = project_dir / "01_source" / "character_descriptions" / f"{character_id}_clarification.md"
    if not path.exists():
        return False
    try:
        sections = _split_sections(path.read_text(encoding="utf-8"))
        return not sections.get("Clarification Response", "").strip()
    except Exception:
        return True


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
                if isinstance(record, dict):
                    normalized_id = str(record.get("canonical_id", character_id)).strip().lower()
                    if normalized_id:
                        item = dict(record); item.setdefault("character_id", normalized_id); item.setdefault("display_name", str(record.get("display_name", normalized_id)).strip() or normalized_id); records[normalized_id] = item
            continue
        character_id = str(payload.get("character_id", payload.get("canonical_id", ""))).strip().lower()
        if character_id:
            item = dict(payload); item.setdefault("character_id", character_id); item.setdefault("display_name", str(payload.get("display_name", character_id)).strip() or character_id); records[character_id] = item
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
    if any(term in role for term in ["protagonist", "lead", "major", "main", "primary"]): return "high"
    if any(term in role for term in ["supporting", "recurring", "secondary"]): return "medium"
    return "normal"


def _rank_character_entries(entries: list[dict[str, Any]], character_bibles: dict[str, dict[str, Any]], selected_chapters: set[str]) -> list[dict[str, Any]]:
    def score_entry(entry: dict[str, Any]) -> tuple[int, ...]:
        character_id = str(entry.get("asset_id", "")).strip().lower()
        bible = character_bibles.get(character_id, {})
        
        # 1. Chapter match (already filtered, but for consistency)
        chapter_match = 1 if any_chapter_matches(entry.get("chapter_mentions", []), selected_chapters) else 0
        
        # 2. Resolved/canonical identity
        is_canonical = 1 if str(bible.get("status", "canonical")).strip().lower() == "canonical" else 0
        
        # 3. No unresolved clarification
        no_clarification_needed = 0 if entry.get("identity_review_required") else 1
        
        # 4. Film-facing individual before group/provisional
        entity_kind = str(bible.get("entity_kind", "individual")).strip().lower()
        is_individual = 1 if entity_kind == "individual" else 0
        
        # 5. Protagonist/main/major role signals
        priority_map = {"high": 2, "medium": 1, "normal": 0}
        priority_score = priority_map.get(_character_priority(bible), 0)
        
        # 6. Descriptor completeness / fewer warnings
        warning_score = -len(entry.get("warnings", []))
        
        # 7. Recurrence in selected chapters
        mentions = entry.get("chapter_mentions", [])
        recurrence = len([m for m in mentions if m in selected_chapters])
        
        # 8. Stable ID and non-placeholder name
        display_name = str(bible.get("display_name", "")).strip().lower()
        has_good_name = 1 if display_name and "character" not in display_name and "unknown" not in display_name else 0
        
        return (chapter_match, is_canonical, no_clarification_needed, is_individual, priority_score, recurrence, warning_score, has_good_name)

    return sorted(entries, key=score_entry, reverse=True)


def _recommended_input_warnings(path: Path) -> list[str]:
    if not path.exists(): return []
    try: package = parse_prompt_package(path)
    except Exception: return []
    return [f"recommended input `{key}` is missing" for key in sorted(key for key in OPTIONAL_BUT_RECOMMENDED_CHARACTER_INPUTS if not str(package.inputs.get(key, "")).strip())]
