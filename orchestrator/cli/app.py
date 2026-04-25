from __future__ import annotations

import json
from typing import Any

from ..character_bible import run_character_bible_synthesis
from ..character_references import (
    approve_character_reference_candidate,
    lock_character_reference_candidate,
    register_character_reference_candidate,
    reject_character_reference_candidate,
    run_character_reference_generation,
    run_character_reference_planning,
)
from ..descriptor_enrichment import run_descriptor_enrichment
from ..dialogue_timeline import run_dialogue_timeline
from ..environment_bible import run_environment_bible_synthesis
from ..environment_references import (
    approve_environment_reference_candidate,
    lock_environment_reference_candidate,
    register_environment_reference_candidate,
    reject_environment_reference_candidate,
    run_environment_reference_generation,
    run_environment_reference_planning,
)
from ..quality_grading import run_quality_grading
from ..scene_bindings import run_scene_binding_synthesis
from ..scene_contracts import run_scene_contract_synthesis
from ..shot_planner import run_shot_planning
from ..prompt_preparation import run_prompt_preparation
from ..visual_fallbacks import run_visual_fallback_synthesis
from .models import CliSummary
from .rerun import plan_rerun
from .status import run_status
from .test_pipeline import run_quick_test


def dispatch(args) -> None:
    summary: Any
    if args.command == "status":
        summary = run_status(args.project_slug)
    elif args.command == "rerun":
        summary = plan_rerun(args.project_slug, args.start_from)
    elif args.command == "test-pipeline":
        summary = _run_or_plan_quick_test(args)
    elif args.command == "refresh-bibles":
        summary = _refresh_bibles(args)
    elif args.command == "synthesize-visual-fallbacks":
        summary = run_visual_fallback_synthesis(args.project_slug, force=args.force)
    elif args.command == "run-stage":
        summary = _run_stage(args)
    elif args.command == "plan-character-references":
        summary = run_character_reference_planning(args.project_slug, force=args.force, variants=args.variants, limit=args.limit)
    elif args.command == "generate-character-references":
        summary = run_character_reference_generation(
            args.project_slug,
            limit=args.limit,
            variants=args.variants,
            character_ids=args.character_ids,
            execute=args.execute,
            seed=args.seed,
            workflow_id=args.workflow_id,
            test_slice=args.test_slice,
            chapters=args.chapters,
            prompt_variant_id=args.prompt_variant,
            booster_bundle_ids=args.booster_bundle_ids,
        )
    elif args.command == "register-character-reference-candidate":
        summary = register_character_reference_candidate(args.project_slug, character_id=args.character_id, variant=args.variant, image_path=args.image_path)
    elif args.command == "approve-character-reference":
        summary = approve_character_reference_candidate(args.project_slug, candidate_id=args.candidate_id)
    elif args.command == "reject-character-reference":
        summary = reject_character_reference_candidate(args.project_slug, candidate_id=args.candidate_id, reason=args.reason)
    elif args.command == "lock-character-reference":
        summary = lock_character_reference_candidate(args.project_slug, candidate_id=args.candidate_id)
    elif args.command == "plan-environment-references":
        summary = run_environment_reference_planning(args.project_slug, force=args.force, variants=args.variants, limit=args.limit)
    elif args.command == "generate-environment-references":
        summary = run_environment_reference_generation(
            args.project_slug,
            limit=args.limit,
            variants=args.variants,
            environment_ids=args.environment_ids,
            execute=args.execute,
            seed=args.seed,
            workflow_id=args.workflow_id,
            test_slice=args.test_slice,
            chapters=args.chapters,
            prompt_variant_id=args.prompt_variant,
            booster_bundle_ids=args.booster_bundle_ids,
        )
    elif args.command == "register-environment-reference-candidate":
        summary = register_environment_reference_candidate(args.project_slug, environment_id=args.environment_id, variant=args.variant, image_path=args.image_path)
    elif args.command == "approve-environment-reference":
        summary = approve_environment_reference_candidate(args.project_slug, candidate_id=args.candidate_id)
    elif args.command == "reject-environment-reference":
        summary = reject_environment_reference_candidate(args.project_slug, candidate_id=args.candidate_id, reason=args.reason)
    elif args.command == "lock-environment-reference":
        summary = lock_environment_reference_candidate(args.project_slug, candidate_id=args.candidate_id)
    elif args.command in {"shot-keyframes", "audio", "video"}:
        summary = CliSummary(command=args.command, project_slug=args.project_slug, status="placeholder", message="Future phase placeholder; no work performed.")
    elif args.command == "legacy":
        summary = CliSummary(command="legacy", project_slug="", status="placeholder", message="Legacy command passthrough is intentionally not automatic. Use archived CLI reference or promote needed commands into the focused CLI.", data={"args": args.legacy_args})
    else:
        raise SystemExit(f"Unknown command: {args.command}")
    print(json.dumps(_to_dict(summary), indent=2))


