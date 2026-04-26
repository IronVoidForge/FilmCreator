"""Tests for chapter entity extraction schema and taxonomy hints."""

import pytest

from orchestrator.features.authoring.entity_taxonomy import (
    EntityTaxonomyHints,
    parse_entity_taxonomy_hints,
    format_entity_taxonomy_markdown,
    VALID_CHARACTER_TYPE_HINTS,
    VALID_MORPHOLOGY_HINTS,
    VALID_SCALE_HINTS,
    VALID_RENDERABILITY_HINTS,
)


class TestEntityTaxonomyParsing:
    """Test parsing of entity taxonomy hints from record fields."""

    def test_parse_complete_hints(self):
        """Test parsing a complete set of entity taxonomy hints."""
        record_fields = {
            "character_type_hint": "human",
            "morphology_hint": "biped",
            "scale_hint": "human_scale",
            "renderability_hint": "renderable",
            "confidence": "0.85",
            "direct_identity_evidence": "described as a man",
            "direct_visual_evidence": "tall, muscular build",
            "costume_or_covering_evidence": "wearing leather armor",
            "movement_evidence": "walks upright",
            "associated_entities": "mount, sword",
            "alias_or_role_evidence": "called 'the captain'",
            "unknowns": "",
            "source_refs": "CH001_para_5, CH001_para_12",
        }
        
        hints = parse_entity_taxonomy_hints(record_fields)
        
        assert hints.character_type_hint == "human"
        assert hints.morphology_hint == "biped"
        assert hints.scale_hint == "human_scale"
        assert hints.renderability_hint == "renderable"
        assert hints.confidence == 0.85
        assert hints.direct_identity_evidence == "described as a man"
        assert hints.direct_visual_evidence == "tall, muscular build"
        assert hints.costume_or_covering_evidence == "wearing leather armor"
        assert hints.movement_evidence == "walks upright"
        assert hints.associated_entities == ["mount", "sword"]
        assert hints.alias_or_role_evidence == "called 'the captain'"
        assert hints.unknowns == ""
        assert hints.source_refs == ["CH001_para_5", "CH001_para_12"]

    def test_parse_missing_fields_defaults_to_unknown(self):
        """Test that missing fields default to unknown/empty."""
        record_fields = {}
        
        hints = parse_entity_taxonomy_hints(record_fields)
        
        assert hints.character_type_hint == "unknown"
        assert hints.morphology_hint == "unknown"
        assert hints.scale_hint == "unknown"
        assert hints.renderability_hint == "unknown"
        assert hints.confidence == 0.0
        assert hints.direct_identity_evidence == ""
        assert hints.associated_entities == []
        assert hints.source_refs == []

    def test_parse_invalid_hint_values_default_to_unknown(self):
        """Test that invalid hint values default to unknown."""
        record_fields = {
            "character_type_hint": "invalid_type",
            "morphology_hint": "invalid_morph",
            "scale_hint": "invalid_scale",
            "renderability_hint": "invalid_render",
        }
        
        hints = parse_entity_taxonomy_hints(record_fields)
        
        assert hints.character_type_hint == "unknown"
        assert hints.morphology_hint == "unknown"
        assert hints.scale_hint == "unknown"
        assert hints.renderability_hint == "unknown"

    def test_parse_confidence_clamped_to_range(self):
        """Test that confidence is clamped to [0.0, 1.0]."""
        record_fields_high = {"confidence": "1.5"}
        record_fields_low = {"confidence": "-0.3"}
        record_fields_invalid = {"confidence": "not_a_number"}
        
        hints_high = parse_entity_taxonomy_hints(record_fields_high)
        hints_low = parse_entity_taxonomy_hints(record_fields_low)
        hints_invalid = parse_entity_taxonomy_hints(record_fields_invalid)
        
        assert hints_high.confidence == 1.0
        assert hints_low.confidence == 0.0
        assert hints_invalid.confidence == 0.0

    def test_parse_associated_entities_list(self):
        """Test parsing comma-separated associated entities."""
        record_fields = {
            "associated_entities": "mount, weapon, companion",
        }
        
        hints = parse_entity_taxonomy_hints(record_fields)
        
        assert hints.associated_entities == ["mount", "weapon", "companion"]

    def test_parse_empty_associated_entities(self):
        """Test parsing empty associated entities."""
        record_fields = {
            "associated_entities": "",
        }
        
        hints = parse_entity_taxonomy_hints(record_fields)
        
        assert hints.associated_entities == []


