from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path

from ...core.paths import ensure_dir, repo_relative
from ...core.validation import validate_clip_id, validate_scene_id
from ...lmstudio_client import LMStudioError
from ...delete_safety import find_project_root, remove_path_within_project

PACKET_START_TAG = "[[FILMCREATOR_PACKET]]"
PACKET_END_TAG = "[[/FILMCREATOR_PACKET]]"
RECORD_START_TAG = "[[FILMCREATOR_RECORD]]"
RECORD_END_TAG = "[[/FILMCREATOR_RECORD]]"
SECTION_END_TAG = "[[/SECTION]]"
SECTION_TAG_PATTERN = re.compile(r"^\[\[SECTION ([a-z0-9_]+)\]\]$", re.IGNORECASE)
PACKET_VERSION = "1"
PREFERRED_SCENE_COUNT = 3
THIN_SCENE_MARKDOWN_THRESHOLD = 240
HEADING_PATTERN = re.compile(r"(?m)^# ([^\r\n]+)\s*$")
INDEX_ENTRY_PATTERN = re.compile(r"(?m)^## ([^\r\n]+)\s*$")
MARKDOWN_TABLE_ROW_PATTERN = re.compile(r"^\|(.+)\|$")
MARKDOWN_TABLE_SEPARATOR_PATTERN = re.compile(r"^\|(?:\s*:?-{3,}:?\s*\|)+\s*$")
CHAPTER_ID_PATTERN = re.compile(r"\b(CH\d{3})\b", re.IGNORECASE)
IMPLICIT_MARKDOWN_FIELD_PATTERN = re.compile(r"^[a-z0-9_]+_markdown:\s*$", re.IGNORECASE)
TOP_LEVEL_FIELD_PATTERN = re.compile(r"^[a-z0-9_]+:\s*$", re.IGNORECASE)
SCENE_ID_PATTERN = re.compile(r"^SC\d{3}$")
CLIP_ID_PATTERN = re.compile(r"^CL\d{3}$")
ASSET_ID_PATTERN = re.compile(r"^[a-z0-9_]+$")


@dataclass(frozen=True)
class ParsedInputsMarkdown:
    items: dict[str, str]
    warnings: list[str]


@dataclass(frozen=True)
class PacketRecord:
    fields: dict[str, str]
    sections: dict[str, str]


@dataclass(frozen=True)
class PacketDocument:
    metadata: dict[str, str]
    sections: dict[str, str]
    records: list[PacketRecord]


def parse_packet_document(response: str, *, expected_task: str | None = None) -> PacketDocument:
    packet_body = extract_packet_body(strip_markdown_fences(response))
    packet = parse_packet_body(packet_body)
    if expected_task is not None:
        actual_task = packet.metadata.get("task", "")
        if actual_task and actual_task != expected_task:
            raise LMStudioError(f"LM Studio returned packet task '{actual_task or '(missing)'}' but expected '{expected_task}'.")
        if not actual_task:
            packet.metadata["task"] = expected_task
    version = packet.metadata.get("version", "")
    if version and version != PACKET_VERSION:
        raise LMStudioError(f"LM Studio returned packet version '{version or '(missing)'}' but expected '{PACKET_VERSION}'.")
    if not version:
        packet.metadata["version"] = PACKET_VERSION
    return packet


def extract_packet_body(response: str) -> str:
    cleaned = sanitize_llm_text(response)
    lines = cleaned.splitlines()
    start_index = next((index for index, line in enumerate(lines) if normalize_structural_packet_tag(line.strip()) == PACKET_START_TAG), -1)
    end_index = next((index for index in range(len(lines) - 1, -1, -1) if normalize_structural_packet_tag(lines[index].strip()) == PACKET_END_TAG), -1)
    if start_index == -1 or end_index == -1 or end_index <= start_index:
        start = cleaned.find(PACKET_START_TAG)
        end = cleaned.rfind(PACKET_END_TAG)
        if start == -1 or end == -1 or end <= start:
            if start_index != -1:
                body_lines = lines[start_index + 1 :]
                while body_lines and not body_lines[-1].strip():
                    body_lines.pop()
                while body_lines and body_lines[-1].strip() == PACKET_START_TAG:
                    body_lines.pop()
                if body_lines:
                    return "\n".join(body_lines).strip()
            raise LMStudioError("LM Studio did not return a FILMCREATOR packet envelope.")
        return cleaned[start + len(PACKET_START_TAG) : end].strip()
    return "\n".join(lines[start_index + 1 : end_index]).strip()


def sanitize_llm_text(text: str) -> str:
    cleaned_chars: list[str] = []
    for ch in text:
        if ch in "\n\r\t":
            cleaned_chars.append(ch)
            continue
        if unicodedata.category(ch) == "Cf":
            continue
        cleaned_chars.append(ch)
    return "".join(cleaned_chars).strip()


