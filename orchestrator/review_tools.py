from __future__ import annotations

from .common import repo_relative
from .features import review_tools as _impl
from .state import load_clip_state, path_to_manifest_value, record_review_batch, resolve_user_path

ReviewCandidate = _impl.ReviewCandidate


def _sync() -> None:
    _impl.resolve_user_path = resolve_user_path
    _impl.path_to_manifest_value = path_to_manifest_value
    _impl.record_review_batch = record_review_batch
    _impl.load_clip_state = load_clip_state


def list_review_candidates(manifest_path):
    _sync()
    return _impl.list_review_candidates(manifest_path)


def review_candidates_summary(manifest_path):
    _sync()
    return _impl.review_candidates_summary(manifest_path)


def review_and_promote_batch(*args, **kwargs):
    _sync()
    return _impl.review_and_promote_batch(*args, **kwargs)


def interactive_review_and_promote_batch(*args, **kwargs):
    _sync()
    return _impl.interactive_review_and_promote_batch(*args, **kwargs)
