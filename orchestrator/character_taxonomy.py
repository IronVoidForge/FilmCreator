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


def _iter_character_taxonomy_hint_records(
    project_dir: Path,
    character_id: str,
    registry_entry: dict[str, Any],
) -> list[dict[str, Any]]:
    """Return structured taxonomy hint records from chapter extraction outputs.
    Do not infer taxonomy from arbitrary prose.
    Do not read character bible files.
    """
    records = []
    
    # Search character breakdown chapters for structured hints
    breakdown_root = project_dir / "02_story_analysis" / "character_breakdowns" / "chapters"
    if not breakdown_root.exists():
        return records
    
    # Iterate through chapter directories
    for chapter_dir in sorted(breakdown_root.iterdir()):
        if not chapter_dir.is_dir():
            continue
        
        # Look for character breakdown file
        char_file = chapter_dir / f"{character_id}.md"
        if not char_file.exists():
            continue
        
        try:
            content = char_file.read_text(encoding="utf-8")
            # Parse structured taxonomy hints if present
            # For now, we'll look for a structured section
            # In the future, this should use packet parser
            record = _parse_taxonomy_hints_from_markdown(content, str(char_file))
            if record:
                records.append(record)
        except Exception:
            continue
    
    return records


def _parse_taxonomy_hints_from_markdown(content: str, source_path: str) -> dict[str, Any] | None:
    """Parse taxonomy hints from markdown if present.
    Returns None if no structured hints found.
    """
    import re
    
    # Field aliases
    field_map = {
        "character_type_hint": "character_type_hint",
        "character_type": "character_type_hint",
        "primary_type_hint": "character_type_hint",
        "type_hint": "character_type_hint",
        "morphology_hint": "morphology_hint",
        "morphology": "morphology_hint",
        "scale_hint": "scale_hint",
        "scale": "scale_hint",
        "renderability_hint": "renderability_hint",
        "renderability": "renderability_hint",
        "confidence": "confidence",
        "taxonomy_confidence": "confidence",
        "direct_identity_evidence": "direct_identity_evidence",
        "identity_evidence": "direct_identity_evidence",
        "direct_visual_evidence": "direct_visual_evidence",
        "visual_evidence": "direct_visual_evidence",
        "costume_or_covering_evidence": "costume_or_covering_evidence",
        "costume_evidence": "costume_or_covering_evidence",
        "equipment_evidence": "costume_or_covering_evidence",
        "movement_evidence": "movement_evidence",
        "associated_entities": "associated_entities",
        "associated_entity_evidence": "associated_entities",
        "alias_or_role_evidence": "alias_or_role_evidence",
        "alias_evidence": "alias_or_role_evidence",
        "role_evidence": "alias_or_role_evidence",
        "unknowns": "unknowns",
        "source_refs": "source_refs",
        "source_references": "source_refs",
    }
    
    # Valid enum values
    valid_character_types = {"human", "humanoid_nonhuman", "animal", "creature", "group", "object", "machine", "abstract", "unknown"}
    valid_morphologies = {"biped", "quadruped", "multi_legged", "serpentine", "winged", "constructed", "amorphous", "unknown"}
    valid_scales = {"tiny", "small", "human_scale", "large", "giant", "unknown"}
    valid_renderabilities = {"renderable", "context_only", "alias_or_role", "unknown"}
    
    def normalize_value(value: str) -> str:
        return value.strip().lower().replace(" ", "_").replace("-", "_")
    
    def validate_enum(value: str, valid_set: set[str]) -> str:
        normalized = normalize_value(value)
        return normalized if normalized in valid_set else "unknown"
    
    # Parse fields
    parsed = {}
    found_any = False
    
    # Match both colon and bullet formats
    pattern = r'^\s*-?\s*([\w_]+)\s*:\s*(.+)$'
    
    for line in content.splitlines():
        match = re.match(pattern, line)
        if not match:
            continue
        
        field_name = match.group(1).strip().lower().replace(" ", "_").replace("-", "_")
        field_value = match.group(2).strip()
        
        if field_name not in field_map:
            continue
        
        canonical_name = field_map[field_name]
        found_any = True
        
        if canonical_name == "character_type_hint":
            parsed[canonical_name] = validate_enum(field_value, valid_character_types)
        elif canonical_name == "morphology_hint":
            parsed[canonical_name] = validate_enum(field_value, valid_morphologies)
        elif canonical_name == "scale_hint":
            parsed[canonical_name] = validate_enum(field_value, valid_scales)
        elif canonical_name == "renderability_hint":
            parsed[canonical_name] = validate_enum(field_value, valid_renderabilities)
        elif canonical_name == "confidence":
            try:
                conf = float(field_value)
                parsed[canonical_name] = max(0.0, min(1.0, conf))
            except (ValueError, TypeError):
                parsed[canonical_name] = 0.0
        elif canonical_name == "associated_entities":
            # Split by semicolon
            entities = [e.strip() for e in field_value.split(";") if e.strip()]
            parsed[canonical_name] = entities
        elif canonical_name == "source_refs":
            # Split by semicolon or comma
            refs = [r.strip() for r in re.split(r'[;,]', field_value) if r.strip()]
            parsed[canonical_name] = refs
        else:
            parsed[canonical_name] = field_value
    
    if not found_any:
        return None
    
    parsed["source_path"] = source_path
    return parsed


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
    
    # Load structured taxonomy hint records from upstream extraction
    hint_records = _iter_character_taxonomy_hint_records(project_dir, character_id, registry_entry)
    
    # Aggregate hints from structured records
    direct_hints = []
    associated_hints = []
    morphology_hints = []
    scale_hints = []
    
    # From registry entity_kind
    entity_kind = registry_entry.get("entity_kind", "unknown")
    if entity_kind == "group":
        direct_hints.append("group")
    
    # Aggregate from structured hint records
    for record in hint_records:
        char_type = record.get("character_type_hint", "unknown")
        if char_type and char_type != "unknown":
            direct_hints.append(char_type)
        
        morph = record.get("morphology_hint", "unknown")
        if morph and morph != "unknown":
            morphology_hints.append(morph)
        
        scale = record.get("scale_hint", "unknown")
        if scale and scale != "unknown":
            scale_hints.append(scale)
        
        # Associated entities are recorded separately
        assoc = record.get("associated_entities", [])
        if assoc:
            associated_hints.extend(assoc)
    
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
