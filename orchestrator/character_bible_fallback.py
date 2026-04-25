"""Character bible visual production fallback helpers."""
from typing import Any


PROMPT_CRITICAL_VISUAL_FIELDS = [
    "identity_baseline",
    "age_presence",
    "physical_build",
    "origin_or_historical_context",
    "movement_language",
    "stable_visual_summary",
    "physical_traits",
    "costume_signature",
    "distinguishing_features",
    "state_variants",
]

PRODUCTION_FALLBACK_FIELDS = [
    "production_identity_descriptor",
    "production_body_descriptor",
    "production_face_descriptor",
    "production_costume_descriptor",
    "production_silhouette",
    "production_movement_descriptor",
    "production_state_variants",
    "negative_terms",
]


def is_unknownish(value: Any) -> bool:
    """Check if a value is unknown, empty, or placeholder-like."""
    if value is None:
        return True
    if isinstance(value, str):
        normalized = value.strip().lower()
        normalized = normalized.strip(".,:;-_ ")
        if not normalized:
            return True
        if normalized in {
            "unknown",
            "unknown.",
            "none",
            "(none)",
            "n/a",
            "na",
            "null",
            "[]",
            "[ ]",
            "insufficient evidence",
            "no data available",
            "not specified",
            "unspecified",
            "not applicable",
        }:
            return True
        if normalized in {"['unknown']", "['[]']"}:
            return True
        return False
    if isinstance(value, list):
        if not value:
            return True
        return not any(not is_unknownish(item) for item in value)
    if isinstance(value, dict):
        return not any(not is_unknownish(item) for item in value.values())
    return False


def visual_field_audit(bible_data: dict[str, Any]) -> dict[str, Any]:
    """Audit visual fields to determine which are missing."""
    missing_fields = [
        field for field in PROMPT_CRITICAL_VISUAL_FIELDS
        if is_unknownish(bible_data.get(field))
    ]
    present_fields = [
        field for field in PROMPT_CRITICAL_VISUAL_FIELDS
        if field not in missing_fields
    ]
    return {
        "total_prompt_critical_fields": len(PROMPT_CRITICAL_VISUAL_FIELDS),
        "missing_count": len(missing_fields),
        "present_count": len(present_fields),
        "missing_fields": missing_fields,
        "present_fields": present_fields,
        "needs_visual_production_fallback": bool(missing_fields),
    }


def needs_visual_production_fallback(bible_data: dict[str, Any]) -> bool:
    """Determine if a character bible needs visual production fallback."""
    return visual_field_audit(bible_data)["needs_visual_production_fallback"]


def fallback_bucket_for_character(entry: dict[str, Any], bible_data: dict[str, Any], evidence_summary: list[str]) -> tuple[str, str | None]:
    """Determine the fallback bucket for a character based on entity kind and evidence.
    
    Returns:
        tuple: (bucket_name, alias_redirect_target or None)
    """
    entity_kind = str(entry.get("entity_kind", "individual")).strip().lower()
    char_id = str(entry.get("canonical_id", "")).strip().lower()
    evidence_text = " ".join(evidence_summary).lower()
    
    # 1. Alias/role redirect
    if char_id == "protagonist" or "protagonist" in evidence_text:
        if "john carter" in evidence_text or "carter" in evidence_text:
            return ("alias_redirect", "john_carter")
    
    # 2. Context-only narrative/deceased/non-renderable
    if entity_kind in {"memory", "reference", "deceased", "abstract"}:
        return ("context_only", None)
    if any(marker in evidence_text for marker in ["dead", "deceased", "corpse", "body", "riddled with arrows", "former", "memory of", "mentioned only"]):
        return ("context_only", None)
    
    # 3. Group/horde
    if entity_kind in {"group", "collective", "horde"}:
        return ("group_or_horde", None)
    if any(marker in evidence_text for marker in ["warriors", "horde", "group", "collective"]):
        return ("group_or_horde", None)
    
    # 4. Quadruped/mount/beast
    if any(marker in evidence_text for marker in ["mount", "mounts", "thoat", "quadruped", "watchdog", "watch dog", "hound"]):
        if any(marker in evidence_text for marker in ["large", "massive", "colossal", "mount"]):
            return ("large_quadruped", None)
        return ("small_quadruped", None)
    
    # 5. Non-human humanoid
    if any(marker in evidence_text for marker in ["martian", "thark", "green martian", "red martian", "barsoom", "helium", "four-armed", "four armed", "15ft", "15 ft"]):
        if any(marker in evidence_text for marker in ["humanoid", "warrior", "chieftain", "leader", "princess", "officer"]):
            return ("non_human_humanoid", None)
    
    # 6. Human
    if any(marker in evidence_text for marker in ["human", "earthling", "american", "confederate", "frontier", "cavalry", "officer", "captain", "virginia"]):
        return ("human", None)
    
    # 7. Creature
    if any(marker in evidence_text for marker in ["creature", "beast", "animal", "calot", "ape", "colossal"]):
        if any(marker in evidence_text for marker in ["large", "massive", "colossal", "giant"]):
            return ("large_creature", None)
        return ("small_creature", None)
    
    # 8. Unknown reference
    if not evidence_summary or len(evidence_summary) < 2:
        return ("unknown_reference", None)
    
    return ("unknown_reference", None)


