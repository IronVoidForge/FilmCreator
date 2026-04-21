from __future__ import annotations

import hashlib
import json
import re
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .core.json_io import read_json, write_json
from .scaffold import create_project


ENRICHMENT_ROOT = Path("02_story_analysis") / "dialogue_enrichment"

SPEECH_VERB_CUES = {
    "whispered": ("whispered", "murmured", "muttered", "softly", "low"),
    "shouted": ("shouted", "cried", "called", "exclaimed", "bellowed", "roared"),
    "asked": ("asked", "questioned", "inquired", "queried"),
    "replied": ("replied", "answered", "said", "remarked"),
    "urgent": ("urgent", "hurry", "must", "quick", "immediately", "at once"),
    "stern": ("stern", "grave", "serious", "cold", "flat", "grim"),
    "warm": ("warm", "happy", "glad", "smiled", "loving", "kind"),
    "defiant": ("defiant", "fight", "never", "won't", "refuse", "resist"),
    "fearful": ("fear", "afraid", "danger", "death", "terrible", "panic"),
}


@dataclass(frozen=True)
class DialogueEnrichmentSummary:
    project_slug: str
    total_chapters: int
    total_events: int
    explicit_delivery_count: int
    review_queue_count: int
    written_files: list[str]
    warnings: list[str]

    def to_dict(self) -> dict[str, Any]:
        return {
            "project_slug": self.project_slug,
            "total_chapters": self.total_chapters,
            "total_events": self.total_events,
            "explicit_delivery_count": self.explicit_delivery_count,
            "review_queue_count": self.review_queue_count,
            "written_files": self.written_files,
            "warnings": self.warnings,
        }


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _fingerprint(data: Any) -> str:
    raw = json.dumps(data, sort_keys=True, ensure_ascii=False)
    return hashlib.sha1(raw.encode("utf-8")).hexdigest()


def _compact_snippet(text: str, *, limit: int = 180) -> str:
    collapsed = " ".join(str(text).split()).strip()
    if len(collapsed) <= limit:
        return collapsed
    return collapsed[: limit - 3].rstrip() + "..."


def _chapter_timelines_root(project_dir: Path) -> Path:
    return project_dir / "02_story_analysis" / "timelines" / "chapters"


def _normalize_text(text: str) -> str:
    return " ".join(str(text).split()).strip()


def _contains_any(text: str, phrases: tuple[str, ...]) -> bool:
    lowered = text.lower()
    return any(phrase in lowered for phrase in phrases)


