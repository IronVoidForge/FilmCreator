from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PROJECTS_ROOT = ROOT / "projects"
REGISTRY_PATH = ROOT / "orchestrator" / "registry" / "workflow_registry.json"
TEMPLATES_ROOT = ROOT / "orchestrator" / "templates"
SCENE_ID_PATTERN = re.compile(r"(?:CH\d{3}_)?SC\d{3}$")
CLIP_ID_PATTERN = re.compile(r"CL\d{3}$")


def ensure_dir(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    return path


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: Any) -> None:
    ensure_dir(path.parent)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def repo_relative(path: Path) -> str:
    return path.resolve().relative_to(ROOT).as_posix()


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


def validate_scene_id(scene_id: str) -> str:
    normalized = scene_id.strip().upper()
    if not SCENE_ID_PATTERN.fullmatch(normalized):
        raise ValueError("scene_id must be SC### or CH###_SC###, for example SC001 or CH008_SC001")
    return normalized


def validate_clip_id(clip_id: str) -> str:
    normalized = clip_id.strip().upper()
    if not CLIP_ID_PATTERN.fullmatch(normalized):
        raise ValueError("clip_id must be CL###, for example CL001")
    return normalized
