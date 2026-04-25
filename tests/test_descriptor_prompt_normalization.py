"""
Test descriptor prompt normalization.

Validates that prompt preparation consumes descriptor fields in the correct precedence:
1. supported field values
2. reference_repair
3. generated field values
4. raw field values
5. fallback arguments
"""

import pytest


def test_repair_outranks_generic_generated():
    """Test that repair value outranks generic generated value."""
    from orchestrator.prompt_preparation import _prompt_field_text
    
    descriptor = {
        "supported_field_values": {},
        "generated_field_values": {
            "body_descriptor": "generic body"
        },
        "field_values": {}
    }
    
    repair = {
        "body_descriptor": "specific repaired body"
    }
    
    result = _prompt_field_text(descriptor, repair, "body_descriptor")
    
    assert result == "specific repaired body", f"Expected repair value, got: {result}"


def test_supported_outranks_repair():
    """Test that supported value outranks repair value."""
    from orchestrator.prompt_preparation import _prompt_field_text
    
    descriptor = {
        "supported_field_values": {
            "face_descriptor": "canon face from evidence"
        },
        "generated_field_values": {},
        "field_values": {}
    }
    
    repair = {
        "face_descriptor": "repaired face"
    }
    
    result = _prompt_field_text(descriptor, repair, "face_descriptor")
    
    assert result == "canon face from evidence", f"Expected supported value, got: {result}"


def test_fallback_fills_missing_generated_field_only():
    """Test that fallback fills a missing generated field only."""
    from orchestrator.prompt_preparation import _prompt_field_text
    
    descriptor = {
        "supported_field_values": {},
        "generated_field_values": {},
        "field_values": {}
    }
    
    repair = {}
    
    result = _prompt_field_text(descriptor, repair, "costume_descriptor", "fallback costume")
    
    assert result == "fallback costume", f"Expected fallback value, got: {result}"


def test_fallback_does_not_overwrite_supported_value():
    """Test that fallback does not overwrite supported value."""
    from orchestrator.prompt_preparation import _prompt_field_text
    
    descriptor = {
        "supported_field_values": {
            "posture_descriptor": "canon posture"
        },
        "generated_field_values": {},
        "field_values": {}
    }
    
    repair = {}
    
    result = _prompt_field_text(descriptor, repair, "posture_descriptor", "fallback posture")
    
    assert result == "canon posture", f"Expected supported value, got: {result}"


def test_generated_outranks_raw_field_values():
    """Test that generated value outranks raw field values."""
    from orchestrator.prompt_preparation import _prompt_field_text
    
    descriptor = {
        "supported_field_values": {},
        "generated_field_values": {
            "expression_descriptor": "generated expression"
        },
        "field_values": {
            "expression_descriptor": "raw expression"
        }
    }
    
    repair = {}
    
    result = _prompt_field_text(descriptor, repair, "expression_descriptor")
    
    assert result == "generated expression", f"Expected generated value, got: {result}"


def test_repair_outranks_raw_field_values():
    """Test that repair value outranks raw field values."""
    from orchestrator.prompt_preparation import _prompt_field_text
    
    descriptor = {
        "supported_field_values": {},
        "generated_field_values": {},
        "field_values": {
            "locked_fields": "raw locked"
        }
    }
    
    repair = {
        "locked_fields": "repaired locked"
    }
    
    result = _prompt_field_text(descriptor, repair, "locked_fields")
    
    assert result == "repaired locked", f"Expected repair value, got: {result}"


def test_full_precedence_chain():
    """Test the full precedence chain with all values present."""
    from orchestrator.prompt_preparation import _prompt_field_text
    
    descriptor = {
        "supported_field_values": {
            "identity_descriptor": "supported identity"
        },
        "generated_field_values": {
            "identity_descriptor": "generated identity"
        },
        "field_values": {
            "identity_descriptor": "raw identity"
        }
    }
    
    repair = {
        "identity_descriptor": "repaired identity"
    }
    
    result = _prompt_field_text(descriptor, repair, "identity_descriptor", "fallback identity")
    
    assert result == "supported identity", f"Expected supported value to win, got: {result}"


def test_repair_wins_when_no_supported():
    """Test that repair wins when supported is missing."""
    from orchestrator.prompt_preparation import _prompt_field_text
    
    descriptor = {
        "supported_field_values": {},
        "generated_field_values": {
            "source_visual_context": "generated context"
        },
        "field_values": {
            "source_visual_context": "raw context"
        }
    }
    
    repair = {
        "source_visual_context": "repaired context"
    }
    
    result = _prompt_field_text(descriptor, repair, "source_visual_context", "fallback context")
    
    assert result == "repaired context", f"Expected repair value to win, got: {result}"


def test_empty_descriptor_uses_fallback():
    """Test that empty descriptor uses fallback."""
    from orchestrator.prompt_preparation import _prompt_field_text
    
    descriptor = None
    repair = {}
    
    result = _prompt_field_text(descriptor, repair, "subject_visual_context", "fallback subject context")
    
    assert result == "fallback subject context", f"Expected fallback value, got: {result}"


def test_none_values_skip_to_next_precedence():
    """Test that None values skip to next precedence level."""
    from orchestrator.prompt_preparation import _prompt_field_text
    
    descriptor = {
        "supported_field_values": {
            "body_descriptor": None
        },
        "generated_field_values": {
            "body_descriptor": "generated body"
        },
        "field_values": {}
    }
    
    repair = {
        "body_descriptor": None
    }
    
    result = _prompt_field_text(descriptor, repair, "body_descriptor")
    
    assert result == "generated body", f"Expected generated value after None values, got: {result}"
