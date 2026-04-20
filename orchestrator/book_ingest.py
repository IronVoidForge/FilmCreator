from __future__ import annotations

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
    chapter_paths: list[str]
    chapter_ids: list[str]

    def to_dict(self) -> dict[str, object]:
        return {
            "project_slug": self.project_slug,
            "raw_book_path": self.raw_book_path,
            "manifest_path": self.manifest_path,
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

    return BookIngestSummary(
        project_slug=project_slug,
        raw_book_path=repo_relative(raw_book_path),
        manifest_path=repo_relative(manifest_path),
        chapter_paths=chapter_paths,
        chapter_ids=chapter_ids,
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


def _slugify_title(title: str) -> str:
    normalized = re.sub(r"[^a-z0-9]+", "_", title.lower()).strip("_")
    return normalized or "chapter"
