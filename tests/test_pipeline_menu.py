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
