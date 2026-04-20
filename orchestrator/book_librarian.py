from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from .book_ingest import _split_paragraphs
from .features.world.global_helpers import load_json
from .scaffold import create_project
from .state import resolve_user_path


@dataclass(frozen=True)
class BookContextSlice:
    chapter_id: str
    chapter_title: str
    chapter_path: str
    paragraph_start: int
    paragraph_end: int
    text: str
    preview: str


def book_index_path(project_slug: str) -> Path:
    return create_project(project_slug) / "01_source" / "book" / "book_index.json"


def load_book_index(project_slug: str) -> dict:
    return load_json(book_index_path(project_slug), {})


def get_chapter_entry(project_slug: str, chapter_id: str) -> dict | None:
    book_index = load_book_index(project_slug)
    for chapter in book_index.get("chapters", []):
        if chapter.get("chapter_id") == chapter_id:
            return chapter
    return None


def list_chapter_entries(project_slug: str) -> list[dict]:
    book_index = load_book_index(project_slug)
    chapters = book_index.get("chapters", [])
    return [chapter for chapter in chapters if isinstance(chapter, dict)]


def chapter_source_path(project_slug: str, chapter_id: str) -> Path:
    chapter_entry = get_chapter_entry(project_slug, chapter_id)
    if not chapter_entry:
        raise FileNotFoundError(f"Chapter {chapter_id} not found in book index for {project_slug}.")
    chapter_path_value = chapter_entry.get("chapter_path")
    if not isinstance(chapter_path_value, str) or not chapter_path_value.strip():
        raise FileNotFoundError(f"Book index entry for {chapter_id} is missing chapter_path.")
    return resolve_user_path(chapter_path_value)


def chapter_text(project_slug: str, chapter_id: str) -> str:
    chapter_path = chapter_source_path(project_slug, chapter_id)
    markdown = chapter_path.read_text(encoding="utf-8")
    return _extract_text_section(markdown)


def chapter_paragraphs(project_slug: str, chapter_id: str) -> list[dict[str, object]]:
    chapter_entry = get_chapter_entry(project_slug, chapter_id)
    if not chapter_entry:
        return []
    text = chapter_text(project_slug, chapter_id)
    paragraphs = chapter_entry.get("paragraphs", [])
    if not isinstance(paragraphs, list):
        return []
    results: list[dict[str, object]] = []
    for paragraph in paragraphs:
        if not isinstance(paragraph, dict):
            continue
        start = int(paragraph.get("char_start", 0))
        end = int(paragraph.get("char_end", 0))
        preview = str(paragraph.get("preview", "")).strip()
        snippet = text[start:end].strip() if start < end else preview
        if not snippet:
            snippet = preview
        results.append(
            {
                "paragraph_index": int(paragraph.get("paragraph_index", len(results) + 1)),
                "char_start": start,
                "char_end": end,
                "preview": preview,
                "text": snippet,
            }
        )
    return results


def get_paragraph_window(project_slug: str, chapter_id: str, start_paragraph: int, end_paragraph: int) -> BookContextSlice:
    if start_paragraph < 1 or end_paragraph < start_paragraph:
        raise ValueError("Invalid paragraph window.")
    chapter_entry = get_chapter_entry(project_slug, chapter_id)
    if not chapter_entry:
        raise FileNotFoundError(f"Chapter {chapter_id} not found in book index for {project_slug}.")
    paragraphs = chapter_paragraphs(project_slug, chapter_id)
    selected = [
        paragraph
        for paragraph in paragraphs
        if start_paragraph <= int(paragraph.get("paragraph_index", 0)) <= end_paragraph
    ]
    text = "\n\n".join(str(paragraph.get("text", "")).strip() for paragraph in selected if str(paragraph.get("text", "")).strip())
    if not text:
        text = "\n\n".join(str(paragraph.get("preview", "")).strip() for paragraph in selected if str(paragraph.get("preview", "")).strip())
    return BookContextSlice(
        chapter_id=chapter_id,
        chapter_title=str(chapter_entry.get("title", chapter_id)),
        chapter_path=str(chapter_entry.get("chapter_path", "")),
        paragraph_start=start_paragraph,
        paragraph_end=end_paragraph,
        text=text.strip(),
        preview=_paragraph_preview(text),
    )


def search_chapter_context(
    project_slug: str,
    chapter_id: str,
    query_terms: list[str],
    *,
    window: int = 1,
    top_n: int = 3,
) -> list[BookContextSlice]:
    if window < 0:
        raise ValueError("Window must be non-negative.")
    normalized_terms = [normalize_term(term) for term in query_terms if normalize_term(term)]
    if not normalized_terms:
        return []
    paragraphs = chapter_paragraphs(project_slug, chapter_id)
    matches: list[BookContextSlice] = []
    seen_ranges: set[tuple[int, int]] = set()
    for paragraph in paragraphs:
        paragraph_index = int(paragraph.get("paragraph_index", 0))
        haystack = " ".join(
            [
                str(paragraph.get("text", "")),
                str(paragraph.get("preview", "")),
            ]
        ).lower()
        if not any(term in haystack for term in normalized_terms):
            continue
        start = max(1, paragraph_index - window)
        end = min(len(paragraphs), paragraph_index + window)
        if (start, end) in seen_ranges:
            continue
        seen_ranges.add((start, end))
        matches.append(get_paragraph_window(project_slug, chapter_id, start, end))
        if len(matches) >= top_n:
            break
    return matches


def search_book_index(project_slug: str, query: str, *, top_n: int = 5) -> list[dict[str, object]]:
    normalized_query = normalize_term(query)
    if not normalized_query:
        return []
    query_tokens = [token for token in normalized_query.split("_") if token]
    results: list[dict[str, object]] = []
    for chapter in list_chapter_entries(project_slug):
        title = str(chapter.get("title", ""))
        title_token = normalize_term(title)
        score = 0
        reasons: list[str] = []
        if normalized_query in title_token:
            score += 10
            reasons.append("title contains query")
        preview_blob = " ".join(str(paragraph.get("preview", "")) for paragraph in chapter.get("paragraphs", []) if isinstance(paragraph, dict))
        preview_blob_norm = normalize_term(preview_blob)
        if normalized_query in preview_blob_norm:
            score += 6
            reasons.append("query appears in paragraph preview")
        for token in query_tokens:
            if token and token in title_token:
                score += 2
            if token and token in preview_blob_norm:
                score += 1
        if score:
            results.append(
                {
                    "chapter_id": chapter.get("chapter_id", ""),
                    "title": title,
                    "chapter_path": chapter.get("chapter_path", ""),
                    "score": score,
                    "reasons": reasons,
                }
            )
    results.sort(key=lambda item: (-int(item["score"]), str(item["chapter_id"])))
    return results[:top_n]


def normalize_term(value: str) -> str:
    normalized = re.sub(r"[^a-z0-9]+", "_", value.strip().lower()).strip("_")
    return normalized


def _extract_text_section(markdown: str) -> str:
    lines = markdown.splitlines()
    in_text_section = False
    text_lines: list[str] = []
    for line in lines:
        if line.strip().lower() == "# text":
            in_text_section = True
            continue
        if in_text_section:
            text_lines.append(line)
    body = "\n".join(text_lines).strip()
    return body or markdown.strip()


def _paragraph_preview(text: str, *, limit: int = 180) -> str:
    collapsed = " ".join(text.split())
    return collapsed[:limit] + ("..." if len(collapsed) > limit else "")
