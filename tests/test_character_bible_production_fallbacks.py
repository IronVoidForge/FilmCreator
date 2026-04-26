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
    # From entity_kind
    entry = {"entity_kind": "deceased", "status": "canonical"}
    bible_data = {}
    evidence = []
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "context_only"
    assert alias_target is None
    
    # From entity_taxonomy renderability
    entry2 = {"entity_kind": "individual", "status": "canonical"}
    bible_data2 = {"entity_taxonomy": {"renderability": "context_only"}}
    evidence2 = []
    bucket2, alias_target2 = fallback_bucket_for_character(entry2, bible_data2, evidence2)
    assert bucket2 == "context_only"
    assert alias_target2 is None


def test_fallback_bucket_alias_redirect_from_metadata():
    """Test alias redirect from explicit alias_resolution metadata."""
    entry = {"canonical_id": "role_label_entity", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "alias_resolution": {
            "status": "approved",
            "canonical_target_id": "human_soldier",
        }
    }
    evidence = []
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "alias_redirect"
    assert alias_target == "human_soldier"


def test_fallback_bucket_human_soldier():
    """Test human soldier is classified as human from taxonomy."""
    entry = {"canonical_id": "human_soldier", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "entity_taxonomy": {
            "primary_type": "human",
            "morphology": "biped",
            "renderability": "renderable",
        }
    }
    evidence = []
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "human"
    assert alias_target is None


def test_fallback_bucket_unnamed_mount_quadruped():
    """Test unnamed mount is classified as large_quadruped from taxonomy."""
    entry = {"canonical_id": "unnamed_mount", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "entity_taxonomy": {
            "primary_type": "animal",
            "morphology": "multi_legged",
            "scale": "large",
            "renderability": "renderable",
        }
    }
    evidence = []
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "large_quadruped"
    assert alias_target is None


def test_fallback_bucket_alien_humanoid_leader():
    """Test alien humanoid leader is non_human_humanoid from taxonomy."""
    entry = {"canonical_id": "humanoid_leader", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "entity_taxonomy": {
            "primary_type": "humanoid_nonhuman",
            "morphology": "biped",
            "scale": "large",
            "renderability": "renderable",
        }
    }
    evidence = []
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "non_human_humanoid"
    assert alias_target is None


def test_fallback_bucket_deceased_reference_context_only():
    """Test deceased reference is context_only from taxonomy."""
    entry = {"canonical_id": "deceased_reference", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "entity_taxonomy": {
            "renderability": "context_only",
        }
    }
    evidence = []
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "context_only"
    assert alias_target is None


def test_fallback_bucket_ape_large_creature():
    """Test ape/colossal creature is large_creature from taxonomy."""
    entry = {"canonical_id": "colossal_ape", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "entity_taxonomy": {
            "primary_type": "creature",
            "scale": "giant",
            "renderability": "renderable",
        }
    }
    evidence = []
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "large_creature"
    assert alias_target is None


def test_fallback_bucket_warriors_group():
    """Test warriors group is group_or_horde from taxonomy."""
    entry = {"canonical_id": "warriors", "entity_kind": "group", "status": "canonical"}
    bible_data = {
        "entity_taxonomy": {
            "primary_type": "group",
            "renderability": "renderable",
        }
    }
    evidence = []
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "group_or_horde"
    assert alias_target is None


def test_fallback_bucket_watchdog_large_quadruped():
    """Test watchdog is classified as large_quadruped from taxonomy."""
    entry = {"canonical_id": "watchdog", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "entity_taxonomy": {
            "primary_type": "animal",
            "morphology": "quadruped",
            "scale": "large",
            "renderability": "renderable",
        }
    }
    evidence = []
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "large_quadruped"
    assert alias_target is None


def test_fallback_bucket_group():
    """Test group_or_horde bucket detection from taxonomy."""
    entry = {"entity_kind": "group", "status": "canonical"}
    bible_data = {
        "entity_taxonomy": {
            "primary_type": "group",
        }
    }
    evidence = []
    
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
    bible_data = {
        "alias_resolution": {
            "status": "approved",
            "canonical_target_id": "human_soldier",
        }
    }
    evidence = []
    
    fallback = deterministic_visual_fallback(entry, bible_data, evidence)
    
    assert fallback["status"] == "alias_redirect"
    assert fallback["fallback_bucket"] == "alias_redirect"
    assert fallback["alias_redirect_target"] == "human_soldier"
    assert "human_soldier" in fallback["production_identity_descriptor"]


