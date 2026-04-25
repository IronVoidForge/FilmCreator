"""Tests for quality grading calibration."""

from pathlib import Path
from orchestrator.quality_grading import (
    _grader_prompt_package,
    _grader_dialogue,
    _has_prompt_semantic_issue,
    _is_silent_dialogue,
)


def test_prompt_with_missing_subject_anchor_not_grade_a():
    """Prompt with missing subject anchor should not grade A."""
    prompt_text = """# Character Prompt

## Review Notes
- Prompt body is missing the required subject anchor

## Positive Prompt
A scene with unknown character

## Negative Prompt
blurry, low quality

## Source Artifact IDs
- char_protagonist

## Reference Asset IDs
- ref_001
"""
    completeness, evidence, consistency, readiness, inference, notes = _grader_prompt_package(prompt_text)
    
    # Should detect the semantic issue
    has_issue, issues = _has_prompt_semantic_issue(prompt_text)
    assert has_issue
    assert any("missing the required subject anchor" in issue for issue in issues)
    assert "Prompt body is missing the required subject anchor" in notes


def test_prompt_readiness_76_cannot_grade_a():
    """Prompt with readiness 76 should not grade A."""
    # Create a prompt that will score around 76 in readiness
    prompt_text = """# Shot Prompt

## Positive Prompt
A basic scene

## Negative Prompt
blurry

## Notes
Some content but thin
"""
    completeness, evidence, consistency, readiness, inference, notes = _grader_prompt_package(prompt_text)
    
    # Readiness should be below 80
    assert readiness < 80, f"Expected readiness < 80, got {readiness}"


def test_prompt_with_image_contradiction_triggers_rerun():
    """Prompt with image1/environment contradiction should trigger rerun."""
    prompt_text = """# Environment Prompt

## Review Notes
- image1 subject contradicts visible primary subject

## Positive Prompt
A mountain landscape

## Negative Prompt
indoor, city

## Source Artifact IDs
- env_cave

## Reference Asset IDs
- ref_002
"""
    completeness, evidence, consistency, readiness, inference, notes = _grader_prompt_package(prompt_text)
    
    has_issue, issues = _has_prompt_semantic_issue(prompt_text)
    assert has_issue
    assert any("image1 subject contradicts" in issue for issue in issues)


def test_silent_dialogue_no_events_does_not_rerun():
    """Silent dialogue timeline with no events and no_dialogue_expected should not rerun."""
    payload = {
        "dialogue_events": [],
        "no_dialogue_expected": True,
        "chapter_id": "CH001",
        "scene_bindings": []
    }
    
    artifact_path = Path("test/DIALOGUE.json")
    completeness, evidence, consistency, readiness, inference, notes = _grader_dialogue(payload, artifact_path=artifact_path)
    
    # Should be marked as silent
    assert _is_silent_dialogue(payload)
    
    # Should not have "no dialogue events" in notes when silent
    assert "no dialogue events" not in notes


def test_empty_dialogue_without_silent_flag_reruns():
    """Empty dialogue timeline without silent flag should still rerun."""
    payload = {
        "dialogue_events": [],
        "chapter_id": "CH001",
        "scene_bindings": []
    }
    
    artifact_path = Path("test/DIALOGUE.json")
    completeness, evidence, consistency, readiness, inference, notes = _grader_dialogue(payload, artifact_path=artifact_path)
    
    # Should not be marked as silent
    assert not _is_silent_dialogue(payload)
    
    # Should have note about no dialogue events
    assert "no dialogue events" in notes


def test_prompt_missing_fallback_terms():
    """Prompt with missing fallback terms should be detected."""
    prompt_text = """# Shot Prompt

## Review Notes
- shot negatives are missing fallback terms

## Positive Prompt
Character in scene

## Negative Prompt
blurry

## Source Artifact IDs
- shot_001
"""
    has_issue, issues = _has_prompt_semantic_issue(prompt_text)
    assert has_issue
    assert any("missing fallback" in issue for issue in issues)


def test_environment_missing_descriptors():
    """Environment prompt missing key descriptors should be detected."""
    prompt_text = """# Environment Prompt

## Positive Prompt
A place with environment

## Negative Prompt
blurry

## Source Artifact IDs
- env_001
"""
    has_issue, issues = _has_prompt_semantic_issue(prompt_text)
    assert has_issue
    # Should detect missing architecture, lighting, mood, or scale
    assert any("environment prompt missing" in issue for issue in issues)


def test_character_missing_body_descriptor():
    """Character prompt missing body_descriptor should be detected."""
    prompt_text = """# Character Prompt

## Positive Prompt
A character in scene

## Negative Prompt
blurry

## Source Artifact IDs
- char_001
"""
    has_issue, issues = _has_prompt_semantic_issue(prompt_text)
    assert has_issue
    assert any("character prompt missing" in issue for issue in issues)


def test_silent_dialogue_with_metadata():
    """Silent dialogue can be marked in metadata."""
    payload = {
        "dialogue_events": [],
        "metadata": {
            "no_dialogue_expected": True
        },
        "chapter_id": "CH001"
    }
    
    assert _is_silent_dialogue(payload)


def test_reference_conflict_detected():
    """Reference conflict should be detected."""
    prompt_text = """# Prompt

## Review Notes
- reference conflict detected

## Positive Prompt
Scene content

## Source Artifact IDs
- ref_001
"""
    has_issue, issues = _has_prompt_semantic_issue(prompt_text)
    assert has_issue
    assert any("reference conflict" in issue for issue in issues)


def test_visible_subject_omitted():
    """Visible subject exists but positive prompt omits it."""
    prompt_text = """# Prompt

## Review Notes
- visible subject exists but positive prompt omits it

## Positive Prompt
A scene

## Source Artifact IDs
- ref_001
"""
    has_issue, issues = _has_prompt_semantic_issue(prompt_text)
    assert has_issue
    assert any("visible subject exists" in issue for issue in issues)
