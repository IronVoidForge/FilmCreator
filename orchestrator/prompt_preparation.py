from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .character_bible import _is_film_facing_character
from .core.json_io import read_json, write_json
from .environment_bible import _is_film_facing_environment
from .prompt_package import PromptPackage, write_prompt_package
from .scaffold import create_project


PROMPT_PREP_ROOT = Path("03_prompt_packages") / "prepared"
CHARACTER_VARIANTS = [
    ("front_view", "Front View", "front-facing full-body reference with the camera square to the subject"),
    ("three_quarter_view", "3/4 View", "three-quarter view with readable face, torso, and costume layers"),
    ("profile_view", "Profile View", "profile view with a clean silhouette and side-plane facial structure"),
    ("back_view", "Back View", "rear view with costume back detail and full silhouette clarity"),
    ("full_body_neutral", "Full Body Neutral", "full-body neutral standing reference with balanced posture"),
    ("bust_portrait", "Bust Portrait", "bust portrait with head, shoulders, and facial structure readable"),
    ("action_pose", "Action Pose", "dynamic action pose that preserves anatomy, costume, and identity"),
    ("expression_sheet", "Expression Sheet", "expression sheet showing several clear emotional beats without changing costume"),
]
ENVIRONMENT_VARIANTS = [
    ("establishing_wide", "Establishing Wide", "wide establishing reference with clear horizon, depth, and geography"),
    ("medium_spatial", "Medium Spatial View", "medium spatial view showing foreground, midground, and background relationships"),
    ("detail_focus", "Detail Focus", "detail-focused view on a recurring anchor or landmark"),
    ("interior_layout", "Interior Layout", "clear interior layout with readable pathways, structure, and scale"),
    ("exterior_geography", "Exterior Geography", "exterior geography view with readable terrain and boundaries"),
    ("lighting_variant", "Lighting Variant", "lighting variant preserving spatial layout while changing illumination"),
    ("time_of_day", "Time of Day Variant", "same place rendered at a different time of day while preserving canon"),
]
SHOT_VARIANTS = [
    ("primary_keyframe", "Primary Keyframe", "primary keyframe that matches the scene contract and shot intent"),
    ("alternate_angle", "Alternate Angle", "same moment from a different camera angle while preserving continuity"),
    ("zoom_variant", "Tighter Zoom", "tighter zoom that keeps the same beat but brings the subjects closer"),
    ("consistency_repair", "Consistency Repair", "continuity repair pass that preserves pose, costume, and spatial relationships"),
]

GENERIC_NEGATIVE_PROMPT = (
    "text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, "
    "distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition"
)


@dataclass(frozen=True)
class PromptPreparationSummary:
    project_slug: str
    total_entries: int
    synthesized_count: int
    reused_count: int
    review_queue_count: int
    written_files: list[str]
    warnings: list[str]

    def to_dict(self) -> dict[str, Any]:
        return {
            "project_slug": self.project_slug,
            "total_entries": self.total_entries,
            "synthesized_count": self.synthesized_count,
            "reused_count": self.reused_count,
            "review_queue_count": self.review_queue_count,
            "written_files": self.written_files,
            "warnings": self.warnings,
        }


def _fingerprint(data: Any) -> str:
    raw = json.dumps(data, sort_keys=True, ensure_ascii=False)
    return hashlib.sha1(raw.encode("utf-8")).hexdigest()


def _compact(text: str, *, limit: int = 220) -> str:
    collapsed = " ".join(text.split()).strip()
    if len(collapsed) <= limit:
        return collapsed
    return collapsed[: limit - 3].rstrip() + "..."


def _first_nonempty(*values: object, fallback: str = "") -> str:
    for value in values:
        if isinstance(value, str) and value.strip():
            return value.strip()
    return fallback


def _normalize_term(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.strip().lower()).strip()


def _strip_terms(text: str, terms: list[str]) -> str:
    cleaned = text
    for term in sorted({term for term in terms if term.strip()}, key=len, reverse=True):
        pattern = re.compile(re.escape(term), re.IGNORECASE)
        cleaned = pattern.sub("", cleaned)
    cleaned = re.sub(r"\s{2,}", " ", cleaned)
    cleaned = re.sub(r"\s+,", ",", cleaned)
    cleaned = re.sub(r",\s*,", ", ", cleaned)
    return cleaned.strip(" ,;")


def _listify(*values: str) -> str:
    items = [value.strip() for value in values if isinstance(value, str) and value.strip()]
    return "; ".join(items)


def _descriptor_phrases(*values: str) -> list[str]:
    phrases: list[str] = []
    for value in values:
        if not isinstance(value, str) or not value.strip():
            continue
        for part in re.split(r"[;\n]", value):
            cleaned = part.strip(" -•\t")
            if cleaned:
                phrases.append(cleaned)
    return phrases


def _looks_like_metadata_summary(text: str) -> bool:
    normalized = " ".join(text.lower().split())
    metadata_markers = [
        "resolved known",
        "no competing canonical alias",
        "kept extracted asset id",
        "canonical id",
        "extracted asset id",
        "singular individual entity",
        "registry fallback",
        "alias detected",
    ]
    return any(marker in normalized for marker in metadata_markers)


