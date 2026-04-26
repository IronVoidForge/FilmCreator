from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .common import ensure_dir, read_json, repo_relative, write_json
from .core.paths import (
    character_taxonomy_dir,
    character_taxonomy_index_path,
    character_taxonomy_path,
    character_taxonomy_review_dir,
)
from .scaffold import create_project
from .world_registry import character_registry_path


def _load_character_registry(project_slug: str) -> dict[str, Any]:
    path = character_registry_path(project_slug)
    if not path.exists():
        return {}
    return read_json(path)


def _load_character_bible(project_dir: Path, character_id: str) -> dict[str, Any] | None:
    bible_path = project_dir / "02_story_analysis" / "bibles" / "characters" / f"CHAR_{character_id}.md"
    if not bible_path.exists():
        return None
    content = bible_path.read_text(encoding="utf-8")
    return {"content": content, "path": str(bible_path)}


def _extract_entity_type_hints(character_id: str, registry_entry: dict, bible_data: dict | None) -> tuple[list[str], list[str]]:
    """Extract direct and associated entity type hints from available sources."""
    direct_hints = []
    associated_hints = []
    
    # From registry entity_kind
    entity_kind = registry_entry.get("entity_kind", "unknown")
    if entity_kind == "group":
        direct_hints.append("group")
    
    # From character bible content
    if bible_data:
        content = bible_data.get("content", "").lower()
        
        # Direct type hints
        if "human" in content and ("earth" in content or "virginia" in content or "confederate" in content):
            direct_hints.append("human")
        if "martian hound" in content or "calot" in content:
            direct_hints.append("animal")
        if "ape" in content and "creature" in content:
            direct_hints.append("creature")
        if "green martian" in content or "red martian" in content:
            direct_hints.append("humanoid_nonhuman")
        if "mummified" in content or "corpse" in content or "deceased" in content:
            direct_hints.append("context_only")
        
        # Associated hints (mounts, clothing, objects)
        if "mount" in content or "riding" in content:
            associated_hints.append("has_mount")
        if "costume" in content or "clothing" in content or "armor" in content:
            associated_hints.append("has_costume")
        if "weapon" in content or "sword" in content:
            associated_hints.append("has_weapon")
    
    return direct_hints, associated_hints


def _extract_morphology_hints(character_id: str, bible_data: dict | None) -> list[str]:
    """Extract morphology hints from available sources."""
    hints = []
    
    if bible_data:
        content = bible_data.get("content", "").lower()
        
        if "biped" in content or "two legs" in content or "humanoid" in content:
            hints.append("biped")
        if "quadruped" in content or "four legs" in content or "canine" in content:
            hints.append("quadruped")
        if "multi-legged" in content or "eight legs" in content:
            hints.append("multi_legged")
        if "wings" in content or "winged" in content or "flying" in content:
            hints.append("winged")
        if "serpentine" in content or "snake" in content:
            hints.append("serpentine")
    
    return hints


def _extract_scale_hints(character_id: str, bible_data: dict | None) -> list[str]:
    """Extract scale hints from available sources."""
    hints = []
    
    if bible_data:
        content = bible_data.get("content", "").lower()
        
        if "tiny" in content or "small creature" in content:
            hints.append("tiny")
        if "small" in content and "scale" in content:
            hints.append("small")
        if "large" in content or "massive" in content or "colossal" in content:
            hints.append("large")
        if "giant" in content or "enormous" in content:
            hints.append("giant")
        if "human-scale" in content or "human scale" in content:
            hints.append("human_scale")
    
    return hints


def _determine_primary_type(direct_hints: list[str], associated_hints: list[str], entity_kind: str) -> tuple[str, float, list[str]]:
    """Determine primary type from hints. Direct evidence only."""
    conflicts = []
    
    if entity_kind == "group":
        return "group", 1.0, []
    
    if not direct_hints:
        return "unknown", 0.0, []
    
    # Check for conflicts
    type_categories = set()
    for hint in direct_hints:
        if hint in ["human", "humanoid_nonhuman"]:
            type_categories.add("humanoid")
        elif hint in ["animal", "creature"]:
            type_categories.add("creature")
        elif hint == "group":
            type_categories.add("group")
        elif hint == "context_only":
            type_categories.add("context")
    
    if len(type_categories) > 1:
        conflicts.append(f"Conflicting type hints: {direct_hints}")
        return "unknown", 0.0, conflicts
    
    # Determine primary type from most common hint
    hint_counts = {}
    for hint in direct_hints:
        hint_counts[hint] = hint_counts.get(hint, 0) + 1
    
    primary = max(hint_counts, key=hint_counts.get)
    confidence = hint_counts[primary] / len(direct_hints)
    
    return primary, confidence, conflicts


