from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

from .core.json_io import read_json, write_json
from .core.paths import ensure_dir, repo_relative
from .scaffold import create_project
from .story_authoring import StoryAnalysisSummary


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


def chapter_local_character_registry_path(*, project_slug: str, chapter_id: str) -> Path:
    project_dir = create_project(project_slug)
    return project_dir / "02_story_analysis" / "world" / "local" / f"{chapter_id}_CHARACTER_REGISTRY.json"


def chapter_local_environment_registry_path(*, project_slug: str, chapter_id: str) -> Path:
    project_dir = create_project(project_slug)
    return project_dir / "02_story_analysis" / "world" / "local" / f"{chapter_id}_ENVIRONMENT_REGISTRY.json"


def _repo_root_from_project_dir(project_dir: Path) -> Path:
    # project_dir is .../<repo_root>/projects/<project_slug>
    return project_dir.parent.parent


def world_sequence_state_path(project_slug: str) -> Path:
    return global_world_dir(project_slug) / "WORLD_SEQUENCE_STATE.json"


def world_failure_log_path(project_slug: str) -> Path:
    return global_world_dir(project_slug) / "WORLD_FAILURE_LOG.json"


def world_snapshot_path(project_slug: str, chapter_id: str) -> Path:
    return world_snapshots_dir(project_slug) / f"{chapter_id}_WORLD_SNAPSHOT.json"


def load_world_snapshot(*, project_slug: str, chapter_id: str) -> dict:
    return _load_json(world_snapshot_path(project_slug, chapter_id), {})


def _load_json(path: Path, default: object) -> object:
    if not path.exists():
        return default
    return read_json(path)


def _write_json(path: Path, data: object) -> None:
    write_json(path, data)


def _load_chapter_registry(path: Path) -> dict:
    return _load_json(path, {}) if path.exists() else {}


def _assert_registry_is_chapter_local(*, registry: dict, chapter_id: str, entity_type: str) -> None:
    expected_chapter_fragment = f"/chapters/{chapter_id}/"
    expected_prefix_fragment = f"/{chapter_id}_"
    for entry_id, entry in registry.items():
        for source in entry.get("sources", []):
            normalized = str(source).replace("\\", "/")
            if expected_chapter_fragment in normalized or expected_prefix_fragment in normalized:
                continue
            raise ValueError(
                f"{entity_type} registry entry '{entry_id}' contains non-local source '{source}' for chapter {chapter_id}."
            )


def _normalize_alias_token(value: str) -> str:
    normalized = re.sub(r"[^a-z0-9]+", "_", value.strip().lower()).strip("_")
    normalized = re.sub(r"^the_", "", normalized)
    return normalized


def _is_generic_character_label(value: str) -> bool:
    normalized = _normalize_alias_token(value)
    return normalized in _GENERIC_CHARACTER_LABELS or any(
        token in normalized.split("_")
        for token in {"narrator", "prisoner", "captive", "guard", "companion", "warrior", "chieftain", "martian"}
    )


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _chapter_sort_key(chapter_id: str) -> int:
    match = _CHAPTER_ID_RE.fullmatch(chapter_id.strip())
    if not match:
        raise ValueError(f"Invalid chapter id: {chapter_id}")
    return int(match.group(1))


def _chapter_lte(left: str, right: str) -> bool:
    return _chapter_sort_key(left) <= _chapter_sort_key(right)


def _empty_character_entry(*, canonical_id: str, entry: dict, chapter_id: str) -> dict:
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


def _empty_environment_entry(*, canonical_id: str, entry: dict, chapter_id: str) -> dict:
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


def _ensure_character_entry_defaults(entry: dict, *, chapter_id: str) -> dict:
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


def _ensure_environment_entry_defaults(entry: dict, *, chapter_id: str) -> dict:
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


