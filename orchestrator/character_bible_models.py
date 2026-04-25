from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class CharacterBibleMetadata:
    artifact_id: str
    artifact_type: str = "character_bible"
    status: str = "generated"
    source_fingerprint: str | None = None
    created_at_utc: str = ""
    updated_at_utc: str = ""
    upstream_dependencies: list[dict[str, Any]] = field(default_factory=list)
    locked_fields: dict[str, bool] = field(default_factory=dict)
    manual_overrides: dict[str, Any] = field(default_factory=dict)
    revision_history: list[dict[str, Any]] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "artifact_id": self.artifact_id,
            "artifact_type": self.artifact_type,
            "status": self.status,
            "source_fingerprint": self.source_fingerprint,
            "created_at_utc": self.created_at_utc,
            "updated_at_utc": self.updated_at_utc,
            "upstream_dependencies": self.upstream_dependencies,
            "locked_fields": self.locked_fields,
            "manual_overrides": self.manual_overrides,
            "revision_history": self.revision_history,
        }


@dataclass
class CharacterBible:
    character_id: str
    display_name: str
    aliases: list[str] = field(default_factory=list)
    status: str = "canonical"
    entity_kind: str = "individual"
    first_seen_chapter: str | None = None
    last_seen_chapter: str | None = None
    chapter_mentions: list[str] = field(default_factory=list)

    identity_baseline: str = ""
    age_presence: str = ""
    physical_build: str = ""
    origin_or_historical_context: str = ""
    movement_language: str = ""
    stable_visual_summary: str = ""
    physical_traits: list[str] = field(default_factory=list)
    costume_signature: str = ""
    distinguishing_features: list[str] = field(default_factory=list)
    state_variants: list[str] = field(default_factory=list)

    personality: str = ""
    role: str = ""
    voice_notes: str = ""
    relationship_notes: list[str] = field(default_factory=list)

    continuity_constraints: list[str] = field(default_factory=list)
    unresolved_ambiguities: list[str] = field(default_factory=list)

    evidence_refs: list[dict[str, Any]] = field(default_factory=list)
    evidence_summary: list[str] = field(default_factory=list)
    visual_production_fallback: dict[str, Any] = field(default_factory=dict)
    metadata: CharacterBibleMetadata | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "character_id": self.character_id,
            "display_name": self.display_name,
            "aliases": self.aliases,
            "status": self.status,
            "entity_kind": self.entity_kind,
            "first_seen_chapter": self.first_seen_chapter,
            "last_seen_chapter": self.last_seen_chapter,
            "chapter_mentions": self.chapter_mentions,
            "identity_baseline": self.identity_baseline,
            "age_presence": self.age_presence,
            "physical_build": self.physical_build,
            "origin_or_historical_context": self.origin_or_historical_context,
            "movement_language": self.movement_language,
            "stable_visual_summary": self.stable_visual_summary,
            "physical_traits": self.physical_traits,
            "costume_signature": self.costume_signature,
            "distinguishing_features": self.distinguishing_features,
            "state_variants": self.state_variants,
            "personality": self.personality,
            "role": self.role,
            "voice_notes": self.voice_notes,
            "relationship_notes": self.relationship_notes,
            "continuity_constraints": self.continuity_constraints,
            "unresolved_ambiguities": self.unresolved_ambiguities,
            "evidence_refs": self.evidence_refs,
            "evidence_summary": self.evidence_summary,
            "visual_production_fallback": self.visual_production_fallback,
            "metadata": self.metadata.to_dict() if self.metadata else None,
        }


@dataclass(frozen=True)
class CharacterBibleSynthesisSummary:
    project_slug: str
    total_registry_entries: int
    synthesized_count: int
    reused_count: int
    stale_locked_count: int
    review_queue_count: int
    written_files: list[str]
    warnings: list[str]

    def to_dict(self) -> dict[str, Any]:
        return {
            "project_slug": self.project_slug,
            "total_registry_entries": self.total_registry_entries,
            "synthesized_count": self.synthesized_count,
            "reused_count": self.reused_count,
            "stale_locked_count": self.stale_locked_count,
            "review_queue_count": self.review_queue_count,
            "written_files": self.written_files,
            "warnings": self.warnings,
        }
