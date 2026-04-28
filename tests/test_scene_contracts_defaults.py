from orchestrator.scene_contracts import _default_primary_subject_seed


def test_default_primary_subject_seed_is_generic_for_group_scene():
    summary = "A crowd of guards and children gathers around the central event while the group reacts."
    assert _default_primary_subject_seed(summary) == "the key group in the scene"


def test_default_primary_subject_seed_is_generic_for_creature_scene():
    summary = "A strange creature emerges from the trees and the beast blocks the path."
    assert _default_primary_subject_seed(summary) == "the primary creature in the scene"


def test_default_primary_subject_seed_preserves_narrator_when_explicit():
    summary = "The narrator describes the hallway in first-person voiceover."
    assert _default_primary_subject_seed(summary) == "The Narrator"