def _append_alias_history(entry: dict, *, alias: str, chapter_id: str, source: str) -> None:
    normalized_alias = _normalize_alias_token(alias)
    if not normalized_alias:
        return
    if normalized_alias not in entry["aliases"]:
        entry["aliases"].append(normalized_alias)
    history_item = {
        "chapter_id": chapter_id,
        "alias": normalized_alias,
        "source": source,
    }
    if history_item not in entry["alias_history"]:
        entry["alias_history"].append(history_item)


def _append_source_history(entry: dict, *, chapter_id: str, source_path: str, record_kind: str) -> None:
    if source_path not in entry["sources"]:
        entry["sources"].append(source_path)
    history_item = {
        "chapter_id": chapter_id,
        "source_path": source_path,
        "record_kind": record_kind,
    }
    if history_item not in entry["source_history"]:
        entry["source_history"].append(history_item)


def _append_description_layer(entry: dict, *, chapter_id: str, summary: str, source_path: str) -> None:
    if not summary:
        return
    initial_item = {
        "chapter_id": chapter_id,
        "summary": summary,
        "source": source_path,
    }
    if initial_item not in entry["description_layers"]["initial_extracted"]:
        entry["description_layers"]["initial_extracted"].append(initial_item)
    chapter_bucket = entry["description_layers"]["chapter_specific"].setdefault(chapter_id, [])
    if summary not in chapter_bucket:
        chapter_bucket.append(summary)
    if summary not in entry["description_layers"]["stable_canonical"] and not _is_generic_character_label(entry["canonical_id"]):
        entry["description_layers"]["stable_canonical"].append(summary)


def _append_resolution_history(entry: dict, *, chapter_id: str, action: str, reason: str, target: str | None = None) -> None:
    item = {
        "chapter_id": chapter_id,
        "action": action,
        "reason": reason,
        "timestamp_utc": _utc_now_iso(),
    }
    if target:
        item["target"] = target
    entry["resolution_history"].append(item)


def _entry_match_tokens(entry: dict) -> set[str]:
    tokens = {
        _normalize_alias_token(entry.get("canonical_id", "")),
        _normalize_alias_token(entry.get("display_name", "")),
    }
    for alias in entry.get("aliases", []):
        tokens.add(_normalize_alias_token(alias))
    return {token for token in tokens if token}


def _find_character_merge_target(global_registry: dict[str, dict], local_entry: dict) -> str | None:
    local_id = local_entry.get("canonical_id", "")
    local_tokens = _entry_match_tokens(local_entry)
    local_generic = _is_generic_character_label(local_id)

    for candidate_id, candidate_entry in global_registry.items():
        if candidate_id == local_id:
            return candidate_id
        candidate_tokens = _entry_match_tokens(candidate_entry)
        if local_tokens & candidate_tokens:
            return candidate_id

    if local_generic:
        normalized_local = _normalize_alias_token(local_id)
        for candidate_id, candidate_entry in global_registry.items():
            if _normalize_alias_token(candidate_id) == normalized_local:
                return candidate_id
            if _is_generic_character_label(candidate_id) and _normalize_alias_token(candidate_entry.get("display_name", "")) == normalized_local:
                return candidate_id

    return None


def _resolve_provisional_into(
    global_registry: dict[str, dict],
    *,
    provisional_id: str,
    canonical_id: str,
    chapter_id: str,
    reason: str,
) -> None:
    provisional_entry = global_registry.get(provisional_id)
    if provisional_entry is None:
        return
    provisional_entry = _ensure_character_entry_defaults(provisional_entry, chapter_id=chapter_id)
    provisional_entry["status"] = "resolved_into"
    provisional_entry["resolved_to"] = canonical_id
    _append_resolution_history(
        provisional_entry,
        chapter_id=chapter_id,
        action="resolved_into",
        reason=reason,
        target=canonical_id,
    )
    global_registry[provisional_id] = provisional_entry


