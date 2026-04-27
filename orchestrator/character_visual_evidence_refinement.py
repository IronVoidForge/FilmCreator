from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .character_bible_models import CharacterBible, CharacterBibleMetadata
from .character_bible_writer import (
    write_character_bible_index,
    write_character_bible_markdown,
    write_character_bible_review_index,
    write_character_review_queue_markdown,
)
from .core.json_io import read_json, write_json
from .scaffold import create_project

SCHEMA_VERSION = "2026-04-27-character-visual-evidence-v1"

VISUAL_TERMS = {
    "appearance": [
        "hair",
        "eyes",
        "eye",
        "face",
        "skin",
        "wrinkle",
        "wrinkles",
        "beard",
        "moustache",
        "mustache",
        "mouth",
        "nose",
        "head",
        "body",
        "arms",
        "legs",
        "hands",
        "feet",
        "small",
        "large",
        "tall",
        "short",
        "fat",
        "thin",
        "chubby",
        "old",
        "young",
    ],
    "costume": [
        "wore",
        "wears",
        "wearing",
        "dressed",
        "dress",
        "frock",
        "gown",
        "clothes",
        "clothing",
        "suit",
        "uniform",
        "hat",
        "bonnet",
        "sunbonnet",
        "shoes",
        "boots",
        "apron",
        "ribbon",
        "belt",
        "cloak",
        "robe",
        "costume",
        "silk",
        "satin",
        "gingham",
        "checked",
        "checks",
    ],
    "equipment": [
        "axe",
        "oil-can",
        "oil can",
        "cap",
        "spectacles",
        "shoes",
        "staff",
        "basket",
        "sword",
        "knife",
        "lantern",
    ],
    "material_state": [
        "straw",
        "tin",
        "rust",
        "rusted",
        "jointed",
        "painted",
        "stuffed",
        "patched",
        "silver",
        "gold",
        "white",
        "blue",
        "green",
        "red",
        "pink",
        "yellow",
        "purple",
        "brown",
        "black",
        "gray",
        "grey",
    ],
    "movement": [
        "walked",
        "walks",
        "limped",
        "bounded",
        "trotted",
        "bowed",
        "climbed",
        "waddled",
        "flew",
        "fluttered",
        "crawled",
    ],
}

PRONOUNS_BY_KIND = {
    "feminine": {"she", "her", "hers"},
    "masculine": {"he", "him", "his"},
    "neutral": {"it", "its"},
}

WEAK_VALUES = {"", "unknown", "none", "(none)", "n/a", "[]", "[ ]", "null"}
AUTO_PATCH_THRESHOLD = 0.85
VISUAL_OBJECT_PATTERN = (
    "dress|frock|gown|clothes|clothing|hat|bonnet|sunbonnet|shoes|boots|apron|ribbon|belt|cloak|robe|"
    "axe|oil-can|oil can|cap|spectacles|staff|basket|sword|knife|lantern"
)


@dataclass
class VisualEvidenceCandidate:
    character_id: str
    chapter_id: str
    paragraph_index: int
    sentence_index: int
    anchor_type: str
    anchor_text: str
    visual_terms: list[str]
    categories: list[str]
    confidence: float
    risk_flags: list[str]
    snippet: str
    source_path: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "character_id": self.character_id,
            "chapter_id": self.chapter_id,
            "paragraph_index": self.paragraph_index,
            "sentence_index": self.sentence_index,
            "anchor_type": self.anchor_type,
            "anchor_text": self.anchor_text,
            "visual_terms": self.visual_terms,
            "categories": self.categories,
            "confidence": self.confidence,
            "risk_flags": self.risk_flags,
            "snippet": self.snippet,
            "source_path": self.source_path,
        }


@dataclass(frozen=True)
class CharacterVisualEvidenceRefinementSummary:
    project_slug: str
    total_characters: int
    evidence_characters: int
    patched_count: int
    review_count: int
    written_files: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "project_slug": self.project_slug,
            "total_characters": self.total_characters,
            "evidence_characters": self.evidence_characters,
            "patched_count": self.patched_count,
            "review_count": self.review_count,
            "written_files": self.written_files,
            "warnings": self.warnings,
        }


