from __future__ import annotations

import argparse
import json

from .character_bible import run_character_bible_synthesis
from .identity_refinement import run_identity_refinement


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="FilmCreator tools")
    subparsers = parser.add_subparsers(dest="command", required=True)

    s = subparsers.add_parser("synthesize-character-bibles")
    s.add_argument("project_slug")
    s.add_argument("--no-llm", action="store_true")
    s.add_argument("--force", action="store_true")

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

    elif args.command == "refine-identities":
        result = run_identity_refinement(
            args.project_slug,
            use_llm=not args.no_llm,
            apply_merge=args.apply,
        )
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
