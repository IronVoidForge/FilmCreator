from __future__ import annotations

from typing import Any

from .visual_fallbacks import (
    environment_negative_terms,
    fallback_text,
    select_environment_fallback_bucket,
)

WEAK_TEXT_VALUES = {"", "unknown", "none", "(none)", "n/a", "[]", "[ ]", "null"}
GENERIC_ENVIRONMENT_PLACEHOLDERS = {
    "described environment with stable spatial anchors",
    "described environment with stable spatial continuity",
    "stable spatial anchors",
}


def repair_environment_reference_fields(
    *,
    canonical_id: str,
    display_name: str,
    field_values: dict[str, Any] | None = None,
    supported_field_values: dict[str, Any] | None = None,
    generated_field_values: dict[str, Any] | None = None,
    evidence_summary: list[str] | None = None,
    visual_fallbacks: dict[str, Any] | None = None,
) -> dict[str, Any]:
    field_values = field_values or {}
    supported_field_values = supported_field_values or {}
    generated_field_values = generated_field_values or {}
    evidence_summary = evidence_summary or []
    visual_fallbacks = visual_fallbacks or {}

    combined_text = " ".join(str(v) for v in [canonical_id, display_name, field_values, supported_field_values, generated_field_values, " ".join(evidence_summary)] if v)
    bucket = select_environment_fallback_bucket(combined_text)
    source_visual_context = str(visual_fallbacks.get("book_visual_context", "")).strip()
    bucket_fallback = fallback_text(visual_fallbacks, "environment", bucket)
    negatives = environment_negative_terms(visual_fallbacks)

    repair = {
        "repair_kind": "environment_reference_repair",
        "repair_sources": ["VISUAL_FALLBACKS.json", "descriptor_enrichment"],
        "fallback_bucket": bucket,
        "fallback_fields_used": [],
        "negative_terms": negatives,
    }

    def current(name: str) -> Any:
        return _first_value(supported_field_values.get(name), field_values.get(name), generated_field_values.get(name))

    layout = _safe(current("layout_descriptor") or current("layout") or current("spatial_layout"))
    if _weak(layout):
        layout = _layout_fallback(bucket, display_name or canonical_id)
        repair["fallback_fields_used"].append("layout_descriptor")
    repair["layout_descriptor"] = layout

    scale = _safe(current("scale_descriptor") or current("scale"))
    if _weak(scale):
        scale = "clear human-readable environmental scale with foreground, midground, and background separation"
        repair["fallback_fields_used"].append("scale_descriptor")
    repair["scale_descriptor"] = scale

    architecture = _safe(current("architecture_descriptor") or current("terrain_descriptor") or current("materials"))
    if _weak(architecture):
        architecture = bucket_fallback or "clear environmental materials and terrain logic"
        repair["fallback_fields_used"].append("architecture_descriptor")
    repair["architecture_descriptor"] = architecture

    landmark = _safe(current("landmark_descriptor") or current("landmark") or current("anchor_objects"))
    if _weak(landmark):
        landmark = _landmark_fallback(bucket)
        repair["fallback_fields_used"].append("landmark_descriptor")
    repair["landmark_descriptor"] = landmark

    lighting = _safe(current("lighting_descriptor") or current("lighting"))
    if _weak(lighting):
        lighting = "clear readable cinematic lighting with visible forms and depth"
        repair["fallback_fields_used"].append("lighting_descriptor")
    repair["lighting_descriptor"] = lighting

    mood = _safe(current("mood_descriptor") or current("mood"))
    if _weak(mood):
        mood = "grounded atmospheric adventure tone"
        repair["fallback_fields_used"].append("mood_descriptor")
    repair["mood_descriptor"] = mood

    locked = _safe(current("locked_fields"))
    if _weak(locked):
        locked = _locked_fallback(bucket)
        repair["fallback_fields_used"].append("locked_fields")
    repair["locked_fields"] = locked

    if _weak(source_visual_context):
        source_visual_context = "cinematic readable adventure-world visual context"
        repair["fallback_fields_used"].append("source_visual_context")
    repair["source_visual_context"] = source_visual_context

    repair["subject_visual_context"] = f"{display_name or canonical_id}: {layout}. Preserve {locked}."
    repair["review_flags"] = ["reference_fields_repaired_from_visual_fallbacks"] if repair["fallback_fields_used"] else []
    return repair


def _first_value(*values: Any) -> Any:
    for value in values:
        if not _weak(value):
            return value
    return ""


def _safe(value: Any) -> str:
    if isinstance(value, list):
        return "; ".join(_safe(v) for v in value if _safe(v))
    if isinstance(value, dict):
        return "; ".join(_safe(v) for v in value.values() if _safe(v))
    return " ".join(str(value or "").split()).strip()


def _weak(value: Any) -> bool:
    text = _safe(value).lower()
    return text in WEAK_TEXT_VALUES or text in GENERIC_ENVIRONMENT_PLACEHOLDERS


def _layout_fallback(bucket: str, name: str) -> str:
    if bucket == "cave_or_cliffside":
        return f"{name}: rugged cliffside or mountain cave entrance with visible cave mouth, rocky threshold, shadowed interior, readable exterior terrain"
    if bucket == "desert_mountain":
        return f"{name}: rugged desert mountain terrain with weathered rock, dry ground cover, readable horizon and scale"
    if bucket == "interior":
        return f"{name}: clear room or chamber layout with pathways, anchor objects, and readable scale"
    return f"{name}: clear cinematic location reference with explicit landmarks and scale"


def _landmark_fallback(bucket: str) -> str:
    if bucket == "cave_or_cliffside":
        return "clearly visible cave mouth in a rock face, strong entrance silhouette, rocky threshold"
    if bucket == "desert_mountain":
        return "recognizable ridge lines, rock formations, and terrain silhouette"
    if bucket == "interior":
        return "doorways, columns, furnishings, or anchor structures defining the space"
    return "clear landmark or anchor feature defining the location"


def _locked_fallback(bucket: str) -> str:
    if bucket == "cave_or_cliffside":
        return "cave mouth, rock face, rocky threshold, shadowed interior"
    if bucket == "desert_mountain":
        return "rugged terrain, rock materials, readable horizon"
    if bucket == "interior":
        return "room layout, pathways, anchor structures"
    return "core landmark, scale, and material identity"