def _record_descriptor_phrases(record: dict[str, Any], keys: list[str], *, strip_terms: list[str] | None = None) -> list[str]:
    parts: list[str] = []
    supported_values = record.get("supported_field_values", {}) if isinstance(record.get("supported_field_values"), dict) else {}
    generated_values = record.get("generated_field_values", {}) if isinstance(record.get("generated_field_values"), dict) else {}
    field_values = record.get("field_values", {}) if isinstance(record.get("field_values"), dict) else {}

    def collect_values(source: dict[str, Any], key: str) -> list[Any]:
        value = source.get(key)
        if isinstance(value, list):
            return [item for item in value if isinstance(item, str) and item.strip()]
        if isinstance(value, str) and value.strip():
            return [value.strip()]
        return []

    for key in keys:
        values = collect_values(supported_values, key) or collect_values(generated_values, key) or collect_values(field_values, key)
        for item in values:
            cleaned = _strip_terms(item, strip_terms or [])
            if cleaned and cleaned.strip().lower() not in {"unknown", "none", "(none)", "n/a"} and not _looks_like_metadata_summary(cleaned):
                parts.extend(_descriptor_phrases(cleaned))
    deduped: list[str] = []
    seen: set[str] = set()
    for item in parts:
        if item not in seen:
            seen.add(item)
            deduped.append(item)
    return deduped


def _prompt_package_exists_with_same_content(path: Path, content: str) -> bool:
    return path.exists() and path.read_text(encoding="utf-8") == content


def _write_prompt_package_if_changed(path: Path, package: PromptPackage, *, force: bool) -> bool:
    content = package.to_markdown()
    if not force and _prompt_package_exists_with_same_content(path, content):
        return False
    write_prompt_package(path, package)
    return True


def _load_json_files(root: Path, pattern: str) -> list[dict[str, Any]]:
    if not root.exists():
        return []
    payloads: list[dict[str, Any]] = []
    for path in sorted(root.glob(pattern)):
        payload = read_json(path)
        if isinstance(payload, dict):
            payloads.append(payload)
    return payloads


def _character_bible_paths(project_dir: Path) -> list[Path]:
    root = project_dir / "02_story_analysis" / "bibles" / "characters"
    if not root.exists():
        return []
    return sorted(path for path in root.glob("CHAR_*.json") if path.is_file())


def _environment_bible_paths(project_dir: Path) -> list[Path]:
    root = project_dir / "02_story_analysis" / "bibles" / "environments"
    if not root.exists():
        return []
    return sorted(path for path in root.glob("ENV_*.json") if path.is_file())


def _scene_contract_paths(project_dir: Path) -> list[Path]:
    root = project_dir / "02_story_analysis" / "contracts" / "scenes"
    if not root.exists():
        return []
    return sorted(path for path in root.glob("CH*/CH*_SC*.json") if path.is_file())


def _shot_index_paths(project_dir: Path) -> list[Path]:
    root = project_dir / "02_story_analysis" / "contracts" / "shots"
    if not root.exists():
        return []
    return sorted(path for path in root.glob("CH*/CH*_SC*/SHOT_INDEX.json") if path.is_file())


def _descriptor_paths(project_dir: Path, kind: str) -> list[Path]:
    root = project_dir / "02_story_analysis" / "descriptors"
    if not root.exists():
        return []
    if kind == "character":
        return sorted(path for path in (root / "characters").glob("*.json") if path.is_file())
    if kind == "environment":
        return sorted(path for path in (root / "environments").glob("*.json") if path.is_file())
    if kind == "scene":
        return sorted(path for path in (root / "scenes").glob("*.json") if path.is_file())
    if kind == "shot":
        return sorted(path for path in (root / "shots").glob("CH*/CH*_SC*/SH*.json") if path.is_file())
    return []


def _load_character_bibles(project_dir: Path) -> dict[str, dict[str, Any]]:
    records: dict[str, dict[str, Any]] = {}
    for path in _character_bible_paths(project_dir):
        payload = read_json(path)
        if not isinstance(payload, dict):
            continue
        character_id = str(payload.get("character_id", "")).strip().lower()
        if character_id:
            records[character_id] = payload
    return records


def _load_environment_bibles(project_dir: Path) -> dict[str, dict[str, Any]]:
    records: dict[str, dict[str, Any]] = {}
    for path in _environment_bible_paths(project_dir):
        payload = read_json(path)
        if not isinstance(payload, dict):
            continue
        environment_id = str(payload.get("environment_id", "")).strip().lower()
        if environment_id:
            records[environment_id] = payload
    return records


def _load_scene_contracts(project_dir: Path) -> dict[str, dict[str, Any]]:
    records: dict[str, dict[str, Any]] = {}
    for path in _scene_contract_paths(project_dir):
        payload = read_json(path)
        if not isinstance(payload, dict):
            continue
        scene_id = str(payload.get("scene_id", "")).strip().upper()
        if scene_id:
            records[scene_id] = payload
    return records