def _chapter_character_resolution_events(global_registry: dict[str, dict], *, chapter_id: str) -> list[dict[str, str]]:
    events: list[dict[str, str]] = []
    for character_id, entry in sorted(global_registry.items()):
        for item in entry.get("resolution_history", []):
            if item.get("chapter_id") == chapter_id and item.get("action") == "resolved_into":
                events.append(
                    {
                        "from": character_id,
                        "to": item.get("target", entry.get("resolved_to", "")),
                        "reason": item.get("reason", ""),
                    }
                )
    return events


def _filter_history_by_chapter(items: list[dict], *, chapter_cutoff: str) -> list[dict]:
    filtered: list[dict] = []
    for item in items:
        item_chapter = str(item.get("chapter_id", "")).strip()
        if item_chapter and _chapter_lte(item_chapter, chapter_cutoff):
            filtered.append(item)
    return filtered


def _character_entry_visible_by_chapter(entry: dict, *, chapter_cutoff: str) -> bool:
    first_seen = str(entry.get("first_seen_chapter", "")).strip()
    return bool(first_seen) and _chapter_lte(first_seen, chapter_cutoff)


def _environment_entry_visible_by_chapter(entry: dict, *, chapter_cutoff: str) -> bool:
    first_seen = str(entry.get("first_seen_chapter", "")).strip()
    return bool(first_seen) and _chapter_lte(first_seen, chapter_cutoff)


def _project_character_snapshot_entry(entry: dict, *, chapter_cutoff: str) -> dict:
    description_layers = entry.get("description_layers", {})
    return {
        "canonical_id": entry.get("canonical_id"),
        "display_name": entry.get("display_name"),
        "status": entry.get("status"),
        "entity_kind": entry.get("entity_kind"),
        "aliases": [
            item.get("alias")
            for item in _filter_history_by_chapter(entry.get("alias_history", []), chapter_cutoff=chapter_cutoff)
            if item.get("alias")
        ],
        "first_seen_chapter": entry.get("first_seen_chapter"),
        "last_seen_chapter": entry.get("last_seen_chapter"),
        "chapter_mentions": [
            chapter_id
            for chapter_id in entry.get("chapter_mentions", [])
            if _chapter_lte(chapter_id, chapter_cutoff)
        ],
        "resolved_to": entry.get("resolved_to"),
        "resolution_history": _filter_history_by_chapter(entry.get("resolution_history", []), chapter_cutoff=chapter_cutoff),
        "source_history": _filter_history_by_chapter(entry.get("source_history", []), chapter_cutoff=chapter_cutoff),
        "description_layers": {
            "initial_extracted": [
                item
                for item in description_layers.get("initial_extracted", [])
                if str(item.get("chapter_id", "")).strip() and _chapter_lte(str(item.get("chapter_id", "")).strip(), chapter_cutoff)
            ],
            "stable_canonical": description_layers.get("stable_canonical", []),
            "chapter_specific": {
                chapter_id: values
                for chapter_id, values in description_layers.get("chapter_specific", {}).items()
                if _chapter_lte(chapter_id, chapter_cutoff)
            },
        },
    }


def _project_environment_snapshot_entry(entry: dict, *, chapter_cutoff: str) -> dict:
    description_layers = entry.get("description_layers", {})
    return {
        "canonical_id": entry.get("canonical_id"),
        "display_name": entry.get("display_name"),
        "status": entry.get("status"),
        "entity_kind": entry.get("entity_kind"),
        "aliases": [
            item.get("alias")
            for item in _filter_history_by_chapter(entry.get("alias_history", []), chapter_cutoff=chapter_cutoff)
            if item.get("alias")
        ],
        "parent_environment_id": entry.get("parent_environment_id"),
        "children": entry.get("children", []),
        "first_seen_chapter": entry.get("first_seen_chapter"),
        "last_seen_chapter": entry.get("last_seen_chapter"),
        "chapter_mentions": [
            chapter_id
            for chapter_id in entry.get("chapter_mentions", [])
            if _chapter_lte(chapter_id, chapter_cutoff)
        ],
        "source_history": _filter_history_by_chapter(entry.get("source_history", []), chapter_cutoff=chapter_cutoff),
        "description_layers": {
            "initial_extracted": [
                item
                for item in description_layers.get("initial_extracted", [])
                if str(item.get("chapter_id", "")).strip() and _chapter_lte(str(item.get("chapter_id", "")).strip(), chapter_cutoff)
            ],
            "stable_canonical": description_layers.get("stable_canonical", []),
            "chapter_specific": {
                chapter_id: values
                for chapter_id, values in description_layers.get("chapter_specific", {}).items()
                if _chapter_lte(chapter_id, chapter_cutoff)
            },
        },
    }


