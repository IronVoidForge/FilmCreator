from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .core.json_io import read_json, write_json
from .scaffold import create_project

VISUAL_FALLBACK_SCHEMA_VERSION = "2026-04-visual-fallbacks-v2-book-agnostic"
VISUAL_FALLBACK_RELATIVE_PATH = Path("02_story_analysis") / "world" / "global" / "VISUAL_FALLBACKS.json"

DEFAULT_CHARACTER_NEGATIVES = [
    "modern suit",
    "necktie",
    "business attire",
    "office clothing",
    "corporate headshot",
    "passport photo",
    "turtleneck",
    "modern athletic shirt",
]

DEFAULT_ENVIRONMENT_NEGATIVES = [
    "generic empty landscape",
    "featureless field",
    "hidden landmark",
    "modern road",
    "cars",
    "modern buildings",
]


@dataclass(frozen=True)
class VisualFallbackSummary:
    project_slug: str
    path: str
    synthesized: bool
    reused: bool
    warnings: list[str]
    written_files: list[str]

    def to_dict(self) -> dict[str, Any]:
        return {
            "project_slug": self.project_slug,
            "path": self.path,
            "synthesized": self.synthesized,
            "reused": self.reused,
            "warnings": self.warnings,
            "written_files": self.written_files,
        }


def visual_fallback_path(project_dir: Path) -> Path:
    return project_dir / VISUAL_FALLBACK_RELATIVE_PATH


def load_visual_fallbacks(project_dir: Path) -> dict[str, Any]:
    path = visual_fallback_path(project_dir)
    if path.exists():
        payload = read_json(path)
        if isinstance(payload, dict):
            return _normalize_visual_fallbacks(payload)
    return default_visual_fallbacks(project_slug=project_dir.name)


def run_visual_fallback_synthesis(project_slug: str, *, force: bool = False) -> VisualFallbackSummary:
    project_dir = create_project(project_slug)
    path = visual_fallback_path(project_dir)
    warnings: list[str] = []
    if path.exists() and not force:
        return VisualFallbackSummary(project_slug=project_slug, path=str(path), synthesized=False, reused=True, warnings=[], written_files=[])

    context = _collect_project_context(project_dir)
    payload = default_visual_fallbacks(project_slug=project_slug, source_title=context.get("source_title", ""))
    payload["source_context_files"] = context.get("source_context_files", [])
    payload["context_digest"] = context.get("context_digest", "")
    payload["book_visual_context"] = _derive_book_visual_context(context)
    payload["character_fallbacks"] = _derive_character_fallbacks(payload["book_visual_context"], context)
    payload["environment_fallbacks"] = _derive_environment_fallbacks(payload["book_visual_context"], context)
    payload = _normalize_visual_fallbacks(payload)
    write_json(path, payload)
    return VisualFallbackSummary(project_slug=project_slug, path=str(path), synthesized=True, reused=False, warnings=warnings, written_files=[str(path)])


