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


def _flatten_text(value: Any) -> list[str]:
    """Recursively collect strings from str/list/dict values."""
    if is_unknownish(value):
        return []
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        result = []
        for item in value:
            result.extend(_flatten_text(item))
        return result
    if isinstance(value, dict):
        result = []
        for v in value.values():
            result.extend(_flatten_text(v))
        return result
    return [str(value)]


def _character_text(entry: dict[str, Any], bible_data: dict[str, Any], evidence_summary: list[str]) -> dict[str, str]:
    """Return separate normalized text channels for classification."""
    id_fields = ["canonical_id", "character_id", "display_name", "aliases"]
    canon_fields = [
        "identity_baseline", "stable_visual_summary", "physical_build", "physical_traits",
        "costume_signature", "distinguishing_features", "movement_language", "role",
        "origin_or_historical_context", "state_variants"
    ]
    
    id_parts = []
    for field in id_fields:
        id_parts.extend(_flatten_text(entry.get(field)))
    id_text = " ".join(id_parts).lower()
    
    canon_parts = []
    for field in canon_fields:
        canon_parts.extend(_flatten_text(bible_data.get(field)))
    canon_text = " ".join(canon_parts).lower()
    
    evidence_text = " ".join(evidence_summary).lower()
    all_text = f"{id_text} {canon_text} {evidence_text}"
    
    return {
        "id_text": id_text,
        "canon_text": canon_text,
        "evidence_text": evidence_text,
        "all_text": all_text,
    }


def has_direct_identity_evidence(text: str, markers: list[str]) -> bool:
    """Check if text contains direct identity evidence."""
    return any(marker in text for marker in markers)


def has_associated_entity_evidence(text: str, markers: list[str]) -> bool:
    """Check if text mentions associated entities (not the subject itself).
    
    Returns True if the text describes the subject USING/WEARING/RIDING something,
    not if the subject IS that thing.
    """
    # Associated evidence uses specific patterns that indicate the subject is NOT the thing
    association_patterns = [
        "riding a", "riding an", "riding the", "riding on",
        "mounted on", "dismount from", "dismounts from",
        "followed by", "carrying a", "carrying an", "carrying the",
        "wearing a", "wearing an", "wearing the", "wearing exotic"
    ]
    return any(pattern in text for pattern in association_patterns)


def conservative_emergency_bucket(entry: dict[str, Any], bible_data: dict[str, Any], text: dict[str, str]) -> str:
    """Return conservative bucket when evidence is weak or mixed."""
    # If entity_kind explicitly says non-renderable, use context_only
    entity_kind = str(entry.get("entity_kind", "individual")).strip().lower()
    if entity_kind in {"memory", "reference", "deceased", "abstract"}:
        return "context_only"
    
    # If canon has active visual evidence, don't default to context_only
    canon_text = text["canon_text"]
    active_visual_markers = ["movement", "visual", "appearance", "build", "frame", "posture"]
    if any(marker in canon_text for marker in active_visual_markers):
        return "unknown_reference"
    
    # Otherwise, weak evidence = unknown_reference
    return "unknown_reference"