def _load_shot_packages(project_dir: Path) -> list[dict[str, Any]]:
    shots: list[dict[str, Any]] = []
    for path in _shot_index_paths(project_dir):
        payload = read_json(path)
        if not isinstance(payload, list):
            continue
        for item in payload:
            if isinstance(item, dict):
                shots.append(item)
    shots.sort(key=lambda item: (str(item.get("chapter_id", "")), str(item.get("scene_id", "")), int(item.get("shot_order", 0))))
    return shots


def _load_descriptor_records(project_dir: Path, kind: str) -> dict[str, dict[str, Any]]:
    records: dict[str, dict[str, Any]] = {}
    for path in _descriptor_paths(project_dir, kind):
        payload = read_json(path)
        if not isinstance(payload, dict):
            continue
        canonical_id = str(payload.get("canonical_id", "")).strip().lower()
        if canonical_id:
            records[canonical_id] = payload
    return records


def _is_film_facing_character_entry(entry: dict[str, Any], bible: dict[str, Any]) -> bool:
    return _is_film_facing_character(entry, bible) and str(bible.get("status", "canonical")).strip() == "canonical"


def _is_film_facing_environment_entry(entry: dict[str, Any], bible: dict[str, Any]) -> bool:
    return _is_film_facing_environment(entry, bible) and str(bible.get("status", "canonical")).strip() == "canonical"


def _character_descriptor(bible: dict[str, Any], descriptor: dict[str, Any] | None = None) -> str:
    parts: list[str] = []
    if descriptor:
        parts.extend(
            _record_descriptor_phrases(
                descriptor,
                [
                    "sex",
                    "age_range",
                    "height",
                    "build",
                    "skin_tone",
                    "hair_color",
                    "hair_style",
                    "eye_color",
                    "face_shape",
                    "facial_hair",
                    "distinctive_features",
                    "costume_layers",
                    "costume_materials",
                    "costume_signature",
                    "silhouette_notes",
                    "recurring_accessories",
                    "posture",
                    "expression_tendency",
                    "physical_presence_notes",
                    "voice_or_presence_notes",
                ],
                strip_terms=[str(bible.get("display_name", "")), str(bible.get("character_id", "")), *[str(alias) for alias in bible.get("aliases", []) if isinstance(alias, str)]],
            )
        )
    for value in [*bible.get("physical_traits", []), bible.get("costume_signature", "")]:
        if isinstance(value, str) and value.strip():
            cleaned = _strip_terms(
                value.strip(),
                [str(bible.get("display_name", "")), str(bible.get("character_id", "")), *[str(alias) for alias in bible.get("aliases", []) if isinstance(alias, str)]],
            )
            if cleaned:
                parts.extend(_descriptor_phrases(cleaned))
    if not parts:
        summary = bible.get("stable_visual_summary", "")
        if isinstance(summary, str) and summary.strip() and not _looks_like_metadata_summary(summary):
            cleaned = _strip_terms(
                summary.strip(),
                [str(bible.get("display_name", "")), str(bible.get("character_id", "")), *[str(alias) for alias in bible.get("aliases", []) if isinstance(alias, str)]],
            )
            if cleaned:
                parts.extend(_descriptor_phrases(cleaned))
    deduped: list[str] = []
    seen: set[str] = set()
    for item in parts:
        if item not in seen:
            seen.add(item)
            deduped.append(item)
    if not deduped:
        deduped.append("described character with stable costume and silhouette")
    return _compact(", ".join(deduped[:4]), limit=240)


def _environment_descriptor(bible: dict[str, Any], descriptor: dict[str, Any] | None = None) -> str:
    parts: list[str] = []
    if descriptor:
        parts.extend(
            _record_descriptor_phrases(
                descriptor,
                [
                    "layout",
                    "scale",
                    "geography",
                    "architecture",
                    "pathways",
                    "camera_friendly_landmarks",
                    "materials",
                    "lighting",
                    "mood",
                    "weather_or_atmosphere",
                    "recurring_anchors",
                    "foreground_midground_background",
                    "depth_cues",
                ],
                strip_terms=[str(bible.get("display_name", "")), str(bible.get("environment_id", ""))],
            )
        )
    for value in [
        bible.get("layout_notes", ""),
        bible.get("lighting", ""),
        bible.get("mood", ""),
        *bible.get("recurring_elements", []),
    ]:
        if isinstance(value, str) and value.strip():
            cleaned = _strip_terms(value.strip(), [str(bible.get("display_name", "")), str(bible.get("environment_id", ""))])
            if cleaned:
                parts.extend(_descriptor_phrases(cleaned))
    if not parts:
        summary = bible.get("visual_summary", "")
        if isinstance(summary, str) and summary.strip():
            cleaned = _strip_terms(summary.strip(), [str(bible.get("display_name", "")), str(bible.get("environment_id", ""))])
            if cleaned:
                parts.extend(_descriptor_phrases(cleaned))
    deduped: list[str] = []
    seen: set[str] = set()
    for item in parts:
        if item not in seen:
            seen.add(item)
            deduped.append(item)
    if not deduped:
        deduped.append("described environment with stable spatial anchors")
    return _compact(", ".join(deduped[:4]), limit=240)


