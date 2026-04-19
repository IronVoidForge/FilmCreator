from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from .common import ensure_dir, repo_relative
from .scaffold import create_project
from .story_authoring import StoryAnalysisSummary
from .world_registry import character_registry_path, environment_registry_path, summarize_character_registry


def global_world_dir(project_slug: str) -> Path:
    project_dir = create_project(project_slug)
    path = project_dir / "02_story_analysis" / "world" / "global"
    ensure_dir(path)
    return path


def world_snapshots_dir(project_slug: str) -> Path:
    project_dir = create_project(project_slug)
    path = project_dir / "02_story_analysis" / "world" / "snapshots"
    ensure_dir(path)
    return path


def global_character_directory_path(project_slug: str) -> Path:
    return global_world_dir(project_slug) / "CHARACTER_DIRECTORY.json"


def global_environment_directory_path(project_slug: str) -> Path:
    return global_world_dir(project_slug) / "ENVIRONMENT_DIRECTORY.json"


def global_character_registry_path(project_slug: str) -> Path:
    return global_world_dir(project_slug) / "CHARACTER_REGISTRY_GLOBAL.json"


def global_environment_registry_path(project_slug: str) -> Path:
    return global_world_dir(project_slug) / "ENVIRONMENT_REGISTRY_GLOBAL.json"


def world_sequence_state_path(project_slug: str) -> Path:
    return global_world_dir(project_slug) / "WORLD_SEQUENCE_STATE.json"


def world_failure_log_path(project_slug: str) -> Path:
    return global_world_dir(project_slug) / "WORLD_FAILURE_LOG.json"


def world_snapshot_path(project_slug: str, chapter_id: str) -> Path:
    return world_snapshots_dir(project_slug) / f"{chapter_id}_WORLD_SNAPSHOT.json"


def _load_json(path: Path, default: object) -> object:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def _write_json(path: Path, data: object) -> None:
    ensure_dir(path.parent)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def _load_chapter_registry(path: Path) -> dict:
    return _load_json(path, {}) if path.exists() else {}


def update_global_character_state(*, project_slug: str, analysis: StoryAnalysisSummary) -> tuple[str, str]:
    local_registry = _load_chapter_registry(character_registry_path(project_slug))
    global_registry_path = global_character_registry_path(project_slug)
    directory_path = global_character_directory_path(project_slug)
    global_registry = _load_json(global_registry_path, {})
    directory = _load_json(directory_path, {})

    for canonical_id, entry in sorted(local_registry.items()):
        global_entry = global_registry.get(
            canonical_id,
            {
                "canonical_id": canonical_id,
                "display_name": entry.get("display_name", canonical_id),
                "status": entry.get("status", "canonical"),
                "entity_kind": entry.get("entity_kind", "individual"),
                "aliases": [],
                "first_seen_chapter": analysis.chapter_id,
                "last_seen_chapter": analysis.chapter_id,
                "chapter_mentions": [],
                "sources": [],
                "open_questions": [],
                "description_layers": {
                    "innate": [],
                    "chapter_specific": {},
                },
            },
        )
        global_entry["status"] = entry.get("status", global_entry["status"])
        global_entry["entity_kind"] = entry.get("entity_kind", global_entry["entity_kind"])
        global_entry["display_name"] = entry.get("display_name", global_entry["display_name"])
        global_entry.setdefault("aliases", [])
        global_entry.setdefault("chapter_mentions", [])
        global_entry.setdefault("sources", [])
        global_entry.setdefault("open_questions", [])
        global_entry.setdefault("description_layers", {"innate": [], "chapter_specific": {}})
        global_entry.setdefault("first_seen_chapter", analysis.chapter_id)
        global_entry["last_seen_chapter"] = analysis.chapter_id
        if analysis.chapter_id not in global_entry["chapter_mentions"]:
            global_entry["chapter_mentions"].append(analysis.chapter_id)
        for alias in entry.get("aliases", []):
            if alias not in global_entry["aliases"]:
                global_entry["aliases"].append(alias)
        for source in entry.get("sources", []):
            if source not in global_entry["sources"]:
                global_entry["sources"].append(source)
        if analysis.chapter_id not in global_entry["description_layers"]["chapter_specific"]:
            global_entry["description_layers"]["chapter_specific"][analysis.chapter_id] = []
        global_registry[canonical_id] = global_entry

        directory[canonical_id] = {
            "canonical_id": canonical_id,
            "status": global_entry["status"],
            "entity_kind": global_entry["entity_kind"],
            "aliases": global_entry["aliases"],
            "first_seen_chapter": global_entry["first_seen_chapter"],
            "last_seen_chapter": global_entry["last_seen_chapter"],
        }

    _write_json(global_registry_path, global_registry)
    _write_json(directory_path, directory)
    return repo_relative(global_registry_path), repo_relative(directory_path)


