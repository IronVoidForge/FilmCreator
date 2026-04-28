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


def _character_entity_kind(asset_id: str, source_markdown: str) -> tuple[str, str]:
    normalized = asset_id.lower()
    markdown = source_markdown.lower()
    if any(token in normalized for token in ["warriors", "soldiers", "guards", "children", "villagers", "crowd", "group"]):
        return "group", "Detected plural/group-like character asset."
    if any(label == normalized or normalized.startswith(f"{label}_") for label in GENERIC_CHARACTER_LABELS):
        return "provisional_role", "Generic role-based character remains provisional."
    if "group" in markdown or "2-3" in markdown or "crowd" in markdown:
        return "group", "Character markdown describes a group entity."
    return "individual", "Character appears to be a singular individual entity."


def _character_resolution(asset_id: str, source_markdown: str) -> tuple[str, str, str, str]:
    entity_kind, entity_reason = _character_entity_kind(asset_id, source_markdown)
    if entity_kind == "provisional_role":
        return asset_id, "provisional", entity_kind, "Generic or role-based character remains provisional pending clarification."
    return asset_id, "canonical", entity_kind, f"No competing canonical alias detected; kept extracted asset id. {entity_reason}"


def _environment_entity_kind(asset_id: str) -> str:
    normalized = asset_id.lower()
    if normalized == "deserted_city_buildings" or ("city" in normalized and "plaza" not in normalized):
        return "city"
    if "plaza" in normalized:
        return "plaza"
    if "building" in normalized:
        return "building"
    if any(token in normalized for token in ["window", "upper_floors", "interior", "deck", "open_ground"]):
        return "sub_location"
    if "warship" in normalized or "airship" in normalized:
        return "vehicle"
    if "hill" in normalized:
        return "landform"
    return "environment"


def _environment_parent(asset_id: str) -> str | None:
    normalized = asset_id.lower()
    if normalized == "city_plaza_open_ground":
        return "city_plaza"
    if normalized == "building_upper_floors_windows":
        return "city_plaza"
    if normalized == "disabled_airship_interior_deck":
        return "drifting_warship"
    if normalized == "city_plaza":
        return "deserted_city_buildings"
    return None


def _environment_resolution(asset_id: str) -> tuple[str, str, str, str, str | None]:
    canonical_id = asset_id
    status = "canonical"
    entity_kind = _environment_entity_kind(asset_id)
    parent_environment_id = _environment_parent(asset_id)
    if asset_id == "city_plaza_open_ground":
        return canonical_id, status, entity_kind, "Open-ground sub-location tied to city_plaza.", parent_environment_id
    if asset_id == "building_upper_floors_windows":
        return canonical_id, status, entity_kind, "Building sub-location attached to plaza/city hierarchy.", parent_environment_id
    if asset_id == "disabled_airship_interior_deck":
        return canonical_id, status, entity_kind, "Interior deck is a sub-location of the drifting warship.", parent_environment_id
    return canonical_id, status, entity_kind, "Environment currently kept under extracted canonical id.", parent_environment_id


def resolve_character_registry(
    project_slug: str,
    character_files: list[Path],
    *,
    load_existing: bool = True,
    write_output: bool = True,
) -> dict:
    path = character_registry_path(project_slug)
    registry = _load_json(path) if load_existing else {}

    for file in _iter_character_files(character_files):
        asset_id = file.stem
        markdown = file.read_text(encoding="utf-8")
        canonical_id, status, entity_kind, resolution_reason = _character_resolution(asset_id, markdown)
        entry = registry.get(
            canonical_id,
            {
                "canonical_id": canonical_id,
                "display_name": canonical_id,
                "status": status,
                "entity_kind": entity_kind,
                "resolution_reason": resolution_reason,
                "aliases": [],
                "sources": [],
                "parent_entity_id": None,
            },
        )
        entry.setdefault("aliases", [])
        entry.setdefault("sources", [])
        entry.setdefault("parent_entity_id", None)
        entry["status"] = status
        entry["entity_kind"] = entity_kind
        entry["resolution_reason"] = resolution_reason
        if asset_id not in entry["aliases"] and asset_id != canonical_id:
            entry["aliases"].append(asset_id)
        rel_path = repo_relative(file)
        if rel_path not in entry["sources"]:
            entry["sources"].append(rel_path)
        registry[canonical_id] = entry

    if write_output:
        _write_json(path, registry)
    return registry