def test_deterministic_visual_fallback_human():
    """Test fallback generation for human bucket."""
    entry = {"canonical_id": "human_soldier", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "identity_baseline": "human soldier",
        "entity_taxonomy": {
            "primary_type": "human",
            "morphology": "biped",
        }
    }
    evidence = []
    
    fallback = deterministic_visual_fallback(entry, bible_data, evidence)
    
    assert fallback["status"] == "generated"
    assert fallback["fallback_bucket"] == "human"
    assert "human" in fallback["production_identity_descriptor"]
    assert "human build" in fallback["production_body_descriptor"]
    assert len(fallback["negative_terms"]) > 0
    # Should not include "human proportions" in negative_terms since taxonomy says human
    assert not any("human" in term.lower() for term in fallback["negative_terms"])
    assert "not strict canon" in fallback["provisionality_note"]


def test_deterministic_visual_fallback_non_human_humanoid():
    """Test fallback generation for non_human_humanoid bucket."""
    entry = {"canonical_id": "humanoid_leader", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "identity_baseline": "alien humanoid leader",
        "physical_build": "15ft tall four-armed frame",
        "entity_taxonomy": {
            "primary_type": "humanoid_nonhuman",
            "morphology": "biped",
        }
    }
    evidence = []
    
    fallback = deterministic_visual_fallback(entry, bible_data, evidence)
    
    assert fallback["status"] == "generated"
    assert fallback["fallback_bucket"] == "non_human_humanoid"
    assert "humanoid" in fallback["production_identity_descriptor"] or "alien" in fallback["production_identity_descriptor"]
    assert "four-armed" in fallback["production_body_descriptor"]
    assert len(fallback["negative_terms"]) > 0
    # Should not include "humanoid" in negative_terms since taxonomy says humanoid_nonhuman
    assert not any("humanoid" in term.lower() for term in fallback["negative_terms"])


def test_deterministic_visual_fallback_large_creature():
    """Test fallback generation for large_creature bucket."""
    entry = {"canonical_id": "colossal_ape", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "identity_baseline": "colossal ape creature",
        "entity_taxonomy": {
            "primary_type": "creature",
            "scale": "giant",
        }
    }
    evidence = []
    
    fallback = deterministic_visual_fallback(entry, bible_data, evidence)
    
    assert fallback["status"] == "generated"
    assert fallback["fallback_bucket"] == "large_creature"
    assert "creature" in fallback["production_identity_descriptor"] or "ape" in fallback["production_identity_descriptor"]
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
        "entity_taxonomy": {
            "primary_type": "humanoid_nonhuman",
            "morphology": "biped",
        }
    }
    evidence = []
    
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
    """Test: humanoid_leader with mount in associated_evidence should be non_human_humanoid from taxonomy."""
    entry = {"canonical_id": "humanoid_leader_with_mount", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "identity_baseline": "A massive, four-armed alien warrior leader.",
        "physical_build": "15ft tall; heavy humanoid frame with four arms.",
        "movement_language": "Dismounts from an eight-legged mount to approach others.",
        "entity_taxonomy": {
            "primary_type": "humanoid_nonhuman",
            "morphology": "biped",
            "scale": "large",
        }
    }
    evidence = []
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "non_human_humanoid", f"Expected non_human_humanoid but got {bucket}"
    assert alias_target is None


def test_humanoid_leader_with_hound_evidence():
    """Test: humanoid leader with hound evidence should be non_human_humanoid from taxonomy."""
    entry = {"canonical_id": "humanoid_leader", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "identity_baseline": "An alien humanoid of significant physical presence.",
        "physical_build": "Large-framed; out of proportion to human-scale furniture.",
        "entity_taxonomy": {
            "primary_type": "humanoid_nonhuman",
            "morphology": "biped",
        }
    }
    evidence = []
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "non_human_humanoid", f"Expected non_human_humanoid but got {bucket}"
    assert alias_target is None


