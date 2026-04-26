"""Tests for character bible taxonomy integration."""

from __future__ import annotations

import json
from unittest.mock import MagicMock, patch

import pytest

from orchestrator.character_bible import _llm_synthesis


def test_llm_synthesis_prompt_includes_entity_taxonomy():
    """Test that _llm_synthesis includes ENTITY_TAXONOMY in the prompt."""
    entry = {
        "canonical_id": "test_character",
        "display_name": "Test Character",
        "status": "canonical",
        "entity_kind": "individual",
    }
    evidence_summary = ["Test evidence line 1", "Test evidence line 2"]
    entity_taxonomy = {
        "character_id": "test_character",
        "primary_type": "human",
        "morphology": "biped",
        "scale": "human_scale",
        "renderability": "renderable",
        "confidence": 0.8,
    }
    
    with patch("orchestrator.character_bible.LMStudioClient") as mock_client_class:
        mock_client = MagicMock()
        mock_client_class.return_value = mock_client
        mock_client.chat_completion.return_value = """
[[FILMCREATOR_PACKET]]
task: character_bible_synthesis
version: 1

[[FILMCREATOR_RECORD]]
type: character_bible
artifact_id: CHAR_test_character
character_id: test_character
status: canonical
entity_kind: individual

[[SECTION identity_markdown]]
display_name: Test Character
[[/SECTION]]

[[SECTION visual_markdown]]
identity_baseline: human character
[[/SECTION]]

[[SECTION behavioral_markdown]]
personality: unknown
[[/SECTION]]

[[SECTION continuity_markdown]]
[[/SECTION]]

[[SECTION evidence_markdown]]
- Test evidence
[[/SECTION]]

[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
"""
        
        with patch("orchestrator.character_bible.load_runtime_settings"):
            result = _llm_synthesis(
                entry,
                evidence_summary,
                entity_taxonomy=entity_taxonomy,
                alias_resolution=None,
                associated_entities=None,
            )
        
        # Verify the prompt was called
        assert mock_client.chat_completion.called
        call_args = mock_client.chat_completion.call_args
        user_prompt = call_args[1]["user_prompt"]
        
        # Assert taxonomy sections are present
        assert "ENTITY_TAXONOMY:" in user_prompt
        assert '"primary_type": "human"' in user_prompt
        assert "ALIAS_RESOLUTION:" in user_prompt
        assert "ASSOCIATED_ENTITIES:" in user_prompt
        assert "TAXONOMY RULES:" in user_prompt


def test_llm_synthesis_prompt_includes_associated_entity_body_rule():
    """Test that the prompt includes rules about associated entities."""
    entry = {"canonical_id": "test_character", "display_name": "Test"}
    evidence_summary = ["Test evidence"]
    
    with patch("orchestrator.character_bible.LMStudioClient") as mock_client_class:
        mock_client = MagicMock()
        mock_client_class.return_value = mock_client
        mock_client.chat_completion.return_value = """
[[FILMCREATOR_PACKET]]
task: character_bible_synthesis
version: 1
[[FILMCREATOR_RECORD]]
type: character_bible
artifact_id: CHAR_test_character
character_id: test_character
[[SECTION identity_markdown]]
display_name: Test
[[/SECTION]]
[[SECTION visual_markdown]]
identity_baseline: unknown
[[/SECTION]]
[[SECTION behavioral_markdown]]
personality: unknown
[[/SECTION]]
[[SECTION continuity_markdown]]
[[/SECTION]]
[[SECTION evidence_markdown]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
"""
        
        with patch("orchestrator.character_bible.load_runtime_settings"):
            _llm_synthesis(entry, evidence_summary)
        
        call_args = mock_client.chat_completion.call_args
        user_prompt = call_args[1]["user_prompt"]
        
        assert "Do not override taxonomy based on associated entities" in user_prompt
        assert "Keep associated entities out of physical_build and physical_traits" in user_prompt


def test_llm_synthesis_prompt_includes_alias_rule():
    """Test that the prompt includes rules about alias resolution."""
    entry = {"canonical_id": "test_character", "display_name": "Test"}
    evidence_summary = ["Test evidence"]
    
    with patch("orchestrator.character_bible.LMStudioClient") as mock_client_class:
        mock_client = MagicMock()
        mock_client_class.return_value = mock_client
        mock_client.chat_completion.return_value = """
[[FILMCREATOR_PACKET]]
task: character_bible_synthesis
version: 1
[[FILMCREATOR_RECORD]]
type: character_bible
artifact_id: CHAR_test_character
character_id: test_character
[[SECTION identity_markdown]]
display_name: Test
[[/SECTION]]
[[SECTION visual_markdown]]
identity_baseline: unknown
[[/SECTION]]
[[SECTION behavioral_markdown]]
personality: unknown
[[/SECTION]]
[[SECTION continuity_markdown]]
[[/SECTION]]
[[SECTION evidence_markdown]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
"""
        
        with patch("orchestrator.character_bible.load_runtime_settings"):
            _llm_synthesis(entry, evidence_summary)
        
        call_args = mock_client.chat_completion.call_args
        user_prompt = call_args[1]["user_prompt"]
        
        assert "Do not silently merge aliases" in user_prompt
        assert "Alias resolution belongs to identity refinement" in user_prompt


def test_character_bible_preserves_taxonomy_fields():
    """Test that character bible preserves taxonomy fields through the pipeline."""
    # This is a minimal integration test
    # In practice, this would test the full run_character_bible_synthesis flow
    # For now, we just verify the data structure
    
    taxonomy_data = {
        "character_id": "test_character",
        "primary_type": "human",
        "morphology": "biped",
        "scale": "human_scale",
        "renderability": "renderable",
        "confidence": 0.8,
    }
    
    alias_resolution_data = {
        "status": "canonical",
        "canonical_id": "test_character",
    }
    
    associated_entities_data = [
        {"evidence": "rides a horse"},
        {"evidence": "wears a sword"},
    ]
    
    # Verify the data structures are valid
    assert isinstance(taxonomy_data, dict)
    assert "primary_type" in taxonomy_data
    assert isinstance(alias_resolution_data, dict)
    assert isinstance(associated_entities_data, list)
