from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .book_librarian import search_chapter_context
from .features.world.global_helpers import (
    global_character_registry_path,
    is_generic_character_label,
    load_json,
    normalize_alias_token,
)
from .scaffold import create_project


@dataclass(frozen=True)
class CharacterMatchCandidate:
    canonical_id: str
    display_name: str
    score: int
    reasons: list[str]
    source_paths: list[str]
    source_chapters: list[str]
    context_snippets: list[str]
    aliases: list[str]

    def to_dict(self) -> dict[str, object]:
        return {
            "canonical_id": self.canonical_id,
            "display_name": self.display_name,
            "score": self.score,
            "reasons": self.reasons,
            "source_paths": self.source_paths,
            "source_chapters": self.source_chapters,
            "context_snippets": self.context_snippets,
            "aliases": self.aliases,
        }


def find_character_match_candidates(
    *,
    project_slug: str,
    asset_id: str,
    aliases: str,
    markdown: str,
    top_n: int = 3,
) -> list[CharacterMatchCandidate]:
    registry = _load_character_registries(project_slug)
    if not registry:
        return []

    query_tokens = _query_tokens(asset_id=asset_id, aliases=aliases, markdown=markdown)
    candidates: list[CharacterMatchCandidate] = []
    for canonical_id, entry in registry.items():
        score, reasons = _score_candidate(
            canonical_id=canonical_id,
            entry=entry,
            query_tokens=query_tokens,
            asset_id=asset_id,
            aliases=aliases,
            markdown=markdown,
        )
        if score <= 0:
            continue
        source_paths = [str(path) for path in entry.get("sources", []) if isinstance(path, str)]
        source_chapters = _source_chapters_from_paths(source_paths)
        context_snippets = _source_context_snippets(
            project_slug=project_slug,
            source_chapters=source_chapters,
            query_terms=[asset_id, *aliases.splitlines(), str(entry.get("display_name", ""))],
        )
        candidates.append(
            CharacterMatchCandidate(
                canonical_id=canonical_id,
                display_name=str(entry.get("display_name", canonical_id)),
                score=score,
                reasons=reasons,
                source_paths=source_paths,
                source_chapters=source_chapters,
                context_snippets=context_snippets,
                aliases=[str(alias) for alias in entry.get("aliases", []) if isinstance(alias, str)],
            )
        )
    candidates.sort(key=lambda candidate: (-candidate.score, candidate.canonical_id))
    return candidates[:top_n]


def _load_character_registries(project_slug: str) -> dict[str, dict]:
    registries: dict[str, dict] = {}
    registry_paths = [
        global_character_registry_path(project_slug),
        create_project(project_slug) / "02_story_analysis" / "world" / "CHARACTER_REGISTRY.json",
    ]
    for registry_path in registry_paths:
        if not registry_path.exists():
            continue
        payload = load_json(registry_path, {})
        if not isinstance(payload, dict):
            continue
        for canonical_id, entry in payload.items():
            if not isinstance(entry, dict):
                continue
            merged = registries.setdefault(
                canonical_id,
                {
                    "canonical_id": canonical_id,
                    "display_name": entry.get("display_name", canonical_id),
                    "aliases": [],
                    "sources": [],
                    "status": entry.get("status", "canonical"),
                    "entity_kind": entry.get("entity_kind", "individual"),
                    "resolution_reason": entry.get("resolution_reason", ""),
                },
            )
            for key in ("display_name", "status", "entity_kind", "resolution_reason"):
                if entry.get(key):
                    merged[key] = entry.get(key)
            for alias in entry.get("aliases", []):
                if isinstance(alias, str) and alias not in merged["aliases"]:
                    merged["aliases"].append(alias)
            for source in entry.get("sources", []):
                if isinstance(source, str) and source not in merged["sources"]:
                    merged["sources"].append(source)
    return registries


def _query_tokens(*, asset_id: str, aliases: str, markdown: str) -> set[str]:
    tokens = {normalize_alias_token(asset_id)}
    tokens |= {normalize_alias_token(alias) for alias in aliases.splitlines()}
    tokens |= {normalize_alias_token(alias) for alias in aliases.split(",")}
    tokens |= {normalize_alias_token(token) for token in markdown.split() if len(token.strip()) > 2}
    tokens.discard("")
    return tokens


def _score_candidate(
    *,
    canonical_id: str,
    entry: dict,
    query_tokens: set[str],
    asset_id: str,
    aliases: str,
    markdown: str,
) -> tuple[int, list[str]]:
    reasons: list[str] = []
    score = 0
    candidate_tokens = _candidate_tokens(canonical_id=canonical_id, entry=entry)
    normalized_asset_id = normalize_alias_token(asset_id)
    if normalized_asset_id and normalized_asset_id == normalize_alias_token(canonical_id):
        score += 60
        reasons.append("asset id exactly matches canonical id")
    for alias in [canonical_id, str(entry.get("display_name", "")), *entry.get("aliases", [])]:
        alias_token = normalize_alias_token(alias)
        if alias_token and alias_token == normalized_asset_id:
            score += 55
            reasons.append(f"query matches alias '{alias_token}'")
    overlap = query_tokens & candidate_tokens
    if overlap:
        score += 6 * len(overlap)
        reasons.append(f"token overlap: {sorted(overlap)}")
    if is_generic_character_label(asset_id) or is_generic_character_label(str(entry.get("display_name", ""))):
        score -= 10
        reasons.append("generic role label reduces confidence")
    if _source_contains_query(entry, markdown, query_tokens):
        score += 10
        reasons.append("source context shares query language")
    return score, reasons


def _candidate_tokens(*, canonical_id: str, entry: dict) -> set[str]:
    tokens = {
        normalize_alias_token(canonical_id),
        normalize_alias_token(str(entry.get("display_name", ""))),
    }
    for alias in entry.get("aliases", []):
        tokens.add(normalize_alias_token(str(alias)))
    tokens.discard("")
    return tokens


def _source_contains_query(entry: dict, markdown: str, query_tokens: set[str]) -> bool:
    candidate_text = " ".join(
        [
            str(entry.get("display_name", "")),
            str(entry.get("resolution_reason", "")),
            " ".join(str(alias) for alias in entry.get("aliases", [])),
            markdown,
        ]
    ).lower()
    return any(token and token in candidate_text for token in query_tokens)


def _source_chapters_from_paths(source_paths: list[str]) -> list[str]:
    chapters: list[str] = []
    for source_path in source_paths:
        chapter_id = _chapter_id_from_path(source_path)
        if chapter_id and chapter_id not in chapters:
            chapters.append(chapter_id)
    return chapters


def _chapter_id_from_path(source_path: str) -> str | None:
    for part in Path(source_path).parts:
        if part.startswith("CH") and len(part) >= 5:
            return part[:5]
    return None


def _source_context_snippets(
    *,
    project_slug: str,
    source_chapters: list[str],
    query_terms: list[str],
) -> list[str]:
    snippets: list[str] = []
    for chapter_id in source_chapters[:3]:
        try:
            contexts = search_chapter_context(project_slug, chapter_id, query_terms, window=1, top_n=1)
        except Exception:
            continue
        for context in contexts:
            snippet = context.preview or context.text
            if snippet:
                snippets.append(f"{chapter_id} {context.paragraph_start}-{context.paragraph_end}: {snippet}")
    return snippets
