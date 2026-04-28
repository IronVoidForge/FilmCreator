"""
Test prompt preparation visual fallback injection and shot role mapping.
"""
from orchestrator.visual_fallbacks import (
    default_visual_fallbacks,
    select_environment_fallback_bucket,
    fallback_text,
    _derive_book_visual_context,
)


def test_environment_fallback_bucket_cave():
    """Test that arizona_mountain_cave selects cave_or_cliffside bucket."""
    bucket = select_environment_fallback_bucket("arizona_mountain_cave")
    assert bucket == "cave_or_cliffside", f"Expected cave_or_cliffside, got {bucket}"


def test_cave_fallback_text_includes_cave_geometry():
    """Test that cave fallback text includes cave/cliff/threshold language."""
    fallbacks = default_visual_fallbacks(project_slug="test")
    text = fallback_text(fallbacks, "environment", "cave_or_cliffside")
    
    assert text, "Cave fallback text should not be empty"
    
    text_lower = text.lower()
    cave_terms = ["cave", "cliff", "threshold", "shadowed", "weathered stone", "entrance"]
    found_terms = [term for term in cave_terms if term in text_lower]
    
    assert len(found_terms) >= 3, f"Expected at least 3 cave terms, found: {found_terms}"


def test_shot_role_mapping_protagonist_and_environment():
    """Test that shot role mapping produces correct image1/image2 assignments."""
    from orchestrator.prompt_preparation import _asset_role_label
    
    visible_primary_subject_id = "protagonist"
    environment_canonical_id = "arizona_mountain_cave"
    
    reference_role_candidates = []
    if visible_primary_subject_id:
        reference_role_candidates.append((
            "identity reference for the primary visible subject",
            _asset_role_label(visible_primary_subject_id)
        ))
    if environment_canonical_id:
        reference_role_candidates.append((
            "environment reference for the scene location",
            _asset_role_label(environment_canonical_id)
        ))
    
    reference_roles = [
        (f"image{index}", role_text, asset_label)
        for index, (role_text, asset_label) in enumerate(reference_role_candidates[:4], start=1)
    ]
    
    assert len(reference_roles) == 2, f"Expected 2 reference roles, got {len(reference_roles)}"
    
    image1_key, image1_role, image1_asset = reference_roles[0]
    image2_key, image2_role, image2_asset = reference_roles[1]
    
    assert image1_key == "image1", f"Expected image1, got {image1_key}"
    assert image1_asset == "protagonist", f"Expected protagonist, got {image1_asset}"
    
    assert image2_key == "image2", f"Expected image2, got {image2_key}"
    assert image2_asset == "arizona mountain cave", f"Expected arizona mountain cave, got {image2_asset}"


def test_shot_role_mapping_does_not_swap_subject_and_environment():
    """Test that environment is never described as image1 subject."""
    from orchestrator.prompt_preparation import _asset_role_label
    
    visible_primary_subject_id = "protagonist"
    environment_canonical_id = "arizona_mountain_cave"
    
    reference_role_candidates = []
    if visible_primary_subject_id:
        reference_role_candidates.append((
            "identity reference for the primary visible subject",
            _asset_role_label(visible_primary_subject_id)
        ))
    if environment_canonical_id:
        reference_role_candidates.append((
            "environment reference for the scene location",
            _asset_role_label(environment_canonical_id)
        ))
    
    reference_roles = [
        (f"image{index}", role_text, asset_label)
        for index, (role_text, asset_label) in enumerate(reference_role_candidates[:4], start=1)
    ]
    
    for image_key, role_text, asset_label in reference_roles:
        if image_key == "image1":
            assert "protagonist" in asset_label.lower(), \
                f"image1 should reference protagonist, not {asset_label}"
            assert "cave" not in asset_label.lower(), \
                f"image1 should not reference environment: {asset_label}"
        if image_key == "image2":
            assert "cave" in asset_label.lower() or "arizona" in asset_label.lower(), \
                f"image2 should reference environment, got {asset_label}"


def test_shot_negative_prompt_merges_character_and_environment_negatives():
    """Test that shot negatives include generic, character, and environment terms."""
    from orchestrator.prompt_preparation import _prompt_negative_prompt, GENERIC_NEGATIVE_PROMPT
    from orchestrator.visual_fallbacks import character_negative_terms, environment_negative_terms
    
    fallbacks = default_visual_fallbacks(project_slug="test")
    
    character_negatives = character_negative_terms(fallbacks)
    environment_negatives = environment_negative_terms(fallbacks)
    
    shot_negative_terms = []
    shot_negative_terms.extend(character_negatives)
    shot_negative_terms.extend(environment_negatives)
    
    shot_negative_prompt = _prompt_negative_prompt(*shot_negative_terms)
    
    assert shot_negative_prompt, "Shot negative prompt should not be empty"
    
    prompt_lower = shot_negative_prompt.lower()
    
    assert "text" in prompt_lower or "watermark" in prompt_lower, \
        "Should include generic negatives"
    
    assert any(term.lower() in prompt_lower for term in character_negatives[:3]), \
        f"Should include character negatives from {character_negatives[:3]}"
    
    assert any(term.lower() in prompt_lower for term in environment_negatives[:3]), \
        f"Should include environment negatives from {environment_negatives[:3]}"


def test_environment_fallback_bucket_desert_mountain():
    """Test that desert/mountain environments select desert_mountain bucket."""
    bucket = select_environment_fallback_bucket("arizona desert mountain")
    assert bucket == "desert_mountain", f"Expected desert_mountain, got {bucket}"


def test_environment_fallback_bucket_interior():
    """Test that interior environments select interior bucket."""
    bucket = select_environment_fallback_bucket("palace chamber interior")
    assert bucket == "interior", f"Expected interior, got {bucket}"


def test_cave_fallback_not_injected_into_non_cave():
    """Test that cave language is not injected into non-cave environments."""
    fallbacks = default_visual_fallbacks(project_slug="test")
    
    desert_bucket = select_environment_fallback_bucket("arizona desert")
    desert_text = fallback_text(fallbacks, "environment", desert_bucket)
    
    assert "cave" not in desert_text.lower(), \
        f"Desert fallback should not contain cave language: {desert_text}"
    
    interior_bucket = select_environment_fallback_bucket("palace interior")
    interior_text = fallback_text(fallbacks, "environment", interior_bucket)
    
    assert "cave" not in interior_text.lower(), \
        f"Interior fallback should not contain cave language: {interior_text}"


def test_book_visual_context_stays_book_agnostic_for_desert_like_digest():
    context = {
        "context_digest": "desert cave cliff terrain with warriors and a remote wilderness approach",
    }

    derived = _derive_book_visual_context(context).lower()

    assert "frontier" not in derived
    assert "arizona" not in derived
    assert "martian" not in derived
