"""Tests for character bible taxonomy integration."""
from __future__ import annotations

import json
from pathlib import Path

import pytest

from orchestrator.character_bible_models import CharacterBible


def test_character_bible_serializes_taxonomy_fields():
    """Test that CharacterBible model serializes taxonomy fields."""
    bible = CharacterBible(
        character_id="test_char",
        display_name="Test Character",
        entity_taxonomy={
            "primary_type": "human",
            "morphology": "biped",
            "scale": "human_scale",
            "renderability": "renderable",
            "confidence": 0.9,
        },
        alias_resolution={
            "status": "canonical",
            "canonical_target_id": None,
            "confidence": 1.0,
        },
        associated_entities=[
            {"evidence": "rides a mount"},
            {"evidence": "wears armor"},
        ],
    )
    
    data = bible.to_dict()
    
    assert "entity_taxonomy" in data
    assert data["entity_taxonomy"]["primary_type"] == "human"
    assert "alias_resolution" in data
    assert data["alias_resolution"]["status"] == "canonical"
    assert "associated_entities" in data
    assert len(data["associated_entities"]) == 2


def test_character_bible_taxonomy_missing_does_not_crash():
    """Test that missing taxonomy does not crash."""
    bible = CharacterBible(
        character_id="test_char",
        display_name="Test Character",
    )
    
    data = bible.to_dict()
    
    assert "entity_taxonomy" in data
    assert data["entity_taxonomy"] == {}
    assert "alias_resolution" in data
    assert data["alias_resolution"] == {}
    assert "associated_entities" in data
    assert data["associated_entities"] == []


def test_alias_candidate_preserved():
    """Test that alias_candidate is preserved and does not auto-redirect."""
    bible = CharacterBible(
        character_id="test_alias",
        display_name="Test Alias",
        alias_resolution={
            "status": "alias_candidate",
            "canonical_target_id": "main_char",
            "confidence": 0.7,
            "requires_human_review": True,
        },
    )
    
    data = bible.to_dict()
    
    assert data["alias_resolution"]["status"] == "alias_candidate"
    assert data["alias_resolution"]["canonical_target_id"] == "main_char"
    assert data["alias_resolution"]["requires_human_review"] is True


def test_alias_approved_serialized():
    """Test that alias_approved is serialized with target."""
    bible = CharacterBible(
        character_id="approved_alias",
        display_name="Approved Alias",
        alias_resolution={
            "status": "alias_approved",
            "canonical_target_id": "canonical_char",
            "confidence": 1.0,
            "requires_human_review": False,
        },
    )
    
    data = bible.to_dict()
    
    assert data["alias_resolution"]["status"] == "alias_approved"
    assert data["alias_resolution"]["canonical_target_id"] == "canonical_char"


def test_associated_evidence_separate_from_body():
    """Test that associated evidence appears in associated_entities, not as physical body traits."""
    bible = CharacterBible(
        character_id="warrior",
        display_name="Warrior",
        physical_traits=["tall", "muscular"],
        entity_taxonomy={
            "primary_type": "human",
            "morphology": "biped",
        },
        associated_entities=[
            {"evidence": "rides a large mount"},
            {"evidence": "carries a sword"},
        ],
    )
    
    data = bible.to_dict()
    
    # Physical traits should not include mount/weapon
    assert "tall" in data["physical_traits"]
    assert "muscular" in data["physical_traits"]
    assert "mount" not in str(data["physical_traits"]).lower()
    
    # Associated entities should be separate
    assert len(data["associated_entities"]) == 2
    assert any("mount" in str(e).lower() for e in data["associated_entities"])


def test_role_label_does_not_redirect():
    """Test that role_label does not auto-redirect."""
    bible = CharacterBible(
        character_id="the_captain",
        display_name="The Captain",
        alias_resolution={
            "status": "role_label",
            "canonical_target_id": None,
            "confidence": 0.0,
            "requires_human_review": True,
        },
    )
    
    data = bible.to_dict()
    
    assert data["alias_resolution"]["status"] == "role_label"
    assert data["alias_resolution"]["canonical_target_id"] is None


def test_canonical_does_not_redirect():
    """Test that canonical status does not redirect."""
    bible = CharacterBible(
        character_id="main_char",
        display_name="Main Character",
        alias_resolution={
            "status": "canonical",
            "canonical_target_id": None,
            "confidence": 1.0,
        },
    )
    
    data = bible.to_dict()
    
    assert data["alias_resolution"]["status"] == "canonical"
    assert data["alias_resolution"]["canonical_target_id"] is None


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
