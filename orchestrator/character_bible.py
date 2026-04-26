from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
import time

from .character_bible_models import (
    CharacterBible,
    CharacterBibleMetadata,
    CharacterBibleSynthesisSummary,
)
from .character_bible_fallback import (
    needs_visual_production_fallback,
    deterministic_visual_fallback,
    visual_field_audit,
    fallback_result_audit,
)
from .character_bible_writer import (
    write_character_bible_index,
    write_character_bible_review_index,
    write_character_bible_markdown,
    write_character_review_queue_markdown,
)
from .core.json_io import read_json, write_json
from .core.paths import ROOT
from .book_librarian import search_book_index, search_chapter_context
from .lmstudio_client import LMStudioClient
from .settings import load_runtime_settings
from .scaffold import create_project
from .features.authoring.packet_parser import parse_packet_document
from .world_global import global_character_registry_path


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _fingerprint(data: Any) -> str:
    raw = json.dumps(data, sort_keys=True, ensure_ascii=False)
    return hashlib.sha1(raw.encode("utf-8")).hexdigest()


def _extract_labelled_block(text: str, label: str) -> str:
    pattern = re.compile(rf"^\*\*{re.escape(label)}:\*\*\s*(.*)$", re.IGNORECASE)
    lines = text.splitlines()
    for index, raw_line in enumerate(lines):
        match = pattern.match(raw_line.strip())
        if not match:
            continue
        inline = match.group(1).strip()
        if inline:
            return inline
        block: list[str] = []
        for follow in lines[index + 1 :]:
            stripped = follow.strip()
            if not stripped:
                if block:
                    break
                continue
            if stripped.startswith("#") or stripped.startswith("**"):
                break
            block.append(stripped)
        if block:
            return " ".join(block)
    return ""


def _collect_character_breakdown_snippets(entry: dict[str, Any]) -> list[tuple[str, dict[str, Any]]]:
    snippets: list[tuple[str, dict[str, Any]]] = []
    seen_paths: set[str] = set()
    source_paths: list[str] = []
    for source in entry.get("sources", []) or []:
        if isinstance(source, str) and source.strip():
            source_paths.append(source.strip())
    for source_history in entry.get("source_history", []) or []:
        if isinstance(source_history, dict):
            source_path = str(source_history.get("source_path", "")).strip()
            if source_path:
                source_paths.append(source_path)

    for source_path in source_paths:
        if source_path in seen_paths:
            continue
        seen_paths.add(source_path)
        path = Path(source_path)
        if not path.is_absolute():
            path = ROOT / path
        if not path.exists() or path.suffix.lower() != ".md":
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except Exception:
            continue
        for label in [
            "Physical Description",
            "Costume/Silhouette",
            "Prompt Phrases",
            "Manual Description Input Required",
            "Manual Description Reason",
        ]:
            snippet = _extract_labelled_block(text, label)
            if snippet:
                snippets.append(
                    (
                        f"[source:{path.as_posix()}] {label}: {_compact_snippet(snippet, limit=220)}",
                        {
                            "source": "chapter_breakdown",
                            "chapter_id": entry.get("first_seen_chapter") or (entry.get("chapter_mentions") or [None])[0],
                            "source_path": path.as_posix(),
                        },
                    )
                )
        if len(snippets) >= 8:
            break
    return snippets[:8]


def _collect_evidence(project_slug: str, entry: dict) -> tuple[list[str], list[dict[str, Any]]]:
    evidence_lines: list[str] = []
    evidence_refs: list[dict[str, Any]] = []
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

    desc = entry.get("description_layers", {})
    for item in desc.get("stable_canonical", [])[:3]:
        if isinstance(item, dict):
            summary = str(item.get("summary", "")).strip()
            if summary:
                add_line(summary, {"source": "registry_stable_canonical", "chapter_id": item.get("chapter_id"), "source_path": item.get("source_path")})
        elif isinstance(item, str):
            add_line(item, {"source": "registry_stable_canonical", "chapter_id": None, "source_path": None})

    for item in desc.get("initial_extracted", [])[:4]:
        if isinstance(item, dict):
            summary = str(item.get("summary", "")).strip()
            if summary:
                add_line(summary, {"source": "registry_initial_extracted", "chapter_id": item.get("chapter_id"), "source_path": item.get("source_path")})
        elif isinstance(item, str):
            add_line(item, {"source": "registry_initial_extracted", "chapter_id": None, "source_path": None})

    for snippet, ref in _collect_character_breakdown_snippets(entry):
        add_line(snippet, ref)

    chapter_mentions = [str(chapter_id) for chapter_id in entry.get("chapter_mentions", []) if isinstance(chapter_id, str)]
    query_terms = _evidence_query_terms(entry)
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
        fallback = _compact_snippet(str(entry.get("resolution_reason", "")).strip() or entry.get("display_name", "") or entry.get("canonical_id", ""))
        if fallback:
            add_line(fallback, {"source": "registry_fallback", "chapter_id": None, "source_path": None})

    return evidence_lines[:8], evidence_refs[:8]


def _deterministic_synthesis(entry: dict, evidence_summary: list[str]) -> dict[str, Any]:
    visual_lines = evidence_summary[:3]
    unresolved = list(entry.get("open_questions", []))
    return {
        "display_name": entry.get("display_name") or entry.get("canonical_id"),
        "identity_baseline": _first_nonempty(visual_lines[0] if visual_lines else None, fallback="unknown"),
        "age_presence": "unknown",
        "physical_build": "unknown",
        "origin_or_historical_context": "unknown",
        "movement_language": "unknown",
        "stable_visual_summary": " ".join(visual_lines) if visual_lines else "",
        "physical_traits": [],
        "costume_signature": "",
        "distinguishing_features": [],
        "state_variants": [],
        "personality": "",
        "role": entry.get("entity_kind", "character"),
        "voice_notes": "",
        "relationship_notes": [],
        "continuity_constraints": [],
        "unresolved_ambiguities": unresolved,
    }


