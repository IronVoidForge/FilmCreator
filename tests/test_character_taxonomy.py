from __future__ import annotations

import json
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from orchestrator.character_taxonomy import (
    _determine_morphology,
    _determine_primary_type,
    _determine_renderability,
    _determine_scale,
    _determine_sentience,
    _extract_entity_type_hints,
    _extract_morphology_hints,
    _extract_scale_hints,
    _synthesize_character_taxonomy,
    run_character_taxonomy,
)
from orchestrator.core.paths import (
    character_taxonomy_dir,
    character_taxonomy_index_path,
    character_taxonomy_path,
    character_taxonomy_review_dir,
)


def test_path_helpers():
    """Test path helper functions."""
    project_dir = Path("C:/test_project")
    
    taxonomy_dir = character_taxonomy_dir(project_dir)
    assert taxonomy_dir == project_dir / "02_story_analysis" / "taxonomy" / "characters"
    
    taxonomy_path = character_taxonomy_path(project_dir, "test_char")
    assert taxonomy_path == taxonomy_dir / "CHAR_test_char_TAXONOMY.json"
    
    index_path = character_taxonomy_index_path(project_dir)
    assert index_path == taxonomy_dir / "CHARACTER_TAXONOMY_INDEX.json"
    
    review_dir = character_taxonomy_review_dir(project_dir)
    assert review_dir == project_dir / "02_story_analysis" / "taxonomy" / "review"


def test_human_with_exotic_clothing_remains_human():
    """Test that a human wearing exotic clothing remains classified as human."""
    bible_data = {
        "content": "A human warrior from Earth wearing elaborate Martian armor and exotic clothing.",
        "path": "/test/path.md"
    }
    
    direct_hints, associated_hints = _extract_entity_type_hints(
        "warrior",
        {"entity_kind": "individual"},
        bible_data
    )
    
    assert "human" in direct_hints
    assert "has_costume" in associated_hints or "has_armor" in associated_hints
    
    primary_type, confidence, conflicts = _determine_primary_type(direct_hints, associated_hints, "individual")
    assert primary_type == "human"
    assert len(conflicts) == 0


def test_rider_remains_humanoid_mount_is_associated():
    """Test that a person riding a mount remains humanoid, mount is associated evidence."""
    bible_data = {
        "content": "A humanoid warrior riding a large mount across the desert.",
        "path": "/test/path.md"
    }
    
    direct_hints, associated_hints = _extract_entity_type_hints(
        "warrior",
        {"entity_kind": "individual"},
        bible_data
    )
    
    # Rider should have humanoid hints
    assert "humanoid_nonhuman" in direct_hints or len(direct_hints) == 0
    # Mount should be in associated evidence
    assert "has_mount" in associated_hints
    
    # Associated evidence should not override primary type
    primary_type, confidence, conflicts = _determine_primary_type(direct_hints, associated_hints, "individual")
    assert primary_type != "animal"  # Should not be classified as animal due to mount


def test_mount_entity_becomes_animal():
    """Test that a mount entity with direct mount evidence becomes animal/creature."""
    bible_data = {
        "content": "A Martian hound, a large quadruped creature used as a mount and companion.",
        "path": "/test/path.md"
    }
    
    direct_hints, associated_hints = _extract_entity_type_hints(
        "mount_creature",
        {"entity_kind": "individual"},
        bible_data
    )
    
    morphology_hints = _extract_morphology_hints("mount_creature", bible_data)
    
    assert "animal" in direct_hints
    assert "quadruped" in morphology_hints
    
    primary_type, confidence, conflicts = _determine_primary_type(direct_hints, associated_hints, "individual")
    assert primary_type == "animal"
    
    morphology, morph_conf, morph_conflicts = _determine_morphology(morphology_hints)
    assert morphology in ["quadruped", "multi_legged"]