def run_character_visual_evidence_refinement(
    project_slug: str,
    *,
    force: bool = False,
    only_review: bool = False,
    chapters: str | None = None,
    limit: int | None = None,
) -> CharacterVisualEvidenceRefinementSummary:
    project_dir = create_project(project_slug)
    bible_dir = project_dir / "02_story_analysis" / "bibles" / "characters"
    evidence_dir = bible_dir / "visual_evidence"
    review_dir = bible_dir / "review"
    evidence_dir.mkdir(parents=True, exist_ok=True)
    review_dir.mkdir(parents=True, exist_ok=True)

    all_bible_paths = sorted(path for path in bible_dir.glob("CHAR_*.json") if path.is_file())
    bible_paths = list(all_bible_paths)
    if limit is not None and limit >= 0:
        bible_paths = bible_paths[:limit]

    selected_chapters = _parse_chapters(chapters)
    written_files: list[str] = []
    warnings: list[str] = []
    evidence_index: list[dict[str, Any]] = []
    patched_ids: set[str] = set()
    review_ids: set[str] = set()
    records: list[CharacterBible] = []

    for bible_path in bible_paths:
        bible_data = read_json(bible_path)
        if not isinstance(bible_data, dict):
            warnings.append(f"Skipped invalid bible JSON: {bible_path}")
            continue
        character_id = str(bible_data.get("character_id") or bible_path.stem.removeprefix("CHAR_")).strip()
        if not character_id:
            continue
        bible_data, sanitized = _strip_previous_visual_evidence_refinement(bible_data)
        if only_review and not _needs_refinement(bible_data):
            records.append(_bible_from_dict(bible_data))
            continue

        candidate_chapters = _candidate_chapters(bible_data, selected_chapters)
        candidates = find_character_visual_evidence(project_dir, bible_data, candidate_chapters)
        high_confidence = [item for item in candidates if item.confidence >= AUTO_PATCH_THRESHOLD and not item.risk_flags]
        review_candidates = [item for item in candidates if item not in high_confidence and item.confidence >= 0.65]

        evidence_payload = {
            "schema_version": SCHEMA_VERSION,
            "project_slug": project_slug,
            "character_id": character_id,
            "display_name": bible_data.get("display_name") or character_id,
            "generated_at_utc": _utc_now(),
            "candidate_count": len(candidates),
            "auto_patch_count": len(high_confidence),
            "review_candidate_count": len(review_candidates),
            "candidates": [item.to_dict() for item in candidates],
        }
        evidence_json = evidence_dir / f"CHAR_{character_id}_VISUAL_EVIDENCE.json"
        evidence_md = evidence_dir / f"CHAR_{character_id}_VISUAL_EVIDENCE.md"
        if candidates or force:
            write_json(evidence_json, evidence_payload)
            _write_evidence_markdown(evidence_md, evidence_payload)
            written_files.extend([str(evidence_json), str(evidence_md)])

        if candidates:
            evidence_index.append(
                {
                    "character_id": character_id,
                    "candidate_count": len(candidates),
                    "auto_patch_count": len(high_confidence),
                    "review_candidate_count": len(review_candidates),
                    "path": str(evidence_json),
                }
            )

        if high_confidence:
            updated = _merge_evidence_into_bible(bible_data, high_confidence, evidence_json)
            write_json(bible_path, updated)
            bible = _bible_from_dict(updated)
            write_character_bible_markdown(bible_path.with_suffix(".md"), bible)
            written_files.extend([str(bible_path), str(bible_path.with_suffix(".md"))])
            patched_ids.add(character_id)
            records.append(bible)
        else:
            if sanitized:
                write_json(bible_path, bible_data)
                bible = _bible_from_dict(bible_data)
                write_character_bible_markdown(bible_path.with_suffix(".md"), bible)
                written_files.extend([str(bible_path), str(bible_path.with_suffix(".md"))])
                records.append(bible)
            else:
                records.append(_bible_from_dict(bible_data))

        if review_candidates:
            review_ids.add(character_id)

    if limit is None:
        index_payload = {
            "schema_version": SCHEMA_VERSION,
            "project_slug": project_slug,
            "generated_at_utc": _utc_now(),
            "total_records": len(evidence_index),
            "patched_count": len(patched_ids),
            "review_count": len(review_ids),
            "records": evidence_index,
        }
        index_json = evidence_dir / "CHARACTER_VISUAL_EVIDENCE_INDEX.json"
        index_md = evidence_dir / "CHARACTER_VISUAL_EVIDENCE_INDEX.md"
        write_json(index_json, index_payload)
        _write_index_markdown(index_md, index_payload)
        written_files.extend([str(index_json), str(index_md)])
    else:
        warnings.append("Limit mode skipped CHARACTER_VISUAL_EVIDENCE_INDEX rewrite because only a subset was processed.")

    all_records = _load_all_bible_records(all_bible_paths)
    _rewrite_character_bible_indexes(bible_dir, review_dir, all_records)
    written_files.extend(
        [
            str(bible_dir / "CHARACTER_BIBLE_INDEX.json"),
            str(bible_dir / "CHARACTER_BIBLE_INDEX.md"),
            str(bible_dir / "CHARACTER_BIBLE_REVIEW_INDEX.json"),
            str(bible_dir / "CHARACTER_BIBLE_REVIEW_INDEX.md"),
            str(review_dir / "CHARACTER_BIBLE_REVIEW_QUEUE.json"),
            str(review_dir / "CHARACTER_BIBLE_REVIEW_QUEUE.md"),
        ]
    )

    return CharacterVisualEvidenceRefinementSummary(
        project_slug=project_slug,
        total_characters=len(all_bible_paths),
        evidence_characters=len(evidence_index),
        patched_count=len(patched_ids),
        review_count=len(review_ids),
        written_files=_dedupe(written_files),
        warnings=warnings,
    )


