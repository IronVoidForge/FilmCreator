from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List

from .common import ensure_dir, repo_relative
from .scaffold import create_project


def _world_dir(project_slug: str) -> Path:
    project_dir = create_project(project_slug)
    world_dir = project_dir / "02_story_analysis" / "world"
    ensure_dir(world_dir)
    return world_dir


def _character_registry_path(project_slug: str) -> Path:
    return _world_dir(project_slug) / "CHARACTER_REGISTRY.json"


def _environment_registry_path(project_slug: str) -> Path:
    return _world_dir(project_slug) / "ENVIRONMENT_REGISTRY.json"


def _load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def _write_json(path: Path, data: dict) -> None:
    ensure_dir(path.parent)
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")


def resolve_character_registry(project_slug: str, character_files: List[Path]) -> dict:
    path = _character_registry_path(project_slug)
    registry = _load_json(path)

    for file in character_files:
        asset_id = file.stem

        # naive canonicalization for B1
        canonical_id = asset_id

        # merge simple aliases
        if "john" in asset_id and "carter" in asset_id:
            canonical_id = "john_carter"

        entry = registry.get(canonical_id, {
            "canonical_id": canonical_id,
            "aliases": [],
            "sources": []
        })

        if asset_id not in entry["aliases"] and asset_id != canonical_id:
            entry["aliases"].append(asset_id)

        rel_path = str(file)
        if rel_path not in entry["sources"]:
            entry["sources"].append(rel_path)

        registry[canonical_id] = entry

    _write_json(path, registry)
    return registry


def resolve_environment_registry(project_slug: str, env_files: List[Path]) -> dict:
    path = _environment_registry_path(project_slug)
    registry = _load_json(path)

    for file in env_files:
        asset_id = file.stem

        canonical_id = asset_id

        entry = registry.get(canonical_id, {
            "canonical_id": canonical_id,
            "sources": []
        })

        rel_path = str(file)
        if rel_path not in entry["sources"]:
            entry["sources"].append(rel_path)

        registry[canonical_id] = entry

    _write_json(path, registry)
    return registry


def run_phase_b1_resolution(project_slug: str) -> dict:
    project_dir = create_project(project_slug)

    char_dir = project_dir / "02_story_analysis" / "character_breakdowns"
    env_dir = project_dir / "02_story_analysis" / "environment_breakdowns"

    char_files = list(char_dir.glob("*.md"))
    env_files = list(env_dir.glob("*.md"))

    char_registry = resolve_character_registry(project_slug, char_files)
    env_registry = resolve_environment_registry(project_slug, env_files)

    return {
        "character_registry": char_registry,
        "environment_registry": env_registry
    }