def _shot_character_descriptors(
    shot: dict[str, Any],
    character_bibles: dict[str, dict[str, Any]],
    character_descriptors: dict[str, dict[str, Any]] | None = None,
) -> list[str]:
    descriptors: list[str] = []
    for ref in shot.get("characters_in_frame", []):
        if not isinstance(ref, dict):
            continue
        canonical_id = str(ref.get("canonical_id", "")).strip().lower()
        bible = character_bibles.get(canonical_id)
        descriptor = (character_descriptors or {}).get(canonical_id)
        if bible:
            descriptors.append(_character_descriptor(bible, descriptor))
        else:
            label = str(ref.get("label", "")).strip()
            descriptors.append(_compact(_strip_terms(label or "supporting character", [label]), limit=80))
    if not descriptors:
        descriptors.append("supporting characters")
    seen: set[str] = set()
    deduped: list[str] = []
    for descriptor in descriptors:
        if descriptor not in seen:
            seen.add(descriptor)
            deduped.append(descriptor)
    return deduped[:3]


def _shot_environment_descriptor(
    shot: dict[str, Any],
    environment_bibles: dict[str, dict[str, Any]],
    environment_descriptors: dict[str, dict[str, Any]] | None = None,
) -> str:
    env = shot.get("environment")
    if isinstance(env, dict):
        canonical_id = str(env.get("canonical_id", "")).strip().lower()
        bible = environment_bibles.get(canonical_id)
        descriptor = (environment_descriptors or {}).get(canonical_id)
        if bible:
            return _environment_descriptor(bible, descriptor)
        label = str(env.get("label", "")).strip()
        if label:
            cleaned = _compact(
                _strip_terms(label, [str(env.get("canonical_id", "")), str(env.get("display_name", ""))]),
                limit=120,
            )
            if cleaned and cleaned != label:
                return cleaned
    return "described environment with stable spatial continuity"


def _base_inputs(
    *,
    subject_kind: str,
    subject_id: str,
    source_artifact_ids: list[str],
    reference_mode: str,
    variant_name: str,
    prompt_enhancer_profile: str,
    change_budget: str,
    reuse_policy: str,
) -> dict[str, str]:
    return {
        "subject_kind": subject_kind,
        "subject_id": subject_id,
        "source_artifact_ids": "; ".join(source_artifact_ids),
        "reference_mode": reference_mode,
        "variant_name": variant_name,
        "lens_family": "neutral_reference",
        "composition_lock": "preserve canonical identity and framing rules",
        "trait_lock": "preserve stable visual canon",
        "image_to_image_source": "",
        "change_budget": change_budget,
        "reuse_policy": reuse_policy,
        "variant_policy": variant_name,
        "review_notes": "",
        "prompt_enhancer_mode": "comfyui_text_prompt_enhancer",
        "prompt_enhancer_profile": prompt_enhancer_profile,
        "target_models": "qwen_image; flux; z_image",
    }


def _package_for_character(
    *,
    project_dir: Path,
    bible: dict[str, Any],
    descriptor: dict[str, Any] | None,
    variant: tuple[str, str, str],
) -> tuple[PromptPackage, Path, list[str]]:
    variant_key, variant_title, variant_hint = variant
    character_id = str(bible.get("character_id", "")).strip().lower()
    display_name = str(bible.get("display_name", character_id)).strip() or character_id
    descriptor_text = _character_descriptor(bible, descriptor)
    title = f"{display_name} Character Reference - {variant_title}"
    prompt_id = f"{character_id}_{variant_key}_prompt"
    positive_prompt = _compact(
        f"Film character reference sheet, {variant_hint}, {descriptor_text}, clean neutral studio background, clear silhouette, consistent costume layers, consistent facial structure, no narrative action, no text, no watermark.",
        limit=320,
    )
    package_path = project_dir / PROMPT_PREP_ROOT / "characters" / character_id / f"{variant_key}_prompt.md"
    sources = [
        project_dir / "02_story_analysis" / "bibles" / "characters" / f"CHAR_{character_id}.json",
    ]
    markdown_source = project_dir / "02_story_analysis" / "bibles" / "characters" / f"CHAR_{character_id}.md"
    if markdown_source.exists():
        sources.append(markdown_source)
    source_artifact_ids = list(dict.fromkeys(path.stem for path in sources))
    inputs = _base_inputs(
        subject_kind="character",
        subject_id=character_id,
        source_artifact_ids=source_artifact_ids,
        reference_mode="character_reference_sheet",
        variant_name=variant_key,
        prompt_enhancer_profile="character_reference",
        change_budget="preserve identity, costume, and silhouette",
        reuse_policy="reuse canonical visual canon",
    )
    package = PromptPackage(
        path=package_path,
        title=title,
        prompt_id=prompt_id,
        purpose="Prepare a compact character reference prompt for enhancer-safe generation.",
        workflow_type="still.t2i.klein.distilled",
        positive_prompt=positive_prompt,
        negative_prompt=GENERIC_NEGATIVE_PROMPT,
        inputs_markdown="\n".join(f"- {key}: {value}" for key, value in inputs.items()),
        continuity_notes_markdown="\n".join(
            [
                "- Preserve canonical identity, costume silhouette, and body proportions.",
                f"- Variant: {variant_title}.",
                "- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.",
                "- Avoid proper nouns in the prompt body unless text is meant to appear on screen.",
            ]
        ),
        sources_markdown="\n".join(f"- {path}" for path in sources),
    )
    return package, package_path, [str(path) for path in sources]