def _llm_synthesis(entry: dict, evidence_summary: list[str]) -> dict[str, Any] | None:
    settings = load_runtime_settings()
    client = LMStudioClient(settings)

    system = (
        "You are a film character bible synthesis system. "
        "Use only the provided evidence. Prefer cinematic clarity and consistency. "
        "Do not invent unsupported details. Return one tagged FilmCreator markdown packet only. "
        "Do not return JSON."
    )

    user = f"""
Synthesize a canonical character bible from the provided evidence as tagged markdown.

PRIORITIES:
1. stable visual identity
2. grounded, non-hallucinated summary
3. concise film-usable language
4. preserve unresolved ambiguity when evidence is weak

BUCKET RULES:
- identity_baseline: who the character is in visually stable terms, not a biography dump
- age_presence: broad visual age read or stage of life
- physical_build: body type, frame, mass, and proportions
- origin_or_historical_context: any setting or era cues that affect appearance
- movement_language: how the character carries themselves or moves when visible on screen
- costume_signature: the compact clothing or armor phrase that should stay stable
- distinguishing_features: scars, marks, unusual anatomy, or repeatable identifiers
- state_variants: distinct visual states worth preserving, such as clothed, armed, wounded, naked, ceremonial, or battle-ready
- stable_visual_summary: one grounded paragraph that fuses the buckets above into a film-usable read
- physical_traits: short supporting visual traits that do not fit the other buckets
- use unknown only when the book and evidence truly do not support a stable choice
- if a detail is inferable but not explicitly stated, place it in a generated or inferred bucket rather than leaving the whole field empty

ENTRY:
{json.dumps(entry, indent=2, ensure_ascii=False)}

EVIDENCE:
{json.dumps(evidence_summary, indent=2, ensure_ascii=False)}

Return exactly one FilmCreator packet in this structure:
[[FILMCREATOR_PACKET]]
task: character_bible_synthesis
version: 1

[[FILMCREATOR_RECORD]]
type: character_bible
artifact_id: CHAR_{entry.get("canonical_id") or entry.get("display_name") or ""}
character_id: {entry.get("canonical_id") or entry.get("display_name") or ""}
status: {entry.get("status", "canonical")}
entity_kind: {entry.get("entity_kind", "individual")}

[[SECTION identity_markdown]]
display_name: <display name>
aliases:
- alias 1
- alias 2
chapter_mentions:
- CH001
- CH010
[[/SECTION]]

[[SECTION visual_markdown]]
identity_baseline: <short stable identity read or unknown>
age_presence: <broad visual age read or unknown>
physical_build: <body type/frame read or unknown>
origin_or_historical_context: <setting or era cue or unknown>
movement_language: <movement or posture read or unknown>
costume_signature: <short costume note or unknown>
distinguishing_features:
- feature 1
- feature 2
state_variants:
- variant 1
- variant 2
stable_visual_summary: <one grounded paragraph>
physical_traits:
- trait 1
- trait 2
[[/SECTION]]

[[SECTION behavioral_markdown]]
personality: <grounded personality note or unknown>
role: <role note or unknown>
voice_notes: <voice note or unknown>
relationship_notes:
- relation note 1
- relation note 2
[[/SECTION]]

[[SECTION continuity_markdown]]
continuity_constraints:
- continuity constraint 1
- continuity constraint 2
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
        return _parse_character_bible_packet(text, entry)
    except Exception:
        return None


def _parse_character_bible_packet(text: str, entry: dict[str, Any]) -> dict[str, Any]:
    packet = parse_packet_document(text, expected_task="character_bible_synthesis")
    if not packet.records:
        raise ValueError("LLM response did not contain a character bible record.")

    record = packet.records[0]
    fields = record.fields
    sections = record.sections

    identity_scalars, identity_lists, identity_freeform = _parse_bible_markdown_section(sections.get("identity_markdown", ""))
    visual_scalars, visual_lists, visual_freeform = _parse_bible_markdown_section(sections.get("visual_markdown", ""))
    behavioral_scalars, behavioral_lists, behavioral_freeform = _parse_bible_markdown_section(sections.get("behavioral_markdown", ""))
    continuity_scalars, continuity_lists, continuity_freeform = _parse_bible_markdown_section(sections.get("continuity_markdown", ""))
    evidence_scalars, evidence_lists, evidence_freeform = _parse_bible_markdown_section(sections.get("evidence_markdown", ""))

    display_name = _first_nonempty(
        identity_scalars.get("display_name"),
        fields.get("display_name"),
        entry.get("display_name"),
        entry.get("canonical_id"),
        fallback=str(entry.get("canonical_id") or ""),
    )

    aliases = _coerce_string_list(identity_lists.get("aliases"), identity_scalars.get("aliases"))
    chapter_mentions = _coerce_string_list(identity_lists.get("chapter_mentions"), identity_scalars.get("chapter_mentions"))
    identity_baseline = _first_nonempty(visual_scalars.get("identity_baseline"), fallback="unknown")
    age_presence = _first_nonempty(visual_scalars.get("age_presence"), fallback="unknown")
    physical_build = _first_nonempty(visual_scalars.get("physical_build"), fallback="unknown")
    origin_or_historical_context = _first_nonempty(visual_scalars.get("origin_or_historical_context"), fallback="unknown")
    movement_language = _first_nonempty(visual_scalars.get("movement_language"), fallback="unknown")
    physical_traits = _coerce_string_list(visual_lists.get("physical_traits"), visual_scalars.get("physical_traits"))
    distinguishing_features = _coerce_string_list(visual_lists.get("distinguishing_features"), visual_scalars.get("distinguishing_features"))
    state_variants = _coerce_string_list(visual_lists.get("state_variants"), visual_scalars.get("state_variants"))
    relationship_notes = _coerce_string_list(behavioral_lists.get("relationship_notes"), behavioral_scalars.get("relationship_notes"))
    continuity_constraints = _coerce_string_list(continuity_lists.get("continuity_constraints"), continuity_scalars.get("continuity_constraints"))
    unresolved_ambiguities = _coerce_string_list(continuity_lists.get("unresolved_ambiguities"), continuity_scalars.get("unresolved_ambiguities"))
    evidence_summary = _coerce_string_list(evidence_lists.get("evidence_markdown"), evidence_scalars.get("evidence_markdown"))
    if not evidence_summary:
        evidence_summary = list(evidence_freeform)

    stable_visual_summary = _first_nonempty(
        visual_scalars.get("stable_visual_summary"),
        visual_freeform[0] if visual_freeform else None,
        fallback="",
    )
    costume_signature = _first_nonempty(visual_scalars.get("costume_signature"), fallback="Unknown")
    personality = _first_nonempty(
        behavioral_scalars.get("personality"),
        behavioral_freeform[0] if behavioral_freeform else None,
        fallback="Insufficient evidence to determine personality.",
    )
    role = _first_nonempty(behavioral_scalars.get("role"), fallback=entry.get("entity_kind", "Unknown"))
    voice_notes = _first_nonempty(behavioral_scalars.get("voice_notes"), fallback="No vocal data available.")

    return {
        "display_name": display_name,
        "identity_baseline": identity_baseline,
        "age_presence": age_presence,
        "physical_build": physical_build,
        "origin_or_historical_context": origin_or_historical_context,
        "movement_language": movement_language,
        "stable_visual_summary": stable_visual_summary,
        "physical_traits": physical_traits,
        "costume_signature": costume_signature,
        "distinguishing_features": distinguishing_features,
        "state_variants": state_variants,
        "personality": personality,
        "role": role,
        "voice_notes": voice_notes,
        "relationship_notes": relationship_notes,
        "continuity_constraints": continuity_constraints,
        "unresolved_ambiguities": unresolved_ambiguities,
        "evidence_summary": evidence_summary[:25],
    }


_CHARACTER_PATCHABLE_SCALAR_FIELDS = {
    "display_name",
    "identity_baseline",
    "age_presence",
    "physical_build",
    "origin_or_historical_context",
    "movement_language",
    "stable_visual_summary",
    "costume_signature",
    "personality",
    "role",
    "voice_notes",
}

_CHARACTER_PATCHABLE_LIST_FIELDS = {
    "aliases",
    "chapter_mentions",
    "physical_traits",
    "distinguishing_features",
    "state_variants",
    "relationship_notes",
    "continuity_constraints",
    "unresolved_ambiguities",
}


def _apply_locked_and_manual_overrides(merged: dict[str, Any], existing: dict | None, metadata: CharacterBibleMetadata) -> dict[str, Any]:
    if existing:
        for field_name, locked in metadata.locked_fields.items():
            if locked and field_name in existing:
                merged[field_name] = existing[field_name]

    for field_name, value in metadata.manual_overrides.items():
        merged[field_name] = value

    return merged


def _merge_with_existing(new: dict[str, Any], existing: dict | None, metadata: CharacterBibleMetadata) -> dict[str, Any]:
    merged = dict(new)
    return _apply_locked_and_manual_overrides(merged, existing, metadata)


def _character_patch_prompt(entry: dict[str, Any], existing: dict[str, Any], evidence_summary: list[str], focus_fields: list[str]) -> str:
    list_fields = sorted(field for field in focus_fields if field in _CHARACTER_PATCHABLE_LIST_FIELDS)
    scalar_fields = sorted(field for field in focus_fields if field in _CHARACTER_PATCHABLE_SCALAR_FIELDS and field not in _CHARACTER_PATCHABLE_LIST_FIELDS)
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
            "identity_baseline",
            "age_presence",
            "physical_build",
            "origin_or_historical_context",
            "movement_language",
            "stable_visual_summary",
            "physical_traits",
            "costume_signature",
            "distinguishing_features",
            "state_variants",
            "personality",
            "role",
            "voice_notes",
            "relationship_notes",
            "continuity_constraints",
            "unresolved_ambiguities",
            "chapter_mentions",
        ]
    }

    return f"""
