from __future__ import annotations

import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .common import (
    PROJECTS_ROOT,
    ROOT,
    TEMPLATES_ROOT,
    ensure_dir,
    read_json,
    repo_relative,
    replace_tokens,
    validate_clip_id,
    validate_scene_id,
    write_json,
)
from .registry_loader import get_workflow
from .state import load_clip_state, write_clip_state


PROJECT_DIRS = [
    "01_source/chapters",
    "01_source/excerpts",
    "01_source/notes",
    "02_story_analysis/story_summary",
    "02_story_analysis/scene_breakdowns",
    "02_story_analysis/character_breakdowns",
    "02_story_analysis/environment_breakdowns",
    "02_story_analysis/clip_plans",
    "03_prompt_packages/characters",
    "03_prompt_packages/environments",
    "03_prompt_packages/scenes",
    "03_prompt_packages/keyframes",
    "03_prompt_packages/fixes",
    "03_prompt_packages/cut_motion",
    "03_prompt_packages/anchors",
    "03_prompt_packages/video",
    "04_references/characters",
    "04_references/environments",
    "04_references/scenes",
    "05_scenes",
    "06_reviews/selected",
    "07_finals",
    "logs",
]

CLIP_STILL_DIRS = [
    "character_refs",
    "environment_refs",
    "scene_build",
    "golden_frame",
    "keyframes",
    "fixes",
    "anchor_frames",
    "interval_frames",
    "selected",
]

ASSET_CODE_BY_TARGET = {
    "scene_build": "SB",
    "golden_frame": "GF",
    "approved_keyframe": "KF",
    "approved_video": "MV",
    "approved_still_fix": "FX",
    "anchor_frame": "AF",
    "interval_frame": "IF",
}


def _project_path(project_slug: str) -> Path:
    return PROJECTS_ROOT / project_slug


def _load_template(name: str, replacements: dict[str, str]) -> dict[str, Any]:
    payload = read_json(TEMPLATES_ROOT / name)
    return replace_tokens(payload, replacements)


def _write_prompt_file(path: Path, title: str, prompt_id: str, workflow_type: str, sources: list[str]) -> None:
    content = "\n".join(
        [
            "# Title",
            title,
            "",
            "# ID",
            prompt_id,
            "",
            "# Purpose",
            "Fill in the stage intent here.",
            "",
            "# Workflow Type",
            workflow_type,
            "",
            "# Positive Prompt",
            "Write the positive prompt text here.",
            "",
            "# Negative Prompt",
            "Write the negative prompt text here.",
            "",
            "# Inputs",
            "- project_id:",
            "- scene_id:",
            "- clip_id:",
            "- duration_seconds:",
            "- required_refs:",
            "- optional_refs:",
            "- style_profile:",
            "- batch_role:",
            "- fix_of:",
            "",
            "# Continuity Notes",
            "- Capture the continuity rules for this stage.",
            "",
            "# Sources",
            *[f"- {source}" for source in sources],
            "",
        ]
    )
    ensure_dir(path.parent)
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def create_project(project_slug: str) -> Path:
    project_dir = _project_path(project_slug)
    replacements = {
        "project_template": project_slug,
    }
    for relative_dir in PROJECT_DIRS:
        ensure_dir(project_dir / relative_dir)

    project_state_path = project_dir / "project_state.json"
    if not project_state_path.exists():
        project_state = _load_template("project_state.template.json", replacements)
        write_json(project_state_path, project_state)
    return project_dir


