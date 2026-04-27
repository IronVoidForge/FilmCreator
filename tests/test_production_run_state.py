import json
from pathlib import Path

from orchestrator.production_run_state import persist_run_summary


def test_persist_run_summary_writes_latest_and_timestamped_files(tmp_path: Path) -> None:
    project_root = tmp_path / "projects" / "demo"
    project_root.mkdir(parents=True)

    run_path = persist_run_summary(
        project_slug="demo",
        run_type="project_status",
        payload={"project_slug": "demo", "status": "ok"},
        repo_root=tmp_path,
    )

    timestamped = Path(run_path)
    latest = project_root / "02_story_analysis" / "runs" / "production" / "production_menu_latest.json"
    assert timestamped.exists()
    assert latest.exists()
    payload = json.loads(latest.read_text(encoding="utf-8"))
    assert payload["run_type"] == "project_status"
    assert payload["payload"]["status"] == "ok"
