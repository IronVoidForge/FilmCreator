from __future__ import annotations

import hashlib
import json
import re
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .book_librarian import search_book_index, search_chapter_context
from .core.json_io import read_json, write_json
from .features.authoring.packet_parser import parse_packet_document
from .lmstudio_client import LMStudioClient
from .scaffold import create_project
from .settings import load_runtime_settings
from .world_global import global_environment_registry_path


@dataclass
class EnvironmentBibleMetadata:
    artifact_id: str
    artifact_type: str = "environment_bible"
    status: str = "generated"
    source_fingerprint: str | None = None
    created_at_utc: str = ""
    updated_at_utc: str = ""
    upstream_dependencies: list[dict[str, Any]] = field(default_factory=list)
    locked_fields: dict[str, bool] = field(default_factory=dict)
    manual_overrides: dict[str, Any] = field(default_factory=dict)
    revision_history: list[dict[str, Any]] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "artifact_id": self.artifact_id,
            "artifact_type": self.artifact_type,
            "status": self.status,
            "source_fingerprint": self.source_fingerprint,
            "created_at_utc": self.created_at_utc,
            "updated_at_utc": self.updated_at_utc,
            "upstream_dependencies": self.upstream_dependencies,
            "locked_fields": self.locked_fields,
            "manual_overrides": self.manual_overrides,
            "revision_history": self.revision_history,
        }


@dataclass
class EnvironmentBible:
    environment_id: str
    display_name: str
    environment_type: str = "environment"
    status: str = "canonical"
    entity_kind: str = "environment"
    first_seen_chapter: str | None = None
    last_seen_chapter: str | None = None
    chapter_mentions: list[str] = field(default_factory=list)
    visual_summary: str = ""
    layout_notes: str = ""
    lighting: str = ""
    mood: str = ""
    recurring_elements: list[str] = field(default_factory=list)
    constraints: list[str] = field(default_factory=list)
    unresolved_ambiguities: list[str] = field(default_factory=list)
    evidence_refs: list[dict[str, Any]] = field(default_factory=list)
    evidence_summary: list[str] = field(default_factory=list)
    metadata: EnvironmentBibleMetadata | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "environment_id": self.environment_id,
            "display_name": self.display_name,
            "environment_type": self.environment_type,
            "status": self.status,
            "entity_kind": self.entity_kind,
            "first_seen_chapter": self.first_seen_chapter,
            "last_seen_chapter": self.last_seen_chapter,
            "chapter_mentions": self.chapter_mentions,
            "visual_summary": self.visual_summary,
            "layout_notes": self.layout_notes,
            "lighting": self.lighting,
            "mood": self.mood,
            "recurring_elements": self.recurring_elements,
            "constraints": self.constraints,
            "unresolved_ambiguities": self.unresolved_ambiguities,
            "evidence_refs": self.evidence_refs,
            "evidence_summary": self.evidence_summary,
            "metadata": self.metadata.to_dict() if self.metadata else None,
        }


@dataclass(frozen=True)
class EnvironmentBibleSynthesisSummary:
    project_slug: str
    total_registry_entries: int
    synthesized_count: int
    reused_count: int
    stale_locked_count: int
    review_queue_count: int
    written_files: list[str]
    warnings: list[str]

    def to_dict(self) -> dict[str, Any]:
        return {
            "project_slug": self.project_slug,
            "total_registry_entries": self.total_registry_entries,
            "synthesized_count": self.synthesized_count,
            "reused_count": self.reused_count,
            "stale_locked_count": self.stale_locked_count,
            "review_queue_count": self.review_queue_count,
            "written_files": self.written_files,
            "warnings": self.warnings,
        }


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _fingerprint(data: Any) -> str:
    raw = json.dumps(data, sort_keys=True, ensure_ascii=False)
    return hashlib.sha1(raw.encode("utf-8")).hexdigest()


def _load_registry_for_synthesis(project_dir: Path, project_slug: str) -> tuple[dict[str, Any], Path]:
    refined_path = project_dir / "02_story_analysis" / "world" / "refinement" / "ENVIRONMENT_REGISTRY_GLOBAL_REFINED.json"
    canonical_path = global_environment_registry_path(project_slug)

    if refined_path.exists():
        return read_json(refined_path), refined_path
    if canonical_path.exists():
        return read_json(canonical_path), canonical_path
    return {}, canonical_path


def _entry_source_paths(entry: dict[str, Any]) -> list[str]:
    paths: list[str] = []
    for source in entry.get("sources", []):
        if isinstance(source, str) and source.strip() and source not in paths:
            paths.append(source.strip())
    for source in entry.get("source_history", []):
        if not isinstance(source, dict):
            continue
        source_path = source.get("source_path")
        if isinstance(source_path, str) and source_path.strip() and source_path not in paths:
            paths.append(source_path.strip())
    return paths


def _source_chapters_from_paths(source_paths: list[str]) -> list[str]:
    chapters: list[str] = []
    for source_path in source_paths:
        for part in Path(source_path).parts:
            if part.startswith("CH") and len(part) >= 5:
                chapter_id = part[:5]
                if chapter_id not in chapters:
                    chapters.append(chapter_id)
                break
    return chapters


