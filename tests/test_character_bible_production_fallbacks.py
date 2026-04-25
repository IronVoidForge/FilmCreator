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
    assert is_unknownish("none")
    assert is_unknownish("n/a")
    assert is_unknownish([])
    assert is_unknownish(["", "  "])
    assert not is_unknownish("valid value")
    assert not is_unknownish(["valid"])


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
    
    # Strong bible with good evidence
    strong_bible = {
        "identity_baseline": "tall Martian warrior",
        "physical_build": "massive muscular frame",
        "costume_signature": "leather harness and metal fittings",
        "stable_visual_summary": "imposing green Martian warrior",
    }
    assert not needs_visual_production_fallback(strong_bible)
    
    # Partially thin bible (only 1 unknown)
    partial_bible = {
        "identity_baseline": "frontier soldier",
        "physical_build": "lean athletic build",
        "costume_signature": "unknown",
        "stable_visual_summary": "weathered cavalry officer",
    }
    assert not needs_visual_production_fallback(partial_bible)


def test_fallback_bucket_context_only():
    """Test context_only bucket for non-renderable entities."""
    entry = {"entity_kind": "deceased", "status": "canonical"}
    bible_data = {}
    evidence = []
    
    bucket = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "context_only"
    
    # Test evidence-based detection
    entry2 = {"entity_kind": "individual", "status": "canonical"}
    evidence2 = ["dead friend", "mentioned only", "former companion"]
    bucket2 = fallback_bucket_for_character(entry2, bible_data, evidence2)
    assert bucket2 == "context_only"


def test_fallback_bucket_earth_human():
    """Test earth_human bucket detection."""
    entry = {"entity_kind": "individual", "status": "canonical"}
    bible_data = {}
    evidence = ["human soldier", "American frontier", "Confederate cavalry officer"]
    
    bucket = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "earth_human"


def test_fallback_bucket_barsoom_humanoid():
    """Test barsoom_humanoid bucket detection."""
    entry = {"entity_kind": "individual", "status": "canonical"}
    bible_data = {}
    evidence = ["green Martian", "Thark warrior", "Barsoom"]
    
    bucket = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "barsoom_humanoid"


def test_fallback_bucket_creature():
    """Test creature_or_primitive bucket detection."""
    entry = {"entity_kind": "individual", "status": "canonical"}
    bible_data = {}
    evidence = ["calot", "beast", "animal companion"]
    
    bucket = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "creature_or_primitive"


def test_fallback_bucket_group():
    """Test group_or_horde bucket detection."""
    entry = {"entity_kind": "group", "status": "canonical"}
    bible_data = {}
    evidence = ["warriors", "collective"]
    
    bucket = fallback_bucket_for_character(entry, bible_data, evidence)
    assert bucket == "group_or_horde"


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


def test_deterministic_visual_fallback_earth_human():
    """Test fallback generation for earth_human bucket."""
    entry = {"entity_kind": "individual", "status": "canonical"}
    bible_data = {}
    evidence = ["human soldier", "frontier", "cavalry"]
    
    fallback = deterministic_visual_fallback(entry, bible_data, evidence)
    
    assert fallback["status"] == "generated"
    assert fallback["fallback_bucket"] == "earth_human"
    assert "frontier" in fallback["production_identity_descriptor"]
    assert "lean athletic" in fallback["production_body_descriptor"]
    assert "weathered face" in fallback["production_face_descriptor"]
    assert len(fallback["production_state_variants"]) > 0
    assert len(fallback["negative_terms"]) > 0
    assert "not strict canon" in fallback["provisionality_note"]


def test_deterministic_visual_fallback_barsoom_humanoid():
    """Test fallback generation for barsoom_humanoid bucket."""
    entry = {"entity_kind": "individual", "status": "canonical"}
    bible_data = {}
    evidence = ["Martian", "Thark", "green skin"]
    
    fallback = deterministic_visual_fallback(entry, bible_data, evidence)
    
    assert fallback["status"] == "generated"
    assert fallback["fallback_bucket"] == "barsoom_humanoid"
    assert "Martian" in fallback["production_identity_descriptor"]
    assert "Martian gravity" in fallback["production_body_descriptor"]
    assert "Martian features" in fallback["production_face_descriptor"]
    assert "harness" in fallback["production_costume_descriptor"]
    assert len(fallback["negative_terms"]) > 0


def test_deterministic_visual_fallback_creature():
    """Test fallback generation for creature_or_primitive bucket."""
    entry = {"entity_kind": "individual", "status": "canonical"}
    bible_data = {}
    evidence = ["calot", "beast", "animal"]
    
    fallback = deterministic_visual_fallback(entry, bible_data, evidence)
    
    assert fallback["status"] == "generated"
    assert fallback["fallback_bucket"] == "creature_or_primitive"
    assert "creature" in fallback["production_identity_descriptor"]
    assert "animal" in fallback["production_body_descriptor"]
    assert "skull" in fallback["production_face_descriptor"]
    assert "hide" in fallback["production_costume_descriptor"]


def test_deterministic_visual_fallback_preserves_canon():
    """Test that fallback does not overwrite canon fields."""
    entry = {"entity_kind": "individual", "status": "canonical"}
    bible_data = {
        "identity_baseline": "tall warrior",
        "physical_build": "muscular",
        "costume_signature": "leather harness",
        "stable_visual_summary": "imposing figure",
    }
    evidence = ["Martian warrior"]
    
    # This bible should NOT need fallback
    assert not needs_visual_production_fallback(bible_data)
    
    # But if we generate fallback anyway, it's separate
    fallback = deterministic_visual_fallback(entry, bible_data, evidence)
    
    # Fallback is in its own block, doesn't touch bible_data
    assert "production_identity_descriptor" in fallback
    assert "identity_baseline" not in fallback


def test_thin_unknown_heavy_entity_receives_fallback():
    """Test that thin unknown-heavy entity receives visual_production_fallback."""
    thin_bible = {
        "identity_baseline": "unknown",
        "physical_build": "unknown",
        "costume_signature": "unknown",
        "stable_visual_summary": "",
    }
    
    assert needs_visual_production_fallback(thin_bible)
    
    entry = {"entity_kind": "individual", "status": "canonical"}
    evidence = ["Martian warrior", "green skin"]
    
    fallback = deterministic_visual_fallback(entry, thin_bible, evidence)
    
    assert fallback["status"] == "generated"
    assert fallback["fallback_bucket"] == "barsoom_humanoid"
    assert fallback["production_identity_descriptor"] != "unknown"
    assert fallback["production_body_descriptor"] != "unknown"


def test_strict_canon_fields_preserved():
    """Test that strict canon fields are preserved and not overwritten."""
    strong_bible = {
        "identity_baseline": "John Carter of Virginia",
        "physical_build": "lean muscular cavalry build",
        "costume_signature": "Confederate uniform remnants",
        "stable_visual_summary": "weathered frontier soldier",
    }
    
    # Should not need fallback
    assert not needs_visual_production_fallback(strong_bible)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
