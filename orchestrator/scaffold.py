from __future__ import annotations

from pathlib import Path

from .common import PROJECTS_ROOT, ROOT, TEMPLATES_ROOT, ensure_dir, read_json, repo_relative, replace_tokens, validate_clip_id, validate_scene_id, write_json
from .features import scaffold as _impl
from .state import load_clip_state, write_clip_state
from .video_utils import VideoFrameExtractionError, extract_last_frame


PROJECT_DIRS = _impl.PROJECT_DIRS
CLIP_STILL_DIRS = _impl.CLIP_STILL_DIRS
ASSET_CODE_BY_TARGET = _impl.ASSET_CODE_BY_TARGET
LAST_VIDEO_FRAME_ASSET_CODE = _impl.LAST_VIDEO_FRAME_ASSET_CODE


def _sync() -> None:
    _impl.PROJECTS_ROOT = PROJECTS_ROOT
    _impl.ROOT = ROOT
    _impl.TEMPLATES_ROOT = TEMPLATES_ROOT
    _impl.ensure_dir = ensure_dir
    _impl.read_json = read_json
    _impl.repo_relative = repo_relative
    _impl.replace_tokens = replace_tokens
    _impl.validate_clip_id = validate_clip_id
    _impl.validate_scene_id = validate_scene_id
    _impl.write_json = write_json
    _impl.load_clip_state = load_clip_state
    _impl.write_clip_state = write_clip_state
    _impl.extract_last_frame = extract_last_frame
    _impl.VideoFrameExtractionError = VideoFrameExtractionError


def create_project(project_slug: str) -> Path:
    _sync()
    return _impl.create_project(project_slug)


def create_scene(project_slug: str, scene_id: str) -> Path:
    _sync()
    return _impl.create_scene(project_slug, scene_id)


def create_clip(project_slug: str, scene_id: str, clip_id: str) -> Path:
    _sync()
    return _impl.create_clip(project_slug, scene_id, clip_id)


def list_workflows() -> list[dict[str, object]]:
    _sync()
    return _impl.list_workflows()


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
    _sync()
    return _impl.create_run_manifest(
        project_slug=project_slug,
        workflow_id=workflow_id,
        stage=stage,
        prompt_file=prompt_file,
        scene_id=scene_id,
        clip_id=clip_id,
        input_refs=input_refs,
        seed=seed,
    )


def promote_asset(
    project_slug: str,
    source: str,
    target: str,
    scene_id: str | None = None,
    clip_id: str | None = None,
    asset_id: str | None = None,
    index: int = 1,
) -> Path:
    _sync()
    return _impl.promote_asset(
        project_slug=project_slug,
        source=source,
        target=target,
        scene_id=scene_id,
        clip_id=clip_id,
        asset_id=asset_id,
        index=index,
    )
