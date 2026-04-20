from __future__ import annotations

import re
from datetime import datetime, timezone
from pathlib import Path

from ...core.json_io import read_json, write_json
from ...core.paths import ensure_dir
from ... import scaffold as scaffold_module


_GENERIC_CHARACTER_LABELS = {
    "narrator",
    "the_narrator",
    "protagonist",
    "companion",
    "unknown_companion",
    "friend_body",
    "prisoner",
    "human_female_prisoner",
    "captive",
    "guard",
    "chieftain",
    "martian",
    "martian_leader",
    "young_warrior",
    "watch_dog",
    "watch_thing",
    "warrior",
    "woman",
    "man",
    "girl",
    "boy",
}

_CHAPTER_ID_RE = re.compile(r"^CH(\d{3})$", re.IGNORECASE)


def global_world_dir(project_slug: str) -> Path:
    project_dir = scaffold_module.create_project(project_slug)
    path = project_dir / "02_story_analysis" / "world" / "global"
    ensure_dir(path)
    return path


def world_snapshots_dir(project_slug: str) -> Path:
    project_dir = scaffold_module.create_project(project_slug)
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


def chapter_local_character_registry_path(*, project_slug: str, chapter_id: str) -> Path:
    project_dir = scaffold_module.create_project(project_slug)
    return project_dir / "02_story_analysis" / "world" / "local" / f"{chapter_id}_CHARACTER_REGISTRY.json"


def chapter_local_environment_registry_path(*, project_slug: str, chapter_id: str) -> Path:
    project_dir = scaffold_module.create_project(project_slug)
    return project_dir / "02_story_analysis" / "world" / "local" / f"{chapter_id}_ENVIRONMENT_REGISTRY.json"


def repo_root_from_project_dir(project_dir: Path) -> Path:
    return project_dir.parent.parent


def world_sequence_state_path(project_slug: str) -> Path:
    return global_world_dir(project_slug) / "WORLD_SEQUENCE_STATE.json"


def world_failure_log_path(project_slug: str) -> Path:
    return global_world_dir(project_slug) / "WORLD_FAILURE_LOG.json"


def world_snapshot_path(project_slug: str, chapter_id: str) -> Path:
    return world_snapshots_dir(project_slug) / f"{chapter_id}_WORLD_SNAPSHOT.json"


def load_world_snapshot(*, project_slug: str, chapter_id: str) -> dict:
    return load_json(world_snapshot_path(project_slug, chapter_id), {})


def load_json(path: Path, default: object) -> object:
    if not path.exists():
        return default
    return read_json(path)


def update_json(path: Path, data: object) -> None:
    write_json(path, data)


def load_chapter_registry(path: Path) -> dict:
    return load_json(path, {}) if path.exists() else {}


def normalize_alias_token(value: str) -> str:
    normalized = re.sub(r"[^a-z0-9]+", "_", value.strip().lower()).strip("_")
    normalized = re.sub(r"^the_", "", normalized)
    return normalized


def is_generic_character_label(value: str) -> bool:
    normalized = normalize_alias_token(value)
    return normalized in _GENERIC_CHARACTER_LABELS or any(
        token in normalized.split("_")
        for token in {"narrator", "prisoner", "captive", "guard", "companion", "warrior", "chieftain", "martian"}
    )


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def chapter_sort_key(chapter_id: str) -> int:
    match = _CHAPTER_ID_RE.fullmatch(chapter_id.strip())
    if not match:
        raise ValueError(f"Invalid chapter id: {chapter_id}")
    return int(match.group(1))


def chapter_lte(left: str, right: str) -> bool:
    return chapter_sort_key(left) <= chapter_sort_key(right)


def empty_character_entry(*, canonical_id: str, entry: dict, chapter_id: str) -> dict:
    return {
        "canonical_id": canonical_id,
        "display_name": entry.get("display_name", canonical_id),
        "status": entry.get("status", "canonical"),
        "entity_kind": entry.get("entity_kind", "individual"),
        "aliases": [],
        "alias_history": [],
        "first_seen_chapter": chapter_id,
        "last_seen_chapter": chapter_id,
        "chapter_mentions": [],
        "sources": [],
        "source_history": [],
        "open_questions": [],
        "resolution_reason": entry.get("resolution_reason", ""),
        "resolved_to": None,
        "resolution_history": [],
        "description_layers": {
            "initial_extracted": [],
            "stable_canonical": [],
            "chapter_specific": {},
        },
    }


