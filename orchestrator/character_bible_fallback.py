"""Character bible visual production fallback helpers."""
from typing import Any


def is_unknownish(value: Any) -> bool:
    """Check if a value is unknown, empty, or placeholder-like."""
    if value is None:
        return True
    if isinstance(value, str):
        normalized = value.strip().lower()
        return not normalized or normalized in {"unknown", "none", "(none)", "n/a", "insufficient evidence", "no data available"}
    if isinstance(value, list):
        return not any(str(item).strip() for item in value)
    return False


def needs_visual_production_fallback(bible_data: dict[str, Any]) -> bool:
    """Determine if a character bible needs visual production fallback."""
    critical_visual_fields = [
        "identity_baseline",
        "physical_build",
        "costume_signature",
        "stable_visual_summary",
    ]
    unknown_count = sum(1 for field in critical_visual_fields if is_unknownish(bible_data.get(field)))
    return unknown_count >= 2


def fallback_bucket_for_character(entry: dict[str, Any], bible_data: dict[str, Any], evidence_summary: list[str]) -> str:
    """Determine the fallback bucket for a character based on entity kind and evidence."""
    entity_kind = str(entry.get("entity_kind", "individual")).strip().lower()
    
    if entity_kind in {"memory", "reference", "deceased", "abstract"}:
        return "context_only"
    
    evidence_text = " ".join(evidence_summary).lower()
    if any(marker in evidence_text for marker in ["dead", "deceased", "corpse", "body", "former", "memory of", "mentioned only"]):
        return "context_only"
    
    if entity_kind in {"group", "collective", "horde"}:
        return "group_or_horde"
    
    if any(marker in evidence_text for marker in ["creature", "beast", "animal", "calot", "thoat", "ape"]):
        return "creature_or_primitive"
    
    if any(marker in evidence_text for marker in ["martian", "thark", "green", "red martian", "barsoom", "helium"]):
        return "barsoom_humanoid"
    
    if any(marker in evidence_text for marker in ["human", "earthling", "american", "confederate", "frontier", "cavalry"]):
        return "earth_human"
    
    if not evidence_summary or len(evidence_summary) < 2:
        return "unknown_reference"
    
    return "barsoom_humanoid"


def deterministic_visual_fallback(entry: dict[str, Any], bible_data: dict[str, Any], evidence_summary: list[str]) -> dict[str, Any]:
    """Generate deterministic visual production fallback when canon evidence is thin."""
    fallback_bucket = fallback_bucket_for_character(entry, bible_data, evidence_summary)
    
    if fallback_bucket == "context_only":
        return {
            "status": "context_only",
            "fallback_bucket": fallback_bucket,
            "production_identity_descriptor": "narrative reference only; not visually rendered",
            "production_body_descriptor": "not applicable",
            "production_face_descriptor": "not applicable",
            "production_costume_descriptor": "not applicable",
            "production_silhouette": "not applicable",
            "production_movement_descriptor": "not applicable",
            "production_state_variants": [],
            "negative_terms": [],
            "provisionality_note": "Entity is a narrative reference only and should not be visually rendered.",
        }
    
    bucket_defaults = {
        "earth_human": {
            "production_identity_descriptor": "frontier-era human with practical field clothing",
            "production_body_descriptor": "lean athletic human build, weathered and capable",
            "production_face_descriptor": "angular weathered face with steady eyes",
            "production_costume_descriptor": "worn cloth, leather, and practical frontier materials",
            "production_silhouette": "upright human silhouette with frontier gear",
            "production_movement_descriptor": "economical military movement with confident balance",
            "production_state_variants": ["armed", "field-ready"],
            "negative_terms": ["ornate", "ceremonial", "alien anatomy"],
        },
        "barsoom_humanoid": {
            "production_identity_descriptor": "Martian humanoid with species-appropriate anatomy",
            "production_body_descriptor": "tall humanoid build adapted to Martian gravity",
            "production_face_descriptor": "humanoid facial structure with Martian features",
            "production_costume_descriptor": "minimal Martian harness, leather, and metal fittings",
            "production_silhouette": "tall humanoid silhouette with Martian proportions",
            "production_movement_descriptor": "fluid movement adapted to low gravity",
            "production_state_variants": ["armed", "battle-ready"],
            "negative_terms": ["Earth clothing", "heavy armor", "human proportions"],
        },
        "creature_or_primitive": {
            "production_identity_descriptor": "non-human creature with bestial anatomy",
            "production_body_descriptor": "powerful animal build with species-specific musculature",
            "production_face_descriptor": "animal skull structure with predatory features",
            "production_costume_descriptor": "natural hide or minimal harness",
            "production_silhouette": "bestial silhouette with non-human proportions",
            "production_movement_descriptor": "animal movement with sudden bursts of force",
            "production_state_variants": ["alert", "aggressive"],
            "negative_terms": ["human anatomy", "clothing", "upright posture"],
        },
        "group_or_horde": {
            "production_identity_descriptor": "collective group with unified visual identity",
            "production_body_descriptor": "varied builds within group-consistent parameters",
            "production_face_descriptor": "varied faces within species-consistent range",
            "production_costume_descriptor": "repeatable group uniform or martial gear",
            "production_silhouette": "group silhouette emphasizing numbers and cohesion",
            "production_movement_descriptor": "coordinated group movement",
            "production_state_variants": ["formation", "dispersed"],
            "negative_terms": ["singular", "individual portrait"],
        },
        "unknown_reference": {
            "production_identity_descriptor": "insufficient canon evidence for stable visual identity",
            "production_body_descriptor": "unknown",
            "production_face_descriptor": "unknown",
            "production_costume_descriptor": "unknown",
            "production_silhouette": "unknown",
            "production_movement_descriptor": "unknown",
            "production_state_variants": [],
            "negative_terms": [],
        },
    }
    
    defaults = bucket_defaults.get(fallback_bucket, bucket_defaults["unknown_reference"])
    
    return {
        "status": "generated" if fallback_bucket != "unknown_reference" else "insufficient_context",
        "fallback_bucket": fallback_bucket,
        "production_identity_descriptor": defaults["production_identity_descriptor"],
        "production_body_descriptor": defaults["production_body_descriptor"],
        "production_face_descriptor": defaults["production_face_descriptor"],
        "production_costume_descriptor": defaults["production_costume_descriptor"],
        "production_silhouette": defaults["production_silhouette"],
        "production_movement_descriptor": defaults["production_movement_descriptor"],
        "production_state_variants": defaults["production_state_variants"],
        "negative_terms": defaults["negative_terms"],
        "provisionality_note": "Generated for visual production because strict canon evidence is thin; not strict canon.",
    }
