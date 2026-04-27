from orchestrator.shot_coverage import expand_scene_coverage


def _scene(beats, **extra):
    payload = {
        "scene_id": "CH001_SC001",
        "scene_title": "Test Scene",
        "summary": "A compact adventure scene.",
        "beat_list": beats,
    }
    payload.update(extra)
    return payload


def test_legacy_returns_one_shot_per_beat():
    scene = _scene([
        {"beat_id": "BT001", "summary": "Dorothy enters the road."},
        {"beat_id": "BT002", "summary": "Dorothy asks the Scarecrow for help."},
    ])

    shots = expand_scene_coverage(scene, coverage_density="legacy")

    assert [shot.shot_id for shot in shots] == ["SH001", "SH002"]
    assert [shot.beat_id for shot in shots] == ["BT001", "BT002"]


def test_minor_travel_medium_stays_economical():
    scene = _scene([
        {
            "beat_id": "BT001",
            "summary": "The friends walk down the path toward the next field.",
            "active_subjects": ["Dorothy", "Scarecrow"],
        }
    ])

    shots = expand_scene_coverage(scene, coverage_density="medium")

    assert 1 <= len(shots) <= 2
    assert all(5.0 <= shot.target_seconds <= 12.0 for shot in shots)


def test_major_reveal_medium_expands_more_than_travel():
    scene = _scene([
        {
            "beat_id": "BT001",
            "summary": "A glittering city is revealed beyond the trees and Dorothy realizes the journey has changed.",
            "coverage_priority": "major",
            "active_subjects": ["Dorothy", "companions"],
        }
    ])

    shots = expand_scene_coverage(scene, coverage_density="medium")

    assert len(shots) >= 5
    assert {shot.coverage_role for shot in shots} & {"partial_reveal", "reveal_wide", "scale_proof_wide"}


def test_two_person_dialogue_differs_from_group_dialogue():
    two_person = _scene([
        {
            "beat_id": "BT001",
            "summary": "Dorothy asks Scarecrow for advice and he answers softly.",
            "active_subjects": ["Dorothy", "Scarecrow"],
        }
    ])
    group = _scene([
        {
            "beat_id": "BT001",
            "summary": "Dorothy warns the group and each companion answers.",
            "active_subjects": ["Dorothy", "Scarecrow", "Tin Woodman", "Lion"],
        }
    ])

    two_person_roles = [shot.coverage_role for shot in expand_scene_coverage(two_person, coverage_density="medium")]
    group_roles = [shot.coverage_role for shot in expand_scene_coverage(group, coverage_density="medium")]

    assert "over_the_shoulder_a" in two_person_roles
    assert "listener_group_reaction" in group_roles
    assert "over_the_shoulder_a" not in group_roles


def test_court_dialogue_avoids_ots_heavy_coverage():
    scene = _scene([
        {
            "beat_id": "BT001",
            "summary": "The Queen answers Dorothy before the throne while the court watches.",
            "active_subjects": ["Queen", "Dorothy", "court"],
        }
    ])

    shots = expand_scene_coverage(scene, coverage_density="medium")
    roles = [shot.coverage_role for shot in shots]

    assert "ceremonial_master" in roles
    assert "authority_single" in roles
    assert not any("shoulder" in role for role in roles)


def test_planned_shots_seed_but_do_not_define_final_count():
    scene = _scene(
        [
            {
                "beat_id": "BT001",
                "summary": "Tin Woodman builds a cart and the result surprises Dorothy.",
                "active_subjects": ["Tin Woodman", "Dorothy"],
            }
        ],
        planned_shots=[
            {
                "planned_shot_id": "SH001",
                "beat_id": "BT001",
                "primary_subject_seed": "Tin Woodman",
                "environment_subzone": "workbench",
            }
        ],
    )

    shots = expand_scene_coverage(scene, coverage_density="medium")

    assert len(shots) > 1
    assert shots[0].seed_planned_shot["primary_subject_seed"] == "Tin Woodman"
    assert [shot.shot_id for shot in shots] == [f"SH{index:03d}" for index in range(1, len(shots) + 1)]
