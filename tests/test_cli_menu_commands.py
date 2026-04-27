import json
import sys
import orchestrator.__main__  # noqa: F401


def _load_legacy_cli_module():
    return sys.modules["orchestrator._legacy_cli"]


def test_cli_project_status_command_persists_and_prints(monkeypatch, capsys) -> None:
    cli_module = _load_legacy_cli_module()
    monkeypatch.setattr(
        sys,
        "argv",
        ["orchestrator", "project-status", "demo", "--chapters", "2-3"],
    )
    monkeypatch.setattr(
        cli_module,
        "get_production_status",
        lambda project_slug, chapters=None: type(
            "Summary",
            (),
            {"to_dict": lambda self: {"project_slug": project_slug, "chapters": chapters, "command": "project-status"}},
        )(),
    )
    persisted: list[tuple[str, str, dict]] = []
    monkeypatch.setattr(
        cli_module,
        "persist_run_summary",
        lambda project_slug, run_type, payload: persisted.append((project_slug, run_type, payload)),
    )

    cli_module.main()

    out = capsys.readouterr().out
    payload = json.loads(out)
    assert payload["project_slug"] == "demo"
    assert persisted[0][0] == "demo"
    assert persisted[0][1] == "project-status"


def test_cli_run_quicktest_composite_dispatches(monkeypatch, capsys) -> None:
    cli_module = _load_legacy_cli_module()
    monkeypatch.setattr(
        sys,
        "argv",
        ["orchestrator", "run-quicktest-composite", "demo", "--composite", "11_to_14", "--chapters", "2-3"],
    )
    monkeypatch.setattr(
        cli_module,
        "run_quicktest_composite",
        lambda project_slug, chapters=None, composite="": {"project_slug": project_slug, "chapters": chapters, "profile": composite},
    )
    monkeypatch.setattr(
        cli_module,
        "persist_run_summary",
        lambda project_slug, run_type, payload: None,
    )

    cli_module.main()

    out = capsys.readouterr().out
    payload = json.loads(out)
    assert payload["profile"] == "11_to_14"
    assert payload["chapters"] == "2-3"