def create_scene(project_slug: str, scene_id: str) -> Path:
    scene_id = validate_scene_id(scene_id)
    project_dir = create_project(project_slug)
    scene_dir = project_dir / "05_scenes" / scene_id

    ensure_dir(project_dir / "02_story_analysis" / "scene_breakdowns" / scene_id)
    ensure_dir(project_dir / "02_story_analysis" / "clip_plans" / scene_id)
    ensure_dir(project_dir / "03_prompt_packages" / "scenes" / scene_id)
    ensure_dir(project_dir / "03_prompt_packages" / "keyframes" / scene_id)
    ensure_dir(project_dir / "03_prompt_packages" / "fixes" / scene_id)
    ensure_dir(project_dir / "03_prompt_packages" / "cut_motion" / scene_id)
    ensure_dir(project_dir / "03_prompt_packages" / "anchors" / scene_id)
    ensure_dir(project_dir / "03_prompt_packages" / "video" / scene_id)
    ensure_dir(project_dir / "04_references" / "scenes" / scene_id)
    ensure_dir(scene_dir / "clips")

    replacements = {
        "project_template": project_slug,
        "SC001": scene_id,
    }
    scene_state_path = scene_dir / "scene_state.json"
    if not scene_state_path.exists():
        scene_state = _load_template("scene_state.template.json", replacements)
        write_json(scene_state_path, scene_state)

    project_state_path = project_dir / "project_state.json"
    project_state = read_json(project_state_path)
    project_state["current_scene_id"] = scene_id
    write_json(project_state_path, project_state)
    return scene_dir


def create_clip(project_slug: str, scene_id: str, clip_id: str) -> Path:
    scene_id = validate_scene_id(scene_id)
    clip_id = validate_clip_id(clip_id)
    scene_dir = create_scene(project_slug, scene_id)
    project_dir = _project_path(project_slug)
    clip_dir = scene_dir / "clips" / clip_id

    ensure_dir(project_dir / "03_prompt_packages" / "scenes" / scene_id / clip_id)
    ensure_dir(project_dir / "03_prompt_packages" / "keyframes" / scene_id / clip_id)
    ensure_dir(project_dir / "03_prompt_packages" / "fixes" / scene_id / clip_id)
    ensure_dir(project_dir / "03_prompt_packages" / "cut_motion" / scene_id / clip_id)
    ensure_dir(project_dir / "03_prompt_packages" / "anchors" / scene_id / clip_id)
    ensure_dir(project_dir / "03_prompt_packages" / "video" / scene_id / clip_id)
    ensure_dir(project_dir / "02_story_analysis" / "clip_plans" / scene_id)
    ensure_dir(clip_dir / "inputs")
    ensure_dir(clip_dir / "video")
    ensure_dir(clip_dir / "logs")
    for stage_dir in CLIP_STILL_DIRS:
        ensure_dir(clip_dir / "stills" / stage_dir)

    replacements = {
        "project_template": project_slug,
        "SC001": scene_id,
        "CL001": clip_id,
    }
    clip_state_path = clip_dir / "clip_state.json"
    if not clip_state_path.exists():
        clip_state = _load_template("clip_state.template.json", replacements)
        write_json(clip_state_path, clip_state)

    scene_state_path = scene_dir / "scene_state.json"
    scene_state = read_json(scene_state_path)
    clip_ids = set(scene_state.get("clip_ids", []))
    clip_ids.add(clip_id)
    scene_state["clip_ids"] = sorted(clip_ids)
    write_json(scene_state_path, scene_state)

    clip_plan_path = project_dir / "02_story_analysis" / "clip_plans" / scene_id / f"{clip_id}.md"
    if not clip_plan_path.exists():
        clip_plan_path.write_text(
            "\n".join(
                [
                    "# Title",
                    f"{scene_id} {clip_id} Clip Plan",
                    "",
                    "# ID",
                    f"{scene_id}_{clip_id}",
                    "",
                    "# Purpose",
                    "Describe the cut beat, framing, and continuity intent for this clip.",
                    "",
                    "# Inputs",
                    "- scene_breakdown:",
                    "- shared_refs:",
                    "- duration_seconds:",
                    "- review_batch_size: 4",
                    "",
                    "# Output Targets",
                    f"- {scene_id}_{clip_id}_KF01_v001.png",
                    f"- {scene_id}_{clip_id}_KF01.png",
                    f"- {scene_id}_{clip_id}_FX01_v001.png",
                    f"- {scene_id}_{clip_id}_MV01_v001.mp4",
                    "",
                ]
            )
            + "\n",
            encoding="utf-8",
        )

    _write_prompt_file(
        project_dir / "03_prompt_packages" / "scenes" / scene_id / clip_id / f"{scene_id}_{clip_id}_scene_stage_prompt.md",
        f"{scene_id} {clip_id} Scene Stage Prompt",
        f"{scene_id}_{clip_id}_scene_stage_prompt",
        "authoring.scene_stage",
        [repo_relative(clip_plan_path)],
    )
    _write_prompt_file(
        project_dir / "03_prompt_packages" / "keyframes" / scene_id / clip_id / f"{scene_id}_{clip_id}_keyframe_prompt.md",
        f"{scene_id} {clip_id} Keyframe Prompt",
        f"{scene_id}_{clip_id}_keyframe_prompt",
        "still.scene_build.four_ref.klein.distilled",
        [repo_relative(clip_plan_path)],
    )
    _write_prompt_file(
        project_dir / "03_prompt_packages" / "fixes" / scene_id / clip_id / f"{scene_id}_{clip_id}_fix_01_prompt.md",
        f"{scene_id} {clip_id} Fix 01 Prompt",
        f"{scene_id}_{clip_id}_fix_01_prompt",
        "still.scene_insert.two_ref.klein.distilled",
        [repo_relative(clip_plan_path)],
    )
    _write_prompt_file(
        project_dir / "03_prompt_packages" / "cut_motion" / scene_id / clip_id / f"{scene_id}_{clip_id}_cut_motion_prompt.md",
        f"{scene_id} {clip_id} Cut Motion Prompt",
        f"{scene_id}_{clip_id}_cut_motion_prompt",
        "video.cut_motion.wan.i2v",
        [repo_relative(clip_plan_path)],
    )
    return clip_dir


