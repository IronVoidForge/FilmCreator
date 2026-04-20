from __future__ import annotations

import re


SCENE_ID_PATTERN = re.compile(r"(?:CH\d{3}_)?SC\d{3}$")
CLIP_ID_PATTERN = re.compile(r"CL\d{3}$")


def validate_scene_id(scene_id: str) -> str:
    normalized = scene_id.strip().upper()
    if not SCENE_ID_PATTERN.fullmatch(normalized):
        raise ValueError("scene_id must be SC### or CH###_SC###, for example SC001 or CH008_SC001")
    return normalized


def validate_clip_id(clip_id: str) -> str:
    normalized = clip_id.strip().upper()
    if not CLIP_ID_PATTERN.fullmatch(normalized):
        raise ValueError("clip_id must be CL###, for example CL001")
    return normalized
