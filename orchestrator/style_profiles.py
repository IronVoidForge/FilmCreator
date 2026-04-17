from __future__ import annotations

import re


DEFAULT_REVIEW_BATCH_SIZE = 4
ALLOWED_REVIEW_BATCH_SIZES = {3, 4}

FIXED_STYLE_PROFILES = [
    "literal_descriptive",
    "cinematic_compositional",
    "performance_action_led",
    "sparse_conservative",
]

STAGE_FAMILY_BY_STAGE = {
    "scene_build": "keyframe",
    "keyframe": "keyframe",
    "scene_refinement": "still_fix",
    "scene_build_two_ref": "still_fix",
    "scene_refinement_two_ref": "still_fix",
    "still_fix": "still_fix",
    "cut_motion": "cut_motion",
    "anchor_frame": "legacy_continuity",
    "interval_frame": "legacy_continuity",
    "character_reference": "shared_reference",
    "environment_reference": "shared_reference",
}

PROPER_NOUN_PATTERN = re.compile(r"\b[A-Z][a-z]{2,}\b")

STYLE_PROMPT_PREFIX = {
    "literal_descriptive": (
        "Use explicit visible nouns, spatial relationships, and plain descriptive language. "
        "Avoid metaphor, flourish, and proper nouns."
    ),
    "cinematic_compositional": (
        "Use cinematic composition, framing, lens, lighting, and production language while keeping "
        "subjects explicitly described and visually grounded."
    ),
    "performance_action_led": (
        "Lead with subject behavior, interaction, body language, and visible action before secondary "
        "camera details."
    ),
    "sparse_conservative": (
        "Use the shortest safe prompt, rely strongly on the provided references and source image, and "
        "avoid adding extra invented details."
    ),
}


def stage_family(stage: str) -> str:
    return STAGE_FAMILY_BY_STAGE.get(stage, stage)


def uses_review_batches(stage: str) -> bool:
    return stage_family(stage) in {"keyframe", "still_fix", "cut_motion"}


def normalize_review_batch_size(raw_value: str | None, *, stage: str) -> int:
    if not uses_review_batches(stage):
        return 1

    if raw_value is None or not raw_value.strip():
        return DEFAULT_REVIEW_BATCH_SIZE

    try:
        batch_size = int(raw_value.strip())
    except ValueError as exc:
        raise ValueError(f"batch_size must be an integer for stage '{stage}'") from exc

    if batch_size not in ALLOWED_REVIEW_BATCH_SIZES:
        allowed = ", ".join(str(size) for size in sorted(ALLOWED_REVIEW_BATCH_SIZES))
        raise ValueError(f"batch_size for stage '{stage}' must be one of: {allowed}")
    return batch_size


def style_profiles_for_batch(batch_size: int) -> list[str]:
    if batch_size < 1 or batch_size > len(FIXED_STYLE_PROFILES):
        raise ValueError(f"Unsupported review batch size: {batch_size}")
    return FIXED_STYLE_PROFILES[:batch_size]


def build_styled_prompt(base_prompt: str, style_profile: str) -> str:
    prefix = STYLE_PROMPT_PREFIX[style_profile]
    return f"{prefix}\n\n{base_prompt.strip()}".strip()


def find_likely_proper_nouns(text: str) -> list[str]:
    ignore = {
        "The",
        "And",
        "For",
        "With",
        "Without",
        "Into",
        "From",
        "This",
        "That",
        "Grand",
        "Both",
        "Emphasize",
        "Use",
        "Avoid",
        "Generate",
        "Let",
        "Motion",
        "No",
        "Start",
        "Two",
    }
    matches = sorted({token for token in PROPER_NOUN_PATTERN.findall(text) if token not in ignore})
    return matches


def empty_stage_style_preferences() -> dict[str, dict[str, dict[str, int]]]:
    preferences: dict[str, dict[str, dict[str, int]]] = {}
    for family in {"keyframe", "still_fix", "cut_motion"}:
        preferences[family] = {}
        for profile in FIXED_STYLE_PROFILES:
            preferences[family][profile] = {
                "appearances": 0,
                "top_two": 0,
                "wins": 0,
            }
    return preferences
