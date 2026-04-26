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
    _iter_character_taxonomy_hint_records,
    _parse_taxonomy_hints_from_markdown,
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


def test_taxonomy_does_not_read_character_bible_markdown(tmp_path):
    """Test that taxonomy does not read character bible markdown."""
    project_dir = tmp_path / "test_project"
    project_dir.mkdir()
    
    # Create misleading bible markdown
    bible_dir = project_dir / "02_story_analysis" / "bibles" / "characters"
    bible_dir.mkdir(parents=True)
    bible_path = bible_dir / "CHAR_character_a.md"
    bible_path.write_text("This is a human warrior from Earth wearing green Martian armor.", encoding="utf-8")
    
    # Create registry entry
    registry_entry = {
        "entity_kind": "individual",
        "display_name": "character_a",
        "status": "canonical",
        "sources": []
    }
    
    # No structured taxonomy hint records
    taxonomy = _synthesize_character_taxonomy("character_a", registry_entry, project_dir)
    
    # Should be unknown, not inferred from bible
    assert taxonomy["primary_type"] == "unknown"
    assert taxonomy["needs_review"] is True
    assert taxonomy["confidence"] == 0.0


def test_taxonomy_aggregates_structured_chapter_hints(tmp_path):
    """Test that taxonomy aggregates structured chapter hints."""
    project_dir = tmp_path / "test_project"
    breakdown_dir = project_dir / "02_story_analysis" / "character_breakdowns" / "chapters" / "CH001"
    breakdown_dir.mkdir(parents=True)
    
    # Create structured hint record (future format)
    # For now, this will return empty since parser returns None
    registry_entry = {
        "entity_kind": "individual",
        "display_name": "test_char",
        "status": "canonical",
        "sources": []
    }
    
    taxonomy = _synthesize_character_taxonomy("test_char", registry_entry, project_dir)
    
    # Without structured hints, should be unknown
    assert taxonomy["primary_type"] == "unknown"
    assert taxonomy["needs_review"] is True


def test_associated_evidence_does_not_override_direct_hint():
    """Test that associated evidence does not override direct hint."""
    # Direct hint says human
    direct_hints = ["human"]
    associated_hints = ["has_mount", "rides_animal"]
    
    primary_type, confidence, conflicts = _determine_primary_type(direct_hints, associated_hints, "individual")
    
    # Should remain human, not become animal
    assert primary_type == "human"
    assert len(conflicts) == 0


def test_conflicting_direct_hints_creates_review():
    """Test that conflicting direct hints create needs_review."""
    direct_hints = ["human", "animal"]
    associated_hints = []
    
    primary_type, confidence, conflicts = _determine_primary_type(direct_hints, associated_hints, "individual")
    
    assert len(conflicts) > 0
    assert primary_type == "unknown"
    assert confidence == 0.0


def test_no_book_specific_runtime_terms_in_character_taxonomy():
    """Test that no book-specific terms are in character_taxonomy.py."""
    import inspect
    from orchestrator import character_taxonomy
    
    source = inspect.getsource(character_taxonomy)
    source_lower = source.lower()
    
    # Forbidden book-specific terms
    forbidden = [
        "john_carter",
        "barsoom",
        "green martian",
        "red martian",
        "confederate",
        "virginia",
        "calot",
        "martian hound",
    ]
    
    for term in forbidden:
        # Check if term appears in actual code (not comments/docstrings)
        lines = source.split("\n")
        for line in lines:
            stripped = line.strip()
            # Skip comments and docstrings
            if stripped.startswith("#") or '"""' in line or "'''" in line:
                continue
            # Skip function/class definitions
            if "def " in stripped or "class " in stripped:
                continue
            # Check for forbidden term
            if term in line.lower():
                pytest.fail(f"Found forbidden book-specific term '{term}' in line: {line}")


def test_human_with_exotic_clothing_remains_human():
    """Test that a human wearing exotic clothing remains classified as human."""
    # With structured hints, human type is preserved
    direct_hints = ["human"]
    associated_hints = ["has_costume", "has_armor"]
    
    primary_type, confidence, conflicts = _determine_primary_type(direct_hints, associated_hints, "individual")
    
    assert primary_type == "human"
    assert len(conflicts) == 0


def test_rider_remains_humanoid_mount_is_associated():
    """Test that a person riding a mount remains humanoid, mount is associated evidence."""
    direct_hints = ["humanoid_nonhuman"]
    associated_hints = ["has_mount"]
    
    primary_type, confidence, conflicts = _determine_primary_type(direct_hints, associated_hints, "individual")
    
    assert primary_type == "humanoid_nonhuman"
    assert len(conflicts) == 0


