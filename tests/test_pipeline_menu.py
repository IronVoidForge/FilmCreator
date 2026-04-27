from pathlib import Path

from orchestrator.pipeline_menu import run_pipeline_menu


def test_pipeline_menu_updates_quick_slice_and_exits(tmp_path: Path) -> None:
    projects_root = tmp_path / "projects"
    (projects_root / "demo").mkdir(parents=True)
    prompts = iter(["2", "2", "14"])
    outputs: list[str] = []

    state = run_pipeline_menu(
        initial_project="demo",
        input_fn=lambda prompt="": next(prompts),
        output_fn=outputs.append,
        projects_root=projects_root,
    )

    assert state.chapters == "2-3"
    assert any("Chapters updated to: 2-3" in line for line in outputs)
    assert any("Exiting pipeline menu." in line for line in outputs)


def test_pipeline_menu_startup_scope_prompts_project_and_all_chapters(tmp_path: Path) -> None:
    projects_root = tmp_path / "projects"
    (projects_root / "demo").mkdir(parents=True)
    prompts = iter(["demo", "", "14"])
    outputs: list[str] = []

    state = run_pipeline_menu(
        initial_project="princess_of_mars_test",
        prompt_on_start=True,
        input_fn=lambda prompt="": next(prompts),
        output_fn=outputs.append,
        projects_root=projects_root,
    )

    assert state.project_slug == "demo"
    assert state.chapters is None
    assert any("Project set to: demo" in line for line in outputs)
    assert any("Chapters set to: ALL" in line for line in outputs)


def test_pipeline_menu_character_reference_plan_uses_current_limit(monkeypatch) -> None:
    prompts = iter(["10", "3", "4", "10", "1", "14"])
    outputs: list[str] = []
    called: dict[str, object] = {}

    monkeypatch.setattr(
        "orchestrator.pipeline_menu.run_character_reference_planning",
        lambda project_slug, force=False, variants=None, limit=None: called.setdefault(
            "summary",
            {"project_slug": project_slug, "limit": limit},
        ),
    )

    state = run_pipeline_menu(
        input_fn=lambda prompt="": next(prompts),
        output_fn=outputs.append,
        projects_root=Path("projects"),
    )

    assert state.character_reference_limit == 4
    assert called["summary"]["limit"] == 4
    assert any('"limit": 4' in line for line in outputs)


def test_pipeline_menu_story_analysis_selected_slice(monkeypatch) -> None:
    prompts = iter(["2", "2", "6", "2", "14"])
    outputs: list[str] = []
    called: dict[str, object] = {}

    monkeypatch.setattr(
        "orchestrator.pipeline_menu.run_story_analysis_pipeline",
        lambda project_slug, chapters=None, mode="resume": called.setdefault(
            "summary",
            {"project_slug": project_slug, "chapters": chapters, "mode": mode},
        ),
    )

    run_pipeline_menu(
        initial_project="demo",
        input_fn=lambda prompt="": next(prompts),
        output_fn=outputs.append,
        projects_root=Path("projects"),
    )

    assert called["summary"]["chapters"] == "2-3"
    assert any('"chapters": "2-3"' in line for line in outputs)


def test_pipeline_menu_downstream_quicktest_composite(monkeypatch) -> None:
    prompts = iter(["8", "9", "14"])
    outputs: list[str] = []
    called: dict[str, object] = {}

    monkeypatch.setattr(
        "orchestrator.pipeline_menu.run_quicktest_composite",
        lambda project_slug, chapters=None, composite="": called.setdefault(
            "summary",
            {"project_slug": project_slug, "chapters": chapters, "composite": composite},
        ),
    )

    run_pipeline_menu(
        initial_project="demo",
        input_fn=lambda prompt="": next(prompts),
        output_fn=outputs.append,
        projects_root=Path("projects"),
    )

    assert called["summary"]["composite"] == "11_to_14"
    assert called["summary"]["chapters"] == "2-3"


def test_pipeline_menu_cleanup_dry_run(monkeypatch) -> None:
    prompts = iter(["12", "2", "14"])
    outputs: list[str] = []

    monkeypatch.setattr(
        "orchestrator.pipeline_menu.create_cleanup_plan",
        lambda project_slug, scope="": {
            "project_slug": project_slug,
            "scope": scope,
            "plan_path": "plan.json",
            "targets": [{"relative_path": "02_story_analysis/contracts", "kind": "dir", "exists": True}],
            "preserved": ["01_source"],
        },
    )
    monkeypatch.setattr(
        "orchestrator.pipeline_menu.format_cleanup_plan",
        lambda summary: ["Project: demo", "Scope: downstream_only", "- dir: 02_story_analysis/contracts (EXISTS)"],
    )

    run_pipeline_menu(
        initial_project="demo",
        input_fn=lambda prompt="": next(prompts),
        output_fn=outputs.append,
        projects_root=Path("projects"),
    )

    assert any("Scope: downstream_only" in line for line in outputs)


def test_pipeline_menu_advanced_range_runs_selected_span(monkeypatch) -> None:
    prompts = iter(["13", "9", "13", "14"])
    outputs: list[str] = []
    called: dict[str, object] = {}

    monkeypatch.setattr(
        "orchestrator.pipeline_menu.run_phase_range",
        lambda project_slug, start_phase="", end_phase="", chapters=None, mode="force": called.setdefault(
            "summary",
            {
                "project_slug": project_slug,
                "profile": "phase_range",
                "start_phase": start_phase,
                "end_phase": end_phase,
                "chapters": chapters,
                "mode": mode,
            },
        ),
    )

    run_pipeline_menu(
        initial_project="demo",
        initial_chapters="2-3",
        initial_mode="force",
        input_fn=lambda prompt="": next(prompts),
        output_fn=outputs.append,
        projects_root=Path("projects"),
    )

    assert called["summary"]["start_phase"] == "scene_contracts"
    assert called["summary"]["end_phase"] == "descriptor_enrichment"