def resolve_environment_registry(
    project_slug: str,
    env_files: list[Path],
    *,
    load_existing: bool = True,
    write_output: bool = True,
) -> dict:
    path = environment_registry_path(project_slug)
    registry = _load_json(path) if load_existing else {}

    for file in _iter_environment_files(env_files):
        asset_id = file.stem
        canonical_id, status, entity_kind, resolution_reason, parent_environment_id = _environment_resolution(asset_id)
        entry = registry.get(
            canonical_id,
            {
                "canonical_id": canonical_id,
                "display_name": canonical_id,
                "status": status,
                "entity_kind": entity_kind,
                "parent_environment_id": parent_environment_id,
                "children": [],
                "resolution_reason": resolution_reason,
                "aliases": [],
                "sources": [],
            },
        )
        entry.setdefault("aliases", [])
        entry.setdefault("sources", [])
        entry.setdefault("children", [])
        entry["status"] = status
        entry["entity_kind"] = entity_kind
        entry["parent_environment_id"] = parent_environment_id
        entry["resolution_reason"] = resolution_reason
        rel_path = repo_relative(file)
        if rel_path not in entry["sources"]:
            entry["sources"].append(rel_path)
        registry[canonical_id] = entry

        if parent_environment_id:
            parent = registry.get(
                parent_environment_id,
                {
                    "canonical_id": parent_environment_id,
                    "display_name": parent_environment_id,
                    "status": "canonical",
                    "entity_kind": _environment_entity_kind(parent_environment_id),
                    "parent_environment_id": _environment_parent(parent_environment_id),
                    "children": [],
                    "resolution_reason": "Synthesized parent environment from hierarchical child mapping.",
                    "aliases": [],
                    "sources": [],
                },
            )
            parent.setdefault("aliases", [])
            parent.setdefault("sources", [])
            parent.setdefault("children", [])
            if canonical_id not in parent["children"]:
                parent["children"].append(canonical_id)
            registry[parent_environment_id] = parent

    if write_output:
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


def summarize_character_registry(registry: dict) -> dict[str, list[str]]:
    canonical_individual_ids: list[str] = []
    canonical_group_ids: list[str] = []
    provisional_role_ids: list[str] = []
    for canonical_id, entry in sorted(registry.items()):
        kind = entry.get("entity_kind")
        status = entry.get("status")
        if status == "provisional":
            provisional_role_ids.append(canonical_id)
        elif kind == "group":
            canonical_group_ids.append(canonical_id)
        else:
            canonical_individual_ids.append(canonical_id)
    return {
        "canonical_individual_ids": canonical_individual_ids,
        "canonical_group_ids": canonical_group_ids,
        "provisional_role_ids": provisional_role_ids,
    }


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
    character_semantics = summarize_character_registry(char_registry)
    return {
        "character_registry_path": repo_relative(character_registry_path(project_slug)),
        "environment_registry_path": repo_relative(environment_registry_path(project_slug)),
        "canonical_character_ids": canonical_character_ids,
        "provisional_character_ids": provisional_character_ids,
        "canonical_environment_ids": canonical_environment_ids,
        "provisional_environment_ids": provisional_environment_ids,
        "canonical_individual_ids": character_semantics["canonical_individual_ids"],
        "canonical_group_ids": character_semantics["canonical_group_ids"],
        "provisional_role_ids": character_semantics["provisional_role_ids"],
        "character_registry": char_registry,
        "environment_registry": env_registry,
    }
