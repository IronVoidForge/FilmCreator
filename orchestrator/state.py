from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .common import PROJECTS_ROOT, ROOT, read_json, repo_relative, write_json
from .style_profiles import empty_stage_style_preferences, stage_family


@dataclass(frozen=True)
class ContinuitySource:
    path: str
    reason: str


def resolve_user_path(value: str) -> Path:
    path = Path(value)
    if path.is_absolute():
        return path
    return ROOT / path


def path_to_manifest_value(path: Path) -> str:
    resolved = path.resolve()
    try:
        return repo_relative(resolved)
    except ValueError:
        return str(resolved)


def project_dir(project_slug: str) -> Path:
    return PROJECTS_ROOT / project_slug


def scene_dir(project_slug: str, scene_id: str) -> Path:
    return project_dir(project_slug) / "05_scenes" / scene_id


def clip_dir(project_slug: str, scene_id: str, clip_id: str) -> Path:
    return scene_dir(project_slug, scene_id) / "clips" / clip_id


def clip_state_path(project_slug: str, scene_id: str, clip_id: str) -> Path:
    return clip_dir(project_slug, scene_id, clip_id) / "clip_state.json"


def load_clip_state(project_slug: str, scene_id: str, clip_id: str) -> dict[str, Any]:
    return normalize_clip_state(read_json(clip_state_path(project_slug, scene_id, clip_id)))


def write_clip_state(project_slug: str, scene_id: str, clip_id: str, payload: dict[str, Any]) -> None:
    write_json(clip_state_path(project_slug, scene_id, clip_id), normalize_clip_state(payload))


def normalize_clip_state(payload: dict[str, Any]) -> dict[str, Any]:
    clip_state = dict(payload)

    inputs = clip_state.setdefault("inputs", {})
    if inputs.get("scene_stage_prompt_package") is None and inputs.get("scene_prompt_package"):
        inputs["scene_stage_prompt_package"] = inputs["scene_prompt_package"]
    if inputs.get("cut_motion_prompt_package") is None and inputs.get("video_prompt_package"):
        inputs["cut_motion_prompt_package"] = inputs["video_prompt_package"]

    inputs.setdefault("shared_character_refs", [])
    inputs.setdefault("shared_environment_refs", [])
    inputs.setdefault("scene_stage_prompt_package", None)
    inputs.setdefault("keyframe_prompt_package", None)
    inputs.setdefault("fix_prompt_packages", [])
    inputs.setdefault("cut_motion_prompt_package", None)
    inputs.setdefault("legacy_anchor_prompt_packages", inputs.get("anchor_prompt_packages", []))
    inputs.setdefault("legacy_video_prompt_package", inputs.get("video_prompt_package"))

    approved_assets = clip_state.setdefault("approved_assets", {})
    if approved_assets.get("approved_keyframe") is None and approved_assets.get("golden_frame"):
        approved_assets["approved_keyframe"] = approved_assets["golden_frame"]
    approved_assets.setdefault("approved_keyframe", None)
    approved_assets.setdefault("golden_frame", approved_assets["approved_keyframe"])
    if approved_assets.get("approved_video") is None and approved_assets.get("cut_motion_videos"):
        approved_assets["approved_video"] = approved_assets["cut_motion_videos"][-1]
    approved_assets.setdefault("approved_video", None)
    approved_assets.setdefault("still_fixes", [])
    approved_assets.setdefault("anchor_frames", [])
    approved_assets.setdefault("interval_frames", [])
    approved_assets.setdefault("cut_motion_videos", [])

    clip_state.setdefault("approved_video_last_frame", None)
    clip_state.setdefault("current_continuity_source", None)
    clip_state.setdefault("latest_runs", {})
    clip_state.setdefault("review_batches", [])
    clip_state.setdefault("latest_review_decision", None)
    clip_state.setdefault("notes", [])

    preferences = clip_state.get("stage_style_preferences")
    default_preferences = empty_stage_style_preferences()
    if not isinstance(preferences, dict):
        preferences = default_preferences
    else:
        for family, family_defaults in default_preferences.items():
            current_family = preferences.setdefault(family, {})
            for profile, counters in family_defaults.items():
                current_profile = current_family.setdefault(profile, {})
                for key, default_value in counters.items():
                    current_profile.setdefault(key, default_value)
    clip_state["stage_style_preferences"] = preferences

    return clip_state


