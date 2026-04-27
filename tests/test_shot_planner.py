from orchestrator.shot_planner import _build_shot_blueprints, _shot_plan_payload_quality_issues


def _shot_payload(shot_id: str) -> dict:
    return {
        "shot_id": shot_id,
        "shot_order": int(shot_id.replace("SH", "")),
        "shot_moment_summary": "Dorothy steps into the road.",
        "primary_subject": "dorothy",
        "start_state": "Dorothy pauses at the road edge.",
        "end_state": "Dorothy begins walking.",
        "action_during_shot": "Dorothy commits to the path.",
        "action_continues_from": "She has just left the previous location.",
        "action_hands_off_to": "Her next step carries into the following shot.",
        "shot_size": "medium",
        "camera_angle": "eye_level",
        "lens_family": "normal",
        "camera_motion": "locked_off",
        "focus_strategy": "deep_focus",
        "lighting_style": "diffuse_ambient",
        "subject_visibility": "on_screen",
        "narration_mode": "none",
        "visible_primary_subject_id": "dorothy",
        "primary_subject_frame_position": "center frame on the road",
        "primary_subject_scale_relation": "human-scale against the roadway",
        "primary_subject_pose_description": "upright walking posture",
        "required_environment_anchor_1": "yellow brick road",
        "camera_package_description": "medium eye-level normal lens locked-off frame",
        "camera_description": "Readable eye-level view.",
        "composition": "Dorothy is framed against the road direction.",
        "environment_subzone": "road edge",
        "continuity_from_previous_shot": "Dorothy has arrived at the road.",
        "continuity_to_next_shot": "Dorothy moves down the road.",
        "pose_anchor_frame": "Dorothy standing at the road edge.",
        "pose_end_frame": "Dorothy stepping forward.",
        "prompt_seed": "Dorothy steps onto the yellow brick road in a readable medium frame.",
        "beat_ids": ["BT001"],
        "subject_blocking": ["Dorothy stands on the road edge."],
        "camera_relative_positions": ["Camera faces Dorothy from road level."],
    }


def test_scene_shot_payload_quality_accepts_complete_scene_packet():
    blueprints = [{"shot_id": "SH001"}, {"shot_id": "SH002"}]
    payload = [_shot_payload("SH001"), _shot_payload("SH002")]

    assert _shot_plan_payload_quality_issues(payload, blueprints) == []


def test_scene_shot_payload_quality_flags_missing_ids_and_thin_fields():
    blueprints = [{"shot_id": "SH001"}, {"shot_id": "SH002"}]
    payload = [_shot_payload("SH001")]
    payload[0]["prompt_seed"] = "thin"
    payload[0]["camera_description"] = ""

    issues = _shot_plan_payload_quality_issues(payload, blueprints)

    assert any("Expected 2 shot records" in issue for issue in issues)
    assert any("Missing shot ids: SH002" in issue for issue in issues)
    assert any("SH001 missing or thin fields" in issue for issue in issues)


def test_scene_shot_payload_quality_rejects_extra_id_and_blank_core_fields():
    blueprints = [{"shot_id": "SH001", "coverage_role": "master_two_shot", "coverage_density": "medium"}]
    payload = [_shot_payload("SH001"), _shot_payload("SH002")]
    payload[0]["primary_subject"] = ""
    payload[0]["start_state"] = ""
    payload[0]["coverage_role"] = ""

    issues = _shot_plan_payload_quality_issues(payload, blueprints)

    assert any("Unexpected shot ids: SH002" in issue for issue in issues)
    assert any("SH001 missing or thin fields" in issue and "primary_subject" in issue for issue in issues)
    assert any("coverage_role" in issue for issue in issues)


def test_build_shot_blueprints_medium_expands_coverage_metadata(tmp_path):
    scene_contract = {
        "scene_id": "CH001_SC001",
        "chapter_id": "CH001",
        "scene_title": "The Warning",
        "summary": "Dorothy warns the companions and they decide what to do.",
        "beat_list": [
            {
                "beat_id": "BT001",
                "summary": "Dorothy warns the group and Scarecrow answers.",
                "active_subjects": ["Dorothy", "Scarecrow", "Tin Woodman"],
                "passive_subjects": ["Lion"],
                "action_start": "The group gathers.",
                "action_end": "The group has heard the warning.",
                "environment_subzone": "road bend",
            }
        ],
    }

    blueprints = _build_shot_blueprints(scene_contract, tmp_path, coverage_density="medium")

    assert len(blueprints) > 1
    assert blueprints[0]["coverage_density"] == "medium"
    assert blueprints[0]["coverage_profile"] == "classic_adventure"
    assert blueprints[0]["coverage_role"]
    assert blueprints[0]["beat_type"] == "dialogue_group"
    assert isinstance(blueprints[0]["coverage_classification"], dict)
    assert all(blueprint["primary_subject"] for blueprint in blueprints)
    assert all(blueprint["start_state"] and blueprint["end_state"] and blueprint["action_during_shot"] for blueprint in blueprints)


def test_build_shot_blueprints_legacy_matches_one_shot_per_beat_shape(tmp_path):
    scene_contract = {
        "scene_id": "CH001_SC001",
        "chapter_id": "CH001",
        "scene_title": "Two Beats",
        "summary": "Two compact beats.",
        "beat_list": [
            {"beat_id": "BT001", "summary": "Dorothy enters the road."},
            {"beat_id": "BT002", "summary": "Dorothy asks Scarecrow for help."},
        ],
    }

    blueprints = _build_shot_blueprints(scene_contract, tmp_path, coverage_density="legacy")

    assert [blueprint["shot_id"] for blueprint in blueprints] == ["SH001", "SH002"]
    assert [blueprint["beat_ids"] for blueprint in blueprints] == [["BT001"], ["BT002"]]