def test_human_with_lifeless_shell_evidence():
    """Test: human with lifeless shell evidence should be human from taxonomy."""
    entry = {"canonical_id": "human_soldier", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "identity_baseline": "An earthman undergoing supernatural transformation.",
        "stable_visual_summary": "naked human male, agile movement, leaping through low gravity.",
        "entity_taxonomy": {
            "primary_type": "human",
            "morphology": "biped",
        }
    }
    evidence = []
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "human", f"Expected human but got {bucket}"
    assert alias_target is None


def test_alias_redirect_from_metadata_only():
    """Test: alias redirect only from explicit alias_resolution metadata."""
    entry = {"canonical_id": "role_label_entity", "display_name": "role_label", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "identity_baseline": "An earthman undergoing supernatural transformation.",
        "stable_visual_summary": "naked human male, agile movement.",
        "alias_resolution": {
            "status": "approved",
            "canonical_target_id": "human_soldier",
        }
    }
    evidence = []
    
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
    """Test: unnamed mount should be large_quadruped from taxonomy."""
    entry = {"canonical_id": "unnamed_mount", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "stable_visual_summary": "eight-legged riding beasts.",
        "physical_build": "Large quadruped frame with eight legs.",
        "entity_taxonomy": {
            "primary_type": "animal",
            "morphology": "multi_legged",
            "scale": "large",
        }
    }
    evidence = []
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "large_quadruped", f"Expected large_quadruped but got {bucket}"
    assert alias_target is None


def test_alien_officer_non_human_humanoid():
    """Test: alien officer should be non_human_humanoid from taxonomy."""
    entry = {"canonical_id": "alien_officer", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "identity_baseline": "Alien officer.",
        "physical_build": "Humanoid frame with alien proportions.",
        "entity_taxonomy": {
            "primary_type": "humanoid_nonhuman",
            "morphology": "biped",
        }
    }
    evidence = []
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "non_human_humanoid", f"Expected non_human_humanoid but got {bucket}"
    assert alias_target is None


def test_multi_legged_creature_not_human():
    """Test: multi-legged creature should be large_quadruped from taxonomy."""
    entry = {"canonical_id": "watch_thing", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "identity_baseline": "Multi-legged creature with non-humanoid anatomy.",
        "physical_build": "Non-humanoid frame with multiple legs.",
        "entity_taxonomy": {
            "primary_type": "creature",
            "morphology": "multi_legged",
            "scale": "large",
        }
    }
    evidence = []
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "large_quadruped", f"Expected large_quadruped but got {bucket}"
    assert alias_target is None


if __name__ == "__main__":
    pytest.main([__file__, "-v"])


# Conservative fallback tests

def test_human_riding_animal_remains_human():
    """Test: human riding animal remains human from taxonomy."""
    entry = {"canonical_id": "human_rider", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "identity_baseline": "human warrior",
        "physical_build": "human build",
        "entity_taxonomy": {
            "primary_type": "human",
            "morphology": "biped",
        }
    }
    evidence = []
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "human", f"Expected human but got {bucket}"
    assert alias_target is None


def test_human_wearing_alien_clothing_remains_human():
    """Test: human wearing alien/exotic clothing remains human from taxonomy."""
    entry = {"canonical_id": "alien_cloaked_human", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "identity_baseline": "human person",
        "physical_build": "human build",
        "costume_signature": "wearing exotic alien harness",
        "entity_taxonomy": {
            "primary_type": "human",
            "morphology": "biped",
        }
    }
    evidence = []
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "human", f"Expected human but got {bucket}"
    assert alias_target is None


def test_humanoid_with_mount_not_quadruped():
    """Test: humanoid associated with mount does not become quadruped from taxonomy."""
    entry = {"canonical_id": "humanoid_leader_with_mount", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "identity_baseline": "alien humanoid leader",
        "physical_build": "humanoid frame",
        "movement_language": "dismounts from mount",
        "entity_taxonomy": {
            "primary_type": "humanoid_nonhuman",
            "morphology": "biped",
        }
    }
    evidence = []
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "non_human_humanoid", f"Expected non_human_humanoid but got {bucket}"
    assert alias_target is None