def _infer_delivery_profile(dialogue_text: str, source_excerpt: str, speaker_label: str) -> dict[str, Any]:
    combined = f"{dialogue_text} {source_excerpt} {speaker_label}".lower()

    style = "replied"
    if _contains_any(combined, SPEECH_VERB_CUES["whispered"]):
        style = "whispered"
    elif _contains_any(combined, SPEECH_VERB_CUES["shouted"]):
        style = "shouted"
    elif _contains_any(combined, SPEECH_VERB_CUES["asked"]) or dialogue_text.strip().endswith("?"):
        style = "asked"
    elif _contains_any(combined, SPEECH_VERB_CUES["urgent"]):
        style = "urgent"
    elif _contains_any(combined, SPEECH_VERB_CUES["stern"]):
        style = "stern"
    elif _contains_any(combined, SPEECH_VERB_CUES["warm"]):
        style = "warm"
    elif _contains_any(combined, SPEECH_VERB_CUES["defiant"]):
        style = "defiant"
    elif _contains_any(combined, SPEECH_VERB_CUES["fearful"]):
        style = "fearful"

    if style == "whispered":
        voice_quality = "soft"
        volume = "low"
        tempo = "slow"
    elif style == "shouted":
        voice_quality = "forceful"
        volume = "high"
        tempo = "fast"
    elif style == "asked":
        voice_quality = "inquiring"
        volume = "medium"
        tempo = "steady"
    elif style == "urgent":
        voice_quality = "pressured"
        volume = "medium"
        tempo = "fast"
    elif style == "stern":
        voice_quality = "gruff"
        volume = "medium"
        tempo = "steady"
    elif style == "warm":
        voice_quality = "warm"
        volume = "medium"
        tempo = "steady"
    elif style == "defiant":
        voice_quality = "hard"
        volume = "medium"
        tempo = "brisk"
    elif style == "fearful":
        voice_quality = "tense"
        volume = "low"
        tempo = "slow"
    else:
        voice_quality = "neutral"
        volume = "medium"
        tempo = "steady"

    emotion = "neutral"
    if _contains_any(combined, ("happy", "glad", "love", "dear", "joy", "smile")):
        emotion = "tender"
    elif _contains_any(combined, ("angry", "rage", "fury", "furious", "enraged")):
        emotion = "angry"
    elif _contains_any(combined, ("sad", "grief", "sorrow", "loss", "die", "death")):
        emotion = "somber"
    elif _contains_any(combined, ("fear", "afraid", "danger", "panic")):
        emotion = "tense"
    elif _contains_any(combined, ("defiant", "fight", "never")):
        emotion = "defiant"
    elif _contains_any(combined, ("grave", "stern", "serious")):
        emotion = "grave"
    elif _contains_any(combined, ("warm", "gentle", "kind")):
        emotion = "warm"
    elif _contains_any(combined, ("laugh", "smile", "amused", "jest", "joke")):
        emotion = "amused"

    evidence_cues = []
    for cue in ("whispered", "murmured", "muttered", "shouted", "cried", "asked", "replied", "answered", "urgent", "stern", "warm", "defiant", "fearful"):
        if cue in combined:
            evidence_cues.append(cue)

    confidence = 0.62
    if style != "replied":
        confidence += 0.18
    if emotion != "neutral":
        confidence += 0.08
    if dialogue_text.strip().endswith(("!", "?")):
        confidence += 0.04
    if len(dialogue_text.split()) <= 8:
        confidence += 0.03
    confidence = round(min(confidence, 0.98), 2)

    delivery_note = f"{style.replace('_', ' ')} delivery with {voice_quality} voice quality, {emotion} emotion, {volume} volume, and {tempo} tempo."
    if not evidence_cues:
        evidence_cues = ["source_context"]

    review_flags: list[str] = []
    if style == "replied" and emotion == "neutral":
        review_flags.append("delivery_inferred_from_structure_only")

    return {
        "delivery_style": style,
        "voice_quality": voice_quality,
        "emotion": emotion,
        "volume": volume,
        "tempo": tempo,
        "delivery_note": delivery_note,
        "confidence": confidence,
        "evidence_cues": evidence_cues[:6],
        "review_flags": review_flags,
    }


def _render_event_lines(event: dict[str, Any]) -> list[str]:
    delivery = event.get("delivery_profile", {})
    speaker = event.get("speaker", {}) if isinstance(event.get("speaker"), dict) else {}
    lines = [
        f"- `{event.get('dialogue_id', '')}`",
        f"  - speaker: `{speaker.get('display_name') or speaker.get('speaker_label') or 'unresolved'}`",
        f"  - scene_id: `{event.get('scene_id', '') or 'unbound'}`",
        f"  - shot_id: `{event.get('shot_id', '') or 'unbound'}`",
        f"  - delivery_style: `{delivery.get('delivery_style', 'unknown')}`",
        f"  - voice_quality: `{delivery.get('voice_quality', 'unknown')}`",
        f"  - emotion: `{delivery.get('emotion', 'unknown')}`",
        f"  - volume: `{delivery.get('volume', 'unknown')}`",
        f"  - tempo: `{delivery.get('tempo', 'unknown')}`",
        f"  - confidence: `{delivery.get('confidence', 0.0)}`",
    ]
    note = str(delivery.get("delivery_note", "")).strip()
    if note:
        lines.append(f"  - note: {note}")
    cues = delivery.get("evidence_cues", [])
    if isinstance(cues, list) and cues:
        lines.append("  - cues:")
        lines.extend([f"    - {str(cue)}" for cue in cues])
    return lines


