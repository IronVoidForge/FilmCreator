"""Tests for character bible production fallbacks."""
import pytest
from orchestrator.character_bible_fallback import (
    is_unknownish,
    needs_visual_production_fallback,
    fallback_bucket_for_character,
    deterministic_visual_fallback,
)


def test_is_unknownish():
    """Test unknown value detection."""
    assert is_unknownish(None)
    assert is_unknownish("")
    assert is_unknownish("unknown")
    assert is_unknownish("Unknown")
    assert is_unknownish("Unknown.")
    assert is_unknownish("none")
    assert is_unknownish("n/a")
    assert is_unknownish("[]")
    assert is_unknownish("[ ]")
    assert is_unknownish([])
    assert is_unknownish(["", "  "])
    assert is_unknownish(["unknown"])
    assert is_unknownish("['unknown']")
    assert is_unknownish("['[]']")
    assert is_unknownish("not specified")
    assert is_unknownish("unspecified")
    assert not is_unknownish("valid value")
    assert not is_unknownish(["valid"])
    assert not is_unknownish("This is unknown to me but has context")


def test_needs_visual_production_fallback():
    """Test detection of thin visual evidence."""
    # Thin bible with many unknowns
    thin_bible = {
        "identity_baseline": "unknown",
        "physical_build": "unknown",
        "costume_signature": "",
        "stable_visual_summary": "unknown",
    }
    assert needs_visual_production_fallback(thin_bible)
    
    # Strong bible with good evidence (all fields present)
    strong_bible = {
        "identity_baseline": "tall alien warrior",
        "age_presence": "adult warrior",
        "physical_build": "massive muscular frame",
        "origin_or_historical_context": "alien world",
        "movement_language": "fluid warrior movement",
        "costume_signature": "leather harness and metal fittings",
        "stable_visual_summary": "imposing alien warrior",
        "physical_traits": ["green skin", "four arms"],
        "distinguishing_features": ["battle scars"],
        "state_variants": ["armed", "battle-ready"],
    }
    assert not needs_visual_production_fallback(strong_bible)


def test_fallback_bucket_context_only():
    """Test context_only bucket for non-renderable entities."""
    entry = {"entity_kind": "deceased", "status": "canonical"}
    bible_data = {}
    evidence = []
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "context_only"
    assert alias_target is None
    
    # Test evidence-based detection with explicit canon markers
    entry2 = {"entity_kind": "individual", "status": "canonical"}
    bible_data2 = {"identity_baseline": "deceased friend"}
    evidence2 = ["mentioned only", "former companion"]
    bucket2, alias_target2 = fallback_bucket_for_character(entry2, bible_data2, evidence2)
    assert bucket2 == "context_only"
    assert alias_target2 is None


def test_fallback_bucket_alias_redirect_from_metadata():
    """Test alias redirect from explicit metadata."""
    entry = {"canonical_id": "role_label_entity", "entity_kind": "individual", "status": "canonical"}
    bible_data = {"alias_redirect_target": "human_soldier"}
    evidence = ["role label", "soldier"]
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "alias_redirect"
    assert alias_target == "human_soldier"


def test_fallback_bucket_human_soldier():
    """Test human soldier is classified as human."""
    entry = {"canonical_id": "human_soldier", "entity_kind": "individual", "status": "canonical"}
    bible_data = {"identity_baseline": "human soldier"}
    evidence = ["soldier", "officer", "human"]
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "human"
    assert alias_target is None


def test_fallback_bucket_unnamed_mount_quadruped():
    """Test unnamed mount is classified as large_quadruped, not humanoid."""
    entry = {"canonical_id": "unnamed_mount", "entity_kind": "individual", "status": "canonical"}
    bible_data = {"identity_baseline": "eight-legged riding beast"}
    evidence = ["mount", "large beast", "riding beast"]
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "large_quadruped"
    assert alias_target is None


def test_fallback_bucket_alien_humanoid_leader():
    """Test alien humanoid leader is non_human_humanoid."""
    entry = {"canonical_id": "humanoid_leader", "entity_kind": "individual", "status": "canonical"}
    bible_data = {"identity_baseline": "15ft tall alien warrior", "physical_build": "four-armed humanoid frame"}
    evidence = ["alien leader", "15ft tall", "four-armed warrior"]
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "non_human_humanoid"
    assert alias_target is None


