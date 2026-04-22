from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .book_librarian import chapter_paragraphs, chapter_source_path, list_chapter_entries
from .chapter_selection import chapter_matches, parse_chapter_selector
from .core.json_io import read_json, write_json
from .scaffold import create_project
from .state import path_to_manifest_value
from .world_global import global_character_registry_path

DIALOGUE_TIMELINE_SCHEMA_VERSION = "2026-04-22-dialogue-timeline-v1"


MOJIBAKE_REPLACEMENTS = {
    "â€œ": '"',
    "â€": '"',
    "â€˜": "'",
    "â€™": "'",
    "â€“": "-",
    "â€”": "-",
    "“": '"',
    "”": '"',
    "‘": "'",
    "’": "'",
}

SPEECH_VERBS = (
    "said",
    "replied",
    "asked",
    "answered",
    "cried",
    "called",
    "shouted",
    "whispered",
    "murmured",
    "exclaimed",
    "retorted",
    "muttered",
)

QUOTE_PATTERN = re.compile(r'"([^"]+)"')
ATTRIBUTION_AFTER_PATTERN = re.compile(
    r"\b(?P<speaker>[A-Z][A-Za-z0-9'\-\. ]{1,70}?)\s+(?:"
    + "|".join(SPEECH_VERBS)
    + r")\b"
)
ATTRIBUTION_BEFORE_PATTERN = re.compile(
    r"\b(?:"
    + "|".join(SPEECH_VERBS)
    + r")\s+(?:the\s+)?(?P<speaker>[A-Z][A-Za-z0-9'\-\. ]{1,70}?)\b"
)
ATTRIBUTION_ROLE_PATTERN = re.compile(
    r"\b(the\s+prisoner|the\s+girl|the\s+woman|the\s+man|the\s+chief|the\s+chieftain|the\s+captain|the\s+warrior|the\s+warriors|the\s+leader)\b"
)


@dataclass(frozen=True)
class DialogueSpeaker:
    speaker_label: str
    canonical_id: str | None = None
    display_name: str = ""
    status: str = "unresolved"
    entity_kind: str = ""
    confidence: float = 0.0
    resolution_method: str = "unresolved"
    notes: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "speaker_label": self.speaker_label,
            "canonical_id": self.canonical_id,
            "display_name": self.display_name,
            "status": self.status,
            "entity_kind": self.entity_kind,
            "confidence": self.confidence,
            "resolution_method": self.resolution_method,
            "notes": self.notes,
        }


@dataclass(frozen=True)
class DialogueEvent:
    dialogue_id: str
    chapter_id: str
    paragraph_index: int
    quote_index: int
    source_ref: str
    source_path: str
    dialogue_text: str
    source_excerpt: str
    speaker: DialogueSpeaker
    scene_id: str | None = None
    shot_id: str | None = None
    clip_id: str | None = None
    scene_binding_confidence: float = 0.0
    shot_binding_confidence: float = 0.0
    binding_method: str = "unbound"
    review_notes: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "dialogue_id": self.dialogue_id,
            "chapter_id": self.chapter_id,
            "paragraph_index": self.paragraph_index,
            "quote_index": self.quote_index,
            "source_ref": self.source_ref,
            "source_path": self.source_path,
            "dialogue_text": self.dialogue_text,
            "source_excerpt": self.source_excerpt,
            "speaker": self.speaker.to_dict(),
            "scene_id": self.scene_id,
            "shot_id": self.shot_id,
            "clip_id": self.clip_id,
            "scene_binding_confidence": self.scene_binding_confidence,
            "shot_binding_confidence": self.shot_binding_confidence,
            "binding_method": self.binding_method,
            "review_notes": self.review_notes,
        }


@dataclass(frozen=True)
class DialogueTimelineSummary:
    project_slug: str
    total_chapters: int
    total_events: int
    total_scene_bindings: int
    total_shot_bindings: int
    review_queue_count: int
    written_files: list[str]
    warnings: list[str]

    def to_dict(self) -> dict[str, Any]:
        return {
            "project_slug": self.project_slug,
            "total_chapters": self.total_chapters,
            "total_events": self.total_events,
            "total_scene_bindings": self.total_scene_bindings,
            "total_shot_bindings": self.total_shot_bindings,
            "review_queue_count": self.review_queue_count,
            "written_files": self.written_files,
            "warnings": self.warnings,
        }


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _fingerprint(data: Any) -> str:
    raw = json.dumps(data, sort_keys=True, ensure_ascii=False)
    return hashlib.sha1(raw.encode("utf-8")).hexdigest()


def _normalize_text(text: str) -> str:
    cleaned = text
    for old, new in MOJIBAKE_REPLACEMENTS.items():
        cleaned = cleaned.replace(old, new)
    return cleaned


def _compact_snippet(text: str, *, limit: int = 220) -> str:
    collapsed = " ".join(text.split()).strip()
    if len(collapsed) <= limit:
        return collapsed
    return collapsed[: limit - 3].rstrip() + "..."


def _chapter_id_from_scene_id(scene_id: str) -> str:
    return scene_id[:5]


