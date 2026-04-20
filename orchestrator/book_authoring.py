from __future__ import annotations

import json
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .common import ensure_dir, read_json, repo_relative
from .scaffold import create_project
from .story_authoring import analyze_chapter, build_chapter_continuity
from .world_global import (
    append_world_failure,
    chapter_local_character_registry_path,
    chapter_local_environment_registry_path,
    load_world_snapshot,
    update_global_character_state,
    update_global_environment_state,
    update_world_sequence_state,
    write_chapter_world_snapshot,
)
from .world_refinement import refine_world_identities


_CHAPTER_ID_RE = re.compile(r"(CH\d{3})", re.IGNORECASE)


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
class ChapterRunResult:
    chapter_id: str
    chapter_path: str
    status: str
    failed_stage: str | None
    error_type: str | None
    error_message: str | None
    chapter_summary_path: str | None
    continuity_state_path: str | None
    continuity_summary_path: str | None
    snapshot_path: str | None
    scene_ids: list[str]

    def to_dict(self) -> dict[str, Any]:
        return {
            "chapter_id": self.chapter_id,
            "chapter_path": self.chapter_path,
            "status": self.status,
            "failed_stage": self.failed_stage,
            "error_type": self.error_type,
            "error_message": self.error_message,
            "chapter_summary_path": self.chapter_summary_path,
            "continuity_state_path": self.continuity_state_path,
            "continuity_summary_path": self.continuity_summary_path,
            "snapshot_path": self.snapshot_path,
            "scene_ids": self.scene_ids,
        }

    def to_legacy_run_summary(self) -> BookChapterRunSummary | None:
        if self.status != "completed":
            return None
        if self.chapter_summary_path is None or self.continuity_summary_path is None or self.snapshot_path is None:
            return None
        return BookChapterRunSummary(
            chapter_id=self.chapter_id,
            chapter_path=self.chapter_path,
            scene_ids=self.scene_ids,
            continuity_summary_path=self.continuity_summary_path,
            snapshot_path=self.snapshot_path,
        )

    def to_legacy_failure_summary(self) -> BookChapterFailureSummary | None:
        if self.status != "failed":
            return None
        return BookChapterFailureSummary(
            chapter_id=self.chapter_id,
            chapter_path=self.chapter_path,
            stage=self.failed_stage or "analysis_or_continuity",
            error=self.error_message or "",
        )


@dataclass(frozen=True)
class BookRunSummary:
    project_slug: str
    manifest_path: str
    status: str
    started_at_utc: str
    completed_at_utc: str
    chapter_results: list[ChapterRunResult]
    completed_chapters: list[str]
    failed_chapters: list[str]
    skipped_chapters: list[str]
    written_files: list[str]

    def to_dict(self) -> dict[str, Any]:
        completed_legacy: list[dict[str, Any]] = []
        failed_legacy: list[dict[str, Any]] = []
        for result in self.chapter_results:
            legacy_run = result.to_legacy_run_summary()
            if legacy_run is not None:
                completed_legacy.append(legacy_run.to_dict())
            legacy_failure = result.to_legacy_failure_summary()
            if legacy_failure is not None:
                failed_legacy.append(legacy_failure.to_dict())
        return {
            "project_slug": self.project_slug,
            "manifest_path": self.manifest_path,
            "status": self.status,
            "started_at_utc": self.started_at_utc,
            "completed_at_utc": self.completed_at_utc,
            "chapter_results": [item.to_dict() for item in self.chapter_results],
            "completed_chapters": self.completed_chapters,
            "failed_chapters": self.failed_chapters,
            "skipped_chapters": self.skipped_chapters,
            "written_files": self.written_files,
            "chapters": completed_legacy,
            "failures": failed_legacy,
        }

    @property
    def chapters(self) -> list[BookChapterRunSummary]:
        return [
            result.to_legacy_run_summary()
            for result in self.chapter_results
            if result.to_legacy_run_summary() is not None
        ]

    @property
    def failures(self) -> list[BookChapterFailureSummary]:
        return [
            result.to_legacy_failure_summary()
            for result in self.chapter_results
            if result.to_legacy_failure_summary() is not None
        ]


BookAnalysisSummary = BookRunSummary


