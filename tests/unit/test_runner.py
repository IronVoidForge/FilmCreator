from pathlib import Path

import orchestrator.runner as runner_module
from orchestrator.prompt_package import PromptPackage


def test_resolve_stage_refs_for_still_fix_skips_video_primary_and_uses_keyframe(tmp_path: Path, monkeypatch) -> None:
    keyframe = tmp_path / "projects" / "demo" / "05_scenes" / "SC001" / "clips" / "CL001" / "stills" / "keyframes" / "SC001_CL001_KF01.png"
    keyframe.parent.mkdir(parents=True, exist_ok=True)
    keyframe.write_bytes(b"png")

    video_last_frame = (
        tmp_path
        / "projects"
        / "demo"
        / "05_scenes"
        / "SC001"
        / "clips"
        / "CL001"
        / "stills"
        / "video_last_frames"
        / "SC001_CL001_VL01.png"
    )
    video_last_frame.parent.mkdir(parents=True, exist_ok=True)
    video_last_frame.write_bytes(b"png")

    char_ref = tmp_path / "projects" / "demo" / "05_scenes" / "SC001" / "clips" / "CL001" / "inputs" / "smoke_char.png"
    char_ref.parent.mkdir(parents=True, exist_ok=True)
    char_ref.write_bytes(b"png")

    monkeypatch.setattr(
        runner_module,
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
    monkeypatch.setattr(
        runner_module,
        "resolve_user_path",
        lambda value: Path(value) if Path(value).is_absolute() else tmp_path / value,
    )

    workflow = {
        "id": "still.scene_insert.two_ref.klein.distilled",
        "required_image_slots": [{"slot": "image_1"}, {"slot": "image_2"}],
        "optional_image_slots": [],
    }
    prompt_package = PromptPackage(
        path=Path("prompt.md"),
        title="Fix Prompt",
        prompt_id="fix_prompt",
        purpose="Fix prompt",
        workflow_type="still.scene_insert.two_ref.klein.distilled",
        positive_prompt="Fix the frame",
        negative_prompt="",
        inputs_markdown="- fix_of: projects/demo/05_scenes/SC001/clips/CL001/video/SC001_CL001_MV03_v003.mp4",
        continuity_notes_markdown="- Keep composition",
        sources_markdown="- projects/demo/02_story_analysis/clip_plans/SC001/CL001.md",
    )

    resolved, continuity_source, warnings = runner_module._resolve_stage_refs(
        workflow=workflow,
        stage="still_fix",
        prompt_package=prompt_package,
        raw_ref_map={"image_2": "projects/demo/05_scenes/SC001/clips/CL001/inputs/smoke_char.png"},
        project_slug="demo",
        scene_id="SC001",
        clip_id="CL001",
    )

    assert resolved["image_1"] == "projects/demo/05_scenes/SC001/clips/CL001/stills/keyframes/SC001_CL001_KF01.png"
    assert continuity_source is None
    assert any("latest approved still-compatible image" in warning for warning in warnings)
