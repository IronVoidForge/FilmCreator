import orchestrator.batch_runner as batch_runner_module


def test_default_fix_of_ignores_latest_review_video_and_prefers_still(monkeypatch) -> None:
    monkeypatch.setattr(
        batch_runner_module,
        "load_clip_state",
        lambda project_slug, scene_id, clip_id: {
            "approved_assets": {
                "approved_keyframe": "projects/demo/05_scenes/SC001/clips/CL001/stills/keyframes/SC001_CL001_KF01.png",
                "golden_frame": "projects/demo/05_scenes/SC001/clips/CL001/stills/keyframes/SC001_CL001_KF01.png",
                "still_fixes": [],
            },
            "current_continuity_source": "projects/demo/05_scenes/SC001/clips/CL001/stills/keyframes/SC001_CL001_KF01.png",
            "approved_video_last_frame": "projects/demo/05_scenes/SC001/clips/CL001/stills/video_last_frames/SC001_CL001_VL01.png",
            "latest_review_decision": {
                "chosen_primary": "projects/demo/05_scenes/SC001/clips/CL001/video/SC001_CL001_MV03_v003.mp4",
            },
        },
    )

    assert batch_runner_module._default_fix_of("demo", "SC001", "CL001") == (
        "projects/demo/05_scenes/SC001/clips/CL001/stills/keyframes/SC001_CL001_KF01.png"
    )