Patch the provided character bible by updating only the requested weak fields.

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
task: character_bible_patch
version: 1

[[FILMCREATOR_RECORD]]
type: character_bible
artifact_id: CHAR_{entry.get("canonical_id") or entry.get("display_name") or ""}
character_id: {entry.get("canonical_id") or entry.get("display_name") or ""}
status: {entry.get("status", "canonical")}
entity_kind: {entry.get("entity_kind", "individual")}

[[SECTION patch_markdown]]
{chr(10).join(field_lines) if field_lines else "(no changes requested)"}
[[/SECTION]]

[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
"""


def _parse_character_bible_patch_packet(text: str, entry: dict[str, Any], focus_fields: list[str]) -> dict[str, Any]:
    packet = parse_packet_document(text, expected_task="character_bible_patch")
    if not packet.records:
        raise ValueError("LLM response did not contain a character bible patch record.")

    record = packet.records[0]
    sections = record.sections
    scalars, lists, freeform = _parse_bible_markdown_section(sections.get("patch_markdown", ""))

    patch: dict[str, Any] = {}
    for field_name in focus_fields:
        if field_name in _CHARACTER_PATCHABLE_LIST_FIELDS:
            values = _coerce_string_list(lists.get(field_name), scalars.get(field_name))
            if values:
                patch[field_name] = values
            continue
        if field_name in _CHARACTER_PATCHABLE_SCALAR_FIELDS:
            value = _first_nonempty(scalars.get(field_name), fallback="")
            if not value and freeform and field_name == "stable_visual_summary":
                value = freeform[0]
            if value and value.lower() not in {"unknown", "(none)", "none", "n/a"}:
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


def _apply_character_patch(existing: dict[str, Any], patch: dict[str, Any], metadata: CharacterBibleMetadata, focus_fields: list[str]) -> dict[str, Any]:
    merged = dict(existing)
    for field_name in focus_fields:
        if field_name not in patch:
            continue
        value = patch[field_name]
        if field_name in _CHARACTER_PATCHABLE_LIST_FIELDS:
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


def _llm_patch_synthesis(entry: dict, existing: dict[str, Any], evidence_summary: list[str], focus_fields: list[str]) -> dict[str, Any] | None:
    if not focus_fields:
        return None

    settings = load_runtime_settings()
    client = LMStudioClient(settings)
    user = _character_patch_prompt(entry, existing, evidence_summary, focus_fields)
    system = (
        "You are a film character bible patching system. "
        "Only update the requested weak fields. "
        "Preserve existing good fields exactly. "
        "Use only the provided evidence and artifact context. "
        "Return one tagged FilmCreator markdown packet only. "
        "Do not return JSON."
    )

    try:
        text = client.chat_completion(system_prompt=system, user_prompt=user, temperature=0.1)
        return _parse_character_bible_patch_packet(text, entry, focus_fields)
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
            if "," in stripped:
                for item in stripped.split(","):
                    item = item.strip()
                    if item and item.lower() not in {"none", "(none)", "n/a"}:
                        items.append(item)
            else:
                items.append(stripped)

    seen: set[str] = set()
    deduped: list[str] = []
    for item in items:
        if item not in seen:
            seen.add(item)
            deduped.append(item)
    return deduped


def _evidence_query_terms(entry: dict[str, Any]) -> list[str]:
    terms: list[str] = []
    for value in [entry.get("canonical_id"), entry.get("display_name"), *entry.get("aliases", [])]:
        if isinstance(value, str):
            normalized = " ".join(value.replace("_", " ").split()).strip()
            if normalized and normalized not in terms:
                terms.append(normalized)
    return terms[:4]


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



def _write_fallback_diagnostics_markdown(path: Path, diagnostics: list[dict[str, Any]], project_slug: str) -> None:
    lines = [
        f"# Character Bible Fallback Diagnostics",
        f"",
        f"**Project:** {project_slug}",
        f"**Total Records:** {len(diagnostics)}",
        f"**Attempted:** {sum(1 for item in diagnostics if item['fallback_attempted'])}",
        f"**Non-Empty:** {sum(1 for item in diagnostics if item['fallback_result_audit']['non_empty'])}",
        f"",
        f"| Character | Missing | Attempted | Bucket | Filled | Status | Preview |",
        f"|-----------|---------|-----------|--------|--------|--------|---------|",
    ]
    
    for item in diagnostics:
        char_id = item["character_id"]
        missing = item["pre_fallback_audit"]["missing_count"]
        total = item["pre_fallback_audit"]["total_prompt_critical_fields"]
        attempted = "yes" if item["fallback_attempted"] else "no"
        bucket = item["fallback_result_audit"].get("fallback_bucket") or "none"
        filled = item["fallback_result_audit"]["filled_count"]
        filled_total = filled + item["fallback_result_audit"]["empty_count"]
        status = item["fallback_result_audit"].get("status") or "none"
        preview = item["fallback_preview"].get("production_body_descriptor") or item["fallback_preview"].get("production_identity_descriptor") or ""
        preview = preview[:60] + "..." if len(preview) > 60 else preview
        
        lines.append(f"| {char_id} | {missing}/{total} | {attempted} | {bucket} | {filled}/{filled_total} | {status} | {preview} |")
    
    path.write_text("\n".join(lines), encoding="utf-8")


def _load_existing_metadata(existing: dict | None, artifact_id: str, fp: str) -> CharacterBibleMetadata:
    old_meta = (existing or {}).get("metadata") or {}
    return CharacterBibleMetadata(
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


def _load_registry_for_synthesis(project_dir: Path, project_slug: str) -> tuple[dict[str, Any], Path]:
    refined_path = project_dir / "02_story_analysis" / "world" / "refinement" / "CHARACTER_REGISTRY_GLOBAL_REFINED.json"
    canonical_path = global_character_registry_path(project_slug)

    if refined_path.exists():
        return (read_json(refined_path), refined_path)
    if canonical_path.exists():
        return (read_json(canonical_path), canonical_path)
    return ({}, canonical_path)


def _is_film_facing_character(entry: dict[str, Any], bible: CharacterBible | None = None) -> bool:
    if entry.get("status") != "canonical":
        return False
    if entry.get("entity_kind") != "individual":
        return False
    return True


def _write_json_and_markdown(base_path: Path, bible: CharacterBible) -> None:
    write_json(base_path.with_suffix(".json"), bible.to_dict())
    write_character_bible_markdown(base_path.with_suffix(".md"), bible)


def run_character_bible_synthesis(
    project_slug: str,
    *,
    use_llm: bool = True,
    force: bool = False,
    limit: int | None = None,
) -> CharacterBibleSynthesisSummary:
    project_dir = create_project(project_slug)

    registry, registry_path = _load_registry_for_synthesis(project_dir, project_slug)

    output_dir = project_dir / "02_story_analysis" / "bibles" / "characters"
    review_dir = output_dir / "review"
    output_dir.mkdir(parents=True, exist_ok=True)
    review_dir.mkdir(parents=True, exist_ok=True)

    synthesized = 0
    reused = 0
    stale_locked = 0
    review_queue: list[dict[str, Any]] = []
    written_files: list[str] = []
    warnings: list[str] = []
    bible_records: list[CharacterBible] = []
    review_records: list[CharacterBible] = []
    fallback_diagnostics: list[dict[str, Any]] = []

    registry_items = list(registry.items())
    if limit is not None and limit >= 0:
        registry_items = registry_items[:limit]
    total_entries = len(registry_items)

    for index, (char_id, entry) in enumerate(registry_items, start=1):
        started_at = time.perf_counter()
        print(f"[character-bible] {index}/{total_entries} starting {char_id}...")
        fp = _fingerprint(entry)
        base_path = output_dir / f"CHAR_{char_id}"
        existing = read_json(base_path.with_suffix(".json")) if base_path.with_suffix(".json").exists() else None
        metadata = _load_existing_metadata(existing, artifact_id=f"CHAR_{char_id}", fp=fp)

        if existing and not force:
            old_meta = existing.get("metadata") or {}
            if old_meta.get("source_fingerprint") == fp:
                reused += 1
                bible = CharacterBible(
                    character_id=existing.get("character_id", char_id),
                    display_name=existing.get("display_name", char_id),
                    aliases=existing.get("aliases", []),
                    status=existing.get("status", "canonical"),
                    entity_kind=existing.get("entity_kind", "individual"),
                    first_seen_chapter=existing.get("first_seen_chapter"),
                    last_seen_chapter=existing.get("last_seen_chapter"),
                    chapter_mentions=existing.get("chapter_mentions", []),
                    identity_baseline=existing.get("identity_baseline", ""),
                    age_presence=existing.get("age_presence", ""),
                    physical_build=existing.get("physical_build", ""),
                    origin_or_historical_context=existing.get("origin_or_historical_context", ""),
                    movement_language=existing.get("movement_language", ""),
                    stable_visual_summary=existing.get("stable_visual_summary", ""),
                    physical_traits=existing.get("physical_traits", []),
                    costume_signature=existing.get("costume_signature", ""),
                    distinguishing_features=existing.get("distinguishing_features", []),
                    state_variants=existing.get("state_variants", []),
                    personality=existing.get("personality", ""),
                    role=existing.get("role", ""),
                    voice_notes=existing.get("voice_notes", ""),
                    relationship_notes=existing.get("relationship_notes", []),
                    continuity_constraints=existing.get("continuity_constraints", []),
                    unresolved_ambiguities=existing.get("unresolved_ambiguities", []),
                    entity_taxonomy=existing.get("entity_taxonomy", {}),
                    alias_resolution=existing.get("alias_resolution", {}),
                    associated_entities=existing.get("associated_entities", []),
                    evidence_refs=existing.get("evidence_refs", []),
                    evidence_summary=existing.get("evidence_summary", []),
                    metadata=metadata,
                )
                bible_records.append(bible)
                if not _is_film_facing_character(entry, bible) or bible.unresolved_ambiguities:
                    review_records.append(bible)
                elapsed = round(time.perf_counter() - started_at, 1)
                print(f"[character-bible] {index}/{total_entries} finished {char_id} (reused) in {elapsed}s")
                continue

            if old_meta.get("status") == "locked":
                stale_locked += 1
                existing["metadata"]["status"] = "stale"
                write_json(base_path.with_suffix(".json"), existing)
                warnings.append(f"Locked character bible became stale and was not regenerated: {char_id}")
                elapsed = round(time.perf_counter() - started_at, 1)
                print(f"[character-bible] {index}/{total_entries} finished {char_id} (stale locked) in {elapsed}s")
                continue

        evidence_summary, evidence_refs = _collect_evidence(project_slug, entry)
        
        # Load taxonomy artifact if present
        taxonomy_artifact_path = project_dir / "02_story_analysis" / "taxonomy" / "characters" / f"CHAR_{char_id}_TAXONOMY.json"
        taxonomy_data = {}
        alias_resolution_data = {}
        associated_entities_data = []
        
        if taxonomy_artifact_path.exists():
            try:
                taxonomy_artifact = read_json(taxonomy_artifact_path)
                taxonomy_data = {
                    "character_id": taxonomy_artifact.get("character_id"),
                    "primary_type": taxonomy_artifact.get("primary_type"),
                    "morphology": taxonomy_artifact.get("morphology"),
                    "scale": taxonomy_artifact.get("scale"),
                    "sentience": taxonomy_artifact.get("sentience"),
                    "renderability": taxonomy_artifact.get("renderability"),
                    "confidence": taxonomy_artifact.get("confidence"),
                    "needs_review": taxonomy_artifact.get("needs_review"),
                }
                alias_resolution_data = taxonomy_artifact.get("alias_resolution", {})
                # Extract associated evidence
                assoc_evidence = taxonomy_artifact.get("associated_evidence", [])
                if assoc_evidence:
                    associated_entities_data = [{"evidence": e} for e in assoc_evidence]
                
                # Add taxonomy to upstream dependencies
                metadata.upstream_dependencies.append({
                    "dependency_type": "character_taxonomy",
                    "dependency_id": char_id,
                    "source_path": str(taxonomy_artifact_path),
                })
            except Exception:
                warnings.append(f"Failed to load taxonomy artifact for {char_id}")
        else:
            warnings.append(f"Taxonomy artifact missing for {char_id}")
        
        synthesized_payload = _llm_synthesis(entry, evidence_summary) if use_llm else None
        if not synthesized_payload:
            synthesized_payload = _deterministic_synthesis(entry, evidence_summary)
            if use_llm:
                warnings.append(f"LLM synthesis failed or returned invalid JSON for {char_id}; used deterministic fallback.")

        merged = _merge_with_existing(synthesized_payload, existing, metadata)

        # Add taxonomy to merged BEFORE fallback so fallback can read it
        if taxonomy_data:
            merged["entity_taxonomy"] = taxonomy_data
        if alias_resolution_data:
            merged["alias_resolution"] = alias_resolution_data
        if associated_entities_data:
            merged["associated_entities"] = associated_entities_data

        # Audit visual fields before fallback
        pre_fallback_audit = visual_field_audit(merged)
        missing_fields = pre_fallback_audit["missing_fields"]

        print(
            f"[character-bible] {char_id} visual audit: "
            f"missing={pre_fallback_audit['missing_count']}/"
            f"{pre_fallback_audit['total_prompt_critical_fields']} "
            f"fields: {', '.join(missing_fields) if missing_fields else 'none'}"
        )

        fallback_attempted = False
        fallback_method = "none"
        fallback_reason = "not_needed"
        fallback = merged.get("visual_production_fallback") or {}

        if pre_fallback_audit["needs_visual_production_fallback"]:
            fallback_attempted = True
            fallback_method = "deterministic"
            fallback_reason = "missing_prompt_critical_fields"
            fallback = deterministic_visual_fallback(entry, merged, evidence_summary)
            merged["visual_production_fallback"] = fallback
        else:
            merged["visual_production_fallback"] = {}

        post_fallback_audit = fallback_result_audit(merged.get("visual_production_fallback") or {})

        print(
            f"[character-bible] {char_id} fallback: "
            f"attempted={'yes' if fallback_attempted else 'no'} "
            f"reason={fallback_reason} "
            f"bucket={post_fallback_audit.get('fallback_bucket') or 'none'} "
            f"method={fallback_method} "
            f"filled={post_fallback_audit['filled_count']}/"
            f"{post_fallback_audit['filled_count'] + post_fallback_audit['empty_count']} "
            f"status={post_fallback_audit.get('status') or 'none'}"
        )

        preview = ""
        if isinstance(fallback, dict):
            preview = str(
                fallback.get("production_body_descriptor")
                or fallback.get("production_identity_descriptor")
                or ""
            ).strip()
        if preview:
            print(f"[character-bible] {char_id} fallback preview: {preview[:180]}")

        fallback_diagnostics.append({
            "character_id": char_id,
            "display_name": merged.get("display_name"),
            "entity_kind": entry.get("entity_kind"),
            "first_seen_chapter": entry.get("first_seen_chapter"),
            "chapter_mentions": entry.get("chapter_mentions", []),
            "synthesis_mode": "reused" if existing and not force else "synthesized",
            "pre_fallback_audit": pre_fallback_audit,
            "fallback_attempted": fallback_attempted,
            "fallback_method": fallback_method,
            "fallback_reason": fallback_reason,
            "fallback_result_audit": post_fallback_audit,
            "fallback_preview": {
                "production_identity_descriptor": fallback.get("production_identity_descriptor") if isinstance(fallback, dict) else "",
                "production_body_descriptor": fallback.get("production_body_descriptor") if isinstance(fallback, dict) else "",
                "production_costume_descriptor": fallback.get("production_costume_descriptor") if isinstance(fallback, dict) else "",
                "production_silhouette": fallback.get("production_silhouette") if isinstance(fallback, dict) else "",
            },
            "evidence_summary": evidence_summary[:5],
        })


        metadata.upstream_dependencies = [
            {
                "dependency_type": "character_registry_entry",
                "dependency_id": char_id,
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

        bible = CharacterBible(
            character_id=char_id,
            display_name=merged.get("display_name") or entry.get("display_name") or char_id,
            aliases=entry.get("aliases", []),
            status=entry.get("status", "canonical"),
            entity_kind=entry.get("entity_kind", "individual"),
            first_seen_chapter=entry.get("first_seen_chapter"),
            last_seen_chapter=entry.get("last_seen_chapter"),
            chapter_mentions=entry.get("chapter_mentions", []),
            identity_baseline=merged.get("identity_baseline", ""),
            age_presence=merged.get("age_presence", ""),
            physical_build=merged.get("physical_build", ""),
            origin_or_historical_context=merged.get("origin_or_historical_context", ""),
            movement_language=merged.get("movement_language", ""),
            stable_visual_summary=merged.get("stable_visual_summary", ""),
            physical_traits=merged.get("physical_traits", []),
            costume_signature=merged.get("costume_signature", ""),
            distinguishing_features=merged.get("distinguishing_features", []),
            state_variants=merged.get("state_variants", []),
            personality=merged.get("personality", ""),
            role=merged.get("role", ""),
            voice_notes=merged.get("voice_notes", ""),
            relationship_notes=merged.get("relationship_notes", []),
            continuity_constraints=merged.get("continuity_constraints", []),
            unresolved_ambiguities=merged.get("unresolved_ambiguities", []),
            entity_taxonomy=taxonomy_data,
            alias_resolution=alias_resolution_data,
            associated_entities=associated_entities_data,
            evidence_refs=evidence_refs,
            evidence_summary=evidence_summary,
            visual_production_fallback=merged.get("visual_production_fallback", {}),
            metadata=metadata,
        )

        _write_json_and_markdown(base_path, bible)
        written_files.extend([str(base_path.with_suffix(".json")), str(base_path.with_suffix(".md"))])
        synthesized += 1
        bible_records.append(bible)

        if not _is_film_facing_character(entry, bible) or bible.unresolved_ambiguities:
            review_records.append(bible)

        if bible.unresolved_ambiguities:
            review_queue.append(
                {
                    "character_id": char_id,
                    "issues": bible.unresolved_ambiguities,
                }
            )

        elapsed = round(time.perf_counter() - started_at, 1)
        mode = "synthesized" if synthesized_payload else "generated"
        print(f"[character-bible] {index}/{total_entries} finished {char_id} ({mode}) in {elapsed}s")

    write_json(review_dir / "CHARACTER_BIBLE_REVIEW_QUEUE.json", review_queue)
    write_character_review_queue_markdown(review_dir / "CHARACTER_BIBLE_REVIEW_QUEUE.md", review_queue)
    
    # Write fallback diagnostics
    diagnostics_path = review_dir / "CHARACTER_BIBLE_FALLBACK_DIAGNOSTICS.json"
    write_json(diagnostics_path, {
        "project_slug": project_slug,
        "generated_at_utc": _utc_now(),
        "total_records": len(fallback_diagnostics),
        "attempted_count": sum(1 for item in fallback_diagnostics if item["fallback_attempted"]),
        "non_empty_count": sum(1 for item in fallback_diagnostics if item["fallback_result_audit"]["non_empty"]),
        "records": fallback_diagnostics,
    })
    written_files.append(str(diagnostics_path))
    
    # Write fallback diagnostics markdown
    _write_fallback_diagnostics_markdown(review_dir / "CHARACTER_BIBLE_FALLBACK_DIAGNOSTICS.md", fallback_diagnostics, project_slug)
    written_files.append(str(review_dir / "CHARACTER_BIBLE_FALLBACK_DIAGNOSTICS.md"))
    
    main_records = [record for record in bible_records if _is_film_facing_character(entry=registry.get(record.character_id, {}), bible=record)]
    write_character_bible_index(output_dir / "CHARACTER_BIBLE_INDEX.md", main_records)
    write_character_bible_review_index(output_dir / "CHARACTER_BIBLE_REVIEW_INDEX.md", review_records)
    write_json(
        output_dir / "CHARACTER_BIBLE_INDEX.json",
        [record.to_dict() for record in sorted(main_records, key=lambda item: item.character_id)],
    )
    write_json(
        output_dir / "CHARACTER_BIBLE_REVIEW_INDEX.json",
        [record.to_dict() for record in sorted(review_records, key=lambda item: item.character_id)],
    )

    written_files.extend(
        [
            str(review_dir / "CHARACTER_BIBLE_REVIEW_QUEUE.json"),
            str(review_dir / "CHARACTER_BIBLE_REVIEW_QUEUE.md"),
            str(output_dir / "CHARACTER_BIBLE_INDEX.md"),
            str(output_dir / "CHARACTER_BIBLE_INDEX.json"),
            str(output_dir / "CHARACTER_BIBLE_REVIEW_INDEX.md"),
            str(output_dir / "CHARACTER_BIBLE_REVIEW_INDEX.json"),
        ]
    )

    return CharacterBibleSynthesisSummary(
        project_slug=project_slug,
        total_registry_entries=len(registry),
        synthesized_count=synthesized,
        reused_count=reused,
        stale_locked_count=stale_locked,
        review_queue_count=len(review_queue),
        written_files=written_files,
        warnings=warnings,
    )


def run_character_bible_patch_reruns(
    project_slug: str,
    queue_items: list[dict[str, Any]],
    *,
    use_llm: bool = True,
) -> CharacterBibleSynthesisSummary:
    project_dir = create_project(project_slug)
    registry, _ = _load_registry_for_synthesis(project_dir, project_slug)

    output_dir = project_dir / "02_story_analysis" / "bibles" / "characters"
    review_dir = output_dir / "review"
    output_dir.mkdir(parents=True, exist_ok=True)
    review_dir.mkdir(parents=True, exist_ok=True)

    patched = 0
    skipped = 0
    stale_locked = 0
    review_queue: list[dict[str, Any]] = []
    written_files: list[str] = []
    warnings: list[str] = []
    bible_records: list[CharacterBible] = []
    review_records: list[CharacterBible] = []
    fallback_diagnostics: list[dict[str, Any]] = []

    character_items = [item for item in queue_items if str(item.get("family", "")).strip() == "character_bible"]
    total_items = len(character_items)

    for index, item in enumerate(character_items, start=1):
        artifact_id = str(item.get("artifact_id") or item.get("display_name") or "").strip()
        char_id = artifact_id
        focus_fields = [str(field).strip() for field in item.get("focus_fields", []) if str(field).strip() in _CHARACTER_PATCHABLE_SCALAR_FIELDS or str(field).strip() in _CHARACTER_PATCHABLE_LIST_FIELDS]
        if not char_id or not focus_fields:
            skipped += 1
            continue

        started_at = time.perf_counter()
        print(f"[character-bible] patch {index}/{total_items} starting {char_id} ({', '.join(focus_fields)})...")
        entry = registry.get(char_id)
        if not isinstance(entry, dict):
            warnings.append(f"Character registry entry not found for patch rerun: {char_id}")
            skipped += 1
            elapsed = round(time.perf_counter() - started_at, 1)
            print(f"[character-bible] patch {index}/{total_items} finished {char_id} (missing registry entry) in {elapsed}s")
            continue

        fp = _fingerprint(entry)
        base_path = output_dir / f"CHAR_{char_id}"
        existing = read_json(base_path.with_suffix(".json")) if base_path.with_suffix(".json").exists() else None
        if not isinstance(existing, dict):
            warnings.append(f"Character bible missing for patch rerun: {char_id}")
            skipped += 1
            elapsed = round(time.perf_counter() - started_at, 1)
            print(f"[character-bible] patch {index}/{total_items} finished {char_id} (missing bible) in {elapsed}s")
            continue

        old_meta = existing.get("metadata") or {}
        if old_meta.get("status") == "locked":
            stale_locked += 1
            existing["metadata"]["status"] = "stale"
            write_json(base_path.with_suffix(".json"), existing)
            warnings.append(f"Locked character bible became stale and was not patched: {char_id}")
            elapsed = round(time.perf_counter() - started_at, 1)
            print(f"[character-bible] patch {index}/{total_items} finished {char_id} (stale locked) in {elapsed}s")
            continue

        metadata = _load_existing_metadata(existing, artifact_id=f"CHAR_{char_id}", fp=fp)
        evidence_summary, evidence_refs = _collect_evidence(project_slug, entry)
        patch_payload = _llm_patch_synthesis(entry, existing, evidence_summary, focus_fields) if use_llm else None
        if not patch_payload:
            patch_payload = {}
            if use_llm:
                warnings.append(f"LLM patch synthesis failed or returned invalid output for {char_id}; existing values were preserved.")

        merged = _apply_character_patch(existing, patch_payload, metadata, focus_fields)
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
                "dependency_type": "character_registry_entry",
                "dependency_id": char_id,
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

        bible = CharacterBible(
            character_id=char_id,
            display_name=merged.get("display_name") or entry.get("display_name") or char_id,
            aliases=merged.get("aliases") if isinstance(merged.get("aliases"), list) else entry.get("aliases", []),
            status=merged.get("status", entry.get("status", "canonical")),
            entity_kind=merged.get("entity_kind", entry.get("entity_kind", "individual")),
            first_seen_chapter=merged.get("first_seen_chapter") or entry.get("first_seen_chapter"),
            last_seen_chapter=merged.get("last_seen_chapter") or entry.get("last_seen_chapter"),
            chapter_mentions=merged.get("chapter_mentions") if isinstance(merged.get("chapter_mentions"), list) else entry.get("chapter_mentions", []),
            identity_baseline=merged.get("identity_baseline", ""),
            age_presence=merged.get("age_presence", ""),
            physical_build=merged.get("physical_build", ""),
            origin_or_historical_context=merged.get("origin_or_historical_context", ""),
            movement_language=merged.get("movement_language", ""),
            stable_visual_summary=merged.get("stable_visual_summary", ""),
            physical_traits=merged.get("physical_traits", []),
            costume_signature=merged.get("costume_signature", ""),
            distinguishing_features=merged.get("distinguishing_features", []),
            state_variants=merged.get("state_variants", []),
            personality=merged.get("personality", ""),
            role=merged.get("role", ""),
            voice_notes=merged.get("voice_notes", ""),
            relationship_notes=merged.get("relationship_notes", []),
            continuity_constraints=merged.get("continuity_constraints", []),
            unresolved_ambiguities=merged.get("unresolved_ambiguities", []),
            evidence_refs=merged_evidence_refs or existing_evidence_refs,
            evidence_summary=merged_evidence_summary or existing_evidence_summary,
            metadata=metadata,
        )

        _write_json_and_markdown(base_path, bible)
        written_files.extend([str(base_path.with_suffix(".json")), str(base_path.with_suffix(".md"))])
        patched += 1
        bible_records.append(bible)

        if not _is_film_facing_character(entry, bible) or bible.unresolved_ambiguities:
            review_records.append(bible)
        if bible.unresolved_ambiguities:
            review_queue.append({"character_id": char_id, "issues": bible.unresolved_ambiguities})

        elapsed = round(time.perf_counter() - started_at, 1)
        print(f"[character-bible] patch {index}/{total_items} finished {char_id} (patched) in {elapsed}s")

    write_json(review_dir / "CHARACTER_BIBLE_REVIEW_QUEUE.json", review_queue)
    write_character_review_queue_markdown(review_dir / "CHARACTER_BIBLE_REVIEW_QUEUE.md", review_queue)
    
    # Write fallback diagnostics
    diagnostics_path = review_dir / "CHARACTER_BIBLE_FALLBACK_DIAGNOSTICS.json"
    write_json(diagnostics_path, {
        "project_slug": project_slug,
        "generated_at_utc": _utc_now(),
        "total_records": len(fallback_diagnostics),
        "attempted_count": sum(1 for item in fallback_diagnostics if item["fallback_attempted"]),
        "non_empty_count": sum(1 for item in fallback_diagnostics if item["fallback_result_audit"]["non_empty"]),
        "records": fallback_diagnostics,
    })
    written_files.append(str(diagnostics_path))
    
    # Write fallback diagnostics markdown
    _write_fallback_diagnostics_markdown(review_dir / "CHARACTER_BIBLE_FALLBACK_DIAGNOSTICS.md", fallback_diagnostics, project_slug)
    written_files.append(str(review_dir / "CHARACTER_BIBLE_FALLBACK_DIAGNOSTICS.md"))
    
    main_records = [record for record in bible_records if _is_film_facing_character(entry=registry.get(record.character_id, {}), bible=record)]
    write_character_bible_index(output_dir / "CHARACTER_BIBLE_INDEX.md", main_records)
    write_character_bible_review_index(output_dir / "CHARACTER_BIBLE_REVIEW_INDEX.md", review_records)
    write_json(
        output_dir / "CHARACTER_BIBLE_INDEX.json",
        [record.to_dict() for record in sorted(main_records, key=lambda item: item.character_id)],
    )
    write_json(
        output_dir / "CHARACTER_BIBLE_REVIEW_INDEX.json",
        [record.to_dict() for record in sorted(review_records, key=lambda item: item.character_id)],
    )

    written_files.extend(
        [
            str(review_dir / "CHARACTER_BIBLE_REVIEW_QUEUE.json"),
            str(review_dir / "CHARACTER_BIBLE_REVIEW_QUEUE.md"),
            str(output_dir / "CHARACTER_BIBLE_INDEX.md"),
            str(output_dir / "CHARACTER_BIBLE_INDEX.json"),
            str(output_dir / "CHARACTER_BIBLE_REVIEW_INDEX.md"),
            str(output_dir / "CHARACTER_BIBLE_REVIEW_INDEX.json"),
        ]
    )

    return CharacterBibleSynthesisSummary(
        project_slug=project_slug,
        total_registry_entries=len(registry),
        synthesized_count=patched,
        reused_count=skipped,
        stale_locked_count=stale_locked,
        review_queue_count=len(review_queue),
        written_files=written_files,
        warnings=warnings,
    )
