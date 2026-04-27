from types import SimpleNamespace

from orchestrator.production_pipeline import run_full_production_pipeline, run_prompt_prep_refresh


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


def test_run_full_production_resume_skips_completed_and_runs_remaining(monkeypatch) -> None:
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

    summary = run_full_production_pipeline("demo", chapters="2-3", mode="resume")

    assert "character_taxonomy" in summary.completed_phases
    assert project_phase_calls == ["identity_refinement", "character_bibles", "environment_bibles", "visual_fallbacks"]
    assert downstream_calls == [("demo", "2-3", "scene_bindings", "resume")]
    assert summary.phase_summaries["character_taxonomy"]["skipped"] is True
    assert summary.phase_summaries["quality_grading"]["phase"] == "quality_grading"
