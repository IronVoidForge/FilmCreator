from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .common import ROOT

BOOSTER_LIBRARY_PATHS = [
    ROOT / "spec" / "prompt_boosters" / "character_reference_boosters.json",
    ROOT / "spec" / "prompt_boosters" / "environment_reference_boosters.json",
    ROOT / "spec" / "prompt_boosters" / "scene_assembly_boosters.json",
    ROOT / "spec" / "prompt_boosters" / "experimental_boosters.json",
]

PROMPT_VARIANTS: dict[str, list[str]] = {
    "raw": [],
    "character_clean": ["character_reference_clean_v1"],
    "character_readability": [
        "character_reference_clean_v1",
        "character_face_readability_v1",
        "character_body_readability_v1",
        "character_costume_readability_v1",
    ],
    "character_polish": [
        "character_reference_clean_v1",
        "character_face_readability_v1",
        "character_body_readability_v1",
        "character_costume_readability_v1",
        "character_reference_polish_v1",
    ],
    "environment_clean": ["environment_reference_clean_v1"],
    "environment_readability": [
        "environment_reference_clean_v1",
        "environment_spatial_readability_v1",
        "environment_landmark_readability_v1",
    ],
    "environment_polish": [
        "environment_reference_clean_v1",
        "environment_spatial_readability_v1",
        "environment_landmark_readability_v1",
        "environment_reference_polish_v1",
    ],
    "scene_clean": ["scene_assembly_clean_v1"],
    "scene_readability": [
        "scene_assembly_clean_v1",
        "scene_character_environment_integration_v1",
        "scene_cinematic_readability_v1",
        "scene_continuity_preservation_v1",
    ],
    "aesthetic_experimental": ["aesthetic_polish_experimental_v1"],
}


@dataclass(frozen=True)
class PromptBoosterBundle:
    bundle_id: str
    category: str
    positive: tuple[str, ...]
    negative: tuple[str, ...]
    notes: str = ""

    @classmethod
    def from_dict(cls, payload: dict[str, Any]) -> "PromptBoosterBundle":
        return cls(
            bundle_id=str(payload.get("bundle_id", "")).strip(),
            category=str(payload.get("category", "")).strip(),
            positive=tuple(str(item).strip() for item in payload.get("positive", []) if str(item).strip()),
            negative=tuple(str(item).strip() for item in payload.get("negative", []) if str(item).strip()),
            notes=str(payload.get("notes", "")).strip(),
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "bundle_id": self.bundle_id,
            "category": self.category,
            "positive": list(self.positive),
            "negative": list(self.negative),
            "notes": self.notes,
        }


def load_booster_library() -> dict[str, PromptBoosterBundle]:
    bundles: dict[str, PromptBoosterBundle] = {}
    for path in BOOSTER_LIBRARY_PATHS:
        if not path.exists():
            continue
        payload = json.loads(path.read_text(encoding="utf-8"))
        for item in payload.get("bundles", []):
            if not isinstance(item, dict):
                continue
            bundle = PromptBoosterBundle.from_dict(item)
            if bundle.bundle_id:
                bundles[bundle.bundle_id] = bundle
    return bundles


def bundle_ids_for_variant(prompt_variant_id: str | None, explicit_bundle_ids: list[str] | None = None) -> list[str]:
    ids: list[str] = []
    variant = (prompt_variant_id or "raw").strip()
    ids.extend(PROMPT_VARIANTS.get(variant, []))
    ids.extend(bundle_id.strip() for bundle_id in explicit_bundle_ids or [] if bundle_id.strip())
    deduped: list[str] = []
    for bundle_id in ids:
        if bundle_id not in deduped:
            deduped.append(bundle_id)
    return deduped


def apply_booster_bundles(
    positive_prompt: str,
    negative_prompt: str,
    *,
    prompt_variant_id: str | None = None,
    bundle_ids: list[str] | None = None,
) -> tuple[str, str, dict[str, Any]]:
    selected_ids = bundle_ids_for_variant(prompt_variant_id, bundle_ids)
    if not selected_ids:
        return (
            positive_prompt,
            negative_prompt,
            {"prompt_variant_id": prompt_variant_id or "raw", "booster_bundle_ids": []},
        )

    library = load_booster_library()
    missing = [bundle_id for bundle_id in selected_ids if bundle_id not in library]
    selected = [library[bundle_id] for bundle_id in selected_ids if bundle_id in library]
    positive_terms: list[str] = []
    negative_terms: list[str] = []
    for bundle in selected:
        positive_terms.extend(bundle.positive)
        negative_terms.extend(bundle.negative)

    boosted_positive = _append_terms(positive_prompt, positive_terms)
    boosted_negative = _append_terms(negative_prompt, negative_terms)
    metadata = {
        "prompt_variant_id": prompt_variant_id or "custom",
        "booster_bundle_ids": [bundle.bundle_id for bundle in selected],
        "missing_booster_bundle_ids": missing,
        "positive_boosters": _dedupe_terms(positive_terms),
        "negative_boosters": _dedupe_terms(negative_terms),
    }
    return boosted_positive, boosted_negative, metadata


def _append_terms(prompt: str, terms: list[str]) -> str:
    prompt = str(prompt or "").strip()
    deduped = _dedupe_terms(terms)
    if not deduped:
        return prompt
    addition = ", ".join(deduped)
    if not prompt:
        return addition
    return f"{prompt}, {addition}"


def _dedupe_terms(terms: list[str]) -> list[str]:
    deduped: list[str] = []
    seen: set[str] = set()
    for term in terms:
        cleaned = str(term).strip()
        key = cleaned.lower()
        if cleaned and key not in seen:
            seen.add(key)
            deduped.append(cleaned)
    return deduped