def fallback_bucket_for_character(entry: dict[str, Any], bible_data: dict[str, Any], evidence_summary: list[str]) -> tuple[str, str | None]:
    """Determine the fallback bucket for a character based on entity kind and evidence.
    
    Conservative rules:
    - Only classify as non-human/quadruped/creature if direct evidence says the entity IS that type
    - Associated evidence (riding X, wearing Y) does not redefine the entity
    - Weak/mixed evidence returns unknown_reference
    - Alias redirects must come from structured metadata, not hardcoded IDs
    
    Returns:
        tuple: (bucket_name, alias_redirect_target or None)
    """
    entity_kind = str(entry.get("entity_kind", "individual")).strip().lower()
    
    text = _character_text(entry, bible_data, evidence_summary)
    id_text = text["id_text"]
    canon_text = text["canon_text"]
    evidence_text = text["evidence_text"]
    all_text = text["all_text"]
    
    # 1. Alias redirect - only from explicit metadata
    alias_metadata = bible_data.get("alias_redirect_target")
    if alias_metadata and not is_unknownish(alias_metadata):
        return ("alias_redirect", str(alias_metadata))
    
    # 2. Group/horde - entity_kind or direct collective evidence
    if entity_kind in {"group", "collective", "horde"}:
        return ("group_or_horde", None)
    group_markers = ["group", "horde", "collective", "warriors", "soldiers"]
    if has_direct_identity_evidence(id_text, group_markers):
        return ("group_or_horde", None)
    
    # 3. Context-only - entity_kind or explicit non-renderable metadata
    if entity_kind in {"memory", "reference", "deceased", "abstract"}:
        return ("context_only", None)
    
    context_only_metadata = bible_data.get("renderable", True)
    if context_only_metadata is False:
        return ("context_only", None)
    
    # Context-only if direct evidence says deceased/non-renderable AND no active visual evidence
    context_markers = ["deceased", "corpse", "mummified", "memory of", "mentioned only", "reference only"]
    if has_direct_identity_evidence(canon_text, context_markers) or has_direct_identity_evidence(id_text, context_markers):
        active_markers = ["movement", "visual", "agile", "leaping", "posture", "build", "frame"]
        if not has_direct_identity_evidence(canon_text, active_markers):
            return ("context_only", None)
    
    # 4. Quadruped - entity itself must BE a mount/beast, not just use one
    # Check for associated evidence first (disqualifies quadruped classification)
    if has_associated_entity_evidence(canon_text, ["mount", "beast", "animal"]):
        # This entity USES a mount, so it's not a mount itself
        pass
    else:
        # Check if entity IS a mount/beast
        quadruped_id_markers = ["mount", "mounts", "watchdog", "hound", "dog"]
        quadruped_canon_markers = ["riding beast", "eight-legged mount", "eight-legged beast", "four-legged", "quadruped", "beast"]
        
        if has_direct_identity_evidence(id_text, quadruped_id_markers) or \
           has_direct_identity_evidence(canon_text, quadruped_canon_markers):
            size_markers = ["large", "massive", "colossal"]
            if has_direct_identity_evidence(all_text, size_markers):
                return ("large_quadruped", None)
            return ("small_quadruped", None)
    
    # 5. Non-human humanoid vs Human - check identity_baseline first
    # If identity_baseline explicitly says "alien" or has non-human markers, prioritize that
    identity_baseline = str(bible_data.get("identity_baseline", "")).lower()
    physical_build = str(bible_data.get("physical_build", "")).lower()
    identity_canon_text = f"{identity_baseline} {physical_build}"
    
    non_human_markers = ["alien", "non-human", "non human", "four-armed", "four armed", "tusks", "green skin", "red skin", "olive-green skin"]
    humanoid_markers = ["humanoid", "bipedal", "upright", "warrior", "leader", "officer"]
    human_markers = ["human", "man", "woman", "earthman", "earthling"]
    
    # Check for non-human markers in identity
    has_non_human_identity = has_direct_identity_evidence(identity_canon_text, non_human_markers) or has_direct_identity_evidence(id_text, non_human_markers)
    
    # Check for explicit height markers that suggest non-human scale
    height_markers = ["15ft", "15 ft", "12ft", "12 ft", "10ft", "10 ft"]
    has_non_human_scale = has_direct_identity_evidence(canon_text, height_markers)
    
    # Check for humanoid markers
    has_humanoid = has_direct_identity_evidence(canon_text, humanoid_markers) or has_direct_identity_evidence(id_text, humanoid_markers)
    
    # Check for human markers
    has_human = has_direct_identity_evidence(canon_text, human_markers) or has_direct_identity_evidence(id_text, human_markers)
    
    # If identity says alien/non-human AND has humanoid markers, classify as non_human_humanoid
    if (has_non_human_identity or has_non_human_scale) and has_humanoid:
        # But not if explicitly beast/animal
        beast_markers = ["beast", "animal", "creature"]
        if not has_direct_identity_evidence(canon_text, beast_markers):
            return ("non_human_humanoid", None)
    
    # If identity says human, classify as human
    if has_human:
        # But not if explicitly non-humanoid
        if "non-humanoid" not in canon_text and "non-humanoid" not in id_text:
            return ("human", None)
    
    # 7. Creature - entity itself must BE a creature/beast
    if has_associated_entity_evidence(canon_text, ["creature", "beast", "animal"]):
        # This entity is associated with creatures, not a creature itself
        pass
    else:
        creature_markers = ["creature", "beast", "animal", "ape", "multi-legged"]
        if has_direct_identity_evidence(canon_text, creature_markers) or has_direct_identity_evidence(id_text, creature_markers):
            size_markers = ["large", "massive", "colossal", "giant"]
            if has_direct_identity_evidence(all_text, size_markers):
                return ("large_creature", None)
            return ("small_creature", None)
    
    # 8. Conservative fallback - weak or mixed evidence
    return conservative_emergency_bucket(entry, bible_data, text), None


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
            "fallback_bucket": "alias_redirect",
            "canonical_target_id": alias_target,
            "alias_redirect_target": alias_target,
            "production_identity_descriptor": f"Alias or role label; use canonical visual reference for {alias_target}.",
            "production_body_descriptor": "Use canonical visual reference.",
            "production_face_descriptor": "Use canonical visual reference.",
            "production_costume_descriptor": "Use canonical visual reference.",
            "production_silhouette": "Use canonical visual reference.",
            "production_movement_descriptor": "Use canonical visual reference.",
            "production_state_variants": [],
            "negative_terms": [],
            "provisionality_note": "Alias/role entry redirected to canonical character; do not render as a separate character.",
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