def default_visual_fallbacks(*, project_slug: str, source_title: str = "") -> dict[str, Any]:
    return {
        "schema_version": VISUAL_FALLBACK_SCHEMA_VERSION,
        "project_slug": project_slug,
        "source_title": source_title,
        "book_visual_context": "cinematic readable reference lighting, era-aware non-modern story adaptation, grounded materials, clear silhouettes, source-supported color logic",
        "character_fallbacks": {
            "general": "era-aware non-modern character styling with clear silhouette, readable materials, and source-supported accessories; avoid contemporary portrait fashion unless explicitly described",
            "human_period": "period-appropriate human clothing, practical natural fabrics, simple closures, worn footwear, no modern business or athletic styling unless explicitly described",
            "humanoid_fantasy": "storybook humanoid styling, color-coded regional costume, practical garments, magical or ceremonial accents only when supported by source evidence",
            "humanoid_speculative": "non-modern speculative humanoid styling, unfamiliar materials or ornaments when supported, coherent culture-specific costume logic, no contemporary Earth fashion",
            "creature_or_animal": "source-appropriate animal or creature anatomy, readable scale, natural texture, movement-ready silhouette, minimal gear only when supported",
            "group_or_crowd": "coherent group visual language with shared era, region, role, palette, and material logic while preserving individual variation",
        },
        "environment_fallbacks": {
            "general": "clear cinematic location reference with explicit landmarks, scale, materials, lighting, and atmosphere",
            "desert_mountain": "rugged desert mountain terrain, dry scrub, weathered rock, clear horizon, readable distance and scale",
            "cave_or_cliffside": "visible cave mouth, cliffside rock face, rocky threshold, shadowed interior, weathered stone, readable entrance landmark",
            "interior": "clear room or chamber layout, foreground midground background separation, pathways, anchor objects, visible scale",
            "wilderness": "natural terrain with distinct foreground, midground, background, landmarks, lighting, and weather atmosphere",
        },
        "negative_terms": {
            "character_wardrobe": list(DEFAULT_CHARACTER_NEGATIVES),
            "environment": list(DEFAULT_ENVIRONMENT_NEGATIVES),
        },
        "notes": [
            "Generated fallback text is descriptor-heavy by design and should not depend on image models knowing the source title.",
            "Fallbacks are inferred visual guidance, not explicit canon unless supported by source artifacts.",
        ],
    }


def character_negative_terms(fallbacks: dict[str, Any]) -> list[str]:
    return _list(fallbacks.get("negative_terms", {}).get("character_wardrobe", [])) or list(DEFAULT_CHARACTER_NEGATIVES)


def environment_negative_terms(fallbacks: dict[str, Any]) -> list[str]:
    return _list(fallbacks.get("negative_terms", {}).get("environment", [])) or list(DEFAULT_ENVIRONMENT_NEGATIVES)


def select_character_fallback_bucket(text: str) -> str:
    normalized = text.lower()
    if any(term in normalized for term in ["horde", "tribe", "war party", "crowd", "group", "warriors"]):
        return "group_or_crowd"
    if any(term in normalized for term in ["creature", "ape", "beast", "non humanoid", "non-humanoid", "multi-legged", "animal"]):
        return "creature_or_animal"
    if any(term in normalized for term in ["witch", "wizard", "sorcerer", "magical", "enchanted", "fairy", "humanoid_nonhuman"]):
        return "humanoid_fantasy"
    if any(term in normalized for term in ["martian", "alien", "planetary", "non-earth", "extraterrestrial"]):
        return "humanoid_speculative"
    return "human_period"


def select_environment_fallback_bucket(text: str) -> str:
    normalized = text.lower()
    if any(term in normalized for term in ["cave", "cliff", "cliffside", "cavern"]):
        return "cave_or_cliffside"
    if any(term in normalized for term in ["desert", "mountain", "mesa", "arizona", "wilderness"]):
        return "desert_mountain"
    if any(term in normalized for term in ["room", "chamber", "interior", "hall", "palace"]):
        return "interior"
    return "general"


def fallback_text(fallbacks: dict[str, Any], family: str, bucket: str) -> str:
    table = fallbacks.get(f"{family}_fallbacks", {})
    if not isinstance(table, dict):
        return ""
    return str(table.get(str(bucket).strip()) or table.get("general") or "").strip()


def _normalize_visual_fallbacks(payload: dict[str, Any]) -> dict[str, Any]:
    normalized = default_visual_fallbacks(project_slug=str(payload.get("project_slug", "")).strip() or "unknown", source_title=str(payload.get("source_title", "")).strip())
    normalized.update({k: v for k, v in payload.items() if k not in {"character_fallbacks", "environment_fallbacks", "negative_terms"}})
    for family in ["character_fallbacks", "environment_fallbacks"]:
        incoming = payload.get(family, {})
        if isinstance(incoming, dict):
            merged = dict(normalized[family])
            for key, value in incoming.items():
                if str(value).strip():
                    merged[str(key)] = str(value).strip()
            normalized[family] = merged
    incoming_negatives = payload.get("negative_terms", {})
    if isinstance(incoming_negatives, dict):
        normalized["negative_terms"] = {
            "character_wardrobe": _dedupe(_list(incoming_negatives.get("character_wardrobe", [])) or DEFAULT_CHARACTER_NEGATIVES),
            "environment": _dedupe(_list(incoming_negatives.get("environment", [])) or DEFAULT_ENVIRONMENT_NEGATIVES),
        }
    normalized["schema_version"] = VISUAL_FALLBACK_SCHEMA_VERSION
    return normalized