def _package_for_environment(
    *,
    project_dir: Path,
    bible: dict[str, Any],
    descriptor: dict[str, Any] | None,
    variant: tuple[str, str, str],
) -> tuple[PromptPackage, Path, list[str]]:
    variant_key, variant_title, variant_hint = variant
    environment_id = str(bible.get("environment_id", "")).strip().lower()
    display_name = str(bible.get("display_name", environment_id)).strip() or environment_id
    descriptor_text = _environment_descriptor(bible, descriptor)
    title = f"{display_name} Environment Reference - {variant_title}"
    prompt_id = f"{environment_id}_{variant_key}_prompt"
    positive_prompt = _compact(
        f"Film environment reference sheet, {variant_hint}, {descriptor_text}, clear spatial layout, readable anchors and depth cues, no characters, no text, no watermark.",
        limit=320,
    )
    package_path = project_dir / PROMPT_PREP_ROOT / "environments" / environment_id / f"{variant_key}_prompt.md"
    sources = [
        project_dir / "02_story_analysis" / "bibles" / "environments" / f"ENV_{environment_id}.json",
    ]
    markdown_source = project_dir / "02_story_analysis" / "bibles" / "environments" / f"ENV_{environment_id}.md"
    if markdown_source.exists():
        sources.append(markdown_source)
    source_artifact_ids = list(dict.fromkeys(path.stem for path in sources))
    inputs = _base_inputs(
        subject_kind="environment",
        subject_id=environment_id,
        source_artifact_ids=source_artifact_ids,
        reference_mode="environment_reference_sheet",
        variant_name=variant_key,
        prompt_enhancer_profile="environment_reference",
        change_budget="preserve geography, lighting, and anchors",
        reuse_policy="reuse canonical spatial canon",
    )
    package = PromptPackage(
        path=package_path,
        title=title,
        prompt_id=prompt_id,
        purpose="Prepare a compact environment reference prompt for enhancer-safe generation.",
        workflow_type="still.t2i.klein.distilled",
        positive_prompt=positive_prompt,
        negative_prompt=GENERIC_NEGATIVE_PROMPT,
        inputs_markdown="\n".join(f"- {key}: {value}" for key, value in inputs.items()),
        continuity_notes_markdown="\n".join(
            [
                "- Preserve geographic layout, scale, lighting, and recurring anchors.",
                f"- Variant: {variant_title}.",
                "- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.",
                "- Avoid proper nouns in the prompt body unless text is meant to appear on screen.",
            ]
        ),
        sources_markdown="\n".join(f"- {path}" for path in sources),
    )
    return package, package_path, [str(path) for path in sources]