def test_fallback_bucket_deceased_reference_context_only():
    """Test deceased reference is context_only."""
    entry = {"canonical_id": "deceased_reference", "entity_kind": "individual", "status": "canonical"}
    bible_data = {"identity_baseline": "deceased friend"}
    evidence = ["dead friend", "riddled with arrows", "deceased prospector"]
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "context_only"
    assert alias_target is None


def test_fallback_bucket_ape_large_creature():
    """Test ape/colossal creature is large_creature."""
    entry = {"canonical_id": "colossal_ape", "entity_kind": "individual", "status": "canonical"}
    bible_data = {"identity_baseline": "colossal ape creature"}
    evidence = ["colossal ape", "massive creature", "beast"]
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "large_creature"
    assert alias_target is None


def test_fallback_bucket_warriors_group():
    """Test warriors group is group_or_horde."""
    entry = {"canonical_id": "warriors", "entity_kind": "group", "status": "canonical"}
    bible_data = {}
    evidence = ["warriors", "group of warriors"]
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "group_or_horde"
    assert alias_target is None


def test_fallback_bucket_watchdog_large_quadruped():
    """Test watchdog is classified as large_quadruped."""
    entry = {"canonical_id": "watchdog", "entity_kind": "individual", "status": "canonical"}
    bible_data = {"identity_baseline": "large watchdog"}
    evidence = ["watchdog", "large hound", "loyal mount"]
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "large_quadruped"
    assert alias_target is None


def test_fallback_bucket_group():
    """Test group_or_horde bucket detection."""
    entry = {"entity_kind": "group", "status": "canonical"}
    bible_data = {}
    evidence = ["warriors", "collective"]
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "group_or_horde"
    assert alias_target is None


def test_deterministic_visual_fallback_context_only():
    """Test fallback generation for context_only entities."""
    entry = {"entity_kind": "deceased", "status": "canonical"}
    bible_data = {}
    evidence = ["dead friend"]
    
    fallback = deterministic_visual_fallback(entry, bible_data, evidence)
    
    assert fallback["status"] == "context_only"
    assert fallback["fallback_bucket"] == "context_only"
    assert "narrative reference only" in fallback["production_identity_descriptor"]
    assert fallback["production_body_descriptor"] == "not applicable"
    assert fallback["production_state_variants"] == []
    assert "should not be visually rendered" in fallback["provisionality_note"].lower()


def test_deterministic_visual_fallback_alias_redirect():
    """Test fallback generation for alias_redirect."""
    entry = {"canonical_id": "role_label_entity", "entity_kind": "individual", "status": "canonical"}
    bible_data = {"alias_redirect_target": "human_soldier"}
    evidence = ["role label", "soldier"]
    
    fallback = deterministic_visual_fallback(entry, bible_data, evidence)
    
    assert fallback["status"] == "alias_redirect"
    assert fallback["fallback_bucket"] == "alias_redirect"
    assert fallback["alias_redirect_target"] == "human_soldier"
    assert "human_soldier" in fallback["production_identity_descriptor"]


def test_deterministic_visual_fallback_human():
    """Test fallback generation for human bucket."""
    entry = {"canonical_id": "human_soldier", "entity_kind": "individual", "status": "canonical"}
    bible_data = {"identity_baseline": "human soldier"}
    evidence = ["human soldier", "cavalry"]
    
    fallback = deterministic_visual_fallback(entry, bible_data, evidence)
    
    assert fallback["status"] == "generated"
    assert fallback["fallback_bucket"] == "human"
    assert "human" in fallback["production_identity_descriptor"]
    assert "human build" in fallback["production_body_descriptor"]
    assert len(fallback["negative_terms"]) > 0
    assert "not strict canon" in fallback["provisionality_note"]