def find_character_visual_evidence(
    project_dir: Path,
    bible_data: dict[str, Any],
    chapter_ids: list[str] | None = None,
) -> list[VisualEvidenceCandidate]:
    character_id = str(bible_data.get("character_id") or "").strip()
    aliases = _character_aliases(bible_data)
    if not character_id or not aliases:
        return []
    pronoun_kind = _pronoun_kind(bible_data)
    chapters = chapter_ids or _candidate_chapters(bible_data, set())
    candidates: list[VisualEvidenceCandidate] = []
    source_root = project_dir / "01_source" / "chapters"
    for chapter_id in chapters:
        chapter_path = _chapter_path(source_root, chapter_id)
        if not chapter_path:
            continue
        text = chapter_path.read_text(encoding="utf-8", errors="ignore")
        paragraphs = split_source_into_paragraphs(text)
        for paragraph_index, paragraph in enumerate(paragraphs, start=1):
            sentences = split_sentences(paragraph)
            previous_subject: str | None = None
            for sentence_index, sentence in enumerate(sentences):
                terms_by_category = classify_visual_terms(sentence)
                direct_aliases = _matching_aliases(sentence, aliases)
                if direct_aliases:
                    previous_subject = character_id
                if not terms_by_category:
                    continue
                candidate = _candidate_from_sentence(
                    character_id=character_id,
                    aliases=aliases,
                    pronoun_kind=pronoun_kind,
                    chapter_id=chapter_id,
                    paragraph_index=paragraph_index,
                    sentence_index=sentence_index,
                    sentence=sentence,
                    previous_sentence=sentences[sentence_index - 1] if sentence_index > 0 else "",
                    next_sentence=sentences[sentence_index + 1] if sentence_index + 1 < len(sentences) else "",
                    previous_subject=previous_subject,
                    terms_by_category=terms_by_category,
                    source_path=str(chapter_path),
                )
                if candidate and candidate.confidence >= 0.65:
                    candidates.append(candidate)
    return _dedupe_candidates(candidates)


def split_source_into_paragraphs(text: str) -> list[str]:
    cleaned = text.replace("\r\n", "\n").replace("\r", "\n")
    paragraphs = [re.sub(r"\s+", " ", part).strip() for part in re.split(r"\n\s*\n+", cleaned)]
    return [part for part in paragraphs if part and not part.startswith("#")]


def split_sentences(paragraph: str) -> list[str]:
    pieces = re.split(r"(?<=[.!?])\s+(?=[\"'A-Z])", paragraph.strip())
    return [piece.strip() for piece in pieces if piece.strip()]


def classify_visual_terms(text: str) -> dict[str, list[str]]:
    normalized = text.lower()
    found: dict[str, list[str]] = {}
    for category, terms in VISUAL_TERMS.items():
        category_terms: list[str] = []
        for term in terms:
            if re.search(rf"\b{re.escape(term)}\b", normalized):
                category_terms.append(term)
        if category_terms:
            found[category] = category_terms
    return found


def _candidate_from_sentence(
    *,
    character_id: str,
    aliases: list[str],
    pronoun_kind: str,
    chapter_id: str,
    paragraph_index: int,
    sentence_index: int,
    sentence: str,
    previous_sentence: str,
    next_sentence: str,
    previous_subject: str | None,
    terms_by_category: dict[str, list[str]],
    source_path: str,
) -> VisualEvidenceCandidate | None:
    anchor_type = ""
    confidence = 0.0
    anchor_text = ""
    risk_flags: list[str] = []

    possessive_alias = _possessive_alias_match(sentence, aliases)
    direct_aliases = _matching_aliases(sentence, aliases)
    if possessive_alias and _has_possessive_visual_object(sentence, possessive_alias):
        anchor_type = "possession"
        confidence = 0.94
        anchor_text = possessive_alias
    elif direct_aliases:
        anchor_type = "direct_name"
        anchor_text = direct_aliases[0]
        if _has_direct_visual_ownership_or_state(sentence, direct_aliases[0], terms_by_category):
            confidence = 0.9
        else:
            confidence = 0.72
            risk_flags.append("weak_direct_anchor")
    elif previous_subject == character_id and _has_character_continuity_reference(sentence, pronoun_kind):
        anchor_type = "pronoun_continuity"
        confidence = 0.78
        anchor_text = _first_pronoun(sentence, pronoun_kind) or "continuity_reference"
        if _has_competing_subject(previous_sentence, sentence, aliases):
            risk_flags.append("competing_subject_near_pronoun")
    else:
        return None

    if _looks_like_dialogue_only(sentence):
        risk_flags.append("dialogue_only")
        confidence -= 0.08
    if _looks_like_environment_description(sentence):
        risk_flags.append("possible_environment_description")
        confidence -= 0.12
    if _mentions_multiple_named_subjects(sentence, aliases):
        risk_flags.append("multiple_named_subjects")
        confidence -= 0.1

    snippet = _context_snippet(previous_sentence, sentence, next_sentence)
    terms = sorted({term for values in terms_by_category.values() for term in values})
    categories = sorted(terms_by_category)
    return VisualEvidenceCandidate(
        character_id=character_id,
        chapter_id=chapter_id,
        paragraph_index=paragraph_index,
        sentence_index=sentence_index + 1,
        anchor_type=anchor_type,
        anchor_text=anchor_text,
        visual_terms=terms,
        categories=categories,
        confidence=round(max(0.0, min(confidence, 0.99)), 2),
        risk_flags=risk_flags,
        snippet=snippet,
        source_path=source_path,
    )