def _render_chapter_markdown(chapter_id: str, chapter_title: str, events: list[dict[str, Any]], review_items: list[dict[str, Any]]) -> str:
    explicit = sum(1 for event in events if str((event.get("delivery_profile") or {}).get("delivery_style", "")).strip() not in {"", "replied"})
    lines = [
        f"# Dialogue Enrichment: {chapter_id}",
        "",
        f"- chapter_title: `{chapter_title}`",
        f"- event_count: `{len(events)}`",
        f"- explicit_delivery_count: `{explicit}`",
        f"- review_count: `{len(review_items)}`",
        "",
        "## Events",
        "",
    ]
    if events:
        for event in events:
            lines.extend(_render_event_lines(event))
            lines.append("")
    else:
        lines.append("- No dialogue events were available.")
        lines.append("")
    if review_items:
        lines.extend(["## Review", ""])
        for item in review_items:
            lines.append(f"- `{item.get('dialogue_id', '')}`: {', '.join(item.get('issues', []))}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def _render_index_markdown(project_slug: str, chapter_summaries: list[dict[str, Any]]) -> str:
    lines = [
        "# Dialogue Enrichment Index",
        "",
        f"- project_slug: `{project_slug}`",
        f"- chapters: `{len(chapter_summaries)}`",
        "",
        "## Chapters",
        "",
    ]
    for chapter in chapter_summaries:
        lines.append(
            f"- `{chapter['chapter_id']}` - {chapter['chapter_title']} "
            f"(events={chapter['event_count']}, explicit_delivery={chapter['explicit_delivery_count']}, review={chapter['review_count']})"
        )
    lines.append("")
    return "\n".join(lines)


def _render_review_markdown(queue: list[dict[str, Any]]) -> str:
    lines = ["# Dialogue Enrichment Review Queue", ""]
    if not queue:
        lines.append("- No review items.")
    else:
        for item in queue:
            lines.append(f"- `{item.get('dialogue_id', '')}`")
            for issue in item.get("issues", []):
                lines.append(f"  - {issue}")
    lines.append("")
    return "\n".join(lines)


def run_dialogue_enrichment(
    project_slug: str,
    *,
    force: bool = False,
) -> DialogueEnrichmentSummary:
    project_dir = create_project(project_slug)
    chapter_root = _chapter_timelines_root(project_dir)
    enrichment_root = project_dir / ENRICHMENT_ROOT
    review_root = enrichment_root / "review"
    enrichment_root.mkdir(parents=True, exist_ok=True)
    review_root.mkdir(parents=True, exist_ok=True)

    chapter_paths = sorted(chapter_root.glob("CH*/CH*_DIALOGUE_TIMELINE.json"))
    chapter_summaries: list[dict[str, Any]] = []
    review_queue: list[dict[str, Any]] = []
    written_files: list[str] = []
    warnings: list[str] = []
    total_events = 0
    explicit_delivery_count = 0

    for index, chapter_path in enumerate(chapter_paths, start=1):
        started_at = time.perf_counter()
        chapter_payload = read_json(chapter_path)
        if not isinstance(chapter_payload, dict):
            warnings.append(f"Skipping unreadable dialogue timeline: {chapter_path}")
            continue
        chapter_id = str(chapter_payload.get("chapter_id", chapter_path.stem[:5])).strip().upper()
        chapter_title = str(chapter_payload.get("chapter_title", chapter_id)).strip() or chapter_id
        events = chapter_payload.get("dialogue_events", [])
        if not isinstance(events, list):
            events = []

        enriched_events: list[dict[str, Any]] = []
        chapter_review_items: list[dict[str, Any]] = []
        for event in events:
            if not isinstance(event, dict):
                continue
            dialogue_id = str(event.get("dialogue_id", "")).strip() or f"{chapter_id}_DLG{len(enriched_events) + 1:03d}"
            dialogue_text = _normalize_text(str(event.get("dialogue_text", "")))
            source_excerpt = _normalize_text(str(event.get("source_excerpt", "")))
            speaker = event.get("speaker", {}) if isinstance(event.get("speaker"), dict) else {}
            speaker_label = str(speaker.get("display_name") or speaker.get("speaker_label") or "unresolved").strip()
            delivery_profile = _infer_delivery_profile(dialogue_text, source_excerpt, speaker_label)
            enriched_event = dict(event)
            enriched_event["delivery_profile"] = delivery_profile
            enriched_event["delivery_source"] = {
                "dialogue_text": dialogue_text,
                "source_excerpt": source_excerpt,
                "speaker_label": speaker_label,
            }
            enriched_events.append(enriched_event)
            total_events += 1
            if delivery_profile["delivery_style"] != "replied":
                explicit_delivery_count += 1
            if speaker_label.lower() == "unresolved" or "Project Gutenberg" in dialogue_text:
                issues = ["speaker unresolved" if speaker_label.lower() == "unresolved" else "false-positive boilerplate dialogue"]
                if delivery_profile["delivery_style"] == "replied":
                    issues.append("delivery inferred from structure only")
                review_item = {"dialogue_id": dialogue_id, "issues": issues}
                chapter_review_items.append(review_item)
                review_queue.append(review_item)

        chapter_summary = {
            "chapter_id": chapter_id,
            "chapter_title": chapter_title,
            "event_count": len(enriched_events),
            "explicit_delivery_count": sum(1 for event in enriched_events if str((event.get("delivery_profile") or {}).get("delivery_style", "")).strip() not in {"", "replied"}),
            "review_count": len(chapter_review_items),
        }
        chapter_summaries.append(chapter_summary)

        chapter_dir = enrichment_root / "chapters" / chapter_id
        chapter_dir.mkdir(parents=True, exist_ok=True)
        chapter_json = chapter_dir / f"{chapter_id}_DIALOGUE_ENRICHMENT.json"
        chapter_md = chapter_dir / f"{chapter_id}_DIALOGUE_ENRICHMENT.md"
        if force or not chapter_json.exists() or not chapter_md.exists():
            write_json(
                chapter_json,
                {
                    "project_slug": project_slug,
                    "chapter_id": chapter_id,
                    "chapter_title": chapter_title,
                    "source_path": chapter_payload.get("source_path"),
                    "source_fingerprint": chapter_payload.get("source_fingerprint", _fingerprint(chapter_payload.get("dialogue_events", []))),
                    "dialogue_events": enriched_events,
                    "review_notes": chapter_review_items,
                },
            )
            chapter_md.write_text(_render_chapter_markdown(chapter_id, chapter_title, enriched_events, chapter_review_items), encoding="utf-8")
            written_files.extend([str(chapter_json), str(chapter_md)])

        elapsed = round(time.perf_counter() - started_at, 1)
        print(f"[dialogue-enrich] {index}/{len(chapter_paths)} finished {chapter_id} in {elapsed}s")

    index_json = enrichment_root / "DIALOGUE_ENRICHMENT_INDEX.json"
    index_md = enrichment_root / "DIALOGUE_ENRICHMENT_INDEX.md"
    review_json = review_root / "DIALOGUE_ENRICHMENT_REVIEW_QUEUE.json"
    review_md = review_root / "DIALOGUE_ENRICHMENT_REVIEW_QUEUE.md"

    write_json(
        index_json,
        {
            "project_slug": project_slug,
            "generated_at_utc": _utc_now(),
            "chapter_count": len(chapter_summaries),
            "dialogue_event_count": total_events,
            "explicit_delivery_count": explicit_delivery_count,
            "chapter_summaries": chapter_summaries,
        },
    )
    index_md.write_text(_render_index_markdown(project_slug, chapter_summaries), encoding="utf-8")
    write_json(review_json, review_queue)
    review_md.write_text(_render_review_markdown(review_queue), encoding="utf-8")

    written_files.extend([str(index_json), str(index_md), str(review_json), str(review_md)])
    return DialogueEnrichmentSummary(
        project_slug=project_slug,
        total_chapters=len(chapter_summaries),
        total_events=total_events,
        explicit_delivery_count=explicit_delivery_count,
        review_queue_count=len(review_queue),
        written_files=written_files,
        warnings=warnings,
    )