def test_deterministic_visual_fallback_non_human_humanoid():
    """Test fallback generation for non_human_humanoid bucket."""
    entry = {"canonical_id": "humanoid_leader", "entity_kind": "individual", "status": "canonical"}
    bible_data = {"identity_baseline": "alien humanoid leader", "physical_build": "15ft tall four-armed frame"}
    evidence = ["alien leader", "15ft tall", "four-armed"]
    
    fallback = deterministic_visual_fallback(entry, bible_data, evidence)
    
    assert fallback["status"] == "generated"
    assert fallback["fallback_bucket"] == "non_human_humanoid"
    assert "humanoid" in fallback["production_identity_descriptor"]
    assert "humanoid build" in fallback["production_body_descriptor"] or "four-armed" in fallback["production_body_descriptor"]
    assert "humanoid facial" in fallback["production_face_descriptor"]
    assert len(fallback["negative_terms"]) > 0


def test_deterministic_visual_fallback_large_creature():
    """Test fallback generation for large_creature bucket."""
    entry = {"canonical_id": "colossal_ape", "entity_kind": "individual", "status": "canonical"}
    bible_data = {"identity_baseline": "colossal ape creature"}
    evidence = ["colossal ape", "massive creature", "beast"]
    
    fallback = deterministic_visual_fallback(entry, bible_data, evidence)
    
    assert fallback["status"] == "generated"
    assert fallback["fallback_bucket"] == "large_creature"
    assert "creature" in fallback["production_identity_descriptor"]
    assert "massive" in fallback["production_body_descriptor"]
    assert "skull" in fallback["production_face_descriptor"]
    assert "hide" in fallback["production_costume_descriptor"]


def test_deterministic_visual_fallback_preserves_canon():
    """Test that fallback adds to canon instead of replacing it."""
    entry = {"canonical_id": "humanoid_leader", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "identity_baseline": "15ft tall alien leader",
        "physical_build": "massive four-armed frame",
        "physical_traits": ["four arms", "green skin"],
        "costume_signature": "metal armlet and leather harness",
        "distinguishing_features": ["ornate armlet"],
        "movement_language": "unknown",
    }
    evidence = ["alien leader", "15ft tall", "four-armed"]
    
    fallback = deterministic_visual_fallback(entry, bible_data, evidence)
    
    # Canon fields should be preserved in fallback
    assert "15ft tall alien leader" in fallback["production_identity_descriptor"]
    assert "four-armed" in fallback["production_body_descriptor"] or "four arms" in fallback["production_body_descriptor"]
    assert "armlet" in fallback["production_face_descriptor"] or "armlet" in fallback["production_silhouette"]
    assert "metal armlet" in fallback["production_costume_descriptor"]
    # Unknown field should get bucket default
    assert fallback["production_movement_descriptor"] != "unknown"


def test_thin_unknown_heavy_entity_receives_fallback():
    """Test that thin unknown-heavy entity receives visual_production_fallback."""
    thin_bible = {
        "identity_baseline": "unknown",
        "physical_build": "unknown",
        "costume_signature": "unknown",
        "stable_visual_summary": "",
    }
    
    assert needs_visual_production_fallback(thin_bible)
    
    entry = {"canonical_id": "alien_warrior", "entity_kind": "individual", "status": "canonical"}
    evidence = ["alien warrior", "female"]
    
    fallback = deterministic_visual_fallback(entry, thin_bible, evidence)
    
    # With weak evidence, should return unknown_reference
    assert fallback["status"] in ["generated", "insufficient_context"]
    assert fallback["fallback_bucket"] in ["unknown_reference", "non_human_humanoid"]
    assert fallback["production_identity_descriptor"] != "unknown"


def test_strict_canon_fields_preserved():
    """Test that strict canon fields are preserved and not overwritten."""
    strong_bible = {
        "identity_baseline": "human soldier from 1860s",
        "age_presence": "mature adult",
        "physical_build": "lean muscular cavalry build",
        "origin_or_historical_context": "1860s frontier",
        "movement_language": "military bearing",
        "costume_signature": "military uniform remnants",
        "stable_visual_summary": "weathered frontier soldier",
        "physical_traits": ["weathered"],
        "distinguishing_features": ["scar on cheek"],
        "state_variants": ["armed"],
    }
    
    # Should not need fallback
    assert not needs_visual_production_fallback(strong_bible)


