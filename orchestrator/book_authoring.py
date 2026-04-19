from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .common import repo_relative
from .scaffold import create_project
from .story_authoring import analyze_chapter, build_chapter_continuity


@dataclass(frozen=True)
class BookChapterRunSummary:
    chapter_id: str
    chapter_path: str
    scene_ids: list[str]
    continuity_summary_path: str

    def to_dict(self) -> dict[str, object]:
        return {
            "chapter_id": self.chapter_id,
            "chapter_path": self.chapter_path,
            "scene_ids": self.scene_ids,
            "continuity_summary_path": self.continuity_summary_path,
        }


@dataclass(frozen=True)
class BookAnalysisSummary:
    project_slug: str
    manifest_path: str
    chapters: list[BookChapterRunSummary]

    def to_dict(self) -> dict[str, object]:
        return {
            "project_slug": self.project_slug,
            "manifest_path": self.manifest_path,
            "chapters": [chapter.to_dict() for chapter in self.chapters],
        }


def analyze_book(*, project_slug: str) -> BookAnalysisSummary:
    project_dir = create_project(project_slug)
    manifest_path = project_dir / "01_source" / "book" / "book_manifest.md"
    if not manifest_path.exists():
        raise FileNotFoundError(f"Book manifest not found: {manifest_path}")

    chapter_paths = _read_manifest_chapter_paths(project_dir=project_dir, manifest_path=manifest_path)
    chapter_summaries: list[BookChapterRunSummary] = []

    for chapter_path in chapter_paths:
        analysis = analyze_chapter(project_slug=project_slug, chapter=repo_relative(chapter_path))
        continuity = build_chapter_continuity(project_slug=project_slug, analysis=analysis)
        chapter_summaries.append(
            BookChapterRunSummary(
                chapter_id=analysis.chapter_id,
                chapter_path=analysis.chapter_path,
                scene_ids=analysis.scene_ids,
                continuity_summary_path=continuity.summary_path,
            )
        )

    return BookAnalysisSummary(
        project_slug=project_slug,
        manifest_path=repo_relative(manifest_path),
        chapters=chapter_summaries,
    )


def _read_manifest_chapter_paths(*, project_dir: Path, manifest_path: Path) -> list[Path]:
    chapter_paths: list[Path] = []
    for line in manifest_path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped.startswith("- CH"):
            continue
        _, rhs = stripped.split(":", 1)
        rel_path = rhs.strip()
        chapter_paths.append(project_dir.parent.parent / rel_path)
    return chapter_paths
