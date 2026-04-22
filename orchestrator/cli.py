from __future__ import annotations

import argparse
import json

from .character_bible import run_character_bible_synthesis
from .descriptor_enrichment import clear_descriptor_artifacts, run_descriptor_enrichment
from .dialogue_enrichment import run_dialogue_enrichment
from .downstream_pipeline import run_downstream_pipeline
from .dialogue_timeline import run_dialogue_timeline
from .environment_bible import run_environment_bible_synthesis
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
    pp.add_argument(
        "--entity-type",
        action="append",
        choices=["character", "environment", "scene", "shot"],
        dest="entity_types",
    )
    pp.add_argument("--entity-id", action="append", dest="entity_ids")
    pp.add_argument("--chapters", type=str, default=None)
    pp.add_argument(
        "--shot-variant",
        action="append",
        choices=["primary_keyframe", "alternate_angle", "consistency_repair"],
        dest="shot_variants",
    )

    de = subparsers.add_parser("synthesize-descriptor-enrichment")
    de.add_argument("project_slug")
    de.add_argument("--no-llm", action="store_true")
    de.add_argument("--force", action="store_true")
    de.add_argument("--limit", type=int, default=None)
    de.add_argument(
        "--entity-type",
        action="append",
        choices=["character", "environment", "scene", "shot", "key_item"],
        dest="entity_types",
    )
    de.add_argument("--entity-id", action="append", dest="entity_ids")
    de.add_argument("--chapters", type=str, default=None)

    qg = subparsers.add_parser("grade-artifacts")
    qg.add_argument("project_slug")
    qg.add_argument(
        "--family",
        action="append",
        choices=[
            "character",
            "environment",
            "scene",
            "shot",
            "dialogue",
            "descriptor",
            "prompt",
            "character_bible",
            "environment_bible",
            "scene_contract",
            "shot_package",
            "dialogue_timeline",
            "prompt_package",
        ],
        dest="families",
    )

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
    dp.add_argument(
        "--start-phase",
        choices=[
            "scene_contracts",
            "scene_bindings",
            "shot_packages",
            "dialogue_timeline",
            "descriptor_enrichment",
            "prompt_preparation",
        ],
        default="scene_contracts",
    )
    dp.add_argument("--pipeline-key", type=str, default="downstream_pipeline")
    dp.add_argument("--no-resume", action="store_true")
    dp.add_argument("--no-llm", action="store_true")
    dp.add_argument(
        "--shot-variant",
        action="append",
        choices=["primary_keyframe", "alternate_angle", "consistency_repair"],
        dest="shot_variants",
    )

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "synthesize-character-bibles":
        summary = run_character_bible_synthesis(
            args.project_slug,
            use_llm=not args.no_llm,
            force=args.force,
        )
        print(json.dumps(summary.to_dict(), indent=2))

    elif args.command == "synthesize-environment-bibles":
        summary = run_environment_bible_synthesis(
            args.project_slug,
            use_llm=not args.no_llm,
            force=args.force,
        )
        print(json.dumps(summary.to_dict(), indent=2))

    elif args.command == "synthesize-scene-contracts":
        summary = run_scene_contract_synthesis(
            args.project_slug,
            use_llm=not args.no_llm,
            force=args.force,
            chapters=args.chapters,
        )
        print(json.dumps(summary.to_dict(), indent=2))

    elif args.command == "synthesize-scene-bindings":
        summary = run_scene_binding_synthesis(
            args.project_slug,
            force=args.force,
            chapters=args.chapters,
        )
        print(json.dumps(summary.to_dict(), indent=2))

    elif args.command == "synthesize-shot-packages":
        summary = run_shot_planning(
            args.project_slug,
            use_llm=not args.no_llm,
            force=args.force,
            chapters=args.chapters,
        )
        print(json.dumps(summary.to_dict(), indent=2))

    elif args.command == "synthesize-dialogue-timeline":
        summary = run_dialogue_timeline(
            args.project_slug,
            force=args.force,
            chapters=args.chapters,
        )
        print(json.dumps(summary.to_dict(), indent=2))

    elif args.command == "synthesize-dialogue-enrichment":
        summary = run_dialogue_enrichment(
            args.project_slug,
            force=args.force,
        )
        print(json.dumps(summary.to_dict(), indent=2))

    elif args.command == "synthesize-prompt-preparation":
        summary = run_prompt_preparation(
            args.project_slug,
            force=args.force,
            limit=args.limit,
            entity_types=args.entity_types,
            entity_ids=args.entity_ids,
            chapters=args.chapters,
            shot_variants=args.shot_variants,
        )
        print(json.dumps(summary.to_dict(), indent=2))

    elif args.command == "synthesize-descriptor-enrichment":
        summary = run_descriptor_enrichment(
            args.project_slug,
            use_llm=not args.no_llm,
            force=args.force,
            limit=args.limit,
            entity_types=args.entity_types,
            entity_ids=args.entity_ids,
            chapters=args.chapters,
        )
        print(json.dumps(summary.to_dict(), indent=2))

    elif args.command == "clear-descriptor-artifacts":
        summary = clear_descriptor_artifacts(
            args.project_slug,
            include_prompt_packages=not args.keep_prompts,
        )
        print(json.dumps(summary.to_dict(), indent=2))

    elif args.command == "grade-artifacts":
        summary = run_quality_grading(
            args.project_slug,
            families=args.families,
        )
        print(json.dumps(summary.to_dict(), indent=2))

    elif args.command == "rerun-quality-artifacts":
        summary = run_selective_reruns(
            args.project_slug,
            execute=args.execute,
        )
        print(json.dumps(summary.to_dict(), indent=2))

    elif args.command == "refine-identities":
        result = run_identity_refinement(
            args.project_slug,
            use_llm=not args.no_llm,
            apply_merge=args.apply,
        )
        print(json.dumps(result.to_dict(), indent=2))

    elif args.command == "run-downstream-pipeline":
        summary = run_downstream_pipeline(
            args.project_slug,
            chapters=args.chapters,
            start_phase=args.start_phase,
            pipeline_key=args.pipeline_key,
            resume=not args.no_resume,
            use_llm=not args.no_llm,
            shot_variants=args.shot_variants,
        )
        print(json.dumps(summary.to_dict(), indent=2))


if __name__ == "__main__":
    main()
