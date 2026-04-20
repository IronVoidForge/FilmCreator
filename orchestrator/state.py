from __future__ import annotations

from . import features as _features  # noqa: F401
from .common import PROJECTS_ROOT, ROOT, repo_relative
from .features import state as _impl

ContinuitySource = _impl.ContinuitySource


def _sync() -> None:
    _impl.PROJECTS_ROOT = PROJECTS_ROOT
    _impl.ROOT = ROOT
    _impl.repo_relative = repo_relative


def resolve_user_path(value: str):
    _sync()
    return _impl.resolve_user_path(value)


def path_to_manifest_value(path):
    _sync()
    return _impl.path_to_manifest_value(path)


def project_dir(project_slug: str):
    _sync()
    return _impl.project_dir(project_slug)


def scene_dir(project_slug: str, scene_id: str):
    _sync()
    return _impl.scene_dir(project_slug, scene_id)


def clip_dir(project_slug: str, scene_id: str, clip_id: str):
    _sync()
    return _impl.clip_dir(project_slug, scene_id, clip_id)


def clip_state_path(project_slug: str, scene_id: str, clip_id: str):
    _sync()
    return _impl.clip_state_path(project_slug, scene_id, clip_id)


def load_clip_state(project_slug: str, scene_id: str, clip_id: str):
    _sync()
    return _impl.load_clip_state(project_slug, scene_id, clip_id)


def write_clip_state(project_slug: str, scene_id: str, clip_id: str, payload):
    _sync()
    return _impl.write_clip_state(project_slug, scene_id, clip_id, payload)


def normalize_clip_state(payload):
    _sync()
    return _impl.normalize_clip_state(payload)


def resolve_continuity_source(project_slug: str, scene_id: str, clip_id: str):
    _sync()
    return _impl.resolve_continuity_source(project_slug, scene_id, clip_id)


def record_clip_run(*args, **kwargs):
    _sync()
    return _impl.record_clip_run(*args, **kwargs)


def record_review_batch(*args, **kwargs):
    _sync()
    return _impl.record_review_batch(*args, **kwargs)


def _update_manifest_review_state(*args, **kwargs):
    _sync()
    return _impl._update_manifest_review_state(*args, **kwargs)


def _update_style_preferences_from_review(*args, **kwargs):
    _sync()
    return _impl._update_style_preferences_from_review(*args, **kwargs)
