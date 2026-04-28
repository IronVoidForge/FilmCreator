from __future__ import annotations

import argparse
import json

from .book_ingest import ensure_book_ingested
from .character_bible import run_character_bible_synthesis
from .character_visual_evidence_refinement import run_character_visual_evidence_refinement
from .character_taxonomy import run_character_taxonomy
from .character_references import (
    approve_character_reference_candidate,
    lock_character_reference_candidate,
    register_character_reference_candidate,
    reject_character_reference_candidate,
    run_character_reference_generation,
    run_character_reference_planning,
)
from .descriptor_enrichment import clear_descriptor_artifacts, run_descriptor_enrichment
from .dialogue_enrichment import run_dialogue_enrichment
from .downstream_pipeline import run_downstream_pipeline, summarize_downstream_run
from .dialogue_timeline import run_dialogue_timeline
from .environment_bible import run_environment_bible_synthesis
from .environment_references import (
    approve_environment_reference_candidate,
    lock_environment_reference_candidate,
    register_environment_reference_candidate,
    reject_environment_reference_candidate,
    run_environment_reference_generation,
    run_environment_reference_planning,
)
from .identity_refinement import run_identity_refinement
from .quality_grading import run_quality_grading
from .selective_rerun import run_selective_reruns
from .prompt_preparation import run_prompt_preparation
from .production_cleanup import create_cleanup_plan, execute_cleanup_plan
from .production_pipeline import (
    OPERATOR_PHASE_ORDER,
    format_production_run_summary,
    plan_trusted_resume_pipeline,
    run_full_production_pipeline,
    run_phase_range,
    run_quicktest_composite,
    run_scene_slice_pipeline,
    run_story_analysis_pipeline,
)
from .production_run_state import persist_run_summary
from .production_status import get_production_status, get_resume_check_summary
from .scene_contracts import run_scene_contract_synthesis
from .scene_bindings import run_scene_binding_synthesis
from .shot_coverage import COVERAGE_DENSITIES
from .shot_planner import run_shot_planning
from .visual_fallbacks import run_visual_fallback_synthesis
from .pipeline_menu import run_pipeline_menu


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="FilmCreator tools")
    subparsers = parser.add_subparsers(dest="command", required=True)

    s = subparsers.add_parser("synthesize-character-bibles")
    s.add_argument("project_slug")
    s.add_argument("--no-llm", action="store_true")
    s.add_argument("--force", action="store_true")
    s.add_argument("--limit", type=int, default=None)

    cve = subparsers.add_parser("refine-character-visual-evidence")
    cve.add_argument("project_slug")
    cve.add_argument("--force", action="store_true")
    cve.add_argument("--only-review", action="store_true")
    cve.add_argument("--chapters", type=str, default=None)
    cve.add_argument("--limit", type=int, default=None)

    e = subparsers.add_parser("synthesize-environment-bibles")
    e.add_argument("project_slug")
    e.add_argument("--no-llm", action="store_true")
    e.add_argument("--force", action="store_true")
    e.add_argument("--limit", type=int, default=None)

    vf = subparsers.add_parser("synthesize-visual-fallbacks")
    vf.add_argument("project_slug")
    vf.add_argument("--force", action="store_true")

    sc = subparsers.add_parser("synthesize-scene-contracts")
    sc.add_argument("project_slug")
    sc.add_argument("--no-llm", action="store_true")
    sc.add_argument("--force", action="store_true")
    sc.add_argument("--chapters", type=str, default=None)

    sb = subparsers.add_parser("synthesize-scene-bindings")
    sb.add_argument("project_slug")
    sb.add_argument("--force", action="store_true")
    sb.add_argument("--chapters", type=str, default=None)

    sp = subparsers.add_parser("synthesize-shot-packages")
    sp.add_argument("project_slug")
    sp.add_argument("--no-llm", action="store_true")
    sp.add_argument("--force", action="store_true")
    sp.add_argument("--chapters", type=str, default=None)
    sp.add_argument("--coverage-density", choices=sorted(COVERAGE_DENSITIES), default=None)

    dt = subparsers.add_parser("synthesize-dialogue-timeline")
    dt.add_argument("project_slug")
    dt.add_argument("--force", action="store_true")
    dt.add_argument("--chapters", type=str, default=None)

    dext = subparsers.add_parser("synthesize-dialogue-enrichment")
    dext.add_argument("project_slug")
    dext.add_argument("--force", action="store_true")

    pp = subparsers.add_parser("synthesize-prompt-preparation")
    pp.add_argument("project_slug")
    pp.add_argument("--force", action="store_true")
    pp.add_argument("--limit", type=int, default=None)
    pp.add_argument("--entity-type", action="append", choices=["character", "environment", "scene", "shot"], dest="entity_types")
    pp.add_argument("--entity-id", action="append", dest="entity_ids")
    pp.add_argument("--chapters", type=str, default=None)
    pp.add_argument("--shot-variant", action="append", choices=["primary_keyframe", "alternate_angle", "consistency_repair"], dest="shot_variants")

    crp = subparsers.add_parser("plan-character-references")
    crp.add_argument("project_slug")
    crp.add_argument("--force", action="store_true")
    crp.add_argument("--limit", type=int, default=None)
    crp.add_argument("--variant", action="append", dest="variants")

    crg = subparsers.add_parser("generate-character-references")
    crg.add_argument("project_slug")
    crg.add_argument("--chapters", type=str, default=None)
    crg.add_argument("--limit", type=int, default=None)
    crg.add_argument("--variant", action="append", dest="variants")
    crg.add_argument("--character-id", action="append", dest="character_ids")
    crg.add_argument("--execute", action="store_true")
    crg.add_argument("--seed", type=int, default=None)
    crg.add_argument("--workflow-id", type=str, default=None)
    crg.add_argument("--test-slice", action="store_true")
    crg.add_argument("--prompt-variant", type=str, default="raw")
    crg.add_argument("--booster-bundle", action="append", dest="booster_bundle_ids")

    crc = subparsers.add_parser("register-character-reference-candidate")
    crc.add_argument("project_slug")
    crc.add_argument("--character-id", required=True)
    crc.add_argument("--variant", required=True)
    crc.add_argument("--image-path", required=True)

    cra = subparsers.add_parser("approve-character-reference")
    cra.add_argument("project_slug")
    cra.add_argument("--candidate-id", required=True)

    crr = subparsers.add_parser("reject-character-reference")
    crr.add_argument("project_slug")
    crr.add_argument("--candidate-id", required=True)
    crr.add_argument("--reason", required=True)

    crl = subparsers.add_parser("lock-character-reference")
    crl.add_argument("project_slug")
    crl.add_argument("--candidate-id", required=True)

    erp = subparsers.add_parser("plan-environment-references")
    erp.add_argument("project_slug")
    erp.add_argument("--force", action="store_true")
    erp.add_argument("--limit", type=int, default=None)
    erp.add_argument("--variant", action="append", dest="variants")

    erg = subparsers.add_parser("generate-environment-references")
    erg.add_argument("project_slug")
    erg.add_argument("--chapters", type=str, default=None)
    erg.add_argument("--limit", type=int, default=None)
    erg.add_argument("--variant", action="append", dest="variants")
    erg.add_argument("--environment-id", action="append", dest="environment_ids")
    erg.add_argument("--execute", action="store_true")
    erg.add_argument("--seed", type=int, default=None)
    erg.add_argument("--workflow-id", type=str, default=None)
    erg.add_argument("--test-slice", action="store_true")
    erg.add_argument("--prompt-variant", type=str, default="raw")
    erg.add_argument("--booster-bundle", action="append", dest="booster_bundle_ids")

    erc = subparsers.add_parser("register-environment-reference-candidate")
    erc.add_argument("project_slug")
    erc.add_argument("--environment-id", required=True)
    erc.add_argument("--variant", required=True)
    erc.add_argument("--image-path", required=True)

    era = subparsers.add_parser("approve-environment-reference")
    era.add_argument("project_slug")
    era.add_argument("--candidate-id", required=True)

    err = subparsers.add_parser("reject-environment-reference")
    err.add_argument("project_slug")
    err.add_argument("--candidate-id", required=True)
    err.add_argument("--reason", required=True)

    erl = subparsers.add_parser("lock-environment-reference")
    erl.add_argument("project_slug")
    erl.add_argument("--candidate-id", required=True)

    de = subparsers.add_parser("synthesize-descriptor-enrichment")
    de.add_argument("project_slug")
    de.add_argument("--no-llm", action="store_true")
    de.add_argument("--force", action="store_true")
    de.add_argument("--limit", type=int, default=None)
    de.add_argument("--entity-type", action="append", choices=["character", "environment", "scene", "shot", "key_item"], dest="entity_types")
    de.add_argument("--entity-id", action="append", dest="entity_ids")
    de.add_argument("--chapters", type=str, default=None)

    qg = subparsers.add_parser("grade-artifacts")
    qg.add_argument("project_slug")
    qg.add_argument("--family", action="append", choices=["character", "environment", "scene", "shot", "dialogue", "descriptor", "prompt", "character_bible", "environment_bible", "scene_contract", "shot_package", "dialogue_timeline", "prompt_package"], dest="families")

    rr = subparsers.add_parser("rerun-quality-artifacts")
    rr.add_argument("project_slug")
    rr.add_argument("--execute", action="store_true")

    ce = subparsers.add_parser("clear-descriptor-artifacts")
    ce.add_argument("project_slug")
    ce.add_argument("--keep-prompts", action="store_true", help="Only clear descriptor artifacts and keep prepared prompts.")

    r = subparsers.add_parser("refine-identities")
    r.add_argument("project_slug")
    r.add_argument("--no-llm", action="store_true")
    r.add_argument("--apply", action="store_true")

    ct = subparsers.add_parser("synthesize-character-taxonomy")
    ct.add_argument("project_slug")
    ct.add_argument("--force", action="store_true")
    ct.add_argument("--limit", type=int, default=None)

    bi = subparsers.add_parser("ensure-book-ingested")
    bi.add_argument("project_slug")

    dp = subparsers.add_parser("run-downstream-pipeline")
    dp.add_argument("project_slug")
    dp.add_argument("--chapters", type=str, default=None)
    dp.add_argument("--start-phase", choices=["scene_contracts", "scene_bindings", "shot_packages", "dialogue_timeline", "descriptor_enrichment", "prompt_preparation"], default="scene_contracts")
    dp.add_argument("--pipeline-key", type=str, default="downstream_pipeline")
    dp.add_argument("--no-resume", action="store_true")
    dp.add_argument("--no-llm", action="store_true")
    dp.add_argument("--shot-variant", action="append", choices=["primary_keyframe", "alternate_angle", "consistency_repair"], dest="shot_variants")
    dp.add_argument("--coverage-density", choices=sorted(COVERAGE_DENSITIES), default=None)

    ds = subparsers.add_parser("summarize-downstream-run")
    ds.add_argument("project_slug")
    ds.add_argument("--pipeline-key", type=str, default="downstream_pipeline")

    ps = subparsers.add_parser("project-status")
    ps.add_argument("project_slug", nargs="?", default="princess_of_mars_test")
    ps.add_argument("--chapters", type=str, default=None)

    rc = subparsers.add_parser("resume-check")
    rc.add_argument("project_slug", nargs="?", default="princess_of_mars_test")
    rc.add_argument("--chapters", type=str, default=None)

    rp = subparsers.add_parser("run-production")
    rp.add_argument("project_slug", nargs="?", default="princess_of_mars_test")
    rp.add_argument("--chapters", type=str, default=None)
    rp.add_argument("--mode", choices=["resume", "force"], default="resume")
    rp.add_argument("--profile", choices=["full", "post-taxonomy"], default="full")
    rp.add_argument("--skip-taxonomy", action="store_true")
    rp.add_argument("--plan-only", action="store_true")
    rp.add_argument("--coverage-density", choices=sorted(COVERAGE_DENSITIES), default=None)

    rsa = subparsers.add_parser("run-story-analysis")
    rsa.add_argument("project_slug", nargs="?", default="princess_of_mars_test")
    rsa.add_argument("--chapters", type=str, default=None)
    rsa.add_argument("--mode", choices=["resume", "force"], default="resume")

    rqc = subparsers.add_parser("run-quicktest-composite")
    rqc.add_argument("project_slug", nargs="?", default="princess_of_mars_test")
    rqc.add_argument("--chapters", type=str, default="2-3")
    rqc.add_argument("--composite", choices=["09_to_14", "11_to_14", "13_to_14"], required=True)

    rss = subparsers.add_parser("run-scene-slice")
    rss.add_argument("project_slug", nargs="?", default="princess_of_mars_test")
    rss.add_argument("--chapter", required=True, help="Chapter to analyze, e.g. 1 or CH001")
    rss.add_argument("--scene", required=True, help="Scene to carry downstream, e.g. 1, SC001, or CH001_SC001")
    rss.add_argument("--mode", choices=["resume", "force"], default="force")
    rss.add_argument("--coverage-density", choices=sorted(COVERAGE_DENSITIES), default=None)

    cp = subparsers.add_parser("clear-production")
    cp.add_argument("project_slug", nargs="?", default="princess_of_mars_test")
    cp.add_argument("--scope", choices=["prompt_prep_only", "downstream_only", "taxonomy_and_downstream", "story_analysis_and_downstream"], required=True)
    cp.add_argument("--execute", action="store_true")

    rpr = subparsers.add_parser("run-production-range")
    rpr.add_argument("project_slug", nargs="?", default="princess_of_mars_test")
    rpr.add_argument("--start-phase", choices=OPERATOR_PHASE_ORDER, required=True)
    rpr.add_argument("--end-phase", choices=OPERATOR_PHASE_ORDER, required=True)
    rpr.add_argument("--chapters", type=str, default=None)
    rpr.add_argument("--mode", choices=["resume", "force"], default="force")

    menu = subparsers.add_parser("menu")
    menu.add_argument("project_slug", nargs="?", default="princess_of_mars_test")
    menu.add_argument("--chapters", type=str, default=None)
    menu.add_argument("--mode", choices=["resume", "force"], default="resume")

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "synthesize-character-bibles":
        summary = run_character_bible_synthesis(args.project_slug, use_llm=not args.no_llm, force=args.force, limit=args.limit)
    elif args.command == "refine-character-visual-evidence":
        summary = run_character_visual_evidence_refinement(args.project_slug, force=args.force, only_review=args.only_review, chapters=args.chapters, limit=args.limit)
    elif args.command == "synthesize-environment-bibles":
        summary = run_environment_bible_synthesis(args.project_slug, use_llm=not args.no_llm, force=args.force, limit=args.limit)
    elif args.command == "synthesize-visual-fallbacks":
        summary = run_visual_fallback_synthesis(args.project_slug, force=args.force)
    elif args.command == "synthesize-scene-contracts":
        summary = run_scene_contract_synthesis(args.project_slug, use_llm=not args.no_llm, force=args.force, chapters=args.chapters)
    elif args.command == "synthesize-scene-bindings":
        summary = run_scene_binding_synthesis(args.project_slug, force=args.force, chapters=args.chapters)
    elif args.command == "synthesize-shot-packages":
        summary = run_shot_planning(args.project_slug, use_llm=not args.no_llm, force=args.force, chapters=args.chapters, coverage_density=args.coverage_density)
    elif args.command == "synthesize-dialogue-timeline":
        summary = run_dialogue_timeline(args.project_slug, force=args.force, chapters=args.chapters)
    elif args.command == "synthesize-dialogue-enrichment":
        summary = run_dialogue_enrichment(args.project_slug, force=args.force)
    elif args.command == "synthesize-prompt-preparation":
        summary = run_prompt_preparation(args.project_slug, force=args.force, limit=args.limit, entity_types=args.entity_types, entity_ids=args.entity_ids, chapters=args.chapters, shot_variants=args.shot_variants)
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
    elif args.command == "synthesize-descriptor-enrichment":
        summary = run_descriptor_enrichment(args.project_slug, use_llm=not args.no_llm, force=args.force, limit=args.limit, entity_types=args.entity_types, entity_ids=args.entity_ids, chapters=args.chapters)
    elif args.command == "clear-descriptor-artifacts":
        summary = clear_descriptor_artifacts(args.project_slug, include_prompt_packages=not args.keep_prompts)
    elif args.command == "grade-artifacts":
        summary = run_quality_grading(args.project_slug, families=args.families)
    elif args.command == "rerun-quality-artifacts":
        summary = run_selective_reruns(args.project_slug, execute=args.execute)
    elif args.command == "refine-identities":
        summary = run_identity_refinement(args.project_slug, use_llm=not args.no_llm, apply_merge=args.apply)
    elif args.command == "synthesize-character-taxonomy":
        summary = run_character_taxonomy(args.project_slug, force=args.force, limit=args.limit)
    elif args.command == "ensure-book-ingested":
        ingest_summary = ensure_book_ingested(project_slug=args.project_slug)
        summary = (
            {"project_slug": args.project_slug, "status": "already_ingested"}
            if ingest_summary is None
            else {"project_slug": args.project_slug, "status": "ingested", **ingest_summary.to_dict()}
        )
    elif args.command == "run-downstream-pipeline":
        summary = run_downstream_pipeline(args.project_slug, chapters=args.chapters, start_phase=args.start_phase, pipeline_key=args.pipeline_key, resume=not args.no_resume, use_llm=not args.no_llm, shot_variants=args.shot_variants, coverage_density=args.coverage_density)
    elif args.command == "summarize-downstream-run":
        summary = summarize_downstream_run(args.project_slug, pipeline_key=args.pipeline_key)
    elif args.command == "project-status":
        summary = get_production_status(args.project_slug, chapters=args.chapters)
    elif args.command == "resume-check":
        summary = get_resume_check_summary(args.project_slug, chapters=args.chapters)
    elif args.command == "run-production":
        if args.plan_only:
            summary = plan_trusted_resume_pipeline(args.project_slug, chapters=args.chapters)
        elif args.profile == "post-taxonomy":
            summary = run_full_production_pipeline(
                args.project_slug,
                chapters=args.chapters,
                mode=args.mode,
                start_phase="character_bibles" if args.skip_taxonomy else "character_taxonomy",
                coverage_density=args.coverage_density,
            )
        else:
            summary = run_full_production_pipeline(
                args.project_slug,
                chapters=args.chapters,
                mode=args.mode,
                coverage_density=args.coverage_density,
            )
    elif args.command == "run-story-analysis":
        summary = run_story_analysis_pipeline(
            args.project_slug,
            chapters=args.chapters,
            mode=args.mode,
        )
    elif args.command == "run-quicktest-composite":
        summary = run_quicktest_composite(
            args.project_slug,
            chapters=args.chapters,
            composite=args.composite,
        )
    elif args.command == "run-scene-slice":
        summary = run_scene_slice_pipeline(
            args.project_slug,
            chapter=args.chapter,
            scene=args.scene,
            mode=args.mode,
            coverage_density=args.coverage_density,
        )
    elif args.command == "clear-production":
        if args.execute:
            summary = execute_cleanup_plan(args.project_slug)
        else:
            summary = create_cleanup_plan(args.project_slug, scope=args.scope)
    elif args.command == "run-production-range":
        summary = run_phase_range(
            args.project_slug,
            start_phase=args.start_phase,
            end_phase=args.end_phase,
            chapters=args.chapters,
            mode=args.mode,
        )
    elif args.command == "menu":
        run_pipeline_menu(
            initial_project=args.project_slug,
            initial_chapters=args.chapters,
            initial_mode=args.mode,
            prompt_on_start=True,
        )
        return
    else:
        parser.error(f"Unknown command: {args.command}")
        return

    if hasattr(summary, 'to_dict'):
        payload = summary.to_dict()
    else:
        payload = summary
    if isinstance(payload, dict) and isinstance(payload.get("project_slug"), str):
        persist_run_summary(
            project_slug=payload["project_slug"],
            run_type=str(payload.get("profile") or payload.get("command") or args.command),
            payload=payload,
        )
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