def resolve_continuity_source(project_slug: str, scene_id: str, clip_id: str) -> ContinuitySource:
    clip_state = load_clip_state(project_slug, scene_id, clip_id)

    current = clip_state.get("current_continuity_source")
    if current:
        return ContinuitySource(path=current, reason="clip_state.current_continuity_source")

    approved_assets = clip_state.get("approved_assets", {})
    if clip_state.get("approved_video_last_frame"):
        return ContinuitySource(
            path=clip_state["approved_video_last_frame"],
            reason="clip_state.approved_video_last_frame",
        )

    interval_frames = approved_assets.get("interval_frames", [])
    if interval_frames:
        return ContinuitySource(path=interval_frames[-1], reason="clip_state.approved_assets.interval_frames[-1]")

    anchor_frames = approved_assets.get("anchor_frames", [])
    if anchor_frames:
        return ContinuitySource(path=anchor_frames[-1], reason="clip_state.approved_assets.anchor_frames[-1]")

    approved_keyframe = approved_assets.get("approved_keyframe")
    if approved_keyframe:
        return ContinuitySource(path=approved_keyframe, reason="clip_state.approved_assets.approved_keyframe")

    golden_frame = approved_assets.get("golden_frame")
    if golden_frame:
        return ContinuitySource(path=golden_frame, reason="clip_state.approved_assets.golden_frame")

    raise ValueError(
        f"No approved continuity source exists yet for {project_slug}/{scene_id}/{clip_id}. "
        "Approve a keyframe before running continuity-dependent stages."
    )


def record_clip_run(
    project_slug: str,
    scene_id: str,
    clip_id: str,
    *,
    stage: str,
    manifest_path: Path,
    prompt_file: Path,
) -> None:
    clip_state = load_clip_state(project_slug, scene_id, clip_id)
    clip_state.setdefault("latest_runs", {})[stage] = path_to_manifest_value(manifest_path)

    inputs = clip_state.setdefault("inputs", {})
    prompt_value = path_to_manifest_value(prompt_file)
    if stage in {"scene_build"}:
        inputs["scene_prompt_package"] = prompt_value
        inputs["scene_stage_prompt_package"] = prompt_value
    elif stage in {"keyframe"}:
        inputs["keyframe_prompt_package"] = prompt_value
    elif stage in {"scene_refinement", "scene_build_two_ref", "scene_refinement_two_ref", "still_fix"}:
        fix_prompts = inputs.setdefault("fix_prompt_packages", [])
        if prompt_value not in fix_prompts:
            fix_prompts.append(prompt_value)
    elif stage in {"anchor_frame", "interval_frame"}:
        anchor_prompts = inputs.setdefault("anchor_prompt_packages", [])
        if prompt_value not in anchor_prompts:
            anchor_prompts.append(prompt_value)
        legacy_anchor_prompts = inputs.setdefault("legacy_anchor_prompt_packages", [])
        if prompt_value not in legacy_anchor_prompts:
            legacy_anchor_prompts.append(prompt_value)
    elif stage in {"cut_motion"}:
        inputs["cut_motion_prompt_package"] = prompt_value

    write_clip_state(project_slug, scene_id, clip_id, clip_state)


