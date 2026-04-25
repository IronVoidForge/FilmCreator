from __future__ import annotations

from typing import Any

from .visual_fallbacks import (
    character_negative_terms,
    fallback_text,
    select_character_fallback_bucket,
)

WEAK_TEXT_VALUES = {"", "unknown", "none", "(none)", "n/a", "[]", "[ ]", "null"}
GENERIC_CHARACTER_PLACEHOLDERS = {
    "described character with stable costume and silhouette",
    "stable costume and silhouette",
    "canon-compatible best-effort character build",
    "canon-compatible best-effort character costume materials",
}

CHARACTER_REFERENCE_REPAIR_FIELDS = [
    "identity_descriptor",
    "body_descriptor",
    "face_descriptor",
    "costume_descriptor",
    "posture_descriptor",
    "expression_descriptor",
    "locked_fields",
    "source_visual_context",
    "subject_visual_context",
]


def repair_character_reference_fields(
    *,
    canonical_id: str,
    display_name: str,
    field_values: dict[str, Any] | None = None,
    supported_field_values: dict[str, Any] | None = None,
    generated_field_values: dict[str, Any] | None = None,
    evidence_summary: list[str] | None = None,
    visual_fallbacks: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Return inferred/fallback fields for reference-prompt readiness.

    This helper deliberately does not mutate or overwrite raw descriptor evidence. It
    creates a small reference_repair payload that descriptor enrichment can attach
    near the end of Phase 11. Phase 11.5 should prefer explicit/supported fields,
    then these repaired fields, then safe defaults.
    """
    field_values = field_values or {}
    supported_field_values = supported_field_values or {}
    generated_field_values = generated_field_values or {}
    evidence_summary = evidence_summary or []
    visual_fallbacks = visual_fallbacks or {}

    combined_text = " ".join(
        str(part)
        for part in [canonical_id, display_name, field_values, supported_field_values, generated_field_values, " ".join(evidence_summary)]
        if part
    )
    bucket = select_character_fallback_bucket(combined_text)
    source_visual_context = str(visual_fallbacks.get("book_visual_context", "")).strip()
    bucket_fallback = fallback_text(visual_fallbacks, "character", bucket)
    negative_terms = character_negative_terms(visual_fallbacks)

    repair: dict[str, Any] = {
        "repair_kind": "character_reference_repair",
        "repair_sources": ["VISUAL_FALLBACKS.json", "descriptor_enrichment"],
        "fallback_bucket": bucket,
        "fallback_fields_used": [],
        "negative_terms": negative_terms,
    }

    def current(field: str) -> Any:
        return _first_value(supported_field_values.get(field), field_values.get(field), generated_field_values.get(field))

    identity = _safe_text(current("identity_descriptor") or current("identity_baseline") or display_name or canonical_id)
    if _is_weak(identity):
        identity = f"{display_name or canonical_id} as a readable non-modern adventure character reference"
        repair["fallback_fields_used"].append("identity_descriptor")
    repair["identity_descriptor"] = identity

    body = _safe_text(current("body_descriptor") or current("physical_build") or current("build") or current("height"))
    if _is_weak(body):
        body = _body_fallback(bucket)
        repair["fallback_fields_used"].append("body_descriptor")
    repair["body_descriptor"] = body

    face = _safe_text(current("face_descriptor") or _join_fragments(current("face_shape"), current("eye_color"), current("hair_style"), current("distinctive_features")))
    if _is_weak(face):
        face = "face not specifically described; use a readable reference face with natural structure and preserve any source-supported distinguishing traits"
        repair["fallback_fields_used"].append("face_descriptor")
    repair["face_descriptor"] = face

    costume = _safe_text(current("costume_descriptor") or _join_fragments(current("costume_layers"), current("costume_materials"), current("costume_signature"), current("recurring_accessories")))
    if _is_weak(costume):
        costume = (
            "Costume not specifically described; use project visual fallback: "
            f"{bucket_fallback or 'non-modern pulp adventure clothing with weathered natural materials'}. "
            "Avoid modern business clothing, suits, ties, turtlenecks, athletic catalog styling, and corporate portrait styling."
        )
        repair["fallback_fields_used"].append("costume_descriptor")
    repair["costume_descriptor"] = costume

    posture = _safe_text(current("posture_descriptor") or current("posture") or current("movement_language"))
    if _is_weak(posture):
        posture = "Neutral readable reference posture unless chapter context specifies action."
        repair["fallback_fields_used"].append("posture_descriptor")
    repair["posture_descriptor"] = posture

    expression = _safe_text(current("expression_descriptor") or current("expression_tendency"))
    if _is_weak(expression):
        expression = "Neutral readable expression unless chapter context specifies fear, aggression, grief, exhaustion, or another clear emotion."
        repair["fallback_fields_used"].append("expression_descriptor")
    repair["expression_descriptor"] = expression

    locked_fields = _safe_text(current("locked_fields") or current("silhouette_notes") or current("distinctive_features"))
    if _is_weak(locked_fields):
        locked_fields = "Preserve confirmed species or body type, skin tone, silhouette, costume era, and any source-supported distinguishing traits."
        repair["fallback_fields_used"].append("locked_fields")
    repair["locked_fields"] = locked_fields

    if _is_weak(source_visual_context):
        source_visual_context = "non-modern pulp adventure visual context, weathered natural materials, cinematic readable reference lighting"
        repair["fallback_fields_used"].append("source_visual_context")
    repair["source_visual_context"] = source_visual_context

    repair["subject_visual_context"] = (
        f"{display_name or canonical_id}: {identity}. Use {bucket_fallback or 'world-appropriate non-modern styling'}; "
        "do not modernize clothing or portrait styling."
    )
    if repair["fallback_fields_used"]:
        repair["review_flags"] = ["reference_fields_repaired_from_visual_fallbacks"]
    else:
        repair["review_flags"] = []
    return repair


def _first_value(*values: Any) -> Any:
    for value in values:
        if not _is_weak(value):
            return value
    return ""


def _safe_text(value: Any) -> str:
    if isinstance(value, list):
        return _join_fragments(*value)
    if isinstance(value, dict):
        return _join_fragments(*value.values())
    return " ".join(str(value or "").split()).strip()


def _is_weak(value: Any) -> bool:
    text = _safe_text(value).lower()
    return text in WEAK_TEXT_VALUES or text in GENERIC_CHARACTER_PLACEHOLDERS


def _join_fragments(*values: Any) -> str:
    parts: list[str] = []
    seen: set[str] = set()
    for value in values:
        if isinstance(value, list):
            candidates = value
        else:
            candidates = [value]
        for candidate in candidates:
            text = _safe_text(candidate)
            if not text or text.lower() in WEAK_TEXT_VALUES:
                continue
            key = text.lower()
            if key not in seen:
                seen.add(key)
                parts.append(text)
    return "; ".join(parts)


def _body_fallback(bucket: str) -> str:
    if bucket == "creature_or_primitive":
        return "body not specifically described; use a feral or primitive non-modern silhouette with readable anatomy appropriate to the source context"
    if bucket == "barsoom_humanoid":
        return "body not specifically described; use a tall non-modern planetary-romance humanoid silhouette with readable proportions"
    if bucket == "group_or_horde":
        return "group body details vary; preserve coherent species, costume era, and group silhouette"
    return "body not specifically described; use a grounded human adventure silhouette with realistic proportions"