def _collect_project_context(project_dir: Path) -> dict[str, Any]:
    candidate_roots = [
        project_dir / "01_source",
        project_dir / "02_story_analysis" / "world" / "summaries",
        project_dir / "02_story_analysis" / "world" / "continuity",
        project_dir / "02_story_analysis" / "world" / "snapshots",
    ]
    files: list[Path] = []
    for root in candidate_roots:
        if not root.exists():
            continue
        files.extend(sorted(path for path in root.glob("*.md") if path.is_file())[:40])
        files.extend(sorted(path for path in root.glob("*.json") if path.is_file())[:40])
    snippets: list[str] = []
    source_files: list[str] = []
    for path in files[:80]:
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        compact = _compact_text(text, limit=900)
        if compact:
            snippets.append(compact)
            source_files.append(str(path))
    combined = "\n".join(snippets)
    return {
        "source_title": _guess_source_title(project_dir, combined),
        "context_digest": _compact_text(combined, limit=4000),
        "source_context_files": source_files,
    }


def _derive_book_visual_context(context: dict[str, Any]) -> str:
    digest = str(context.get("context_digest", "")).lower()
    descriptors = ["cinematic readable reference lighting"]
    if any(term in digest for term in ["witch", "wizard", "magic", "magical", "enchanted", "fairy", "castle"]):
        descriptors.extend(["storybook fantasy adventure", "color-coded regional design", "practical fairy-tale costumes"])
    elif any(term in digest for term in ["planet", "martian", "alien", "extraterrestrial"]):
        descriptors.extend(["speculative adventure", "non-modern unfamiliar-world culture"])
    else:
        descriptors.append("classic adventure visual style")
    if any(term in digest for term in ["desert", "mountain", "cave", "cliff", "wilderness"]):
        descriptors.extend(["terrain-specific natural realism", "weathered rock and readable landscape depth"])
    if any(term in digest for term in ["sword", "warrior", "harness", "tribal", "chieftain"]):
        descriptors.extend(["non-modern clothing", "weathered natural materials", "tribal or gladiatorial costume logic"])
    if len(descriptors) < 5:
        descriptors.extend(["non-modern clothing", "weathered natural materials"])
    return ", ".join(_dedupe(descriptors))


def _derive_character_fallbacks(book_context: str, context: dict[str, Any]) -> dict[str, str]:
    base = default_visual_fallbacks(project_slug="template")["character_fallbacks"]
    return {
        **base,
        "general": f"{book_context}; non-modern character styling; avoid contemporary portrait fashion unless explicitly described",
    }


def _derive_environment_fallbacks(book_context: str, context: dict[str, Any]) -> dict[str, str]:
    base = default_visual_fallbacks(project_slug="template")["environment_fallbacks"]
    return {
        **base,
        "general": f"{book_context}; clear cinematic location reference with explicit landmarks, scale, materials, lighting, and atmosphere",
    }


def _guess_source_title(project_dir: Path, text: str) -> str:
    return project_dir.name.replace("_", " ").strip().title()


def _compact_text(text: str, *, limit: int) -> str:
    cleaned = re.sub(r"\s+", " ", text).strip()
    return cleaned[:limit].rstrip() if len(cleaned) > limit else cleaned


def _list(value: Any) -> list[str]:
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    if isinstance(value, str) and value.strip():
        return [value.strip()]
    return []


def _dedupe(items: list[str]) -> list[str]:
    out: list[str] = []
    seen: set[str] = set()
    for item in items:
        cleaned = str(item).strip()
        key = cleaned.lower()
        if cleaned and key not in seen:
            seen.add(key)
            out.append(cleaned)
    return out