def list_workflows() -> list[dict[str, Any]]:
    from .registry_loader import load_registry

    return load_registry()["workflows"]


def _next_run_id(log_dir: Path) -> str:
    ensure_dir(log_dir)
    existing = sorted(log_dir.glob("RUN_*.json"))
    if not existing:
        return "RUN_0001"
    last_number = int(existing[-1].stem.split("_")[1])
    return f"RUN_{last_number + 1:04d}"


def create_run_manifest(
    project_slug: str,
    workflow_id: str,
    stage: str,
    prompt_file: str,
    scene_id: str | None = None,
    clip_id: str | None = None,
    input_refs: list[str] | None = None,
    seed: int | None = None,
) -> Path:
    workflow = get_workflow(workflow_id)
    project_dir = create_project(project_slug)
    input_refs = input_refs or []

    if workflow["output_scope"] == "clip":
        if not scene_id or not clip_id:
            raise ValueError("clip-scoped workflows require both scene_id and clip_id")
        clip_dir = create_clip(project_slug, scene_id, clip_id)
        log_dir = clip_dir / "logs"
        output_root = clip_dir / ("video" if stage == "cut_motion" else "stills")
    elif workflow["output_scope"] == "scene":
        if not scene_id:
            raise ValueError("scene-scoped workflows require scene_id")
        scene_dir = create_scene(project_slug, scene_id)
        log_dir = scene_dir
        output_root = scene_dir
    else:
        log_dir = project_dir / "logs"
        output_root = project_dir / "04_references"

    run_id = _next_run_id(log_dir)
    manifest = _load_template(
        "run_manifest.template.json",
        {
            "project_template": project_slug,
            "SC001": scene_id or "SC001",
            "CL001": clip_id or "CL001",
            "RUN_0001": run_id,
            "still.scene_build.four_ref.klein.distilled": workflow_id,
            "scene_build": stage,
            "projects/project_template/03_prompt_packages/scenes/SC001/CL001/SC001_CL001_scene_build_prompt.md": prompt_file,
        },
    )
    manifest["run_id"] = run_id
    manifest["project_id"] = project_slug
    manifest["scene_id"] = scene_id
    manifest["clip_id"] = clip_id
    manifest["stage"] = stage
    manifest["workflow_id"] = workflow_id
    manifest["prompt_file"] = prompt_file
    manifest["input_refs"] = input_refs
    manifest["seed"] = seed
    manifest["timestamp"] = datetime.now(timezone.utc).isoformat()
    manifest["status"] = "planned"
    manifest["output_root"] = repo_relative(output_root)

    manifest_path = log_dir / f"{run_id}.json"
    write_json(manifest_path, manifest)
    return manifest_path


