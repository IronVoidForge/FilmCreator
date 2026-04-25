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
        "identity_baseline": "tall Martian warrior",
        "age_presence": "adult warrior",
        "physical_build": "massive muscular frame",
        "origin_or_historical_context": "Barsoom",
        "movement_language": "fluid warrior movement",
        "costume_signature": "leather harness and metal fittings",
        "stable_visual_summary": "imposing green Martian warrior",
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
    
    # Test evidence-based detection
    entry2 = {"entity_kind": "individual", "status": "canonical"}
    evidence2 = ["dead friend", "mentioned only", "former companion"]
    bucket2, alias_target2 = fallback_bucket_for_character(entry2, bible_data, evidence2)
    assert bucket2 == "context_only"
    assert alias_target2 is None


def test_fallback_bucket_protagonist_redirect():
    """Test protagonist redirects to john_carter."""
    entry = {"canonical_id": "protagonist", "entity_kind": "individual", "status": "canonical"}
    bible_data = {}
    evidence = ["protagonist", "John Carter", "Virginia cavalry officer"]
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "alias_redirect"
    assert alias_target == "john_carter"


def test_fallback_bucket_john_carter_human():
    """Test john_carter is classified as human."""
    entry = {"canonical_id": "john_carter", "entity_kind": "individual", "status": "canonical"}
    bible_data = {}
    evidence = ["John Carter", "Virginia", "Confederate officer", "human"]
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "human"
    assert alias_target is None


def test_fallback_bucket_martian_mounts_quadruped():
    """Test martian_mounts is classified as large_quadruped, not humanoid."""
    entry = {"canonical_id": "martian_mounts", "entity_kind": "individual", "status": "canonical"}
    bible_data = {}
    evidence = ["Martian mounts", "thoat", "large beast", "mount"]
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "large_quadruped"
    assert alias_target is None


def test_fallback_bucket_green_martian_non_human_humanoid():
    """Test green Martian chieftain is non_human_humanoid."""
    entry = {"canonical_id": "tars_tarkas", "entity_kind": "individual", "status": "canonical"}
    bible_data = {}
    evidence = ["green Martian", "Thark chieftain", "15ft tall", "four-armed warrior"]
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "non_human_humanoid"
    assert alias_target is None


def test_fallback_bucket_dead_friend_context_only():
    """Test dead friend is context_only."""
    entry = {"canonical_id": "dead_friend", "entity_kind": "individual", "status": "canonical"}
    bible_data = {}
    evidence = ["dead friend", "riddled with arrows", "deceased prospector"]
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "context_only"
    assert alias_target is None


def test_fallback_bucket_ape_large_creature():
    """Test ape/colossal creature is large_creature."""
    entry = {"canonical_id": "white_apes", "entity_kind": "individual", "status": "canonical"}
    bible_data = {}
    evidence = ["colossal ape", "massive creature", "beast"]
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "large_creature"
    assert alias_target is None


def test_fallback_bucket_apache_warriors_group():
    """Test apache_warriors is group_or_horde."""
    entry = {"canonical_id": "apache_warriors", "entity_kind": "group", "status": "canonical"}
    bible_data = {}
    evidence = ["Apache warriors", "group of warriors"]
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "group_or_horde"
    assert alias_target is None


def test_fallback_bucket_woola_large_quadruped():
    """Test woola/watchdog is classified as large_quadruped."""
    entry = {"canonical_id": "woola", "entity_kind": "individual", "status": "canonical"}
    bible_data = {}
    evidence = ["Martian watchdog", "calot", "large hound", "loyal mount"]
    
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
    entry = {"canonical_id": "protagonist", "entity_kind": "individual", "status": "canonical"}
    bible_data = {}
    evidence = ["protagonist", "John Carter"]
    
    fallback = deterministic_visual_fallback(entry, bible_data, evidence)
    
    assert fallback["status"] == "alias_redirect"
    assert fallback["fallback_bucket"] == "alias_redirect"
    assert fallback["alias_redirect_target"] == "john_carter"
    assert "john_carter" in fallback["production_identity_descriptor"]