class TestRiderMountSeparation:
    """Test that riders and mounts are classified separately."""

    def test_rider_is_not_quadruped(self):
        """Test that a rider is not classified as quadruped even if they ride a mount."""
        # Simulating extraction where the leader is mentioned with a mount
        leader_fields = {
            "asset_id": "leader",
            "character_type_hint": "humanoid_nonhuman",
            "morphology_hint": "biped",
            "scale_hint": "human_scale",
            "renderability_hint": "renderable",
            "confidence": "0.7",
            "direct_identity_evidence": "described as the leader",
            "associated_entities": "eight_legged_mount",
        }
        
        mount_fields = {
            "asset_id": "eight_legged_mount",
            "character_type_hint": "animal",
            "morphology_hint": "multi_legged",
            "scale_hint": "large",
            "renderability_hint": "renderable",
            "confidence": "0.8",
            "direct_visual_evidence": "eight-legged mount",
        }
        
        leader_hints = parse_entity_taxonomy_hints(leader_fields)
        mount_hints = parse_entity_taxonomy_hints(mount_fields)
        
        # Leader should be biped, not affected by mount
        assert leader_hints.morphology_hint == "biped"
        assert leader_hints.character_type_hint in {"humanoid_nonhuman", "human", "unknown"}
        assert "eight_legged_mount" in leader_hints.associated_entities
        
        # Mount should be multi_legged animal
        assert mount_hints.morphology_hint == "multi_legged"
        assert mount_hints.character_type_hint == "animal"


class TestHumanWearingExoticClothing:
    """Test that clothing doesn't change species classification."""

    def test_human_with_exotic_clothing_remains_human(self):
        """Test that a human wearing exotic clothing is still classified as human."""
        record_fields = {
            "character_type_hint": "human",
            "morphology_hint": "biped",
            "scale_hint": "human_scale",
            "renderability_hint": "renderable",
            "confidence": "0.9",
            "direct_identity_evidence": "described as a man",
            "costume_or_covering_evidence": "wearing exotic alien robes and ornate headpiece",
        }
        
        hints = parse_entity_taxonomy_hints(record_fields)
        
        assert hints.character_type_hint == "human"
        assert hints.morphology_hint == "biped"
        assert "exotic alien robes" in hints.costume_or_covering_evidence


class TestGroupOfWarriors:
    """Test that groups are classified correctly."""

    def test_group_entity_classification(self):
        """Test that a group of warriors is classified as group."""
        record_fields = {
            "character_type_hint": "group",
            "morphology_hint": "unknown",
            "scale_hint": "unknown",
            "renderability_hint": "context_only",
            "confidence": "0.6",
            "direct_identity_evidence": "a group of warriors",
        }
        
        hints = parse_entity_taxonomy_hints(record_fields)
        
        assert hints.character_type_hint == "group"
        assert hints.renderability_hint == "context_only"


class TestAnimalMount:
    """Test that animal mounts are classified correctly."""

    def test_animal_mount_classification(self):
        """Test that an animal mount is classified as animal/creature with appropriate morphology."""
        record_fields = {
            "character_type_hint": "animal",
            "morphology_hint": "quadruped",
            "scale_hint": "large",
            "renderability_hint": "renderable",
            "confidence": "0.85",
            "direct_visual_evidence": "large four-legged beast",
        }
        
        hints = parse_entity_taxonomy_hints(record_fields)
        
        assert hints.character_type_hint == "animal"
        assert hints.morphology_hint == "quadruped"
        assert hints.scale_hint == "large"