def strip_markdown_fences(response: str) -> str:
    cleaned = response.strip()
    if not cleaned.startswith("```"):
        return cleaned
    lines = cleaned.splitlines()
    if lines and lines[0].startswith("```"):
        lines = lines[1:]
    if lines and lines[-1].startswith("```"):
        lines = lines[:-1]
    return "\n".join(lines).strip()


def parse_packet_body(packet_body: str) -> PacketDocument:
    metadata: dict[str, str] = {}
    sections: dict[str, str] = {}
    records: list[PacketRecord] = []
    lines = packet_body.splitlines()
    index = 0
    while index < len(lines):
        stripped = lines[index].strip()
        normalized_tag = normalize_structural_packet_tag(stripped)
        if not stripped:
            index += 1
            continue
        if normalized_tag == SECTION_END_TAG:
            index += 1
            continue
        if normalized_tag == RECORD_START_TAG:
            record_lines, index = collect_tagged_block(lines, index, RECORD_START_TAG, RECORD_END_TAG, fallback_start_tag=RECORD_START_TAG)
            records.append(parse_packet_record(record_lines))
            continue
        section_match = SECTION_TAG_PATTERN.fullmatch(stripped)
        if section_match:
            section_name = section_match.group(1).lower()
            section_lines, index = collect_tagged_block(lines, index, stripped, SECTION_END_TAG, fallback_stop_any_tag=True)
            sections[section_name] = "\n".join(section_lines).strip()
            continue
        key, value = split_packet_key_value(stripped)
        if key.endswith("_markdown") and not value:
            block_lines, index = collect_implicit_markdown_block(lines, index + 1)
            markdown_text = "\n".join(block_lines).strip()
            metadata[key] = markdown_text
            sections.setdefault(key, markdown_text)
            continue
        metadata[key] = value
        index += 1
    return PacketDocument(metadata=metadata, sections=sections, records=records)


def parse_packet_record(record_lines: list[str]) -> PacketRecord:
    fields: dict[str, str] = {}
    sections: dict[str, str] = {}
    index = 0
    while index < len(record_lines):
        stripped = record_lines[index].strip()
        normalized_tag = normalize_structural_packet_tag(stripped)
        if not stripped:
            index += 1
            continue
        if normalized_tag == SECTION_END_TAG:
            index += 1
            continue
        section_match = SECTION_TAG_PATTERN.fullmatch(stripped)
        if section_match:
            section_name = section_match.group(1).lower()
            section_body, index = collect_tagged_block(record_lines, index, stripped, SECTION_END_TAG, fallback_stop_any_tag=True)
            sections[section_name] = "\n".join(section_body).strip()
            continue
        key, value = split_packet_key_value(stripped)
        if key.endswith("_markdown") and not value:
            block_lines, index = collect_implicit_markdown_block(record_lines, index + 1)
            sections[key] = "\n".join(block_lines).strip()
            continue
        fields[key] = value
        index += 1
    record_type = fields.get("type", "")
    if not record_type:
        raise LMStudioError("Packet record is missing required field 'type'.")
    return PacketRecord(fields=fields, sections=sections)


def collect_implicit_markdown_block(lines: list[str], start_index: int) -> tuple[list[str], int]:
    body: list[str] = []
    index = start_index
    while index < len(lines):
        stripped = lines[index].strip()
        normalized_tag = normalize_structural_packet_tag(stripped)
        if not stripped:
            body.append(lines[index])
            index += 1
            continue
        if normalized_tag in {PACKET_START_TAG, PACKET_END_TAG, RECORD_START_TAG, RECORD_END_TAG}:
            break
        if SECTION_TAG_PATTERN.fullmatch(stripped):
            break
        if TOP_LEVEL_FIELD_PATTERN.fullmatch(stripped):
            break
        body.append(lines[index])
        index += 1
    return body, index


def collect_tagged_block(
    lines: list[str],
    start_index: int,
    start_tag: str,
    end_tag: str,
    *,
    fallback_start_tag: str | None = None,
    fallback_stop_any_tag: bool = False,
) -> tuple[list[str], int]:
    if normalize_structural_packet_tag(lines[start_index].strip()) != start_tag:
        raise LMStudioError(f"Expected start tag '{start_tag}' but found '{lines[start_index].strip()}'.")
    body: list[str] = []
    index = start_index + 1
    while index < len(lines):
        stripped = lines[index].strip()
        normalized_tag = normalize_structural_packet_tag(stripped)
        if normalized_tag == end_tag:
            return body, index + 1
        if fallback_start_tag is not None and normalized_tag == fallback_start_tag:
            return body, index
        if fallback_stop_any_tag and is_structural_packet_tag(stripped):
            return body, index
        body.append(lines[index])
        index += 1
    return body, index


