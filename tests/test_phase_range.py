from orchestrator.production_pipeline import format_production_run_summary, run_phase_range


def test_run_phase_range_force_runs_selected_span(monkeypatch) -> None:
    calls: list[str] = []

    def fake_run(project_slug, phase_name, *, chapters=None, mode="force"):
        calls.append(phase_name)
        return {"phase": phase_name}

    monkeypatch.setattr("orchestrator.production_pipeline._run_operator_phase", fake_run)

    summary = run_phase_range(
        "demo",
        start_phase="scene_bindings",
        end_phase="descriptor_enrichment",
        chapters="2-3",
        mode="force",
    )

    assert calls == ["scene_bindings", "shot_packages", "dialogue_timeline", "descriptor_enrichment"]
    lines = format_production_run_summary(summary)
    assert any("Range: scene_bindings -> descriptor_enrichment" in line for line in lines)


def test_run_phase_range_resume_skips_completed(monkeypatch) -> None:
    monkeypatch.setattr(
        "orchestrator.production_pipeline.get_production_status",
        lambda project_slug, chapters=None: type(
            "StatusSummary",
            (),
            {
                "phases": [
                    {"phase": "scene_contracts", "complete": True},
                    {"phase": "scene_bindings", "complete": False},
                ]
            },
        )(),
    )
    calls: list[str] = []

    def fake_run(project_slug, phase_name, *, chapters=None, mode="resume"):
        calls.append(phase_name)
        return {"phase": phase_name}

    monkeypatch.setattr("orchestrator.production_pipeline._run_operator_phase", fake_run)

    summary = run_phase_range(
        "demo",
        start_phase="scene_contracts",
        end_phase="scene_bindings",
        chapters="2-3",
        mode="resume",
    )

    assert summary.phase_summaries["scene_contracts"]["skipped"] is True
    assert calls == ["scene_bindings"]
