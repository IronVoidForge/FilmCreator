from __future__ import annotations

from pathlib import Path
from typing import Any

from .core.json_io import read_json, write_json
from .core.paths import PROJECTS_ROOT, REGISTRY_PATH, ROOT, TEMPLATES_ROOT, ensure_dir, repo_relative
from .core.validation import CLIP_ID_PATTERN, SCENE_ID_PATTERN, validate_clip_id, validate_scene_id


def replace_tokens(payload: Any, replacements: dict[str, str]) -> Any:
    if isinstance(payload, dict):
        return {key: replace_tokens(value, replacements) for key, value in payload.items()}
    if isinstance(payload, list):
        return [replace_tokens(item, replacements) for item in payload]
    if isinstance(payload, str):
        result = payload
        for key, value in replacements.items():
            result = result.replace(key, value)
        return result
    return payload


__all__ = [
    "ROOT",
    "PROJECTS_ROOT",
    "REGISTRY_PATH",
    "TEMPLATES_ROOT",
    "ensure_dir",
    "read_json",
    "write_json",
    "repo_relative",
    "replace_tokens",
    "SCENE_ID_PATTERN",
    "CLIP_ID_PATTERN",
    "validate_scene_id",
    "validate_clip_id",
]