def _run_or_plan_quick_test(args) -> Any:
    if not args.execute:
        return run_quick_test(args.project_slug)
    warnings: list[str] = []
    steps: dict[str, Any] = {}
    if args.refresh_bibles:
        steps["bibles"] = _refresh_bibles(args).to_dict()
    steps["scene_contracts"] = run_scene_contract_synthesis(args.project_slug, use_llm=True, force=True, chapters=args.chapters).to_dict()
    steps["scene_bindings"] = run_scene_binding_synthesis(args.project_slug, force=True, chapters=args.chapters).to_dict()
    steps["shot_packages"] = run_shot_planning(args.project_slug, use_llm=True, force=True, chapters=args.chapters).to_dict()
    steps["dialogue_timeline"] = run_dialogue_timeline(args.project_slug, force=True, chapters=args.chapters).to_dict()
    steps["visual_fallbacks"] = run_visual_fallback_synthesis(args.project_slug, force=True).to_dict()
    steps["descriptor_enrichment"] = run_descriptor_enrichment(args.project_slug, use_llm=True, force=True, chapters=args.chapters).to_dict()
    steps["prompt_preparation"] = run_prompt_preparation(args.project_slug, force=True, chapters=args.chapters).to_dict()
    steps["quality_grading"] = run_quality_grading(args.project_slug).to_dict()
    return CliSummary(command="test-pipeline", project_slug=args.project_slug, message="Quick-test pipeline executed.", data=steps, warnings=warnings)


def _refresh_bibles(args) -> CliSummary:
    run_characters = args.characters or not args.environments
    run_environments = args.environments or not args.characters
    data: dict[str, Any] = {}
    if run_characters:
        data["characters"] = run_character_bible_synthesis(args.project_slug, use_llm=not args.no_llm, force=args.force, limit=args.character_limit).to_dict()
    if run_environments:
        data["environments"] = run_environment_bible_synthesis(args.project_slug, use_llm=not args.no_llm, force=args.force, limit=args.environment_limit).to_dict()
    return CliSummary(command="refresh-bibles", project_slug=args.project_slug, message="Bible refresh complete.", data=data)


def _run_stage(args) -> Any:
    if args.stage == "visual_fallbacks":
        return run_visual_fallback_synthesis(args.project_slug, force=args.force)
    if args.stage == "scene_contracts":
        return run_scene_contract_synthesis(args.project_slug, use_llm=not args.no_llm, force=args.force, chapters=args.chapters)
    if args.stage == "scene_bindings":
        return run_scene_binding_synthesis(args.project_slug, force=args.force, chapters=args.chapters)
    if args.stage == "shot_packages":
        return run_shot_planning(args.project_slug, use_llm=not args.no_llm, force=args.force, chapters=args.chapters)
    if args.stage == "dialogue_timeline":
        return run_dialogue_timeline(args.project_slug, force=args.force, chapters=args.chapters)
    if args.stage == "descriptor_enrichment":
        return run_descriptor_enrichment(args.project_slug, use_llm=not args.no_llm, force=args.force, limit=args.limit, chapters=args.chapters)
    if args.stage == "prompt_preparation":
        return run_prompt_preparation(args.project_slug, force=args.force, limit=args.limit, chapters=args.chapters)
    if args.stage == "quality_grading":
        return run_quality_grading(args.project_slug)
    raise SystemExit(f"Unknown stage: {args.stage}")


def _to_dict(summary: Any) -> dict[str, Any]:
    if hasattr(summary, "to_dict"):
        return summary.to_dict()
    if isinstance(summary, dict):
        return summary
    return {"result": str(summary)}