def _chapter_source_path(project_slug: str, chapter_id: str) -> Path:
    return chapter_source_path(project_slug, chapter_id)


def _load_scene_contracts(project_dir: Path) -> dict[str, list[dict[str, Any]]]:
    scene_contract_root = project_dir / "02_story_analysis" / "contracts" / "scenes"
    grouped: dict[str, list[dict[str, Any]]] = {}
    if not scene_contract_root.exists():
        return grouped
    for path in sorted(scene_contract_root.glob("CH*/CH*_SC*.json")):
        payload = read_json(path)
        if not isinstance(payload, dict):
            continue
        scene_id = str(payload.get("scene_id", "")).strip().upper() or path.stem.upper()
        chapter_id = str(payload.get("chapter_id", "")).strip().upper() or _chapter_id_from_scene_id(scene_id)
        grouped.setdefault(chapter_id, []).append(payload)
    for chapter_id in grouped:
        grouped[chapter_id].sort(key=lambda item: str(item.get("scene_id", "")))
    return grouped


def _load_shot_indexes(project_dir: Path) -> dict[str, dict[str, list[dict[str, Any]]]]:
    shot_root = project_dir / "02_story_analysis" / "contracts" / "shots"
    grouped: dict[str, dict[str, list[dict[str, Any]]]] = {}
    if not shot_root.exists():
        return grouped
    for path in sorted(shot_root.glob("CH*/CH*_SC*/SHOT_INDEX.json")):
        payload = read_json(path)
        if not isinstance(payload, list):
            continue
        scene_id = path.parent.name.upper()
        chapter_id = path.parent.parent.name.upper()
        grouped.setdefault(chapter_id, {})[scene_id] = [item for item in payload if isinstance(item, dict)]
    return grouped


def _load_character_registry(project_dir: Path, project_slug: str, chapter_id: str) -> dict[str, dict[str, Any]]:
    local_path = project_dir / "02_story_analysis" / "world" / "local" / f"{chapter_id}_CHARACTER_REGISTRY.json"
    if local_path.exists():
        payload = read_json(local_path)
        if isinstance(payload, dict):
            return {key: value for key, value in payload.items() if isinstance(value, dict)}
    canonical_path = global_character_registry_path(project_slug)
    if canonical_path.exists():
        payload = read_json(canonical_path)
        if isinstance(payload, dict):
            return {key: value for key, value in payload.items() if isinstance(value, dict)}
    return {}


def _speaker_variants(canonical_id: str, display_name: str, aliases: list[str] | None = None) -> list[str]:
    variants: list[str] = []
    raw_parts = [part for part in re.split(r"[_\s]+", canonical_id.strip()) if part]
    if raw_parts:
        full = " ".join(raw_parts).strip()
        if full:
            variants.append(full)
        if len(raw_parts) >= 2:
            tail = raw_parts[-1].strip()
            if tail and tail not in variants:
                variants.append(tail)
    display = " ".join(display_name.replace("_", " ").split()).strip()
    if display and display not in variants:
        variants.append(display)
    if aliases:
        for alias in aliases:
            normalized = " ".join(alias.replace("_", " ").split()).strip()
            if normalized and normalized not in variants:
                variants.append(normalized)
    variants.sort(key=len, reverse=True)
    return variants