def test_direct_animal_becomes_quadruped():
    """Test: direct animal/mount entity becomes quadruped from taxonomy."""
    entry = {"canonical_id": "unnamed_mount", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "identity_baseline": "eight-legged riding beast",
        "physical_build": "large quadruped frame",
        "entity_taxonomy": {
            "primary_type": "animal",
            "morphology": "multi_legged",
            "scale": "large",
        }
    }
    evidence = []
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "large_quadruped", f"Expected large_quadruped but got {bucket}"
    assert alias_target is None


def test_weak_evidence_becomes_unknown_reference():
    """Test: weak evidence (missing taxonomy) becomes unknown_reference."""
    entry = {"canonical_id": "vague_entity", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "identity_baseline": "unknown",
        "physical_build": "unknown",
        # No entity_taxonomy provided
    }
    evidence = []
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "unknown_reference", f"Expected unknown_reference but got {bucket}"
    assert alias_target is None


def test_explicit_alias_metadata_produces_redirect():
    """Test: explicit structured alias_resolution metadata produces alias_redirect."""
    entry = {"canonical_id": "role_label", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "alias_resolution": {
            "status": "approved",
            "canonical_target_id": "human_soldier",
        }
    }
    evidence = []
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "alias_redirect", f"Expected alias_redirect but got {bucket}"
    assert alias_target == "human_soldier"


def test_explicit_context_only_metadata():
    """Test: explicit structured context-only metadata produces context_only."""
    entry = {"canonical_id": "deceased_reference", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "entity_taxonomy": {
            "renderability": "context_only",
        }
    }
    evidence = []
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "context_only", f"Expected context_only but got {bucket}"
    assert alias_target is None


def test_mummified_corpse_context_only():
    """Test: mummified corpse is context_only from taxonomy."""
    entry = {"canonical_id": "mummified_woman", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "identity_baseline": "a preserved, desiccated female corpse",
        "physical_build": "unknown",
        "movement_language": "unknown",
        "entity_taxonomy": {
            "renderability": "context_only",
        }
    }
    evidence = []
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "context_only", f"Expected context_only but got {bucket}"
    assert alias_target is None


def test_leader_with_hounds_not_hound():
    """Test: leader followed by hounds is not a hound from taxonomy."""
    entry = {"canonical_id": "humanoid_leader", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "identity_baseline": "alien humanoid leader",
        "physical_build": "humanoid frame",
        "role": "leader followed by hounds",
        "entity_taxonomy": {
            "primary_type": "humanoid_nonhuman",
            "morphology": "biped",
        }
    }
    evidence = []
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "non_human_humanoid", f"Expected non_human_humanoid but got {bucket}"
    assert alias_target is None


def test_warrior_carrying_weapon_not_weapon():
    """Test: warrior carrying weapon is not a weapon from taxonomy."""
    entry = {"canonical_id": "human_soldier", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "identity_baseline": "human warrior",
        "physical_build": "human build",
        "costume_signature": "carrying sword and shield",
        "entity_taxonomy": {
            "primary_type": "human",
            "morphology": "biped",
        }
    }
    evidence = []
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "human", f"Expected human but got {bucket}"
    assert alias_target is None


if __name__ == "__main__":
    pytest.main([__file__, "-v"])


# New taxonomy-based tests

def test_taxonomy_human_to_bucket_human():
    """Test: taxonomy primary_type human -> bucket human."""
    entry = {"canonical_id": "test_human", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "entity_taxonomy": {
            "primary_type": "human",
            "morphology": "biped",
            "renderability": "renderable",
        }
    }
    evidence = []
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "human"
    assert alias_target is None


def test_taxonomy_humanoid_nonhuman_to_bucket():
    """Test: taxonomy primary_type humanoid_nonhuman -> bucket non_human_humanoid."""
    entry = {"canonical_id": "test_alien", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "entity_taxonomy": {
            "primary_type": "humanoid_nonhuman",
            "morphology": "biped",
            "renderability": "renderable",
        }
    }
    evidence = []
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "non_human_humanoid"
    assert alias_target is None