def test_group_entity_becomes_group_type():
    """Test that a group entity becomes primary_type group."""
    registry_entry = {"entity_kind": "group", "display_name": "warriors"}
    
    direct_hints, associated_hints = _extract_entity_type_hints(
        "warriors",
        registry_entry,
        None
    )
    
    primary_type, confidence, conflicts = _determine_primary_type(direct_hints, associated_hints, "group")
    assert primary_type == "group"
    assert confidence == 1.0


def test_deceased_entity_becomes_context_only():
    """Test that deceased/narrative-only entity becomes context_only."""
    bible_data = {
        "content": "A mummified corpse, deceased and preserved, found in an ancient chamber.",
        "path": "/test/path.md"
    }
    
    direct_hints, associated_hints = _extract_entity_type_hints(
        "mummified_person",
        {"entity_kind": "individual"},
        bible_data
    )
    
    assert "context_only" in direct_hints
    
    primary_type, confidence, conflicts = _determine_primary_type(direct_hints, associated_hints, "individual")
    renderability = _determine_renderability(primary_type, "individual", "mummified_person")
    
    assert renderability == "context_only"


def test_ambiguous_role_label_requires_review():
    """Test that ambiguous role label becomes alias_candidate with review required."""
    registry_entry = {
        "entity_kind": "provisional_role",
        "status": "provisional",
        "display_name": "the_captain"
    }
    
    taxonomy = _synthesize_character_taxonomy(
        "the_captain",
        registry_entry,
        Path("/test/project")
    )
    
    assert taxonomy["alias_resolution"]["status"] == "role_label"
    assert taxonomy["alias_resolution"]["requires_human_review"] is True
    assert taxonomy["alias_resolution"]["canonical_target_id"] is None
    assert taxonomy["needs_review"] is True
    assert taxonomy["renderability"] == "alias_redirect_candidate"


def test_conflicting_type_hints_create_review():
    """Test that conflicting type hints create needs_review."""
    bible_data = {
        "content": "A strange being, described as both human and a green Martian creature.",
        "path": "/test/path.md"
    }
    
    direct_hints, associated_hints = _extract_entity_type_hints(
        "strange_being",
        {"entity_kind": "individual"},
        bible_data
    )
    
    # Manually add conflicting hints for test
    direct_hints = ["human", "humanoid_nonhuman", "creature"]
    
    primary_type, confidence, conflicts = _determine_primary_type(direct_hints, associated_hints, "individual")
    
    assert len(conflicts) > 0
    assert primary_type == "unknown"


def test_no_evidence_becomes_unknown():
    """Test that no evidence becomes unknown, not guessed."""
    bible_data = None
    
    direct_hints, associated_hints = _extract_entity_type_hints(
        "mystery_entity",
        {"entity_kind": "individual"},
        bible_data
    )
    
    assert len(direct_hints) == 0
    
    primary_type, confidence, conflicts = _determine_primary_type(direct_hints, associated_hints, "individual")
    assert primary_type == "unknown"
    assert confidence == 0.0


def test_sentience_determination():
    """Test sentience determination from primary type."""
    assert _determine_sentience("human") == "person"
    assert _determine_sentience("humanoid_nonhuman") == "person"
    assert _determine_sentience("animal") == "animal"
    assert _determine_sentience("creature") == "monster"
    assert _determine_sentience("object") == "object"
    assert _determine_sentience("abstract") == "abstract"
    assert _determine_sentience("unknown") == "unknown"


def test_morphology_conflict_detection():
    """Test that conflicting morphology hints are detected."""
    hints = ["biped", "quadruped", "biped"]
    
    morphology, confidence, conflicts = _determine_morphology(hints)
    
    assert len(conflicts) > 0
    assert morphology == "unknown"


def test_scale_conflict_detection():
    """Test that conflicting scale hints are detected."""
    hints = ["tiny", "giant", "small"]
    
    scale, confidence, conflicts = _determine_scale(hints)
    
    assert len(conflicts) > 0
    assert scale == "unknown"