def is_structural_packet_tag(stripped: str) -> bool:
    normalized_tag = normalize_structural_packet_tag(stripped)
    return (
        normalized_tag in {PACKET_START_TAG, PACKET_END_TAG, RECORD_START_TAG, RECORD_END_TAG, SECTION_END_TAG}
        or SECTION_TAG_PATTERN.fullmatch(stripped) is not None
    )


def normalize_structural_packet_tag(stripped: str) -> str | None:
    if not stripped.startswith("[[") or not stripped.endswith("]]"):
        return None
    if stripped in {PACKET_START_TAG, PACKET_END_TAG, RECORD_START_TAG, RECORD_END_TAG, SECTION_END_TAG}:
        return stripped
    lowered = stripped.lower()
    if SECTION_TAG_PATTERN.fullmatch(stripped):
        return stripped
    core = lowered[2:-2].strip()
    if core.startswith("section "):
        return None
    if core.startswith("/section") or core in {"end_section", "endsection", "esection"}:
        return SECTION_END_TAG
    normalized_core = re.sub(r"[^a-z/]+", "", core)
    if not normalized_core:
        return None
    is_end = "/" in normalized_core or normalized_core.startswith("end")
    if "section" in normalized_core:
        return SECTION_END_TAG if is_end else None
    if "packet" in normalized_core:
        return PACKET_END_TAG if is_end else PACKET_START_TAG
    if "record" in normalized_core:
        return RECORD_END_TAG if is_end else RECORD_START_TAG
    return None


def clean_section_text(value: str) -> str:
    cleaned = value.strip()
    inline_match = re.fullmatch(r"\[\[SECTION\s+(.*?)\s*\[\[/SECTION\]\]", cleaned, flags=re.DOTALL)
    if inline_match:
        return inline_match.group(1).strip()

    lines = cleaned.splitlines()
    while lines and lines[0].strip() == "[[SECTION":
        lines = lines[1:]
    while lines and lines[-1].strip() == SECTION_END_TAG:
        lines = lines[:-1]
    return "\n".join(lines).strip()


def split_packet_key_value(line: str) -> tuple[str, str]:
    if ":" not in line:
        raise LMStudioError(f"Expected 'key: value' packet line but got '{line}'.")
    key, value = line.split(":", 1)
    normalized_key = key.strip().lower()
    if not normalized_key:
        raise LMStudioError(f"Invalid empty packet key in line '{line}'.")
    return normalized_key, value.strip()


def require_packet_section(packet: PacketDocument, section_name: str, *, allow_empty: bool = False) -> str:
    value = clean_section_text(packet.sections.get(section_name.lower(), ""))
    if not value and not allow_empty:
        raise LMStudioError(f"Packet is missing required section '{section_name}'.")
    return value


def require_packet_records(packet: PacketDocument, *, record_type: str) -> list[PacketRecord]:
    matching_records = [record for record in packet.records if record.fields.get("type") == record_type]
    if not matching_records:
        raise LMStudioError(f"Packet did not contain any '{record_type}' records.")
    return matching_records


def require_single_packet_record(packet: PacketDocument, *, record_type: str) -> PacketRecord:
    records = require_packet_records(packet, record_type=record_type)
    if len(records) != 1:
        raise LMStudioError(f"Packet was expected to contain exactly one '{record_type}' record but found {len(records)}.")
    return records[0]


def require_record_field(record: PacketRecord, field_name: str, *, allow_empty: bool = False) -> str:
    value = record.fields.get(field_name.lower(), "").strip()
    if not value and not allow_empty:
        raise LMStudioError(f"Packet record is missing required field '{field_name}'.")
    return value


def require_record_section(record: PacketRecord, section_name: str, *, allow_empty: bool = False) -> str:
    value = clean_section_text(record.sections.get(section_name.lower(), ""))
    if not value and not allow_empty:
        raise LMStudioError(f"Packet record is missing required section '{section_name}'.")
    return value


def extract_character_records_from_index_markdown(markdown: str) -> list[PacketRecord]:
    records = _extract_table_records(
        markdown,
        record_type="character",
        fallback_prefix="character",
        column_aliases={
            "asset_id": "asset_id",
            "canonical_character_id": "canonical_character_id",
            "canonical_character": "canonical_character_id",
            "aliases": "aliases",
            "fully_identified": "is_fully_identified",
            "is_fully_identified": "is_fully_identified",
            "description": "description",
        },
        default_section_title="Character Index",
    )
    if records:
        return records
    return _extract_heading_block_records(markdown, record_type="character", fallback_prefix="character")


