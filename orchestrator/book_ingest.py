from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path

from .core.paths import ensure_dir, repo_relative
from .scaffold import create_project


CHAPTER_HEADING_RE = re.compile(r"(?im)^(chapter|book)\s+([ivxlcdm0-9]+)\b[^\n\r]*$")


@dataclass(frozen=True)
class BookIngestSummary:
    project_slug: str
    raw_book_path: str
    manifest_path: str
    book_index_path: str
    chapter_paths: list[str]
    chapter_ids: list[str]

    def to_dict(self) -> dict[str, object]:
        return {
            "project_slug": self.project_slug,
            "raw_book_path": self.raw_book_path,
            "manifest_path": self.manifest_path,
            "book_index_path": self.book_index_path,
            "chapter_paths": self.chapter_paths,
            "chapter_ids": self.chapter_ids,
        }


def ingest_book_text(
    *,
    project_slug: str,
    raw_text: str,
    source_name: str = "raw_book.txt",
) -> BookIngestSummary:
    project_dir = create_project(project_slug)
    book_dir = project_dir / "01_source" / "book"
    chapter_dir = project_dir / "01_source" / "chapters"
    ensure_dir(book_dir)
    ensure_dir(chapter_dir)

    raw_book_path = book_dir / source_name
    raw_book_path.write_text(raw_text.rstrip() + "\n", encoding="utf-8")

    chapters = split_book_into_chapters(raw_text)
    chapter_paths: list[str] = []
    chapter_ids: list[str] = []

    for index, chapter in enumerate(chapters, start=1):
        chapter_id = f"CH{index:03d}"
        title = chapter["title"].strip() or chapter_id
        safe_title = _slugify_title(title)
        chapter_path = chapter_dir / f"{chapter_id}_{safe_title}.md"
        chapter_body = "\n".join(
            [
                "# Chapter",
                chapter_id,
                "",
                "# Title",
                title,
                "",
                "# Text",
                chapter["text"].strip(),
                "",
            ]
        )
        chapter_path.write_text(chapter_body, encoding="utf-8")
        chapter_paths.append(repo_relative(chapter_path))
        chapter_ids.append(chapter_id)

    manifest_path = write_book_manifest(
        project_slug=project_slug,
        chapter_ids=chapter_ids,
        chapter_paths=chapter_paths,
    )
    book_index_path = write_book_index(
        project_slug=project_slug,
        source_name=source_name,
        chapters=chapters,
        chapter_paths=chapter_paths,
        chapter_ids=chapter_ids,
    )

    return BookIngestSummary(
        project_slug=project_slug,
        raw_book_path=repo_relative(raw_book_path),
        manifest_path=repo_relative(manifest_path),
        book_index_path=repo_relative(book_index_path),
        chapter_paths=chapter_paths,
        chapter_ids=chapter_ids,
    )


def ensure_book_ingested(*, project_slug: str) -> BookIngestSummary | None:
    project_dir = create_project(project_slug)
    book_dir = project_dir / "01_source" / "book"
    manifest_path = book_dir / "book_manifest.md"
    if manifest_path.exists():
        return None

    raw_book_path = book_dir / "raw_book.txt"
    book_input_path = book_dir / "book_input.txt"
    if raw_book_path.exists():
        raw_text = raw_book_path.read_text(encoding="utf-8")
    elif book_input_path.exists():
        raw_text = book_input_path.read_text(encoding="utf-8")
    else:
        raise FileNotFoundError(
            "Book ingest has not run and no source text was found. Expected one of: "
            f"{raw_book_path}, {book_input_path}"
        )

    return ingest_book_text(
        project_slug=project_slug,
        raw_text=raw_text,
        source_name="raw_book.txt",
    )


def split_book_into_chapters(raw_text: str) -> list[dict[str, str]]:
    matches = list(CHAPTER_HEADING_RE.finditer(raw_text))
    if not matches:
        cleaned = raw_text.strip()
        if not cleaned:
            raise ValueError("Raw book text is empty.")
        return [{"title": "Chapter 1", "text": cleaned}]

    chapters: list[dict[str, str]] = []
    for index, match in enumerate(matches):
        start = match.start()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(raw_text)
        chunk = raw_text[start:end].strip()
        lines = chunk.splitlines()
        title = lines[0].strip() if lines else f"Chapter {index + 1}"
        body = "\n".join(lines[1:]).strip() if len(lines) > 1 else chunk
        chapters.append(
            {
                "title": title,
                "text": body,
            }
        )
    return chapters


def write_book_manifest(
    *,
    project_slug: str,
    chapter_ids: list[str],
    chapter_paths: list[str],
) -> Path:
    project_dir = create_project(project_slug)
    manifest_path = project_dir / "01_source" / "book" / "book_manifest.md"
    lines = [
        "# Book Manifest",
        "",
        "## Chapter Order",
        "",
    ]
    for chapter_id, chapter_path in zip(chapter_ids, chapter_paths):
        lines.append(f"- {chapter_id}: {chapter_path}")
    lines.append("")
    manifest_path.write_text("\n".join(lines), encoding="utf-8")
    return manifest_path


def write_book_index(
    *,
    project_slug: str,
    source_name: str,
    chapters: list[dict[str, str]],
    chapter_paths: list[str],
    chapter_ids: list[str],
) -> Path:
    project_dir = create_project(project_slug)
    index_path = project_dir / "01_source" / "book" / "book_index.json"
    chapter_entries: list[dict[str, object]] = []
    for chapter_id, chapter_path, chapter in zip(chapter_ids, chapter_paths, chapters):
        paragraph_entries = _index_paragraphs(chapter.get("text", ""))
        chapter_entries.append(
            {
                "chapter_id": chapter_id,
                "title": chapter.get("title", chapter_id).strip() or chapter_id,
                "chapter_path": chapter_path,
                "paragraph_count": len(paragraph_entries),
                "paragraphs": paragraph_entries,
            }
        )

    payload = {
        "project_slug": project_slug,
        "source_name": source_name,
        "chapter_count": len(chapter_entries),
        "chapters": chapter_entries,
    }
    index_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return index_path


def _index_paragraphs(text: str) -> list[dict[str, object]]:
    paragraphs: list[dict[str, object]] = []
    cursor = 0
    for paragraph_index, paragraph in enumerate(_split_paragraphs(text), start=1):
        if not paragraph.strip():
            continue
        start = text.find(paragraph, cursor)
        if start < 0:
            start = cursor
        end = start + len(paragraph)
        cursor = end
        paragraphs.append(
            {
                "paragraph_index": paragraph_index,
                "char_start": start,
                "char_end": end,
                "preview": _paragraph_preview(paragraph),
            }
        )
    return paragraphs


def _split_paragraphs(text: str) -> list[str]:
    return [paragraph.strip() for paragraph in re.split(r"\n\s*\n", text.strip()) if paragraph.strip()]


def _paragraph_preview(paragraph: str, *, limit: int = 180) -> str:
    collapsed = " ".join(paragraph.split())
    return collapsed[:limit] + ("..." if len(collapsed) > limit else "")


def _slugify_title(title: str) -> str:
    normalized = re.sub(r"[^a-z0-9]+", "_", title.lower()).strip("_")
    return normalized or "chapter"