def update_global_environment_state(*, project_slug: str, analysis: StoryAnalysisSummary) -> tuple[str, str]:
    local_registry = _load_chapter_registry(environment_registry_path(project_slug))
    global_registry_path = global_environment_registry_path(project_slug)
    directory_path = global_environment_directory_path(project_slug)
    global_registry = _load_json(global_registry_path, {})
    directory = _load_json(directory_path, {})

    for canonical_id, entry in sorted(local_registry.items()):
        global_entry = global_registry.get(
            canonical_id,
            {
                "canonical_id": canonical_id,
                "display_name": entry.get("display_name", canonical_id),
                "status": entry.get("status", "canonical"),
                "entity_kind": entry.get("entity_kind", "environment"),
                "aliases": [],
                "parent_environment_id": entry.get("parent_environment_id"),
                "children": [],
                "first_seen_chapter": analysis.chapter_id,
                "last_seen_chapter": analysis.chapter_id,
                "chapter_mentions": [],
                "sources": [],
                "state_notes": [],
                "description_layers": {
                    "innate": [],
                    "chapter_specific": {},
                },
            },
        )
        global_entry["status"] = entry.get("status", global_entry["status"])
        global_entry["entity_kind"] = entry.get("entity_kind", global_entry["entity_kind"])
        global_entry["display_name"] = entry.get("display_name", global_entry["display_name"])
        global_entry["parent_environment_id"] = entry.get("parent_environment_id", global_entry.get("parent_environment_id"))
        global_entry.setdefault("aliases", [])
        global_entry.setdefault("children", [])
        global_entry.setdefault("chapter_mentions", [])
        global_entry.setdefault("sources", [])
        global_entry.setdefault("state_notes", [])
        global_entry.setdefault("description_layers", {"innate": [], "chapter_specific": {}})
        global_entry.setdefault("first_seen_chapter", analysis.chapter_id)
        global_entry["last_seen_chapter"] = analysis.chapter_id
        if analysis.chapter_id not in global_entry["chapter_mentions"]:
            global_entry["chapter_mentions"].append(analysis.chapter_id)
        for alias in entry.get("aliases", []):
            if alias not in global_entry["aliases"]:
                global_entry["aliases"].append(alias)
        for source in entry.get("sources", []):
            if source not in global_entry["sources"]:
                global_entry["sources"].append(source)
        for child in entry.get("children", []):
            if child not in global_entry["children"]:
                global_entry["children"].append(child)
        if analysis.chapter_id not in global_entry["description_layers"]["chapter_specific"]:
            global_entry["description_layers"]["chapter_specific"][analysis.chapter_id] = []
        global_registry[canonical_id] = global_entry

        directory[canonical_id] = {
            "canonical_id": canonical_id,
            "status": global_entry["status"],
            "entity_kind": global_entry["entity_kind"],
            "aliases": global_entry["aliases"],
            "parent_environment_id": global_entry.get("parent_environment_id"),
            "first_seen_chapter": global_entry["first_seen_chapter"],
            "last_seen_chapter": global_entry["last_seen_chapter"],
        }

    _write_json(global_registry_path, global_registry)
    _write_json(directory_path, directory)
    return repo_relative(global_registry_path), repo_relative(directory_path)


def write_chapter_world_snapshot(
    *,
    project_slug: str,
    analysis: StoryAnalysisSummary,
    global_character_registry_relpath: str,
    global_environment_registry_relpath: str,
    global_character_directory_relpath: str,
    global_environment_directory_relpath: str,
) -> str:
    project_dir = create_project(project_slug)
    local_character_registry = _load_chapter_registry(character_registry_path(project_slug))
    character_semantics = summarize_character_registry(local_character_registry)
    snapshot = {
        "chapter_id": analysis.chapter_id,
        "chapter_path": analysis.chapter_path,
        "known_characters": character_semantics["canonical_individual_ids"],
        "known_groups": character_semantics["canonical_group_ids"],
        "provisional_roles": character_semantics["provisional_role_ids"],
        "known_environments": analysis.canonical_environment_ids,
        "global_character_directory_path": global_character_directory_relpath,
        "global_environment_directory_path": global_environment_directory_relpath,
        "global_character_registry_path": global_character_registry_relpath,
        "global_environment_registry_path": global_environment_registry_relpath,
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
    }
    path = world_snapshot_path(project_slug, analysis.chapter_id)
    _write_json(path, snapshot)
    return repo_relative(path)


def append_world_failure(
    *,
    project_slug: str,
    chapter_id: str,
    chapter_path: str,
    stage: str,
    error: str,
    failure_artifact_path: str | None,
) -> str:
    path = world_failure_log_path(project_slug)
    failures = _load_json(path, [])
    failures.append(
        {
            "chapter_id": chapter_id,
            "chapter_path": chapter_path,
            "stage": stage,
            "error": error,
            "failure_artifact_path": failure_artifact_path or "",
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        }
    )
    _write_json(path, failures)
    return repo_relative(path)


def update_world_sequence_state(*, project_slug: str, succeeded_chapter_ids: list[str], failed_chapter_ids: list[str]) -> str:
    path = world_sequence_state_path(project_slug)
    payload = {
        "processed_chapters": succeeded_chapter_ids,
        "failed_chapters": failed_chapter_ids,
        "updated_at_utc": datetime.now(timezone.utc).isoformat(),
    }
    _write_json(path, payload)
    return repo_relative(path)
