import json
from pathlib import Path

import orchestrator.state as state_module


def test_resolve_continuity_source_prefers_current_continuity_source(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setattr(state_module, "PROJECTS_ROOT", tmp_path)
    monkeypatch.setattr(state_module, "ROOT", tmp_path)

    clip_state_path = tmp_path / "demo" / "05_scenes" / "SC001" / "clips" / "CL001" / "clip_state.json"
    clip_state_path.parent.mkdir(parents=True, exist_ok=True)
    clip_state_path.write_text(
        json.dumps(
            {
                "approved_assets": {
                    "golden_frame": "projects/demo/05_scenes/SC001/clips/CL001/stills/golden_frame/SC001_CL001_GF01.png",
                    "anchor_frames": [],
                    "interval_frames": [],
                },
                "current_continuity_source": "projects/demo/05_scenes/SC001/clips/CL001/stills/golden_frame/SC001_CL001_GF01.png",
            }
        ),
        encoding="utf-8",
    )

    continuity = state_module.resolve_continuity_source("demo", "SC001", "CL001")

    assert continuity.path.endswith("SC001_CL001_GF01.png")
    assert continuity.reason == "clip_state.current_continuity_source"


def test_normalize_clip_state_backfills_approved_video_from_history() -> None:
    payload = {
        "approved_assets": {
            "cut_motion_videos": [
                "projects/demo/05_scenes/SC001/clips/CL001/video/SC001_CL001_MV01.mp4",
            ]
        }
    }

    normalized = state_module.normalize_clip_state(payload)

    assert normalized["approved_assets"]["approved_video"] == (
        "projects/demo/05_scenes/SC001/clips/CL001/video/SC001_CL001_MV01.mp4"
    )
