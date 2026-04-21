from __future__ import annotations

from pathlib import Path
from typing import Any

from .character_bible_models import CharacterBible


def write_character_bible_markdown(path: Path, bible: CharacterBible) -> None:
    lines = [
        f"# Character Bible: {bible.display_name}",
        "",
        f"- character_id: `{bible.character_id}`",
        f"- status: `{bible.status}`",
        f"- entity_kind: `{bible.entity_kind}`",
        f"- first_seen_chapter: `{bible.first_seen_chapter}`",
        f"- last_seen_chapter: `{bible.last_seen_chapter}`",
        "",
        "## Identity",
        "",
        f"- display_name: {bible.display_name}",
        f"- aliases: {', '.join(bible.aliases) if bible.aliases else '(none)'}",
        f"- chapter_mentions: {', '.join(bible.chapter_mentions) if bible.chapter_mentions else '(none)'}",
        "",
        "## Visual Bible",
        "",
        f"- identity_baseline: {bible.identity_baseline or '(none)'}",
        f"- age_presence: {bible.age_presence or '(none)'}",
        f"- physical_build: {bible.physical_build or '(none)'}",
        f"- origin_or_historical_context: {bible.origin_or_historical_context or '(none)'}",
        f"- movement_language: {bible.movement_language or '(none)'}",
        bible.stable_visual_summary or "(no stable visual summary yet)",
        "",
        f"- physical_traits: {', '.join(bible.physical_traits) if bible.physical_traits else '(none)'}",
        f"- costume_signature: {bible.costume_signature or '(none)'}",
        f"- distinguishing_features: {', '.join(bible.distinguishing_features) if bible.distinguishing_features else '(none)'}",
        f"- state_variants: {', '.join(bible.state_variants) if bible.state_variants else '(none)'}",
        "",
        "## Behavioral Bible",
        "",
        f"- personality: {bible.personality or '(none)'}",
        f"- role: {bible.role or '(none)'}",
        f"- voice_notes: {bible.voice_notes or '(none)'}",
        f"- relationship_notes: {', '.join(bible.relationship_notes) if bible.relationship_notes else '(none)'}",
        "",
        "## Continuity",
        "",
        f"- continuity_constraints: {', '.join(bible.continuity_constraints) if bible.continuity_constraints else '(none)'}",
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


def write_character_bible_index(index_path: Path, records: list[CharacterBible]) -> None:
    lines = ["# Character Bible Index", ""]
    for record in sorted(records, key=lambda item: item.character_id):
        lines.append(
            f"- `{record.character_id}` â€” {record.display_name} "
            f"(status={record.status}, mentions={len(record.chapter_mentions)}, ambiguities={len(record.unresolved_ambiguities)})"
        )
    index_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_character_bible_review_index(index_path: Path, records: list[CharacterBible]) -> None:
    lines = ["# Character Bible Review Index", ""]
    if not records:
        lines.append("- No review entries.")
        index_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        return

    for record in sorted(records, key=lambda item: item.character_id):
        flags: list[str] = []
        if record.status != "canonical":
            flags.append(f"status={record.status}")
        if record.entity_kind != "individual":
            flags.append(f"entity_kind={record.entity_kind}")
        if record.unresolved_ambiguities:
            flags.append(f"ambiguities={len(record.unresolved_ambiguities)}")
        flag_text = ", ".join(flags) if flags else "review"
        lines.append(f"- `{record.character_id}` â€” {record.display_name} ({flag_text})")

    index_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_character_review_queue_markdown(path: Path, queue: list[dict[str, Any]]) -> None:
    lines = ["# Character Bible Review Queue", ""]
    if not queue:
        lines.append("- No character bible review items.")
    else:
        for item in queue:
            lines.append(f"- `{item.get('character_id')}`")
            for issue in item.get("issues", []):
                lines.append(f"  - {issue}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