def _build_speaker_lexicon(registry: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    lexicon: list[dict[str, Any]] = []
    for canonical_id, entry in registry.items():
        aliases = entry.get("aliases", [])
        display_name = str(entry.get("display_name", canonical_id))
        lexicon.append(
            {
                "canonical_id": canonical_id,
                "display_name": display_name,
                "status": str(entry.get("status", "canonical")),
                "entity_kind": str(entry.get("entity_kind", "individual")),
                "variants": _speaker_variants(canonical_id, display_name, aliases if isinstance(aliases, list) else []),
            }
        )
    return lexicon


def _extract_quotes(paragraph_text: str) -> list[tuple[int, int, str]]:
    normalized = _normalize_text(paragraph_text)
    matches: list[tuple[int, int, str]] = []
    for index, match in enumerate(QUOTE_PATTERN.finditer(normalized), start=1):
        text = " ".join(match.group(1).split()).strip()
        if text:
            matches.append((index, match.start(), text))
    return matches


def _speaker_match_from_context(context: str, lexicon: list[dict[str, Any]]) -> DialogueSpeaker | None:
    normalized_context = _normalize_text(context)
    candidates: list[tuple[int, DialogueSpeaker]] = []

    for match in ATTRIBUTION_AFTER_PATTERN.finditer(normalized_context):
        phrase = match.group("speaker").strip()
        resolved = _resolve_speaker_phrase(phrase, lexicon)
        if resolved:
            candidates.append((len(phrase), resolved))

    for match in ATTRIBUTION_BEFORE_PATTERN.finditer(normalized_context):
        phrase = match.group("speaker").strip()
        resolved = _resolve_speaker_phrase(phrase, lexicon)
        if resolved:
            candidates.append((len(phrase), resolved))

    if candidates:
        candidates.sort(key=lambda item: item[0], reverse=True)
        return candidates[0][1]

    role_match = ATTRIBUTION_ROLE_PATTERN.search(normalized_context)
    if role_match:
        phrase = role_match.group(1).strip()
        return DialogueSpeaker(
            speaker_label=phrase,
            canonical_id=None,
            display_name=phrase,
            status="review",
            entity_kind="role",
            confidence=0.35,
            resolution_method="role_attribution",
            notes="Attributed through a role label rather than a canonical name.",
        )

    return None


def _resolve_speaker_phrase(phrase: str, lexicon: list[dict[str, Any]]) -> DialogueSpeaker | None:
    normalized_phrase = " ".join(_normalize_text(phrase).lower().split())
    for entry in lexicon:
        for variant in entry.get("variants", []):
            normalized_variant = " ".join(_normalize_text(variant).lower().split())
            if not normalized_variant:
                continue
            if normalized_variant == normalized_phrase or normalized_variant in normalized_phrase or normalized_phrase in normalized_variant:
                confidence = 0.92 if normalized_variant == normalized_phrase else 0.74
                return DialogueSpeaker(
                    speaker_label=phrase.strip(),
                    canonical_id=str(entry.get("canonical_id", "")).strip() or None,
                    display_name=str(entry.get("display_name", "")).strip() or phrase.strip(),
                    status=str(entry.get("status", "canonical")),
                    entity_kind=str(entry.get("entity_kind", "individual")),
                    confidence=confidence,
                    resolution_method="attribution_name",
                    notes=f"Matched speaker phrase '{phrase.strip()}' to '{entry.get('canonical_id', '')}'.",
                )
    return None


def _infer_speaker(
    paragraph_text: str,
    quote_start: int,
    quote_end: int,
    lexicon: list[dict[str, Any]],
    scene_character_ids: list[str] | None = None,
) -> DialogueSpeaker:
    before = paragraph_text[max(0, quote_start - 140) : quote_start]
    after = paragraph_text[quote_end : min(len(paragraph_text), quote_end + 160)]
    context = before + " " + after

    resolved = _speaker_match_from_context(context, lexicon)
    if resolved:
        return resolved

    role_guess = _role_based_speaker_guess(context, lexicon, scene_character_ids or [])
    if role_guess:
        return role_guess

    return DialogueSpeaker(
        speaker_label="unresolved",
        canonical_id=None,
        display_name="unresolved",
        status="unresolved",
        entity_kind="unknown",
        confidence=0.0,
        resolution_method="unresolved",
        notes="No canonical speaker could be inferred from the source context.",
    )


def _role_based_speaker_guess(
    context: str,
    lexicon: list[dict[str, Any]],
    scene_character_ids: list[str],
) -> DialogueSpeaker | None:
    normalized = " ".join(_normalize_text(context).lower().split())

    def find_by_id(target_ids: list[str], *, confidence: float, method: str, notes: str) -> DialogueSpeaker | None:
        for target_id in target_ids:
            for entry in lexicon:
                if str(entry.get("canonical_id", "")).strip().lower() != target_id.lower():
                    continue
                return DialogueSpeaker(
                    speaker_label=str(entry.get("display_name", target_id)),
                    canonical_id=str(entry.get("canonical_id", target_id)),
                    display_name=str(entry.get("display_name", target_id)),
                    status=str(entry.get("status", "canonical")),
                    entity_kind=str(entry.get("entity_kind", "individual")),
                    confidence=confidence,
                    resolution_method=method,
                    notes=notes,
                )
        return None

    if "prisoner" in normalized or "captive" in normalized:
        prisoner_targets = [target for target in scene_character_ids if "dejah_thoris" in target.lower() or "prisoner" in target.lower()]
        guessed = find_by_id(
            prisoner_targets,
            confidence=0.48,
            method="role_hint",
            notes="Attributed from prisoner/captive wording in the surrounding context.",
        )
        if guessed:
            return guessed

    if re.search(r"\b(i|me|my)\b", normalized):
        guessed = find_by_id(
            [target for target in scene_character_ids if target.lower() == "john_carter"],
            confidence=0.42,
            method="first_person_hint",
            notes="First-person narration suggests John Carter as the speaker.",
        )
        if guessed:
            return guessed

    if re.search(r"\b(she|her)\b", normalized):
        guessed = find_by_id(
            [target for target in scene_character_ids if any(token in target.lower() for token in ["dejah_thoris", "sola"])],
            confidence=0.38,
            method="gendered_role_hint",
            notes="Context suggests a female speaker, but the source wording is still ambiguous.",
        )
        if guessed:
            return guessed

    return None


def _allocate_ranges(total: int, weights: list[int]) -> list[tuple[int, int]]:
    if total <= 0:
        return []
    if not weights:
        return [(1, total)]
    total_weight = sum(max(1, weight) for weight in weights)
    ranges: list[tuple[int, int]] = []
    start = 1
    remaining = total
    for index, weight in enumerate(weights):
        if index == len(weights) - 1:
            end = total
        else:
            share = max(1, round(total * max(1, weight) / total_weight))
            max_allowed = remaining - (len(weights) - index - 1)
            share = min(share, max(1, max_allowed))
            end = min(total, start + share - 1)
        if end < start:
            end = start
        ranges.append((start, end))
        start = end + 1
        remaining = total - end
    if ranges:
        last_start, _ = ranges[-1]
        ranges[-1] = (last_start, total)
    return ranges


def _locate_range(index: int, ranges: list[tuple[int, int]]) -> int | None:
    for idx, (start, end) in enumerate(ranges):
        if start <= index <= end:
            return idx
    return len(ranges) - 1 if ranges else None


def _load_scene_and_shot_maps(project_dir: Path) -> tuple[dict[str, list[dict[str, Any]]], dict[str, dict[str, list[dict[str, Any]]]]]:
    scene_contracts = _load_scene_contracts(project_dir)
    shot_indexes = _load_shot_indexes(project_dir)
    return scene_contracts, shot_indexes


def _weighted_scene_ranges(paragraph_count: int, scene_contracts: list[dict[str, Any]]) -> list[tuple[int, int]]:
    weights = [max(1, len(item.get("beat_list", [])) or 0) for item in scene_contracts]
    if not weights:
        weights = [1]
    return _allocate_ranges(paragraph_count, weights)


def _assign_scenes_to_dialogue_events(
    *,
    events: list[DialogueEvent],
    scene_contracts: list[dict[str, Any]],
    paragraph_count: int,
) -> tuple[list[DialogueEvent], dict[str, list[DialogueEvent]]]:
    if not scene_contracts:
        scene_contracts = []
    scene_ranges = _weighted_scene_ranges(paragraph_count, scene_contracts) if scene_contracts else []
    grouped: dict[str, list[DialogueEvent]] = {}
    assigned: list[DialogueEvent] = []

    for event in events:
        scene_id: str | None = None
        scene_confidence = 0.0
        if scene_contracts and scene_ranges:
            scene_index = _locate_range(event.paragraph_index, scene_ranges)
            if scene_index is not None:
                scene_id = str(scene_contracts[min(scene_index, len(scene_contracts) - 1)].get("scene_id", "")).strip().upper() or None
                scene_confidence = 0.55
        updated = DialogueEvent(
            dialogue_id=event.dialogue_id,
            chapter_id=event.chapter_id,
            paragraph_index=event.paragraph_index,
            quote_index=event.quote_index,
            source_ref=event.source_ref,
            source_path=event.source_path,
            dialogue_text=event.dialogue_text,
            source_excerpt=event.source_excerpt,
            speaker=event.speaker,
            scene_id=scene_id,
            shot_id=None,
            clip_id=None,
            scene_binding_confidence=scene_confidence,
            shot_binding_confidence=0.0,
            binding_method="scene_range" if scene_id else "unassigned",
            review_notes=list(event.review_notes),
        )
        assigned.append(updated)
        if scene_id:
            grouped.setdefault(scene_id, []).append(updated)

    return assigned, grouped


def _assign_shots_to_scene_events(
    *,
    chapter_id: str,
    scene_id: str,
    events: list[DialogueEvent],
    shot_packages: list[dict[str, Any]],
) -> list[DialogueEvent]:
    if not events:
        return []
    if not shot_packages:
        updated: list[DialogueEvent] = []
        for event in events:
            updated.append(
                DialogueEvent(
                    dialogue_id=event.dialogue_id,
                    chapter_id=event.chapter_id,
                    paragraph_index=event.paragraph_index,
                    quote_index=event.quote_index,
                    source_ref=event.source_ref,
                    source_path=event.source_path,
                    dialogue_text=event.dialogue_text,
                    source_excerpt=event.source_excerpt,
                    speaker=event.speaker,
                    scene_id=scene_id,
                    shot_id=None,
                    clip_id=None,
                    scene_binding_confidence=event.scene_binding_confidence,
                    shot_binding_confidence=0.0,
                    binding_method="scene_only",
                    review_notes=list(event.review_notes) + ["No shot packages were available for this scene."],
                )
            )
        return updated

    sorted_shots = sorted(shot_packages, key=lambda item: (int(item.get("shot_order", 0) or 0), str(item.get("shot_id", ""))))
    total_events = len(events)
    total_shots = len(sorted_shots)
    updated: list[DialogueEvent] = []
    for index, event in enumerate(events):
        shot_index = min(total_shots - 1, int((index * total_shots) / max(1, total_events)))
        shot = sorted_shots[shot_index]
        shot_id = str(shot.get("shot_id", "")).strip().upper() or None
        clip_id = f"CL{shot_index + 1:03d}" if shot_id else None
        updated.append(
            DialogueEvent(
                dialogue_id=event.dialogue_id,
                chapter_id=chapter_id,
                paragraph_index=event.paragraph_index,
                quote_index=event.quote_index,
                source_ref=event.source_ref,
                source_path=event.source_path,
                dialogue_text=event.dialogue_text,
                source_excerpt=event.source_excerpt,
                speaker=event.speaker,
                scene_id=scene_id,
                shot_id=shot_id,
                clip_id=clip_id,
                scene_binding_confidence=event.scene_binding_confidence,
                shot_binding_confidence=0.45,
                binding_method="shot_sequence",
                review_notes=list(event.review_notes),
            )
        )
    return updated


def _render_event_markdown(event: DialogueEvent) -> str:
    lines = [
        f"- dialogue_id: `{event.dialogue_id}`",
        f"- paragraph_index: `{event.paragraph_index}`",
        f"- source_ref: `{event.source_ref}`",
        f"- speaker: `{event.speaker.display_name or event.speaker.speaker_label}`",
        f"- scene_id: `{event.scene_id or '(unassigned)'}`",
        f"- shot_id: `{event.shot_id or '(unassigned)'}`",
        f"- clip_id: `{event.clip_id or '(unassigned)'}`",
        f"- dialogue_text: {event.dialogue_text}",
        f"- source_excerpt: {event.source_excerpt}",
        f"- binding_method: `{event.binding_method}`",
    ]
    if event.review_notes:
        lines.append("- review_notes:")
        lines.extend([f"  - {note}" for note in event.review_notes])
    return "\n".join(lines)


def _render_shot_dialogue_markdown(scene_id: str, shot_id: str, events: list[DialogueEvent]) -> str:
    lines = [
        f"# Dialogue Notes: {scene_id}/{shot_id}",
        "",
        f"- shot_id: `{shot_id}`",
        f"- scene_id: `{scene_id}`",
        f"- dialogue_events: `{len(events)}`",
        "",
    ]
    if not events:
        lines.append("- No dialogue events were bound to this shot.")
        return "\n".join(lines) + "\n"
    for event in events:
        lines.append(f"## {event.dialogue_id}")
        lines.append("")
        lines.append(f"- speaker: `{event.speaker.display_name or event.speaker.speaker_label}`")
        lines.append(f"- source_ref: `{event.source_ref}`")
        lines.append(f"- clip_id: `{event.clip_id or '(unassigned)'}`")
        lines.append(f"- dialogue_text: {event.dialogue_text}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def _render_scene_dialogue_index(scene_id: str, events: list[DialogueEvent]) -> str:
    lines = [f"# Scene Dialogue Index: {scene_id}", ""]
    if not events:
        lines.append("- No dialogue events were assigned to this scene.")
        return "\n".join(lines) + "\n"
    for event in events:
        lines.append(
            f"- `{event.dialogue_id}` -> `{event.shot_id or '(unassigned)'}` "
            f"speaker={event.speaker.display_name or event.speaker.speaker_label}"
        )
    return "\n".join(lines) + "\n"


def _render_chapter_dialogue_timeline(chapter_id: str, events: list[DialogueEvent]) -> str:
    lines = [f"# Dialogue Timeline: {chapter_id}", ""]
    lines.append(f"- dialogue_events: `{len(events)}`")
    unresolved = [event for event in events if event.speaker.status == "unresolved"]
    lines.append(f"- unresolved_speakers: `{len(unresolved)}`")
    lines.append("")
    if not events:
        lines.append("- No dialogue events detected in this chapter.")
        return "\n".join(lines) + "\n"
    for event in events:
        lines.append(f"## {event.dialogue_id}")
        lines.append("")
        lines.append(f"- speaker: `{event.speaker.display_name or event.speaker.speaker_label}`")
        lines.append(f"- source_ref: `{event.source_ref}`")
        lines.append(f"- scene_id: `{event.scene_id or '(unassigned)'}`")
        lines.append(f"- shot_id: `{event.shot_id or '(unassigned)'}`")
        lines.append(f"- clip_id: `{event.clip_id or '(unassigned)'}`")
        lines.append(f"- dialogue_text: {event.dialogue_text}")
        lines.append(f"- excerpt: {event.source_excerpt}")
        if event.review_notes:
            lines.append("- review_notes:")
            lines.extend([f"  - {note}" for note in event.review_notes])
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def _render_edit_timeline(project_slug: str, chapter_entries: list[dict[str, Any]]) -> str:
    lines = ["# Edit Timeline", ""]
    lines.append(f"- project_slug: `{project_slug}`")
    lines.append(f"- chapters: `{len(chapter_entries)}`")
    lines.append("")
    if not chapter_entries:
        lines.append("- No chapter edit entries.")
        return "\n".join(lines) + "\n"
    for chapter in chapter_entries:
        lines.append(f"## {chapter['chapter_id']}")
        lines.append("")
        lines.append(f"- chapter_title: {chapter.get('chapter_title', chapter['chapter_id'])}")
        lines.append(f"- scene_count: `{chapter.get('scene_count', 0)}`")
        lines.append(f"- dialogue_events: `{chapter.get('dialogue_events', 0)}`")
        lines.append(f"- estimated_duration_seconds: `{chapter.get('estimated_duration_seconds', 0)}`")
        lines.append(f"- transition_note: {chapter.get('transition_note', '')}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def _render_project_dialogue_index(project_slug: str, chapter_summaries: list[dict[str, Any]]) -> str:
    lines = ["# Dialogue Timeline Index", ""]
    lines.append(f"- project_slug: `{project_slug}`")
    lines.append("")
    if not chapter_summaries:
        lines.append("- No chapter dialogue timelines were generated.")
        return "\n".join(lines) + "\n"
    for chapter in chapter_summaries:
        lines.append(
            f"- `{chapter['chapter_id']}` - {chapter.get('chapter_title', chapter['chapter_id'])} "
            f"(dialogue_events={chapter.get('dialogue_events', 0)}, unresolved={chapter.get('unresolved_speakers', 0)})"
        )
    return "\n".join(lines) + "\n"


def _render_review_queue_markdown(queue: list[dict[str, Any]]) -> str:
    lines = ["# Dialogue Timeline Review Queue", ""]
    if not queue:
        lines.append("- No review items.")
        return "\n".join(lines) + "\n"
    for item in queue:
        lines.append(f"- `{item.get('dialogue_id', '')}`")
        for issue in item.get("issues", []):
            lines.append(f"  - {issue}")
    return "\n".join(lines) + "\n"


def run_dialogue_timeline(
    project_slug: str,
    *,
    force: bool = False,
    chapters: str | None = None,
    run_tracker: "DownstreamRunTracker | None" = None,
) -> DialogueTimelineSummary:
    project_dir = create_project(project_slug)
    timeline_root = project_dir / "02_story_analysis" / "timelines"
    chapter_root = timeline_root / "chapters"
    review_root = timeline_root / "review"
    timeline_root.mkdir(parents=True, exist_ok=True)
    chapter_root.mkdir(parents=True, exist_ok=True)
    review_root.mkdir(parents=True, exist_ok=True)

    scene_contracts_by_chapter, shot_indexes_by_chapter = _load_scene_and_shot_maps(project_dir)
    selected_chapters = set(parse_chapter_selector(chapters))
    book_entries = [entry for entry in list_chapter_entries(project_slug) if chapter_matches(str(entry.get("chapter_id", "")), selected_chapters)]
    warnings: list[str] = []
    review_queue: list[dict[str, Any]] = []
    chapter_summaries: list[dict[str, Any]] = []
    edit_entries: list[dict[str, Any]] = []
    written_files: list[str] = []
    all_events: list[DialogueEvent] = []
    phase_name = "dialogue_timeline"
    if run_tracker is not None:
        run_tracker.set_phase_total(phase_name, len(book_entries))

    for chapter_entry in book_entries:
        chapter_id = str(chapter_entry.get("chapter_id", "")).strip().upper()
        if not chapter_id:
            continue
        chapter_title = str(chapter_entry.get("title", chapter_id)).strip() or chapter_id
        source_path = _chapter_source_path(project_slug, chapter_id)
        chapter_path = chapter_root / chapter_id
        chapter_path.mkdir(parents=True, exist_ok=True)

        paragraphs = chapter_paragraphs(project_slug, chapter_id)
        if not paragraphs:
            warnings.append(f"No paragraphs were available for {chapter_id}; skipped dialogue extraction.")
            continue

        registry = _load_character_registry(project_dir, project_slug, chapter_id)
        lexicon = _build_speaker_lexicon(registry)
        scene_contracts = scene_contracts_by_chapter.get(chapter_id, [])
        shot_indexes = shot_indexes_by_chapter.get(chapter_id, {})
        chapter_json = chapter_path / f"{chapter_id}_DIALOGUE_TIMELINE.json"
        chapter_md = chapter_path / f"{chapter_id}_DIALOGUE_TIMELINE.md"
        chapter_fp = _fingerprint(
            {
                "schema_version": DIALOGUE_TIMELINE_SCHEMA_VERSION,
                "paragraphs": [paragraph.get("text", "") for paragraph in paragraphs],
                "scene_contracts": scene_contracts,
                "shot_indexes": shot_indexes,
            }
        )
        if run_tracker is not None and run_tracker.is_item_completed(phase_name, chapter_id, chapter_fp) and chapter_json.exists():
            existing_payload = read_json(chapter_json)
            if isinstance(existing_payload, dict):
                chapter_events_payload = existing_payload.get("dialogue_events", [])
                if isinstance(existing_payload.get("review_notes"), list):
                    review_queue.extend([item for item in existing_payload.get("review_notes", []) if isinstance(item, dict)])
                if isinstance(chapter_events_payload, list):
                    all_events.extend([DialogueEvent(**item) for item in chapter_events_payload if isinstance(item, dict)])
                chapter_summaries.append(
                    {
                        "chapter_id": chapter_id,
                        "chapter_title": chapter_title,
                        "source_path": path_to_manifest_value(source_path),
                        "dialogue_events": len(chapter_events_payload) if isinstance(chapter_events_payload, list) else 0,
                        "unresolved_speakers": len(
                            [
                                item
                                for item in chapter_events_payload
                                if isinstance(item, dict)
                                and isinstance(item.get("speaker"), dict)
                                and str(item.get("speaker", {}).get("status", "")).strip() == "unresolved"
                            ]
                        ) if isinstance(chapter_events_payload, list) else 0,
                        "scene_count": len(scene_contracts),
                        "shot_count": sum(len(shot_indexes.get(str(scene.get('scene_id', '')).strip().upper(), [])) for scene in scene_contracts),
                    }
                )
                edit_entries.append(
                    {
                        "chapter_id": chapter_id,
                        "chapter_title": chapter_title,
                        "scene_count": len(scene_contracts),
                        "dialogue_events": len(chapter_events_payload) if isinstance(chapter_events_payload, list) else 0,
                        "estimated_duration_seconds": max(10, (len(chapter_events_payload) if isinstance(chapter_events_payload, list) else 0) * 3 + len(scene_contracts) * 5),
                        "transition_note": _compact_snippet(
                            " / ".join(
                                part
                                for part in [
                                    str(scene_contracts[0].get("emotional_arc", "")) if scene_contracts else "",
                                    str(scene_contracts[-1].get("production_intent", "")) if scene_contracts else "",
                                ]
                                if part.strip()
                            ),
                            limit=120,
                        ),
                    }
                )
            continue

        chapter_events: list[DialogueEvent] = []
        scene_character_ids = sorted(
            {
                str(character.get("canonical_id", "")).strip()
                for scene_contract in scene_contracts
                for character in scene_contract.get("characters_required", [])
                if isinstance(character, dict) and str(character.get("canonical_id", "")).strip()
            }
        )

        for paragraph in paragraphs:
            paragraph_index = int(paragraph.get("paragraph_index", 0))
            paragraph_text = _normalize_text(str(paragraph.get("text", "")))
            if not paragraph_text.strip():
                continue
            quotes = _extract_quotes(paragraph_text)
            if not quotes:
                continue
            for quote_index, quote_start, dialogue_text in quotes:
                speaker = _infer_speaker(
                    paragraph_text,
                    quote_start,
                    quote_start + len(dialogue_text) + 2,
                    lexicon,
                    scene_character_ids,
                )
                source_ref = f"{chapter_id}:p{paragraph_index:03d}:q{quote_index:02d}"
                excerpt = _compact_snippet(paragraph_text, limit=240)
                review_notes: list[str] = []
                if speaker.status == "unresolved":
                    review_notes.append("Speaker could not be resolved from the source context.")
                event = DialogueEvent(
                    dialogue_id=f"{chapter_id}_DLG{len(chapter_events) + 1:03d}",
                    chapter_id=chapter_id,
                    paragraph_index=paragraph_index,
                    quote_index=quote_index,
                    source_ref=source_ref,
                    source_path=path_to_manifest_value(source_path),
                    dialogue_text=dialogue_text,
                    source_excerpt=excerpt,
                    speaker=speaker,
                    review_notes=review_notes,
                )
                chapter_events.append(event)

        assigned_events, scene_grouped = _assign_scenes_to_dialogue_events(
            events=chapter_events,
            scene_contracts=scene_contracts,
            paragraph_count=len(paragraphs),
        )

        final_events: list[DialogueEvent] = []
        for scene_contract in scene_contracts:
            scene_id = str(scene_contract.get("scene_id", "")).strip().upper()
            scene_events = scene_grouped.get(scene_id, [])
            shot_packages = shot_indexes.get(scene_id, [])
            scene_assigned = _assign_shots_to_scene_events(
                chapter_id=chapter_id,
                scene_id=scene_id,
                events=scene_events,
                shot_packages=shot_packages,
            )
            final_events.extend(scene_assigned)
            if scene_assigned:
                scene_dir = chapter_path / scene_id
                scene_dir.mkdir(parents=True, exist_ok=True)
                scene_index_path = scene_dir / "DIALOGUE_INDEX.md"
                scene_index_json = scene_dir / "DIALOGUE_INDEX.json"
                write_json(scene_index_json, [event.to_dict() for event in scene_assigned])
                scene_index_path.write_text(_render_scene_dialogue_index(scene_id, scene_assigned), encoding="utf-8")
                written_files.extend([str(scene_index_json), str(scene_index_path)])

            shot_map: dict[str, list[DialogueEvent]] = {}
            for event in scene_assigned:
                if not event.shot_id:
                    continue
                shot_map.setdefault(event.shot_id, []).append(event)
            for shot in shot_packages:
                shot_id = str(shot.get("shot_id", "")).strip().upper()
                if not shot_id:
                    continue
                shot_events = shot_map.get(shot_id, [])
                shot_dir = project_dir / "02_story_analysis" / "contracts" / "shots" / chapter_id / scene_id / shot_id
                shot_dir.mkdir(parents=True, exist_ok=True)
                shot_json = shot_dir / "DIALOGUE.json"
                shot_md = shot_dir / "DIALOGUE.md"
                write_json(shot_json, [event.to_dict() for event in shot_events])
                shot_md.write_text(_render_shot_dialogue_markdown(scene_id, shot_id, shot_events), encoding="utf-8")
                written_files.extend([str(shot_json), str(shot_md)])

        unresolved_events = [event for event in assigned_events if event.speaker.status == "unresolved"]
        if unresolved_events:
            for event in unresolved_events[:10]:
                review_queue.append(
                    {
                        "dialogue_id": event.dialogue_id,
                        "issues": [
                            "Speaker unresolved from chapter source context.",
                            f"Source reference: {event.source_ref}",
                        ],
                    }
                )

        chapter_summary = {
            "chapter_id": chapter_id,
            "chapter_title": chapter_title,
            "source_path": path_to_manifest_value(source_path),
            "dialogue_events": len(final_events),
            "unresolved_speakers": len(unresolved_events),
            "scene_count": len(scene_contracts),
            "shot_count": sum(len(shot_indexes.get(str(scene.get('scene_id', '')).strip().upper(), [])) for scene in scene_contracts),
        }
        chapter_summaries.append(chapter_summary)
        chapter_fp = _fingerprint(
            {
                "schema_version": DIALOGUE_TIMELINE_SCHEMA_VERSION,
                "paragraphs": [paragraph.get("text", "") for paragraph in paragraphs],
                "scene_contracts": scene_contracts,
                "shot_indexes": shot_indexes,
            }
        )

        chapter_payload = {
            "project_slug": project_slug,
            "chapter_id": chapter_id,
            "chapter_title": chapter_title,
            "source_path": path_to_manifest_value(source_path),
            "source_fingerprint": chapter_fp,
            "dialogue_events": [event.to_dict() for event in final_events],
            "scene_bindings": [
                {
                    "scene_id": scene_id,
                    "dialogue_ids": [event.dialogue_id for event in final_events if event.scene_id == scene_id],
                    "shot_ids": [event.shot_id for event in final_events if event.scene_id == scene_id and event.shot_id],
                }
                for scene_id in [str(scene.get("scene_id", "")).strip().upper() for scene in scene_contracts]
            ],
            "review_notes": [item for item in review_queue if str(item.get("dialogue_id", "")).startswith(chapter_id)],
        }
        chapter_json = chapter_path / f"{chapter_id}_DIALOGUE_TIMELINE.json"
        chapter_md = chapter_path / f"{chapter_id}_DIALOGUE_TIMELINE.md"
        if force or run_tracker is not None or not chapter_json.exists() or not chapter_md.exists():
            write_json(chapter_json, chapter_payload)
            chapter_md.write_text(_render_chapter_dialogue_timeline(chapter_id, final_events), encoding="utf-8")
            written_files.extend([str(chapter_json), str(chapter_md)])
            if run_tracker is not None:
                run_tracker.mark_item_completed(
                    phase_name,
                    chapter_id,
                    chapter_fp,
                    outputs=[str(chapter_json), str(chapter_md)],
                )

        edit_entries.append(
            {
                "chapter_id": chapter_id,
                "chapter_title": chapter_title,
                "scene_count": len(scene_contracts),
                "dialogue_events": len(final_events),
                "estimated_duration_seconds": max(10, len(final_events) * 3 + len(scene_contracts) * 5),
                "transition_note": _compact_snippet(
                    " / ".join(
                        part
                        for part in [
                            str(scene_contracts[0].get("emotional_arc", "")) if scene_contracts else "",
                            str(scene_contracts[-1].get("production_intent", "")) if scene_contracts else "",
                        ]
                        if part.strip()
                    ),
                    limit=120,
                ),
            }
        )

        all_events.extend(final_events)

    project_index_json = timeline_root / "dialogue_timeline.json"
    project_index_md = timeline_root / "dialogue_timeline.md"
    edit_timeline_json = timeline_root / "edit_timeline.json"
    edit_timeline_md = timeline_root / "edit_timeline.md"
    review_json = review_root / "DIALOGUE_TIMELINE_REVIEW_QUEUE.json"
    review_md = review_root / "DIALOGUE_TIMELINE_REVIEW_QUEUE.md"

    project_payload = {
        "project_slug": project_slug,
        "generated_at_utc": _utc_now(),
        "chapter_count": len(chapter_summaries),
        "dialogue_event_count": len(all_events),
        "chapter_summaries": chapter_summaries,
        "dialogue_events": [event.to_dict() for event in all_events],
    }
    write_json(project_index_json, project_payload)
    project_index_md.write_text(_render_project_dialogue_index(project_slug, chapter_summaries), encoding="utf-8")
    write_json(edit_timeline_json, {"project_slug": project_slug, "chapters": edit_entries})
    edit_timeline_md.write_text(_render_edit_timeline(project_slug, edit_entries), encoding="utf-8")
    write_json(review_json, review_queue)
    review_md.write_text(_render_review_queue_markdown(review_queue), encoding="utf-8")

    written_files.extend(
        [
            str(project_index_json),
            str(project_index_md),
            str(edit_timeline_json),
            str(edit_timeline_md),
            str(review_json),
            str(review_md),
        ]
    )

    total_scene_bindings = sum(1 for event in all_events if event.scene_id)
    total_shot_bindings = sum(1 for event in all_events if event.shot_id)
    return DialogueTimelineSummary(
        project_slug=project_slug,
        total_chapters=len(chapter_summaries),
        total_events=len(all_events),
        total_scene_bindings=total_scene_bindings,
        total_shot_bindings=total_shot_bindings,
        review_queue_count=len(review_queue),
        written_files=written_files,
        warnings=warnings,
    )
