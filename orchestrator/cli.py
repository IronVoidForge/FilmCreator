from __future__ import annotations

import argparse
import json

from .authoring import lmstudio_check, write_prompts
from .batch_runner import plan_prompt_batch, run_prompt_batch
from .book_authoring import refine_world, retry_failed_chapters
from .registry_loader import get_workflow
from .review_tools import interactive_review_and_promote_batch, review_candidates_summary
from .runner import run_still
from .scaffold import (
    create_clip,
    create_project,
    create_run_manifest,
    create_scene,
    list_workflows,
    promote_asset,
)
from .story_authoring import analyze_chapter, authoring_checkpoint, plan_scene, write_shared_prompts
from .state import record_review_batch
from .character_bible import run_character_bible_synthesis


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="FilmCreator orchestration scaffold tools")
    subparsers = parser.add_subparsers(dest="command", required=True)

    synth_cmd = subparsers.add_parser(
        "synthesize-character-bibles",
        help="Run Phase 7 character bible synthesis",
    )
    synth_cmd.add_argument("project_slug")
    synth_cmd.add_argument("--no-llm", action="store_true")
    synth_cmd.add_argument("--force", action="store_true")

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
        return


if __name__ == "__main__":
    main()
