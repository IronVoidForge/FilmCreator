"""Test chapter entity extraction schema and taxonomy hint output."""

from __future__ import annotations

import pytest

from orchestrator.features.authoring.entity_taxonomy import (
    EntityTaxonomyHints,
    format_entity_taxonomy_markdown,
    parse_entity_taxonomy_hints,
)
from orchestrator.character_taxonomy import _parse_taxonomy_hints_from_markdown


def test_format_entity_taxonomy_markdown_complete():
    """Test formatting complete taxonomy hints to markdown."""
    hints = EntityTaxonomyHints(
        character_type_hint="human",
        morphology_hint="biped",
        scale_hint="human_scale",
        renderability_hint="renderable",
        confidence=0.9,
        direct_identity_evidence="explicitly called a human traveler",
        direct_visual_evidence="upright bipedal person",
        costume_or_covering_evidence="wears travel clothes",
        movement_evidence="walks upright",
        associated_entities=["rides a large animal", "carries a lantern"],
        alias_or_role_evidence="none",
        unknowns="exact age",
        source_refs=["CH001:P12"],
    )
    
    markdown = format_entity_taxonomy_markdown(hints)
    
    assert "# Entity Type Hints" in markdown
    assert "character_type: human" in markdown
    assert "morphology: biped" in markdown
    assert "scale: human_scale" in markdown
    assert "renderability: renderable" in markdown
    assert "confidence: 0.90" in markdown
    assert "## Direct Identity Evidence" in markdown
    assert "explicitly called a human traveler" in markdown
    assert "## Direct Visual Evidence" in markdown
    assert "upright bipedal person" in markdown
    assert "## Costume/Equipment" in markdown
    assert "wears travel clothes" in markdown
    assert "## Movement" in markdown
    assert "walks upright" in markdown
    assert "## Associated Entities" in markdown
    assert "rides a large animal" in markdown
    assert "carries a lantern" in markdown
    assert "## Alias/Role Evidence" in markdown
    assert "none" in markdown
    assert "## Unknowns" in markdown
    assert "exact age" in markdown
    assert "## Source References" in markdown
    assert "CH001:P12" in markdown


def test_format_entity_taxonomy_markdown_minimal():
    """Test formatting minimal taxonomy hints to markdown."""
    hints = EntityTaxonomyHints(
        character_type_hint="unknown",
        morphology_hint="unknown",
        scale_hint="unknown",
        renderability_hint="unknown",
        confidence=0.0,
    )
    
    markdown = format_entity_taxonomy_markdown(hints)
    
    assert "# Entity Type Hints" in markdown
    assert "character_type: unknown" in markdown
    assert "morphology: unknown" in markdown
    assert "scale: unknown" in markdown
    assert "renderability: unknown" in markdown
    assert "confidence: 0.00" in markdown
    # Should not include empty evidence sections
    assert "## Direct Identity Evidence" not in markdown
    assert "## Direct Visual Evidence" not in markdown


def test_parse_entity_taxonomy_hints_from_record_fields():
    """Test parsing taxonomy hints from record fields."""
    record_fields = {
        "character_type_hint": "human",
        "morphology_hint": "biped",
        "scale_hint": "human_scale",
        "renderability_hint": "renderable",
        "confidence": "0.85",
        "direct_identity_evidence": "explicitly called a human traveler",
        "direct_visual_evidence": "upright bipedal person",
        "costume_or_covering_evidence": "wears travel clothes",
        "movement_evidence": "walks upright",
        "associated_entities": "rides a large animal, carries a lantern",
        "alias_or_role_evidence": "none",
        "unknowns": "exact age",
        "source_refs": "CH001:P12, CH001:P15",
    }
    
    hints = parse_entity_taxonomy_hints(record_fields)
    
    assert hints.character_type_hint == "human"
    assert hints.morphology_hint == "biped"
    assert hints.scale_hint == "human_scale"
    assert hints.renderability_hint == "renderable"
    assert hints.confidence == 0.85
    assert hints.direct_identity_evidence == "explicitly called a human traveler"
    assert hints.direct_visual_evidence == "upright bipedal person"
    assert hints.costume_or_covering_evidence == "wears travel clothes"
    assert hints.movement_evidence == "walks upright"
    assert hints.associated_entities == ["rides a large animal", "carries a lantern"]
    assert hints.alias_or_role_evidence == "none"
    assert hints.unknowns == "exact age"
    assert hints.source_refs == ["CH001:P12", "CH001:P15"]


def test_parse_entity_taxonomy_hints_invalid_values():
    """Test parsing taxonomy hints with invalid enum values."""
    record_fields = {
        "character_type_hint": "invalid_type",
        "morphology_hint": "invalid_morph",
        "scale_hint": "invalid_scale",
        "renderability_hint": "invalid_render",
        "confidence": "invalid",
    }
    
    hints = parse_entity_taxonomy_hints(record_fields)
    
    assert hints.character_type_hint == "unknown"
    assert hints.morphology_hint == "unknown"
    assert hints.scale_hint == "unknown"
    assert hints.renderability_hint == "unknown"
    assert hints.confidence == 0.0


def test_parse_entity_taxonomy_hints_confidence_clamped():
    """Test that confidence is clamped to 0.0-1.0."""
    record_fields1 = {"confidence": "2.0"}
    hints1 = parse_entity_taxonomy_hints(record_fields1)
    assert hints1.confidence == 1.0
    
    record_fields2 = {"confidence": "-1.0"}
    hints2 = parse_entity_taxonomy_hints(record_fields2)
    assert hints2.confidence == 0.0


