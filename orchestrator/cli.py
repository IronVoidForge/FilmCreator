from __future__ import annotations

import argparse
import json

from .character_bible import run_character_bible_synthesis
from .descriptor_enrichment import run_descriptor_enrichment
from .dialogue_timeline import run_dialogue_timeline
from .environment_bible import run_environment_bible_synthesis
from .identity_refinement import run_identity_refinement
from .prompt_preparation import run_prompt_preparation
from .scene_contracts import run_scene_contract_synthesis
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

    sp = subparsers.add_parser("synthesize-shot-packages")
    sp.add_argument("project_slug")
    sp.add_argument("--no-llm", action="store_true")
    sp.add_argument("--force", action="store_true")

    dt = subparsers.add_parser("synthesize-dialogue-timeline")
    dt.add_argument("project_slug")
    dt.add_argument("--force", action="store_true")

    pp = subparsers.add_parser("synthesize-prompt-preparation")
    pp.add_argument("project_slug")
    pp.add_argument("--force", action="store_true")

    de = subparsers.add_parser("synthesize-descriptor-enrichment")
    de.add_argument("project_slug")
    de.add_argument("--no-llm", action="store_true")
    de.add_argument("--force", action="store_true")

    r = subparsers.add_parser("refine-identities")
    r.add_argument("project_slug")
    r.add_argument("--no-llm", action="store_true")
    r.add_argument("--apply", action="store_true")

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
        )
        print(json.dumps(summary.to_dict(), indent=2))

    elif args.command == "synthesize-shot-packages":
        summary = run_shot_planning(
            args.project_slug,
            use_llm=not args.no_llm,
            force=args.force,
        )
        print(json.dumps(summary.to_dict(), indent=2))

    elif args.command == "synthesize-dialogue-timeline":
        summary = run_dialogue_timeline(
            args.project_slug,
            force=args.force,
        )
        print(json.dumps(summary.to_dict(), indent=2))

    elif args.command == "synthesize-prompt-preparation":
        summary = run_prompt_preparation(
            args.project_slug,
            force=args.force,
        )
        print(json.dumps(summary.to_dict(), indent=2))

    elif args.command == "synthesize-descriptor-enrichment":
        summary = run_descriptor_enrichment(
            args.project_slug,
            use_llm=not args.no_llm,
            force=args.force,
        )
        print(json.dumps(summary.to_dict(), indent=2))

    elif args.command == "refine-identities":
        result = run_identity_refinement(
            args.project_slug,
            use_llm=not args.no_llm,
            apply_merge=args.apply,
        )
        print(json.dumps(result.to_dict(), indent=2))


if __name__ == "__main__":
    main()
