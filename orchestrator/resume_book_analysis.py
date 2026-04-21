from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

from .book_authoring import (
    _chapter_id_from_path,
    _read_manifest_chapter_paths,
    analyze_book,
    retry_failed_chapters,
)


_CHAPTER_RE = re.compile(r"(CH\d{3})", re.IGNORECASE)


def build_resume_plan(project_slug: str) -> dict[str, Any]:
    project_dir = Path.cwd() / "projects" / project_slug
    manifest_path = project_dir / "01_source" / "book" / "book_manifest.md"
    state_path = project_dir / "project_state.json"
    analysis_dir = project_dir / "02_story_analysis" / "chapter_analysis"
    failed_path = project_dir / "02_story_analysis" / "runs" / "failed_chapters.json"

    manifest_chapter_ids: list[str] = []
    if manifest_path.exists():
        manifest_chapter_paths = _read_manifest_chapter_paths(project_dir=project_dir, manifest_path=manifest_path)
        manifest_chapter_ids = [_chapter_id_from_path(path) for path in manifest_chapter_paths]

    current_chapter_id = _read_current_chapter_id(state_path)
    completed_chapter_ids = sorted(
        {
            path.stem.split("_")[0].upper()
            for path in analysis_dir.glob("CH*_summary.md")
            if path.is_file()
        }
    )
    failed_chapter_ids = _load_failed_chapter_ids(failed_path)
    resume_chapter_ids = _build_resume_chapter_ids(
        manifest_chapter_ids=manifest_chapter_ids,
        completed_chapter_ids=completed_chapter_ids,
        current_chapter_id=current_chapter_id,
    )

    return {
        "project_slug": project_slug,
        "project_dir": str(project_dir),
        "manifest_path": str(manifest_path),
        "state_path": str(state_path),
        "analysis_dir": str(analysis_dir),
        "failed_path": str(failed_path),
        "current_chapter_id": current_chapter_id,
        "manifest_chapter_ids": manifest_chapter_ids,
        "completed_chapter_ids": completed_chapter_ids,
        "failed_chapter_ids": failed_chapter_ids,
        "resume_chapter_ids": resume_chapter_ids,
    }


def run_resume_book_analysis(*, project_slug: str, fail_fast: bool = False) -> dict[str, Any]:
    initial_plan = build_resume_plan(project_slug)
    retry_summary = None
    resumed_summary = None

    failed_path = Path(initial_plan["failed_path"])
    if failed_path.exists():
        retry_summary = retry_failed_chapters(project_slug=project_slug, fail_fast=fail_fast)

    refreshed_plan = build_resume_plan(project_slug)
    resume_chapter_ids = list(refreshed_plan["resume_chapter_ids"])
    if resume_chapter_ids:
        resumed_summary = analyze_book(
            project_slug=project_slug,
            chapters=resume_chapter_ids,
            fail_fast=fail_fast,
        )

    return {
        "project_slug": project_slug,
        "retry_failed_chapters": retry_summary.to_dict() if retry_summary is not None else None,
        "resume_plan": refreshed_plan,
        "resumed_book_analysis": resumed_summary.to_dict() if resumed_summary is not None else None,
    }


def _build_resume_chapter_ids(
    *,
    manifest_chapter_ids: list[str],
    completed_chapter_ids: list[str],
    current_chapter_id: str | None,
) -> list[str]:
    manifest = [chapter_id.upper() for chapter_id in manifest_chapter_ids]
    completed = {chapter_id.upper() for chapter_id in completed_chapter_ids}

    if current_chapter_id:
        current_chapter_id = current_chapter_id.upper()
        if current_chapter_id in manifest:
            start_index = manifest.index(current_chapter_id)
            resumed: list[str] = []
            for chapter_id in manifest[start_index:]:
                if chapter_id == current_chapter_id:
                    resumed.append(chapter_id)
                    continue
                if chapter_id not in completed:
                    resumed.append(chapter_id)
            return resumed

    return [chapter_id for chapter_id in manifest if chapter_id not in completed]


def _load_failed_chapter_ids(path: Path) -> list[str]:
    if not path.exists():
        return []
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []
    failed_entries = payload.get("failed_chapters", []) if isinstance(payload, dict) else []
    result: list[str] = []
    for entry in failed_entries:
        if not isinstance(entry, dict):
            continue
        value = str(entry.get("chapter_id") or entry.get("chapter_path") or "")
        match = _CHAPTER_RE.search(value)
        if match:
            chapter_id = match.group(1).upper()
            if chapter_id not in result:
                result.append(chapter_id)
    return result


def _read_current_chapter_id(path: Path) -> str | None:
    if not path.exists():
        return None
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None
    if not isinstance(payload, dict):
        return None
    current_scene_id = str(payload.get("current_scene_id") or "")
    match = _CHAPTER_RE.search(current_scene_id)
    return match.group(1).upper() if match else None


def main() -> None:
    parser = argparse.ArgumentParser(description="Resume FilmCreator book analysis from the last partial chapter.")
    parser.add_argument("project_slug")
    parser.add_argument("--fail-fast", action="store_true")
    args = parser.parse_args()

    result = run_resume_book_analysis(project_slug=args.project_slug, fail_fast=args.fail_fast)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