def _parse_environment_breakdown_markdown(markdown: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    for raw_line in markdown.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        match = re.match(r"^\*\*(.+?)\:\*\*\s*(.+)$", line)
        if match:
            key = _normalize_key(match.group(1))
            value = match.group(2).strip()
            if value:
                fields[key] = value
                if key == "lighting_atmosphere":
                    fields.setdefault("lighting", value)
                    fields.setdefault("atmosphere", value)
                elif key in {"scale_anchors", "scale_and_anchors"}:
                    fields.setdefault("scale", value)
                    fields.setdefault("anchors", value)
            continue
        if ":" in line:
            key, value = line.split(":", 1)
            key = _normalize_key(key)
            value = value.strip()
            if key and value:
                fields[key] = value
                if key == "lighting_atmosphere":
                    fields.setdefault("lighting", value)
                    fields.setdefault("atmosphere", value)
                elif key in {"scale_anchors", "scale_and_anchors"}:
                    fields.setdefault("scale", value)
                    fields.setdefault("anchors", value)
    return fields


def _normalize_key(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", value.strip().lower()).strip("_")


def _compact_snippet(text: str, *, limit: int = 220) -> str:
    collapsed = " ".join(text.split()).strip()
    if len(collapsed) <= limit:
        return collapsed
    return collapsed[: limit - 3].rstrip() + "..."


def _first_nonempty(*values: object, fallback: str = "") -> str:
    for value in values:
        if isinstance(value, str) and value.strip():
            return value.strip()
    return fallback


def _coerce_string_list(*values: object) -> list[str]:
    items: list[str] = []
    for value in values:
        if value is None:
            continue
        if isinstance(value, list):
            for item in value:
                if isinstance(item, str) and item.strip() and item.strip().lower() not in {"none", "(none)", "n/a"}:
                    items.append(item.strip())
        elif isinstance(value, str):
            stripped = value.strip()
            if not stripped or stripped.lower() in {"none", "(none)", "n/a"}:
                continue
            parts = [part.strip() for part in re.split(r",|\n", stripped) if part.strip()]
            if parts:
                items.extend(parts)
            else:
                items.append(stripped)

    seen: set[str] = set()
    deduped: list[str] = []
    for item in items:
        if item not in seen:
            seen.add(item)
            deduped.append(item)
    return deduped


def _evidence_query_terms(entry: dict[str, Any], parsed_sources: list[dict[str, str]]) -> list[str]:
    terms: list[str] = []
    for value in [entry.get("canonical_id"), entry.get("display_name"), *entry.get("aliases", [])]:
        if isinstance(value, str):
            normalized = " ".join(value.replace("_", " ").split()).strip()
            if normalized and normalized not in terms:
                terms.append(normalized)

    for parsed in parsed_sources:
        for key in ("role", "geography", "lighting", "atmosphere", "scale", "prompt_phrases"):
            value = parsed.get(key, "")
            if not value:
                continue
            normalized = " ".join(value.replace("_", " ").split()).strip()
            if normalized and normalized not in terms:
                terms.append(normalized)

    return terms[:5]


def _collect_evidence(project_slug: str, entry: dict[str, Any]) -> tuple[list[str], list[dict[str, Any]], list[dict[str, str]]]:
    evidence_lines: list[str] = []
    evidence_refs: list[dict[str, Any]] = []
    parsed_sources: list[dict[str, str]] = []
    seen_lines: set[str] = set()

    def add_line(line: str, ref: dict[str, Any] | None = None) -> None:
        normalized = " ".join(line.split()).strip()
        if not normalized or normalized in seen_lines:
            return
        if len(normalized) > 260:
            normalized = normalized[:257].rstrip() + "..."
        seen_lines.add(normalized)
        evidence_lines.append(normalized)
        if ref is not None:
            evidence_refs.append(ref)

    description_layers = entry.get("description_layers", {})
    for item in description_layers.get("stable_canonical", [])[:3]:
        if isinstance(item, dict):
            summary = str(item.get("summary", "")).strip()
            if summary:
                add_line(
                    summary,
                    {
                        "source": "registry_stable_canonical",
                        "chapter_id": item.get("chapter_id"),
                        "source_path": item.get("source_path"),
                    },
                )
        elif isinstance(item, str):
            add_line(item, {"source": "registry_stable_canonical", "chapter_id": None, "source_path": None})

    for item in description_layers.get("chapter_specific", {}).values():
        if not isinstance(item, list):
            continue
        for sub_item in item[:2]:
            if not isinstance(sub_item, dict):
                continue
            summary = str(sub_item.get("summary", "")).strip()
            if summary:
                add_line(
                    summary,
                    {
                        "source": "registry_chapter_specific",
                        "chapter_id": sub_item.get("chapter_id"),
                        "source_path": sub_item.get("source_path"),
                    },
                )

    source_paths = _entry_source_paths(entry)
    for source_path in source_paths[:3]:
        path = Path(source_path)
        if not path.exists():
            continue
        try:
            parsed = _parse_environment_breakdown_markdown(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        if parsed:
            parsed_sources.append(parsed)
        for key in ("role", "geography", "lighting", "atmosphere", "scale", "prompt_phrases"):
            value = parsed.get(key, "").strip()
            if value:
                label = key.replace("_", " ").title()
                add_line(
                    f"{label}: {value}",
                    {
                        "source": "environment_breakdown_markdown",
                        "chapter_id": _chapter_id_from_path(source_path),
                        "source_path": source_path,
                    },
                )

    chapter_mentions = [str(chapter_id) for chapter_id in entry.get("chapter_mentions", []) if isinstance(chapter_id, str)]
    for parsed in parsed_sources:
        chapter_hint = parsed.get("role", "") or parsed.get("geography", "") or parsed.get("prompt_phrases", "")
        if chapter_hint:
            query_terms = _evidence_query_terms(entry, [parsed])
            search_terms = " ".join(query_terms[:3]).strip()
            if search_terms:
                index_hits = search_book_index(project_slug, search_terms, top_n=3)
                for hit in index_hits:
                    chapter_id = str(hit.get("chapter_id", "")).strip()
                    title = str(hit.get("title", "")).strip()
                    reasons = ", ".join(str(reason) for reason in hit.get("reasons", [])[:2] if str(reason).strip())
                    add_line(
                        f"[{chapter_id}] {title} ({reasons or 'book index hit'})",
                        {"source": "book_index", "chapter_id": chapter_id or None, "source_path": None},
                    )
                    if chapter_id and chapter_id not in chapter_mentions:
                        chapter_mentions.append(chapter_id)

    query_terms = _evidence_query_terms(entry, parsed_sources)
    for chapter_id in chapter_mentions[:3]:
        try:
            contexts = search_chapter_context(project_slug, chapter_id, query_terms, window=1, top_n=2)
        except Exception:
            continue
        for context in contexts:
            snippet = _compact_snippet(context.preview or context.text)
            if not snippet:
                continue
            add_line(
                f"[{chapter_id} p{context.paragraph_start}-p{context.paragraph_end}] {snippet}",
                {
                    "source": "paragraph_window",
                    "chapter_id": chapter_id,
                    "source_path": context.chapter_path,
                    "paragraph_start": context.paragraph_start,
                    "paragraph_end": context.paragraph_end,
                },
            )
            if len(evidence_lines) >= 8:
                break
        if len(evidence_lines) >= 8:
            break

    if not evidence_lines:
        fallback = _compact_snippet(
            str(entry.get("resolution_reason", "")).strip() or entry.get("display_name", "") or entry.get("canonical_id", "")
        )
        if fallback:
            add_line(fallback, {"source": "registry_fallback", "chapter_id": None, "source_path": None})

    return evidence_lines[:8], evidence_refs[:8], parsed_sources


def _deterministic_synthesis(entry: dict[str, Any], evidence_summary: list[str], parsed_sources: list[dict[str, str]]) -> dict[str, Any]:
    parsed = parsed_sources[0] if parsed_sources else {}
    visual = _first_nonempty(parsed.get("geography"), parsed.get("scale"), *evidence_summary[:2], fallback="")
    layout = _first_nonempty(parsed.get("geography"), parsed.get("scale"), fallback="No layout notes available.")
    lighting = _first_nonempty(parsed.get("lighting"), parsed.get("lighting_atmosphere"), parsed.get("atmosphere"), fallback="Unknown")
    mood = _first_nonempty(parsed.get("atmosphere"), parsed.get("lighting_atmosphere"), parsed.get("lighting"), fallback="Unknown")
    recurring = _coerce_string_list(parsed.get("prompt_phrases"))
    constraints = _coerce_string_list(entry.get("resolution_reason"), parsed.get("role"))
    return {
        "display_name": entry.get("display_name") or entry.get("canonical_id"),
        "environment_type": _first_nonempty(parsed.get("role"), fallback=entry.get("entity_kind", "environment")),
        "visual_summary": visual,
        "layout_notes": layout,
        "lighting": lighting,
        "mood": mood,
        "recurring_elements": recurring,
        "constraints": constraints,
        "unresolved_ambiguities": list(entry.get("open_questions", [])),
    }


def _llm_synthesis(entry: dict[str, Any], evidence_summary: list[str]) -> dict[str, Any] | None:
    settings = load_runtime_settings()
    client = LMStudioClient(settings)

    system = (
        "You are a film environment bible synthesis system. "
        "Use only the provided evidence. Prefer cinematic clarity and spatial consistency. "
        "Do not invent unsupported details. Return one tagged FilmCreator markdown packet only. "
        "Do not return JSON."
    )

    user = f"""
Synthesize a canonical environment bible from the provided evidence as tagged markdown.

PRIORITIES:
1. stable spatial identity
2. grounded, non-hallucinated summary
3. concise film-usable language
4. preserve uncertainty when evidence is weak

ENTRY:
{json.dumps(entry, indent=2, ensure_ascii=False)}

EVIDENCE:
{json.dumps(evidence_summary, indent=2, ensure_ascii=False)}

Return exactly one FilmCreator packet in this structure:
[[FILMCREATOR_PACKET]]
task: environment_bible_synthesis
version: 1

[[FILMCREATOR_RECORD]]
type: environment_bible
artifact_id: ENV_{entry.get("canonical_id") or entry.get("display_name") or ""}
environment_id: {entry.get("canonical_id") or entry.get("display_name") or ""}
status: {entry.get("status", "canonical")}
entity_kind: {entry.get("entity_kind", "environment")}

[[SECTION identity_markdown]]
display_name: <display name>
environment_type: <environment type or role>
chapter_mentions:
- CH001
- CH010
[[/SECTION]]

[[SECTION visual_markdown]]
visual_summary: <one grounded paragraph>
layout_notes: <short spatial note>
lighting: <short lighting note or unknown>
mood: <short mood note or unknown>
[[/SECTION]]

[[SECTION motif_markdown]]
recurring_elements:
- recurring element 1
- recurring element 2
constraints:
- constraint 1
- constraint 2
[[/SECTION]]

[[SECTION continuity_markdown]]
unresolved_ambiguities:
- ambiguity 1
- ambiguity 2
[[/SECTION]]

[[SECTION evidence_markdown]]
- evidence line 1
- evidence line 2
[[/SECTION]]

[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
"""

    try:
        text = client.chat_completion(system_prompt=system, user_prompt=user, temperature=0.1)
        return _parse_environment_bible_packet(text, entry)
    except Exception:
        return None


def _parse_environment_bible_packet(text: str, entry: dict[str, Any]) -> dict[str, Any]:
    packet = parse_packet_document(text, expected_task="environment_bible_synthesis")
    if not packet.records:
        raise ValueError("LLM response did not contain an environment bible record.")

    record = packet.records[0]
    fields = record.fields
    sections = record.sections

    identity_scalars, identity_lists, identity_freeform = _parse_bible_markdown_section(sections.get("identity_markdown", ""))
    visual_scalars, visual_lists, visual_freeform = _parse_bible_markdown_section(sections.get("visual_markdown", ""))
    motif_scalars, motif_lists, motif_freeform = _parse_bible_markdown_section(sections.get("motif_markdown", ""))
    continuity_scalars, continuity_lists, continuity_freeform = _parse_bible_markdown_section(sections.get("continuity_markdown", ""))
    evidence_scalars, evidence_lists, evidence_freeform = _parse_bible_markdown_section(sections.get("evidence_markdown", ""))

    display_name = _first_nonempty(
        identity_scalars.get("display_name"),
        fields.get("display_name"),
        entry.get("display_name"),
        entry.get("canonical_id"),
        fallback=str(entry.get("canonical_id") or ""),
    )

    chapter_mentions = _coerce_string_list(identity_lists.get("chapter_mentions"), identity_scalars.get("chapter_mentions"))
    recurring_elements = _coerce_string_list(motif_lists.get("recurring_elements"), motif_scalars.get("recurring_elements"))
    constraints = _coerce_string_list(motif_lists.get("constraints"), motif_scalars.get("constraints"))
    unresolved_ambiguities = _coerce_string_list(continuity_lists.get("unresolved_ambiguities"), continuity_scalars.get("unresolved_ambiguities"))
    evidence_summary = _coerce_string_list(evidence_lists.get("evidence_markdown"), evidence_scalars.get("evidence_markdown"))
    if not evidence_summary:
        evidence_summary = list(evidence_freeform)

    visual_summary = _first_nonempty(
        visual_scalars.get("visual_summary"),
        visual_freeform[0] if visual_freeform else None,
        fallback="",
    )
    layout_notes = _first_nonempty(visual_scalars.get("layout_notes"), fallback="No layout notes provided.")
    lighting = _first_nonempty(visual_scalars.get("lighting"), fallback="Unknown")
    mood = _first_nonempty(visual_scalars.get("mood"), fallback="Unknown")
    environment_type = _first_nonempty(identity_scalars.get("environment_type"), fallback=entry.get("entity_kind", "environment"))

    return {
        "display_name": display_name,
        "environment_type": environment_type,
        "visual_summary": visual_summary,
        "layout_notes": layout_notes,
        "lighting": lighting,
        "mood": mood,
        "recurring_elements": recurring_elements,
        "constraints": constraints,
        "unresolved_ambiguities": unresolved_ambiguities,
        "evidence_summary": evidence_summary[:25],
        "chapter_mentions": chapter_mentions,
    }


_ENVIRONMENT_PATCHABLE_SCALAR_FIELDS = {
    "display_name",
    "environment_type",
    "visual_summary",
    "layout_notes",
    "lighting",
    "mood",
}

_ENVIRONMENT_PATCHABLE_LIST_FIELDS = {
    "recurring_elements",
    "constraints",
    "unresolved_ambiguities",
    "chapter_mentions",
}


def _apply_locked_and_manual_overrides(merged: dict[str, Any], existing: dict | None, metadata: EnvironmentBibleMetadata) -> dict[str, Any]:
    if existing:
        for field_name, locked in metadata.locked_fields.items():
            if locked and field_name in existing:
                merged[field_name] = existing[field_name]

    for field_name, value in metadata.manual_overrides.items():
        merged[field_name] = value

    return merged


def _environment_patch_prompt(entry: dict[str, Any], existing: dict[str, Any], evidence_summary: list[str], focus_fields: list[str]) -> str:
    list_fields = sorted(field for field in focus_fields if field in _ENVIRONMENT_PATCHABLE_LIST_FIELDS)
    scalar_fields = sorted(field for field in focus_fields if field in _ENVIRONMENT_PATCHABLE_SCALAR_FIELDS and field not in _ENVIRONMENT_PATCHABLE_LIST_FIELDS)
    field_lines: list[str] = []
    for field_name in scalar_fields:
        field_lines.append(f"{field_name}: <updated value or omit if unchanged>")
    for field_name in list_fields:
        field_lines.append(f"{field_name}:")
        field_lines.append("- updated item 1")
        field_lines.append("- updated item 2")

    current_artifact = {
        key: existing.get(key)
        for key in [
            "display_name",
            "environment_type",
            "visual_summary",
            "layout_notes",
            "lighting",
            "mood",
            "recurring_elements",
            "constraints",
            "unresolved_ambiguities",
            "chapter_mentions",
        ]
    }

    return f"""
Patch the provided environment bible by updating only the requested weak fields.

RULES:
- Preserve every field that is not explicitly requested.
- Do not rewrite the whole artifact.
- If a field cannot be improved, omit it.
- Keep existing good information intact.
- Use only the provided evidence and current artifact context.

ENTRY:
{json.dumps(entry, indent=2, ensure_ascii=False)}

CURRENT_ARTIFACT:
{json.dumps(current_artifact, indent=2, ensure_ascii=False)}

EVIDENCE:
{json.dumps(evidence_summary, indent=2, ensure_ascii=False)}

FIELDS_TO_UPDATE:
{json.dumps(focus_fields, indent=2, ensure_ascii=False)}

Return exactly one FilmCreator packet in this structure:
[[FILMCREATOR_PACKET]]
task: environment_bible_patch
version: 1

[[FILMCREATOR_RECORD]]
type: environment_bible
artifact_id: ENV_{entry.get("canonical_id") or entry.get("display_name") or ""}
environment_id: {entry.get("canonical_id") or entry.get("display_name") or ""}
status: {entry.get("status", "canonical")}
entity_kind: {entry.get("entity_kind", "environment")}

[[SECTION patch_markdown]]
{chr(10).join(field_lines) if field_lines else "(no changes requested)"}
[[/SECTION]]

[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
"""


def _parse_environment_patch_packet(text: str, entry: dict[str, Any], focus_fields: list[str]) -> dict[str, Any]:
    packet = parse_packet_document(text, expected_task="environment_bible_patch")
    if not packet.records:
        raise ValueError("LLM response did not contain an environment bible patch record.")

    record = packet.records[0]
    sections = record.sections
    scalars, lists, freeform = _parse_bible_markdown_section(sections.get("patch_markdown", ""))

    patch: dict[str, Any] = {}
    for field_name in focus_fields:
        if field_name in _ENVIRONMENT_PATCHABLE_LIST_FIELDS:
            values = _coerce_string_list(lists.get(field_name), scalars.get(field_name))
            if values:
                patch[field_name] = values
            continue
        if field_name in _ENVIRONMENT_PATCHABLE_SCALAR_FIELDS:
            value = _first_nonempty(scalars.get(field_name), fallback="")
            if not value and freeform and field_name == "visual_summary":
                value = freeform[0]
            if value and value.lower() not in {"unknown", "none", "(none)", "n/a"}:
                patch[field_name] = value

    display_name = _first_nonempty(
        scalars.get("display_name"),
        record.fields.get("display_name"),
        entry.get("display_name"),
        entry.get("canonical_id"),
        fallback=str(entry.get("canonical_id") or ""),
    )
    if display_name:
        patch["display_name"] = display_name

    return patch


def _apply_environment_patch(existing: dict[str, Any], patch: dict[str, Any], metadata: EnvironmentBibleMetadata, focus_fields: list[str]) -> dict[str, Any]:
    merged = dict(existing)
    for field_name in focus_fields:
        if field_name not in patch:
            continue
        value = patch[field_name]
        if field_name in _ENVIRONMENT_PATCHABLE_LIST_FIELDS:
            if isinstance(value, list) and value:
                merged[field_name] = value
            elif isinstance(value, str):
                coerced = _coerce_string_list(value)
                if coerced:
                    merged[field_name] = coerced
            continue
        if isinstance(value, str) and value.strip() and value.strip().lower() not in {"unknown", "none", "(none)", "n/a"}:
            merged[field_name] = value.strip()

    return _apply_locked_and_manual_overrides(merged, existing, metadata)


def _llm_patch_synthesis(entry: dict[str, Any], existing: dict[str, Any], evidence_summary: list[str], focus_fields: list[str]) -> dict[str, Any] | None:
    if not focus_fields:
        return None

    settings = load_runtime_settings()
    client = LMStudioClient(settings)

    system = (
        "You are a film environment bible patching system. "
        "Only update the requested weak fields. "
        "Preserve existing good fields exactly. "
        "Use only the provided evidence and artifact context. "
        "Return one tagged FilmCreator markdown packet only. "
        "Do not return JSON."
    )
    user = _environment_patch_prompt(entry, existing, evidence_summary, focus_fields)

    try:
        text = client.chat_completion(system_prompt=system, user_prompt=user, temperature=0.1)
        return _parse_environment_patch_packet(text, entry, focus_fields)
    except Exception:
        return None


def _parse_bible_markdown_section(section_text: str) -> tuple[dict[str, str], dict[str, list[str]], list[str]]:
    scalars: dict[str, str] = {}
    lists: dict[str, list[str]] = {}
    freeform: list[str] = []
    current_list_key: str | None = None

    for raw_line in section_text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("- "):
            item = line[2:].strip()
            if current_list_key:
                if item and item.lower() not in {"none", "(none)", "n/a"}:
                    lists.setdefault(current_list_key, []).append(item)
            elif item:
                freeform.append(item)
            continue
        if ":" in line:
            key, value = line.split(":", 1)
            key = key.strip().lower().replace(" ", "_")
            value = value.strip()
            if value:
                scalars[key] = value
                current_list_key = None
            else:
                current_list_key = key
                lists.setdefault(key, [])
            continue
        if current_list_key:
            lists.setdefault(current_list_key, []).append(line)
        else:
            freeform.append(line)

    return scalars, lists, freeform


def _load_existing_metadata(existing: dict | None, artifact_id: str, fp: str) -> EnvironmentBibleMetadata:
    old_meta = (existing or {}).get("metadata") or {}
    return EnvironmentBibleMetadata(
        artifact_id=artifact_id,
        status=old_meta.get("status", "generated"),
        source_fingerprint=fp,
        created_at_utc=old_meta.get("created_at_utc") or _utc_now(),
        updated_at_utc=_utc_now(),
        upstream_dependencies=old_meta.get("upstream_dependencies", []),
        locked_fields=old_meta.get("locked_fields", {}),
        manual_overrides=old_meta.get("manual_overrides", {}),
        revision_history=old_meta.get("revision_history", []),
    )


def _merge_with_existing(new: dict[str, Any], existing: dict | None, metadata: EnvironmentBibleMetadata) -> dict[str, Any]:
    if not existing:
        return new

    merged = dict(new)
    for field_name, locked in metadata.locked_fields.items():
        if locked and field_name in existing:
            merged[field_name] = existing[field_name]

    for field_name, value in metadata.manual_overrides.items():
        merged[field_name] = value

    return merged


def _is_film_facing_environment(entry: dict[str, Any], bible: EnvironmentBible | None = None) -> bool:
    if entry.get("status") != "canonical":
        return False
    if entry.get("entity_kind") != "environment":
        return False
    return True


def _write_json_and_markdown(base_path: Path, bible: EnvironmentBible) -> None:
    write_json(base_path.with_suffix(".json"), bible.to_dict())
    write_environment_bible_markdown(base_path.with_suffix(".md"), bible)


def _chapter_id_from_path(source_path: str) -> str:
    for part in Path(source_path).parts:
        if part.startswith("CH") and len(part) >= 5:
            return part[:5]
    return ""


def write_environment_bible_markdown(path: Path, bible: EnvironmentBible) -> None:
    lines = [
        f"# Environment Bible: {bible.display_name}",
        "",
        f"- environment_id: `{bible.environment_id}`",
        f"- status: `{bible.status}`",
        f"- entity_kind: `{bible.entity_kind}`",
        f"- first_seen_chapter: `{bible.first_seen_chapter}`",
        f"- last_seen_chapter: `{bible.last_seen_chapter}`",
        "",
        "## Identity",
        "",
        f"- display_name: {bible.display_name}",
        f"- environment_type: {bible.environment_type or '(none)'}",
        f"- chapter_mentions: {', '.join(bible.chapter_mentions) if bible.chapter_mentions else '(none)'}",
        "",
        "## Visual Bible",
        "",
        bible.visual_summary or "(no stable visual summary yet)",
        "",
        f"- layout_notes: {bible.layout_notes or '(none)'}",
        f"- lighting: {bible.lighting or '(none)'}",
        f"- mood: {bible.mood or '(none)'}",
        f"- recurring_elements: {', '.join(bible.recurring_elements) if bible.recurring_elements else '(none)'}",
        "",
        "## Continuity",
        "",
        f"- constraints: {', '.join(bible.constraints) if bible.constraints else '(none)'}",
        f"- unresolved_ambiguities: {', '.join(bible.unresolved_ambiguities) if bible.unresolved_ambiguities else '(none)'}",
        "",
        "## Evidence Summary",
        "",
    ]

    if bible.evidence_summary:
        lines.extend([f"- {item}" for item in bible.evidence_summary])
    else:
        lines.append("- (none)")

    lines.extend(["", "## Metadata", ""])
    if bible.metadata:
        lines.extend(
            [
                f"- artifact_id: `{bible.metadata.artifact_id}`",
                f"- status: `{bible.metadata.status}`",
                f"- source_fingerprint: `{bible.metadata.source_fingerprint}`",
                f"- created_at_utc: `{bible.metadata.created_at_utc}`",
                f"- updated_at_utc: `{bible.metadata.updated_at_utc}`",
            ]
        )

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_environment_bible_index(index_path: Path, records: list[EnvironmentBible]) -> None:
    lines = ["# Environment Bible Index", ""]
    for record in sorted(records, key=lambda item: item.environment_id):
        lines.append(
            f"- `{record.environment_id}` - {record.display_name} "
            f"(type={record.environment_type}, status={record.status}, mentions={len(record.chapter_mentions)}, constraints={len(record.constraints)})"
        )
    index_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_environment_bible_review_index(index_path: Path, records: list[EnvironmentBible]) -> None:
    lines = ["# Environment Bible Review Index", ""]
    if not records:
        lines.append("- No review entries.")
        index_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        return

    for record in sorted(records, key=lambda item: item.environment_id):
        flags: list[str] = []
        if record.status != "canonical":
            flags.append(f"status={record.status}")
        if record.entity_kind != "environment":
            flags.append(f"entity_kind={record.entity_kind}")
        if record.unresolved_ambiguities:
            flags.append(f"ambiguities={len(record.unresolved_ambiguities)}")
        flag_text = ", ".join(flags) if flags else "review"
        lines.append(f"- `{record.environment_id}` - {record.display_name} ({flag_text})")

    index_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_environment_review_queue_markdown(path: Path, queue: list[dict[str, Any]]) -> None:
    lines = ["# Environment Bible Review Queue", ""]
    if not queue:
        lines.append("- No environment bible review items.")
    else:
        for item in queue:
            lines.append(f"- `{item.get('environment_id')}`")
            for issue in item.get("issues", []):
                lines.append(f"  - {issue}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def run_environment_bible_synthesis(
    project_slug: str,
    *,
    use_llm: bool = True,
    force: bool = False,
    limit: int | None = None,
) -> EnvironmentBibleSynthesisSummary:
    project_dir = create_project(project_slug)

    registry, _registry_path = _load_registry_for_synthesis(project_dir, project_slug)

    output_dir = project_dir / "02_story_analysis" / "bibles" / "environments"
    review_dir = output_dir / "review"
    output_dir.mkdir(parents=True, exist_ok=True)
    review_dir.mkdir(parents=True, exist_ok=True)

    synthesized = 0
    reused = 0
    stale_locked = 0
    review_queue: list[dict[str, Any]] = []
    written_files: list[str] = []
    warnings: list[str] = []
    bible_records: list[EnvironmentBible] = []
    review_records: list[EnvironmentBible] = []
    registry_items = list(registry.items())
    if limit is not None and limit >= 0:
        registry_items = registry_items[:limit]
    total_entries = len(registry_items)

    for index, (env_id, entry) in enumerate(registry_items, start=1):
        started_at = time.perf_counter()
        print(f"[environment-bible] {index}/{total_entries} starting {env_id}...")
        fp = _fingerprint(entry)
        base_path = output_dir / f"ENV_{env_id}"
        existing = read_json(base_path.with_suffix(".json")) if base_path.with_suffix(".json").exists() else None
        metadata = _load_existing_metadata(existing, artifact_id=f"ENV_{env_id}", fp=fp)

        if existing and not force:
            old_meta = existing.get("metadata") or {}
            if old_meta.get("source_fingerprint") == fp:
                reused += 1
                bible = EnvironmentBible(
                    environment_id=existing.get("environment_id", env_id),
                    display_name=existing.get("display_name", env_id),
                    environment_type=existing.get("environment_type", "environment"),
                    status=existing.get("status", "canonical"),
                    entity_kind=existing.get("entity_kind", "environment"),
                    first_seen_chapter=existing.get("first_seen_chapter"),
                    last_seen_chapter=existing.get("last_seen_chapter"),
                    chapter_mentions=existing.get("chapter_mentions", []),
                    visual_summary=existing.get("visual_summary", ""),
                    layout_notes=existing.get("layout_notes", ""),
                    lighting=existing.get("lighting", ""),
                    mood=existing.get("mood", ""),
                    recurring_elements=existing.get("recurring_elements", []),
                    constraints=existing.get("constraints", []),
                    unresolved_ambiguities=existing.get("unresolved_ambiguities", []),
                    evidence_refs=existing.get("evidence_refs", []),
                    evidence_summary=existing.get("evidence_summary", []),
                    metadata=metadata,
                )
                bible_records.append(bible)
                if not _is_film_facing_environment(entry, bible) or bible.unresolved_ambiguities:
                    review_records.append(bible)
                elapsed = round(time.perf_counter() - started_at, 1)
                print(f"[environment-bible] {index}/{total_entries} finished {env_id} (reused) in {elapsed}s")
                continue

            if old_meta.get("status") == "locked":
                stale_locked += 1
                existing["metadata"]["status"] = "stale"
                write_json(base_path.with_suffix(".json"), existing)
                warnings.append(f"Locked environment bible became stale and was not regenerated: {env_id}")
                elapsed = round(time.perf_counter() - started_at, 1)
                print(f"[environment-bible] {index}/{total_entries} finished {env_id} (stale locked) in {elapsed}s")
                continue

        evidence_summary, evidence_refs, parsed_sources = _collect_evidence(project_slug, entry)
        synthesized_payload = _llm_synthesis(entry, evidence_summary) if use_llm else None
        if not synthesized_payload:
            synthesized_payload = _deterministic_synthesis(entry, evidence_summary, parsed_sources)
            if use_llm:
                warnings.append(f"LLM synthesis failed or returned invalid markdown packet for {env_id}; used deterministic fallback.")

        merged = _merge_with_existing(synthesized_payload, existing, metadata)

        metadata.upstream_dependencies = [
            {
                "dependency_type": "environment_registry_entry",
                "dependency_id": env_id,
                "version": fp,
            }
        ]
        metadata.revision_history.append(
            {
                "timestamp_utc": _utc_now(),
                "action": "synthesized",
                "source_fingerprint": fp,
            }
        )

        bible = EnvironmentBible(
            environment_id=env_id,
            display_name=merged.get("display_name") or entry.get("display_name") or env_id,
            environment_type=merged.get("environment_type") or entry.get("entity_kind", "environment"),
            status=entry.get("status", "canonical"),
            entity_kind=entry.get("entity_kind", "environment"),
            first_seen_chapter=entry.get("first_seen_chapter"),
            last_seen_chapter=entry.get("last_seen_chapter"),
            chapter_mentions=entry.get("chapter_mentions", []),
            visual_summary=merged.get("visual_summary", ""),
            layout_notes=merged.get("layout_notes", ""),
            lighting=merged.get("lighting", ""),
            mood=merged.get("mood", ""),
            recurring_elements=merged.get("recurring_elements", []),
            constraints=merged.get("constraints", []),
            unresolved_ambiguities=merged.get("unresolved_ambiguities", []),
            evidence_refs=evidence_refs,
            evidence_summary=evidence_summary,
            metadata=metadata,
        )

        _write_json_and_markdown(base_path, bible)
        written_files.extend([str(base_path.with_suffix(".json")), str(base_path.with_suffix(".md"))])
        synthesized += 1
        bible_records.append(bible)

        if not _is_film_facing_environment(entry, bible) or bible.unresolved_ambiguities:
            review_records.append(bible)

        if bible.unresolved_ambiguities:
            review_queue.append(
                {
                    "environment_id": env_id,
                    "issues": bible.unresolved_ambiguities,
                }
            )

        elapsed = round(time.perf_counter() - started_at, 1)
        mode = "synthesized" if synthesized_payload else "generated"
        print(f"[environment-bible] {index}/{total_entries} finished {env_id} ({mode}) in {elapsed}s")

    write_json(review_dir / "ENVIRONMENT_BIBLE_REVIEW_QUEUE.json", review_queue)
    write_environment_review_queue_markdown(review_dir / "ENVIRONMENT_BIBLE_REVIEW_QUEUE.md", review_queue)
    main_records = [
        record
        for record in bible_records
        if _is_film_facing_environment(entry=registry.get(record.environment_id, {}), bible=record)
    ]
    write_environment_bible_index(output_dir / "ENVIRONMENT_BIBLE_INDEX.md", main_records)
    write_environment_bible_review_index(output_dir / "ENVIRONMENT_BIBLE_REVIEW_INDEX.md", review_records)
    write_json(
        output_dir / "ENVIRONMENT_BIBLE_INDEX.json",
        [record.to_dict() for record in sorted(main_records, key=lambda item: item.environment_id)],
    )
    write_json(
        output_dir / "ENVIRONMENT_BIBLE_REVIEW_INDEX.json",
        [record.to_dict() for record in sorted(review_records, key=lambda item: item.environment_id)],
    )

    written_files.extend(
        [
            str(review_dir / "ENVIRONMENT_BIBLE_REVIEW_QUEUE.json"),
            str(review_dir / "ENVIRONMENT_BIBLE_REVIEW_QUEUE.md"),
            str(output_dir / "ENVIRONMENT_BIBLE_INDEX.md"),
            str(output_dir / "ENVIRONMENT_BIBLE_INDEX.json"),
            str(output_dir / "ENVIRONMENT_BIBLE_REVIEW_INDEX.md"),
            str(output_dir / "ENVIRONMENT_BIBLE_REVIEW_INDEX.json"),
        ]
    )

    return EnvironmentBibleSynthesisSummary(
        project_slug=project_slug,
        total_registry_entries=len(registry),
        synthesized_count=synthesized,
        reused_count=reused,
        stale_locked_count=stale_locked,
        review_queue_count=len(review_queue),
        written_files=written_files,
        warnings=warnings,
    )


def run_environment_bible_patch_reruns(
    project_slug: str,
    queue_items: list[dict[str, Any]],
    *,
    use_llm: bool = True,
) -> EnvironmentBibleSynthesisSummary:
    project_dir = create_project(project_slug)
    registry, _registry_path = _load_registry_for_synthesis(project_dir, project_slug)

    output_dir = project_dir / "02_story_analysis" / "bibles" / "environments"
    review_dir = output_dir / "review"
    output_dir.mkdir(parents=True, exist_ok=True)
    review_dir.mkdir(parents=True, exist_ok=True)

    patched = 0
    skipped = 0
    stale_locked = 0
    review_queue: list[dict[str, Any]] = []
    written_files: list[str] = []
    warnings: list[str] = []
    bible_records: list[EnvironmentBible] = []
    review_records: list[EnvironmentBible] = []

    env_items = [item for item in queue_items if str(item.get("family", "")).strip() == "environment_bible"]
    total_items = len(env_items)

    for index, item in enumerate(env_items, start=1):
        env_id = str(item.get("artifact_id") or item.get("display_name") or "").strip()
        focus_fields = [str(field).strip() for field in item.get("focus_fields", []) if str(field).strip() in _ENVIRONMENT_PATCHABLE_SCALAR_FIELDS or str(field).strip() in _ENVIRONMENT_PATCHABLE_LIST_FIELDS]
        if not env_id or not focus_fields:
            skipped += 1
            continue

        started_at = time.perf_counter()
        print(f"[environment-bible] patch {index}/{total_items} starting {env_id} ({', '.join(focus_fields)})...")
        entry = registry.get(env_id)
        if not isinstance(entry, dict):
            warnings.append(f"Environment registry entry not found for patch rerun: {env_id}")
            skipped += 1
            elapsed = round(time.perf_counter() - started_at, 1)
            print(f"[environment-bible] patch {index}/{total_items} finished {env_id} (missing registry entry) in {elapsed}s")
            continue

        fp = _fingerprint(entry)
        base_path = output_dir / f"ENV_{env_id}"
        existing = read_json(base_path.with_suffix(".json")) if base_path.with_suffix(".json").exists() else None
        if not isinstance(existing, dict):
            warnings.append(f"Environment bible missing for patch rerun: {env_id}")
            skipped += 1
            elapsed = round(time.perf_counter() - started_at, 1)
            print(f"[environment-bible] patch {index}/{total_items} finished {env_id} (missing bible) in {elapsed}s")
            continue

        old_meta = existing.get("metadata") or {}
        if old_meta.get("status") == "locked":
            stale_locked += 1
            existing["metadata"]["status"] = "stale"
            write_json(base_path.with_suffix(".json"), existing)
            warnings.append(f"Locked environment bible became stale and was not patched: {env_id}")
            elapsed = round(time.perf_counter() - started_at, 1)
            print(f"[environment-bible] patch {index}/{total_items} finished {env_id} (stale locked) in {elapsed}s")
            continue

        metadata = _load_existing_metadata(existing, artifact_id=f"ENV_{env_id}", fp=fp)
        evidence_summary, evidence_refs, parsed_sources = _collect_evidence(project_slug, entry)
        patch_payload = _llm_patch_synthesis(entry, existing, evidence_summary, focus_fields) if use_llm else None
        if not patch_payload:
            patch_payload = {}
            if use_llm:
                warnings.append(f"LLM patch synthesis failed or returned invalid output for {env_id}; existing values were preserved.")

        merged = _apply_environment_patch(existing, patch_payload, metadata, focus_fields)
        existing_evidence_summary = existing.get("evidence_summary", [])
        existing_evidence_refs = existing.get("evidence_refs", [])
        merged_evidence_summary = _coerce_string_list(existing_evidence_summary, evidence_summary)
        merged_evidence_refs: list[dict[str, Any]] = []
        seen_ref_keys: set[str] = set()
        for ref in [*existing_evidence_refs, *evidence_refs]:
            if not isinstance(ref, dict):
                continue
            ref_key = json.dumps(ref, sort_keys=True, ensure_ascii=False)
            if ref_key in seen_ref_keys:
                continue
            seen_ref_keys.add(ref_key)
            merged_evidence_refs.append(ref)

        metadata.upstream_dependencies = [
            {
                "dependency_type": "environment_registry_entry",
                "dependency_id": env_id,
                "version": fp,
            }
        ]
        metadata.revision_history.append(
            {
                "timestamp_utc": _utc_now(),
                "action": "patched_fields",
                "source_fingerprint": fp,
                "patched_fields": focus_fields,
            }
        )

        bible = EnvironmentBible(
            environment_id=env_id,
            display_name=merged.get("display_name") or entry.get("display_name") or env_id,
            environment_type=merged.get("environment_type") or entry.get("entity_kind", "environment"),
            status=entry.get("status", "canonical"),
            entity_kind=entry.get("entity_kind", "environment"),
            first_seen_chapter=merged.get("first_seen_chapter") or entry.get("first_seen_chapter"),
            last_seen_chapter=merged.get("last_seen_chapter") or entry.get("last_seen_chapter"),
            chapter_mentions=merged.get("chapter_mentions") if isinstance(merged.get("chapter_mentions"), list) else entry.get("chapter_mentions", []),
            visual_summary=merged.get("visual_summary", ""),
            layout_notes=merged.get("layout_notes", ""),
            lighting=merged.get("lighting", ""),
            mood=merged.get("mood", ""),
            recurring_elements=merged.get("recurring_elements", []),
            constraints=merged.get("constraints", []),
            unresolved_ambiguities=merged.get("unresolved_ambiguities", []),
            evidence_refs=merged_evidence_refs or existing_evidence_refs,
            evidence_summary=merged_evidence_summary or existing_evidence_summary,
            metadata=metadata,
        )

        _write_json_and_markdown(base_path, bible)
        written_files.extend([str(base_path.with_suffix(".json")), str(base_path.with_suffix(".md"))])
        patched += 1
        bible_records.append(bible)

        if not _is_film_facing_environment(entry, bible) or bible.unresolved_ambiguities:
            review_records.append(bible)
        if bible.unresolved_ambiguities:
            review_queue.append({"environment_id": env_id, "issues": bible.unresolved_ambiguities})

        elapsed = round(time.perf_counter() - started_at, 1)
        print(f"[environment-bible] patch {index}/{total_items} finished {env_id} (patched) in {elapsed}s")

    write_json(review_dir / "ENVIRONMENT_BIBLE_REVIEW_QUEUE.json", review_queue)
    write_environment_review_queue_markdown(review_dir / "ENVIRONMENT_BIBLE_REVIEW_QUEUE.md", review_queue)
    main_records = [
        record
        for record in bible_records
        if _is_film_facing_environment(entry=registry.get(record.environment_id, {}), bible=record)
    ]
    write_environment_bible_index(output_dir / "ENVIRONMENT_BIBLE_INDEX.md", main_records)
    write_environment_bible_review_index(output_dir / "ENVIRONMENT_BIBLE_REVIEW_INDEX.md", review_records)
    write_json(
        output_dir / "ENVIRONMENT_BIBLE_INDEX.json",
        [record.to_dict() for record in sorted(main_records, key=lambda item: item.environment_id)],
    )
    write_json(
        output_dir / "ENVIRONMENT_BIBLE_REVIEW_INDEX.json",
        [record.to_dict() for record in sorted(review_records, key=lambda item: item.environment_id)],
    )

    written_files.extend(
        [
            str(review_dir / "ENVIRONMENT_BIBLE_REVIEW_QUEUE.json"),
            str(review_dir / "ENVIRONMENT_BIBLE_REVIEW_QUEUE.md"),
            str(output_dir / "ENVIRONMENT_BIBLE_INDEX.md"),
            str(output_dir / "ENVIRONMENT_BIBLE_INDEX.json"),
            str(output_dir / "ENVIRONMENT_BIBLE_REVIEW_INDEX.md"),
            str(output_dir / "ENVIRONMENT_BIBLE_REVIEW_INDEX.json"),
        ]
    )

    return EnvironmentBibleSynthesisSummary(
        project_slug=project_slug,
        total_registry_entries=len(registry),
        synthesized_count=patched,
        reused_count=skipped,
        stale_locked_count=stale_locked,
        review_queue_count=len(review_queue),
        written_files=written_files,
        warnings=warnings,
    )