def test_deterministic_visual_fallback_human():
    """Test fallback generation for human bucket."""
    entry = {"canonical_id": "john_carter", "entity_kind": "individual", "status": "canonical"}
    bible_data = {}
    evidence = ["John Carter", "human soldier", "Virginia", "cavalry"]
    
    fallback = deterministic_visual_fallback(entry, bible_data, evidence)
    
    assert fallback["status"] == "generated"
    assert fallback["fallback_bucket"] == "human"
    assert "human" in fallback["production_identity_descriptor"]
    assert "human build" in fallback["production_body_descriptor"]
    assert len(fallback["negative_terms"]) > 0
    assert "not strict canon" in fallback["provisionality_note"]


def test_deterministic_visual_fallback_non_human_humanoid():
    """Test fallback generation for non_human_humanoid bucket."""
    entry = {"canonical_id": "tars_tarkas", "entity_kind": "individual", "status": "canonical"}
    bible_data = {}
    evidence = ["green Martian", "Thark chieftain", "15ft tall", "four-armed"]
    
    fallback = deterministic_visual_fallback(entry, bible_data, evidence)
    
    assert fallback["status"] == "generated"
    assert fallback["fallback_bucket"] == "non_human_humanoid"
    assert "humanoid" in fallback["production_identity_descriptor"]
    assert "humanoid build" in fallback["production_body_descriptor"]
    assert "humanoid facial" in fallback["production_face_descriptor"]
    assert len(fallback["negative_terms"]) > 0


def test_deterministic_visual_fallback_large_creature():
    """Test fallback generation for large_creature bucket."""
    entry = {"canonical_id": "white_apes", "entity_kind": "individual", "status": "canonical"}
    bible_data = {}
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
    entry = {"canonical_id": "martian_leader", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "identity_baseline": "15ft tall green Martian chieftain",
        "physical_build": "massive four-armed frame",
        "physical_traits": ["four arms", "green skin"],
        "costume_signature": "metal armlet and leather harness",
        "distinguishing_features": ["ornate armlet"],
        "movement_language": "unknown",
    }
    evidence = ["green Martian", "chieftain", "15ft tall", "four-armed"]
    
    fallback = deterministic_visual_fallback(entry, bible_data, evidence)
    
    # Canon fields should be preserved in fallback
    assert "15ft tall green Martian chieftain" in fallback["production_identity_descriptor"]
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
    
    entry = {"canonical_id": "sola", "entity_kind": "individual", "status": "canonical"}
    evidence = ["green Martian", "warrior", "female"]
    
    fallback = deterministic_visual_fallback(entry, thin_bible, evidence)
    
    assert fallback["status"] == "generated"
    assert fallback["fallback_bucket"] == "non_human_humanoid"
    assert fallback["production_identity_descriptor"] != "unknown"
    assert fallback["production_body_descriptor"] != "unknown"


def test_strict_canon_fields_preserved():
    """Test that strict canon fields are preserved and not overwritten."""
    strong_bible = {
        "identity_baseline": "John Carter of Virginia",
        "age_presence": "mature adult",
        "physical_build": "lean muscular cavalry build",
        "origin_or_historical_context": "1860s Virginia",
        "movement_language": "military bearing",
        "costume_signature": "Confederate uniform remnants",
        "stable_visual_summary": "weathered frontier soldier",
        "physical_traits": ["weathered"],
        "distinguishing_features": ["scar on cheek"],
        "state_variants": ["armed"],
    }
    
    # Should not need fallback
    assert not needs_visual_production_fallback(strong_bible)