def _merge_evidence_into_bible(
    bible_data: dict[str, Any],
    evidence: list[VisualEvidenceCandidate],
    evidence_path: Path,
) -> dict[str, Any]:
    updated = dict(bible_data)
    snippets = [_clean_snippet(item.snippet, limit=240) for item in evidence]
    costume_snippets = [item for item in evidence if any(cat in item.categories for cat in ["costume", "equipment"])]
    trait_snippets = [item for item in evidence if any(cat in item.categories for cat in ["appearance", "material_state"])]
    movement_snippets = [item for item in evidence if "movement" in item.categories]

    if costume_snippets:
        updated["costume_signature"] = _merge_scalar(
            updated.get("costume_signature"),
            _evidence_phrase(costume_snippets, "Source-supported costume/equipment"),
        )
    if trait_snippets:
        updated["physical_traits"] = _merge_list(
            updated.get("physical_traits"),
            _evidence_list(trait_snippets, "source visual"),
        )
        updated["distinguishing_features"] = _merge_list(
            updated.get("distinguishing_features"),
            _evidence_list(trait_snippets + costume_snippets, "source-supported"),
        )
    if movement_snippets:
        updated["movement_language"] = _merge_scalar(
            updated.get("movement_language"),
            _evidence_phrase(movement_snippets, "Source-supported movement"),
        )

    summary_addition = "Recovered visual evidence: " + " ".join(snippets[:3])
    updated["stable_visual_summary"] = _merge_scalar(updated.get("stable_visual_summary"), summary_addition)

    evidence_summary = _merge_list(
        updated.get("evidence_summary"),
        [f"[visual-evidence:{item.chapter_id} p{item.paragraph_index}] {item.snippet}" for item in evidence[:8]],
    )
    updated["evidence_summary"] = evidence_summary
    updated["evidence_refs"] = _merge_refs(updated.get("evidence_refs"), evidence, evidence_path)
    updated["unresolved_ambiguities"] = _filter_resolved_ambiguities(updated.get("unresolved_ambiguities"), updated)
    updated.setdefault("metadata", {})
    if isinstance(updated["metadata"], dict):
        updated["metadata"]["updated_at_utc"] = _utc_now()
        history = updated["metadata"].setdefault("revision_history", [])
        if isinstance(history, list):
            history.append(
                {
                    "timestamp_utc": _utc_now(),
                    "action": "character_visual_evidence_refinement",
                    "source_path": str(evidence_path),
                    "auto_patch_count": len(evidence),
                }
            )
        deps = updated["metadata"].setdefault("upstream_dependencies", [])
        if isinstance(deps, list):
            deps.append(
                {
                    "dependency_type": "character_visual_evidence",
                    "dependency_id": updated.get("character_id"),
                    "source_path": str(evidence_path),
                }
            )
    return updated


def _strip_previous_visual_evidence_refinement(data: dict[str, Any]) -> tuple[dict[str, Any], bool]:
    updated = dict(data)
    changed = False
    scalar_markers = [
        "Recovered visual evidence:",
        " Recovered visual evidence:",
        "Source-supported costume/equipment:",
        " Source-supported costume/equipment:",
        "Source-supported movement:",
        " Source-supported movement:",
    ]
    for field_name in ["stable_visual_summary", "costume_signature", "movement_language"]:
        value = str(updated.get(field_name) or "")
        cleaned = value
        for marker in scalar_markers:
            if marker in cleaned:
                cleaned = cleaned.split(marker, 1)[0].rstrip()
        if cleaned != value:
            updated[field_name] = cleaned
            changed = True

    for field_name in ["physical_traits", "distinguishing_features"]:
        values = _string_list(updated.get(field_name))
        cleaned_values = [
            item
            for item in values
            if not item.lower().startswith(("source visual evidence", "source-supported evidence"))
        ]
        if cleaned_values != values:
            updated[field_name] = cleaned_values
            changed = True

    evidence_summary = _string_list(updated.get("evidence_summary"))
    cleaned_summary = [item for item in evidence_summary if not item.startswith("[visual-evidence:")]
    if cleaned_summary != evidence_summary:
        updated["evidence_summary"] = cleaned_summary
        changed = True

    refs = updated.get("evidence_refs")
    if isinstance(refs, list):
        cleaned_refs = [item for item in refs if not (isinstance(item, dict) and item.get("source") == "character_visual_evidence")]
        if cleaned_refs != refs:
            updated["evidence_refs"] = cleaned_refs
            changed = True

    return updated, changed


