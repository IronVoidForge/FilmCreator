from __future__ import annotations

import argparse
import json

from .batch_runner import plan_prompt_batch, run_prompt_batch
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
from .state import record_review_batch


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="FilmCreator orchestration scaffold tools")
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_project = subparsers.add_parser("init-project", help="Create a project workspace")
    init_project.add_argument("project_slug")

    init_scene = subparsers.add_parser("init-scene", help="Create a scene workspace")
    init_scene.add_argument("project_slug")
    init_scene.add_argument("scene_id")

    init_clip = subparsers.add_parser("init-clip", help="Create a clip workspace")
    init_clip.add_argument("project_slug")
    init_clip.add_argument("scene_id")
    init_clip.add_argument("clip_id")

    list_cmd = subparsers.add_parser("list-workflows", help="List canonical workflow registry entries")
    list_cmd.add_argument("--json", action="store_true", help="Print the registry as JSON")

    show_cmd = subparsers.add_parser("show-workflow", help="Show one workflow registry entry")
    show_cmd.add_argument("workflow_id")

    manifest_cmd = subparsers.add_parser("plan-run", help="Create a planned run manifest")
    manifest_cmd.add_argument("project_slug")
    manifest_cmd.add_argument("workflow_id")
    manifest_cmd.add_argument("stage")
    manifest_cmd.add_argument("prompt_file")
    manifest_cmd.add_argument("--scene")
    manifest_cmd.add_argument("--clip")
    manifest_cmd.add_argument("--seed", type=int)
    manifest_cmd.add_argument("--ref", action="append", default=[])

    promote_cmd = subparsers.add_parser("promote-asset", help="Promote a selected asset into the canonical hierarchy")
    promote_cmd.add_argument("project_slug")
    promote_cmd.add_argument("source")
    promote_cmd.add_argument("target")
    promote_cmd.add_argument("--scene")
    promote_cmd.add_argument("--clip")
    promote_cmd.add_argument("--asset-id")
    promote_cmd.add_argument("--index", type=int, default=1)

    review_cmd = subparsers.add_parser("review-batch", help="Record the review result for a generated candidate batch")
    review_cmd.add_argument("project_slug")
    review_cmd.add_argument("scene_id")
    review_cmd.add_argument("clip_id")
    review_cmd.add_argument("stage")
    review_cmd.add_argument("manifest_path")
    review_cmd.add_argument("--decision", required=True, choices=["approve", "needs_fix", "regenerate_batch"])
    review_cmd.add_argument("--primary")
    review_cmd.add_argument("--top-two", action="append", default=[])

    review_candidates_cmd = subparsers.add_parser(
        "list-review-candidates",
        help="List the candidate outputs recorded in a batch manifest",
    )
    review_candidates_cmd.add_argument("manifest_path")

    interactive_review_cmd = subparsers.add_parser(
        "interactive-review-and-promote",
        help="Interactively review a batch and promote the selected primary candidate",
    )
    interactive_review_cmd.add_argument("project_slug")
    interactive_review_cmd.add_argument("scene_id")
    interactive_review_cmd.add_argument("clip_id")
    interactive_review_cmd.add_argument("stage")
    interactive_review_cmd.add_argument("manifest_path")
    interactive_review_cmd.add_argument("promotion_target")
    interactive_review_cmd.add_argument("--index", type=int, default=1)

    run_cmd = subparsers.add_parser("run-still", help="Prepare or execute a still-image run")
    run_cmd.add_argument("project_slug")
    run_cmd.add_argument("stage")
    run_cmd.add_argument("prompt_file")
    run_cmd.add_argument("--workflow-id")
    run_cmd.add_argument("--scene")
    run_cmd.add_argument("--clip")
    run_cmd.add_argument("--asset-id")
    run_cmd.add_argument("--ref", action="append", default=[], help="Image slot mapping in slot=path form")
    run_cmd.add_argument("--seed", type=int)
    run_cmd.add_argument(
        "--execute",
        action="store_true",
        help="Submit the prepared workflow to ComfyUI after validation",
    )

    plan_batch_cmd = subparsers.add_parser(
        "plan-batch",
        help="Generate a review batch of styled prompt packages for a keyframe or still-fix stage",
    )
    plan_batch_cmd.add_argument("project_slug")
    plan_batch_cmd.add_argument("stage")
    plan_batch_cmd.add_argument("--prompt-file")
    plan_batch_cmd.add_argument("--scene")
    plan_batch_cmd.add_argument("--clip")
    plan_batch_cmd.add_argument("--workflow-id")
    plan_batch_cmd.add_argument("--batch-size", type=int)
    plan_batch_cmd.add_argument("--seed", type=int)

    run_batch_cmd = subparsers.add_parser(
        "run-batch",
        help="Prepare or execute every candidate prompt in a planned review batch",
    )
    run_batch_cmd.add_argument("batch_manifest")
    run_batch_cmd.add_argument("--ref", action="append", default=[], help="Image slot mapping in slot=path form")
    run_batch_cmd.add_argument("--seed-base", type=int)
    run_batch_cmd.add_argument(
        "--execute",
        action="store_true",
        help="Submit every prepared candidate workflow in the batch to ComfyUI",
    )

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "init-project":
        path = create_project(args.project_slug)
        print(path)
        return

    if args.command == "init-scene":
        path = create_scene(args.project_slug, args.scene_id)
        print(path)
        return

    if args.command == "init-clip":
        path = create_clip(args.project_slug, args.scene_id, args.clip_id)
        print(path)
        return

    if args.command == "list-workflows":
        workflows = list_workflows()
        if args.json:
            print(json.dumps(workflows, indent=2))
        else:
            for workflow in workflows:
                print(f"{workflow['id']}: {workflow['filename']}")
        return

    if args.command == "show-workflow":
        print(json.dumps(get_workflow(args.workflow_id), indent=2))
        return

    if args.command == "plan-run":
        path = create_run_manifest(
            project_slug=args.project_slug,
            workflow_id=args.workflow_id,
            stage=args.stage,
            prompt_file=args.prompt_file,
            scene_id=args.scene,
            clip_id=args.clip,
            input_refs=args.ref,
            seed=args.seed,
        )
        print(path)
        return

    if args.command == "promote-asset":
        path = promote_asset(
            project_slug=args.project_slug,
            source=args.source,
            target=args.target,
            scene_id=args.scene,
            clip_id=args.clip,
            asset_id=args.asset_id,
            index=args.index,
        )
        print(path)
        return

    if args.command == "run-still":
        summary = run_still(
            project_slug=args.project_slug,
            stage=args.stage,
            prompt_file=args.prompt_file,
            workflow_id=args.workflow_id,
            scene_id=args.scene,
            clip_id=args.clip,
            asset_id=args.asset_id,
            ref_args=args.ref,
            seed=args.seed,
            execute=args.execute,
        )
        print(json.dumps(summary.to_dict(), indent=2))
        return

    if args.command == "plan-batch":
        summary = plan_prompt_batch(
            project_slug=args.project_slug,
            stage=args.stage,
            prompt_file=args.prompt_file,
            scene_id=args.scene,
            clip_id=args.clip,
            workflow_id=args.workflow_id,
            batch_size=args.batch_size,
            seed=args.seed,
        )
        print(json.dumps(summary.to_dict(), indent=2))
        return

    if args.command == "run-batch":
        summary = run_prompt_batch(
            batch_manifest_path=args.batch_manifest,
            ref_args=args.ref,
            seed_base=args.seed_base,
            execute=args.execute,
        )
        print(json.dumps(summary.to_dict(), indent=2))
        return

    if args.command == "review-batch":
        review = record_review_batch(
            args.project_slug,
            args.scene_id,
            args.clip_id,
            stage=args.stage,
            manifest_path=args.manifest_path,
            review_decision=args.decision,
            chosen_primary=args.primary,
            top_two=args.top_two,
        )
        print(json.dumps(review, indent=2))
        return

    if args.command == "list-review-candidates":
        print(json.dumps(review_candidates_summary(args.manifest_path), indent=2))
        return

    if args.command == "interactive-review-and-promote":
        summary = interactive_review_and_promote_batch(
            project_slug=args.project_slug,
            scene_id=args.scene_id,
            clip_id=args.clip_id,
            stage=args.stage,
            manifest_path=args.manifest_path,
            promotion_target=args.promotion_target,
            promotion_index=args.index,
        )
        clip_state = summary["clip_state"]
        manifest = summary["manifest"]
        latest_review = clip_state.get("latest_review_decision") or {}

        print("Approval summary:")
        if args.promotion_target == "approved_keyframe":
            print(f"approved_keyframe: {clip_state['approved_assets'].get('approved_keyframe')}")
            print(f"golden_frame: {clip_state['approved_assets'].get('golden_frame')}")
            print(f"current_continuity_source: {clip_state.get('current_continuity_source')}")
        elif args.promotion_target == "approved_video":
            print(f"approved_video: {clip_state['approved_assets'].get('approved_video')}")
            print(f"approved_video_last_frame: {clip_state.get('approved_video_last_frame')}")
        elif args.promotion_target == "approved_still_fix":
            still_fixes = clip_state["approved_assets"].get("still_fixes", [])
            print(f"approved_still_fix: {still_fixes[-1] if still_fixes else None}")
            print(f"current_continuity_source: {clip_state.get('current_continuity_source')}")
        print(f"latest_review_decision: {latest_review.get('decision')}")
        print(f"chosen_primary: {latest_review.get('chosen_primary')}")
        print("top_two:")
        for candidate in latest_review.get("top_two", []):
            print(f"  {candidate}")
        print("")
        print("Manifest review summary:")
        print(f"batch.review_status: {manifest.get('batch', {}).get('review_status')}")
        print(f"batch.chosen_primary: {manifest.get('batch', {}).get('chosen_primary')}")
        print("batch.top_two:")
        for candidate in manifest.get("batch", {}).get("top_two", []):
            print(f"  {candidate}")
        return


if __name__ == "__main__":
    main()
