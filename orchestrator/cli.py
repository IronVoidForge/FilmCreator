from __future__ import annotations

import argparse
import json

from .character_bible import run_character_bible_synthesis
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
from .scene_contracts import run_scene_contract_synthesis
from .scene_bindings import run_scene_binding_synthesis
from .shot_planner import run_shot_planning


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="FilmCreator tools")
    subparsers = parser.add_subparsers(dest="command", required=True)

    s = subparsers.add_parser("synthesize-character-bibles")
    s.add_argument("project_slug")
    s.add_argument("--no-llm", action="store_true")
    s.add_argument("--force", action="store_true")

    e = subparsers.add_parser("synthesize-environment-bibles")
    e.add_argument("project_slug")
    e.add_argument("--no-llm", action="store_true")
    e.add_argument("--force", action="store_true")

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
    crg.add_argument("--limit", type=int, default=None)
    crg.add_argument("--variant", action="append", dest="variants")
    crg.add_argument("--character-id", action="append", dest="character_ids")
    crg.add_argument("--execute", action="store_true")
    crg.add_argument("--seed", type=int, default=None)
    crg.add_argument("--workflow-id", type=str, default=None)

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
    erg.add_argument("--limit", type=int, default=None)
    erg.add_argument("--variant", action="append", dest="variants")
    erg.add_argument("--environment-id", action="append", dest="environment_ids")
    erg.add_argument("--execute", action="store_true")
    erg.add_argument("--seed", type=int, default=None)
    erg.add_argument("--workflow-id", type=str, default=None)

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

    dp = subparsers.add_parser("run-downstream-pipeline")
    dp.add_argument("project_slug")
    dp.add_argument("--chapters", type=str, default=None)
    dp.add_argument("--start-phase", choices=["scene_contracts", "scene_bindings", "shot_packages", "dialogue_timeline", "descriptor_enrichment", "prompt_preparation"], default="scene_contracts")
    dp.add_argument("--pipeline-key", type=str, default="downstream_pipeline")
    dp.add_argument("--no-resume", action="store_true")
    dp.add_argument("--no-llm", action="store_true")
    dp.add_argument("--shot-variant", action="append", choices=["primary_keyframe", "alternate_angle", "consistency_repair"], dest="shot_variants")

    ds = subparsers.add_parser("summarize-downstream-run")
    ds.add_argument("project_slug")
    ds.add_argument("--pipeline-key", type=str, default="downstream_pipeline")

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "synthesize-character-bibles":
        summary = run_character_bible_synthesis(args.project_slug, use_llm=not args.no_llm, force=args.force)
    elif args.command == "synthesize-environment-bibles":
        summary = run_environment_bible_synthesis(args.project_slug, use_llm=not args.no_llm, force=args.force)
    elif args.command == "synthesize-scene-contracts":
        summary = run_scene_contract_synthesis(args.project_slug, use_llm=not args.no_llm, force=args.force, chapters=args.chapters)
    elif args.command == "synthesize-scene-bindings":
        summary = run_scene_binding_synthesis(args.project_slug, force=args.force, chapters=args.chapters)
    elif args.command == "synthesize-shot-packages":
        summary = run_shot_planning(args.project_slug, use_llm=not args.no_llm, force=args.force, chapters=args.chapters)
    elif args.command == "synthesize-dialogue-timeline":
        summary = run_dialogue_timeline(args.project_slug, force=args.force, chapters=args.chapters)
    elif args.command == "synthesize-dialogue-enrichment":
        summary = run_dialogue_enrichment(args.project_slug, force=args.force)
    elif args.command == "synthesize-prompt-preparation":
        summary = run_prompt_preparation(args.project_slug, force=args.force, limit=args.limit, entity_types=args.entity_types, entity_ids=args.entity_ids, chapters=args.chapters, shot_variants=args.shot_variants)
    elif args.command == "plan-character-references":
        summary = run_character_reference_planning(args.project_slug, force=args.force, variants=args.variants, limit=args.limit)
    elif args.command == "generate-character-references":
        summary = run_character_reference_generation(args.project_slug, limit=args.limit, variants=args.variants, character_ids=args.character_ids, execute=args.execute, seed=args.seed, workflow_id=args.workflow_id)
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
        summary = run_environment_reference_generation(args.project_slug, limit=args.limit, variants=args.variants, environment_ids=args.environment_ids, execute=args.execute, seed=args.seed, workflow_id=args.workflow_id)
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
    elif args.command == "run-downstream-pipeline":
        summary = run_downstream_pipeline(args.project_slug, chapters=args.chapters, start_phase=args.start_phase, pipeline_key=args.pipeline_key, resume=not args.no_resume, use_llm=not args.no_llm, shot_variants=args.shot_variants)
    elif args.command == "summarize-downstream-run":
        summary = summarize_downstream_run(args.project_slug, pipeline_key=args.pipeline_key)
    else:
        parser.error(f"Unknown command: {args.command}")
        return

    print(json.dumps(summary.to_dict(), indent=2))


if __name__ == "__main__":
    main()