def extract_environment_records_from_index_markdown(markdown: str) -> list[PacketRecord]:
    records = _extract_table_records(
        markdown,
        record_type="environment",
        fallback_prefix="environment",
        column_aliases={
            "asset_id": "asset_id",
            "role": "role",
            "geography": "geography",
            "lighting": "lighting",
            "atmosphere": "atmosphere",
            "scale": "scale",
            "anchors": "anchors",
            "description": "description",
        },
        default_section_title="Environment Index",
    )
    if records:
        return records
    return _extract_heading_block_records(markdown, record_type="environment", fallback_prefix="environment")


def extract_scene_records_from_index_markdown(markdown: str) -> list[PacketRecord]:
    records = _extract_table_records(
        markdown,
        record_type="scene",
        fallback_prefix="scene",
        column_aliases={
            "scene_id": "scene_id",
            "summary": "summary",
            "scene_summary": "summary",
            "purpose": "purpose",
            "scene_purpose": "purpose",
            "description": "summary",
            "emotional_shift": "summary",
        },
        default_section_title="Scene Index",
    )
    if records:
        return records
    return _extract_scene_heading_or_bullet_records(markdown)


def _extract_scene_heading_or_bullet_records(markdown: str) -> list[PacketRecord]:
    records: list[PacketRecord] = []
    lines = markdown.splitlines()
    current_scene_id: str | None = None
    current_lines: list[str] = []

    def flush() -> None:
        nonlocal current_scene_id, current_lines
        if current_scene_id is None:
            return
        fields: dict[str, str] = {
            "type": "scene",
            "scene_id": normalize_scene_id(current_scene_id),
        }
        summary = "\n".join(line.strip() for line in current_lines if line.strip()).strip()
        if summary:
            fields["summary"] = summary
        sections = {
            "markdown": _build_salvaged_markdown(
                record_type="scene",
                title=current_scene_id,
                fields=fields,
                raw_lines=current_lines,
                heading_level=2,
            )
        }
        records.append(PacketRecord(fields=fields, sections=sections))
        current_scene_id = None
        current_lines = []

    for line in lines:
        stripped = line.strip()
        if not stripped:
            if current_scene_id is not None:
                current_lines.append(line)
            continue
        heading_match = re.fullmatch(r"#+\s*(SC\d{3})\s*$", stripped, re.IGNORECASE)
        if heading_match:
            flush()
            current_scene_id = heading_match.group(1).upper()
            current_lines = []
            continue
        bullet_match = re.fullmatch(r"(?:[-*]\s+)?(?:\*\*)?(SC\d{3})(?:\*\*)?(?:\s*[:\-–]\s*(.+))?", stripped, re.IGNORECASE)
        if bullet_match:
            flush()
            current_scene_id = bullet_match.group(1).upper()
            current_lines = []
            summary = bullet_match.group(2) or ""
            if summary:
                current_lines.append(summary.strip())
            continue
        if current_scene_id is not None:
            current_lines.append(line)
    flush()
    return records


def _extract_heading_block_records(markdown: str, *, record_type: str, fallback_prefix: str) -> list[PacketRecord]:
    records: list[PacketRecord] = []
    lines = markdown.splitlines()
    current_title: str | None = None
    current_lines: list[str] = []

    def flush() -> None:
        nonlocal current_title, current_lines
        if current_title is None:
            return
        if _looks_like_generic_index_heading(current_title):
            current_title = None
            current_lines = []
            return
        fields: dict[str, str] = {
            "type": record_type,
            "asset_id": normalize_asset_id(current_title, fallback_prefix=fallback_prefix),
        }
        for line in current_lines:
            key, value = parse_markdown_bullet_key_value(line)
            if key:
                fields[key] = value
        if not fields.get("asset_id"):
            fields["asset_id"] = normalize_asset_id(current_title, fallback_prefix=fallback_prefix)
        if record_type == "character":
            _hydrate_salvaged_character_fields(fields)
        elif record_type == "environment":
            _hydrate_salvaged_environment_fields(fields)
        sections = {"markdown": _build_salvaged_markdown(record_type=record_type, title=current_title, fields=fields, raw_lines=current_lines, heading_level=2)}
        records.append(PacketRecord(fields=fields, sections=sections))
        current_title = None
        current_lines = []

    for line in lines:
        match = INDEX_ENTRY_PATTERN.fullmatch(line.strip())
        if match:
            flush()
            current_title = match.group(1).strip()
            current_lines = []
            continue
        if current_title is not None:
            current_lines.append(line)
    flush()
    return records