def _rewrite_character_bible_indexes(bible_dir: Path, review_dir: Path, records: list[CharacterBible]) -> None:
    main_records = [record for record in records if record.status == "canonical" and record.entity_kind == "individual"]
    review_records = [
        record
        for record in records
        if record.status != "canonical" or record.entity_kind != "individual" or record.unresolved_ambiguities
    ]
    review_queue = [{"character_id": record.character_id, "issues": record.unresolved_ambiguities} for record in review_records if record.unresolved_ambiguities]
    write_character_bible_index(bible_dir / "CHARACTER_BIBLE_INDEX.md", main_records)
    write_character_bible_review_index(bible_dir / "CHARACTER_BIBLE_REVIEW_INDEX.md", review_records)
    write_json(bible_dir / "CHARACTER_BIBLE_INDEX.json", [record.to_dict() for record in sorted(main_records, key=lambda item: item.character_id)])
    write_json(bible_dir / "CHARACTER_BIBLE_REVIEW_INDEX.json", [record.to_dict() for record in sorted(review_records, key=lambda item: item.character_id)])
    write_json(review_dir / "CHARACTER_BIBLE_REVIEW_QUEUE.json", review_queue)
    write_character_review_queue_markdown(review_dir / "CHARACTER_BIBLE_REVIEW_QUEUE.md", review_queue)


def _load_all_bible_records(paths: list[Path]) -> list[CharacterBible]:
    records: list[CharacterBible] = []
    for path in paths:
        data = read_json(path)
        if isinstance(data, dict):
            records.append(_bible_from_dict(data))
    return records


def _bible_from_dict(data: dict[str, Any]) -> CharacterBible:
    metadata_data = data.get("metadata") if isinstance(data.get("metadata"), dict) else {}
    metadata = CharacterBibleMetadata(
        artifact_id=str(metadata_data.get("artifact_id") or f"CHAR_{data.get('character_id', '')}"),
        artifact_type=str(metadata_data.get("artifact_type") or "character_bible"),
        status=str(metadata_data.get("status") or "generated"),
        source_fingerprint=metadata_data.get("source_fingerprint"),
        created_at_utc=str(metadata_data.get("created_at_utc") or ""),
        updated_at_utc=str(metadata_data.get("updated_at_utc") or ""),
        upstream_dependencies=metadata_data.get("upstream_dependencies") if isinstance(metadata_data.get("upstream_dependencies"), list) else [],
        locked_fields=metadata_data.get("locked_fields") if isinstance(metadata_data.get("locked_fields"), dict) else {},
        manual_overrides=metadata_data.get("manual_overrides") if isinstance(metadata_data.get("manual_overrides"), dict) else {},
        revision_history=metadata_data.get("revision_history") if isinstance(metadata_data.get("revision_history"), list) else [],
    )
    return CharacterBible(
        character_id=str(data.get("character_id") or ""),
        display_name=str(data.get("display_name") or data.get("character_id") or ""),
        aliases=_string_list(data.get("aliases")),
        status=str(data.get("status") or "canonical"),
        entity_kind=str(data.get("entity_kind") or "individual"),
        first_seen_chapter=data.get("first_seen_chapter"),
        last_seen_chapter=data.get("last_seen_chapter"),
        chapter_mentions=_string_list(data.get("chapter_mentions")),
        identity_baseline=str(data.get("identity_baseline") or ""),
        age_presence=str(data.get("age_presence") or ""),
        physical_build=str(data.get("physical_build") or ""),
        origin_or_historical_context=str(data.get("origin_or_historical_context") or ""),
        movement_language=str(data.get("movement_language") or ""),
        stable_visual_summary=str(data.get("stable_visual_summary") or ""),
        physical_traits=_string_list(data.get("physical_traits")),
        costume_signature=str(data.get("costume_signature") or ""),
        distinguishing_features=_string_list(data.get("distinguishing_features")),
        state_variants=_string_list(data.get("state_variants")),
        personality=str(data.get("personality") or ""),
        role=str(data.get("role") or ""),
        voice_notes=str(data.get("voice_notes") or ""),
        relationship_notes=_string_list(data.get("relationship_notes")),
        continuity_constraints=_string_list(data.get("continuity_constraints")),
        unresolved_ambiguities=_string_list(data.get("unresolved_ambiguities")),
        entity_taxonomy=data.get("entity_taxonomy") if isinstance(data.get("entity_taxonomy"), dict) else {},
        alias_resolution=data.get("alias_resolution") if isinstance(data.get("alias_resolution"), dict) else {},
        associated_entities=data.get("associated_entities") if isinstance(data.get("associated_entities"), list) else [],
        evidence_refs=data.get("evidence_refs") if isinstance(data.get("evidence_refs"), list) else [],
        evidence_summary=_string_list(data.get("evidence_summary")),
        visual_production_fallback=data.get("visual_production_fallback") if isinstance(data.get("visual_production_fallback"), dict) else {},
        metadata=metadata,
    )