def record_review_batch(
    project_slug: str,
    scene_id: str,
    clip_id: str,
    *,
    stage: str,
    manifest_path: str | Path,
    review_decision: str,
    chosen_primary: str | None,
    top_two: list[str],
) -> dict[str, Any]:
    valid_decisions = {"approve", "needs_fix", "regenerate_batch"}
    if review_decision not in valid_decisions:
        allowed = ", ".join(sorted(valid_decisions))
        raise ValueError(f"review_decision must be one of: {allowed}")

    manifest_file = resolve_user_path(str(manifest_path))
    if not manifest_file.exists():
        raise FileNotFoundError(f"Run manifest not found: {manifest_file}")

    manifest = read_json(manifest_file)
    candidate_paths = _extract_manifest_candidate_paths(manifest)
    normalized_top_two = [path_to_manifest_value(resolve_user_path(path)) for path in top_two]
    normalized_chosen = path_to_manifest_value(resolve_user_path(chosen_primary)) if chosen_primary else None

    if review_decision == "regenerate_batch":
        normalized_top_two = []
        normalized_chosen = None
    else:
        if len(normalized_top_two) != 2:
            raise ValueError("Top-two review requires exactly two candidate paths.")
        if normalized_chosen is None:
            raise ValueError("A chosen primary candidate is required unless the batch is being regenerated.")
        if normalized_chosen not in normalized_top_two:
            raise ValueError("The chosen primary candidate must also be one of the top two finalists.")

    invalid_paths = sorted(set(normalized_top_two + ([normalized_chosen] if normalized_chosen else [])) - set(candidate_paths))
    if invalid_paths:
        invalid_text = ", ".join(invalid_paths)
        raise ValueError(f"Review paths were not found in the run manifest outputs: {invalid_text}")

    _update_manifest_review_state(
        manifest_file,
        manifest,
        review_decision=review_decision,
        chosen_primary=normalized_chosen,
        top_two=normalized_top_two,
    )

    clip_state = load_clip_state(project_slug, scene_id, clip_id)
    review_entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "stage": stage,
        "stage_family": stage_family(stage),
        "manifest_path": path_to_manifest_value(manifest_file),
        "review_decision": review_decision,
        "candidates": candidate_paths,
        "top_two": normalized_top_two,
        "chosen_primary": normalized_chosen,
    }
    clip_state.setdefault("review_batches", []).append(review_entry)
    clip_state["latest_review_decision"] = {
        "stage": stage,
        "stage_family": stage_family(stage),
        "decision": review_decision,
        "manifest_path": path_to_manifest_value(manifest_file),
        "chosen_primary": normalized_chosen,
        "top_two": normalized_top_two,
        "timestamp": review_entry["timestamp"],
    }

    _update_style_preferences_from_review(clip_state, manifest, review_entry)
    write_clip_state(project_slug, scene_id, clip_id, clip_state)
    return review_entry


def _extract_manifest_candidate_paths(manifest: dict[str, Any]) -> list[str]:
    batch = manifest.get("batch", {})
    candidate_entries = batch.get("candidates", [])
    if candidate_entries:
        paths = []
        for entry in candidate_entries:
            output_files = entry.get("output_files", [])
            if output_files:
                paths.extend(output_files)
        if paths:
            return paths
    return list(manifest.get("output_files", []))


def _update_manifest_review_state(
    manifest_file: Path,
    manifest: dict[str, Any],
    *,
    review_decision: str,
    chosen_primary: str | None,
    top_two: list[str],
) -> None:
    batch = manifest.setdefault("batch", {})
    batch["review_status"] = review_decision
    batch["chosen_primary"] = chosen_primary
    batch["top_two"] = top_two

    for entry in batch.get("candidates", []):
        output_files = entry.get("output_files", [])
        output_file = output_files[0] if output_files else None
        if review_decision == "regenerate_batch":
            entry["review_status"] = "regenerate_batch"
        elif output_file == chosen_primary:
            entry["review_status"] = "chosen_primary"
        elif output_file in top_two:
            entry["review_status"] = "top_two"
        else:
            entry["review_status"] = "rejected"

    write_json(manifest_file, manifest)


def _update_style_preferences_from_review(
    clip_state: dict[str, Any],
    manifest: dict[str, Any],
    review_entry: dict[str, Any],
) -> None:
    family = review_entry["stage_family"]
    preferences = clip_state.setdefault("stage_style_preferences", empty_stage_style_preferences())
    family_preferences = preferences.setdefault(family, {})

    batch = manifest.get("batch", {})
    for entry in batch.get("candidates", []):
        style_profile = entry.get("style_profile")
        output_files = entry.get("output_files", [])
        output_file = output_files[0] if output_files else None
        if not style_profile or not output_file:
            continue

        stats = family_preferences.setdefault(
            style_profile,
            {
                "appearances": 0,
                "top_two": 0,
                "wins": 0,
            },
        )
        stats["appearances"] += 1
        if output_file in review_entry["top_two"]:
            stats["top_two"] += 1
        if output_file == review_entry["chosen_primary"]:
            stats["wins"] += 1