def analyze_book(
    *,
    project_slug: str,
    fail_fast: bool = False,
    chapters: list[str] | None = None,
    retry_failed_only: bool = False,
    continue_on_error: bool | None = None,
) -> BookRunSummary:
    if continue_on_error is not None:
        fail_fast = not continue_on_error

    project_dir = create_project(project_slug)
    manifest_path = project_dir / "01_source" / "book" / "book_manifest.md"
    if not manifest_path.exists():
        raise FileNotFoundError(f"Book manifest not found: {manifest_path}")

    started_at_utc = _utc_now_iso()
    manifest_chapter_paths = _read_manifest_chapter_paths(project_dir=project_dir, manifest_path=manifest_path)
    selected_chapter_paths = _resolve_requested_chapter_paths(
        project_dir=project_dir,
        manifest_chapter_paths=manifest_chapter_paths,
        chapters=chapters,
        retry_failed_only=retry_failed_only,
    )

    if retry_failed_only and not selected_chapter_paths:
        summary = _empty_book_run_summary(
            project_slug=project_slug,
            manifest_path=repo_relative(manifest_path),
            started_at_utc=started_at_utc,
        )
        print("[authoring] No failed chapters remain to retry.")
        return summary

    chapter_results: list[ChapterRunResult] = []
    succeeded_ids: list[str] = []
    failed_ids: list[str] = []
    failure_log_path: str | None = None
    captured_exception: Exception | None = None
    captured_traceback = None
    total_selected = len(selected_chapter_paths)

    for index, chapter_path in enumerate(selected_chapter_paths, start=1):
        chapter_rel = _repo_relative_or_input(chapter_path)
        chapter_id = _chapter_id_from_path(chapter_path)
        print(f"[authoring] Starting manifest chapter {index}/{total_selected}: {chapter_rel}")

        analysis = None
        continuity = None
        chapter_summary_path: str | None = None
        continuity_state_path: str | None = None
        continuity_summary_path: str | None = None
        snapshot_path: str | None = None
        scene_ids: list[str] = []

        try:
            if not chapter_path.exists():
                raise FileNotFoundError(f"Chapter source not found: {chapter_path}")

            analysis = analyze_chapter(project_slug=project_slug, chapter=chapter_rel)
            chapter_id = analysis.chapter_id
            chapter_summary_path = repo_relative(
                project_dir / "02_story_analysis" / "chapter_analysis" / f"{chapter_id}_summary.md"
            )

            char_reg_rel, char_dir_rel = update_global_character_state(
                project_slug=project_slug,
                analysis=analysis,
            )
            env_reg_rel, env_dir_rel = update_global_environment_state(
                project_slug=project_slug,
                analysis=analysis,
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
                chapter_character_registry_data = (
                    json.loads(chapter_character_registry.read_text(encoding="utf-8"))
                    if chapter_character_registry.exists()
                    else {}
                )
                chapter_environment_registry_data = (
                    json.loads(chapter_environment_registry.read_text(encoding="utf-8"))
                    if chapter_environment_registry.exists()
                    else {}
                )
                if chapter_character_registry_data or chapter_environment_registry_data:
                    raise ValueError(
                        f"Chapter {analysis.chapter_id} produced an empty snapshot despite local registry artifacts existing."
                    )

            continuity = build_chapter_continuity(
                project_slug=project_slug,
                analysis=analysis,
                snapshot_data=snapshot_data,
            )
            continuity_state_path = continuity.state_path
            continuity_summary_path = continuity.summary_path
            scene_ids = analysis.scene_ids

            chapter_results.append(
                ChapterRunResult(
                    chapter_id=analysis.chapter_id,
                    chapter_path=analysis.chapter_path,
                    status="completed",
                    failed_stage=None,
                    error_type=None,
                    error_message=None,
                    chapter_summary_path=chapter_summary_path,
                    continuity_state_path=continuity_state_path,
                    continuity_summary_path=continuity_summary_path,
                    snapshot_path=snapshot_path,
                    scene_ids=analysis.scene_ids,
                )
            )
            succeeded_ids.append(analysis.chapter_id)

        except Exception as exc:  # noqa: BLE001
            failed_stage, error_message = _classify_book_error(exc)
            failing_chapter_id = analysis.chapter_id if analysis is not None else chapter_id
            chapter_results.append(
                ChapterRunResult(
                    chapter_id=failing_chapter_id,
                    chapter_path=chapter_rel,
                    status="failed",
                    failed_stage=failed_stage,
                    error_type=type(exc).__name__,
                    error_message=error_message,
                    chapter_summary_path=chapter_summary_path,
                    continuity_state_path=continuity_state_path,
                    continuity_summary_path=continuity_summary_path,
                    snapshot_path=snapshot_path,
                    scene_ids=scene_ids,
                )
            )
            failed_ids.append(failing_chapter_id)

            failure_log_path = append_world_failure(
                project_slug=project_slug,
                chapter_id=failing_chapter_id,
                chapter_path=chapter_rel,
                stage=failed_stage,
                error=error_message,
                failure_artifact_path=None,
            )

            print(f"[authoring] Chapter {failing_chapter_id} failed: {error_message}")
            if fail_fast:
                captured_exception = exc
                captured_traceback = exc.__traceback__
                break

            print("[authoring] Continuing to next chapter.")

    skipped_chapters = _derive_skipped_chapters(
        manifest_chapter_paths=manifest_chapter_paths,
        processed_chapter_ids=succeeded_ids + failed_ids,
    )
    completed_at_utc = _utc_now_iso()
    status = _book_run_status(chapter_results)

    sequence_state_path = update_world_sequence_state(
        project_slug=project_slug,
        succeeded_chapter_ids=succeeded_ids,
        failed_chapter_ids=failed_ids,
    )

    summary = _build_book_run_summary(
        project_slug=project_slug,
        manifest_path=repo_relative(manifest_path),
        status=status,
        started_at_utc=started_at_utc,
        completed_at_utc=completed_at_utc,
        chapter_results=chapter_results,
        succeeded_ids=succeeded_ids,
        failed_ids=failed_ids,
        skipped_chapters=skipped_chapters,
        sequence_state_path=sequence_state_path,
        failure_log_path=failure_log_path,
    )
    _write_book_run_artifacts(summary)

    print("[authoring] Multi-chapter analysis finished.")
    print(f"[authoring] Completed chapters: {len(succeeded_ids)}")
    print(f"[authoring] Failed chapters: {len(failed_ids)}")
    print(f"[authoring] Skipped chapters: {len(skipped_chapters)}")
    print(f"[authoring] Failed chapter list saved to: {_failed_chapters_json_path(project_slug)}")

    if captured_exception is not None:
        raise captured_exception.with_traceback(captured_traceback)

    return summary


def retry_failed_chapters(*, project_slug: str, fail_fast: bool = False) -> BookRunSummary:
    failed_payload = _load_latest_failed_chapters(project_slug=project_slug)
    project_dir = create_project(project_slug)
    manifest_path = project_dir / "01_source" / "book" / "book_manifest.md"
    if not manifest_path.exists():
        raise FileNotFoundError(f"Book manifest not found: {manifest_path}")

    failed_entries = list(failed_payload.get("failed_chapters", [])) if isinstance(failed_payload, dict) else []
    failed_paths = [entry["chapter_path"] for entry in failed_entries if entry.get("chapter_path")]
    if not failed_paths:
        started_at_utc = _utc_now_iso()
        summary = _empty_book_run_summary(
            project_slug=project_slug,
            manifest_path=repo_relative(manifest_path),
            started_at_utc=started_at_utc,
        )
        print("[authoring] No failed chapters remain to retry.")
        return summary

    prior_run_path = failed_payload.get("book_run_path") if isinstance(failed_payload, dict) else None
    prior_summary = None
    if prior_run_path:
        prior_run_path_obj = Path(prior_run_path)
        if not prior_run_path_obj.is_absolute():
            prior_run_path_obj = project_dir.parent.parent / prior_run_path_obj
        if prior_run_path_obj.exists():
            prior_summary = read_json(prior_run_path_obj)
    prior_completed_ids = []
    if isinstance(prior_summary, dict):
        prior_completed_ids = list(prior_summary.get("completed_chapters", []))

    summary = analyze_book(
        project_slug=project_slug,
        fail_fast=fail_fast,
        chapters=failed_paths,
    )

    if prior_completed_ids:
        merged_completed = _ordered_unique(prior_completed_ids + summary.completed_chapters)
        merged_failed = summary.failed_chapters
        update_world_sequence_state(
            project_slug=project_slug,
            succeeded_chapter_ids=merged_completed,
            failed_chapter_ids=merged_failed,
        )

    return summary


def refine_world(project_slug: str, *, use_llm: bool = True, apply_changes: bool = True) -> dict[str, object]:
    summary = refine_world_identities(
        project_slug=project_slug,
        use_llm=use_llm,
        apply_changes=apply_changes,
    )
    return summary.to_dict()


def _build_book_run_summary(
    *,
    project_slug: str,
    manifest_path: str,
    status: str,
    started_at_utc: str,
    completed_at_utc: str,
    chapter_results: list[ChapterRunResult],
    succeeded_ids: list[str],
    failed_ids: list[str],
    skipped_chapters: list[str],
    sequence_state_path: str,
    failure_log_path: str | None,
) -> BookRunSummary:
    written_files = [
        repo_relative(_book_run_latest_path(project_slug)),
        repo_relative(_book_run_timestamp_path(project_slug, started_at_utc)),
        repo_relative(_failed_chapters_json_path(project_slug)),
        repo_relative(_failed_chapters_report_path(project_slug)),
        sequence_state_path,
    ]
    if failure_log_path:
        written_files.append(failure_log_path)
    written_files = _ordered_unique(written_files)
    return BookRunSummary(
        project_slug=project_slug,
        manifest_path=manifest_path,
        status=status,
        started_at_utc=started_at_utc,
        completed_at_utc=completed_at_utc,
        chapter_results=chapter_results,
        completed_chapters=succeeded_ids,
        failed_chapters=failed_ids,
        skipped_chapters=skipped_chapters,
        written_files=written_files,
    )


def _write_book_run_artifacts(summary: BookRunSummary) -> None:
    run_dir = _book_runs_dir(summary.project_slug)
    timestamp_path = _book_run_timestamp_path(summary.project_slug, summary.started_at_utc)
    latest_path = _book_run_latest_path(summary.project_slug)
    failed_json_path = _failed_chapters_json_path(summary.project_slug)
    failed_report_path = _failed_chapters_report_path(summary.project_slug)

    run_payload = summary.to_dict()
    _write_json(latest_path, run_payload)
    _write_json(timestamp_path, run_payload)
    _write_json(failed_json_path, _build_failed_chapters_payload(summary))
    failed_report_path.write_text(_build_failed_chapters_report(summary), encoding="utf-8")
    ensure_dir(run_dir)


def _build_failed_chapters_payload(summary: BookRunSummary) -> dict[str, Any]:
    failed_entries = [
        {
            "chapter_id": result.chapter_id,
            "chapter_path": result.chapter_path,
            "failed_stage": result.failed_stage,
            "error_type": result.error_type,
            "error_message": result.error_message,
            "chapter_summary_path": result.chapter_summary_path,
            "continuity_state_path": result.continuity_state_path,
            "continuity_summary_path": result.continuity_summary_path,
            "snapshot_path": result.snapshot_path,
        }
        for result in summary.chapter_results
        if result.status == "failed"
    ]
    return {
        "project_slug": summary.project_slug,
        "manifest_path": summary.manifest_path,
        "book_run_path": repo_relative(_book_run_latest_path(summary.project_slug)),
        "generated_at_utc": summary.completed_at_utc,
        "failed_chapters": failed_entries,
    }


def _build_failed_chapters_report(summary: BookRunSummary) -> str:
    lines = [
        "# Failed Chapters Report",
        "",
        f"- project_slug: {summary.project_slug}",
        f"- manifest_path: {summary.manifest_path}",
        f"- generated_at_utc: {summary.completed_at_utc}",
        "",
    ]
    failed_results = [result for result in summary.chapter_results if result.status == "failed"]
    if not failed_results:
        lines.extend(["- None", ""])
        return "\n".join(lines)

    for result in failed_results:
        lines.append(f"- {result.chapter_id}")
        lines.append(f"  - path: {result.chapter_path}")
        lines.append(f"  - stage: {result.failed_stage}")
        lines.append(f"  - error_type: {result.error_type}")
        lines.append(f"  - error: {result.error_message}")
    lines.append("")
    return "\n".join(lines)


def _classify_book_error(exc: Exception) -> tuple[str, str]:
    message = str(exc)
    if "Character extraction returned no usable character records" in message:
        return "character_extraction_validation", message
    if "Environment extraction returned no usable" in message:
        return "environment_extraction_validation", message
    if "Scene decomposition" in message:
        return "scene_decomposition_validation", message
    if "snapshot" in message.lower():
        return "snapshot_generation", message
    return type(exc).__name__, message


def _book_runs_dir(project_slug: str) -> Path:
    project_dir = create_project(project_slug)
    path = project_dir / "02_story_analysis" / "runs"
    ensure_dir(path)
    return path


def _book_run_latest_path(project_slug: str) -> Path:
    return _book_runs_dir(project_slug) / "BOOK_RUN_latest.json"


def _book_run_timestamp_path(project_slug: str, started_at_utc: str) -> Path:
    timestamp = _sanitize_timestamp_for_filename(started_at_utc)
    return _book_runs_dir(project_slug) / f"BOOK_RUN_{timestamp}.json"


def _failed_chapters_json_path(project_slug: str) -> Path:
    return _book_runs_dir(project_slug) / "failed_chapters.json"


def _failed_chapters_report_path(project_slug: str) -> Path:
    return _book_runs_dir(project_slug) / "FAILED_CHAPTERS_REPORT.md"


def _load_latest_failed_chapters(*, project_slug: str) -> dict[str, Any]:
    path = _failed_chapters_json_path(project_slug)
    if not path.exists():
        return {}
    payload = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(payload, dict):
        return payload
    return {}


def _resolve_requested_chapter_paths(
    *,
    project_dir: Path,
    manifest_chapter_paths: list[Path],
    chapters: list[str] | None,
    retry_failed_only: bool,
) -> list[Path]:
    if retry_failed_only:
        failed_payload = _load_latest_failed_chapters(project_slug=project_dir.name)
        failed_entries = list(failed_payload.get("failed_chapters", []))
        return _ordered_unique(
            [
                _resolve_chapter_path(project_dir=project_dir, chapter_value=entry["chapter_path"])
                for entry in failed_entries
                if entry.get("chapter_path")
            ]
        )

    if chapters is None:
        return list(manifest_chapter_paths)

    resolved = [_resolve_chapter_path(project_dir=project_dir, chapter_value=chapter) for chapter in chapters]
    return _ordered_unique(resolved)


def _resolve_chapter_path(*, project_dir: Path, chapter_value: str) -> Path:
    candidate = Path(chapter_value)
    if candidate.is_absolute():
        return candidate
    if candidate.exists():
        return candidate
    repo_root = project_dir.parent.parent
    repo_candidate = repo_root / candidate
    if repo_candidate.exists():
        return repo_candidate
    project_candidate = project_dir / candidate
    if project_candidate.exists():
        return project_candidate
    chapter_dir = project_dir / "01_source" / "chapters"
    chapter_candidate = chapter_dir / candidate.name
    if chapter_candidate.exists():
        return chapter_candidate
    return repo_candidate


def _chapter_id_from_path(chapter_path: Path) -> str:
    match = _CHAPTER_ID_RE.search(chapter_path.stem)
    if match:
        return match.group(1).upper()
    return chapter_path.name.split("_")[0].upper()


def _derive_skipped_chapters(*, manifest_chapter_paths: list[Path], processed_chapter_ids: list[str]) -> list[str]:
    processed = {chapter_id.upper() for chapter_id in processed_chapter_ids}
    skipped: list[str] = []
    for chapter_path in manifest_chapter_paths:
        chapter_id = _chapter_id_from_path(chapter_path)
        if chapter_id not in processed:
            skipped.append(chapter_id)
    return skipped


def _book_run_status(chapter_results: list[ChapterRunResult]) -> str:
    completed = sum(1 for result in chapter_results if result.status == "completed")
    failed = sum(1 for result in chapter_results if result.status == "failed")
    if failed == 0:
        return "completed"
    if completed == 0:
        return "failed"
    return "completed_with_failures"


def _ordered_unique(items: list[Any]) -> list[Any]:
    seen: set[Any] = set()
    result: list[Any] = []
    for item in items:
        marker = item
        try:
            if marker in seen:
                continue
        except TypeError:
            marker = repr(item)
            if marker in seen:
                continue
        seen.add(marker)
        result.append(item)
    return result


def _empty_book_run_summary(*, project_slug: str, manifest_path: str, started_at_utc: str) -> BookRunSummary:
    completed_at_utc = _utc_now_iso()
    status = "completed"
    run = BookRunSummary(
        project_slug=project_slug,
        manifest_path=manifest_path,
        status=status,
        started_at_utc=started_at_utc,
        completed_at_utc=completed_at_utc,
        chapter_results=[],
        completed_chapters=[],
        failed_chapters=[],
        skipped_chapters=[],
        written_files=[],
    )
    return run


def _repo_relative_or_input(path: Path) -> str:
    try:
        return repo_relative(path)
    except Exception:
        return path.as_posix()


def _sanitize_timestamp_for_filename(value: str) -> str:
    return value.replace(":", "").replace("-", "").replace(".", "").replace("+", "p")


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


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


def _write_json(path: Path, data: object) -> None:
    ensure_dir(path.parent)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