def test_martian_leader_with_mount_evidence():
    """Test A: martian_leader with evidence mentioning mount should be non_human_humanoid."""
    entry = {"canonical_id": "martian_leader", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "identity_baseline": "A massive, four-armed Martian warrior leader.",
        "physical_build": "15ft tall; heavy humanoid frame with four arms.",
        "movement_language": "Dismounts from an eight-legged mount to approach others.",
        "physical_traits": "Four arms, Red eyes, Tusks, Olive-green skin",
        "costume_signature": "Unarmed, carrying a metal armlet as peace offering.",
    }
    evidence = ["dismounts from his eight-legged mount", "massive Martian warrior", "four-armed leader"]
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "non_human_humanoid", f"Expected non_human_humanoid but got {bucket}"
    assert alias_target is None


def test_chieftain_with_furniture_evidence():
    """Test B: chieftain with furniture/mount/hound evidence should be non_human_humanoid."""
    entry = {"canonical_id": "chieftain", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "identity_baseline": "A green Martian of significant physical presence.",
        "physical_build": "Large-framed; out of proportion to human-scale furniture.",
        "role": "Leader/Chieftain of a Martian assemblage.",
        "distinguishing_features": "Green skin, large scale",
    }
    evidence = ["chieftain", "green Martian", "chariot hound following behind"]
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "non_human_humanoid", f"Expected non_human_humanoid but got {bucket}"
    assert alias_target is None


def test_john_carter_with_lifeless_shell_evidence():
    """Test C: john_carter with lifeless shell/body evidence should be human, not context_only."""
    entry = {"canonical_id": "john_carter", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "identity_baseline": "An Earthman undergoing supernatural transformation.",
        "stable_visual_summary": "naked human male, agile movement, leaping through low gravity.",
        "physical_build": "agile human male",
        "costume_signature": "naked post-transformation",
    }
    evidence = ["lifeless physical shell", "John Carter", "Earthman", "agile movement"]
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "human", f"Expected human but got {bucket}"
    assert alias_target is None


def test_protagonist_always_redirects():
    """Test D: protagonist always redirects to john_carter."""
    entry = {"canonical_id": "protagonist", "display_name": "protagonist", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "identity_baseline": "An Earthman undergoing supernatural transformation.",
        "stable_visual_summary": "naked human male, agile movement.",
    }
    evidence = ["some evidence without John Carter mention"]
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "alias_redirect", f"Expected alias_redirect but got {bucket}"
    assert alias_target == "john_carter"
    
    # Test full fallback generation
    fallback = deterministic_visual_fallback(entry, bible_data, evidence)
    assert fallback["status"] == "alias_redirect"
    assert fallback["fallback_bucket"] == "alias_redirect"
    assert fallback["canonical_target_id"] == "john_carter"
    assert fallback["alias_redirect_target"] == "john_carter"
    assert "john_carter" in fallback["production_identity_descriptor"]


def test_martian_mounts_classification():
    """Test E: martian_mounts should be large_quadruped or large_creature."""
    entry = {"canonical_id": "martian_mounts", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "stable_visual_summary": "Martian mounts; eight-legged riding beasts.",
        "physical_build": "Large quadruped frame with eight legs.",
    }
    evidence = ["Martian mounts", "eight-legged riding beasts", "large mount"]
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket in ["large_quadruped", "large_creature"], f"Expected large_quadruped or large_creature but got {bucket}"
    assert alias_target is None


def test_notan_non_human_humanoid():
    """Test F: notan should be non_human_humanoid, not human."""
    entry = {"canonical_id": "notan", "entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "identity_baseline": "Red Martian officer.",
        "physical_build": "Humanoid frame with Martian proportions.",
        "role": "Officer in the Martian hierarchy.",
    }
    evidence = ["Red Martian", "officer", "humanoid"]
    
    bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "non_human_humanoid", f"Expected non_human_humanoid but got {bucket}"
    assert alias_target is None


def test_watch_thing_not_human():
    """Test G: watch_thing should be large_creature or large_quadruped, not human."""
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