def test_taxonomy_group_to_bucket():
    """Test: taxonomy primary_type group -> bucket group_or_horde."""
    entry = {"canonical_id": "test_group", "entity_kind": "group", "status": "canonical"}
    bible_data = {
        "entity_taxonomy": {
            "primary_type": "group",
            "renderability": "renderable",
        }
    }
    evidence = []
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "group_or_horde"
    assert alias_target is None


def test_taxonomy_quadruped_unknown_scale():
    """Test: taxonomy quadruped with unknown scale -> large_quadruped (default)."""
    entry = {"canonical_id": "test_beast", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "entity_taxonomy": {
            "primary_type": "animal",
            "morphology": "quadruped",
            "scale": "unknown",
            "renderability": "renderable",
        }
    }
    evidence = []
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "large_quadruped"
    assert alias_target is None


def test_taxonomy_small_quadruped():
    """Test: taxonomy small quadruped -> small_quadruped."""
    entry = {"canonical_id": "test_small_animal", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "entity_taxonomy": {
            "primary_type": "animal",
            "morphology": "quadruped",
            "scale": "small",
            "renderability": "renderable",
        }
    }
    evidence = []
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "small_quadruped"
    assert alias_target is None


def test_alias_resolution_approved():
    """Test: alias_resolution status approved -> alias_redirect with target."""
    entry = {"canonical_id": "test_alias", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "alias_resolution": {
            "status": "approved",
            "canonical_target_id": "canonical_character",
        }
    }
    evidence = []
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "alias_redirect"
    assert alias_target == "canonical_character"


def test_alias_candidate_not_redirect():
    """Test: alias_resolution status candidate (not approved) -> not alias_redirect."""
    entry = {"canonical_id": "test_candidate", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "alias_resolution": {
            "status": "candidate",
            "canonical_target_id": "some_character",
        },
        "entity_taxonomy": {
            "primary_type": "human",
        }
    }
    evidence = []
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket != "alias_redirect"
    assert alias_target is None


def test_context_only_taxonomy():
    """Test: taxonomy renderability context_only -> context_only bucket."""
    entry = {"canonical_id": "test_context", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "entity_taxonomy": {
            "renderability": "context_only",
        }
    }
    evidence = []
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "context_only"
    assert alias_target is None


def test_associated_mount_cannot_override_taxonomy():
    """Test: associated mount evidence cannot override taxonomy classification."""
    entry = {"canonical_id": "test_humanoid", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "movement_language": "riding a large mount",
        "entity_taxonomy": {
            "primary_type": "humanoid_nonhuman",
            "morphology": "biped",
        }
    }
    evidence = ["riding mount", "dismounts from beast"]
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "non_human_humanoid"
    assert alias_target is None


def test_missing_taxonomy_weak_evidence():
    """Test: missing taxonomy + weak evidence -> unknown_reference."""
    entry = {"canonical_id": "test_unknown", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "identity_baseline": "unknown",
        # No entity_taxonomy
    }
    evidence = ["vague mention"]
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "unknown_reference"
    assert alias_target is None


def test_human_taxonomy_no_contradictory_negatives():
    """Test: human taxonomy must not receive negative_terms contradicting humanity."""
    entry = {"canonical_id": "test_human", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "identity_baseline": "human soldier",
        "entity_taxonomy": {
            "primary_type": "human",
            "morphology": "biped",
        }
    }
    evidence = []
    
    fallback = deterministic_visual_fallback(entry, bible_data, evidence)
    
    # Should not include "human proportions" or "human anatomy" in negative_terms
    for term in fallback["negative_terms"]:
        assert "human" not in term.lower(), f"Found contradictory negative term: {term}"


def test_humanoid_taxonomy_no_quadruped_from_associated():
    """Test: humanoid taxonomy must not become quadruped because of associated entity evidence."""
    entry = {"canonical_id": "test_humanoid", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "identity_baseline": "alien warrior",
        "movement_language": "riding a beast",
        "entity_taxonomy": {
            "primary_type": "humanoid_nonhuman",
            "morphology": "biped",
        }
    }
    evidence = ["riding beast", "mounted on creature"]
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "non_human_humanoid"
    assert bucket != "large_quadruped"
    assert bucket != "small_quadruped"
    assert alias_target is None