def test_humanoid_leader_with_mount_evidence():
    """Test: humanoid_leader with evidence mentioning mount should be non_human_humanoid, not quadruped."""
    entry = {"canonical_id": "humanoid_leader_with_mount", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "identity_baseline": "A massive, four-armed alien warrior leader.",
        "physical_build": "15ft tall; heavy humanoid frame with four arms.",
        "movement_language": "Dismounts from an eight-legged mount to approach others.",
        "physical_traits": "Four arms, Red eyes, Tusks, Olive-green skin",
        "costume_signature": "Unarmed, carrying a metal armlet as peace offering.",
    }
    evidence = ["dismounts from his eight-legged mount", "massive alien warrior", "four-armed leader"]
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "non_human_humanoid", f"Expected non_human_humanoid but got {bucket}"
    assert alias_target is None


def test_humanoid_leader_with_hound_evidence():
    """Test: humanoid leader with hound/mount evidence should be non_human_humanoid, not creature."""
    entry = {"canonical_id": "humanoid_leader", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "identity_baseline": "An alien humanoid of significant physical presence.",
        "physical_build": "Large-framed; out of proportion to human-scale furniture.",
        "role": "Leader of an alien assemblage.",
        "distinguishing_features": "Green skin, large scale",
    }
    evidence = ["leader", "alien humanoid", "hound following behind"]
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "non_human_humanoid", f"Expected non_human_humanoid but got {bucket}"
    assert alias_target is None


def test_human_with_lifeless_shell_evidence():
    """Test: human with lifeless shell/body evidence should be human if canon has active visual evidence."""
    entry = {"canonical_id": "human_soldier", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "identity_baseline": "An earthman undergoing supernatural transformation.",
        "stable_visual_summary": "naked human male, agile movement, leaping through low gravity.",
        "physical_build": "agile human male",
        "costume_signature": "naked post-transformation",
    }
    evidence = ["lifeless physical shell", "earthman", "agile movement"]
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "human", f"Expected human but got {bucket}"
    assert alias_target is None


def test_alias_redirect_from_metadata_only():
    """Test: alias redirect only from explicit metadata, not from ID patterns."""
    entry = {"canonical_id": "role_label_entity", "display_name": "role_label", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "identity_baseline": "An earthman undergoing supernatural transformation.",
        "stable_visual_summary": "naked human male, agile movement.",
        "alias_redirect_target": "human_soldier",
    }
    evidence = ["some evidence without specific mention"]
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "alias_redirect", f"Expected alias_redirect but got {bucket}"
    assert alias_target == "human_soldier"
    
    # Test full fallback generation
    fallback = deterministic_visual_fallback(entry, bible_data, evidence)
    assert fallback["status"] == "alias_redirect"
    assert fallback["fallback_bucket"] == "alias_redirect"
    assert fallback["canonical_target_id"] == "human_soldier"
    assert fallback["alias_redirect_target"] == "human_soldier"
    assert "human_soldier" in fallback["production_identity_descriptor"]


def test_unnamed_mount_classification():
    """Test: unnamed mount should be large_quadruped or large_creature."""
    entry = {"canonical_id": "unnamed_mount", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "stable_visual_summary": "eight-legged riding beasts.",
        "physical_build": "Large quadruped frame with eight legs.",
    }
    evidence = ["mounts", "eight-legged riding beasts", "large mount"]
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket in ["large_quadruped", "large_creature"], f"Expected large_quadruped or large_creature but got {bucket}"
    assert alias_target is None


def test_alien_officer_non_human_humanoid():
    """Test: alien officer should be non_human_humanoid, not human."""
    entry = {"canonical_id": "alien_officer", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "identity_baseline": "Alien officer.",
        "physical_build": "Humanoid frame with alien proportions.",
        "role": "Officer in the alien hierarchy.",
    }
    evidence = ["alien", "officer", "humanoid"]
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "non_human_humanoid", f"Expected non_human_humanoid but got {bucket}"
    assert alias_target is None


def test_multi_legged_creature_not_human():
    """Test: multi-legged creature should be large_creature or large_quadruped, not human."""
    entry = {"canonical_id": "watch_thing", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "identity_baseline": "Multi-legged creature with non-humanoid anatomy.",
        "physical_build": "Non-humanoid frame with multiple legs.",
        "stable_visual_summary": "Multi-legged beast with alien anatomy.",
    }
    evidence = ["multi-legged", "non-humanoid", "beast"]
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket in ["large_creature", "large_quadruped", "small_creature", "small_quadruped"], f"Expected creature/quadruped but got {bucket}"
    assert alias_target is None


