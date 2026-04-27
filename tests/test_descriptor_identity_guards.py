from orchestrator.descriptor_enrichment import (
    _character_identity_review_flags,
    _rewrite_character_generated_fields,
)


def test_identity_guards_rewrite_feminine_child_defaults() -> None:
    base_fields = {
        "entity_kind": "individual",
        "role": "traveler",
        "aliases": ["farm girl"],
        "identity_baseline": "A young girl in simple travel clothes.",
        "age_presence": "visibly child-sized",
    }
    evidence_summary = [
        "She clutches the basket and looks up at the adults around her.",
        "The little girl runs ahead before turning back to her companions.",
    ]
    rewritten, flags = _rewrite_character_generated_fields(
        {
            "sex": "male",
            "age_range": "adult",
            "facial_hair": "clean-shaven or light stubble",
        },
        base_fields=base_fields,
        evidence_summary=evidence_summary,
        canonical_id="chapter_traveler",
        display_name="Chapter Traveler",
    )

    assert rewritten["sex"] == "female"
    assert rewritten["age_range"] == "child"
    assert rewritten["facial_hair"] == "none"
    assert "identity_cue_conflict_sex" in flags
    assert "identity_cue_conflict_age" in flags
    assert "identity_cue_conflict_grooming" in flags


def test_identity_guards_rewrite_collective_group_defaults() -> None:
    base_fields = {
        "entity_kind": "group",
        "role": "flying troop",
        "identity_baseline": "A troop of winged monkey-like creatures.",
    }
    evidence_summary = [
        "They sweep overhead as a coordinated group.",
        "Their formation closes around the travelers.",
    ]
    rewritten, flags = _rewrite_character_generated_fields(
        {
            "sex": "male",
            "facial_hair": "clean-shaven or light stubble",
        },
        base_fields=base_fields,
        evidence_summary=evidence_summary,
        canonical_id="winged_troop",
        display_name="Winged Troop",
    )

    assert rewritten["sex"] == "mixed or unspecified group"
    assert rewritten["facial_hair"] != "clean-shaven or light stubble"
    assert "identity_cue_conflict_group_vs_individual" in flags


def test_identity_guards_rewrite_creature_human_bundle() -> None:
    base_fields = {
        "entity_kind": "individual",
        "role": "creature",
        "identity_baseline": "A large rabbit-like creature with white fur and a quick muzzle.",
    }
    evidence_summary = [
        "The creature twitches its whiskers and paws at the ground.",
    ]
    rewritten, flags = _rewrite_character_generated_fields(
        {
            "skin_tone": "weathered light-to-medium skin",
            "hair_style": "short practical frontier cut",
            "face_shape": "angular face",
            "facial_hair": "clean-shaven or light stubble",
        },
        base_fields=base_fields,
        evidence_summary=evidence_summary,
        canonical_id="white_rabbit_like_creature",
        display_name="White Rabbit-Like Creature",
    )

    assert rewritten["skin_tone"] != "weathered light-to-medium skin"
    assert rewritten["hair_style"] != "short practical frontier cut"
    assert rewritten["face_shape"] != "angular face"
    assert rewritten["facial_hair"] != "clean-shaven or light stubble"
    assert any(flag.startswith("identity_cue_conflict_species") for flag in flags)


def test_identity_review_flags_surface_remaining_conflicts() -> None:
    base_fields = {
        "entity_kind": "individual",
        "role": "young heroine",
        "aliases": ["little girl"],
        "identity_baseline": "A young girl in a plain dress.",
        "age_presence": "child",
    }
    evidence_summary = [
        "She stands apart from the adults and looks frightened.",
    ]
    flags = _character_identity_review_flags(
        {
            "sex": "male",
            "age_range": "adult",
            "facial_hair": "light stubble",
            "skin_tone": "fair skin",
            "hair_color": "brown",
            "hair_style": "braided hair",
            "face_shape": "round youthful face",
            "costume_materials": "plain cotton dress fabric",
            "identity_baseline": "A young girl in a plain dress.",
        },
        base_fields=base_fields,
        evidence_summary=evidence_summary,
        canonical_id="young_heroine",
        display_name="Young Heroine",
    )

    assert "identity_cue_conflict_sex" in flags
    assert "identity_cue_conflict_age" in flags
    assert "identity_cue_conflict_grooming" in flags