def _package_for_shot(
    *,
    project_dir: Path,
    scene_contract: dict[str, Any],
    shot: dict[str, Any],
    variant: tuple[str, str, str],
    character_bibles: dict[str, dict[str, Any]],
    environment_bibles: dict[str, dict[str, Any]],
    scene_descriptor: dict[str, Any] | None = None,
    shot_descriptor: dict[str, Any] | None = None,
    character_descriptors: dict[str, dict[str, Any]] | None = None,
    environment_descriptors: dict[str, dict[str, Any]] | None = None,
) -> tuple[PromptPackage, Path, list[str], list[str]]:
    variant_key, variant_title, variant_hint = variant
    scene_id = str(shot.get("scene_id", "")).strip().upper()
    chapter_id = str(shot.get("chapter_id", "")).strip().upper() or scene_id[:5]
    shot_id = str(shot.get("shot_id", "")).strip().upper()
    shot_type = str(shot.get("shot_type", "")).strip() or "shot"
    shot_title = str(shot.get("shot_title", "")).strip() or shot_id
    scene_title = str(scene_contract.get("scene_title", "")).strip() or scene_id
    scene_descriptor_values = (scene_descriptor or {}).get("field_values", {}) if isinstance((scene_descriptor or {}).get("field_values", {}), dict) else {}
    shot_descriptor_values = (shot_descriptor or {}).get("field_values", {}) if isinstance((shot_descriptor or {}).get("field_values", {}), dict) else {}
    scene_arc = _first_nonempty(
        scene_descriptor_values.get("emotional_beat", ""),
        str(scene_contract.get("emotional_arc", "")).strip(),
    )
    characters = _shot_character_descriptors(shot, character_bibles, character_descriptors)
    environment_descriptor = _shot_environment_descriptor(shot, environment_bibles, environment_descriptors)
    strip_terms: list[str] = [scene_id, scene_title, shot_id, str(shot.get("shot_title", "")).strip()]
    for ref in shot.get("characters_in_frame", []):
        if not isinstance(ref, dict):
            continue
        for key in ("label", "canonical_id", "display_name"):
            value = str(ref.get(key, "")).strip()
            if value:
                strip_terms.append(value)
        bible = character_bibles.get(str(ref.get("canonical_id", "")).strip().lower())
        if bible:
            strip_terms.extend(
                str(value).strip()
                for value in [bible.get("display_name", ""), bible.get("character_id", ""), *bible.get("aliases", [])]
                if isinstance(value, str) and str(value).strip()
            )
    env_ref = shot.get("environment")
    if isinstance(env_ref, dict):
        for key in ("label", "canonical_id", "display_name"):
            value = str(env_ref.get(key, "")).strip()
            if value:
                strip_terms.append(value)
        bible = environment_bibles.get(str(env_ref.get("canonical_id", "")).strip().lower())
        if bible:
            strip_terms.extend(
                str(value).strip()
                for value in [bible.get("display_name", ""), bible.get("environment_id", "")]
                if isinstance(value, str) and str(value).strip()
            )
    camera_description = _compact(
        _strip_terms(
            _first_nonempty(
                shot_descriptor_values.get("camera_motion", ""),
                shot_descriptor_values.get("perspective_notes", ""),
                shot.get("camera_description", ""),
                fallback="",
            ),
            strip_terms,
        ),
        limit=180,
    )
    composition_hint = _first_nonempty(
        shot_descriptor_values.get("framing", ""),
        shot_descriptor_values.get("spatial_continuity", ""),
        shot.get("composition", ""),
        fallback={
            "primary_keyframe": "balanced framing with clear spatial separation",
            "alternate_angle": "shifted perspective with preserved subject spacing",
            "zoom_variant": "tighter framing on the same moment",
            "consistency_repair": "continuity-preserving framing with exact pose and costume locks",
        }.get(variant_key, variant_hint),
    )
    continuity = _coerce_bullets(shot.get("continuity_constraints", []), scene_contract.get("continuity_constraints", []))
    variant_camera = {
        "primary_keyframe": "Primary keyframe with balanced composition and clear subject placement.",
        "alternate_angle": "Alternate angle with the same beat and preserved continuity.",
        "zoom_variant": "Tighter zoom with the same beat and preserved continuity.",
        "consistency_repair": "Continuity repair pass that preserves pose, costume, lighting, and spatial relationships.",
    }.get(variant_key, variant_hint)
    title = f"{shot_id} Shot Prompt - {variant_title}"
    prompt_id = f"{scene_id}_{shot_id}_{variant_key}_prompt"
    prompt_parts = [
        "Film shot prompt",
        variant_camera,
        _compact(_strip_terms(scene_arc or scene_contract.get("production_intent", "") or scene_title, strip_terms), limit=140),
        camera_description,
        _compact(_strip_terms(composition_hint, strip_terms), limit=160),
        f"Characters: {', '.join(characters)}",
        f"Environment: {environment_descriptor}",
        "Keep continuity exact across costume, silhouette, lighting, and spatial relationships.",
        "Avoid proper nouns in the prompt body unless text is meant to appear on screen.",
        "No text, no watermark, no logo.",
    ]
    positive_prompt = _compact(". ".join(part for part in prompt_parts if part), limit=420)
    package_path = project_dir / PROMPT_PREP_ROOT / "shots" / chapter_id / scene_id / shot_id / f"{variant_key}_prompt.md"
    sources = [
        project_dir / "02_story_analysis" / "contracts" / "scenes" / chapter_id / f"{scene_id}.json",
        project_dir / "02_story_analysis" / "contracts" / "shots" / chapter_id / scene_id / "SHOT_INDEX.json",
        project_dir / "02_story_analysis" / "contracts" / "shots" / chapter_id / scene_id / shot_id / "DIALOGUE.json",
    ]
    source_artifact_ids = [path.stem for path in sources if path.exists()]
    if scene_contract.get("characters_required"):
        source_artifact_ids.extend(
            str(ref.get("canonical_id", ref.get("label", ""))).strip()
            for ref in scene_contract.get("characters_required", [])
            if isinstance(ref, dict)
        )
    inputs = _base_inputs(
        subject_kind="shot",
        subject_id=shot_id,
        source_artifact_ids=[artifact for artifact in source_artifact_ids if artifact],
        reference_mode="shot_prompt_bundle",
        variant_name=variant_key,
        prompt_enhancer_profile="shot_reference",
        change_budget="preserve scene continuity and shot intent",
        reuse_policy="reuse canonical shot contract canon",
    )
    inputs.update(
        {
            "scene_id": scene_id,
            "chapter_id": chapter_id,
            "shot_type": shot_type,
            "camera_description": camera_description,
            "composition": composition_hint,
            "prompt_family": "shot_prompt",
        }
    )
    package = PromptPackage(
        path=package_path,
        title=title,
        prompt_id=prompt_id,
        purpose="Prepare a compact shot prompt for enhancer-safe generation.",
        workflow_type="still.scene_build.four_ref.klein.distilled",
        positive_prompt=positive_prompt,
        negative_prompt=GENERIC_NEGATIVE_PROMPT,
        inputs_markdown="\n".join(f"- {key}: {value}" for key, value in inputs.items()),
        continuity_notes_markdown="\n".join(
            [
                f"- Scene: {scene_id} / {scene_title}.",
                f"- Variant: {variant_title}.",
                *[f"- {item}" for item in continuity[:6]],
                "- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.",
            ]
        ),
        sources_markdown="\n".join(f"- {path}" for path in sources if path.exists()),
    )
    review_notes: list[str] = []
    if not characters:
        review_notes.append("No stable character descriptors could be derived.")
    if "None" in environment_descriptor or "unresolved" in environment_descriptor.lower():
        review_notes.append("Environment descriptor is unresolved or thin.")
    return package, package_path, [str(path) for path in sources if path.exists()], review_notes