def validate_snapshot_provenance(snapshot: dict, *, chapter_id: str) -> None:
    for entry in snapshot.get("character_entries", []):
        first_seen = str(entry.get("first_seen_chapter", "")).strip()
        if first_seen and not _chapter_lte(first_seen, chapter_id):
            raise ValueError(
                f"Snapshot {chapter_id} includes future character '{entry.get('canonical_id')}' first seen in {first_seen}."
            )
    for entry in snapshot.get("environment_entries", []):
        first_seen = str(entry.get("first_seen_chapter", "")).strip()
        if first_seen and not _chapter_lte(first_seen, chapter_id):
            raise ValueError(
                f"Snapshot {chapter_id} includes future environment '{entry.get('canonical_id')}' first seen in {first_seen}."
            )


def update_global_character_state(*, project_slug: str, analysis: StoryAnalysisSummary) -> tuple[str, str]:
    local_registry = _load_chapter_registry(
        chapter_local_character_registry_path(
            project_slug=project_slug,
            chapter_id=analysis.chapter_id,
        )
    )
    _assert_registry_is_chapter_local(registry=local_registry, chapter_id=analysis.chapter_id, entity_type="Character")
    global_registry_path = global_character_registry_path(project_slug)
    directory_path = global_character_directory_path(project_slug)
    global_registry = _load_json(global_registry_path, {})
    directory = _load_json(directory_path, {})

    for local_id, entry in sorted(local_registry.items()):
        target_id = _find_character_merge_target(global_registry, entry) or local_id

        if target_id not in global_registry:
            global_registry[target_id] = _empty_character_entry(
                canonical_id=target_id,
                entry=entry,
                chapter_id=analysis.chapter_id,
            )
            _append_resolution_history(
                global_registry[target_id],
                chapter_id=analysis.chapter_id,
                action="created_as_provisional" if entry.get("status") == "provisional" else "created_as_canonical",
                reason=entry.get("resolution_reason", "Initial global registry creation from chapter-local registry."),
            )

        global_entry = _ensure_character_entry_defaults(global_registry[target_id], chapter_id=analysis.chapter_id)
        global_entry["display_name"] = entry.get("display_name", global_entry["display_name"])
        if global_entry.get("status") != "resolved_into":
            local_status = entry.get("status", global_entry["status"])
            if local_status == "provisional" or _is_generic_character_label(local_id):
                global_entry["status"] = "provisional" if local_status == "provisional" else global_entry["status"]
            else:
                global_entry["status"] = local_status
        global_entry["entity_kind"] = entry.get("entity_kind", global_entry["entity_kind"])
        global_entry["resolution_reason"] = entry.get("resolution_reason", global_entry.get("resolution_reason", ""))
        global_entry["last_seen_chapter"] = analysis.chapter_id
        if analysis.chapter_id not in global_entry["chapter_mentions"]:
            global_entry["chapter_mentions"].append(analysis.chapter_id)

        _append_alias_history(
            global_entry,
            alias=local_id,
            chapter_id=analysis.chapter_id,
            source=entry.get("sources", [analysis.chapter_path])[0] if entry.get("sources") else analysis.chapter_path,
        )
        for alias in entry.get("aliases", []):
            _append_alias_history(
                global_entry,
                alias=alias,
                chapter_id=analysis.chapter_id,
                source=entry.get("sources", [analysis.chapter_path])[0] if entry.get("sources") else analysis.chapter_path,
            )
        for source in entry.get("sources", []):
            _append_source_history(
                global_entry,
                chapter_id=analysis.chapter_id,
                source_path=source,
                record_kind="chapter_local_character_breakdown",
            )
            _append_description_layer(
                global_entry,
                chapter_id=analysis.chapter_id,
                summary=entry.get("resolution_reason", ""),
                source_path=source,
            )

        global_registry[target_id] = global_entry

        if target_id != local_id:
            if local_id not in global_registry:
                global_registry[local_id] = _empty_character_entry(
                    canonical_id=local_id,
                    entry=entry,
                    chapter_id=analysis.chapter_id,
                )
            local_history_entry = _ensure_character_entry_defaults(global_registry[local_id], chapter_id=analysis.chapter_id)
            local_history_entry["display_name"] = entry.get("display_name", local_history_entry["display_name"])
            local_history_entry["entity_kind"] = entry.get("entity_kind", local_history_entry["entity_kind"])
            local_history_entry["resolution_reason"] = entry.get("resolution_reason", local_history_entry.get("resolution_reason", ""))
            local_history_entry["last_seen_chapter"] = analysis.chapter_id
            if analysis.chapter_id not in local_history_entry["chapter_mentions"]:
                local_history_entry["chapter_mentions"].append(analysis.chapter_id)
            for source in entry.get("sources", []):
                _append_source_history(
                    local_history_entry,
                    chapter_id=analysis.chapter_id,
                    source_path=source,
                    record_kind="chapter_local_character_breakdown",
                )
                _append_description_layer(
                    local_history_entry,
                    chapter_id=analysis.chapter_id,
                    summary=entry.get("resolution_reason", ""),
                    source_path=source,
                )
            _append_alias_history(
                local_history_entry,
                alias=local_id,
                chapter_id=analysis.chapter_id,
                source=entry.get("sources", [analysis.chapter_path])[0] if entry.get("sources") else analysis.chapter_path,
            )
            for alias in entry.get("aliases", []):
                _append_alias_history(
                    local_history_entry,
                    alias=alias,
                    chapter_id=analysis.chapter_id,
                    source=entry.get("sources", [analysis.chapter_path])[0] if entry.get("sources") else analysis.chapter_path,
                )
            global_registry[local_id] = local_history_entry
            _resolve_provisional_into(
                global_registry,
                provisional_id=local_id,
                canonical_id=target_id,
                chapter_id=analysis.chapter_id,
                reason=(
                    f"Resolved chapter-local character '{local_id}' into existing global character '{target_id}' via conservative alias/name matching."
                ),
            )

    for canonical_id, global_entry in sorted(global_registry.items()):
        directory[canonical_id] = {
            "canonical_id": canonical_id,
            "status": global_entry.get("status", "canonical"),
            "entity_kind": global_entry.get("entity_kind", "individual"),
            "aliases": global_entry.get("aliases", []),
            "first_seen_chapter": global_entry.get("first_seen_chapter"),
            "last_seen_chapter": global_entry.get("last_seen_chapter"),
            "resolved_to": global_entry.get("resolved_to"),
        }

    _write_json(global_registry_path, global_registry)
    _write_json(directory_path, directory)
    return repo_relative(global_registry_path), repo_relative(directory_path)


