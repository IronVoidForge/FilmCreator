from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable

from .common import ensure_dir, repo_relative
from .scaffold import create_project


CHARACTER_SKIP_NAMES = {"CHARACTER_INDEX.md", "README.md"}
ENVIRONMENT_SKIP_NAMES = {"ENVIRONMENT_INDEX.md", "README.md"}
GENERIC_CHARACTER_LABELS = {"captain", "guard", "captive", "woman", "man", "girl", "boy", "narrator", "hound"}


def _world_dir(project_slug: str) -> Path:
    project_dir = create_project(project_slug)
    world_dir = project_dir / "02_story_analysis" / "world"
    ensure_dir(world_dir)
    return world_dir


def character_registry_path(project_slug: str) -> Path:
    return _world_dir(project_slug) / "CHARACTER_REGISTRY.json"


def environment_registry_path(project_slug: str) -> Path:
    return _world_dir(project_slug) / "ENVIRONMENT_REGISTRY.json"


def _load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def _write_json(path: Path, data: dict) -> None:
    ensure_dir(path.parent)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def _iter_character_files(character_files: Iterable[Path]) -> list[Path]:
    return [path for path in character_files if path.name not in CHARACTER_SKIP_NAMES]


def _iter_environment_files(environment_files: Iterable[Path]) -> list[Path]:
    return [path for path in environment_files if path.name not in ENVIRONMENT_SKIP_NAMES]


def _character_resolution(asset_id: str) -> tuple[str, str, str]:
    if asset_id in {"carter", "john_carter", "johncarter"}:
        return "john_carter", "canonical", "Resolved known Carter alias to john_carter."
    if any(label == asset_id or asset_id.startswith(f"{label}_") for label in GENERIC_CHARACTER_LABELS):
        return asset_id, "provisional", "Generic or role-based character remains provisional pending clarification."
    return asset_id, "canonical", "No competing canonical alias detected; kept extracted asset id."


def _environment_resolution(asset_id: str) -> tuple[str, str, str]:
    return asset_id, "canonical", "Environment currently kept under extracted canonical id."


def resolve_character_registry(project_slug: str, character_files: list[Path]) -> dict:
    path = character_registry_path(project_slug)
    registry = _load_json(path)

    for file in _iter_character_files(character_files):
        asset_id = file.stem
        canonical_id, status, resolution_reason = _character_resolution(asset_id)

        entry = registry.get(
            canonical_id,
            {
                "canonical_id": canonical_id,
                "status": status,
                "resolution_reason": resolution_reason,
                "aliases": [],
                "sources": [],
            },
        )

        entry["status"] = status
        entry["resolution_reason"] = resolution_reason

        if asset_id not in entry["aliases"] and asset_id != canonical_id:
            entry["aliases"].append(asset_id)

        rel_path = repo_relative(file)
        if rel_path not in entry["sources"]:
            entry["sources"].append(rel_path)

        registry[canonical_id] = entry

    _write_json(path, registry)
    return registry


def resolve_environment_registry(project_slug: str, env_files: list[Path]) -> dict:
    path = environment_registry_path(project_slug)
    registry = _load_json(path)

    for file in _iter_environment_files(env_files):
        asset_id = file.stem
        canonical_id, status, resolution_reason = _environment_resolution(asset_id)
        entry = registry.get(
            canonical_id,
            {
                "canonical_id": canonical_id,
                "status": status,
                "resolution_reason": resolution_reason,
                "aliases": [],
                "sources": [],
            },
        )

        entry["status"] = status
        entry["resolution_reason"] = resolution_reason

        rel_path = repo_relative(file)
        if rel_path not in entry["sources"]:
            entry["sources"].append(rel_path)

        registry[canonical_id] = entry

    _write_json(path, registry)
    return registry


def summarize_registry_status(registry: dict) -> tuple[list[str], list[str]]:
    canonical_ids: list[str] = []
    provisional_ids: list[str] = []
    for canonical_id, entry in sorted(registry.items()):
        if entry.get("status") == "provisional":
            provisional_ids.append(canonical_id)
        else:
            canonical_ids.append(canonical_id)
    return canonical_ids, provisional_ids


def run_phase_b1_resolution(project_slug: str) -> dict:
    project_dir = create_project(project_slug)

    char_dir = project_dir / "02_story_analysis" / "character_breakdowns"
    env_dir = project_dir / "02_story_analysis" / "environment_breakdowns"

    char_files = list(char_dir.glob("*.md"))
    env_files = list(env_dir.glob("*.md"))

    char_registry = resolve_character_registry(project_slug, char_files)
    env_registry = resolve_environment_registry(project_slug, env_files)
    canonical_character_ids, provisional_character_ids = summarize_registry_status(char_registry)
    canonical_environment_ids, provisional_environment_ids = summarize_registry_status(env_registry)

    return {
        "character_registry_path": repo_relative(character_registry_path(project_slug)),
        "environment_registry_path": repo_relative(environment_registry_path(project_slug)),
        "canonical_character_ids": canonical_character_ids,
        "provisional_character_ids": provisional_character_ids,
        "canonical_environment_ids": canonical_environment_ids,
        "provisional_environment_ids": provisional_environment_ids,
        "character_registry": char_registry,
        "environment_registry": env_registry,
    }
