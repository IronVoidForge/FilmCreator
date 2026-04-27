from types import SimpleNamespace

from orchestrator.production_pipeline import (
    _resolve_story_analysis_chapter_paths,
    plan_trusted_resume_pipeline,
    run_quicktest_composite,
    run_full_production_pipeline,
    run_prompt_prep_refresh,
    run_story_analysis_pipeline,
    run_trusted_resume_pipeline,
)


def test_run_prompt_prep_refresh_force_runs_both(monkeypatch) -> None:
    calls: list[tuple[str, str | None, bool]] = []

    def fake_descriptor(project_slug, *, use_llm, force, chapters, run_tracker=None):
        calls.append(("descriptor_enrichment", chapters, force))
        return {"phase": "descriptor_enrichment"}

    def fake_prompt(project_slug, *, force, chapters, shot_variants=None, run_tracker=None, limit=None):
        calls.append(("prompt_preparation", chapters, force))
        return {"phase": "prompt_preparation"}

    monkeypatch.setattr("orchestrator.production_pipeline.run_descriptor_enrichment", fake_descriptor)
    monkeypatch.setattr("orchestrator.production_pipeline.run_prompt_preparation", fake_prompt)

    summary = run_prompt_prep_refresh("demo", chapters="2-3", mode="force")

    assert summary.completed_phases == ["descriptor_enrichment", "prompt_preparation"]
    assert calls == [
        ("descriptor_enrichment", "2-3", True),
        ("prompt_preparation", "2-3", True),
    ]


def test_run_full_production_force_runs_remaining_pipeline(monkeypatch) -> None:
    monkeypatch.setattr(
        "orchestrator.production_pipeline.get_production_status",
        lambda project_slug, chapters=None: SimpleNamespace(
            phases=[
                {"phase": "character_taxonomy", "complete": True},
                {"phase": "identity_refinement", "complete": False},
                {"phase": "character_bibles", "complete": False},
                {"phase": "environment_bibles", "complete": False},
                {"phase": "visual_fallbacks", "complete": False},
                {"phase": "scene_contracts", "complete": True},
                {"phase": "scene_bindings", "complete": False},
                {"phase": "shot_packages", "complete": False},
                {"phase": "dialogue_timeline", "complete": False},
                {"phase": "descriptor_enrichment", "complete": False},
                {"phase": "prompt_preparation", "complete": False},
                {"phase": "quality_grading", "complete": False},
            ]
        ),
    )

    project_phase_calls: list[str] = []

    def fake_project_phase(project_slug, phase_name, *, mode):
        project_phase_calls.append(phase_name)
        return {"phase": phase_name}

    downstream_calls: list[tuple[str, str | None, str, str]] = []

    def fake_downstream(project_slug, *, chapters=None, start_phase="scene_contracts", mode="resume"):
        downstream_calls.append((project_slug, chapters, start_phase, mode))
        return SimpleNamespace(
            completed_phases=["scene_bindings", "shot_packages", "dialogue_timeline", "descriptor_enrichment", "prompt_preparation"],
            phase_summaries={"scene_bindings": {"phase": "scene_bindings"}},
        )

    monkeypatch.setattr("orchestrator.production_pipeline._run_project_phase", fake_project_phase)
    monkeypatch.setattr("orchestrator.production_pipeline.run_downstream_production", fake_downstream)
    monkeypatch.setattr("orchestrator.production_pipeline.run_quality_grading", lambda project_slug: {"phase": "quality_grading"})

    summary = run_full_production_pipeline("demo", chapters="2-3", mode="force")

    assert project_phase_calls == ["character_taxonomy", "identity_refinement", "character_bibles", "environment_bibles", "visual_fallbacks"]
    assert downstream_calls == [("demo", "2-3", "scene_contracts", "force")]
    assert summary.phase_summaries["quality_grading"]["phase"] == "quality_grading"


def test_run_story_analysis_pipeline_resume_uses_resume_runner(monkeypatch) -> None:
    monkeypatch.setattr(
        "orchestrator.production_pipeline.run_resume_book_analysis",
        lambda project_slug, fail_fast=False: {"project_slug": project_slug, "resume": True},
    )

    summary = run_story_analysis_pipeline("demo", mode="resume")

    assert summary.completed_phases == ["story_analysis"]
    assert summary.phase_summaries["story_analysis"]["resume"] is True


def test_plan_trusted_resume_pipeline_matches_bat_mapping(monkeypatch) -> None:
    monkeypatch.setattr(
        "orchestrator.production_pipeline.find_first_incomplete_stage",
        lambda project_slug, chapters="": "descriptor_enrichment",
    )

    summary = plan_trusted_resume_pipeline("demo", chapters="2-3")

    assert summary.phase_summaries["resume_stage"] == "descriptor_enrichment"
    assert summary.phase_summaries["start_phase"] == "descriptor_enrichment"
    assert summary.phase_summaries["planned_phases"] == ["descriptor_enrichment", "prompt_preparation", "quality_grading"]


def test_run_trusted_resume_pipeline_uses_forced_bat_sequence(monkeypatch) -> None:
    monkeypatch.setattr(
        "orchestrator.production_pipeline.find_first_incomplete_stage",
        lambda project_slug, chapters="": "character_taxonomy",
    )
    calls: list[tuple[str, str | None]] = []
    monkeypatch.setattr(
        "orchestrator.production_pipeline.lmstudio_check",
        lambda: {"phase": "lmstudio_check"},
    )

    def fake_trusted(project_slug, phase_name, *, chapters=None):
        calls.append((phase_name, chapters))
        return {"phase": phase_name}

    monkeypatch.setattr("orchestrator.production_pipeline._run_trusted_phase", fake_trusted)

    summary = run_trusted_resume_pipeline("demo", chapters="2-3")

    assert summary.completed_phases[0] == "character_taxonomy"
    assert calls[0] == ("character_taxonomy", "2-3")
    assert calls[-1] == ("quality_grading", "2-3")


def test_run_quicktest_composite_11_to_14_maps_to_shot_packages(monkeypatch) -> None:
    monkeypatch.setattr(
        "orchestrator.production_pipeline.run_downstream_production",
        lambda project_slug, chapters=None, start_phase="scene_contracts", mode="resume": {
            "project_slug": project_slug,
            "chapters": chapters,
            "start_phase": start_phase,
            "mode": mode,
        },
    )

    summary = run_quicktest_composite("demo", chapters="2-3", composite="11_to_14")

    assert summary["start_phase"] == "shot_packages"
    assert summary["mode"] == "force"


def test_resolve_story_analysis_chapter_paths_filters_manifest(monkeypatch, tmp_path) -> None:
    project_root = tmp_path / "projects" / "demo" / "01_source" / "book"
    project_root.mkdir(parents=True)
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(
        "orchestrator.production_pipeline._read_manifest_chapter_paths",
        lambda project_dir, manifest_path: [
            tmp_path / "projects" / "demo" / "01_source" / "chapters" / "CH001_one.md",
            tmp_path / "projects" / "demo" / "01_source" / "chapters" / "CH002_two.md",
            tmp_path / "projects" / "demo" / "01_source" / "chapters" / "CH003_three.md",
        ],
    )
    monkeypatch.setattr(
        "orchestrator.production_pipeline._chapter_id_from_path",
        lambda path: path.name.split("_", 1)[0],
    )

    resolved = _resolve_story_analysis_chapter_paths("demo", "2-3")

    assert [path.name for path in resolved] == ["CH002_two.md", "CH003_three.md"]
