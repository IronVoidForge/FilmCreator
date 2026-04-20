from __future__ import annotations

import json
from types import SimpleNamespace
from pathlib import Path

import pytest

import orchestrator.book_authoring as book_authoring_module
from orchestrator.lmstudio_client import LMStudioError


def _make_analysis(project_slug: str, chapter_id: str, chapter_path: str, scene_ids: list[str]) -> SimpleNamespace:
    return SimpleNamespace(
        project_slug=project_slug,
        chapter_path=chapter_path,
        chapter_id=chapter_id,
        model="test-model",
        written_files=[],
        scene_ids=scene_ids,
        manual_character_description_requests=[],
        character_clarification_requests=[],
        warnings=[],
        canonical_character_ids=[f"{chapter_id.lower()}_character"],
        provisional_character_ids=[],
        canonical_environment_ids=[f"{chapter_id.lower()}_environment"],
        provisional_environment_ids=[],
        world_registry_paths=[
            f"projects/{project_slug}/02_story_analysis/world/CHARACTER_REGISTRY.json",
            f"projects/{project_slug}/02_story_analysis/world/ENVIRONMENT_REGISTRY.json",
        ],
    )


def _write_chapter_file(path: Path, chapter_id: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "\n".join(
            [
                "# Chapter",
                chapter_id,
                "",
                "# Title",
                chapter_id,
                "",
                "# Text",
                f"{chapter_id} body text.",
                "",
            ]
        ),
        encoding="utf-8",
    )