def test_taxonomy_synthesis_complete():
    """Test complete taxonomy synthesis for a character."""
    registry_entry = {
        "entity_kind": "individual",
        "display_name": "test_warrior",
        "status": "canonical",
        "sources": ["/test/source.md"]
    }
    
    with patch("orchestrator.character_taxonomy._load_character_bible") as mock_bible:
        mock_bible.return_value = {
            "content": "A human warrior from Earth, wearing armor and riding a mount.",
            "path": "/test/bible.md"
        }
        
        taxonomy = _synthesize_character_taxonomy(
            "test_warrior",
            registry_entry,
            Path("/test/project")
        )
    
    assert taxonomy["character_id"] == "test_warrior"
    assert taxonomy["display_name"] == "test_warrior"
    assert taxonomy["entity_kind"] == "individual"
    assert "primary_type" in taxonomy
    assert "morphology" in taxonomy
    assert "scale" in taxonomy
    assert "sentience" in taxonomy
    assert "renderability" in taxonomy
    assert "confidence" in taxonomy
    assert "direct_evidence" in taxonomy
    assert "associated_evidence" in taxonomy
    assert "conflicts" in taxonomy
    assert "unknowns" in taxonomy
    assert "needs_review" in taxonomy
    assert "review_reasons" in taxonomy
    assert "alias_resolution" in taxonomy
    assert "source_files" in taxonomy
    assert "generated_at_utc" in taxonomy


def test_run_character_taxonomy_empty_registry():
    """Test run_character_taxonomy with empty registry."""
    with patch("orchestrator.character_taxonomy._load_character_registry") as mock_registry:
        mock_registry.return_value = {}
        
        with patch("orchestrator.character_taxonomy.create_project") as mock_project:
            mock_project.return_value = Path("/test/project")
            
            result = run_character_taxonomy("test_project")
    
    assert result["status"] == "error"
    assert result["total_registry_entries"] == 0
    assert len(result["warnings"]) > 0


def test_run_character_taxonomy_with_limit():
    """Test run_character_taxonomy with limit parameter."""
    mock_registry = {
        "char1": {"entity_kind": "individual", "display_name": "char1", "status": "canonical", "sources": []},
        "char2": {"entity_kind": "individual", "display_name": "char2", "status": "canonical", "sources": []},
        "char3": {"entity_kind": "individual", "display_name": "char3", "status": "canonical", "sources": []},
    }
    
    with patch("orchestrator.character_taxonomy._load_character_registry") as mock_reg:
        mock_reg.return_value = mock_registry
        
        with patch("orchestrator.character_taxonomy.create_project") as mock_project:
            mock_project.return_value = Path("/test/project")
            
            with patch("orchestrator.character_taxonomy._load_character_bible") as mock_bible:
                mock_bible.return_value = None
                
                with patch("orchestrator.character_taxonomy.write_json"):
                    with patch("orchestrator.character_taxonomy.ensure_dir"):
                        with patch("orchestrator.character_taxonomy.repo_relative") as mock_rel:
                            mock_rel.side_effect = lambda p: f"test/{p.name}"
                            result = run_character_taxonomy("test_project", limit=2)
    
    assert result["status"] == "success"
    assert result["synthesized_count"] <= 2


def test_book_agnostic_no_hardcoded_names():
    """Test that no book-specific names are hardcoded in taxonomy logic."""
    # This test verifies the code doesn't contain hardcoded character names
    import inspect
    from orchestrator import character_taxonomy
    
    source = inspect.getsource(character_taxonomy)
    
    # Check for forbidden hardcoded names
    forbidden_names = ["john_carter", "barsoom", "dejah_thoris", "tars_tarkas", "mars"]
    
    for name in forbidden_names:
        # Allow in comments and docstrings, but not in actual logic
        lines = source.split("\n")
        for line in lines:
            # Skip comments and docstrings
            if line.strip().startswith("#") or '"""' in line or "'''" in line:
                continue
            # Check if forbidden name appears in actual code
            if name in line.lower() and "def " not in line and "class " not in line:
                pytest.fail(f"Found hardcoded book-specific name '{name}' in taxonomy logic: {line}")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