def test_roundtrip_format_and_parse():
    """Test that formatting and parsing are compatible."""
    original_hints = EntityTaxonomyHints(
        character_type_hint="humanoid_nonhuman",
        morphology_hint="biped",
        scale_hint="human_scale",
        renderability_hint="renderable",
        confidence=0.75,
        direct_identity_evidence="described as a green-skinned warrior",
        direct_visual_evidence="tall bipedal humanoid",
        costume_or_covering_evidence="wears leather harness",
        movement_evidence="walks and runs like a human",
        associated_entities=["rides a thoat"],
        alias_or_role_evidence="called a warrior",
        unknowns="exact height",
        source_refs=["CH002:P05"],
    )
    
    # Format to markdown
    markdown = format_entity_taxonomy_markdown(original_hints)
    
    # Parse back from markdown
    parsed = _parse_taxonomy_hints_from_markdown(markdown, "/test/path.md")
    
    assert parsed is not None
    assert parsed["character_type_hint"] == "humanoid_nonhuman"
    assert parsed["morphology_hint"] == "biped"
    assert parsed["scale_hint"] == "human_scale"
    assert parsed["renderability_hint"] == "renderable"
    assert parsed["confidence"] == 0.75
    assert parsed["direct_identity_evidence"] == "described as a green-skinned warrior"
    assert parsed["direct_visual_evidence"] == "tall bipedal humanoid"
    assert parsed["costume_or_covering_evidence"] == "wears leather harness"
    assert parsed["movement_evidence"] == "walks and runs like a human"
    assert parsed["associated_entities"] == ["rides a thoat"]
    assert parsed["alias_or_role_evidence"] == "called a warrior"
    assert parsed["unknowns"] == "exact height"
    assert parsed["source_refs"] == ["CH002:P05"]


def test_humanoid_rider_keeps_rider_separate_from_mount():
    """Test that a humanoid riding a mount keeps the rider separate."""
    hints = EntityTaxonomyHints(
        character_type_hint="humanoid_nonhuman",
        morphology_hint="biped",
        scale_hint="human_scale",
        renderability_hint="renderable",
        confidence=0.85,
        direct_identity_evidence="green-skinned warrior",
        direct_visual_evidence="tall bipedal humanoid",
        associated_entities=["rides an eight-legged thoat"],
    )
    
    markdown = format_entity_taxonomy_markdown(hints)
    
    # Rider type should be humanoid_nonhuman
    assert "character_type: humanoid_nonhuman" in markdown
    assert "morphology: biped" in markdown
    
    # Mount should be in associated entities, not direct evidence
    assert "## Associated Entities" in markdown
    assert "rides an eight-legged thoat" in markdown
    assert "eight-legged" not in markdown.split("## Associated Entities")[0]


def test_prose_only_markdown_returns_none():
    """Test that prose-only markdown returns None from parser."""
    prose_markdown = """# Character Breakdown

The traveler rides a huge beast and walks into town.
He appears to be a human warrior wearing exotic armor.
"""
    
    result = _parse_taxonomy_hints_from_markdown(prose_markdown, "/test/path.md")
    
    assert result is None


def test_taxonomy_hints_with_display_labels():
    """Test parsing taxonomy hints with display labels (without _hint suffix)."""
    markdown = """# Character Breakdown

- character_type: animal
- morphology: quadruped
- scale: large
- renderability: renderable
- confidence: 0.9
"""
    
    result = _parse_taxonomy_hints_from_markdown(markdown, "/test/path.md")
    
    assert result is not None
    assert result["character_type_hint"] == "animal"
    assert result["morphology_hint"] == "quadruped"
    assert result["scale_hint"] == "large"
    assert result["renderability_hint"] == "renderable"
    assert result["confidence"] == 0.9


def test_associated_entities_semicolon_separated():
    """Test that associated entities can be semicolon separated."""
    hints = EntityTaxonomyHints(
        character_type_hint="human",
        morphology_hint="biped",
        scale_hint="human_scale",
        renderability_hint="renderable",
        confidence=0.8,
        associated_entities=["rides a horse", "carries a sword", "wears a cloak"],
    )
    
    markdown = format_entity_taxonomy_markdown(hints)
    
    assert "## Associated Entities" in markdown
    assert "rides a horse" in markdown
    assert "carries a sword" in markdown
    assert "wears a cloak" in markdown


def test_unknown_with_explanation():
    """Test that unknown type includes explanation in unknowns field."""
    hints = EntityTaxonomyHints(
        character_type_hint="unknown",
        morphology_hint="unknown",
        scale_hint="unknown",
        renderability_hint="unknown",
        confidence=0.0,
        unknowns="Entity is only mentioned by name, no physical description provided",
    )
    
    markdown = format_entity_taxonomy_markdown(hints)
    
    assert "character_type: unknown" in markdown
    assert "## Unknowns" in markdown
    assert "Entity is only mentioned by name" in markdown


def test_group_entity_type():
    """Test that group entity type is supported."""
    hints = EntityTaxonomyHints(
        character_type_hint="group",
        morphology_hint="unknown",
        scale_hint="unknown",
        renderability_hint="renderable",
        confidence=1.0,
        direct_identity_evidence="described as a group of warriors",
    )
    
    markdown = format_entity_taxonomy_markdown(hints)
    
    assert "character_type: group" in markdown
    assert "## Direct Identity Evidence" in markdown
    assert "described as a group of warriors" in markdown


def test_context_only_renderability():
    """Test that context_only renderability is supported."""
    hints = EntityTaxonomyHints(
        character_type_hint="human",
        morphology_hint="biped",
        scale_hint="human_scale",
        renderability_hint="context_only",
        confidence=0.9,
        direct_identity_evidence="deceased character mentioned in dialogue",
    )
    
    markdown = format_entity_taxonomy_markdown(hints)
    
    assert "renderability: context_only" in markdown
    assert "deceased character mentioned in dialogue" in markdown


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
