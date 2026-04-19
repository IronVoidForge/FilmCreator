from __future__ import annotations

import json
from pathlib import Path

from .scaffold import create_project
from .story_authoring import author_chapter, build_chapter_continuity


DEFAULT_PROJECT_SLUG = "princess_of_mars_test"
DEFAULT_CHAPTER_ID = "CH008"


def _resolve_chapter_filename(*, project_slug: str, chapter_id: str) -> str:
    project_dir = create_project(project_slug)
    chapter_dir = project_dir / "01_source" / "chapters"
    matches = sorted(chapter_dir.glob(f"{chapter_id}_*.md"))
    if not matches:
        raise FileNotFoundError(
            f"No chapter source file matching {chapter_id}_*.md found under {chapter_dir}"
        )
    return matches[0].name


def run_full_chapter_authoring(*, project_slug: str, chapter: str | None = None, chapter_id: str | None = None) -> dict[str, object]:
    resolved_chapter = chapter
    if not resolved_chapter:
        target_chapter_id = chapter_id or DEFAULT_CHAPTER_ID
        resolved_chapter = _resolve_chapter_filename(project_slug=project_slug, chapter_id=target_chapter_id)
        print(f"[authoring] Resolved chapter source for full cascade: {resolved_chapter}")

    summary = author_chapter(project_slug=project_slug, chapter=resolved_chapter)
    continuity = build_chapter_continuity(project_slug=project_slug, analysis=summary.analysis)
    return {
        "analysis": summary.analysis.to_dict(),
        "continuity": continuity.to_dict(),
        "scene_runs": [scene_run.to_dict() for scene_run in summary.scene_runs],
        "shared_prompts": summary.shared_prompts.to_dict(),
    }


if __name__ == "__main__":
    payload = run_full_chapter_authoring(
        project_slug=DEFAULT_PROJECT_SLUG,
        chapter_id=DEFAULT_CHAPTER_ID,
    )
    print(json.dumps(payload, indent=2))