def _extract_table_records(
    markdown: str,
    *,
    record_type: str,
    fallback_prefix: str,
    column_aliases: dict[str, str],
    default_section_title: str,
) -> list[PacketRecord]:
    lines = markdown.splitlines()
    records: list[PacketRecord] = []
    index = 0
    while index < len(lines):
        stripped = lines[index].strip()
        if not MARKDOWN_TABLE_ROW_PATTERN.fullmatch(stripped):
            index += 1
            continue
        if index + 1 >= len(lines) or not MARKDOWN_TABLE_SEPARATOR_PATTERN.fullmatch(lines[index + 1].strip()):
            index += 1
            continue
        header_cells = _split_markdown_table_row(stripped)
        normalized_headers = [re.sub(r"[^a-z0-9]+", "_", cell.strip().lower()).strip("_") for cell in header_cells]
        row_index = index + 2
        while row_index < len(lines):
            row_line = lines[row_index].strip()
            if not MARKDOWN_TABLE_ROW_PATTERN.fullmatch(row_line):
                break
            row_cells = _split_markdown_table_row(row_line)
            if len(row_cells) != len(normalized_headers):
                row_index += 1
                continue
            row_map: dict[str, str] = {}
            for header, cell in zip(normalized_headers, row_cells):
                mapped = column_aliases.get(header)
                if mapped:
                    row_map[mapped] = cell.strip()
            asset_id = row_map.get("asset_id", "")
            if not asset_id:
                asset_id = normalize_asset_id(row_map.get("canonical_character_id", "") or row_map.get("description", "") or fallback_prefix, fallback_prefix=fallback_prefix)
            fields: dict[str, str] = {"type": record_type, "asset_id": asset_id}
            fields.update(row_map)
            if record_type == "character":
                _hydrate_salvaged_character_fields(fields)
            elif record_type == "environment":
                _hydrate_salvaged_environment_fields(fields)
            title = row_map.get("canonical_character_id") or row_map.get("description") or row_map.get("asset_id") or default_section_title
            sections = {"markdown": _build_salvaged_markdown(record_type=record_type, title=title, fields=fields, raw_lines=[row_line], heading_level=1)}
            records.append(PacketRecord(fields=fields, sections=sections))
            row_index += 1
        index = row_index
    return records


def _split_markdown_table_row(line: str) -> list[str]:
    cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
    return cells


def _hydrate_salvaged_character_fields(fields: dict[str, str]) -> None:
    description = fields.get("description", "").strip()
    fully_identified = fields.get("is_fully_identified", "").strip().lower()
    if not fields.get("canonical_character_id"):
        fields["canonical_character_id"] = fields.get("asset_id", "")
    if not fields.get("aliases"):
        fields["aliases"] = "-"
    if not fields.get("is_fully_identified"):
        fields["is_fully_identified"] = "false"
    if not fields.get("manual_description_required"):
        fields["manual_description_required"] = "true" if _character_description_needs_manual_followup(description, fully_identified) else "false"
    if not fields.get("manual_description_reason"):
        fields["manual_description_reason"] = _character_manual_description_reason(description)
    if not fields.get("clarification_required"):
        fields["clarification_required"] = "false"
    fields.setdefault("clarification_reason", "")
    fields.setdefault("clarification_question", "")


def _hydrate_salvaged_environment_fields(fields: dict[str, str]) -> None:
    if not fields.get("aliases"):
        fields["aliases"] = "-"
    fields.setdefault("role", fields.get("description", ""))
    fields.setdefault("description", fields.get("description", ""))


def _character_description_needs_manual_followup(description: str, fully_identified: str) -> bool:
    normalized = description.lower().strip()
    if fully_identified in {"false", "no", "0"}:
        return True
    if len(normalized) < 60:
        return True
    return any(term in normalized for term in ["referenced only", "uncertain", "unknown", "no physical", "sparse"])


def _character_manual_description_reason(description: str) -> str:
    normalized = description.strip()
    if not normalized:
        return "The salvaged index summary did not provide enough physical description for dependable image generation."
    return f"The salvaged index summary only provides: {normalized[:180]}"