def _coerce_bullets(*values: Any) -> list[str]:
    bullets: list[str] = []
    for value in values:
        if isinstance(value, list):
            for item in value:
                if isinstance(item, str) and item.strip():
                    bullets.append(item.strip())
        elif isinstance(value, str) and value.strip():
            bullets.extend(part.strip() for part in re.split(r"[;\n]", value) if part.strip())
    deduped: list[str] = []
    seen: set[str] = set()
    for item in bullets:
        if item not in seen:
            seen.add(item)
            deduped.append(item)
    return deduped


def _write_index(path: Path, records: list[dict[str, Any]], *, title: str) -> None:
    lines = [f"# {title}", ""]
    if not records:
        lines.append("- No entries.")
    else:
        for record in records:
            lines.append(
                f"- `{record['prompt_id']}` - {record['title']} "
                f"(subject_kind={record['subject_kind']}, status={record['status']}, variant={record['variant_name']})"
            )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _write_review_queue(path: Path, queue: list[dict[str, Any]], *, title: str) -> None:
    lines = [f"# {title}", ""]
    if not queue:
        lines.append("- No review items.")
    else:
        for item in queue:
            lines.append(f"- `{item.get('prompt_id', '')}`")
            for issue in item.get("issues", []):
                lines.append(f"  - {issue}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def run_prompt_preparation(project_slug: str, *, force: bool = False) -> PromptPreparationSummary:
    project_dir = create_project(project_slug)
    root = project_dir / PROMPT_PREP_ROOT
    review_root = root / "review"
    root.mkdir(parents=True, exist_ok=True)
    review_root.mkdir(parents=True, exist_ok=True)

    character_bibles = _load_character_bibles(project_dir)
    environment_bibles = _load_environment_bibles(project_dir)
    scene_contracts = _load_scene_contracts(project_dir)
    shot_packages = _load_shot_packages(project_dir)
    character_descriptors = _load_descriptor_records(project_dir, "character")
    environment_descriptors = _load_descriptor_records(project_dir, "environment")
    scene_descriptors = _load_descriptor_records(project_dir, "scene")
    shot_descriptors = _load_descriptor_records(project_dir, "shot")

    written_files: list[str] = []
    warnings: list[str] = []
    review_queue: list[dict[str, Any]] = []
    index_records: list[dict[str, Any]] = []
    total_entries = 0
    synthesized_count = 0
    reused_count = 0

    # Character reference bundles.
    for bible in sorted(character_bibles.values(), key=lambda item: str(item.get("character_id", ""))):
        total_entries += 1
        if not _is_film_facing_character_entry(bible, bible):
            review_queue.append(
                {
                    "prompt_id": str(bible.get("character_id", "")),
                    "subject_kind": "character",
                    "subject_id": str(bible.get("character_id", "")),
                    "variant_name": "review",
                    "title": f"{bible.get('display_name', bible.get('character_id', 'character'))} Character Reference Review",
                    "issues": [
                        f"Character status={bible.get('status', 'unknown')} entity_kind={bible.get('entity_kind', 'unknown')}.",
                        "Kept out of the main prompt-prep index because it is not a canonical film-facing individual.",
                    ],
                }
            )
            continue
        for variant in CHARACTER_VARIANTS:
            descriptor = character_descriptors.get(str(bible.get("character_id", "")).strip().lower())
            package, package_path, sources = _package_for_character(project_dir=project_dir, bible=bible, descriptor=descriptor, variant=variant)
            if _write_prompt_package_if_changed(package_path, package, force=force):
                synthesized_count += 1
                written_files.append(str(package_path))
            else:
                reused_count += 1
            index_records.append(
                {
                    "prompt_id": package.prompt_id,
                    "title": package.title,
                    "subject_kind": "character",
                    "subject_id": package.inputs.get("subject_id", ""),
                    "variant_name": package.inputs.get("variant_name", ""),
                    "status": "canonical",
                    "path": str(package_path),
                    "source_fingerprint": _fingerprint(sources),
                }
            )

    # Environment reference bundles.
    for bible in sorted(environment_bibles.values(), key=lambda item: str(item.get("environment_id", ""))):
        total_entries += 1
        if not _is_film_facing_environment_entry(bible, bible):
            review_queue.append(
                {
                    "prompt_id": str(bible.get("environment_id", "")),
                    "subject_kind": "environment",
                    "subject_id": str(bible.get("environment_id", "")),
                    "variant_name": "review",
                    "title": f"{bible.get('display_name', bible.get('environment_id', 'environment'))} Environment Reference Review",
                    "issues": [
                        f"Environment status={bible.get('status', 'unknown')} entity_kind={bible.get('entity_kind', 'unknown')}.",
                        "Kept out of the main prompt-prep index because it is not a canonical film-facing environment.",
                    ],
                }
            )
            continue
        for variant in ENVIRONMENT_VARIANTS:
            descriptor = environment_descriptors.get(str(bible.get("environment_id", "")).strip().lower())
            package, package_path, sources = _package_for_environment(project_dir=project_dir, bible=bible, descriptor=descriptor, variant=variant)
            if _write_prompt_package_if_changed(package_path, package, force=force):
                synthesized_count += 1
                written_files.append(str(package_path))
            else:
                reused_count += 1
            index_records.append(
                {
                    "prompt_id": package.prompt_id,
                    "title": package.title,
                    "subject_kind": "environment",
                    "subject_id": package.inputs.get("subject_id", ""),
                    "variant_name": package.inputs.get("variant_name", ""),
                    "status": "canonical",
                    "path": str(package_path),
                    "source_fingerprint": _fingerprint(sources),
                }
            )

    # Shot prompt bundles.
    for shot in shot_packages:
        total_entries += 1
        scene_id = str(shot.get("scene_id", "")).strip().upper()
        shot_id = str(shot.get("shot_id", "")).strip().upper()
        if not scene_id or not shot_id:
            continue
        scene_contract = scene_contracts.get(scene_id, {})
        scene_descriptor = scene_descriptors.get(scene_id.lower())
        shot_descriptor = shot_descriptors.get(f"{scene_id.lower()}_{shot_id.lower()}")
        for variant in SHOT_VARIANTS:
            package, package_path, sources, review_notes = _package_for_shot(
                project_dir=project_dir,
                scene_contract=scene_contract,
                shot=shot,
                variant=variant,
                character_bibles=character_bibles,
                environment_bibles=environment_bibles,
                scene_descriptor=scene_descriptor,
                shot_descriptor=shot_descriptor,
                character_descriptors=character_descriptors,
                environment_descriptors=environment_descriptors,
            )
            if _write_prompt_package_if_changed(package_path, package, force=force):
                synthesized_count += 1
                written_files.append(str(package_path))
            else:
                reused_count += 1
            index_records.append(
                {
                    "prompt_id": package.prompt_id,
                    "title": package.title,
                    "subject_kind": "shot",
                    "subject_id": package.inputs.get("subject_id", ""),
                    "variant_name": package.inputs.get("variant_name", ""),
                    "status": "generated" if not review_notes else "review",
                    "path": str(package_path),
                    "source_fingerprint": _fingerprint(sources),
                }
            )
            if review_notes:
                review_queue.append(
                    {
                        "prompt_id": package.prompt_id,
                        "subject_kind": "shot",
                        "subject_id": package.inputs.get("subject_id", ""),
                        "variant_name": package.inputs.get("variant_name", ""),
                        "title": package.title,
                        "issues": review_notes,
                    }
                )

    index_path = root / "PROMPT_PREPARATION_INDEX.md"
    index_json = root / "PROMPT_PREPARATION_INDEX.json"
    review_index_path = root / "PROMPT_PREPARATION_REVIEW_INDEX.md"
    review_index_json = root / "PROMPT_PREPARATION_REVIEW_INDEX.json"
    review_queue_path = review_root / "PROMPT_PREPARATION_REVIEW_QUEUE.md"
    review_queue_json = review_root / "PROMPT_PREPARATION_REVIEW_QUEUE.json"

    _write_index(index_path.with_suffix(".md"), index_records, title="Prompt Preparation Index")
    write_json(index_json, index_records)
    review_records = [
        {
            "prompt_id": item.get("prompt_id", ""),
            "title": item.get("title", ""),
            "subject_kind": item.get("subject_kind", ""),
            "subject_id": item.get("subject_id", ""),
            "variant_name": item.get("variant_name", ""),
            "status": "review",
            "path": item.get("path", ""),
        }
        for item in review_queue
    ]
    review_records.extend(record for record in index_records if record["status"] == "review")
    _write_index(review_index_path, review_records, title="Prompt Preparation Review Index")
    write_json(review_index_json, review_records)
    _write_review_queue(review_queue_path, review_queue, title="Prompt Preparation Review Queue")
    write_json(review_queue_json, review_queue)
    written_files.extend(
        [
            str(index_path.with_suffix(".md")),
            str(index_json),
            str(review_index_path),
            str(review_index_json),
            str(review_queue_path),
            str(review_queue_json),
        ]
    )

    return PromptPreparationSummary(
        project_slug=project_slug,
        total_entries=total_entries,
        synthesized_count=synthesized_count,
        reused_count=reused_count,
        review_queue_count=len(review_queue),
        written_files=written_files,
        warnings=warnings,
    )