def _determine_morphology(hints: list[str]) -> tuple[str, float, list[str]]:
    """Determine morphology from hints."""
    conflicts = []
    
    if not hints:
        return "unknown", 0.0, []
    
    # Check for conflicts
    if len(set(hints)) > 1:
        conflicts.append(f"Conflicting morphology hints: {hints}")
        return "unknown", 0.0, conflicts
    
    hint_counts = {}
    for hint in hints:
        hint_counts[hint] = hint_counts.get(hint, 0) + 1
    
    primary = max(hint_counts, key=hint_counts.get)
    confidence = hint_counts[primary] / len(hints)
    
    return primary, confidence, conflicts


def _determine_scale(hints: list[str]) -> tuple[str, float, list[str]]:
    """Determine scale from hints."""
    conflicts = []
    
    if not hints:
        return "unknown", 0.0, []
    
    # Check for conflicts
    if len(set(hints)) > 1:
        conflicts.append(f"Conflicting scale hints: {hints}")
        return "unknown", 0.0, conflicts
    
    hint_counts = {}
    for hint in hints:
        hint_counts[hint] = hint_counts.get(hint, 0) + 1
    
    primary = max(hint_counts, key=hint_counts.get)
    confidence = hint_counts[primary] / len(hints)
    
    return primary, confidence, conflicts


def _determine_sentience(primary_type: str) -> str:
    """Determine sentience from primary type."""
    if primary_type in ["human", "humanoid_nonhuman"]:
        return "person"
    if primary_type == "animal":
        return "animal"
    if primary_type == "creature":
        return "monster"
    if primary_type == "object":
        return "object"
    if primary_type == "abstract":
        return "abstract"
    return "unknown"


def _determine_renderability(primary_type: str, entity_kind: str, character_id: str) -> str:
    """Determine renderability from primary type and entity kind."""
    if primary_type == "context_only":
        return "context_only"
    if entity_kind == "provisional_role":
        return "alias_redirect_candidate"
    if primary_type == "unknown":
        return "unknown"
    return "renderable"


def _determine_alias_status(character_id: str, entity_kind: str, registry_entry: dict) -> dict[str, Any]:
    """Determine alias resolution status."""
    if entity_kind == "provisional_role":
        return {
            "status": "role_label",
            "canonical_target_id": None,
            "confidence": 0.0,
            "evidence": ["Entity kind is provisional_role"],
            "requires_human_review": True
        }
    
    if registry_entry.get("status") == "provisional":
        return {
            "status": "unresolved",
            "canonical_target_id": None,
            "confidence": 0.0,
            "evidence": ["Registry status is provisional"],
            "requires_human_review": True
        }
    
    return {
        "status": "canonical",
        "canonical_target_id": None,
        "confidence": 1.0,
        "evidence": ["Registry status is canonical"],
        "requires_human_review": False
    }


def _synthesize_character_taxonomy(
    character_id: str,
    registry_entry: dict,
    project_dir: Path
) -> dict[str, Any]:
    """Synthesize taxonomy for a single character."""
    
    # Load character bible if available
    bible_data = _load_character_bible(project_dir, character_id)
    
    # Extract hints
    direct_hints, associated_hints = _extract_entity_type_hints(character_id, registry_entry, bible_data)
    morphology_hints = _extract_morphology_hints(character_id, bible_data)
    scale_hints = _extract_scale_hints(character_id, bible_data)
    
    # Determine taxonomy
    entity_kind = registry_entry.get("entity_kind", "unknown")
    primary_type, type_confidence, type_conflicts = _determine_primary_type(direct_hints, associated_hints, entity_kind)
    morphology, morph_confidence, morph_conflicts = _determine_morphology(morphology_hints)
    scale, scale_confidence, scale_conflicts = _determine_scale(scale_hints)
    sentience = _determine_sentience(primary_type)
    renderability = _determine_renderability(primary_type, entity_kind, character_id)
    alias_resolution = _determine_alias_status(character_id, entity_kind, registry_entry)
    
    # Aggregate conflicts
    all_conflicts = type_conflicts + morph_conflicts + scale_conflicts
    
    # Determine if review is needed
    needs_review = (
        len(all_conflicts) > 0 or
        primary_type == "unknown" or
        alias_resolution["requires_human_review"]
    )
    
    review_reasons = []
    if len(all_conflicts) > 0:
        review_reasons.append("Conflicting taxonomy hints detected")
    if primary_type == "unknown" and direct_hints:
        review_reasons.append("Unable to resolve primary type from hints")
    if alias_resolution["requires_human_review"]:
        review_reasons.append("Alias resolution requires human review")
    
    # Calculate overall confidence
    confidences = [c for c in [type_confidence, morph_confidence, scale_confidence] if c > 0]
    overall_confidence = sum(confidences) / len(confidences) if confidences else 0.0
    
    # Build taxonomy
    taxonomy = {
        "character_id": character_id,
        "display_name": registry_entry.get("display_name", character_id),
        "entity_kind": entity_kind,
        "primary_type": primary_type,
        "morphology": morphology,
        "scale": scale,
        "sentience": sentience,
        "renderability": renderability,
        "confidence": round(overall_confidence, 2),
        "direct_evidence": direct_hints,
        "associated_evidence": associated_hints,
        "conflicts": all_conflicts,
        "unknowns": [],
        "needs_review": needs_review,
        "review_reasons": review_reasons,
        "alias_resolution": alias_resolution,
        "source_files": registry_entry.get("sources", []),
        "generated_at_utc": datetime.now(timezone.utc).isoformat()
    }
    
    # Add unknowns
    if primary_type == "unknown":
        taxonomy["unknowns"].append("primary_type")
    if morphology == "unknown":
        taxonomy["unknowns"].append("morphology")
    if scale == "unknown":
        taxonomy["unknowns"].append("scale")
    
    return taxonomy


