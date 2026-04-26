"""Entity taxonomy helpers for chapter-level extraction."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class EntityTaxonomyHints:
    """Structured entity type hints from chapter extraction."""
    
    character_type_hint: str = "unknown"
    morphology_hint: str = "unknown"
    scale_hint: str = "unknown"
    renderability_hint: str = "unknown"
    confidence: float = 0.0
    direct_identity_evidence: str = ""
    direct_visual_evidence: str = ""
    costume_or_covering_evidence: str = ""
    movement_evidence: str = ""
    associated_entities: list[str] | None = None
    alias_or_role_evidence: str = ""
    unknowns: str = ""
    source_refs: list[str] | None = None

    def to_dict(self) -> dict[str, object]:
        return {
            "character_type_hint": self.character_type_hint,
            "morphology_hint": self.morphology_hint,
            "scale_hint": self.scale_hint,
            "renderability_hint": self.renderability_hint,
            "confidence": self.confidence,
            "direct_identity_evidence": self.direct_identity_evidence,
            "direct_visual_evidence": self.direct_visual_evidence,
            "costume_or_covering_evidence": self.costume_or_covering_evidence,
            "movement_evidence": self.movement_evidence,
            "associated_entities": self.associated_entities or [],
            "alias_or_role_evidence": self.alias_or_role_evidence,
            "unknowns": self.unknowns,
            "source_refs": self.source_refs or [],
        }


VALID_CHARACTER_TYPE_HINTS = {
    "human",
    "humanoid_nonhuman",
    "animal",
    "creature",
    "group",
    "object",
    "machine",
    "abstract",
    "unknown",
}

VALID_MORPHOLOGY_HINTS = {
    "biped",
    "quadruped",
    "multi_legged",
    "serpentine",
    "winged",
    "constructed",
    "amorphous",
    "unknown",
}

VALID_SCALE_HINTS = {
    "tiny",
    "small",
    "human_scale",
    "large",
    "giant",
    "unknown",
}

VALID_RENDERABILITY_HINTS = {
    "renderable",
    "context_only",
    "alias_or_role",
    "unknown",
}


def parse_entity_taxonomy_hints(record_fields: dict[str, str]) -> EntityTaxonomyHints:
    """Parse entity taxonomy hints from a character record, with safe defaults."""
    character_type_hint = _normalize_hint(
        record_fields.get("character_type_hint", "").strip(),
        VALID_CHARACTER_TYPE_HINTS,
        default="unknown",
    )
    morphology_hint = _normalize_hint(
        record_fields.get("morphology_hint", "").strip(),
        VALID_MORPHOLOGY_HINTS,
        default="unknown",
    )
    scale_hint = _normalize_hint(
        record_fields.get("scale_hint", "").strip(),
        VALID_SCALE_HINTS,
        default="unknown",
    )
    renderability_hint = _normalize_hint(
        record_fields.get("renderability_hint", "").strip(),
        VALID_RENDERABILITY_HINTS,
        default="unknown",
    )
    
    confidence_str = record_fields.get("confidence", "0.0").strip()
    try:
        confidence = max(0.0, min(1.0, float(confidence_str)))
    except (ValueError, TypeError):
        confidence = 0.0
    
    direct_identity_evidence = record_fields.get("direct_identity_evidence", "").strip()
    direct_visual_evidence = record_fields.get("direct_visual_evidence", "").strip()
    costume_or_covering_evidence = record_fields.get("costume_or_covering_evidence", "").strip()
    movement_evidence = record_fields.get("movement_evidence", "").strip()
    
    associated_entities_str = record_fields.get("associated_entities", "").strip()
    associated_entities = [
        item.strip()
        for item in associated_entities_str.split(",")
        if item.strip()
    ] if associated_entities_str else []
    
    alias_or_role_evidence = record_fields.get("alias_or_role_evidence", "").strip()
    unknowns = record_fields.get("unknowns", "").strip()
    
    source_refs_str = record_fields.get("source_refs", "").strip()
    source_refs = [
        item.strip()
        for item in source_refs_str.split(",")
        if item.strip()
    ] if source_refs_str else []
    
    return EntityTaxonomyHints(
        character_type_hint=character_type_hint,
        morphology_hint=morphology_hint,
        scale_hint=scale_hint,
        renderability_hint=renderability_hint,
        confidence=confidence,
        direct_identity_evidence=direct_identity_evidence,
        direct_visual_evidence=direct_visual_evidence,
        costume_or_covering_evidence=costume_or_covering_evidence,
        movement_evidence=movement_evidence,
        associated_entities=associated_entities,
        alias_or_role_evidence=alias_or_role_evidence,
        unknowns=unknowns,
        source_refs=source_refs,
    )


def _normalize_hint(value: str, valid_set: set[str], default: str) -> str:
    """Normalize a hint value to a valid option or default."""
    normalized = value.lower().replace("-", "_").replace(" ", "_")
    return normalized if normalized in valid_set else default


def format_entity_taxonomy_markdown(hints: EntityTaxonomyHints) -> str:
    """Format entity taxonomy hints as a concise markdown section."""
    lines = [
        "# Entity Type Hints",
        "",
        f"- character_type: {hints.character_type_hint}",
        f"- morphology: {hints.morphology_hint}",
        f"- scale: {hints.scale_hint}",
        f"- renderability: {hints.renderability_hint}",
        f"- confidence: {hints.confidence:.2f}",
    ]
    
    if hints.direct_identity_evidence:
        lines.extend(["", "## Direct Identity Evidence", hints.direct_identity_evidence])
    
    if hints.direct_visual_evidence:
        lines.extend(["", "## Direct Visual Evidence", hints.direct_visual_evidence])
    
    if hints.costume_or_covering_evidence:
        lines.extend(["", "## Costume/Equipment", hints.costume_or_covering_evidence])
    
    if hints.movement_evidence:
        lines.extend(["", "## Movement", hints.movement_evidence])
    
    if hints.associated_entities:
        lines.extend(["", "## Associated Entities", ", ".join(hints.associated_entities)])
    
    if hints.alias_or_role_evidence:
        lines.extend(["", "## Alias/Role Evidence", hints.alias_or_role_evidence])
    
    if hints.unknowns:
        lines.extend(["", "## Unknowns", hints.unknowns])
    
    if hints.source_refs:
        lines.extend(["", "## Source References", ", ".join(hints.source_refs)])
    
    return "\n".join(lines)