def test_analyze_book_continues_after_failure_and_writes_run_artifacts(tmp_path: Path, monkeypatch) -> None:
    project_slug = "demo"
    projects_root = tmp_path / "projects"
    project_dir = projects_root / project_slug
    manifest_path = project_dir / "01_source" / "book" / "book_manifest.md"
    chapter_dir = project_dir / "01_source" / "chapters"

    monkeypatch.setattr(book_authoring_module, "create_project", lambda slug: project_dir)
    monkeypatch.setattr(book_authoring_module, "repo_relative", lambda path: path.relative_to(tmp_path).as_posix())

    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    _write_chapter_file(chapter_dir / "CH001_alpha.md", "CH001")
    _write_chapter_file(chapter_dir / "CH002_beta.md", "CH002")
    _write_chapter_file(chapter_dir / "CH003_gamma.md", "CH003")
    manifest_path.write_text(
        "\n".join(
            [
                "# Book Manifest",
                "",
                "## Chapter Order",
                "",
                "- CH001: projects/demo/01_source/chapters/CH001_alpha.md",
                "- CH002: projects/demo/01_source/chapters/CH002_beta.md",
                "- CH003: projects/demo/01_source/chapters/CH003_gamma.md",
                "",
            ]
        ),
        encoding="utf-8",
    )

    written_snapshots: dict[str, dict[str, object]] = {}
    sequence_updates: list[tuple[list[str], list[str]]] = []
    failure_log_entries: list[dict[str, str]] = []

    def fake_analyze_chapter(*, project_slug: str, chapter: str):  # noqa: ARG001
        chapter_id = Path(chapter).stem.split("_")[0]
        if chapter_id == "CH002":
            raise LMStudioError("Character extraction returned no usable character records after validation.")
        return _make_analysis(project_slug, chapter_id, chapter, [f"{chapter_id}_SC001"])

    def fake_update_global_character_state(*, project_slug: str, analysis):  # noqa: ARG001
        return (
            f"projects/{project_slug}/02_story_analysis/world/global/CHARACTER_REGISTRY_GLOBAL.json",
            f"projects/{project_slug}/02_story_analysis/world/global/CHARACTER_DIRECTORY.json",
        )

    def fake_update_global_environment_state(*, project_slug: str, analysis):  # noqa: ARG001
        return (
            f"projects/{project_slug}/02_story_analysis/world/global/ENVIRONMENT_REGISTRY_GLOBAL.json",
            f"projects/{project_slug}/02_story_analysis/world/global/ENVIRONMENT_DIRECTORY.json",
        )

    def fake_write_chapter_world_snapshot(
        *,
        project_slug: str,
        analysis,
        global_character_registry_relpath: str,  # noqa: ARG001
        global_environment_registry_relpath: str,  # noqa: ARG001
        global_character_directory_relpath: str,  # noqa: ARG001
        global_environment_directory_relpath: str,  # noqa: ARG001
    ) -> str:
        snapshot_path = project_dir / "02_story_analysis" / "world" / "snapshots" / f"{analysis.chapter_id}_WORLD_SNAPSHOT.json"
        snapshot_path.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "chapter_id": analysis.chapter_id,
            "chapter_path": analysis.chapter_path,
            "scene_order": analysis.scene_ids,
            "known_characters": analysis.canonical_character_ids,
            "known_environments": analysis.canonical_environment_ids,
            "provisional_roles": analysis.provisional_character_ids,
            "character_entries": [{"canonical_id": analysis.canonical_character_ids[0]}],
            "environment_entries": [{"canonical_id": analysis.canonical_environment_ids[0]}],
        }
        snapshot_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        written_snapshots[analysis.chapter_id] = payload
        return snapshot_path.relative_to(tmp_path).as_posix()

    def fake_load_world_snapshot(*, project_slug: str, chapter_id: str):  # noqa: ARG001
        return written_snapshots.get(chapter_id, {})

    def fake_build_chapter_continuity(*, project_slug: str, analysis, snapshot_data=None):  # noqa: ARG001
        state_path = project_dir / "02_story_analysis" / "world" / "continuity" / f"{analysis.chapter_id}_STATE.json"
        summary_path = project_dir / "02_story_analysis" / "world" / "continuity" / f"{analysis.chapter_id}_CONTINUITY_SUMMARY.md"
        state_path.parent.mkdir(parents=True, exist_ok=True)
        state_path.write_text("{}", encoding="utf-8")
        summary_path.write_text(f"# {analysis.chapter_id}", encoding="utf-8")
        return SimpleNamespace(
            chapter_id=analysis.chapter_id,
            state_path=state_path.relative_to(tmp_path).as_posix(),
            summary_path=summary_path.relative_to(tmp_path).as_posix(),
            known_characters=[],
            known_environments=[],
            unresolved_character_ids=[],
            scene_order=list(analysis.scene_ids),
        )

    def fake_append_world_failure(
        *,
        project_slug: str,  # noqa: ARG001
        chapter_id: str,  # noqa: ARG001
        chapter_path: str,  # noqa: ARG001
        stage: str,
        error: str,
        failure_artifact_path: str | None,  # noqa: ARG001
    ) -> str:
        failure_log_entries.append({"stage": stage, "error": error})
        return f"projects/{project_slug}/02_story_analysis/world/global/WORLD_FAILURE_LOG.json"

    def fake_update_world_sequence_state(*, project_slug: str, succeeded_chapter_ids: list[str], failed_chapter_ids: list[str]) -> str:  # noqa: ARG001
        sequence_updates.append((list(succeeded_chapter_ids), list(failed_chapter_ids)))
        sequence_path = project_dir / "02_story_analysis" / "world" / "global" / "WORLD_SEQUENCE_STATE.json"
        sequence_path.parent.mkdir(parents=True, exist_ok=True)
        sequence_path.write_text(
            json.dumps(
                {
                    "processed_chapters": succeeded_chapter_ids,
                    "failed_chapters": failed_chapter_ids,
                },
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        return sequence_path.relative_to(tmp_path).as_posix()

    monkeypatch.setattr(book_authoring_module, "analyze_chapter", fake_analyze_chapter)
    monkeypatch.setattr(book_authoring_module, "update_global_character_state", fake_update_global_character_state)
    monkeypatch.setattr(book_authoring_module, "update_global_environment_state", fake_update_global_environment_state)
    monkeypatch.setattr(book_authoring_module, "write_chapter_world_snapshot", fake_write_chapter_world_snapshot)
    monkeypatch.setattr(book_authoring_module, "load_world_snapshot", fake_load_world_snapshot)
    monkeypatch.setattr(book_authoring_module, "build_chapter_continuity", fake_build_chapter_continuity)
    monkeypatch.setattr(book_authoring_module, "append_world_failure", fake_append_world_failure)
    monkeypatch.setattr(book_authoring_module, "update_world_sequence_state", fake_update_world_sequence_state)

    summary = book_authoring_module.analyze_book(project_slug=project_slug)

    assert summary.status == "completed_with_failures"
    assert summary.completed_chapters == ["CH001", "CH003"]
    assert summary.failed_chapters == ["CH002"]
    assert summary.skipped_chapters == []
    assert [result.chapter_id for result in summary.chapter_results] == ["CH001", "CH002", "CH003"]
    assert summary.chapter_results[1].failed_stage == "character_extraction_validation"
    assert sequence_updates[-1] == (["CH001", "CH003"], ["CH002"])
    assert failure_log_entries == [{"stage": "character_extraction_validation", "error": "Character extraction returned no usable character records after validation."}]

    run_dir = project_dir / "02_story_analysis" / "runs"
    latest_run = json.loads((run_dir / "BOOK_RUN_latest.json").read_text(encoding="utf-8"))
    failed_payload = json.loads((run_dir / "failed_chapters.json").read_text(encoding="utf-8"))
    report_text = (run_dir / "FAILED_CHAPTERS_REPORT.md").read_text(encoding="utf-8")

    assert latest_run["status"] == "completed_with_failures"
    assert latest_run["failed_chapters"] == ["CH002"]
    assert failed_payload["failed_chapters"][0]["chapter_id"] == "CH002"
    assert "CH002" in report_text


def test_retry_failed_chapters_reprocesses_only_failed_entries(tmp_path: Path, monkeypatch) -> None:
    project_slug = "demo"
    projects_root = tmp_path / "projects"
    project_dir = projects_root / project_slug
    manifest_path = project_dir / "01_source" / "book" / "book_manifest.md"
    chapter_dir = project_dir / "01_source" / "chapters"

    monkeypatch.setattr(book_authoring_module, "create_project", lambda slug: project_dir)
    monkeypatch.setattr(book_authoring_module, "repo_relative", lambda path: path.relative_to(tmp_path).as_posix())

    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    _write_chapter_file(chapter_dir / "CH001_alpha.md", "CH001")
    _write_chapter_file(chapter_dir / "CH002_beta.md", "CH002")
    manifest_path.write_text(
        "\n".join(
            [
                "# Book Manifest",
                "",
                "## Chapter Order",
                "",
                "- CH001: projects/demo/01_source/chapters/CH001_alpha.md",
                "- CH002: projects/demo/01_source/chapters/CH002_beta.md",
                "",
            ]
        ),
        encoding="utf-8",
    )

    # Seed a previous run with one failure.
    run_dir = project_dir / "02_story_analysis" / "runs"
    run_dir.mkdir(parents=True, exist_ok=True)
    previous_run = {
        "project_slug": project_slug,
        "manifest_path": "projects/demo/01_source/book/book_manifest.md",
        "status": "completed_with_failures",
        "started_at_utc": "2026-04-19T00:00:00+00:00",
        "completed_at_utc": "2026-04-19T00:10:00+00:00",
        "chapter_results": [],
        "completed_chapters": ["CH001"],
        "failed_chapters": ["CH002"],
        "skipped_chapters": [],
        "written_files": [],
        "chapters": [],
        "failures": [],
    }
    (run_dir / "BOOK_RUN_latest.json").write_text(json.dumps(previous_run, indent=2) + "\n", encoding="utf-8")
    (run_dir / "failed_chapters.json").write_text(
        json.dumps(
            {
                "project_slug": project_slug,
                "manifest_path": "projects/demo/01_source/book/book_manifest.md",
                "book_run_path": "projects/demo/02_story_analysis/runs/BOOK_RUN_latest.json",
                "generated_at_utc": "2026-04-19T00:10:00+00:00",
                "failed_chapters": [
                    {
                        "chapter_id": "CH002",
                        "chapter_path": "projects/demo/01_source/chapters/CH002_beta.md",
                        "failed_stage": "character_extraction_validation",
                        "error_type": "LMStudioError",
                        "error_message": "Character extraction returned no usable character records after validation.",
                    }
                ],
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    analyze_calls: list[str] = []
    sequence_updates: list[tuple[list[str], list[str]]] = []

    def fake_analyze_chapter(*, project_slug: str, chapter: str):  # noqa: ARG001
        analyze_calls.append(Path(chapter).stem.split("_")[0])
        return _make_analysis(project_slug, "CH002", chapter, ["CH002_SC001"])

    def fake_update_global_character_state(*, project_slug: str, analysis):  # noqa: ARG001
        return (
            f"projects/{project_slug}/02_story_analysis/world/global/CHARACTER_REGISTRY_GLOBAL.json",
            f"projects/{project_slug}/02_story_analysis/world/global/CHARACTER_DIRECTORY.json",
        )

    def fake_update_global_environment_state(*, project_slug: str, analysis):  # noqa: ARG001
        return (
            f"projects/{project_slug}/02_story_analysis/world/global/ENVIRONMENT_REGISTRY_GLOBAL.json",
            f"projects/{project_slug}/02_story_analysis/world/global/ENVIRONMENT_DIRECTORY.json",
        )

    def fake_write_chapter_world_snapshot(
        *,
        project_slug: str,
        analysis,
        global_character_registry_relpath: str,  # noqa: ARG001
        global_environment_registry_relpath: str,  # noqa: ARG001
        global_character_directory_relpath: str,  # noqa: ARG001
        global_environment_directory_relpath: str,  # noqa: ARG001
    ) -> str:
        snapshot_path = project_dir / "02_story_analysis" / "world" / "snapshots" / f"{analysis.chapter_id}_WORLD_SNAPSHOT.json"
        snapshot_path.parent.mkdir(parents=True, exist_ok=True)
        snapshot_path.write_text(
            json.dumps(
                {
                    "chapter_id": analysis.chapter_id,
                    "chapter_path": analysis.chapter_path,
                    "scene_order": analysis.scene_ids,
                    "known_characters": analysis.canonical_character_ids,
                    "known_environments": analysis.canonical_environment_ids,
                    "provisional_roles": analysis.provisional_character_ids,
                    "character_entries": [{"canonical_id": analysis.canonical_character_ids[0]}],
                    "environment_entries": [{"canonical_id": analysis.canonical_environment_ids[0]}],
                },
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        return snapshot_path.relative_to(tmp_path).as_posix()

    def fake_load_world_snapshot(*, project_slug: str, chapter_id: str):  # noqa: ARG001
        return {
            "chapter_id": chapter_id,
            "scene_order": ["CH002_SC001"],
            "known_characters": ["ch002_character"],
            "known_environments": ["ch002_environment"],
            "provisional_roles": [],
            "character_entries": [{"canonical_id": "ch002_character"}],
            "environment_entries": [{"canonical_id": "ch002_environment"}],
        }

    def fake_build_chapter_continuity(*, project_slug: str, analysis, snapshot_data=None):  # noqa: ARG001
        state_path = project_dir / "02_story_analysis" / "world" / "continuity" / f"{analysis.chapter_id}_STATE.json"
        summary_path = project_dir / "02_story_analysis" / "world" / "continuity" / f"{analysis.chapter_id}_CONTINUITY_SUMMARY.md"
        state_path.parent.mkdir(parents=True, exist_ok=True)
        state_path.write_text("{}", encoding="utf-8")
        summary_path.write_text(f"# {analysis.chapter_id}", encoding="utf-8")
        return SimpleNamespace(
            chapter_id=analysis.chapter_id,
            state_path=state_path.relative_to(tmp_path).as_posix(),
            summary_path=summary_path.relative_to(tmp_path).as_posix(),
            known_characters=[],
            known_environments=[],
            unresolved_character_ids=[],
            scene_order=list(analysis.scene_ids),
        )

    sequence_file = project_dir / "02_story_analysis" / "world" / "global" / "WORLD_SEQUENCE_STATE.json"

    def fake_append_world_failure(
        *,
        project_slug: str,  # noqa: ARG001
        chapter_id: str,  # noqa: ARG001
        chapter_path: str,  # noqa: ARG001
        stage: str,  # noqa: ARG001
        error: str,  # noqa: ARG001
        failure_artifact_path: str | None,  # noqa: ARG001
    ) -> str:
        return f"projects/{project_slug}/02_story_analysis/world/global/WORLD_FAILURE_LOG.json"

    def fake_update_world_sequence_state(*, project_slug: str, succeeded_chapter_ids: list[str], failed_chapter_ids: list[str]) -> str:  # noqa: ARG001
        sequence_updates.append((list(succeeded_chapter_ids), list(failed_chapter_ids)))
        sequence_file.parent.mkdir(parents=True, exist_ok=True)
        sequence_file.write_text(
            json.dumps(
                {
                    "processed_chapters": succeeded_chapter_ids,
                    "failed_chapters": failed_chapter_ids,
                },
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        return sequence_file.relative_to(tmp_path).as_posix()

    monkeypatch.setattr(book_authoring_module, "analyze_chapter", fake_analyze_chapter)
    monkeypatch.setattr(book_authoring_module, "update_global_character_state", fake_update_global_character_state)
    monkeypatch.setattr(book_authoring_module, "update_global_environment_state", fake_update_global_environment_state)
    monkeypatch.setattr(book_authoring_module, "write_chapter_world_snapshot", fake_write_chapter_world_snapshot)
    monkeypatch.setattr(book_authoring_module, "load_world_snapshot", fake_load_world_snapshot)
    monkeypatch.setattr(book_authoring_module, "build_chapter_continuity", fake_build_chapter_continuity)
    monkeypatch.setattr(book_authoring_module, "append_world_failure", fake_append_world_failure)
    monkeypatch.setattr(book_authoring_module, "update_world_sequence_state", fake_update_world_sequence_state)

    summary = book_authoring_module.retry_failed_chapters(project_slug=project_slug)

    assert analyze_calls == ["CH002"]
    assert summary.completed_chapters == ["CH002"]
    assert summary.failed_chapters == []
    assert sequence_updates[-1] == (["CH001", "CH002"], [])
    latest_run = json.loads((run_dir / "BOOK_RUN_latest.json").read_text(encoding="utf-8"))
    assert latest_run["completed_chapters"] == ["CH002"]
    failed_payload = json.loads((run_dir / "failed_chapters.json").read_text(encoding="utf-8"))
    assert failed_payload["failed_chapters"] == []