def run_character_taxonomy(
    project_slug: str,
    *,
    force: bool = False,
    limit: int | None = None
) -> dict[str, Any]:
    """Run character taxonomy synthesis."""
    
    project_dir = create_project(project_slug)
    taxonomy_dir = character_taxonomy_dir(project_dir)
    ensure_dir(taxonomy_dir)
    
    review_dir = character_taxonomy_review_dir(project_dir)
    ensure_dir(review_dir)
    
    # Load character registry
    registry = _load_character_registry(project_slug)
    
    if not registry:
        return {
            "status": "error",
            "message": "No character registry found",
            "total_registry_entries": 0,
            "synthesized_count": 0,
            "reused_count": 0,
            "needs_review_count": 0,
            "unknown_count": 0,
            "written_files": [],
            "warnings": ["Character registry is empty or missing"]
        }
    
    # Process characters
    synthesized_count = 0
    reused_count = 0
    needs_review_count = 0
    unknown_count = 0
    written_files = []
    warnings = []
    review_queue = []
    
    character_ids = list(registry.keys())
    if limit:
        character_ids = character_ids[:limit]
    
    index = {}
    
    for character_id in character_ids:
        registry_entry = registry[character_id]
        taxonomy_path = character_taxonomy_path(project_dir, character_id)
        
        # Check if already exists
        if taxonomy_path.exists() and not force:
            taxonomy = read_json(taxonomy_path)
            reused_count += 1
        else:
            taxonomy = _synthesize_character_taxonomy(character_id, registry_entry, project_dir)
            write_json(taxonomy_path, taxonomy)
            written_files.append(repo_relative(taxonomy_path))
            synthesized_count += 1
        
        # Update counters
        if taxonomy.get("needs_review"):
            needs_review_count += 1
            review_queue.append({
                "character_id": character_id,
                "display_name": taxonomy.get("display_name"),
                "review_reasons": taxonomy.get("review_reasons", []),
                "taxonomy_path": repo_relative(taxonomy_path)
            })
        
        if taxonomy.get("primary_type") == "unknown":
            unknown_count += 1
        
        # Add to index
        index[character_id] = {
            "display_name": taxonomy.get("display_name"),
            "primary_type": taxonomy.get("primary_type"),
            "entity_kind": taxonomy.get("entity_kind"),
            "needs_review": taxonomy.get("needs_review"),
            "confidence": taxonomy.get("confidence"),
            "taxonomy_path": repo_relative(taxonomy_path)
        }
    
    # Write index
    index_path = character_taxonomy_index_path(project_dir)
    write_json(index_path, index)
    written_files.append(repo_relative(index_path))
    
    # Write review queue
    if review_queue:
        review_json_path = review_dir / "CHARACTER_TAXONOMY_REVIEW_QUEUE.json"
        write_json(review_json_path, {"review_queue": review_queue, "count": len(review_queue)})
        written_files.append(repo_relative(review_json_path))
        
        # Write markdown review queue
        review_md_path = review_dir / "CHARACTER_TAXONOMY_REVIEW_QUEUE.md"
        md_lines = ["# Character Taxonomy Review Queue\n"]
        for item in review_queue:
            md_lines.append(f"## {item['display_name']} ({item['character_id']})\n")
            md_lines.append(f"- Taxonomy Path: `{item['taxonomy_path']}`\n")
            md_lines.append("- Review Reasons:\n")
            for reason in item['review_reasons']:
                md_lines.append(f"  - {reason}\n")
            md_lines.append("\n")
        review_md_path.write_text("".join(md_lines), encoding="utf-8")
        written_files.append(repo_relative(review_md_path))
    
    return {
        "status": "success",
        "total_registry_entries": len(registry),
        "synthesized_count": synthesized_count,
        "reused_count": reused_count,
        "needs_review_count": needs_review_count,
        "unknown_count": unknown_count,
        "written_files": written_files,
        "warnings": warnings
    }
