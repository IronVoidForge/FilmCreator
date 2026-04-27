"""
Overnight pipeline resume validator.

Finds the first incomplete stage for a project/chapter slice.
Validation is content-aware: existing but empty indexes do not count as complete.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Callable

from .chapter_selection import normalize_chapter_id
from .prompt_package import parse_prompt_package


STAGES: list[str] = [
    "story_analysis",
    "character_taxonomy",
    "identity_refinement",
    "character_bibles",
    "character_visual_evidence",
    "environment_bibles",
    "visual_fallbacks",
    "scene_contracts",
    "scene_bindings",
    "shot_packages",
    "dialogue_timeline",
    "descriptor_enrichment",
    "prompt_preparation",
    "quality_grading",
]


def _repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def _project_root(project_slug: str) -> Path:
    return _repo_root() / "projects" / project_slug


def _read_json(path: Path) -> dict[str, Any] | list[Any]:
    try:
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)
        return data
    except Exception:
        return {}


def _count_records(data: dict[str, Any] | list[Any]) -> int:
    if isinstance(data, list):
        return len(data)
    if not isinstance(data, dict):
        return 0
    for key in ("total_entries", "total_records", "record_count", "count", "synthesized_count"):
        value = data.get(key)
        if isinstance(value, int) and value > 0:
            return value
    for key in ("records", "entries", "items", "families", "artifacts"):
        value = data.get(key)
        if isinstance(value, list):
            return len(value)
        if isinstance(value, dict):
            return len(value)
    return 0


def _is_nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _string_list(value: Any) -> list[str]:
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    if _is_nonempty_string(value):
        return [str(value).strip()]
    return []


def _chapter_ids_from_value(value: Any) -> set[str]:
    found: set[str] = set()
    if isinstance(value, dict):
        for nested in value.values():
            found.update(_chapter_ids_from_value(nested))
        return found
    if isinstance(value, list):
        for item in value:
            found.update(_chapter_ids_from_value(item))
        return found
    if not _is_nonempty_string(value):
        return found
    text = str(value).strip()
    normalized = normalize_chapter_id(text)
    if normalized:
        found.add(normalized)
    for token in text.replace(",", " ").split():
        normalized = normalize_chapter_id(token)
        if normalized:
            found.add(normalized)
    return found


def _chapter_coverage_from_records(records: list[dict[str, Any]]) -> set[str]:
    coverage: set[str] = set()
    for record in records:
        if not isinstance(record, dict):
            continue
        for key in ("chapter_mentions", "chapter_id", "first_seen_chapter", "last_seen_chapter", "artifact_path", "path", "prompt_id", "subject_id"):
            coverage.update(_chapter_ids_from_value(record.get(key)))
    return coverage


def _matches_requested_chapters(records: list[dict[str, Any]], chapters: str) -> tuple[bool, dict[str, Any]]:
    requested = {_chapter_id(number) for number in parse_chapters(chapters)}
    if not requested:
        return True, {"requested": [], "covered": []}
    covered = _chapter_coverage_from_records(records)
    missing = sorted(requested - covered)
    return not missing, {"requested": sorted(requested), "covered": sorted(covered), "missing": missing}


def parse_chapters(chapters: str) -> list[int]:
    chapters = (chapters or "").strip().strip('"\'')
    if not chapters:
        return []
    result: list[int] = []
    for part in chapters.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            start_s, end_s = part.split("-", 1)
            start = int(start_s)
            end = int(end_s)
            result.extend(range(start, end + 1))
        else:
            result.append(int(part))
    return sorted(set(result))


def _chapter_id(chapter_num: int) -> str:
    return f"CH{chapter_num:03d}"


def count_source_chapters(project_root: Path) -> int:
    chapters_dir = project_root / "01_source" / "chapters"
    if not chapters_dir.exists():
        return 0
    return len(list(chapters_dir.glob("CH*.md")))


def check_story_analysis(project_root: Path, chapters: str = "") -> tuple[bool, str, dict[str, Any]]:
    analysis_dir = project_root / "02_story_analysis"
    chapter_analysis_dir = analysis_dir / "chapter_analysis"
    if not chapter_analysis_dir.exists():
        return False, "missing chapter_analysis directory", {}

    source_count = count_source_chapters(project_root)
    if source_count <= 0:
        return False, "no source chapters found", {}

    summary_files = list(chapter_analysis_dir.glob("CH*_summary.md"))
    world_global = analysis_dir / "world" / "global"

    missing = []
    if len(summary_files) < source_count:
        missing.append(f"chapter summaries {len(summary_files)}/{source_count}")
    for required in ["CHARACTER_REGISTRY_GLOBAL.json", "ENVIRONMENT_REGISTRY_GLOBAL.json", "WORLD_SEQUENCE_STATE.json"]:
        if not (world_global / required).exists():
            missing.append(required)

    if missing:
        return False, "missing " + ", ".join(missing), {
            "source_count": source_count,
            "summary_count": len(summary_files),
        }

    return True, f"{len(summary_files)} chapter summaries and global registries found", {
        "source_count": source_count,
        "summary_count": len(summary_files),
    }


def check_character_taxonomy(project_root: Path, chapters: str = "") -> tuple[bool, str, dict[str, Any]]:
    taxonomy_dir = project_root / "02_story_analysis" / "taxonomy" / "characters"
    index_file = taxonomy_dir / "CHARACTER_TAXONOMY_INDEX.json"
    if not index_file.exists():
        return False, "missing CHARACTER_TAXONOMY_INDEX.json", {}

    files = [p for p in taxonomy_dir.glob("CHAR_*_TAXONOMY.json") if p.is_file()]
    valid = 0
    for path in files:
        data = _read_json(path)
        if not isinstance(data, dict):
            continue
        if (
            ("primary_type" in data or "entity_kind" in data)
            and "morphology" in data
            and "renderability" in data
            and "confidence" in data
            and "direct_evidence_records" in data
        ):
            valid += 1

    if valid <= 0:
        return False, "taxonomy index exists but no valid taxonomy JSONs found", {"files": len(files), "valid": valid}

    return True, f"{valid}/{len(files)} taxonomy JSONs contain required fields", {"files": len(files), "valid": valid}


def check_identity_refinement(project_root: Path, chapters: str = "") -> tuple[bool, str, dict[str, Any]]:
    refinement_dir = project_root / "02_story_analysis" / "world" / "refinement"
    required = [
        "REFINEMENT_RESULT.json",
        "REFINEMENT_DECISIONS.json",
        "CHARACTER_REGISTRY_GLOBAL_REFINED.json",
        "ENVIRONMENT_REGISTRY_GLOBAL_REFINED.json",
    ]
    missing = [name for name in required if not (refinement_dir / name).exists()]
    if missing:
        return False, "missing " + ", ".join(missing), {}

    return True, "refinement result, decisions, and refined registries found", {}


def check_character_bibles(project_root: Path, chapters: str = "") -> tuple[bool, str, dict[str, Any]]:
    bibles_dir = project_root / "02_story_analysis" / "bibles" / "characters"
    index_file = bibles_dir / "CHARACTER_BIBLE_INDEX.json"
    if not index_file.exists():
        return False, "missing CHARACTER_BIBLE_INDEX.json", {}

    files = [p for p in bibles_dir.glob("CHAR_*.json") if p.is_file()]
    valid = 0
    for path in files:
        data = _read_json(path)
        if not isinstance(data, dict):
            continue
        if all(k in data for k in ["entity_taxonomy", "alias_resolution", "associated_entities", "visual_production_fallback"]):
            valid += 1

    if valid <= 0:
        return False, "character bible index exists but no taxonomy-aware bibles found", {"files": len(files), "valid": valid}

    return True, f"{valid}/{len(files)} character bibles contain taxonomy/fallback fields", {"files": len(files), "valid": valid}


def check_environment_bibles(project_root: Path, chapters: str = "") -> tuple[bool, str, dict[str, Any]]:
    bibles_dir = project_root / "02_story_analysis" / "bibles" / "environments"
    index_file = bibles_dir / "ENVIRONMENT_BIBLE_INDEX.json"
    if not index_file.exists():
        return False, "missing ENVIRONMENT_BIBLE_INDEX.json", {}

    files = [p for p in bibles_dir.glob("*.json") if p.name != "ENVIRONMENT_BIBLE_INDEX.json" and "REVIEW" not in p.name]
    if not files:
        return False, "environment bible index exists but no environment bible JSONs found", {}

    return True, f"{len(files)} environment bible JSONs found", {"files": len(files)}


def check_character_visual_evidence(project_root: Path, chapters: str = "") -> tuple[bool, str, dict[str, Any]]:
    evidence_dir = project_root / "02_story_analysis" / "bibles" / "characters" / "visual_evidence"
    index_file = evidence_dir / "CHARACTER_VISUAL_EVIDENCE_INDEX.json"
    if not index_file.exists():
        return False, "missing CHARACTER_VISUAL_EVIDENCE_INDEX.json", {}

    data = _read_json(index_file)
    if not isinstance(data, dict):
        return False, "CHARACTER_VISUAL_EVIDENCE_INDEX.json is not a valid dict", {}

    records = data.get("records", [])
    if not isinstance(records, list):
        return False, "CHARACTER_VISUAL_EVIDENCE_INDEX records is not a list", {}

    bible_dir = project_root / "02_story_analysis" / "bibles" / "characters"
    bible_count = len([p for p in bible_dir.glob("CHAR_*.json") if p.is_file()])
    if bible_count <= 0:
        return False, "no character bible JSONs found for visual evidence refinement", {}

    return True, "character visual evidence refinement index found", {
        "records": len(records),
        "patched_count": data.get("patched_count", 0),
        "review_count": data.get("review_count", 0),
        "bible_count": bible_count,
    }


def check_visual_fallbacks(project_root: Path, chapters: str = "") -> tuple[bool, str, dict[str, Any]]:
    path = project_root / "02_story_analysis" / "world" / "global" / "VISUAL_FALLBACKS.json"
    if not path.exists():
        return False, "missing VISUAL_FALLBACKS.json", {}

    data = _read_json(path)
    if not isinstance(data, dict):
        return False, "VISUAL_FALLBACKS.json is not a valid dict", {}
    
    missing: list[str] = []
    if not _is_nonempty_string(data.get("source_title")):
        missing.append("source_title")
    if not _is_nonempty_string(data.get("book_visual_context")):
        missing.append("book_visual_context")

    for family in ("character_fallbacks", "environment_fallbacks"):
        payload = data.get(family)
        if not isinstance(payload, dict) or not payload or not any(_is_nonempty_string(value) for value in payload.values()):
            missing.append(family)
        elif not _is_nonempty_string(payload.get("general")):
            missing.append(f"{family}.general")

    negatives = data.get("negative_terms")
    if not isinstance(negatives, dict):
        missing.append("negative_terms")
    else:
        if not _string_list(negatives.get("character_wardrobe")):
            missing.append("negative_terms.character_wardrobe")
        if not _string_list(negatives.get("environment")):
            missing.append("negative_terms.environment")

    has_digest = _is_nonempty_string(data.get("context_digest"))
    has_sources = bool(_string_list(data.get("source_context_files")))
    if not has_digest and not has_sources:
        missing.append("context_digest/source_context_files")

    if missing:
        return False, "VISUAL_FALLBACKS missing/empty required content: " + ", ".join(missing), {
            "has_context_digest": has_digest,
            "source_context_files": len(_string_list(data.get("source_context_files"))),
        }

    return True, "visual fallbacks contain source title, context, fallback buckets, negatives, and source context", {
        "source_context_files": len(_string_list(data.get("source_context_files"))),
        "has_context_digest": has_digest,
    }


def check_scene_contracts(project_root: Path, chapters: str = "") -> tuple[bool, str, dict[str, Any]]:
    # Based on actual observation: contracts are NOT in contracts/ root
    # They should be in contracts/scenes/ or similar
    contracts_base = project_root / "02_story_analysis" / "contracts"
    
    # Check multiple possible locations
    possible_dirs = [
        contracts_base / "scenes",
        contracts_base / "scene_contracts",
        contracts_base,
    ]
    
    chapter_nums = parse_chapters(chapters)
    
    # If no chapters specified, look for any contracts
    if not chapter_nums:
        for check_dir in possible_dirs:
            if check_dir.exists():
                files = list(check_dir.rglob("*.json"))
                files = [f for f in files if "scene" in f.name.lower() and "binding" not in f.name.lower() and "shot" not in f.name.lower()]
                if files:
                    return True, f"{len(files)} scene contract files found", {"files": len(files)}
        return False, "no scene contract files found", {"files": 0}
    
    # Check for specific chapters
    missing: list[str] = []
    counts: dict[str, int] = {}
    for ch_num in chapter_nums:
        ch = _chapter_id(ch_num)
        found = False
        for check_dir in possible_dirs:
            if not check_dir.exists():
                continue
            # Look for chapter-specific contracts
            patterns = [
                f"{ch}/**/*.json",
                f"{ch}_*.json",
                f"*/{ch}/*.json",
            ]
            for pattern in patterns:
                files = list(check_dir.glob(pattern))
                files = [f for f in files if "scene" in f.name.lower() and "binding" not in f.name.lower() and "shot" not in f.name.lower()]
                if files:
                    counts[ch] = len(files)
                    found = True
                    break
            if found:
                break
        if not found:
            missing.append(ch)
            counts[ch] = 0
    
    if missing:
        return False, "missing scene contracts for " + ", ".join(missing), counts
    
    return True, "scene contracts found for requested chapters", counts


def check_scene_bindings(project_root: Path, chapters: str = "") -> tuple[bool, str, dict[str, Any]]:
    contracts_base = project_root / "02_story_analysis" / "contracts"
    
    possible_dirs = [
        contracts_base / "scene_bindings",
        contracts_base / "bindings",
        contracts_base / "scenes",
        contracts_base,
    ]
    
    chapter_nums = parse_chapters(chapters)
    
    if not chapter_nums:
        for check_dir in possible_dirs:
            if check_dir.exists():
                files = list(check_dir.rglob("*.json"))
                files = [f for f in files if "binding" in f.name.lower()]
                if files:
                    return True, f"{len(files)} scene binding files found", {"files": len(files)}
        return False, "no scene binding files found", {"files": 0}
    
    missing: list[str] = []
    counts: dict[str, int] = {}
    for ch_num in chapter_nums:
        ch = _chapter_id(ch_num)
        found = False
        for check_dir in possible_dirs:
            if not check_dir.exists():
                continue
            patterns = [
                f"{ch}/**/*binding*.json",
                f"{ch}_*binding*.json",
                f"*/{ch}/*binding*.json",
            ]
            for pattern in patterns:
                files = list(check_dir.glob(pattern))
                if files:
                    counts[ch] = len(files)
                    found = True
                    break
            if found:
                break
        if not found:
            missing.append(ch)
            counts[ch] = 0
    
    if missing:
        return False, "missing scene bindings for " + ", ".join(missing), counts
    
    return True, "scene bindings found for requested chapters", counts


def check_shot_packages(project_root: Path, chapters: str = "") -> tuple[bool, str, dict[str, Any]]:
    contracts_base = project_root / "02_story_analysis" / "contracts"
    shots_dir = contracts_base / "shots"
    
    # Check shot package index
    index_candidates = [
        shots_dir / "SHOT_PACKAGE_INDEX.json",
        contracts_base / "SHOT_PACKAGE_INDEX.json",
    ]
    
    index_data = None
    index_path = None
    for candidate in index_candidates:
        if candidate.exists():
            index_data = _read_json(candidate)
            index_path = candidate
            break
    
    # Reject if index is empty array or has zero counts
    if index_data is not None:
        if isinstance(index_data, list) and len(index_data) == 0:
            return False, "SHOT_PACKAGE_INDEX is empty array", {"index_path": str(index_path)}
        if isinstance(index_data, dict):
            scene_count = index_data.get("total_scene_entries", 0)
            shot_count = index_data.get("total_shot_entries", 0)
            synthesized = index_data.get("synthesized_count", 0)
            if scene_count == 0 or shot_count == 0 or synthesized == 0:
                return False, "SHOT_PACKAGE_INDEX has zero scene/shot/synthesized entries", {
                    "index_path": str(index_path),
                    "total_scene_entries": scene_count,
                    "total_shot_entries": shot_count,
                    "synthesized_count": synthesized,
                }
    
    # Check for actual shot files
    chapter_nums = parse_chapters(chapters)
    
    if not chapter_nums:
        if shots_dir.exists():
            files = list(shots_dir.rglob("*.json"))
            files = [f for f in files if "shot" in f.name.lower() and "INDEX" not in f.name and "REVIEW" not in f.name]
            if files:
                return True, f"{len(files)} shot package files found", {"files": len(files)}
        return False, "no shot package files found", {"files": 0}
    
    missing: list[str] = []
    counts: dict[str, int] = {}
    for ch_num in chapter_nums:
        ch = _chapter_id(ch_num)
        if shots_dir.exists():
            patterns = [
                f"{ch}/**/*.json",
                f"{ch}_*.json",
            ]
            found_files = []
            for pattern in patterns:
                files = list(shots_dir.glob(pattern))
                files = [f for f in files if "shot" in f.name.lower() and "INDEX" not in f.name and "REVIEW" not in f.name]
                found_files.extend(files)
            if found_files:
                counts[ch] = len(found_files)
            else:
                missing.append(ch)
                counts[ch] = 0
        else:
            missing.append(ch)
            counts[ch] = 0
    
    if missing:
        return False, "missing shot packages for " + ", ".join(missing), counts
    
    return True, "shot packages found for requested chapters", counts


def check_dialogue_timeline(project_root: Path, chapters: str = "") -> tuple[bool, str, dict[str, Any]]:
    timelines_dir = project_root / "02_story_analysis" / "timelines" / "chapters"
    chapter_nums = parse_chapters(chapters)

    if not chapter_nums:
        files = list(timelines_dir.glob("CH*/*_DIALOGUE_TIMELINE.json")) if timelines_dir.exists() else []
    else:
        files = [
            timelines_dir / _chapter_id(ch_num) / f"{_chapter_id(ch_num)}_DIALOGUE_TIMELINE.json"
            for ch_num in chapter_nums
        ]

    missing = [str(p.name) for p in files if not p.exists()]
    if missing:
        return False, "missing dialogue timeline files: " + ", ".join(missing), {"missing": missing}

    total_scene_bindings = 0
    total_shot_bindings = 0
    total_events = 0
    for path in files:
        if not path.exists():
            continue
        data = _read_json(path)
        if not isinstance(data, dict):
            continue
        total_scene_bindings += int(data.get("total_scene_bindings") or 0)
        total_shot_bindings += int(data.get("total_shot_bindings") or 0)
        total_events += int(data.get("total_events") or 0)

    # Reject if zero bindings (dialogue events may be zero in silent chapters)
    if total_scene_bindings == 0 and total_shot_bindings == 0:
        return False, "dialogue timelines exist but have zero scene and shot bindings", {
            "total_events": total_events,
            "total_scene_bindings": total_scene_bindings,
            "total_shot_bindings": total_shot_bindings,
        }

    return True, "dialogue timelines contain scene/shot binding context", {
        "total_events": total_events,
        "total_scene_bindings": total_scene_bindings,
        "total_shot_bindings": total_shot_bindings,
    }


def check_descriptor_enrichment(project_root: Path, chapters: str = "") -> tuple[bool, str, dict[str, Any]]:
    index_file = project_root / "02_story_analysis" / "descriptors" / "DESCRIPTOR_INDEX.json"
    if not index_file.exists():
        return False, "missing DESCRIPTOR_INDEX.json", {}

    data = _read_json(index_file)
    
    # Reject empty array
    if isinstance(data, list) and len(data) == 0:
        return False, "DESCRIPTOR_INDEX is empty array", {}
    
    if isinstance(data, dict):
        count = _count_records(data)
        synthesized = data.get("synthesized_count", 0)
        if count <= 0 and synthesized <= 0:
            return False, "DESCRIPTOR_INDEX has zero entries", {"count": count, "synthesized_count": synthesized}
        return True, f"descriptor index has {count or synthesized} entries", {"count": count, "synthesized_count": synthesized}
    if isinstance(data, list):
        if not data:
            return False, "DESCRIPTOR_INDEX has zero entries", {"count": 0}
        chapter_ok, details = _matches_requested_chapters([item for item in data if isinstance(item, dict)], chapters)
        if not chapter_ok:
            return False, "descriptor index exists but requested chapter coverage is missing", details
        return True, f"descriptor index has {len(data)} entries with requested chapter coverage", {"count": len(data), **details}
    
    return False, "DESCRIPTOR_INDEX is not valid JSON", {}


def check_prompt_preparation(project_root: Path, chapters: str = "") -> tuple[bool, str, dict[str, Any]]:
    # Reject prompt prep if descriptors are structurally empty
    descriptor_ok, descriptor_reason, descriptor_details = check_descriptor_enrichment(project_root, chapters)
    if not descriptor_ok:
        return False, "descriptor enrichment incomplete, so prompt prep must rerun: " + descriptor_reason, descriptor_details

    # Check for index in prepared/ subdirectory (observed actual location)
    index_candidates = [
        project_root / "03_prompt_packages" / "prepared" / "PROMPT_PREPARATION_INDEX.json",
        project_root / "03_prompt_packages" / "PROMPT_PREPARATION_INDEX.json",
    ]
    index_file = next((p for p in index_candidates if p.exists()), None)
    if index_file is None:
        return False, "missing PROMPT_PREPARATION_INDEX.json", {}

    data = _read_json(index_file)
    
    # Reject empty array
    if isinstance(data, list) and len(data) == 0:
        return False, "prompt preparation index is empty array", {"index": str(index_file)}
    
    if isinstance(data, dict):
        count = _count_records(data)
        synthesized = data.get("synthesized_count", 0)
        if count <= 0 and synthesized <= 0:
            return False, "prompt preparation index has zero entries", {"count": count, "synthesized_count": synthesized, "index": str(index_file)}
        prepared_dir = project_root / "03_prompt_packages" / "prepared"
        prompt_files = list(prepared_dir.rglob("*_prompt.md")) if prepared_dir.exists() else []
        if not prompt_files:
            return False, "no prepared prompt markdown files found", {"index": str(index_file)}
        return True, f"prompt prep index and {len(prompt_files)} prompt files found", {
            "index": str(index_file),
            "prompt_files": len(prompt_files),
        }

    if not isinstance(data, list):
        return False, "prompt preparation index is not valid JSON", {"index": str(index_file)}

    canonical_records = [item for item in data if isinstance(item, dict) and str(item.get("status", "")).strip().lower() == "canonical"]
    if not canonical_records:
        return False, "prompt preparation index has no canonical records", {"index": str(index_file), "count": len(data)}

    chapter_ok, chapter_details = _matches_requested_chapters(canonical_records, chapters)
    if not chapter_ok:
        return False, "prompt preparation index exists but requested chapter coverage is missing", {"index": str(index_file), **chapter_details}

    missing_files: list[str] = []
    empty_files: list[str] = []
    parse_failures: list[str] = []
    subject_kind_variants: dict[str, set[str]] = {}
    for record in canonical_records:
        subject_kind = str(record.get("subject_kind", "")).strip().lower()
        variant_name = str(record.get("variant_name", "")).strip().lower()
        if subject_kind:
            subject_kind_variants.setdefault(subject_kind, set()).add(variant_name)
        path_value = str(record.get("path", "")).strip()
        if not path_value:
            missing_files.append(f"{record.get('prompt_id', '(unknown)')} (missing path)")
            continue
        prompt_path = Path(path_value)
        if not prompt_path.exists():
            missing_files.append(path_value)
            continue
        try:
            if not prompt_path.read_text(encoding="utf-8").strip():
                empty_files.append(path_value)
                continue
            package = parse_prompt_package(prompt_path)
            if not package.positive_prompt.strip():
                empty_files.append(path_value)
        except Exception:
            parse_failures.append(path_value)

    if missing_files or empty_files or parse_failures:
        return False, "prompt preparation prompt files are missing, empty, or invalid", {
            "index": str(index_file),
            "missing_files": missing_files[:10],
            "empty_files": empty_files[:10],
            "parse_failures": parse_failures[:10],
        }

    if not subject_kind_variants:
        return False, "prompt preparation index has no recognized subject kinds", {"index": str(index_file)}

    variant_issues: list[str] = []
    if "character" in subject_kind_variants and not ({"bust_portrait", "full_body_neutral"} & subject_kind_variants["character"]):
        variant_issues.append("character missing bust_portrait/full_body_neutral")
    if "environment" in subject_kind_variants and "establishing_wide" not in subject_kind_variants["environment"]:
        variant_issues.append("environment missing establishing_wide")
    if "shot" in subject_kind_variants and "primary_keyframe" not in subject_kind_variants["shot"]:
        variant_issues.append("shot missing primary_keyframe")
    if variant_issues:
        return False, "prompt preparation index is missing expected variants", {
            "index": str(index_file),
            "subject_kind_variants": {key: sorted(value) for key, value in subject_kind_variants.items()},
            "issues": variant_issues,
        }

    return True, f"prompt prep index and {len(canonical_records)} canonical prompt records validated", {
        "index": str(index_file),
        "canonical_records": len(canonical_records),
        "subject_kind_variants": {key: sorted(value) for key, value in subject_kind_variants.items()},
        **chapter_details,
    }


def check_quality_grading(project_root: Path, chapters: str = "") -> tuple[bool, str, dict[str, Any]]:
    candidates = [
        project_root / "02_story_analysis" / "grading" / "QUALITY_GRADE_INDEX.json",
        project_root / "02_story_analysis" / "quality" / "QUALITY_GRADE_INDEX.json",
        project_root / "02_story_analysis" / "grading" / "QUALITY_GRADING_INDEX.json",
        project_root / "02_story_analysis" / "quality" / "QUALITY_GRADING_INDEX.json",
    ]

    rerun_candidates = [
        project_root / "02_story_analysis" / "grading" / "review" / "QUALITY_RERUN_QUEUE.json",
        project_root / "02_story_analysis" / "quality" / "review" / "QUALITY_RERUN_QUEUE.json",
    ]

    for path in candidates:
        if not path.exists():
            continue
        data = _read_json(path)
        if isinstance(data, list) and len(data) == 0:
            continue
        if isinstance(data, dict):
            count = _count_records(data)
            total_records = data.get("total_records", 0)
            family_summaries = data.get("family_summaries", [])
            rerun_queue = data.get("rerun_queue", None)
            if not isinstance(family_summaries, list) or not family_summaries:
                return False, "quality grading index missing family summaries", {"path": str(path), "total_records": total_records}
            invalid_family_summary = next(
                (
                    summary for summary in family_summaries
                    if not isinstance(summary, dict)
                    or not _is_nonempty_string(summary.get("family"))
                    or int(summary.get("count", 0) or 0) < 0
                    or not isinstance(summary.get("grade_counts", {}), dict)
                ),
                None,
            )
            if invalid_family_summary is not None:
                return False, "quality grading family summaries are malformed", {"path": str(path)}
            queue_path = next((candidate for candidate in rerun_candidates if candidate.exists()), None)
            queue_payload = rerun_queue
            if queue_path is not None:
                queue_payload = _read_json(queue_path)
            if not isinstance(queue_payload, list):
                return False, "quality grading rerun queue is missing or malformed", {"path": str(path), "rerun_queue_path": str(queue_path) if queue_path else ""}
            invalid_queue_item = next(
                (
                    item for item in queue_payload
                    if not isinstance(item, dict)
                    or not _is_nonempty_string(item.get("family"))
                    or not _is_nonempty_string(item.get("artifact_id"))
                    or not isinstance(item.get("reason", []), list)
                ),
                None,
            )
            if invalid_queue_item is not None:
                return False, "quality grading rerun queue items are malformed", {"path": str(path), "rerun_queue_path": str(queue_path) if queue_path else ""}
            if count > 0 or total_records > 0:
                return True, "quality grading index contains records, family summaries, and rerun queue", {
                    "path": str(path),
                    "count": count,
                    "total_records": total_records,
                    "family_summaries": len(family_summaries),
                    "rerun_queue": len(queue_payload),
                }

    # Fallback: any nonempty json in grading/quality
    for check_dir in [project_root / "02_story_analysis" / "grading", project_root / "02_story_analysis" / "quality"]:
        if check_dir.exists():
            for path in check_dir.glob("*.json"):
                data = _read_json(path)
                if isinstance(data, list) and len(data) > 0:
                    return True, "quality grading JSON contains records", {"path": str(path), "count": len(data)}
                if isinstance(data, dict):
                    count = _count_records(data)
                    total_records = data.get("total_records", 0)
                    if count > 0 or total_records > 0:
                        return True, "quality grading JSON contains records", {"path": str(path), "count": count, "total_records": total_records}

    return False, "missing quality grading index/report with records", {}


CHECKS: dict[str, Callable[[Path, str], tuple[bool, str, dict[str, Any]]]] = {
    "story_analysis": check_story_analysis,
    "character_taxonomy": check_character_taxonomy,
    "identity_refinement": check_identity_refinement,
    "character_bibles": check_character_bibles,
    "character_visual_evidence": check_character_visual_evidence,
    "environment_bibles": check_environment_bibles,
    "visual_fallbacks": check_visual_fallbacks,
    "scene_contracts": check_scene_contracts,
    "scene_bindings": check_scene_bindings,
    "shot_packages": check_shot_packages,
    "dialogue_timeline": check_dialogue_timeline,
    "descriptor_enrichment": check_descriptor_enrichment,
    "prompt_preparation": check_prompt_preparation,
    "quality_grading": check_quality_grading,
}


def validation_report(project_slug: str, chapters: str = "") -> list[dict[str, Any]]:
    project_root = _project_root(project_slug)
    if not project_root.exists():
        return [{
            "stage": "story_analysis",
            "complete": False,
            "reason": f"project root not found: {project_root}",
            "details": {},
        }]

    report: list[dict[str, Any]] = []
    for stage in STAGES:
        ok, reason, details = CHECKS[stage](project_root, chapters)
        report.append({
            "stage": stage,
            "complete": ok,
            "reason": reason,
            "details": details,
        })
    return report


def find_first_incomplete_stage(project_slug: str, chapters: str = "") -> str | None:
    for row in validation_report(project_slug, chapters):
        if not row["complete"]:
            return str(row["stage"])
    return None


def _print_report(project_slug: str, chapters: str = "") -> None:
    rows = validation_report(project_slug, chapters)
    first = None
    for row in rows:
        status = "PASS" if row["complete"] else "FAIL"
        print(f"CHECK {row['stage']}: {status} - {row['reason']}")
        details = row.get("details") or {}
        if details:
            print(f"  DETAILS: {json.dumps(details, ensure_ascii=False, sort_keys=True)}")
        if first is None and not row["complete"]:
            first = row["stage"]
    print(f"Resume will start at: {first or 'complete'}")


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("story_analysis")
        return 0

    project_slug = argv[1]
    chapters = ""
    report = False
    for arg in argv[2:]:
        if arg == "--report":
            report = True
        elif not chapters:
            chapters = arg

    if report:
        _print_report(project_slug, chapters)
        return 0

    print(find_first_incomplete_stage(project_slug, chapters) or "complete")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
