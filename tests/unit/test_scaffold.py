import json
from pathlib import Path

import orchestrator.scaffold as scaffold_module
import orchestrator.state as state_module
from orchestrator.common import TEMPLATES_ROOT as REAL_TEMPLATES_ROOT


def test_create_run_manifest_project_scope_uses_explicit_fields(tmp_path: Path, monkeypatch) -> None:
    projects_root = tmp_path / "projects"
    monkeypatch.setattr(scaffold_module, "PROJECTS_ROOT", projects_root)
    monkeypatch.setattr(scaffold_module, "repo_relative", lambda path: path.relative_to(tmp_path).as_posix())

    manifest_path = scaffold_module.create_run_manifest(
        "demo",
        "still.t2i.klein.distilled",
        "character_reference",
        "projects/demo/03_prompt_packages/characters/hero/hero_ref_prompt.md",
    )

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

    assert manifest["project_id"] == "demo"
    assert manifest["scene_id"] is None
    assert manifest["clip_id"] is None
    assert manifest["stage"] == "character_reference"
    assert manifest["workflow_id"] == "still.t2i.klein.distilled"
    assert manifest["prompt_file"] == "projects/demo/03_prompt_packages/characters/hero/hero_ref_prompt.md"


def test_promote_asset_approved_video_updates_clip_state(tmp_path: Path, monkeypatch) -> None:
    projects_root = tmp_path / "projects"
    monkeypatch.setattr(scaffold_module, "PROJECTS_ROOT", projects_root)
    monkeypatch.setattr(scaffold_module, "ROOT", tmp_path)
    monkeypatch.setattr(scaffold_module, "repo_relative", lambda path: path.relative_to(tmp_path).as_posix())
    monkeypatch.setattr(scaffold_module, "TEMPLATES_ROOT", REAL_TEMPLATES_ROOT)
    monkeypatch.setattr(state_module, "PROJECTS_ROOT", projects_root)
    monkeypatch.setattr(state_module, "ROOT", tmp_path)

    source_video = tmp_path / "candidate_video.mp4"
    source_video.write_bytes(b"filmcreator-test-video")

    destination = scaffold_module.promote_asset(
        "demo",
        str(source_video),
        "approved_video",
        scene_id="SC001",
        clip_id="CL001",
        index=1,
    )

    assert destination == projects_root / "demo" / "05_scenes" / "SC001" / "clips" / "CL001" / "video" / "SC001_CL001_MV01.mp4"
    assert destination.exists()

    clip_state_path = projects_root / "demo" / "05_scenes" / "SC001" / "clips" / "CL001" / "clip_state.json"
    clip_state = json.loads(clip_state_path.read_text(encoding="utf-8"))

    assert clip_state["approved_assets"]["approved_video"] == "projects/demo/05_scenes/SC001/clips/CL001/video/SC001_CL001_MV01.mp4"
    assert clip_state["approved_assets"]["cut_motion_videos"] == [
        "projects/demo/05_scenes/SC001/clips/CL001/video/SC001_CL001_MV01.mp4"
    ]

    review_copy = projects_root / "demo" / "06_reviews" / "selected" / "SC001_CL001_MV01.mp4"
    assert review_copy.exists()
