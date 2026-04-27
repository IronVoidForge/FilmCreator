import json
from pathlib import Path

from orchestrator.production_cleanup import create_cleanup_plan, execute_cleanup_plan


def test_create_cleanup_plan_writes_expected_targets(tmp_path: Path) -> None:
    project_root = tmp_path / "projects" / "demo"
    (project_root / "02_story_analysis" / "contracts").mkdir(parents=True)
    (project_root / "03_prompt_packages" / "prepared").mkdir(parents=True)

    summary = create_cleanup_plan("demo", scope="downstream_only", repo_root=tmp_path)

    assert summary.scope == "downstream_only"
    assert Path(summary.plan_path).exists()
    payload = json.loads(Path(summary.plan_path).read_text(encoding="utf-8"))
    assert payload["scope"] == "downstream_only"
    assert any(target["relative_path"] == "02_story_analysis/contracts" for target in payload["targets"])


def test_execute_cleanup_plan_deletes_only_planned_targets(tmp_path: Path) -> None:
    project_root = tmp_path / "projects" / "demo"
    contracts = project_root / "02_story_analysis" / "contracts"
    descriptors = project_root / "02_story_analysis" / "descriptors"
    source_dir = project_root / "01_source"
    contracts.mkdir(parents=True)
    descriptors.mkdir(parents=True)
    source_dir.mkdir(parents=True)
    (contracts / "a.json").write_text("{}", encoding="utf-8")
    (descriptors / "b.json").write_text("{}", encoding="utf-8")
    (source_dir / "keep.txt").write_text("keep", encoding="utf-8")

    create_cleanup_plan("demo", scope="downstream_only", repo_root=tmp_path)
    summary = execute_cleanup_plan("demo", repo_root=tmp_path)

    assert not contracts.exists()
    assert not descriptors.exists()
    assert source_dir.exists()
    assert summary.verification_failed == []
