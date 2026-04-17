import json
from pathlib import Path

import orchestrator.review_tools as review_tools_module
import orchestrator.scaffold as scaffold_module
import orchestrator.state as state_module
from orchestrator.common import TEMPLATES_ROOT as REAL_TEMPLATES_ROOT


def test_review_candidates_summary_uses_manifest_candidates(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setattr(review_tools_module, "resolve_user_path", lambda value: Path(value))
    monkeypatch.setattr(review_tools_module, "path_to_manifest_value", lambda path: path.as_posix())

    video_one = tmp_path / "video_01.mp4"
    video_one.write_bytes(b"one")
    video_two = tmp_path / "video_02.mp4"
    video_two.write_bytes(b"two")
    ignored = tmp_path / "ignored.mp4"
    ignored.write_bytes(b"ignored")

    manifest_path = tmp_path / "RUN_1000.json"
    manifest_path.write_text(
        json.dumps(
            {
                "batch": {
                    "candidates": [
                        {"output_files": [video_one.as_posix()]},
                        {"output_files": [video_two.as_posix()]},
                    ]
                },
                "output_files": [ignored.as_posix()],
            }
        ),
        encoding="utf-8",
    )

    summary = review_tools_module.review_candidates_summary(manifest_path)

    assert summary["candidate_count"] == 2
    assert summary["candidates"] == [
        {"index": 1, "path": video_one.as_posix(), "name": "video_01.mp4"},
        {"index": 2, "path": video_two.as_posix(), "name": "video_02.mp4"},
    ]


def test_review_and_promote_batch_updates_keyframe_state(tmp_path: Path, monkeypatch) -> None:
    projects_root = tmp_path / "projects"
    monkeypatch.setattr(scaffold_module, "PROJECTS_ROOT", projects_root)
    monkeypatch.setattr(scaffold_module, "ROOT", tmp_path)
    monkeypatch.setattr(scaffold_module, "repo_relative", lambda path: path.relative_to(tmp_path).as_posix())
    monkeypatch.setattr(scaffold_module, "TEMPLATES_ROOT", REAL_TEMPLATES_ROOT)
    monkeypatch.setattr(state_module, "PROJECTS_ROOT", projects_root)
    monkeypatch.setattr(state_module, "ROOT", tmp_path)
    monkeypatch.setattr(state_module, "repo_relative", lambda path: path.relative_to(tmp_path).as_posix())
    monkeypatch.setattr(review_tools_module, "resolve_user_path", lambda value: Path(value) if Path(value).is_absolute() else tmp_path / value)
    monkeypatch.setattr(review_tools_module, "path_to_manifest_value", lambda path: path.relative_to(tmp_path).as_posix())

    clip_dir = scaffold_module.create_clip("demo", "SC001", "CL001")
    candidate_one = clip_dir / "stills" / "keyframes" / "SC001_CL001_KF01_v001.png"
    candidate_one.write_bytes(b"candidate-one")
    candidate_two = clip_dir / "stills" / "keyframes" / "SC001_CL001_KF02_v002.png"
    candidate_two.write_bytes(b"candidate-two")

    manifest_path = clip_dir / "logs" / "RUN_0009.json"
    manifest_path.write_text(
        json.dumps(
            {
                "batch": {
                    "candidates": [
                        {"output_files": [candidate_one.relative_to(tmp_path).as_posix()], "style_profile": "literal_descriptive"},
                        {"output_files": [candidate_two.relative_to(tmp_path).as_posix()], "style_profile": "cinematic_compositional"},
                    ],
                    "review_status": "pending",
                    "chosen_primary": None,
                    "top_two": [],
                }
            }
        ),
        encoding="utf-8",
    )

    result = review_tools_module.review_and_promote_batch(
        project_slug="demo",
        scene_id="SC001",
        clip_id="CL001",
        stage="keyframe",
        manifest_path=manifest_path.relative_to(tmp_path).as_posix(),
        top_two_indexes=[1, 2],
        primary_index=2,
        promotion_target="approved_keyframe",
        promotion_index=1,
    )

    clip_state = result["clip_state"]
    assert clip_state["approved_assets"]["approved_keyframe"] == (
        "projects/demo/05_scenes/SC001/clips/CL001/stills/keyframes/SC001_CL001_KF01.png"
    )
    assert clip_state["latest_review_decision"]["chosen_primary"] == candidate_two.relative_to(tmp_path).as_posix()
    assert result["manifest"]["batch"]["review_status"] == "approve"