def _character_aliases(bible_data: dict[str, Any]) -> list[str]:
    aliases = [str(bible_data.get("display_name") or ""), str(bible_data.get("character_id") or "").replace("_", " ")]
    aliases.extend(_string_list(bible_data.get("aliases")))
    aliases.extend(_article_aliases(aliases))
    return sorted(_dedupe([alias for alias in aliases if len(alias.strip()) >= 3]), key=len, reverse=True)


def _article_aliases(aliases: list[str]) -> list[str]:
    out: list[str] = []
    for alias in aliases:
        normalized = re.sub(r"\s+", " ", str(alias or "").strip().lower())
        if not normalized:
            continue
        if normalized.startswith("the "):
            out.append(normalized.removeprefix("the "))
        else:
            out.append(f"the {normalized}")
    return out


def _pronoun_kind(bible_data: dict[str, Any]) -> str:
    text = " ".join(str(bible_data.get(key) or "") for key in ["display_name", "identity_baseline", "role", "stable_visual_summary"]).lower()
    if any(term in text for term in ["girl", "woman", "aunt", "mother", "sister", "daughter", "queen", "princess", "wife"]):
        return "feminine"
    if any(term in text for term in ["man", "boy", "father", "brother", "son", "king", "prince", "uncle", "husband"]):
        return "masculine"
    return "neutral"


def _candidate_chapters(bible_data: dict[str, Any], selected_chapters: set[str]) -> list[str]:
    mentions = _string_list(bible_data.get("chapter_mentions"))
    if selected_chapters:
        mentions = [chapter for chapter in mentions if chapter in selected_chapters]
    if not mentions:
        for key in ["first_seen_chapter", "last_seen_chapter"]:
            chapter = str(bible_data.get(key) or "").strip()
            if chapter:
                mentions.append(chapter)
    return _dedupe(mentions)


def _parse_chapters(chapters: str | None) -> set[str]:
    if not chapters:
        return set()
    out: set[str] = set()
    for part in str(chapters).split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            start_s, end_s = part.split("-", 1)
            for number in range(int(start_s), int(end_s) + 1):
                out.add(f"CH{number:03d}")
        else:
            out.add(f"CH{int(part):03d}" if part.isdigit() else part.upper())
    return out


def _chapter_path(source_root: Path, chapter_id: str) -> Path | None:
    matches = sorted(source_root.glob(f"{chapter_id}_*.md"))
    if matches:
        return matches[0]
    direct = source_root / f"{chapter_id}.md"
    return direct if direct.exists() else None


def _matching_aliases(text: str, aliases: list[str]) -> list[str]:
    normalized = text.lower()
    return [alias for alias in aliases if re.search(rf"\b{re.escape(alias.lower())}\b", normalized)]


def _possessive_alias_match(text: str, aliases: list[str]) -> str:
    normalized = text.lower()
    for alias in aliases:
        escaped = re.escape(alias.lower())
        if re.search(rf"\b{escaped}(?:'s|')\b", normalized):
            return alias
    return ""


def _has_character_pronoun(text: str, pronoun_kind: str) -> bool:
    pronouns = PRONOUNS_BY_KIND.get(pronoun_kind, PRONOUNS_BY_KIND["neutral"])
    normalized = text.lower()
    return any(re.search(rf"\b{pronoun}\b", normalized) for pronoun in pronouns)


def _first_pronoun(text: str, pronoun_kind: str) -> str:
    pronouns = PRONOUNS_BY_KIND.get(pronoun_kind, PRONOUNS_BY_KIND["neutral"])
    normalized = text.lower()
    for pronoun in pronouns:
        if re.search(rf"\b{pronoun}\b", normalized):
            return pronoun
    return ""


def _has_character_continuity_reference(text: str, pronoun_kind: str) -> bool:
    if _has_character_pronoun(text, pronoun_kind):
        return True
    normalized = text.lower()
    return bool(
        re.search(
            r"\b(?:the rest of|rest of|the figure|the body|the head|the face|the hands|the arms|the legs|the clothes|the clothing|the costume)\b",
            normalized,
        )
    )


def _has_competing_subject(previous_sentence: str, sentence: str, aliases: list[str]) -> bool:
    text = f"{previous_sentence} {sentence}"
    alias_hits = _matching_aliases(text, aliases)
    proper_nouns = set(re.findall(r"\b[A-Z][a-z]{2,}(?:\s+[A-Z][a-z]{2,}){0,2}\b", text))
    role_terms = {
        term
        for term in re.findall(
            r"\b(?:girl|boy|woman|man|child|mother|father|aunt|uncle|sister|brother|queen|king|princess|prince|soldier|guard|servant|farmer|keeper|captain|leader|creature|beast|animal)\b",
            text.lower(),
        )
    }
    normalized_aliases = {alias.lower().removeprefix("the ") for alias in aliases}
    competing_roles = {term for term in role_terms if term not in normalized_aliases}
    return len(proper_nouns) + len(competing_roles) > max(2, len(alias_hits) + 1)