def _build_salvaged_markdown(*, record_type: str, title: str, fields: dict[str, str], raw_lines: list[str], heading_level: int) -> str:
    heading_prefix = "#" * max(1, min(heading_level, 6))
    display_title = title.strip() or "Salvaged Entry"
    lines = [f"{heading_prefix} {display_title}"]
    if record_type == "character":
        lines.extend(
            [
                "",
                f"**Chapter Role:** {fields.get('description', '').strip() or 'Index summary'}",
                f"**Canonical Character ID:** {fields.get('canonical_character_id', '').strip() or fields.get('asset_id', '').strip()}",
                f"**Aliases:** {fields.get('aliases', '').strip() or '-'}",
                f"**Identification Status:** {fields.get('is_fully_identified', '').strip() or 'false'}",
                f"**Description:** {fields.get('description', '').strip() or 'See salvaged index summary.'}",
                "**Uncertainty Notes:** Salvaged from index output because explicit record wrappers were missing.",
            ]
        )
    else:
        lines.extend(
            [
                "",
                f"**Role:** {fields.get('role', '').strip() or 'Index summary'}",
                f"**Description:** {fields.get('description', '').strip() or 'See salvaged index summary.'}",
                "**Uncertainty Notes:** Salvaged from index output because explicit record wrappers were missing.",
            ]
        )
    if raw_lines:
        lines.extend(["", "**Salvage Source:**", *[f"- {line.strip()}" for line in raw_lines if line.strip()]])
    return "\n".join(lines).strip()


def _looks_like_generic_index_heading(title: str) -> bool:
    normalized = re.sub(r"[^a-z0-9]+", " ", title.lower()).strip()
    return normalized in {
        "visible characters",
        "character records",
        "environment index",
        "visible environments",
        "scene index",
        "beat index",
        "clip roster",
    }


def validate_scene_decomposition(*, chapter_id: str, scene_records: list[PacketRecord]) -> list[str]:
    warnings: list[str] = []
    if not scene_records:
        raise LMStudioError(f"Scene decomposition for {chapter_id} returned no usable scenes.")

    if len(scene_records) < PREFERRED_SCENE_COUNT:
        warnings.append(
            f"Scene decomposition for {chapter_id} returned only {len(scene_records)} scenes; preferred minimum is {PREFERRED_SCENE_COUNT}."
        )

    emotional_shifts: list[str] = []
    thin_scene_count = 0
    normalized_summaries: list[str] = []
    for record in scene_records:
        markdown = require_record_section(record, "markdown")
        normalized = markdown.lower()
        summary = scene_record_summary_line(markdown)
        normalized_summaries.append(re.sub(r"[^a-z0-9]+", " ", summary.lower()).strip())
        if len(normalized.strip()) < THIN_SCENE_MARKDOWN_THRESHOLD:
            thin_scene_count += 1
        if "aftermath" in normalized or "payoff" in normalized or "helplessness" in normalized or "reveal" in normalized:
            emotional_shifts.append("aftermath")
        if "battle" in normalized or "attack" in normalized or "destruction" in normalized or "boarding" in normalized:
            emotional_shifts.append("action")
        if "introduce" in normalized or "setup" in normalized or "return" in normalized or "arrival" in normalized:
            emotional_shifts.append("setup")

    if thin_scene_count:
        warnings.append(
            f"Scene decomposition for {chapter_id} has {thin_scene_count} thin scene markdown block(s) below the preferred detail threshold."
        )

    if len(scene_records) <= 2 and len({summary for summary in normalized_summaries if summary}) <= 1:
        warnings.append(
            f"Scene decomposition for {chapter_id} may be repetitive: the scene summaries are too similar across the small scene set."
        )

    if len(scene_records) <= 2 and not {"action", "aftermath", "setup"} & set(emotional_shifts):
        warnings.append(
            f"Scene decomposition for {chapter_id} has only {len(scene_records)} scenes and no strong transition markers; review the split for possible collapse."
        )

    if "action" in emotional_shifts and "aftermath" not in emotional_shifts:
        warnings.append("Scene decomposition may have collapsed aftermath/reveal material into action scenes; no aftermath-like scene language detected.")
    return warnings


def extract_clip_beat_refs(markdown: str) -> set[str]:
    refs: set[str] = set()
    for match in re.finditer(r"BT\d{3}", markdown.upper()):
        refs.add(match.group(0))
    return refs


def scene_allows_single_clip(scene_markdown: str) -> bool:
    normalized = scene_markdown.lower()
    return "single-shot" in normalized or "single shot" in normalized


