from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

from .common import repo_relative
from .scaffold import create_project
from .story_authoring import analyze_chapter, build_chapter_continuity
from .world_global import (
    chapter_local_character_registry_path,
    chapter_local_environment_registry_path,
    append_world_failure,
    load_world_snapshot,
    update_global_character_state,
    update_global_environment_state,
    write_chapter_world_snapshot,
    update_world_sequence_state,
)
from .world_refinement import refine_world_identities


@dataclass(frozen=True)
class BookChapterRunSummary:
    chapter_id: str
    chapter_path: str
    scene_ids: list[str]
    continuity_summary_path: str
    snapshot_path: str

    def to_dict(self) -> dict[str, object]:
        return {
            "chapter_id": self.chapter_id,
            "chapter_path": self.chapter_path,
            "scene_ids": self.scene_ids,
            "continuity_summary_path": self.continuity_summary_path,
            "snapshot_path": self.snapshot_path,
        }


@dataclass(frozen=True)
class BookChapterFailureSummary:
    chapter_id: str
    chapter_path: str
    stage: str
    error: str

    def to_dict(self) -> dict[str, object]:
        return {
            "chapter_id": self.chapter_id,
            "chapter_path": self.chapter_path,
            "stage": self.stage,
            "error": self.error,
        }


@dataclass(frozen=True)
class BookAnalysisSummary:
    project_slug: str
    manifest_path: str
    chapters: list[BookChapterRunSummary]
    failures: list[BookChapterFailureSummary]

    def to_dict(self) -> dict[str, object]:
        return {
            "project_slug": self.project_slug,
            "manifest_path": self.manifest_path,
            "chapters": [chapter.to_dict() for chapter in self.chapters],
            "failures": [failure.to_dict() for failure in self.failures],
        }


def analyze_book(*, project_slug: str, continue_on_error: bool = False) -> BookAnalysisSummary:
    project_dir = create_project(project_slug)
    manifest_path = project_dir / "01_source" / "book" / "book_manifest.md"
    if not manifest_path.exists():
        raise FileNotFoundError(f"Book manifest not found: {manifest_path}")

    chapter_paths = _read_manifest_chapter_paths(project_dir=project_dir, manifest_path=manifest_path)
    chapter_summaries: list[BookChapterRunSummary] = []
    failures: list[BookChapterFailureSummary] = []
    succeeded_ids: list[str] = []
    failed_ids: list[str] = []
    total_chapters = len(chapter_paths)

    for index, chapter_path in enumerate(chapter_paths, start=1):
        chapter_rel = repo_relative(chapter_path)
        print(f"[authoring] Starting manifest chapter {index}/{total_chapters}: {chapter_rel}")
        try:
            analysis = analyze_chapter(project_slug=project_slug, chapter=chapter_rel)

            char_reg_rel, char_dir_rel = update_global_character_state(
                project_slug=project_slug, analysis=analysis
            )
            env_reg_rel, env_dir_rel = update_global_environment_state(
                project_slug=project_slug, analysis=analysis
            )

            snapshot_path = write_chapter_world_snapshot(
                project_slug=project_slug,
                analysis=analysis,
                global_character_registry_relpath=char_reg_rel,
                global_environment_registry_relpath=env_reg_rel,
                global_character_directory_relpath=char_dir_rel,
                global_environment_directory_relpath=env_dir_rel,
            )
            snapshot_data = load_world_snapshot(project_slug=project_slug, chapter_id=analysis.chapter_id)
            if not snapshot_data.get("character_entries") and not snapshot_data.get("environment_entries"):
                chapter_character_registry = chapter_local_character_registry_path(
                    project_slug=project_slug,
                    chapter_id=analysis.chapter_id,
                )
                chapter_environment_registry = chapter_local_environment_registry_path(
                    project_slug=project_slug,
                    chapter_id=analysis.chapter_id,
                )
                chapter_character_registry_data = json.loads(chapter_character_registry.read_text(encoding="utf-8")) if chapter_character_registry.exists() else {}
                chapter_environment_registry_data = json.loads(chapter_environment_registry.read_text(encoding="utf-8")) if chapter_environment_registry.exists() else {}
                if chapter_character_registry_data or chapter_environment_registry_data:
                    raise ValueError(
                        f"Chapter {analysis.chapter_id} produced an empty snapshot despite local registry artifacts existing."
                    )
            continuity = build_chapter_continuity(
                project_slug=project_slug,
                analysis=analysis,
                snapshot_data=snapshot_data,
            )

            chapter_summaries.append(
                BookChapterRunSummary(
                    chapter_id=analysis.chapter_id,
                    chapter_path=analysis.chapter_path,
                    scene_ids=analysis.scene_ids,
                    continuity_summary_path=continuity.summary_path,
                    snapshot_path=snapshot_path,
                )
            )
            succeeded_ids.append(analysis.chapter_id)

        except Exception as exc:  # noqa: BLE001
            chapter_id = chapter_path.name.split("_")[0]
            failure = BookChapterFailureSummary(
                chapter_id=chapter_id,
                chapter_path=chapter_rel,
                stage="analysis_or_continuity",
                error=str(exc),
            )
            failures.append(failure)
            failed_ids.append(chapter_id)

            append_world_failure(
                project_slug=project_slug,
                chapter_id=chapter_id,
                chapter_path=chapter_rel,
                stage="analysis_or_continuity",
                error=str(exc),
                failure_artifact_path=None,
            )

            if not continue_on_error:
                update_world_sequence_state(
                    project_slug=project_slug,
                    succeeded_chapter_ids=succeeded_ids,
                    failed_chapter_ids=failed_ids,
                )
                raise
            continue

    update_world_sequence_state(
        project_slug=project_slug,
        succeeded_chapter_ids=succeeded_ids,
        failed_chapter_ids=failed_ids,
    )

    return BookAnalysisSummary(
        project_slug=project_slug,
        manifest_path=repo_relative(manifest_path),
        chapters=chapter_summaries,
        failures=failures,
    )


def refine_world(project_slug: str, *, use_llm: bool = True, apply_changes: bool = True) -> dict[str, object]:
    summary = refine_world_identities(
        project_slug=project_slug,
        use_llm=use_llm,
        apply_changes=apply_changes,
    )
    return summary.to_dict()


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