def _mentions_multiple_named_subjects(sentence: str, aliases: list[str]) -> bool:
    alias_hits = _matching_aliases(sentence, aliases)
    proper_nouns = set(re.findall(r"\b[A-Z][a-z]{2,}(?:\s+[A-Z][a-z]{2,}){0,2}\b", sentence))
    normalized_aliases = {alias.lower() for alias in aliases}
    non_alias_names = {
        name
        for name in proper_nouns
        if name.lower() not in normalized_aliases and f"the {name.lower()}" not in normalized_aliases
    }
    return bool(alias_hits and non_alias_names)


def _looks_like_dialogue_only(sentence: str) -> bool:
    stripped = sentence.strip()
    return stripped.startswith(("\"", "'", "“")) and not any(term in stripped.lower() for term in ["said", "answered", "cried", "asked"])


def _looks_like_environment_description(sentence: str) -> bool:
    normalized = sentence.lower()
    return any(term in normalized for term in ["room was", "country was", "field was", "road was", "house was", "walls were"]) and not any(
        term in normalized for term in ["wore", "dressed", "hair", "eyes", "face", "shoes", "hat", "body"]
    )


def _has_direct_visual_ownership_or_state(sentence: str, alias: str, terms_by_category: dict[str, list[str]]) -> bool:
    normalized = sentence.lower()
    escaped = re.escape(alias.lower())
    has_costume_or_equipment = any(category in terms_by_category for category in ["costume", "equipment"])

    if _has_possessive_visual_object(sentence, alias):
        return True
    if has_costume_or_equipment and re.search(
        rf"\b{escaped}\b[^.!?;:,\"]{{0,80}}\b(?:wore|wears|wearing|put on|carried|held)\b[^.!?;:,\"]{{0,80}}\b(?:{VISUAL_OBJECT_PATTERN})\b",
        normalized,
    ):
        return True
    if has_costume_or_equipment and re.search(
        rf"\b{escaped}\b[^.!?;:,\"]{{0,80}}\b(?:had|has)\b(?:\s+(?:a|an|the|one|only|other|[\w-]+)){{0,6}}\s+\b(?:{VISUAL_OBJECT_PATTERN})\b",
        normalized,
    ):
        return True
    if has_costume_or_equipment and re.search(
        rf"\b{escaped}\b[^.!?;:,\"]{{0,40}}\b(?:was|is|were|are)\b[^.!?;:,\"]{{0,20}}\bdressed\b[^.!?;:,\"]{{0,80}}\b(?:{VISUAL_OBJECT_PATTERN})\b",
        normalized,
    ):
        return True
    if has_costume_or_equipment and re.search(
        rf"\b(?:wore|wears|wearing|put on|carried|held)\b[^.!?;:,\"]{{0,80}}\b(?:{VISUAL_OBJECT_PATTERN})\b[^.!?;:,\"]{{0,80}}\b{escaped}\b",
        normalized,
    ):
        return True
    if has_costume_or_equipment and re.search(rf"\b(?:handed|gave|fitted|put)\b[^.!?;:]{{0,120}}\b(?:to|on|over)\b[^.!?;:]{{0,40}}\b{escaped}\b", normalized):
        return True
    if re.search(rf"\b(my|my own)\b[^.!?;:]{{0,80}}\b(?:dress|shoes|hat|bonnet|gown|hair|face|hands|feet|body)\b[^.!?;:]{{0,120}}\bsaid\b[^.!?;:]{{0,40}}\b{escaped}\b", normalized):
        return True
    return False


def _has_possessive_visual_object(sentence: str, alias: str) -> bool:
    normalized = sentence.lower()
    escaped = re.escape(alias.lower())
    return bool(re.search(rf"\b{escaped}(?:'s|')\b[^.!?;:,\"]{{0,40}}\b(?:{VISUAL_OBJECT_PATTERN})\b", normalized))


def _context_snippet(previous_sentence: str, sentence: str, next_sentence: str) -> str:
    parts = [part.strip() for part in [previous_sentence, sentence, next_sentence] if part.strip()]
    return _clean_snippet(" ".join(parts), limit=420)


def _clean_snippet(text: str, *, limit: int) -> str:
    compact = re.sub(r"\s+", " ", text).strip()
    return compact if len(compact) <= limit else compact[: limit - 3].rstrip() + "..."


def _dedupe_candidates(candidates: list[VisualEvidenceCandidate]) -> list[VisualEvidenceCandidate]:
    out: list[VisualEvidenceCandidate] = []
    seen: set[tuple[str, int, int]] = set()
    for candidate in sorted(candidates, key=lambda item: (-item.confidence, item.chapter_id, item.paragraph_index, item.sentence_index)):
        key = (candidate.chapter_id, candidate.paragraph_index, candidate.sentence_index)
        if key in seen:
            continue
        seen.add(key)
        out.append(candidate)
    return out