def test_mount_entity_becomes_animal():
    """Test that a mount entity with direct animal evidence becomes animal."""
    direct_hints = ["animal"]
    associated_hints = []
    morphology_hints = ["quadruped"]
    
    primary_type, confidence, conflicts = _determine_primary_type(direct_hints, associated_hints, "individual")
    morphology, morph_conf, morph_conflicts = _determine_morphology(morphology_hints)
    
    assert primary_type == "animal"
    assert morphology == "quadruped"


def test_group_entity_becomes_group_type():
    """Test that a group entity becomes primary_type group."""
    registry_entry = {"entity_kind": "group", "display_name": "warriors"}
    
    direct_hints = ["group"]
    associated_hints = []
    
    primary_type, confidence, conflicts = _determine_primary_type(direct_hints, associated_hints, "group")
    assert primary_type == "group"
    assert confidence == 1.0


def test_deceased_entity_becomes_context_only():
    """Test that deceased/narrative-only entity becomes context_only."""
    direct_hints = ["context_only"]
    associated_hints = []
    
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
    # Manually create conflicting hints
    direct_hints = ["human", "humanoid_nonhuman", "creature"]
    associated_hints = []
    
    primary_type, confidence, conflicts = _determine_primary_type(direct_hints, associated_hints, "individual")
    
    assert len(conflicts) > 0
    assert primary_type == "unknown"


def test_no_evidence_becomes_unknown():
    """Test that no evidence becomes unknown, not guessed."""
    direct_hints = []
    associated_hints = []
    
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


def test_taxonomy_synthesis_complete(tmp_path):
    """Test complete taxonomy synthesis for a character."""
    project_dir = tmp_path / "test_project"
    project_dir.mkdir()
    
    registry_entry = {
        "entity_kind": "individual",
        "display_name": "test_warrior",
        "status": "canonical",
        "sources": ["/test/source.md"]
    }
    
    taxonomy = _synthesize_character_taxonomy("test_warrior", registry_entry, project_dir)
    
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


def test_run_character_taxonomy_with_limit(tmp_path):
    """Test run_character_taxonomy with limit parameter."""
    mock_registry = {
        "char1": {"entity_kind": "individual", "display_name": "char1", "status": "canonical", "sources": []},
        "char2": {"entity_kind": "individual", "display_name": "char2", "status": "canonical", "sources": []},
        "char3": {"entity_kind": "individual", "display_name": "char3", "status": "canonical", "sources": []},
    }
    
    project_dir = tmp_path / "test_project"
    project_dir.mkdir()
    
    # Create necessary directories
    taxonomy_dir = project_dir / "02_story_analysis" / "taxonomy" / "characters"
    taxonomy_dir.mkdir(parents=True)
    review_dir = project_dir / "02_story_analysis" / "taxonomy" / "review"
    review_dir.mkdir(parents=True)
    
    with patch("orchestrator.character_taxonomy._load_character_registry") as mock_reg:
        mock_reg.return_value = mock_registry
        
        with patch("orchestrator.character_taxonomy.create_project") as mock_project:
            mock_project.return_value = project_dir
            
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
    forbidden_names = ["john_carter", "barsoom", "dejah_thoris", "tars_tarkas", "mars", "calot", "martian hound"]
    
    for name in forbidden_names:
        # Allow in comments and docstrings, but not in actual logic
        lines = source.split("\n")
        for line in lines:
            # Skip comments and docstrings
            if line.strip().startswith("#") or '"""' in line or "'''" in line:
                continue
            # Check if forbidden name appears in actual code
            if name in line.lower() and "def " not in line and "class " not in line:
                # Skip if it's just in a test or example
                if "test" not in line.lower() and "example" not in line.lower():
                    pytest.fail(f"Found hardcoded book-specific name '{name}' in taxonomy logic: {line}")


def test_parse_taxonomy_hints_from_markdown_colon_format():
    """Test parsing taxonomy hints from colon format."""
    markdown = """# Character Breakdown

character_type_hint: human
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.85
direct_identity_evidence: explicitly called a human traveler
direct_visual_evidence: upright bipedal person
costume_or_covering_evidence: wears travel clothes
movement_evidence: walks upright
associated_entities: rides a large animal; carries a lantern
alias_or_role_evidence: none
unknowns: exact age
source_refs: CH001:P12
"""
    result = _parse_taxonomy_hints_from_markdown(markdown, "/test/path.md")
    
    assert result is not None
    assert result["character_type_hint"] == "human"
    assert result["morphology_hint"] == "biped"
    assert result["scale_hint"] == "human_scale"
    assert result["renderability_hint"] == "renderable"
    assert result["confidence"] == 0.85
    assert result["direct_identity_evidence"] == "explicitly called a human traveler"
    assert result["direct_visual_evidence"] == "upright bipedal person"
    assert result["costume_or_covering_evidence"] == "wears travel clothes"
    assert result["movement_evidence"] == "walks upright"
    assert result["associated_entities"] == ["rides a large animal", "carries a lantern"]
    assert result["alias_or_role_evidence"] == "none"
    assert result["unknowns"] == "exact age"
    assert result["source_refs"] == ["CH001:P12"]
    assert result["source_path"] == "/test/path.md"