def promote_asset(
    project_slug: str,
    source: str,
    target: str,
    scene_id: str | None = None,
    clip_id: str | None = None,
    asset_id: str | None = None,
    index: int = 1,
) -> Path:
    source_path = Path(source)
    if not source_path.is_absolute():
        source_path = ROOT / source
    if not source_path.exists():
        raise FileNotFoundError(f"Source asset not found: {source_path}")

    project_dir = create_project(project_slug)
    extension = source_path.suffix

    if target in {"approved_keyframe", "golden_frame", "approved_video", "approved_still_fix", "anchor_frame", "interval_frame"}:
        if not scene_id or not clip_id:
            raise ValueError(f"{target} promotion requires scene_id and clip_id")
        scene_id = validate_scene_id(scene_id)
        clip_id = validate_clip_id(clip_id)
        clip_dir = create_clip(project_slug, scene_id, clip_id)
        folder_map = {
            "approved_keyframe": "keyframes",
            "golden_frame": "golden_frame",
            "approved_video": "video",
            "approved_still_fix": "fixes",
            "anchor_frame": "anchor_frames",
            "interval_frame": "interval_frames",
        }
        asset_code = ASSET_CODE_BY_TARGET[target]
        if target == "approved_video":
            destination = clip_dir / folder_map[target] / f"{scene_id}_{clip_id}_{asset_code}{index:02d}{extension}"
        else:
            destination = clip_dir / "stills" / folder_map[target] / f"{scene_id}_{clip_id}_{asset_code}{index:02d}{extension}"

        clip_state_path = clip_dir / "clip_state.json"
        clip_state = load_clip_state(project_slug, scene_id, clip_id)
        destination_rel = repo_relative(destination)
        if target in {"approved_keyframe", "golden_frame"}:
            clip_state["approved_assets"]["approved_keyframe"] = destination_rel
            clip_state["approved_assets"]["golden_frame"] = destination_rel
            clip_state["current_continuity_source"] = destination_rel
        elif target == "approved_video":
            clip_state["approved_assets"]["approved_video"] = destination_rel
            cut_motion_videos = clip_state["approved_assets"].setdefault("cut_motion_videos", [])
            if destination_rel not in cut_motion_videos:
                cut_motion_videos.append(destination_rel)
        elif target == "approved_still_fix":
            clip_state["approved_assets"]["still_fixes"].append(destination_rel)
            clip_state["current_continuity_source"] = destination_rel
        elif target == "anchor_frame":
            clip_state["approved_assets"]["anchor_frames"].append(destination_rel)
            clip_state["current_continuity_source"] = destination_rel
        else:
            clip_state["approved_assets"]["interval_frames"].append(destination_rel)
            clip_state["current_continuity_source"] = destination_rel
        write_clip_state(project_slug, scene_id, clip_id, clip_state)
    elif target in {"character_reference", "environment_reference"}:
        if not asset_id:
            raise ValueError(f"{target} promotion requires asset_id")
        family = "characters" if target == "character_reference" else "environments"
        prefix = asset_id
        destination = project_dir / "04_references" / family / asset_id / f"{prefix}_ref{index:02d}{extension}"

        project_state_path = project_dir / "project_state.json"
        project_state = read_json(project_state_path)
        destination_rel = repo_relative(destination)
        if target == "character_reference":
            project_state["approved_character_refs"][asset_id] = destination_rel
        else:
            project_state["approved_environment_refs"][asset_id] = destination_rel
        write_json(project_state_path, project_state)
    else:
        raise ValueError(f"Unsupported promotion target: {target}")

    ensure_dir(destination.parent)
    shutil.copy2(source_path, destination)

    review_copy = project_dir / "06_reviews" / "selected" / destination.name
    ensure_dir(review_copy.parent)
    shutil.copy2(destination, review_copy)
    return destination