def validate_clip_plan(
    *,
    scene_id: str,
    scene_markdown: str,
    beat_ids: list[str],
    clip_ids: list[str],
    clip_markdowns: dict[str, str],
    roster_markdown: str,
    strict_missing_beats: bool = False,
) -> list[str]:
    warnings: list[str] = []
    if len(clip_ids) < 2 and not scene_allows_single_clip(scene_markdown):
        raise LMStudioError(f"Clip plan for {scene_id} produced only {len(clip_ids)} clip(s), but the scene is not marked as a valid single-shot scene.")
    covered_beats: set[str] = set()
    for markdown in clip_markdowns.values():
        covered_beats.update(extract_clip_beat_refs(markdown))
    missing_beats = [beat_id for beat_id in beat_ids if beat_id not in covered_beats]
    if missing_beats:
        message = f"Clip plan for {scene_id} does not explicitly reference all beats. Missing beat refs: {', '.join(missing_beats)}"
        if strict_missing_beats:
            raise LMStudioError(message)
        warnings.append(message)
    roster_ids = re.findall(r"\bCL\d{3}\b", roster_markdown.upper())
    if roster_ids and len(set(roster_ids)) != len(clip_ids):
        warnings.append(f"Clip roster / clip file parity mismatch in {scene_id}: roster shows {len(set(roster_ids))} clip ids but {len(clip_ids)} clip files were created.")
    if len(beat_ids) >= 3 and len(clip_ids) == 1:
        raise LMStudioError(f"Clip plan for {scene_id} compressed {len(beat_ids)} beats into a single clip, which is not allowed.")
    warnings.extend(validate_scene_duration_sanity(scene_id=scene_id, beat_ids=beat_ids, clip_ids=clip_ids))
    return warnings


def validate_scene_duration_sanity(*, scene_id: str, beat_ids: list[str], clip_ids: list[str]) -> list[str]:
    warnings: list[str] = []
    estimated_duration_seconds = len(clip_ids) * 5
    if len(beat_ids) >= 4 and estimated_duration_seconds < 15:
        warnings.append(f"{scene_id} may be under-covered: {len(beat_ids)} beats mapped to only {len(clip_ids)} clips (~{estimated_duration_seconds}s).")
    if len(clip_ids) >= 10 and estimated_duration_seconds > 60:
        warnings.append(f"{scene_id} may be over-segmented: {len(clip_ids)} clips (~{estimated_duration_seconds}s).")
    return warnings


def parse_packet_bool(value: str) -> bool:
    normalized = value.strip().lower()
    if normalized in {"true", "yes", "1"}:
        return True
    if normalized in {"false", "no", "0"}:
        return False
    raise LMStudioError(f"Expected boolean packet field but got '{value}'.")


def parse_markdown_bullet_key_value(line: str) -> tuple[str, str]:
    stripped = line.strip()
    if stripped.startswith(("- ", "* ")):
        stripped = stripped[2:].strip()
    stripped = re.sub(r"^\*\*(.+?)\*\*", r"\1", stripped)
    if ":" not in stripped:
        return "", ""
    key, value = stripped.split(":", 1)
    normalized_key = re.sub(r"[^a-z0-9]+", "_", key.strip().lower()).strip("_")
    return normalized_key, value.strip()


def parse_markdown_key_value_items(markdown: str, *, asset_id: str, asset_type: str) -> ParsedInputsMarkdown:
    values: dict[str, str] = {}
    warnings: list[str] = []
    current_key: str | None = None
    for line in markdown.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith(("- ", "* ")):
            stripped = stripped[2:].strip()
        if ":" in stripped:
            key, value = stripped.split(":", 1)
            normalized_key = key.strip()
            if normalized_key:
                values[normalized_key] = value.strip()
                current_key = normalized_key
                continue
            warnings.append(f"Ignored inputs_markdown line with empty key: {line.strip()}")
            continue
        if current_key is not None:
            values[current_key] = f"{values[current_key]}\n{stripped}" if values[current_key] else stripped
            continue
        if re.search(r"[\\/].+\.[a-z0-9]+$", stripped, re.IGNORECASE):
            generated_key = f"source_{len(values) + 1}"
            values[generated_key] = stripped
            current_key = generated_key
            continue
        if stripped:
            generated_key = f"note_{len(values) + 1}"
            values[generated_key] = stripped
            current_key = generated_key
            warnings.append(f"Salvaged freeform inputs_markdown line into {generated_key}: {line.strip()}")
    if not values:
        values = {"project_asset": f"{asset_type}:{asset_id}", "asset_id": asset_id}
        warnings.append("Synthesized minimal inputs_markdown because no usable lines were returned.")
    return ParsedInputsMarkdown(items=values, warnings=warnings)


def parse_markdown_list(markdown: str) -> list[str]:
    items: list[str] = []
    for line in markdown.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith(("- ", "* ")):
            stripped = stripped[2:].strip()
        items.append(stripped)
    if not items:
        raise LMStudioError("Expected at least one list item in Markdown list content.")
    return items


def split_sections(text: str) -> dict[str, str]:
    matches = list(HEADING_PATTERN.finditer(text))
    if not matches:
        return {}
    sections: dict[str, str] = {}
    for index, match in enumerate(matches):
        heading = match.group(1).strip()
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        sections[heading] = text[start:end].strip()
    return sections


def chapter_id_from_name(name: str) -> str:
    match = CHAPTER_ID_PATTERN.search(name)
    return match.group(1).upper() if match else ""


