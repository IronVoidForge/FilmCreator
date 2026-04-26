# Patch for descriptor_enrichment.py
# Add these functions after _coerce_string_list and before _character_specific_generated_default

def _looks_like_entity_association(text: str) -> bool:
    """Check if text looks like an entity/relationship reference rather than a wearable object."""
    import re
    normalized = text.strip().lower()
    if not normalized:
        return False
    
    # Patterns that indicate entity associations
    association_patterns = [
        r"\(nearby\)",
        r"\(near\)",
        r"\bnearby\b",
        r"\bnext to\b",
        r"\bstanding beside\b",
        r"\bassociated with\b",
        r"\baccompanied by\b",
        r"\bwith\s+[A-Z][a-z]+\b",  # "with PersonName"
        r"\bprotagonist\b",
        r"\bcharacter\b",
        r"\bcompanion\b",
    ]
    
    for pattern in association_patterns:
        if re.search(pattern, normalized):
            return True
    
    # Check if it looks like a character name (capitalized words that aren't common nouns)
    words = normalized.split()
    if len(words) <= 3:
        # Check if original has capital letters suggesting proper nouns
        original_words = text.strip().split()
        capitalized_count = sum(1 for w in original_words if w and w[0].isupper())
        if capitalized_count >= len(original_words) * 0.5 and len(original_words) > 1:
            # Likely a name, not an accessory
            return True
    
    return False


def _filter_entity_associations(values: list[str]) -> list[str]:
    """Remove entity/relationship references from accessory/costume lists."""
    filtered: list[str] = []
    for value in values:
        if not _looks_like_entity_association(value):
            filtered.append(value)
    return filtered


def _is_generic_group_filler(field_name: str, value: Any) -> bool:
    """Check if a field value is generic group filler without evidence."""
    import re
    if not isinstance(value, str):
        return False
    
    normalized = value.strip().lower()
    
    # Generic filler patterns for group descriptors
    generic_patterns = [
        r"varied\s+(hair|eye|face|skin)",
        r"group-consistent\s+",
        r"where\s+applicable",
        r"species-consistent",
        r"mixed\s+or\s+(minimal|unspecified)",
        r"across\s+the\s+group",
    ]
    
    for pattern in generic_patterns:
        if re.search(pattern, normalized):
            return True
    
    return False


def _should_suppress_group_field(field_name: str, value: Any, supported_values: dict[str, Any]) -> bool:
    """Determine if a group field should be suppressed due to lack of evidence."""
    # Fields that should only appear with evidence for groups
    evidence_required_fields = {
        "hair_color",
        "eye_color",
        "face_shape",
        "skin_tone",
        "facial_hair",
    }
    
    if field_name not in evidence_required_fields:
        return False
    
    # Check if there's evidence in supported values
    if field_name in supported_values:
        supported_value = supported_values.get(field_name)
        if supported_value and not _is_generic_group_filler(field_name, supported_value):
            return False
    
    # Check if the value itself is generic filler
    if _is_generic_group_filler(field_name, value):
        return True
    
    return False


# MODIFICATION TO _character_specific_generated_default:
# Replace the collective_group section with:
"""
    if profile_class == "collective_group":
        # For groups, prefer group-level fields over individual portrait fields
        collective_defaults = {
            "costume_materials": "repeatable martial fabrics, leathers, and gear materials",
            "posture": "disciplined group-ready posture",
            "expression_tendency": "alert, battle-ready expressions",
            "voice_or_presence_notes": "group presence reads as organized and formidable",
            "physical_build": "group silhouette emphasizes numbers and hardiness",
            "movement_language": "coordinated, military group movement",
            "sex": "mixed or unspecified group",
            "age_range": "adult fighting-age group",
        }
        if field_name in collective_defaults:
            return collective_defaults[field_name]
        # Suppress individual portrait fields for groups unless evidence-backed
        if field_name in {"height", "build", "skin_tone", "hair_color", "hair_style", "eye_color", "face_shape", "facial_hair"}:
            return None
"""

# MODIFICATION TO _sanitize_character_fields:
# Replace the entire function with:
"""
def _sanitize_character_fields(base_fields: dict[str, Any], field_origin: dict[str, str]) -> None:
    # Filter entity associations from accessory/costume fields
    accessory_fields = ["recurring_accessories", "costume_layers", "held_items"]
    for field_name in accessory_fields:
        if field_name in base_fields:
            raw_list = _coerce_string_list(base_fields.get(field_name, []))
            filtered = _filter_entity_associations(raw_list)
            if filtered:
                base_fields[field_name] = filtered
            else:
                base_fields.pop(field_name, None)
                field_origin.pop(field_name, None)
    
    # Standard list field cleaning
    for field_name in ["distinctive_features", "state_variants", "aliases"]:
        if field_name in base_fields:
            cleaned = _coerce_string_list(base_fields.get(field_name, []))
            if cleaned:
                base_fields[field_name] = cleaned
            else:
                base_fields.pop(field_name, None)
                field_origin.pop(field_name, None)

    for field_name in ["identity_baseline", "age_presence", "physical_build", "origin_or_historical_context", "movement_language", "costume_signature", "voice_or_presence_notes"]:
        if field_name in base_fields:
            cleaned = _clean_visual_summary(base_fields.get(field_name), fallback="")
            if cleaned:
                base_fields[field_name] = cleaned
            else:
                base_fields[field_name] = "unknown"
                field_origin[field_name] = "fallback"

    base_fields["silhouette_notes"] = _join_visual_fragments(
        base_fields.get("costume_signature", ""),
        base_fields.get("physical_build", ""),
        base_fields.get("identity_baseline", ""),
        fallback="unknown",
    )
    base_fields["physical_presence_notes"] = _join_visual_fragments(
        base_fields.get("identity_baseline", ""),
        base_fields.get("age_presence", ""),
        base_fields.get("physical_build", ""),
        base_fields.get("movement_language", ""),
        base_fields.get("voice_or_presence_notes", ""),
        fallback="unknown",
    )
"""

# ADD TO _base_character_descriptor after _sanitize_character_fields call:
"""
    # Suppress generic group filler for collective entities
    profile = _character_profile(base_fields, evidence_summary, char_id, bible.get("display_name") or entry.get("display_name") or char_id)
    if profile["is_collective"]:
        supported_values = {k: v for k, v in base_fields.items() if field_origin.get(k) in EXPLICIT_ORIGINS}
        fields_to_check = list(base_fields.keys())
        for field_name in fields_to_check:
            if _should_suppress_group_field(field_name, base_fields.get(field_name), supported_values):
                base_fields.pop(field_name, None)
                field_origin.pop(field_name, None)
                review_flags.append(f"suppressed_generic_group_filler_{field_name}")
"""
