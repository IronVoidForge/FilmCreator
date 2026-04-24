from __future__ import annotations

from pathlib import Path

from .models import CliContext


def build_context(project_slug: str, *, chapters: str | None = None, dry_run: bool = False) -> CliContext:
    repo_root = Path.cwd()
    project_root = repo_root / "projects" / project_slug
    return CliContext(
        project_slug=project_slug,
        repo_root=repo_root,
        project_root=project_root,
        chapters=chapters,
        dry_run=dry_run,
    )


def parse_chapter_slice(chapters: str | None) -> list[str]:
    if not chapters:
        return []
    cleaned = chapters.strip()
    if not cleaned:
        return []
    if "-" in cleaned:
        start, end = cleaned.split("-", 1)
        if start.strip().isdigit() and end.strip().isdigit():
            return [str(index) for index in range(int(start), int(end) + 1)]
    return [item.strip() for item in cleaned.split(",") if item.strip()]