def _needs_refinement(data: dict[str, Any]) -> bool:
    fields = [
        data.get("physical_build"),
        data.get("movement_language"),
        data.get("costume_signature"),
        data.get("stable_visual_summary"),
    ]
    if any(_is_weak(field) for field in fields):
        return True
    if data.get("visual_production_fallback"):
        return True
    return bool(_string_list(data.get("unresolved_ambiguities")))


def _is_weak(value: Any) -> bool:
    if isinstance(value, list):
        return not [item for item in value if not _is_weak(item)]
    text = str(value or "").strip().lower()
    return text in WEAK_VALUES


def _merge_scalar(existing: Any, addition: str) -> str:
    existing_text = str(existing or "").strip()
    addition = addition.strip()
    if not addition:
        return existing_text
    if _is_weak(existing_text):
        return addition
    if addition.lower() in existing_text.lower():
        return existing_text
    return f"{existing_text} {addition}"


def _merge_list(existing: Any, additions: list[str]) -> list[str]:
    return _dedupe([*_string_list(existing), *additions])


def _evidence_phrase(evidence: list[VisualEvidenceCandidate], prefix: str) -> str:
    snippets = [_clean_snippet(item.snippet, limit=180) for item in evidence[:3]]
    return f"{prefix}: " + " | ".join(snippets)


def _evidence_list(evidence: list[VisualEvidenceCandidate], prefix: str) -> list[str]:
    values: list[str] = []
    for item in evidence[:6]:
        values.append(f"{prefix} evidence ({item.chapter_id}): {_clean_snippet(item.snippet, limit=180)}")
    return values


def _merge_refs(existing: Any, evidence: list[VisualEvidenceCandidate], evidence_path: Path) -> list[dict[str, Any]]:
    refs = [item for item in existing if isinstance(item, dict)] if isinstance(existing, list) else []
    for item in evidence:
        refs.append(
            {
                "source": "character_visual_evidence",
                "chapter_id": item.chapter_id,
                "source_path": item.source_path,
                "evidence_path": str(evidence_path),
                "paragraph_index": item.paragraph_index,
                "sentence_index": item.sentence_index,
                "confidence": item.confidence,
            }
        )
    out: list[dict[str, Any]] = []
    seen: set[str] = set()
    for ref in refs:
        key = json.dumps(ref, sort_keys=True, ensure_ascii=False)
        if key not in seen:
            seen.add(key)
            out.append(ref)
    return out


def _filter_resolved_ambiguities(ambiguities: Any, data: dict[str, Any]) -> list[str]:
    out: list[str] = []
    has_costume = not _is_weak(data.get("costume_signature"))
    has_traits = bool(_string_list(data.get("physical_traits")) or _string_list(data.get("distinguishing_features")))
    has_movement = not _is_weak(data.get("movement_language"))
    for item in _string_list(ambiguities):
        lowered = item.lower()
        if has_costume and any(term in lowered for term in ["costume", "clothing", "attire"]):
            continue
        if has_traits and any(term in lowered for term in ["physical", "facial", "hair", "visual appearance", "specific visual"]):
            continue
        if has_movement and "movement" in lowered:
            continue
        out.append(item)
    return out


def _write_evidence_markdown(path: Path, payload: dict[str, Any]) -> None:
    lines = [
        f"# Character Visual Evidence: {payload.get('character_id')}",
        "",
        f"- candidate_count: {payload.get('candidate_count', 0)}",
        f"- auto_patch_count: {payload.get('auto_patch_count', 0)}",
        f"- review_candidate_count: {payload.get('review_candidate_count', 0)}",
        "",
    ]
    for item in payload.get("candidates", []):
        lines.append(f"## {item.get('chapter_id')} p{item.get('paragraph_index')} s{item.get('sentence_index')}")
        lines.append("")
        lines.append(f"- anchor_type: {item.get('anchor_type')}")
        lines.append(f"- confidence: {item.get('confidence')}")
        lines.append(f"- visual_terms: {', '.join(item.get('visual_terms', []))}")
        lines.append(f"- risk_flags: {', '.join(item.get('risk_flags', [])) if item.get('risk_flags') else '(none)'}")
        lines.append("")
        lines.append(str(item.get("snippet", "")))
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def _write_index_markdown(path: Path, payload: dict[str, Any]) -> None:
    lines = ["# Character Visual Evidence Index", ""]
    for item in payload.get("records", []):
        lines.append(
            f"- `{item.get('character_id')}` candidates={item.get('candidate_count')} "
            f"auto_patch={item.get('auto_patch_count')} review={item.get('review_candidate_count')}"
        )
    if not payload.get("records"):
        lines.append("- No visual evidence candidates found.")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _string_list(value: Any) -> list[str]:
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip() and str(item).strip() not in {"[]", "[ ]"}]
    if isinstance(value, str) and value.strip():
        return [value.strip()]
    return []


def _dedupe(items: list[str]) -> list[str]:
    out: list[str] = []
    seen: set[str] = set()
    for item in items:
        cleaned = str(item).strip()
        key = cleaned.lower()
        if cleaned and key not in seen:
            seen.add(key)
            out.append(cleaned)
    return out


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()
