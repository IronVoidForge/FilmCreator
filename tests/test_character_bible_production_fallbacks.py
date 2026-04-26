"""Tests for character bible production fallbacks."""
from __future__ import annotations

import pytest

from orchestrator.character_bible_fallback import (
    fallback_bucket_for_character,
    deterministic_visual_fallback,
)


def test_alias_approved_redirects():
    """Test that alias_approved redirects."""
    entry = {"entity_kind": "individual"}
    bible_data = {
        "alias_resolution": {
            "status": "alias_approved",
            "canonical_target_id": "main_char",
        }
    }
    
    bucket, target = fallback_bucket_for_character(entry, bible_data, [])
    
    assert bucket == "alias_redirect"
    assert target == "main_char"


def test_legacy_approved_redirects():
    """Test that legacy 'approved' status redirects."""
    entry = {"entity_kind": "individual"}
    bible_data = {
        "alias_resolution": {
            "status": "approved",
            "canonical_target_id": "main_char",
        }
    }
    
    bucket, target = fallback_bucket_for_character(entry, bible_data, [])
    
    assert bucket == "alias_redirect"
    assert target == "main_char"


def test_alias_candidate_does_not_redirect():
    """Test that alias_candidate does not redirect."""
    entry = {"entity_kind": "individual"}
    bible_data = {
        "alias_resolution": {
            "status": "alias_candidate",
            "canonical_target_id": "main_char",
        }
    }
    
    bucket, target = fallback_bucket_for_character(entry, bible_data, [])
    
    assert bucket != "alias_redirect"
    assert target is None


def test_role_label_does_not_redirect():
    """Test that role_label does not redirect."""
    entry = {"entity_kind": "individual"}
    bible_data = {
        "alias_resolution": {
            "status": "role_label",
            "canonical_target_id": None,
        }
    }
    
    bucket, target = fallback_bucket_for_character(entry, bible_data, [])
    
    assert bucket != "alias_redirect"
    assert target is None


def test_canonical_does_not_redirect():
    """Test that canonical does not redirect."""
    entry = {"entity_kind": "individual"}
    bible_data = {
        "alias_resolution": {
            "status": "canonical",
            "canonical_target_id": None,
        }
    }
    
    bucket, target = fallback_bucket_for_character(entry, bible_data, [])
    
    assert bucket != "alias_redirect"
    assert target is None


def test_taxonomy_human_to_human_fallback():
    """Test that taxonomy human maps to human fallback."""
    entry = {"entity_kind": "individual"}
    bible_data = {
        "entity_taxonomy": {
            "primary_type": "human",
            "morphology": "biped",
            "scale": "human_scale",
            "renderability": "renderable",
        }
    }
    
    bucket, target = fallback_bucket_for_character(entry, bible_data, [])
    
    assert bucket == "human"
    assert target is None


def test_taxonomy_humanoid_nonhuman_to_non_human_humanoid_fallback():
    """Test that taxonomy humanoid_nonhuman maps to non_human_humanoid fallback."""
    entry = {"entity_kind": "individual"}
    bible_data = {
        "entity_taxonomy": {
            "primary_type": "humanoid_nonhuman",
            "morphology": "biped",
            "scale": "human_scale",
            "renderability": "renderable",
        }
    }
    
    bucket, target = fallback_bucket_for_character(entry, bible_data, [])
    
    assert bucket == "non_human_humanoid"
    assert target is None


def test_taxonomy_missing_to_unknown_reference():
    """Test that missing taxonomy maps to unknown_reference, not guessed from prose."""
    entry = {"entity_kind": "individual"}
    bible_data = {}
    
    bucket, target = fallback_bucket_for_character(entry, bible_data, [])
    
    assert bucket == "unknown_reference"
    assert target is None


def test_fallback_human_descriptor():
    """Test human fallback descriptor generation."""
    entry = {"entity_kind": "individual"}
    bible_data = {
        "entity_taxonomy": {
            "primary_type": "human",
            "morphology": "biped",
            "renderability": "renderable",
        }
    }
    
    fallback = deterministic_visual_fallback(entry, bible_data, [])
    
    assert fallback["fallback_bucket"] == "human"
    assert "human" in fallback["production_identity_descriptor"].lower()
    assert "alien anatomy" in fallback["negative_terms"]


def test_fallback_non_human_humanoid_descriptor():
    """Test non-human humanoid fallback descriptor generation."""
    entry = {"entity_kind": "individual"}
    bible_data = {
        "entity_taxonomy": {
            "primary_type": "humanoid_nonhuman",
            "morphology": "biped",
            "renderability": "renderable",
        }
    }
    
    fallback = deterministic_visual_fallback(entry, bible_data, [])
    
    assert fallback["fallback_bucket"] == "non_human_humanoid"
    assert "humanoid" in fallback["production_identity_descriptor"].lower()
    assert "human proportions" in fallback["negative_terms"]


def test_fallback_large_quadruped_descriptor():
    """Test large quadruped fallback descriptor generation."""
    entry = {"entity_kind": "individual"}
    bible_data = {
        "entity_taxonomy": {
            "primary_type": "animal",
            "morphology": "quadruped",
            "scale": "large",
            "renderability": "renderable",
        }
    }
    
    fallback = deterministic_visual_fallback(entry, bible_data, [])
    
    assert fallback["fallback_bucket"] == "large_quadruped"
    assert "four-legged" in fallback["production_identity_descriptor"].lower() or "quadruped" in fallback["production_identity_descriptor"].lower()
    # Negative terms should exclude human/upright characteristics
    assert any("human" in term.lower() or "upright" in term.lower() for term in fallback["negative_terms"])


def test_fallback_context_only():
    """Test context_only fallback."""
    entry = {"entity_kind": "individual"}
    bible_data = {
        "entity_taxonomy": {
            "primary_type": "abstract",
            "renderability": "context_only",
        }
    }
    
    fallback = deterministic_visual_fallback(entry, bible_data, [])
    
    assert fallback["fallback_bucket"] == "context_only"
    assert fallback["status"] == "context_only"
    assert "not applicable" in fallback["production_body_descriptor"].lower()


def test_fallback_negative_terms_filtered_by_taxonomy():
    """Test that negative terms are filtered to prevent contradictions with taxonomy."""
    entry = {"entity_kind": "individual"}
    bible_data = {
        "entity_taxonomy": {
            "primary_type": "human",
            "morphology": "biped",
        }
    }
    
    fallback = deterministic_visual_fallback(entry, bible_data, [])
    
    # Should not include "human" in negative terms since taxonomy says human
    negative_str = " ".join(fallback["negative_terms"]).lower()
    assert "human" not in negative_str or "non-human" in negative_str


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