if __name__ == "__main__":
    pytest.main([__file__, "-v"])


# Conservative fallback tests

def test_human_riding_animal_remains_human():
    """Test: human riding animal remains human, not quadruped."""
    entry = {"canonical_id": "human_rider", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "identity_baseline": "human warrior",
        "physical_build": "human build",
        "movement_language": "riding a large mount",
    }
    evidence = ["human", "riding mount", "warrior"]
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "human", f"Expected human but got {bucket}"
    assert alias_target is None


def test_human_wearing_alien_clothing_remains_human():
    """Test: human wearing alien/exotic clothing remains human, not alien."""
    entry = {"canonical_id": "alien_cloaked_human", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "identity_baseline": "human person",
        "physical_build": "human build",
        "costume_signature": "wearing exotic alien harness",
    }
    evidence = ["human", "wearing alien harness", "exotic clothing"]
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "human", f"Expected human but got {bucket}"
    assert alias_target is None


def test_humanoid_with_mount_not_quadruped():
    """Test: humanoid associated with mount does not become quadruped."""
    entry = {"canonical_id": "humanoid_leader_with_mount", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "identity_baseline": "alien humanoid leader",
        "physical_build": "humanoid frame",
        "movement_language": "dismounts from mount",
    }
    evidence = ["humanoid", "leader", "dismounts from mount"]
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "non_human_humanoid", f"Expected non_human_humanoid but got {bucket}"
    assert alias_target is None


def test_direct_animal_becomes_quadruped():
    """Test: direct animal/mount entity becomes quadruped or creature."""
    entry = {"canonical_id": "unnamed_mount", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "identity_baseline": "eight-legged riding beast",
        "physical_build": "large quadruped frame",
    }
    evidence = ["mount", "riding beast", "large"]
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket in ["large_quadruped", "large_creature"], f"Expected large_quadruped or large_creature but got {bucket}"
    assert alias_target is None


def test_weak_evidence_becomes_unknown_reference():
    """Test: weak evidence becomes unknown_reference."""
    entry = {"canonical_id": "vague_entity", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "identity_baseline": "unknown",
        "physical_build": "unknown",
    }
    evidence = ["vague mention", "unclear"]
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "unknown_reference", f"Expected unknown_reference but got {bucket}"
    assert alias_target is None


def test_explicit_alias_metadata_produces_redirect():
    """Test: explicit structured alias metadata produces alias_redirect."""
    entry = {"canonical_id": "role_label", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "alias_redirect_target": "human_soldier",
    }
    evidence = ["role label"]
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "alias_redirect", f"Expected alias_redirect but got {bucket}"
    assert alias_target == "human_soldier"


def test_explicit_context_only_metadata():
    """Test: explicit structured context-only metadata produces context_only."""
    entry = {"canonical_id": "deceased_reference", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "renderable": False,
    }
    evidence = ["mentioned only"]
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "context_only", f"Expected context_only but got {bucket}"
    assert alias_target is None


def test_mummified_corpse_context_only():
    """Test: mummified corpse without active visual evidence is context_only."""
    entry = {"canonical_id": "mummified_woman", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "identity_baseline": "a preserved, desiccated female corpse",
        "physical_build": "unknown",
        "movement_language": "unknown",
    }
    evidence = ["mummified", "desiccated", "corpse"]
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "context_only", f"Expected context_only but got {bucket}"
    assert alias_target is None


def test_leader_with_hounds_not_hound():
    """Test: leader followed by hounds is not a hound."""
    entry = {"canonical_id": "humanoid_leader", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "identity_baseline": "alien humanoid leader",
        "physical_build": "humanoid frame",
        "role": "leader followed by hounds",
    }
    evidence = ["leader", "humanoid", "hounds following"]
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "non_human_humanoid", f"Expected non_human_humanoid but got {bucket}"
    assert alias_target is None


def test_warrior_carrying_weapon_not_weapon():
    """Test: warrior carrying weapon is not a weapon."""
    entry = {"canonical_id": "human_soldier", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "identity_baseline": "human warrior",
        "physical_build": "human build",
        "costume_signature": "carrying sword and shield",
    }
    evidence = ["human", "warrior", "carrying weapon"]
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "human", f"Expected human but got {bucket}"
    assert alias_target is None


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