def update_global_environment_state(*, project_slug: str, analysis: StoryAnalysisSummary) -> tuple[str, str]:
    local_registry = _load_chapter_registry(
        chapter_local_environment_registry_path(
            project_slug=project_slug,
            chapter_id=analysis.chapter_id,
        )
    )
    _assert_registry_is_chapter_local(registry=local_registry, chapter_id=analysis.chapter_id, entity_type="Environment")
    global_registry_path = global_environment_registry_path(project_slug)
    directory_path = global_environment_directory_path(project_slug)
    global_registry = _load_json(global_registry_path, {})
    directory = _load_json(directory_path, {})

    for canonical_id, entry in sorted(local_registry.items()):
        global_entry = global_registry.get(
            canonical_id,
            _empty_environment_entry(canonical_id=canonical_id, entry=entry, chapter_id=analysis.chapter_id),
        )
        global_entry = _ensure_environment_entry_defaults(global_entry, chapter_id=analysis.chapter_id)
        global_entry["status"] = entry.get("status", global_entry["status"])
        global_entry["entity_kind"] = entry.get("entity_kind", global_entry["entity_kind"])
        global_entry["display_name"] = entry.get("display_name", global_entry["display_name"])
        global_entry["parent_environment_id"] = entry.get("parent_environment_id", global_entry.get("parent_environment_id"))
        global_entry["last_seen_chapter"] = analysis.chapter_id
        if analysis.chapter_id not in global_entry["chapter_mentions"]:
            global_entry["chapter_mentions"].append(analysis.chapter_id)
        for alias in entry.get("aliases", []):
            normalized_alias = _normalize_alias_token(alias)
            if normalized_alias and normalized_alias not in global_entry["aliases"]:
                global_entry["aliases"].append(normalized_alias)
                global_entry["alias_history"].append(
                    {
                        "chapter_id": analysis.chapter_id,
                        "alias": normalized_alias,
                        "source": entry.get("sources", [analysis.chapter_path])[0] if entry.get("sources") else analysis.chapter_path,
                    }
                )
        for source in entry.get("sources", []):
            _append_source_history(
                global_entry,
                chapter_id=analysis.chapter_id,
                source_path=source,
                record_kind="chapter_local_environment_breakdown",
            )
            _append_description_layer(
                global_entry,
                chapter_id=analysis.chapter_id,
                summary=entry.get("resolution_reason", ""),
                source_path=source,
            )
        for child in entry.get("children", []):
            if child not in global_entry["children"]:
                global_entry["children"].append(child)
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
    repo_root = _repo_root_from_project_dir(project_dir)

    global_character_registry_path = repo_root / global_character_registry_relpath
    global_environment_registry_path = repo_root / global_environment_registry_relpath

    global_character_registry = _load_json(global_character_registry_path, {})
    global_environment_registry = _load_json(global_environment_registry_path, {})

    print(f"[authoring] Snapshot build for {analysis.chapter_id}:")
    print(f"[authoring]   repo_root: {repo_root}")
    print(f"[authoring]   global_character_registry_path: {global_character_registry_path}")
    print(f"[authoring]   global_environment_registry_path: {global_environment_registry_path}")
    print(f"[authoring]   global_character_registry_exists: {global_character_registry_path.exists()}")
    print(f"[authoring]   global_environment_registry_exists: {global_environment_registry_path.exists()}")
    print(f"[authoring]   loaded_global_character_entries: {len(global_character_registry)}")
    print(f"[authoring]   loaded_global_environment_entries: {len(global_environment_registry)}")

    visible_characters = {
        canonical_id: entry
        for canonical_id, entry in global_character_registry.items()
        if _character_entry_visible_by_chapter(entry, chapter_cutoff=analysis.chapter_id)
    }
    visible_environments = {
        canonical_id: entry
        for canonical_id, entry in global_environment_registry.items()
        if _environment_entry_visible_by_chapter(entry, chapter_cutoff=analysis.chapter_id)
    }
    print(f"[authoring]   visible_character_entries_for_{analysis.chapter_id}: {len(visible_characters)}")
    print(f"[authoring]   visible_environment_entries_for_{analysis.chapter_id}: {len(visible_environments)}")

    character_entries = [
        _project_character_snapshot_entry(entry, chapter_cutoff=analysis.chapter_id)
        for _, entry in sorted(visible_characters.items())
    ]
    environment_entries = [
        _project_environment_snapshot_entry(entry, chapter_cutoff=analysis.chapter_id)
        for _, entry in sorted(visible_environments.items())
    ]
    print(f"[authoring]   projected_character_entries_for_{analysis.chapter_id}: {len(character_entries)}")
    print(f"[authoring]   projected_environment_entries_for_{analysis.chapter_id}: {len(environment_entries)}")
    if not character_entries and global_character_registry:
        print(f"[authoring]   WARNING: Snapshot {analysis.chapter_id} projected zero character entries.")
        for canonical_id, entry in sorted(global_character_registry.items()):
            print(
                "[authoring]     character candidate:",
                canonical_id,
                "first_seen=",
                entry.get("first_seen_chapter"),
                "last_seen=",
                entry.get("last_seen_chapter"),
                "chapter_mentions=",
                entry.get("chapter_mentions", []),
            )
    if not environment_entries and global_environment_registry:
        print(f"[authoring]   WARNING: Snapshot {analysis.chapter_id} projected zero environment entries.")
        for canonical_id, entry in sorted(global_environment_registry.items()):
            print(
                "[authoring]     environment candidate:",
                canonical_id,
                "first_seen=",
                entry.get("first_seen_chapter"),
                "last_seen=",
                entry.get("last_seen_chapter"),
                "chapter_mentions=",
                entry.get("chapter_mentions", []),
            )
    if global_character_registry and not character_entries:
        raise ValueError(
            f"Snapshot {analysis.chapter_id} projected zero character entries even though the global character registry is non-empty. "
            f"Loaded global characters={len(global_character_registry)}, "
            f"loaded global environments={len(global_environment_registry)}, "
            f"visible characters={len(visible_characters)}, "
            f"visible environments={len(visible_environments)}."
        )
    if global_environment_registry and not environment_entries:
        raise ValueError(
            f"Snapshot {analysis.chapter_id} projected zero environment entries even though the global environment registry is non-empty. "
            f"Loaded global characters={len(global_character_registry)}, "
            f"loaded global environments={len(global_environment_registry)}, "
            f"visible characters={len(visible_characters)}, "
            f"visible environments={len(visible_environments)}."
        )

    known_characters = [
        entry["canonical_id"]
        for entry in character_entries
        if entry.get("status") != "resolved_into" and entry.get("entity_kind") == "individual"
    ]
    known_groups = [
        entry["canonical_id"]
        for entry in character_entries
        if entry.get("status") != "resolved_into" and entry.get("entity_kind") != "individual"
    ]
    provisional_roles = [
        entry["canonical_id"]
        for entry in character_entries
        if entry.get("status") == "provisional"
    ]
    known_environments = [entry["canonical_id"] for entry in environment_entries if entry.get("status") != "resolved_into"]

    snapshot = {
        "chapter_id": analysis.chapter_id,
        "chapter_path": analysis.chapter_path,
        "scene_order": analysis.scene_ids,
        "known_characters": known_characters,
        "known_groups": known_groups,
        "provisional_roles": provisional_roles,
        "known_environments": known_environments,
        "resolved_this_chapter": _chapter_character_resolution_events(global_character_registry, chapter_id=analysis.chapter_id),
        "character_entries": character_entries,
        "environment_entries": environment_entries,
        "global_character_directory_path": global_character_directory_relpath,
        "global_environment_directory_path": global_environment_directory_relpath,
        "global_character_registry_path": global_character_registry_relpath,
        "global_environment_registry_path": global_environment_registry_relpath,
        "generated_at_utc": _utc_now_iso(),
    }
    validate_snapshot_provenance(snapshot, chapter_id=analysis.chapter_id)
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
            "timestamp_utc": _utc_now_iso(),
        }
    )
    _write_json(path, failures)
    return repo_relative(path)


def update_world_sequence_state(*, project_slug: str, succeeded_chapter_ids: list[str], failed_chapter_ids: list[str]) -> str:
    path = world_sequence_state_path(project_slug)
    payload = {
        "processed_chapters": succeeded_chapter_ids,
        "failed_chapters": failed_chapter_ids,
        "updated_at_utc": _utc_now_iso(),
    }
    _write_json(path, payload)
    return repo_relative(path)