def fallback_result_audit(fallback: dict[str, Any]) -> dict[str, Any]:
    """Audit fallback result to determine which fields were filled."""
    filled_fields = [
        field for field in PRODUCTION_FALLBACK_FIELDS
        if not is_unknownish(fallback.get(field))
    ]
    empty_fields = [
        field for field in PRODUCTION_FALLBACK_FIELDS
        if field not in filled_fields
    ]
    return {
        "status": fallback.get("status"),
        "fallback_bucket": fallback.get("fallback_bucket"),
        "filled_count": len(filled_fields),
        "empty_count": len(empty_fields),
        "filled_fields": filled_fields,
        "empty_fields": empty_fields,
        "non_empty": bool(filled_fields),
    }


def deterministic_visual_fallback(entry: dict[str, Any], bible_data: dict[str, Any], evidence_summary: list[str]) -> dict[str, Any]:
    """Generate deterministic visual production fallback when canon evidence is thin."""
    fallback_bucket, alias_target = fallback_bucket_for_character(entry, bible_data, evidence_summary)
    
    if fallback_bucket == "alias_redirect":
        return {
            "status": "alias_redirect",
            "fallback_bucket": fallback_bucket,
            "alias_redirect_target": alias_target,
            "production_identity_descriptor": f"alias redirect to {alias_target}",
            "production_body_descriptor": "see canonical character",
            "production_face_descriptor": "see canonical character",
            "production_costume_descriptor": "see canonical character",
            "production_silhouette": "see canonical character",
            "production_movement_descriptor": "see canonical character",
            "production_state_variants": [],
            "negative_terms": [],
            "provisionality_note": f"This is an alias or role reference that redirects to the canonical character: {alias_target}",
        }
    
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
        "human": {
            "production_identity_descriptor": "human with period-appropriate appearance",
            "production_body_descriptor": "human build and proportions",
            "production_face_descriptor": "human facial structure",
            "production_costume_descriptor": "period-appropriate clothing",
            "production_silhouette": "upright human silhouette",
            "production_movement_descriptor": "natural human movement",
            "production_state_variants": [],
            "negative_terms": ["alien anatomy", "non-human features"],
        },
        "non_human_humanoid": {
            "production_identity_descriptor": "humanoid with non-human anatomy",
            "production_body_descriptor": "humanoid build with species-specific proportions",
            "production_face_descriptor": "humanoid facial structure with non-human features",
            "production_costume_descriptor": "minimal harness or species-appropriate gear",
            "production_silhouette": "upright humanoid silhouette with non-human proportions",
            "production_movement_descriptor": "humanoid movement with species-specific characteristics",
            "production_state_variants": [],
            "negative_terms": ["human proportions", "Earth clothing"],
        },
        "small_quadruped": {
            "production_identity_descriptor": "small four-legged animal",
            "production_body_descriptor": "compact quadruped build",
            "production_face_descriptor": "animal skull structure",
            "production_costume_descriptor": "natural hide or minimal harness",
            "production_silhouette": "low quadruped silhouette",
            "production_movement_descriptor": "agile four-legged movement",
            "production_state_variants": [],
            "negative_terms": ["human anatomy", "upright posture", "bipedal"],
        },
        "large_quadruped": {
            "production_identity_descriptor": "large four-legged mount or beast",
            "production_body_descriptor": "massive quadruped build",
            "production_face_descriptor": "large animal skull structure",
            "production_costume_descriptor": "natural hide or riding harness",
            "production_silhouette": "imposing quadruped silhouette",
            "production_movement_descriptor": "powerful four-legged movement",
            "production_state_variants": [],
            "negative_terms": ["human anatomy", "upright posture", "bipedal"],
        },
        "small_creature": {
            "production_identity_descriptor": "small non-human creature",
            "production_body_descriptor": "compact creature build",
            "production_face_descriptor": "creature facial structure",
            "production_costume_descriptor": "natural hide or minimal covering",
            "production_silhouette": "small creature silhouette",
            "production_movement_descriptor": "creature-specific movement",
            "production_state_variants": [],
            "negative_terms": ["human anatomy", "humanoid"],
        },
        "large_creature": {
            "production_identity_descriptor": "large non-human creature",
            "production_body_descriptor": "massive creature build with powerful musculature",
            "production_face_descriptor": "large creature skull structure",
            "production_costume_descriptor": "natural hide or thick skin",
            "production_silhouette": "imposing creature silhouette",
            "production_movement_descriptor": "powerful creature movement",
            "production_state_variants": [],
            "negative_terms": ["human anatomy", "humanoid", "delicate"],
        },
        "group_or_horde": {
            "production_identity_descriptor": "collective group with unified visual identity",
            "production_body_descriptor": "varied builds within group-consistent parameters",
            "production_face_descriptor": "varied faces within species-consistent range",
            "production_costume_descriptor": "repeatable group uniform or martial gear",
            "production_silhouette": "group silhouette emphasizing numbers and cohesion",
            "production_movement_descriptor": "coordinated group movement",
            "production_state_variants": [],
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
    
    # Canon-additive fallback: prefer canon, add bucket defaults only if needed
    def _get_field(canon_key: str, default_key: str) -> str:
        canon_val = bible_data.get(canon_key, "")
        if not is_unknownish(canon_val):
            return str(canon_val)
        return defaults[default_key]
    
    def _combine_fields(*canon_keys: str, default_key: str) -> str:
        parts = []
        for key in canon_keys:
            val = bible_data.get(key, "")
            if not is_unknownish(val):
                if isinstance(val, list):
                    parts.extend(str(v) for v in val if not is_unknownish(v))
                else:
                    parts.append(str(val))
        if parts:
            return "; ".join(parts)
        return defaults[default_key]
    
    def _get_list_field(canon_key: str, default_key: str) -> list[str]:
        canon_val = bible_data.get(canon_key, [])
        if isinstance(canon_val, list) and any(not is_unknownish(v) for v in canon_val):
            return [str(v) for v in canon_val if not is_unknownish(v)]
        if isinstance(canon_val, str) and not is_unknownish(canon_val):
            return [str(canon_val)]
        return defaults[default_key]
    
    return {
        "status": "generated" if fallback_bucket != "unknown_reference" else "insufficient_context",
        "fallback_bucket": fallback_bucket,
        "production_identity_descriptor": _get_field("identity_baseline", "production_identity_descriptor") or _get_field("stable_visual_summary", "production_identity_descriptor"),
        "production_body_descriptor": _combine_fields("physical_build", "physical_traits", default_key="production_body_descriptor"),
        "production_face_descriptor": _combine_fields("distinguishing_features", default_key="production_face_descriptor"),
        "production_costume_descriptor": _get_field("costume_signature", "production_costume_descriptor"),
        "production_silhouette": _combine_fields("distinguishing_features", "physical_build", default_key="production_silhouette"),
        "production_movement_descriptor": _get_field("movement_language", "production_movement_descriptor"),
        "production_state_variants": _get_list_field("state_variants", "production_state_variants"),
        "negative_terms": defaults["negative_terms"],
        "provisionality_note": "Generated for visual production because strict canon evidence is thin; not strict canon.",
    }