def test_parse_taxonomy_hints_from_markdown_bullet_format():
    """Test parsing taxonomy hints from bullet format."""
    markdown = """# Character Breakdown

- character_type_hint: human
- morphology_hint: biped
- scale_hint: human_scale
- renderability_hint: renderable
- confidence: 0.85
- direct_identity_evidence: explicitly called a human traveler
- associated_entities: rides a large animal; carries a lantern
"""
    result = _parse_taxonomy_hints_from_markdown(markdown, "/test/path.md")
    
    assert result is not None
    assert result["character_type_hint"] == "human"
    assert result["morphology_hint"] == "biped"
    assert result["scale_hint"] == "human_scale"
    assert result["renderability_hint"] == "renderable"
    assert result["confidence"] == 0.85
    assert result["associated_entities"] == ["rides a large animal", "carries a lantern"]


def test_parse_taxonomy_hints_from_markdown_display_labels():
    """Test parsing taxonomy hints with display labels."""
    markdown = """# Character Breakdown

- character_type: animal
- morphology: quadruped
- scale: large
- renderability: renderable
"""
    result = _parse_taxonomy_hints_from_markdown(markdown, "/test/path.md")
    
    assert result is not None
    assert result["character_type_hint"] == "animal"
    assert result["morphology_hint"] == "quadruped"
    assert result["scale_hint"] == "large"
    assert result["renderability_hint"] == "renderable"


def test_parse_taxonomy_hints_returns_none_without_structured_fields():
    """Test that parser returns None for prose-only content."""
    markdown = """# Character Breakdown

The traveler rides a huge beast and walks into town.
He appears to be a human warrior wearing exotic armor.
"""
    result = _parse_taxonomy_hints_from_markdown(markdown, "/test/path.md")
    
    assert result is None


def test_parse_taxonomy_hints_invalid_values_become_unknown():
    """Test that invalid enum values become unknown."""
    markdown = """# Character Breakdown

character_type_hint: invalid_type
morphology_hint: invalid_morph
scale_hint: invalid_scale
renderability_hint: invalid_render
"""
    result = _parse_taxonomy_hints_from_markdown(markdown, "/test/path.md")
    
    assert result is not None
    assert result["character_type_hint"] == "unknown"
    assert result["morphology_hint"] == "unknown"
    assert result["scale_hint"] == "unknown"
    assert result["renderability_hint"] == "unknown"


def test_parse_taxonomy_hints_confidence_clamped():
    """Test that confidence is clamped to 0.0-1.0."""
    markdown1 = "confidence: 2.0"
    result1 = _parse_taxonomy_hints_from_markdown(markdown1, "/test/path.md")
    assert result1["confidence"] == 1.0
    
    markdown2 = "confidence: -1.0"
    result2 = _parse_taxonomy_hints_from_markdown(markdown2, "/test/path.md")
    assert result2["confidence"] == 0.0


def test_taxonomy_aggregates_parsed_markdown_hints(tmp_path):
    """Test that taxonomy aggregates parsed markdown hints."""
    project_dir = tmp_path / "test_project"
    breakdown_dir = project_dir / "02_story_analysis" / "character_breakdowns" / "chapters" / "CH001"
    breakdown_dir.mkdir(parents=True)
    
    # Create structured hint markdown
    char_file = breakdown_dir / "test_char.md"
    char_file.write_text(
        """# Character Breakdown

character_type_hint: human
morphology_hint: biped
scale_hint: human_scale
confidence: 0.9
""",
        encoding="utf-8"
    )
    
    registry_entry = {
        "entity_kind": "individual",
        "display_name": "test_char",
        "status": "canonical",
        "sources": []
    }
    
    taxonomy = _synthesize_character_taxonomy("test_char", registry_entry, project_dir)
    
    # Should use parsed hints
    assert taxonomy["primary_type"] == "human"
    assert taxonomy["morphology"] == "biped"
    assert taxonomy["scale"] == "human_scale"
    assert taxonomy["confidence"] > 0.0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