def normalize_scene_id(value: str) -> str:
    normalized = value.strip().upper()
    if not SCENE_ID_PATTERN.fullmatch(normalized):
        raise LMStudioError(f"Invalid scene id returned by LM Studio: {value}")
    return validate_scene_id(normalized)


def normalize_beat_id(value: str) -> str:
    normalized = value.strip().upper()
    if not re.fullmatch(r"BT\d{3}", normalized):
        raise LMStudioError(f"Invalid beat id returned by LM Studio: {value}")
    return normalized


def is_hierarchical_clip_id(value: str) -> bool:
    normalized = value.strip().upper().replace("-", "_").replace(" ", "")
    return bool(re.fullmatch(r"CL(?:IP)?_?\d{1,3}_(\d{1,3}|[A-Z])", normalized))


def normalize_clip_id(
    value: str,
    *,
    promoted_hierarchical_map: dict[str, str] | None = None,
    hierarchical_sequence_seen: int = 0,
) -> tuple[str, str | None]:
    original = value.strip()
    normalized = original.upper().replace("-", "_").replace(" ", "")
    direct_match = re.fullmatch(r"CL(?:IP)?_?(\d{1,3})", normalized)
    subclip_match = re.fullmatch(r"CL(?:IP)?_?(\d{1,3})_(\d{1,3}|[A-Z])", normalized)
    suffixed_match = re.fullmatch(r"CL(?:IP)?_?(\d{1,3})([A-Z])", normalized)
    plain_number_match = re.fullmatch(r"\d{1,3}", normalized)
    compound_number_match = re.fullmatch(r"(\d{1,3})_(\d{1,3})", normalized)
    warning = None
    if subclip_match:
        if promoted_hierarchical_map is None:
            promoted_hierarchical_map = {}
        if normalized not in promoted_hierarchical_map:
            promoted_hierarchical_map[normalized] = f"CL{hierarchical_sequence_seen + 1:03d}"
        coerced = promoted_hierarchical_map[normalized]
        warning = f"Promoted hierarchical clip id '{value}' to top-level canonical clip id '{coerced}'."
    elif plain_number_match:
        coerced = f"CL{int(normalized):03d}"
    elif direct_match:
        coerced = f"CL{int(direct_match.group(1)):03d}"
    elif suffixed_match:
        coerced = f"CL{int(suffixed_match.group(1)):03d}"
        warning = f"Normalized suffixed non-canonical clip id '{value}' to '{coerced}'."
    elif compound_number_match:
        coerced = f"CL{int(compound_number_match.group(1)):03d}"
        warning = f"Normalized compound non-canonical clip id '{value}' to '{coerced}'."
    else:
        raise LMStudioError(f"Invalid clip id returned by LM Studio: {value}")
    if warning is None and coerced != original.upper():
        warning = f"Normalized non-canonical clip id '{value}' to '{coerced}'."
    return validate_clip_id(coerced), warning


def normalize_asset_id(value: str, *, fallback_prefix: str) -> str:
    normalized = re.sub(r"[^a-z0-9]+", "_", value.strip().lower()).strip("_")
    if not normalized:
        normalized = fallback_prefix
    if not ASSET_ID_PATTERN.fullmatch(normalized):
        raise LMStudioError(f"Invalid asset id returned by LM Studio: {value}")
    return normalized


def scene_record_summary_line(markdown: str) -> str:
    sections = split_sections(markdown)
    for heading in ("Scene Summary", "Scene Purpose", "Summary"):
        value = sections.get(heading, "").strip()
        if value:
            return value.replace("\n", " ")[:200]
    for line in markdown.splitlines():
        stripped = line.strip()
        if stripped and not stripped.startswith("#"):
            return stripped[:200]
    return "Scene extracted without an explicit summary."


def markdown_bundle(*, directory: Path, exclude_names: set[str]) -> str:
    chunks: list[str] = []
    for path in sorted(directory.glob("*.md")):
        if path.name in exclude_names:
            continue
        chunks.append(f"## {path.name}\n{path.read_text(encoding='utf-8').strip()}")
    return "\n\n".join(chunks)


def prune_markdown_dir(directory: Path, *, keep_names: set[str]) -> None:
    if not directory.exists():
        return
    project_root = find_project_root(directory)
    if project_root is None:
        raise ValueError(f"Refusing to prune markdown outside a project directory: {directory}")
    for path in directory.glob("*.md"):
        if path.name in keep_names:
            continue
        try:
            remove_path_within_project(path, project_root=project_root, missing_ok=True)
        except PermissionError:
            continue


def write_text(path: Path, content: str) -> None:
    ensure_dir(path.parent)
    text = content.rstrip() + "\n"
    path.write_text(text, encoding="utf-8")