def empty_environment_entry(*, canonical_id: str, entry: dict, chapter_id: str) -> dict:
    return {
        "canonical_id": canonical_id,
        "display_name": entry.get("display_name", canonical_id),
        "status": entry.get("status", "canonical"),
        "entity_kind": entry.get("entity_kind", "environment"),
        "aliases": [],
        "alias_history": [],
        "parent_environment_id": entry.get("parent_environment_id"),
        "children": [],
        "first_seen_chapter": chapter_id,
        "last_seen_chapter": chapter_id,
        "chapter_mentions": [],
        "sources": [],
        "source_history": [],
        "state_notes": [],
        "description_layers": {
            "initial_extracted": [],
            "stable_canonical": [],
            "chapter_specific": {},
        },
    }


def ensure_character_entry_defaults(entry: dict, *, chapter_id: str) -> dict:
    entry.setdefault("display_name", entry.get("canonical_id", ""))
    entry.setdefault("status", "canonical")
    entry.setdefault("entity_kind", "individual")
    entry.setdefault("aliases", [])
    entry.setdefault("alias_history", [])
    entry.setdefault("first_seen_chapter", chapter_id)
    entry.setdefault("last_seen_chapter", chapter_id)
    entry.setdefault("chapter_mentions", [])
    entry.setdefault("sources", [])
    entry.setdefault("source_history", [])
    entry.setdefault("open_questions", [])
    entry.setdefault("resolution_reason", "")
    entry.setdefault("resolved_to", None)
    entry.setdefault("resolution_history", [])
    entry.setdefault(
        "description_layers",
        {
            "initial_extracted": [],
            "stable_canonical": [],
            "chapter_specific": {},
        },
    )
    entry["description_layers"].setdefault("initial_extracted", [])
    entry["description_layers"].setdefault("stable_canonical", [])
    entry["description_layers"].setdefault("chapter_specific", {})
    return entry


def ensure_environment_entry_defaults(entry: dict, *, chapter_id: str) -> dict:
    entry.setdefault("display_name", entry.get("canonical_id", ""))
    entry.setdefault("status", "canonical")
    entry.setdefault("entity_kind", "environment")
    entry.setdefault("aliases", [])
    entry.setdefault("alias_history", [])
    entry.setdefault("parent_environment_id", None)
    entry.setdefault("children", [])
    entry.setdefault("first_seen_chapter", chapter_id)
    entry.setdefault("last_seen_chapter", chapter_id)
    entry.setdefault("chapter_mentions", [])
    entry.setdefault("sources", [])
    entry.setdefault("source_history", [])
    entry.setdefault("state_notes", [])
    entry.setdefault(
        "description_layers",
        {
            "initial_extracted": [],
            "stable_canonical": [],
            "chapter_specific": {},
        },
    )
    entry["description_layers"].setdefault("initial_extracted", [])
    entry["description_layers"].setdefault("stable_canonical", [])
    entry["description_layers"].setdefault("chapter_specific", {})
    return entry


def append_alias_history(entry: dict, *, alias: str, chapter_id: str, source: str) -> None:
    entry.setdefault("alias_history", []).append(
        {
            "chapter_id": chapter_id,
            "alias": alias,
            "source": source,
            "timestamp_utc": utc_now_iso(),
        }
    )


def append_source_history(entry: dict, *, chapter_id: str, source_path: str, record_kind: str) -> None:
    entry.setdefault("source_history", []).append(
        {
            "chapter_id": chapter_id,
            "source_path": source_path,
            "record_kind": record_kind,
            "timestamp_utc": utc_now_iso(),
        }
    )


def append_description_layer(entry: dict, *, chapter_id: str, summary: str, source_path: str) -> None:
    description_layers = entry.setdefault(
        "description_layers",
        {
            "initial_extracted": [],
            "stable_canonical": [],
            "chapter_specific": {},
        },
    )
    description_layers.setdefault("chapter_specific", {}).setdefault(chapter_id, []).append(
        {
            "summary": summary,
            "source_path": source_path,
            "timestamp_utc": utc_now_iso(),
        }
    )


def append_resolution_history(
    entry: dict,
    *,
    chapter_id: str,
    action: str,
    reason: str,
    target: str | None = None,
) -> None:
    item = {
        "chapter_id": chapter_id,
        "action": action,
        "reason": reason,
        "timestamp_utc": utc_now_iso(),
    }
    if target:
        item["target"] = target
    entry.setdefault("resolution_history", []).append(item)