class TestRoleLabel:
    """Test that role labels are captured correctly."""

    def test_role_label_as_alias_candidate(self):
        """Test that role labels are captured in alias_or_role_evidence."""
        record_fields = {
            "character_type_hint": "unknown",
            "morphology_hint": "unknown",
            "scale_hint": "unknown",
            "renderability_hint": "alias_or_role",
            "confidence": "0.3",
            "alias_or_role_evidence": "referred to as 'the captain' but no physical description",
        }
        
        hints = parse_entity_taxonomy_hints(record_fields)
        
        assert hints.renderability_hint == "alias_or_role"
        assert "the captain" in hints.alias_or_role_evidence


class TestUnknownEntity:
    """Test that unknown entities are handled correctly."""

    def test_unknown_entity_with_explanation(self):
        """Test that unknown entities have confidence and explanation."""
        record_fields = {
            "character_type_hint": "unknown",
            "morphology_hint": "unknown",
            "scale_hint": "unknown",
            "renderability_hint": "unknown",
            "confidence": "0.2",
            "unknowns": "No physical description provided; only mentioned by name",
        }
        
        hints = parse_entity_taxonomy_hints(record_fields)
        
        assert hints.character_type_hint == "unknown"
        assert hints.confidence == 0.2
        assert "No physical description" in hints.unknowns


class TestMarkdownFormatting:
    """Test markdown formatting of entity taxonomy hints."""

    def test_format_complete_hints(self):
        """Test formatting complete hints to markdown."""
        hints = EntityTaxonomyHints(
            character_type_hint="human",
            morphology_hint="biped",
            scale_hint="human_scale",
            renderability_hint="renderable",
            confidence=0.85,
            direct_identity_evidence="described as a man",
            direct_visual_evidence="tall, muscular",
            costume_or_covering_evidence="leather armor",
            movement_evidence="walks upright",
            associated_entities=["mount", "sword"],
            alias_or_role_evidence="called 'captain'",
            unknowns="",
            source_refs=["CH001_para_5"],
        )
        
        markdown = format_entity_taxonomy_markdown(hints)
        
        assert "# Entity Type Hints" in markdown
        assert "character_type: human" in markdown
        assert "morphology: biped" in markdown
        assert "confidence: 0.85" in markdown
        assert "## Direct Identity Evidence" in markdown
        assert "## Associated Entities" in markdown
        assert "mount, sword" in markdown

    def test_format_minimal_hints(self):
        """Test formatting minimal hints to markdown."""
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
        assert "confidence: 0.00" in markdown
        # Should not include empty sections
        assert "## Direct Identity Evidence" not in markdown
        assert "## Associated Entities" not in markdown


class TestValidHintSets:
    """Test that valid hint sets are properly defined."""

    def test_character_type_hints_are_book_agnostic(self):
        """Test that character type hints don't include book-specific values."""
        forbidden_terms = {"john_carter", "barsoom", "green_martian", "princess_of_mars"}
        
        for hint in VALID_CHARACTER_TYPE_HINTS:
            assert not any(term in hint.lower() for term in forbidden_terms)

    def test_morphology_hints_are_book_agnostic(self):
        """Test that morphology hints don't include book-specific values."""
        forbidden_terms = {"john_carter", "barsoom", "green_martian", "thoat"}
        
        for hint in VALID_MORPHOLOGY_HINTS:
            assert not any(term in hint.lower() for term in forbidden_terms)

    def test_all_hint_sets_include_unknown(self):
        """Test that all hint sets include 'unknown' as a fallback."""
        assert "unknown" in VALID_CHARACTER_TYPE_HINTS
        assert "unknown" in VALID_MORPHOLOGY_HINTS
        assert "unknown" in VALID_SCALE_HINTS
        assert "unknown" in VALID_RENDERABILITY_HINTS
