from __future__ import annotations

import json
import re
import time
import unicodedata
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from types import SimpleNamespace

from .authoring import PromptWriteSummary, write_prompts
from .core.paths import ensure_dir, repo_relative
from .core.validation import validate_clip_id, validate_scene_id
from .lmstudio_client import LMStudioClient, LMStudioError
from .delete_safety import find_project_root, remove_path_within_project
from .prompt_package import PromptPackage, write_prompt_package
from .scaffold import create_clip, create_project, create_scene
from .settings import load_runtime_settings
from .features.authoring import shared_prompts as authoring_prompts
from .features.authoring import packet_parser as authoring_packets
from .book_librarian import chapter_text, get_paragraph_window, search_chapter_context
from .character_match import find_character_match_candidates
from .environment_match import EnvironmentMatchCandidate, find_environment_match_candidates
from .features.world.global_helpers import is_generic_character_label
from .world_registry import (
    character_registry_path,
    environment_registry_path,
    resolve_character_registry,
    resolve_environment_registry,
    summarize_registry_status,
)


HEADING_PATTERN = re.compile(r"(?m)^# ([^\r\n]+)\s*$")
CHAPTER_ID_PATTERN = re.compile(r"\b(CH\d{3})\b", re.IGNORECASE)
SCENE_ID_PATTERN = re.compile(r"^SC\d{3}$")
CLIP_ID_PATTERN = re.compile(r"^CL\d{3}$")
ASSET_ID_PATTERN = re.compile(r"^[a-z0-9_]+$")
SECTION_TAG_PATTERN = re.compile(r"^\[\[SECTION ([a-z0-9_]+)\]\]$", re.IGNORECASE)
PACKET_START_TAG = "[[FILMCREATOR_PACKET]]"
PACKET_END_TAG = "[[/FILMCREATOR_PACKET]]"
RECORD_START_TAG = "[[FILMCREATOR_RECORD]]"
RECORD_END_TAG = "[[/FILMCREATOR_RECORD]]"
SECTION_END_TAG = "[[/SECTION]]"
PACKET_VERSION = "1"
MANUAL_PLACEHOLDER_MARKER = "<!-- FILMCREATOR_MANUAL_PLACEHOLDER -->"
CLARIFICATION_PLACEHOLDER_MARKER = "<!-- FILMCREATOR_CHARACTER_CLARIFICATION -->"
PREFERRED_SCENE_COUNT = 3
THIN_SCENE_MARKDOWN_THRESHOLD = 240


@dataclass(frozen=True)
class ManualCharacterDescriptionRequest:
    asset_id: str
    source_path: str
    reason: str

    def to_dict(self) -> dict[str, str]:
        return {
            "asset_id": self.asset_id,
            "source_path": self.source_path,
            "reason": self.reason,
        }


@dataclass(frozen=True)
class CharacterClarificationRequest:
    asset_id: str
    source_path: str
    reason: str
    question: str
    candidate_summaries: tuple[str, ...] = ()

    def to_dict(self) -> dict[str, str]:
        payload = {
            "asset_id": self.asset_id,
            "source_path": self.source_path,
            "reason": self.reason,
            "question": self.question,
        }
        if self.candidate_summaries:
            payload["candidate_summaries"] = list(self.candidate_summaries)
        return payload


@dataclass(frozen=True)
class CharacterClarificationDetails:
    reason: str
    question: str
    candidate_summaries: tuple[str, ...] = ()


@dataclass(frozen=True)
class EnvironmentClarificationRequest:
    asset_id: str
    source_path: str
    reason: str
    question: str
    candidate_summaries: tuple[str, ...] = ()

    def to_dict(self) -> dict[str, object]:
        payload: dict[str, object] = {
            "asset_id": self.asset_id,
            "source_path": self.source_path,
            "reason": self.reason,
            "question": self.question,
        }
        if self.candidate_summaries:
            payload["candidate_summaries"] = list(self.candidate_summaries)
        return payload


@dataclass(frozen=True)
class EnvironmentClarificationDetails:
    reason: str
    question: str
    candidate_summaries: tuple[str, ...] = ()


@dataclass(frozen=True)
class StoryAnalysisSummary:
    project_slug: str
    chapter_path: str
    chapter_id: str
    model: str
    written_files: list[str]
    scene_ids: list[str]
    manual_character_description_requests: list[ManualCharacterDescriptionRequest]
    character_clarification_requests: list[CharacterClarificationRequest]
    warnings: list[str]
    canonical_character_ids: list[str]
    provisional_character_ids: list[str]
    canonical_environment_ids: list[str]
    provisional_environment_ids: list[str]
    world_registry_paths: list[str]

    def to_dict(self) -> dict[str, object]:
        return {
            "project_slug": self.project_slug,
            "chapter_path": self.chapter_path,
            "chapter_id": self.chapter_id,
            "model": self.model,
            "written_files": self.written_files,
            "scene_ids": self.scene_ids,
            "manual_character_description_requests": [
                item.to_dict() for item in self.manual_character_description_requests
            ],
            "character_clarification_requests": [
                item.to_dict() for item in self.character_clarification_requests
            ],
            "warnings": self.warnings,
            "canonical_character_ids": self.canonical_character_ids,
            "provisional_character_ids": self.provisional_character_ids,
            "canonical_environment_ids": self.canonical_environment_ids,
            "provisional_environment_ids": self.provisional_environment_ids,
            "world_registry_paths": self.world_registry_paths,
        }


@dataclass(frozen=True)
class ScenePlanningSummary:
    project_slug: str
    scene_id: str
    model: str
    written_files: list[str]
    beat_ids: list[str]
    clip_ids: list[str]
    warnings: list[str]

    def to_dict(self) -> dict[str, object]:
        return {
            "project_slug": self.project_slug,
            "scene_id": self.scene_id,
            "model": self.model,
            "written_files": self.written_files,
            "beat_ids": self.beat_ids,
            "clip_ids": self.clip_ids,
            "warnings": self.warnings,
        }


@dataclass(frozen=True)
class SharedPromptFailure:
    asset_id: str
    asset_type: str
    reason: str
    failure_artifact_path: str

    def to_dict(self) -> dict[str, str]:
        return {
            "asset_id": self.asset_id,
            "asset_type": self.asset_type,
            "reason": self.reason,
            "failure_artifact_path": self.failure_artifact_path,
        }


@dataclass(frozen=True)
class SharedPromptSummary:
    project_slug: str
    model: str
    written_files: list[str]
    warnings: list[str]
    failures: list[SharedPromptFailure]

    def to_dict(self) -> dict[str, object]:
        return {
            "project_slug": self.project_slug,
            "model": self.model,
            "written_files": self.written_files,
            "warnings": self.warnings,
            "failures": [item.to_dict() for item in self.failures],
            "success_count": len(self.written_files),
            "failure_count": len(self.failures),
        }


@dataclass(frozen=True)
class SceneAuthoringSummary:
    planning: ScenePlanningSummary
    clip_prompts: PromptWriteSummary

    def to_dict(self) -> dict[str, object]:
        return {
            "planning": self.planning.to_dict(),
            "clip_prompts": self.clip_prompts.to_dict(),
        }


@dataclass(frozen=True)
class ChapterAuthoringSummary:
    analysis: StoryAnalysisSummary
    scene_runs: list[SceneAuthoringSummary]
    shared_prompts: SharedPromptSummary

    def to_dict(self) -> dict[str, object]:
        return {
            "analysis": self.analysis.to_dict(),
            "scene_runs": [scene_run.to_dict() for scene_run in self.scene_runs],
            "shared_prompts": self.shared_prompts.to_dict(),
        }


@dataclass(frozen=True)
class ChapterContinuitySummary:
    chapter_id: str
    state_path: str
    summary_path: str
    known_characters: list[str]
    known_environments: list[str]
    unresolved_character_ids: list[str]
    scene_order: list[str]

    def to_dict(self) -> dict[str, object]:
        return {
            "chapter_id": self.chapter_id,
            "state_path": self.state_path,
            "summary_path": self.summary_path,
            "known_characters": self.known_characters,
            "known_environments": self.known_environments,
            "unresolved_character_ids": self.unresolved_character_ids,
            "scene_order": self.scene_order,
        }


@dataclass(frozen=True)
class AuthoringCheckpointSummary:
    analysis: StoryAnalysisSummary
    planning: ScenePlanningSummary
    shared_prompts: SharedPromptSummary
    clip_prompts: PromptWriteSummary

    def to_dict(self) -> dict[str, object]:
        return {
            "analysis": self.analysis.to_dict(),
            "planning": self.planning.to_dict(),
            "shared_prompts": self.shared_prompts.to_dict(),
            "clip_prompts": self.clip_prompts.to_dict(),
        }


@dataclass(frozen=True)
class _ChapterSource:
    path: Path
    chapter_id: str
    title: str
    full_markdown: str
    text: str


@dataclass(frozen=True)
class _ParsedInputsMarkdown:
    items: dict[str, str]
    warnings: list[str]


@dataclass(frozen=True)
class _StructuredPromptDraft:
    asset_id: str
    purpose: str
    positive_prompt: str
    negative_prompt: str
    inputs: dict[str, str]
    continuity_notes: list[str]
    repair_notes: list[str]
    warnings: list[str]


@dataclass(frozen=True)
class _PacketRecord:
    fields: dict[str, str]
    sections: dict[str, str]


@dataclass(frozen=True)
class _PacketDocument:
    metadata: dict[str, str]
    sections: dict[str, str]
    records: list[_PacketRecord]


@dataclass(frozen=True)
class _TaskAttempt:
    kind: str
    status: str
    log_path: str
    message: str


def analyze_chapter(*, project_slug: str, chapter: str | None = None) -> StoryAnalysisSummary:
    started = time.perf_counter()
    print(f"[authoring] Starting chapter analysis for {project_slug}...")
    client, resolved_model = _client_and_model()
    project_dir = create_project(project_slug)
    chapter_source = _resolve_chapter_source(project_slug, chapter)

    _prune_markdown_dir(_chapter_character_breakdown_dir(project_dir=project_dir, chapter_id=chapter_source.chapter_id), keep_names=set())
    _prune_markdown_dir(_chapter_environment_breakdown_dir(project_dir=project_dir, chapter_id=chapter_source.chapter_id), keep_names=set())
    _prune_markdown_dir(_chapter_scene_breakdown_dir(project_dir=project_dir, chapter_id=chapter_source.chapter_id), keep_names=set())

    written_files: list[str] = []
    manual_requests: list[ManualCharacterDescriptionRequest] = []
    clarification_requests: list[CharacterClarificationRequest] = []
    environment_clarification_requests: list[EnvironmentClarificationRequest] = []
    warnings: list[str] = []

    summary_packet, summary_warnings = _call_chapter_summary_with_chunked_fallback(
        client=client,
        project_dir=project_dir,
        project_slug=project_slug,
        chapter_source=chapter_source,
    )
    warnings.extend(summary_warnings)
    project_summary_markdown = _require_packet_section(summary_packet, "project_summary_markdown")
    chapter_summary_markdown = _require_packet_section(summary_packet, "chapter_summary_markdown")

    project_summary_path = project_dir / "02_story_analysis" / "story_summary" / "project_summary.md"
    chapter_summary_path = project_dir / "02_story_analysis" / "chapter_analysis" / f"{chapter_source.chapter_id}_summary.md"
    _write_text(project_summary_path, project_summary_markdown)
    _write_text(chapter_summary_path, chapter_summary_markdown)
    written_files.extend([repo_relative(project_summary_path), repo_relative(chapter_summary_path)])

    character_packet, character_fallback_warnings = _call_record_extraction_with_chunked_fallback(
        client=client,
        project_dir=project_dir,
        project_slug=project_slug,
        chapter_source=chapter_source,
        chapter_summary_markdown=chapter_summary_markdown,
        task_name="character_extraction",
        record_type="character",
        index_section_name="character_index_markdown",
        prompt_builder=authoring_prompts.character_extraction_user_prompt,
        degraded_prompt_builder=authoring_prompts.character_extraction_user_prompt,
    )
    warnings.extend(character_fallback_warnings)
    character_index_markdown = _require_packet_section(character_packet, "character_index_markdown")
    character_index_path = _chapter_character_index_path(project_dir=project_dir, chapter_id=chapter_source.chapter_id)
    _write_text(character_index_path, character_index_markdown)
    _write_text(_legacy_character_index_path(project_dir=project_dir), character_index_markdown)
    written_files.append(repo_relative(character_index_path))
    written_files.append(repo_relative(_legacy_character_index_path(project_dir=project_dir)))

    canonical_lookup = _existing_character_lookup(project_dir=project_dir)
    active_manual_description_requests: dict[str, str] = {}
    active_clarification_requests: dict[str, CharacterClarificationRequest] = {}
    usable_character_count = 0
    character_breakdown_dir = _chapter_character_breakdown_dir(project_dir=project_dir, chapter_id=chapter_source.chapter_id)
    try:
        character_records = _require_packet_records(character_packet, record_type="character")
    except LMStudioError:
        character_records = []
    if not character_records:
        character_records = _extract_character_records_from_index_markdown(character_index_markdown)

    for index, raw_character in enumerate(character_records, start=1):
        try:
            asset_id = _normalize_asset_id(_require_record_field(raw_character, "asset_id"), fallback_prefix="character")
            markdown = _require_record_section(raw_character, "markdown")
            manual_description_required = _parse_packet_bool(_require_record_field(raw_character, "manual_description_required"))
            manual_description_reason = _require_record_field(raw_character, "manual_description_reason", allow_empty=not manual_description_required)
            clarification_required = _parse_packet_bool(_require_record_field(raw_character, "clarification_required", allow_empty=True) or "false")
            clarification_reason = _require_record_field(raw_character, "clarification_reason", allow_empty=True)
            clarification_question = _require_record_field(raw_character, "clarification_question", allow_empty=True)
            if clarification_required:
                if not clarification_reason:
                    clarification_reason = "The character record indicates clarification is needed, but LM Studio did not supply a reason."
                    warnings.append(f"Synthesized clarification_reason for character '{asset_id}'.")
                if not clarification_question:
                    clarification_question = "This character appears to need clarification. Can you identify the missing canonical identity or provide the missing visual facts?"
                    warnings.append(f"Synthesized clarification_question for character '{asset_id}'.")
            aliases = _require_record_field(raw_character, "aliases", allow_empty=True)
            canonical_character_id = _require_record_field(raw_character, "canonical_character_id", allow_empty=True)
            is_fully_identified = _require_record_field(raw_character, "is_fully_identified", allow_empty=True) or "false"
        except LMStudioError as exc:
            warnings.append(f"Skipped malformed character record #{index}: {exc}. Fields present: {sorted(raw_character.fields.keys())}. Sections present: {sorted(raw_character.sections.keys())}.")
            continue

        resolved_asset_id, inferred_clarification = _resolve_character_identity(
            project_slug=project_slug,
            asset_id=asset_id,
            canonical_character_id=canonical_character_id,
            aliases=aliases,
            markdown=markdown,
            canonical_lookup=canonical_lookup,
        )
        filename = f"{resolved_asset_id}.md"

        if inferred_clarification is not None and not clarification_required:
            clarification_required = True
            clarification_reason = inferred_clarification.reason
            clarification_question = inferred_clarification.question
            warnings.append(f"Auto-generated clarification request for character '{resolved_asset_id}'.")

        if clarification_required:
            manual_description_required = False
            manual_description_reason = ""

        # Extract taxonomy hints from record fields
        from .features.authoring.entity_taxonomy import EntityTaxonomyHints, format_entity_taxonomy_markdown
        
        taxonomy_hints = EntityTaxonomyHints(
            character_type_hint=raw_character.fields.get("character_type_hint", "unknown").strip() or "unknown",
            morphology_hint=raw_character.fields.get("morphology_hint", "unknown").strip() or "unknown",
            scale_hint=raw_character.fields.get("scale_hint", "unknown").strip() or "unknown",
            renderability_hint=raw_character.fields.get("renderability_hint", "unknown").strip() or "unknown",
            confidence=_parse_confidence(raw_character.fields.get("confidence", "0.0")),
            direct_identity_evidence=raw_character.fields.get("direct_identity_evidence", "").strip(),
            direct_visual_evidence=raw_character.fields.get("direct_visual_evidence", "").strip(),
            costume_or_covering_evidence=raw_character.fields.get("costume_or_covering_evidence", "").strip(),
            movement_evidence=raw_character.fields.get("movement_evidence", "").strip(),
            associated_entities=_parse_list_field(raw_character.fields.get("associated_entities", "")),
            alias_or_role_evidence=raw_character.fields.get("alias_or_role_evidence", "").strip(),
            unknowns=raw_character.fields.get("unknowns", "").strip(),
            source_refs=_parse_list_field(raw_character.fields.get("source_refs", "")),
        )
        
        taxonomy_section = format_entity_taxonomy_markdown(taxonomy_hints)
        
        character_markdown = _append_manual_description_section(
            markdown=_append_character_identity_section(
                markdown=markdown + "\n\n" + taxonomy_section,
                aliases=aliases,
                canonical_character_id=resolved_asset_id,
                is_fully_identified=is_fully_identified,
            ),
            manual_required=manual_description_required,
            manual_reason=manual_description_reason,
        )
        character_path = character_breakdown_dir / filename
        _write_text(character_path, character_markdown)
        written_files.append(repo_relative(character_path))

        if manual_description_required:
            manual_path = _manual_description_path(project_dir=project_dir, asset_id=resolved_asset_id)
            active_manual_description_requests[resolved_asset_id] = manual_description_reason
            manual_requests.append(ManualCharacterDescriptionRequest(asset_id=resolved_asset_id, source_path=repo_relative(manual_path), reason=manual_description_reason))

        if clarification_required:
            clarification_path = _character_clarification_path(project_dir=project_dir, asset_id=resolved_asset_id)
            clarification_request = CharacterClarificationRequest(
                asset_id=resolved_asset_id,
                source_path=repo_relative(clarification_path),
                reason=clarification_reason,
                question=clarification_question,
                candidate_summaries=inferred_clarification.candidate_summaries if inferred_clarification is not None else (),
            )
            active_clarification_requests[resolved_asset_id] = clarification_request
            clarification_requests.append(clarification_request)
        usable_character_count += 1

    if usable_character_count == 0:
        raise LMStudioError("Character extraction returned no usable character records after validation.")

    manual_placeholder_paths = _reconcile_manual_character_description_placeholders(project_dir=project_dir, active_requests=active_manual_description_requests)
    clarification_placeholder_paths = _reconcile_character_clarification_placeholders(project_dir=project_dir, active_requests=active_clarification_requests)
    written_files.extend(repo_relative(path) for path in manual_placeholder_paths)
    written_files.extend(repo_relative(path) for path in clarification_placeholder_paths)

    environment_packet, environment_fallback_warnings = _call_record_extraction_with_chunked_fallback(
        client=client,
        project_dir=project_dir,
        project_slug=project_slug,
        chapter_source=chapter_source,
        chapter_summary_markdown=chapter_summary_markdown,
        task_name="environment_extraction",
        record_type="environment",
        index_section_name="environment_index_markdown",
        prompt_builder=authoring_prompts.environment_extraction_user_prompt,
        degraded_prompt_builder=authoring_prompts.environment_extraction_user_prompt,
    )
    warnings.extend(environment_fallback_warnings)
    environment_index_markdown = _require_packet_section(environment_packet, "environment_index_markdown")
    environment_index_path = _chapter_environment_index_path(project_dir=project_dir, chapter_id=chapter_source.chapter_id)
    _write_text(environment_index_path, environment_index_markdown)
    _write_text(_legacy_environment_index_path(project_dir=project_dir), environment_index_markdown)
    written_files.append(repo_relative(environment_index_path))
    written_files.append(repo_relative(_legacy_environment_index_path(project_dir=project_dir)))

    environment_breakdown_dir = _chapter_environment_breakdown_dir(project_dir=project_dir, chapter_id=chapter_source.chapter_id)
    active_environment_clarification_requests: dict[str, EnvironmentClarificationRequest] = {}
    try:
        environment_records = _require_packet_records(environment_packet, record_type="environment")
    except LMStudioError:
        environment_records = []
    if not environment_records:
        environment_records = _extract_environment_records_from_index_markdown(environment_index_markdown)

    for raw_environment in environment_records:
        asset_id = _normalize_asset_id(_require_record_field(raw_environment, "asset_id"), fallback_prefix="environment")
        filename = f"{asset_id}.md"
        markdown = _require_record_section(raw_environment, "markdown")
        environment_candidates = find_environment_match_candidates(
            project_slug=project_slug,
            asset_id=asset_id,
            markdown=markdown,
            top_n=3,
        )
        environment_clarification = _resolve_environment_clarification(
            asset_id=asset_id,
            candidates=environment_candidates,
        )
        if environment_clarification is not None:
            clarification_path = _environment_clarification_path(project_dir=project_dir, asset_id=asset_id)
            environment_clarification_request = EnvironmentClarificationRequest(
                asset_id=asset_id,
                source_path=repo_relative(clarification_path),
                reason=environment_clarification.reason,
                question=environment_clarification.question,
                candidate_summaries=environment_clarification.candidate_summaries,
            )
            active_environment_clarification_requests[asset_id] = environment_clarification_request
            environment_clarification_requests.append(environment_clarification_request)
        environment_path = environment_breakdown_dir / filename
        _write_text(environment_path, markdown)
        written_files.append(repo_relative(environment_path))

    environment_clarification_placeholder_paths = _reconcile_environment_clarification_placeholders(project_dir=project_dir, active_requests=active_environment_clarification_requests)
    written_files.extend(repo_relative(path) for path in environment_clarification_placeholder_paths)

    _prune_markdown_dir(project_dir / "02_story_analysis" / "character_breakdowns", keep_names={"CHARACTER_INDEX.md", "README.md"})
    _prune_markdown_dir(project_dir / "02_story_analysis" / "environment_breakdowns", keep_names={"ENVIRONMENT_INDEX.md", "README.md"})

    scene_packet = _call_packet_task(
        client=client,
        project_dir=project_dir,
        task_name="scene_decomposition",
        system_prompt=authoring_prompts.analysis_system_prompt(),
        user_prompt=authoring_prompts.scene_decomposition_user_prompt(
            project_slug=project_slug,
            chapter_id=chapter_source.chapter_id,
            chapter_summary=chapter_summary_markdown,
        ),
        degraded_user_prompt=authoring_prompts.scene_decomposition_user_prompt(
            project_slug=project_slug,
            chapter_id=chapter_source.chapter_id,
            chapter_summary=chapter_summary_markdown,
            degraded=True,
        ),
    )
    scene_index_markdown, scene_records, scene_output_warnings = _extract_scene_decomposition_outputs(
        packet=scene_packet,
        chapter_id=chapter_source.chapter_id,
    )
    warnings.extend(scene_output_warnings)

    scene_index_path = _chapter_scene_index_path(
        project_dir=project_dir,
        chapter_id=chapter_source.chapter_id,
    )
    _write_text(scene_index_path, scene_index_markdown)
    _write_text(_legacy_scene_index_path(project_dir=project_dir), scene_index_markdown)
    written_files.append(repo_relative(scene_index_path))
    written_files.append(repo_relative(_legacy_scene_index_path(project_dir=project_dir)))

    warnings.extend(
        _validate_scene_decomposition(
            chapter_id=chapter_source.chapter_id,
            scene_records=scene_records,
        )
    )

    scene_ids: list[str] = []
    duplicate_scene_ids: list[str] = []
    scene_breakdown_dir = _chapter_scene_breakdown_dir(project_dir=project_dir, chapter_id=chapter_source.chapter_id)
    for raw_scene in scene_records:
        raw_scene_id = _normalize_scene_id(_require_record_field(raw_scene, "scene_id"))
        scene_id = validate_scene_id(f"{chapter_source.chapter_id}_{raw_scene_id}")
        filename = f"{scene_id}.md"
        markdown = _require_record_section(raw_scene, "markdown")
        create_scene(project_slug, scene_id)
        scene_path = scene_breakdown_dir / filename
        _write_text(scene_path, markdown)
        written_files.append(repo_relative(scene_path))
        if scene_id in scene_ids:
            duplicate_scene_ids.append(scene_id)
        scene_ids.append(scene_id)

    if duplicate_scene_ids:
        for duplicate_scene_id in _ordered_unique(duplicate_scene_ids):
            warnings.append(f"Duplicate scene_id detected after normalization: {duplicate_scene_id}. Keeping first occurrence and skipping later duplicate in chapter summary output.")
        scene_ids = _ordered_unique(scene_ids)

    character_breakdowns = sorted(path for path in character_breakdown_dir.glob("*.md") if path.name != "README.md")
    environment_breakdowns = sorted(path for path in environment_breakdown_dir.glob("*.md") if path.name != "README.md")
    _shared_character_registry = resolve_character_registry(project_slug, character_breakdowns)
    _shared_environment_registry = resolve_environment_registry(project_slug, environment_breakdowns)
    character_registry = resolve_character_registry(
        project_slug,
        character_breakdowns,
        load_existing=False,
        write_output=False,
    )
    environment_registry = resolve_environment_registry(
        project_slug,
        environment_breakdowns,
        load_existing=False,
        write_output=False,
    )
    canonical_character_ids, provisional_character_ids = summarize_registry_status(character_registry)
    canonical_environment_ids, provisional_environment_ids = summarize_registry_status(environment_registry)
    chapter_character_registry_path = _chapter_local_character_registry_path(
        project_dir=project_dir,
        chapter_id=chapter_source.chapter_id,
    )
    chapter_environment_registry_path = _chapter_local_environment_registry_path(
        project_dir=project_dir,
        chapter_id=chapter_source.chapter_id,
    )
    _write_text(chapter_character_registry_path, json.dumps(character_registry, indent=2))
    _write_text(chapter_environment_registry_path, json.dumps(environment_registry, indent=2))
    world_registry_paths = [repo_relative(character_registry_path(project_slug)), repo_relative(environment_registry_path(project_slug))]
    written_files.append(repo_relative(chapter_character_registry_path))
    written_files.append(repo_relative(chapter_environment_registry_path))
    written_files.extend(world_registry_paths)

    key_artifacts: list[str] = [
        repo_relative(project_summary_path),
        repo_relative(chapter_summary_path),
        repo_relative(character_index_path),
        repo_relative(environment_index_path),
        repo_relative(scene_index_path),
        repo_relative(chapter_character_registry_path),
        repo_relative(chapter_environment_registry_path),
        *world_registry_paths,
    ]
    _print_saved_artifacts("[authoring] Saved chapter analysis artifacts:", key_artifacts)

    elapsed = time.perf_counter() - started
    print(f"[authoring] Finished chapter analysis in {elapsed:.1f}s")
    return StoryAnalysisSummary(
        project_slug=project_slug,
        chapter_path=repo_relative(chapter_source.path),
        chapter_id=chapter_source.chapter_id,
        model=resolved_model,
        written_files=written_files,
        scene_ids=scene_ids,
        manual_character_description_requests=manual_requests,
        character_clarification_requests=clarification_requests,
        warnings=warnings,
        canonical_character_ids=canonical_character_ids,
        provisional_character_ids=provisional_character_ids,
        canonical_environment_ids=canonical_environment_ids,
        provisional_environment_ids=provisional_environment_ids,
        world_registry_paths=world_registry_paths,
    )


def plan_scene(*, project_slug: str, scene_id: str) -> ScenePlanningSummary:
    started = time.perf_counter()
    print(f"[authoring] Starting scene planning for {project_slug}/{scene_id}...")
    scene_id = validate_scene_id(scene_id)
    client, resolved_model = _client_and_model()
    project_dir = create_project(project_slug)
    scene_path = _resolve_scene_breakdown_path(project_dir=project_dir, scene_id=scene_id)
    if not scene_path.exists():
        raise FileNotFoundError(f"Scene breakdown not found: {scene_path}")

    written_files: list[str] = []
    warnings: list[str] = []

    beat_dir = project_dir / "02_story_analysis" / "beat_bundles" / scene_id
    ensure_dir(beat_dir)
    _prune_markdown_dir(beat_dir, keep_names=set())

    beat_packet = _call_packet_task(
        client=client,
        project_dir=project_dir,
        task_name="scene_beats",
        system_prompt=authoring_prompts.analysis_system_prompt(),
        user_prompt=authoring_prompts.scene_beats_user_prompt(project_slug=project_slug, scene_id=scene_id, scene_markdown=authoring_prompts.scene_brief_markdown(scene_path)),
        degraded_user_prompt=authoring_prompts.scene_beats_user_prompt(project_slug=project_slug, scene_id=scene_id, scene_markdown=authoring_prompts.scene_brief_markdown(scene_path), degraded=True),
    )
    updated_scene_markdown = _require_packet_section(beat_packet, "updated_scene_markdown")
    beat_index_markdown = _require_packet_section(beat_packet, "beat_index_markdown")
    _write_text(scene_path, updated_scene_markdown)
    written_files.append(repo_relative(scene_path))

    beat_index_path = beat_dir / "BEAT_INDEX.md"
    _write_text(beat_index_path, beat_index_markdown)
    written_files.append(repo_relative(beat_index_path))

    beat_ids: list[str] = []
    for raw_beat in _require_packet_records(beat_packet, record_type="beat"):
        beat_id = _normalize_beat_id(_require_record_field(raw_beat, "beat_id"))
        beat_path = beat_dir / f"{beat_id}.md"
        _write_text(beat_path, _require_record_section(raw_beat, "markdown"))
        written_files.append(repo_relative(beat_path))
        beat_ids.append(beat_id)

    clip_dir = project_dir / "02_story_analysis" / "clip_plans" / scene_id
    ensure_dir(clip_dir)
    _prune_markdown_dir(clip_dir, keep_names=set())
    scene_markdown_for_validation = authoring_prompts.scene_brief_markdown(scene_path)

    clip_attempt_specs = [
        {"label": "normal", "scene_markdown": scene_markdown_for_validation, "degraded": False},
        {"label": "repair_retry", "scene_markdown": scene_markdown_for_validation + "\n\n# Repair Instruction\nRebuild this clip roster so every beat is covered and every shot has a unique top-level CL### id. Do not compress multiple beats into one clip unless the scene is explicitly single-shot.", "degraded": True},
    ]

    last_validation_error: str | None = None
    accepted_clip_ids: list[str] = []
    accepted_clip_warnings: list[str] = []
    accepted_written_files: list[str] = []

    for attempt in clip_attempt_specs:
        attempt_written_files: list[str] = []
        attempt_warnings: list[str] = []

        clip_packet = _call_packet_task(
            client=client,
            project_dir=project_dir,
            task_name="clip_planning",
            system_prompt=authoring_prompts.analysis_system_prompt(),
            user_prompt=authoring_prompts.clip_planning_user_prompt(project_slug=project_slug, scene_id=scene_id, scene_markdown=attempt["scene_markdown"], beat_index_path=beat_index_path, degraded=attempt["degraded"]),
            degraded_user_prompt=authoring_prompts.clip_planning_user_prompt(project_slug=project_slug, scene_id=scene_id, scene_markdown=attempt["scene_markdown"], beat_index_path=beat_index_path, degraded=True),
        )
        clip_roster_markdown = _require_packet_section(clip_packet, "clip_roster_markdown")
        clip_roster_path = clip_dir / f"{scene_id}_clip_roster.md"
        _write_text(clip_roster_path, clip_roster_markdown)
        attempt_written_files.append(repo_relative(clip_roster_path))

        clip_ids: list[str] = []
        clip_markdowns: dict[str, str] = {}
        seen_clip_ids: set[str] = set()
        promoted_hierarchical_map: dict[str, str] = {}
        hierarchical_sequence_seen = 0

        _prune_markdown_dir(clip_dir, keep_names={clip_roster_path.name})

        for raw_clip in _require_packet_records(clip_packet, record_type="clip"):
            raw_clip_id = _require_record_field(raw_clip, "clip_id")
            try:
                clip_id, clip_warning = _normalize_clip_id(raw_clip_id, promoted_hierarchical_map=promoted_hierarchical_map, hierarchical_sequence_seen=hierarchical_sequence_seen)
                if _is_hierarchical_clip_id(raw_clip_id):
                    hierarchical_sequence_seen += 1
            except LMStudioError as exc:
                attempt_warnings.append(f"Skipped clip record with unusable clip_id '{raw_clip_id}': {exc}")
                continue
            if clip_warning:
                attempt_warnings.append(clip_warning)
            if clip_id in seen_clip_ids:
                attempt_warnings.append(f"Skipped duplicate clip record after normalization: '{raw_clip_id}' resolved to '{clip_id}', which already exists.")
                continue
            clip_path = clip_dir / f"{clip_id}.md"
            markdown = _require_record_section(raw_clip, "markdown")
            create_clip(project_slug, scene_id, clip_id)
            _write_text(clip_path, markdown)
            attempt_written_files.append(repo_relative(clip_path))
            clip_ids.append(clip_id)
            clip_markdowns[clip_id] = markdown
            seen_clip_ids.add(clip_id)

        if not clip_ids:
            last_validation_error = "Clip planning did not yield any usable clip ids after normalization."
            attempt_warnings.append(last_validation_error)
            warnings.extend(attempt_warnings)
            continue

        try:
            validation_warnings = _validate_clip_plan(scene_id=scene_id, scene_markdown=scene_markdown_for_validation, beat_ids=beat_ids, clip_ids=clip_ids, clip_markdowns=clip_markdowns, roster_markdown=clip_roster_markdown, strict_missing_beats=attempt["degraded"])
            attempt_warnings.extend(validation_warnings)
            missing_beat_warning = next((warning for warning in validation_warnings if "does not explicitly reference all beats" in warning), None)
            if missing_beat_warning and not attempt["degraded"]:
                last_validation_error = missing_beat_warning
                attempt_warnings.append(f"Clip plan for {scene_id} will be retried because beat coverage is incomplete on the first pass.")
                warnings.extend(attempt_warnings)
                continue
            accepted_clip_ids = clip_ids
            accepted_clip_warnings = attempt_warnings
            accepted_written_files = attempt_written_files
            break
        except LMStudioError as exc:
            last_validation_error = str(exc)
            attempt_warnings.append(f"Clip plan validation failed for {scene_id} during {attempt['label']}: {exc}")
            warnings.extend(attempt_warnings)
            continue

    if not accepted_clip_ids:
        raise LMStudioError(last_validation_error or f"Clip planning for {scene_id} failed validation after retries.")

    written_files.extend(accepted_written_files)
    warnings.extend(accepted_clip_warnings)
    clip_ids = accepted_clip_ids

    legacy_scene_path = project_dir / "02_story_analysis" / "scene_breakdowns" / f"{scene_id}.md"
    if legacy_scene_path != scene_path:
        _write_text(legacy_scene_path, updated_scene_markdown)
        written_files.append(repo_relative(legacy_scene_path))

    stale_scene_path = project_dir / "02_story_analysis" / "scene_breakdowns" / f"{scene_id}_airship_attack_and_captive_reveal.md"
    if stale_scene_path.exists():
        remove_path_within_project(stale_scene_path, project_root=project_dir.resolve())

    _print_saved_artifacts(
        f"[authoring] Saved scene planning artifacts for {scene_id}:",
        [repo_relative(scene_path), repo_relative(beat_index_path), repo_relative(clip_dir / f"{scene_id}_clip_roster.md")],
    )
    print(f"[authoring] Planned {len(clip_ids)} clips for {scene_id}: {', '.join(clip_ids)}")
    elapsed = time.perf_counter() - started
    print(f"[authoring] Finished scene planning for {scene_id} in {elapsed:.1f}s")
    return ScenePlanningSummary(project_slug=project_slug, scene_id=scene_id, model=resolved_model, written_files=written_files, beat_ids=beat_ids, clip_ids=clip_ids, warnings=warnings)


def author_scene(*, project_slug: str, scene_id: str) -> SceneAuthoringSummary:
    planning = plan_scene(project_slug=project_slug, scene_id=scene_id)
    clip_prompts = write_prompts(project_slug=project_slug, scene_id=scene_id)
    return SceneAuthoringSummary(planning=planning, clip_prompts=clip_prompts)


def author_chapter(*, project_slug: str, chapter: str | None = None) -> ChapterAuthoringSummary:
    started = time.perf_counter()
    print(f"[authoring] Starting chapter authoring cascade for {project_slug}...")
    analysis = analyze_chapter(project_slug=project_slug, chapter=chapter)
    raw_scene_ids = analysis.scene_ids
    unique_scene_ids = _ordered_unique(raw_scene_ids)
    print(f"[authoring] Raw analyzed scene order: {', '.join(raw_scene_ids)}")
    if unique_scene_ids != raw_scene_ids:
        print(f"[authoring] Deduped scene order for cascade: {', '.join(unique_scene_ids)}")
    scene_runs: list[SceneAuthoringSummary] = []
    total_scenes = len(unique_scene_ids)
    for index, scene_id in enumerate(unique_scene_ids, start=1):
        print(f"[authoring] Starting scene cascade {index}/{total_scenes}: {scene_id}")
        scene_started = time.perf_counter()
        scene_run = author_scene(project_slug=project_slug, scene_id=scene_id)
        scene_runs.append(scene_run)
        scene_elapsed = time.perf_counter() - scene_started
        succeeded = scene_run.clip_prompts.success_count
        failed = scene_run.clip_prompts.failure_count
        print(f"[authoring] Finished scene cascade {scene_id} in {scene_elapsed:.1f}s ({succeeded} prompt targets succeeded, {failed} failed)")
    shared_prompts = write_shared_prompts(project_slug=project_slug)
    elapsed = time.perf_counter() - started
    print(f"[authoring] Finished chapter authoring cascade in {elapsed:.1f}s")
    return ChapterAuthoringSummary(analysis=analysis, scene_runs=scene_runs, shared_prompts=shared_prompts)


def write_shared_prompts(*, project_slug: str) -> SharedPromptSummary:
    started = time.perf_counter()
    print(f"[authoring] Starting shared prompt writing for {project_slug}...")
    client, resolved_model = _client_and_model()
    project_dir = create_project(project_slug)
    character_index_path = _legacy_character_index_path(project_dir=project_dir)
    environment_index_path = _legacy_environment_index_path(project_dir=project_dir)
    written_files: list[str] = []
    warnings: list[str] = []
    failures: list[SharedPromptFailure] = []

    for character_breakdown_path in _iter_character_breakdown_files(project_dir=project_dir):
        asset_id = _normalize_asset_id(character_breakdown_path.stem, fallback_prefix="character")
        manual_description_path = _manual_description_path(project_dir=project_dir, asset_id=asset_id)
        try:
            character_packet = _call_packet_task(
                client=client,
                project_dir=project_dir,
                task_name="character_shared_prompts",
                system_prompt=authoring_prompts.analysis_system_prompt(),
                user_prompt=authoring_prompts.character_shared_prompt_user_prompt(project_slug=project_slug, asset_id=asset_id, character_breakdown_path=character_breakdown_path, manual_description_path=manual_description_path),
                degraded_user_prompt=authoring_prompts.character_shared_prompt_user_prompt(project_slug=project_slug, asset_id=asset_id, character_breakdown_path=character_breakdown_path, manual_description_path=manual_description_path, degraded=True),
            )
            raw_prompt = _require_single_packet_record(character_packet, record_type="character_prompt")
            record_asset_id = _normalize_asset_id(_require_record_field(raw_prompt, "asset_id"), fallback_prefix="character")
            if record_asset_id != asset_id:
                raise LMStudioError(f"LM Studio returned character prompt for '{record_asset_id}' when '{asset_id}' was requested.")
            draft = _structured_prompt_draft(raw_prompt, asset_id=asset_id, asset_type="character")
            warnings.extend(f"{asset_id}: {warning}" for warning in draft.warnings)
            prompt_path = project_dir / "03_prompt_packages" / "characters" / asset_id / f"{asset_id}_ref_prompt.md"
            sources = [repo_relative(character_index_path), repo_relative(character_breakdown_path)]
            legacy_character_source = project_dir / "02_story_analysis" / "character_breakdowns" / f"{asset_id}.md"
            if legacy_character_source != character_breakdown_path:
                sources.append(repo_relative(legacy_character_source))
            if manual_description_path.exists():
                sources.append(repo_relative(manual_description_path))
            write_prompt_package(prompt_path, _build_prompt_package(path=prompt_path, title=f"{asset_id} Character Reference Prompt", prompt_id=f"{asset_id}_ref_prompt", workflow_type="still.t2i.klein.distilled", draft=draft, sources=sources))
            written_files.append(repo_relative(prompt_path))
        except LMStudioError as exc:
            failure_path = _write_authoring_failure_artifact(project_dir=project_dir, task_name="character_shared_prompts", asset_id=asset_id, reason=str(exc))
            failures.append(SharedPromptFailure(asset_id=asset_id, asset_type="character", reason=str(exc), failure_artifact_path=repo_relative(failure_path)))

    for environment_breakdown_path in _iter_environment_breakdown_files(project_dir=project_dir):
        asset_id = _normalize_asset_id(environment_breakdown_path.stem, fallback_prefix="environment")
        try:
            environment_packet = _call_packet_task(
                client=client,
                project_dir=project_dir,
                task_name="environment_shared_prompts",
                system_prompt=authoring_prompts.analysis_system_prompt(),
                user_prompt=authoring_prompts.environment_shared_prompt_user_prompt(project_slug=project_slug, asset_id=asset_id, environment_breakdown_path=environment_breakdown_path),
                degraded_user_prompt=authoring_prompts.environment_shared_prompt_user_prompt(project_slug=project_slug, asset_id=asset_id, environment_breakdown_path=environment_breakdown_path, degraded=True),
            )
            raw_prompt = _require_single_packet_record(environment_packet, record_type="environment_prompt")
            record_asset_id = _normalize_asset_id(_require_record_field(raw_prompt, "asset_id"), fallback_prefix="environment")
            if record_asset_id != asset_id:
                raise LMStudioError(f"LM Studio returned environment prompt for '{record_asset_id}' when '{asset_id}' was requested.")
            draft = _structured_prompt_draft(raw_prompt, asset_id=asset_id, asset_type="environment")
            warnings.extend(f"{asset_id}: {warning}" for warning in draft.warnings)
            prompt_path = project_dir / "03_prompt_packages" / "environments" / asset_id / f"{asset_id}_ref_prompt.md"
            sources = [repo_relative(environment_index_path), repo_relative(environment_breakdown_path)]
            legacy_environment_source = project_dir / "02_story_analysis" / "environment_breakdowns" / f"{asset_id}.md"
            if legacy_environment_source != environment_breakdown_path:
                sources.append(repo_relative(legacy_environment_source))
            write_prompt_package(prompt_path, _build_prompt_package(path=prompt_path, title=f"{asset_id} Environment Reference Prompt", prompt_id=f"{asset_id}_ref_prompt", workflow_type="still.t2i.klein.distilled", draft=draft, sources=sources))
            written_files.append(repo_relative(prompt_path))
        except LMStudioError as exc:
            failure_path = _write_authoring_failure_artifact(project_dir=project_dir, task_name="environment_shared_prompts", asset_id=asset_id, reason=str(exc))
            failures.append(SharedPromptFailure(asset_id=asset_id, asset_type="environment", reason=str(exc), failure_artifact_path=repo_relative(failure_path)))

    elapsed = time.perf_counter() - started
    print(f"[authoring] Finished shared prompt writing in {elapsed:.1f}s")
    return SharedPromptSummary(project_slug=project_slug, model=resolved_model, written_files=written_files, warnings=warnings, failures=failures)


def build_chapter_continuity(*, project_slug: str, analysis: StoryAnalysisSummary, snapshot_data: dict | None = None) -> ChapterContinuitySummary:
    project_dir = create_project(project_slug)
    continuity_dir = project_dir / "02_story_analysis" / "world" / "continuity"
    ensure_dir(continuity_dir)
    state_path = continuity_dir / f"{analysis.chapter_id}_STATE.json"
    summary_path = continuity_dir / f"{analysis.chapter_id}_CONTINUITY_SUMMARY.md"

    snapshot_data = snapshot_data or {}
    scene_order = list(snapshot_data.get("scene_order", analysis.scene_ids))
    known_characters = list(snapshot_data.get("known_characters", analysis.canonical_character_ids))
    known_environments = list(snapshot_data.get("known_environments", analysis.canonical_environment_ids))
    unresolved_character_ids = list(snapshot_data.get("provisional_roles", analysis.provisional_character_ids))

    state = {
        "chapter_id": analysis.chapter_id,
        "scene_order": scene_order,
        "known_characters": known_characters,
        "known_environments": known_environments,
        "unresolved_character_ids": unresolved_character_ids,
        "world_registry_paths": analysis.world_registry_paths,
        "snapshot_path": repo_relative(project_dir / "02_story_analysis" / "world" / "snapshots" / f"{analysis.chapter_id}_WORLD_SNAPSHOT.json"),
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
    }
    _write_text(state_path, json.dumps(state, indent=2))
    summary_markdown = "\n".join([
        f"# {analysis.chapter_id} Continuity Summary",
        "",
        "## Scene Order",
        *[f"- {scene_id}" for scene_id in scene_order],
        "",
        "## Known Canonical Characters",
        *([f"- {item}" for item in known_characters] or ["- None"]),
        "",
        "## Unresolved / Provisional Characters",
        *([f"- {item}" for item in unresolved_character_ids] or ["- None"]),
        "",
        "## Known Canonical Environments",
        *([f"- {item}" for item in known_environments] or ["- None"]),
        "",
        "## Registry Artifacts",
        *[f"- {item}" for item in analysis.world_registry_paths],
        "",
    ])
    _write_text(summary_path, summary_markdown)
    _print_saved_artifacts(f"[authoring] Saved chapter continuity artifacts for {analysis.chapter_id}:", [repo_relative(state_path), repo_relative(summary_path)])
    return ChapterContinuitySummary(chapter_id=analysis.chapter_id, state_path=repo_relative(state_path), summary_path=repo_relative(summary_path), known_characters=known_characters, known_environments=known_environments, unresolved_character_ids=unresolved_character_ids, scene_order=scene_order)


def authoring_checkpoint(*, project_slug: str, chapter: str | None = None, scene_id: str | None = None) -> AuthoringCheckpointSummary:
    started = time.perf_counter()
    print(f"[authoring] Starting authoring checkpoint for {project_slug}...")
    analysis = analyze_chapter(project_slug=project_slug, chapter=chapter)
    build_chapter_continuity(project_slug=project_slug, analysis=analysis)
    fallback_scene_id = validate_scene_id(f"{analysis.chapter_id}_SC001")
    target_scene_id = scene_id or (analysis.scene_ids[0] if analysis.scene_ids else fallback_scene_id)
    planning = plan_scene(project_slug=project_slug, scene_id=target_scene_id)
    shared_prompts = write_shared_prompts(project_slug=project_slug)
    clip_prompts = write_prompts(project_slug=project_slug, scene_id=target_scene_id)
    elapsed = time.perf_counter() - started
    print(f"[authoring] Finished authoring checkpoint in {elapsed:.1f}s")
    return AuthoringCheckpointSummary(analysis=analysis, planning=planning, shared_prompts=shared_prompts, clip_prompts=clip_prompts)


def _client_and_model() -> tuple[LMStudioClient, str]:
    settings = load_runtime_settings()
    client = LMStudioClient(settings)
    return client, client.resolve_model()


def _resolve_chapter_source(project_slug: str, chapter: str | None) -> _ChapterSource:
    project_dir = create_project(project_slug)
    chapter_dir = project_dir / "01_source" / "chapters"
    if chapter:
        candidate = Path(chapter)
        if not candidate.is_absolute():
            if candidate.exists():
                chapter_path = candidate
            else:
                chapter_path = chapter_dir / chapter
        else:
            chapter_path = candidate
    else:
        chapter_files = sorted(chapter_dir.glob("*.md"))
        if not chapter_files:
            raise FileNotFoundError(f"No files matching *.md found under {chapter_dir}")
        chapter_path = chapter_files[0]
    if not chapter_path.exists():
        raise FileNotFoundError(f"Chapter source not found: {chapter_path}")
    full_markdown = chapter_path.read_text(encoding="utf-8")
    sections = _split_sections(full_markdown)
    chapter_id = sections.get("Chapter", "").strip() or _chapter_id_from_name(chapter_path.name)
    title = sections.get("Title", "").strip() or chapter_path.stem
    text = sections.get("Text", "").strip() or full_markdown.strip()
    if not chapter_id:
        raise ValueError(f"Could not resolve chapter id from {chapter_path}")
    return _ChapterSource(path=chapter_path, chapter_id=chapter_id, title=title, full_markdown=full_markdown, text=text)


def _chapter_character_index_path(*, project_dir: Path, chapter_id: str) -> Path:
    return project_dir / "02_story_analysis" / "character_breakdowns" / "indices" / f"{chapter_id}_CHARACTER_INDEX.md"


def _chapter_environment_index_path(*, project_dir: Path, chapter_id: str) -> Path:
    return project_dir / "02_story_analysis" / "environment_breakdowns" / "indices" / f"{chapter_id}_ENVIRONMENT_INDEX.md"


def _chapter_local_character_registry_path(*, project_dir: Path, chapter_id: str) -> Path:
    return project_dir / "02_story_analysis" / "world" / "local" / f"{chapter_id}_CHARACTER_REGISTRY.json"


def _chapter_local_environment_registry_path(*, project_dir: Path, chapter_id: str) -> Path:
    return project_dir / "02_story_analysis" / "world" / "local" / f"{chapter_id}_ENVIRONMENT_REGISTRY.json"


def _chapter_scene_index_path(*, project_dir: Path, chapter_id: str) -> Path:
    return project_dir / "02_story_analysis" / "scene_breakdowns" / "indices" / f"{chapter_id}_SCENE_INDEX.md"


def _chapter_character_breakdown_dir(*, project_dir: Path, chapter_id: str) -> Path:
    path = project_dir / "02_story_analysis" / "character_breakdowns" / "chapters" / chapter_id
    ensure_dir(path)
    return path


def _chapter_environment_breakdown_dir(*, project_dir: Path, chapter_id: str) -> Path:
    path = project_dir / "02_story_analysis" / "environment_breakdowns" / "chapters" / chapter_id
    ensure_dir(path)
    return path


def _chapter_scene_breakdown_dir(*, project_dir: Path, chapter_id: str) -> Path:
    path = project_dir / "02_story_analysis" / "scene_breakdowns" / "chapters" / chapter_id
    ensure_dir(path)
    return path


def _legacy_character_index_path(*, project_dir: Path) -> Path:
    return project_dir / "02_story_analysis" / "character_breakdowns" / "CHARACTER_INDEX.md"


def _legacy_environment_index_path(*, project_dir: Path) -> Path:
    return project_dir / "02_story_analysis" / "environment_breakdowns" / "ENVIRONMENT_INDEX.md"


def _legacy_scene_index_path(*, project_dir: Path) -> Path:
    return project_dir / "02_story_analysis" / "scene_breakdowns" / "SCENE_INDEX.md"


def _iter_character_breakdown_files(*, project_dir: Path) -> list[Path]:
    chapter_root = project_dir / "02_story_analysis" / "character_breakdowns" / "chapters"
    files = sorted(path for path in chapter_root.rglob("*.md") if path.name != "README.md") if chapter_root.exists() else []
    if files:
        return files
    legacy_root = project_dir / "02_story_analysis" / "character_breakdowns"
    return sorted(path for path in legacy_root.glob("*.md") if path.name not in {"CHARACTER_INDEX.md", "README.md"})


def _iter_environment_breakdown_files(*, project_dir: Path) -> list[Path]:
    chapter_root = project_dir / "02_story_analysis" / "environment_breakdowns" / "chapters"
    files = sorted(path for path in chapter_root.rglob("*.md") if path.name != "README.md") if chapter_root.exists() else []
    if files:
        return files
    legacy_root = project_dir / "02_story_analysis" / "environment_breakdowns"
    return sorted(path for path in legacy_root.glob("*.md") if path.name not in {"ENVIRONMENT_INDEX.md", "README.md"})


def _resolve_scene_breakdown_path(*, project_dir: Path, scene_id: str) -> Path:
    chapter_id = scene_id.split("_", 1)[0]
    chapter_path = _chapter_scene_breakdown_dir(project_dir=project_dir, chapter_id=chapter_id) / f"{scene_id}.md"
    if chapter_path.exists():
        return chapter_path
    legacy_path = project_dir / "02_story_analysis" / "scene_breakdowns" / f"{scene_id}.md"
    if legacy_path.exists():
        return legacy_path
    return chapter_path


def _existing_character_lookup(*, project_dir: Path) -> dict[str, str]:
    lookup: dict[str, str] = {}
    for path in _iter_character_breakdown_files(project_dir=project_dir):
        asset_id = path.stem
        lookup[asset_id] = asset_id
        sections = _split_sections(path.read_text(encoding="utf-8"))
        aliases = sections.get("Aliases", "").strip()
        for line in aliases.splitlines():
            normalized = _normalize_alias(line)
            if normalized:
                lookup.setdefault(normalized, asset_id)
    return lookup


def _normalize_alias(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", value.strip().lower()).strip("_")


def _ordered_unique(values: list[str]) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []
    for value in values:
        if value in seen:
            continue
        seen.add(value)
        ordered.append(value)
    return ordered


def _print_saved_artifacts(header: str, paths: list[str]) -> None:
    if not paths:
        return
    print(header)
    for path in paths:
        print(f"  - {path}")


def _resolve_character_identity(*, project_slug: str, asset_id: str, canonical_character_id: str, aliases: str, markdown: str, canonical_lookup: dict[str, str]) -> tuple[str, CharacterClarificationDetails | None]:
    candidates = [asset_id]
    if canonical_character_id:
        candidates.append(_normalize_alias(canonical_character_id))
    for alias_line in aliases.splitlines():
        normalized = _normalize_alias(alias_line)
        if normalized:
            candidates.append(normalized)
    for candidate in candidates:
        if candidate in canonical_lookup:
            return canonical_lookup[candidate], None
    scored_candidates = find_character_match_candidates(
        project_slug=project_slug,
        asset_id=asset_id,
        aliases=aliases,
        markdown=markdown,
        top_n=3,
    )
    if scored_candidates:
        top_candidate = scored_candidates[0]
        second_score = scored_candidates[1].score if len(scored_candidates) > 1 else 0
        strong_unique_match = top_candidate.score >= 70 and top_candidate.score - second_score >= 10
        if strong_unique_match and not is_generic_character_label(top_candidate.canonical_id):
            return top_candidate.canonical_id, None
        if top_candidate.score >= 40 or second_score:
            candidate_lines = []
            for candidate in scored_candidates[:3]:
                chapter_texts = ", ".join(candidate.source_chapters[:2]) or "no source chapter"
                snippet = candidate.context_snippets[0] if candidate.context_snippets else ""
                snippet_text = f" Example context: {snippet}" if snippet else ""
                candidate_lines.append(
                    f"- {candidate.canonical_id} (score {candidate.score}; chapters: {chapter_texts}; aliases: {', '.join(candidate.aliases[:4]) or '-'}){snippet_text}"
                )
            reason = "Potential existing identity matches detected:\n" + "\n".join(candidate_lines)
            question = (
                "This character may match one of the existing canonical identities above. "
                "Can you inspect the candidate chapter descriptions and confirm whether FilmCreator should merge into one of them, "
                "or keep this as a new canonical character?"
            )
            return asset_id, CharacterClarificationDetails(reason=reason, question=question, candidate_summaries=tuple(candidate_lines))
    generic_labels = {"narrator", "captain", "captive", "guard", "woman", "man", "girl", "boy", "hound"}
    if any(label in asset_id for label in generic_labels):
        question = "This character is named or role-labeled but not fully identified. Can you find a stronger canonical identity from another chapter, or should FilmCreator keep this as a scene-local provisional character?"
        return asset_id, CharacterClarificationDetails(reason="The extracted character id appears generic or role-based rather than clearly canonical.", question=question)
    sections = _split_sections(markdown)
    description_blob = "\n".join(sections.values()).lower()
    if "no physical description" in description_blob or "uncertain" in description_blob:
        question = "This character is named but lacks a stable visual description. Can you find a description from another source chapter, or should FilmCreator generate a reusable film-wide description?"
        return asset_id, CharacterClarificationDetails(reason="The character is not fully identified from this chapter alone.", question=question)
    return asset_id, None


def _resolve_environment_clarification(*, asset_id: str, candidates: list[EnvironmentMatchCandidate]) -> EnvironmentClarificationDetails | None:
    if not candidates:
        return None
    top_candidate = candidates[0]
    second_score = candidates[1].score if len(candidates) > 1 else 0
    strong_unique_match = top_candidate.score >= 70 and top_candidate.score - second_score >= 10
    if strong_unique_match:
        return None
    if top_candidate.score < 40 and not second_score:
        return None
    candidate_lines = []
    for candidate in candidates[:3]:
        chapter_texts = ", ".join(candidate.source_chapters[:2]) or "no source chapter"
        snippet = candidate.context_snippets[0] if candidate.context_snippets else ""
        snippet_text = f" Example context: {snippet}" if snippet else ""
        candidate_lines.append(
            f"- {candidate.canonical_id} (score {candidate.score}; chapters: {chapter_texts}; aliases: {', '.join(candidate.aliases[:4]) or '-'}){snippet_text}"
        )
    reason = "Potential existing environment matches detected:\n" + "\n".join(candidate_lines)
    question = (
        "This environment may match one of the existing canonical settings above. "
        "Can you inspect the candidate chapter descriptions and confirm whether FilmCreator should merge into one of them, "
        "or keep this as a new canonical environment?"
    )
    return EnvironmentClarificationDetails(reason=reason, question=question, candidate_summaries=tuple(candidate_lines))


def _extract_scene_decomposition_outputs(
    *,
    packet: _PacketDocument,
    chapter_id: str,
) -> tuple[str, list[_PacketRecord], list[str]]:
    warnings: list[str] = []
    scene_records = _require_packet_records(packet, record_type="scene")
    try:
        scene_index_markdown = _require_packet_section(packet, "scene_index_markdown")
    except LMStudioError:
        scene_index_markdown = _synthesize_scene_index_markdown(
            chapter_id=chapter_id,
            scene_records=scene_records,
        )
        warnings.append(
            f"Synthesized scene_index_markdown for {chapter_id} because the packet omitted the top-level scene index section."
        )
    scene_records, scene_id_warnings = _repair_scene_records(
        chapter_id=chapter_id,
        scene_records=scene_records,
        scene_index_markdown=scene_index_markdown,
    )
    warnings.extend(scene_id_warnings)
    return scene_index_markdown, scene_records, warnings


def _repair_scene_records(
    *,
    chapter_id: str,
    scene_records: list[_PacketRecord],
    scene_index_markdown: str,
) -> tuple[list[_PacketRecord], list[str]]:
    warnings: list[str] = []
    inferred_ids = re.findall(r"\bSC\d{3}\b", scene_index_markdown.upper())
    repaired: list[_PacketRecord] = []
    for index, record in enumerate(scene_records, start=1):
        fields = dict(record.fields)
        raw_scene_id = str(fields.get("scene_id", "")).strip().upper()
        if not raw_scene_id:
            inferred = inferred_ids[index - 1] if index - 1 < len(inferred_ids) else f"SC{index:03d}"
            fields["scene_id"] = inferred
            warnings.append(
                f"Inferred missing scene_id '{inferred}' for {chapter_id} scene record {index}."
            )
        repaired.append(_PacketRecord(fields=fields, sections=dict(record.sections)))
    return repaired, warnings


def _synthesize_scene_index_markdown(
    *,
    chapter_id: str,
    scene_records: list[_PacketRecord],
) -> str:
    lines = [
        f"# {chapter_id} Scene Index",
        "",
        "| Scene ID | Summary |",
        "|---|---|",
    ]
    for record in scene_records:
        scene_id = _require_record_field(record, "scene_id")
        markdown = _require_record_section(record, "markdown")
        summary = _scene_record_summary_line(markdown)
        lines.append(f"| {scene_id} | {summary} |")
    return "\n".join(lines)


def _scene_record_summary_line(markdown: str) -> str:
    sections = _split_sections(markdown)
    for heading in ("Scene Summary", "Scene Purpose", "Summary"):
        value = sections.get(heading, "").strip()
        if value:
            return value.replace("\n", " ")[:200]
    for line in markdown.splitlines():
        stripped = line.strip()
        if stripped and not stripped.startswith("#"):
            return stripped[:200]
    return "Scene extracted without an explicit summary."


def _analysis_system_prompt() -> str:
    return "\n".join([
        "You are FilmCreator's local authoring analyst.",
        "Work like a careful local planning assistant for chapter analysis and shot-prep authoring.",
        "Return exactly one FILMCREATOR packet in Markdown.",
        "Do not return JSON.",
        "Do not use markdown fences.",
        "Do not add commentary before or after the packet.",
        "Preserve uncertainty instead of inventing hidden facts.",
        "Prefer short, concrete section bodies over long prose.",
        "Follow the requested headings and record fields exactly.",
        "When asked to write Markdown file contents, place the complete file body inside the requested SECTION tags.",
        "When asked to extract render-facing facts, focus on visible, continuity-relevant details.",
        "If information is missing, say so briefly instead of guessing.",
    ])


def _packet_contract_block(*, task_name: str, section_names: list[str], record_templates: list[tuple[str, list[str], list[str]]] | None = None) -> str:
    lines = ["Return exactly one Markdown packet using this outer envelope:", PACKET_START_TAG, f"task: {task_name}", f"version: {PACKET_VERSION}"]
    for section_name in section_names:
        lines.extend(["", f"[[SECTION {section_name}]]", f"...{section_name} content...", SECTION_END_TAG])
    if record_templates:
        lines.extend(["", "Repeat one FILMCREATOR_RECORD block for every extracted item of that type."])
    for record_type, field_names, record_section_names in record_templates or []:
        lines.extend(["", RECORD_START_TAG, f"type: {record_type}"])
        for field_name in field_names:
            lines.append(f"{field_name}: <value>")
        for record_section_name in record_section_names:
            lines.extend(["", f"[[SECTION {record_section_name}]]", f"...{record_section_name} content...", SECTION_END_TAG])
        lines.append(RECORD_END_TAG)
    lines.append(PACKET_END_TAG)
    return "\n".join(lines)


def _chapter_summary_user_prompt(project_slug: str, chapter_source: _ChapterSource, degraded: bool = False) -> str:
    requirements = [
        "- proper nouns are allowed",
        "- do not mention ComfyUI nodes or workflow patching",
        "- separate visual continuity facts from broad story summary",
        "- make the project summary reusable across later chapters, not just this one scene",
        "- make the chapter summary specific enough to support later scene decomposition without re-reading the whole chapter",
    ]
    if degraded:
        requirements = ["- keep both sections short and concrete", "- avoid flourish and avoid hidden assumptions", "- if uncertain, state uncertainty briefly and continue"]
    return "\n\n".join([f"Project slug: {project_slug}", f"Chapter id: {chapter_source.chapter_id}", "Task: write project summary plus chapter summary for later scene extraction.", _packet_contract_block(task_name="chapter_summary", section_names=["project_summary_markdown", "chapter_summary_markdown"]), "", "Requirements:", *requirements, "", "Chapter source markdown:", chapter_source.full_markdown])


def _character_extraction_user_prompt(*, project_slug: str, chapter_source: _ChapterSource, chapter_summary: str, degraded: bool = False) -> str:
    record_fields = ["asset_id", "canonical_character_id", "aliases", "is_fully_identified", "manual_description_required", "manual_description_reason", "clarification_required", "clarification_reason", "clarification_question"]
    body_requirements = [
        "- if a character does not have enough physical or visual description in the supplied material to support dependable later image generation, set manual_description_required to true",
        "- explain exactly why in manual_description_reason",
        "- do not guess ornate missing details just to avoid the flag",
        "- if the chapter names a character without enough stable identification, set is_fully_identified to false",
        "- use aliases for alternate names or partial labels seen in the chapter",
        "- if the character might already exist under another name or is too weakly identified, set clarification_required to true and ask a targeted question",
        "- if clarification is not required, still include clarification_reason and clarification_question as empty values",
        "- every character record must include a non-empty markdown section",
        "- if details are sparse, still write a short markdown file explaining the uncertainty instead of omitting markdown",
        "- never omit the markdown section for any character record",
    ]
    if degraded:
        body_requirements = ["- keep one record per meaningful character mention", "- prefer short facts over long prose", "- if uncertain, use clarification_required instead of guessing", "- if clarification is not required, still include clarification_reason and clarification_question as empty values"]
    return "\n\n".join([f"Project slug: {project_slug}", f"Chapter id: {chapter_source.chapter_id}", "Task: extract visible and referenced characters into a character index plus one Markdown file per character.", _packet_contract_block(task_name="character_extraction", section_names=["character_index_markdown"], record_templates=[("character", record_fields, ["markdown"])]), "", "Important rules:", *body_requirements, "", "Asset id rules:", "- lowercase snake_case", "- stable across later reruns", "", "Each character Markdown file should include:", "- display name and chapter role", "- whether the character is physically present, referenced, or uncertain", "- physical description that is actually supported by the source", "- costume, silhouette, and continuity-critical traits when known", "- useful descriptive noun phrases for later render-facing prompt writing", "- explicit uncertainty notes when important details are missing", "", "Chapter summary:", chapter_summary])


def _environment_extraction_user_prompt(*, project_slug: str, chapter_source: _ChapterSource, chapter_summary: str, degraded: bool = False) -> str:
    notes = ["- include stable environment families rather than every one-off mention", "- prefer visible geography and atmosphere over literary abstraction"]
    if degraded:
        notes = ["- keep the environment set small and useful", "- use concise visible descriptions"]
    return "\n\n".join([f"Project slug: {project_slug}", f"Chapter id: {chapter_source.chapter_id}", "Task: extract environment families into an environment index plus one Markdown file per environment family.", _packet_contract_block(task_name="environment_extraction", section_names=["environment_index_markdown"], record_templates=[("environment", ["asset_id"], ["markdown"])]), "", "Asset id rules:", "- lowercase snake_case", "- stable across later reruns", *notes, "", "Each environment Markdown file should include:", "- environment role such as primary, secondary, or transit setting", "- architecture or geography", "- lighting and atmosphere cues", "- scale cues and recurring environmental anchors", "- useful descriptive noun phrases for later render-facing prompt writing", "", "Chapter summary:", chapter_summary])


def _scene_decomposition_user_prompt(*, project_slug: str, chapter_id: str, chapter_summary: str, degraded: bool = False) -> str:
    extra_rules = [
        "Prefer dramatic and staging boundaries, not every paragraph break.",
        "Preserve major narrative function changes as separate scenes.",
        "Do not merge setup, escalation, climax, and aftermath into one scene if they have different emotional or staging functions.",
        "If the chapter includes a reveal, aftermath, or emotional payoff after action, give that material its own scene when possible.",
        "Use a new scene when location, primary objective, or emotional mode changes significantly.",
        "For action chapters, prefer a sequence like: setup scene, escalation scene, climax/action consequence scene, aftermath/reveal scene when the source supports it.",
    ]
    if degraded:
        extra_rules = ["Keep scene count practical, but do not collapse the ending payoff into the action scene.", "Prefer 4 strong scenes over 3 merged scenes when the chapter clearly contains setup, escalation, consequence, and aftermath.", "Create a new scene when a new emotional function begins."]
    return "\n\n".join([f"Project slug: {project_slug}", f"Chapter id: {chapter_id}", "Task: break the chapter into a small number of coherent scenes for later beat and clip planning.", _packet_contract_block(task_name="scene_decomposition", section_names=["scene_index_markdown"], record_templates=[("scene", ["scene_id"], ["markdown"])]), "", "Scene id rules:", "- use SC### only inside the packet", "- start at SC001 for this chapter", "- do not include the chapter prefix in scene_id values", "- the chapter prefix will be applied externally by FilmCreator", *extra_rules, "Each scene Markdown file should include:", "- scene purpose", "- scene summary", "- participating characters", "- participating environments", "- dominant emotional shift", "- likely visual coverage families", "- likely continuity sensitivities", "", "Chapter summary:", chapter_summary])


def _scene_beats_user_prompt(*, project_slug: str, scene_id: str, scene_markdown: str, degraded: bool = False) -> str:
    extra_rules = ["- keep beats reusable for later coverage planning"]
    if degraded:
        extra_rules = ["- keep beats short and practical"]
    return "\n\n".join([f"Project slug: {project_slug}", f"Scene id: {scene_id}", "Task: deepen one scene into reusable beat bundles and update the scene breakdown with clearer staging facts.", _packet_contract_block(task_name="scene_beats", section_names=["updated_scene_markdown", "beat_index_markdown"], record_templates=[("beat", ["beat_id"], ["markdown"])]), "", "Beat id rules:", "- use BT### within the scene", *extra_rules, "Each beat Markdown file should include:", "- beat purpose", "- beat start state and end state", "- character placement and movement logic", "- geography, axis, or eyeline facts when relevant", "- prop, vehicle, crowd, and environmental state that affects continuity", "- likely coverage families", "", "Scene breakdown markdown:", scene_markdown])


def _clip_planning_user_prompt(*, project_slug: str, scene_id: str, scene_markdown: str, beat_index_path: Path, degraded: bool = False) -> str:
    beat_bundle_dir = beat_index_path.parent
    beat_bundles = _markdown_bundle(directory=beat_bundle_dir, exclude_names={"BEAT_INDEX.md", "README.md"})
    clip_rules = [
        "- clip = cut",
        "- use clip ids in canonical CL001 format only",
        "- every shot must get its own top-level clip id such as CL001, CL002, CL003, CL004",
        "- never use parent-child or hierarchical clip ids such as CL001_001, CL001-A, CL001.1, CL001/001, CL001a, or CL001_variant",
        "- do not append suffixes like _01, -A, _variant, _alt, or sub-shot fragments to clip ids",
        "- if you feel tempted to write CL001_001 and CL001_002, write CL001 and CL002 instead",
        "- if you need to describe an alternate angle or sub-shot, put that in the clip markdown, not the clip id",
        "- most clips should target around 5 seconds",
        "- treat continuous_follow as rare",
        "- prefer reframe_same_moment, reblock_same_scene, insert, and cutaway when appropriate",
        "- include continuity mode, composition type, starting keyframe strategy, dependency policy, fallback strategy, visible character assets, required refs, optional refs, opening keyframe intent, cut motion intent, and interval beats",
        "- identify one or two strong initial test clips if the scene allows it",
    ]
    if degraded:
        clip_rules = ["- keep the first clip roster small and testable", "- prefer independent clips", "- use simple canonical ids only, such as CL001, CL002, CL003", "- never use hierarchical ids like CL001_001 or CL001-A", "- do not add suffixes or variants to clip ids", "- keep metadata concise but complete"]
    return "\n\n".join([f"Project slug: {project_slug}", f"Scene id: {scene_id}", "Task: turn the scene and beat bundles into an ordered clip roster and one clip plan per clip.", _packet_contract_block(task_name="clip_planning", section_names=["clip_roster_markdown"], record_templates=[("clip", ["clip_id"], ["markdown"])]), "", "Clip planning rules:", *clip_rules, "", "Scene breakdown markdown:", scene_markdown, "", f"Beat index path: {repo_relative(beat_index_path)}", beat_index_path.read_text(encoding="utf-8"), "", "Beat bundle files:", beat_bundles or "(none)"])


def _character_shared_prompt_user_prompt(*, project_slug: str, asset_id: str, character_breakdown_path: Path, manual_description_path: Path, degraded: bool = False) -> str:
    character_markdown = character_breakdown_path.read_text(encoding="utf-8")
    manual_description = manual_description_path.read_text(encoding="utf-8") if manual_description_path.exists() else ""
    rules = ["- purpose and inputs may use stable asset ids", "- final positive and negative prompt bodies should avoid proper nouns and use descriptive noun phrases", "- keep prompts concrete and visible", "- prefer stable face, hair, body type, costume logic, silhouette, and recurring materials over scene-specific blocking"]
    if degraded:
        rules = ["- keep the sections short and usable", "- preserve only the most stable visible traits", "- if uncertain, leave a short continuity note instead of inventing detail"]
    return "\n\n".join([f"Project slug: {project_slug}", f"Asset id: {asset_id}", "Task: write one reusable shared character-reference prompt draft for stable local generation.", _packet_contract_block(task_name="character_shared_prompts", section_names=[], record_templates=[("character_prompt", ["asset_id"], ["purpose", "positive_prompt", "negative_prompt", "inputs_markdown", "continuity_notes_markdown", "repair_notes_markdown"])]), "", "Rules:", *rules, "", f"Character breakdown path: {repo_relative(character_breakdown_path)}", character_markdown, "", f"Manual character description path: {repo_relative(manual_description_path)}", manual_description or "(missing)"])


def _environment_shared_prompt_user_prompt(*, project_slug: str, asset_id: str, environment_breakdown_path: Path, degraded: bool = False) -> str:
    environment_markdown = environment_breakdown_path.read_text(encoding="utf-8")
    rules = ["- purpose and inputs may use stable asset ids", "- final positive and negative prompt bodies should avoid proper nouns and use descriptive noun phrases", "- keep prompts concrete and visible", "- emphasize stable architecture, geography, scale, atmosphere, and recurring environmental anchors"]
    if degraded:
        rules = ["- keep the environment identity compact and stable", "- use short visible descriptors only"]
    return "\n\n".join([f"Project slug: {project_slug}", f"Asset id: {asset_id}", "Task: write one reusable shared environment-reference prompt draft for stable local generation.", _packet_contract_block(task_name="environment_shared_prompts", section_names=[], record_templates=[("environment_prompt", ["asset_id"], ["purpose", "positive_prompt", "negative_prompt", "inputs_markdown", "continuity_notes_markdown", "repair_notes_markdown"])]), "", "Rules:", *rules, "", f"Environment breakdown path: {repo_relative(environment_breakdown_path)}", environment_markdown])


def _scene_brief_markdown(scene_path: Path) -> str:
    sections = _split_sections(scene_path.read_text(encoding="utf-8"))
    desired_headings = ["Scene Purpose", "Scene Summary", "Participating Characters", "Participating Environments", "Dominant Emotional Shift", "Likely Visual Coverage Families", "Likely Continuity Sensitivities"]
    parts: list[str] = []
    for heading in desired_headings:
        value = sections.get(heading, "").strip()
        if value:
            parts.extend([f"# {heading}", value, ""])
    if parts:
        return "\n".join(parts).strip()
    return scene_path.read_text(encoding="utf-8")


def _call_packet_task(*, client: LMStudioClient, project_dir: Path, task_name: str, system_prompt: str, user_prompt: str, degraded_user_prompt: str) -> _PacketDocument:
    task_started = time.perf_counter()
    print(f"[authoring] Task {task_name} started...")
    attempts: list[_TaskAttempt] = []
    for kind, active_user_prompt in [("normal", user_prompt), ("same_prompt_retry", user_prompt), ("degraded_retry", degraded_user_prompt)]:
        if kind != "normal":
            print(f"[authoring] Task {task_name} retrying with {kind}...")
        result = _chat_completion_result(client=client, system_prompt=system_prompt, user_prompt=active_user_prompt, temperature=0.2)
        log_path = _write_authoring_exchange_log(project_dir=project_dir, task_name=task_name, system_prompt=system_prompt, user_prompt=active_user_prompt, response=result.text)
        if result.is_success:
            try:
                packet = _parse_packet_document(result.text, expected_task=task_name)
                elapsed = time.perf_counter() - task_started
                print(f"[authoring] Task {task_name} finished in {elapsed:.1f}s")
                return packet
            except LMStudioError as exc:
                attempts.append(_TaskAttempt(kind=kind, status="parse_failed", log_path=repo_relative(log_path), message=str(exc)))
                continue
        attempts.append(_TaskAttempt(kind=kind, status=result.status, log_path=repo_relative(log_path), message=result.error_message or "Unspecified LM Studio authoring failure."))
    failure_path = _write_authoring_failure_artifact(project_dir=project_dir, task_name=task_name, asset_id=None, reason="; ".join(f"{attempt.kind}:{attempt.status}:{attempt.message}" for attempt in attempts))
    raise LMStudioError(f"Authoring task '{task_name}' failed after retries. Failure artifact: {repo_relative(failure_path)}")


def _call_record_extraction_with_chunked_fallback(
    *,
    client: LMStudioClient,
    project_dir: Path,
    project_slug: str,
    chapter_source: _ChapterSource,
    chapter_summary_markdown: str,
    task_name: str,
    record_type: str,
    index_section_name: str,
    prompt_builder,
    degraded_prompt_builder,
) -> tuple[_PacketDocument, list[str]]:
    warnings: list[str] = []
    full_packet: _PacketDocument | None = None
    try:
        full_packet = _call_packet_task(
            client=client,
            project_dir=project_dir,
            task_name=task_name,
            system_prompt=authoring_prompts.analysis_system_prompt(),
            user_prompt=prompt_builder(
                project_slug=project_slug,
                chapter_source=chapter_source,
                chapter_summary=chapter_summary_markdown,
            ),
            degraded_user_prompt=degraded_prompt_builder(
                project_slug=project_slug,
                chapter_source=chapter_source,
                chapter_summary=chapter_summary_markdown,
                degraded=True,
            ),
        )
    except LMStudioError as exc:
        warnings.append(f"{task_name} full chapter pass failed: {exc}")
    else:
        full_records, full_record_warnings, full_index_markdown = _extract_usable_records_from_packet(
            packet=full_packet,
            record_type=record_type,
            index_section_name=index_section_name,
        )
        warnings.extend(full_record_warnings)
        if full_records:
            if not full_index_markdown.strip():
                full_index_markdown = _synthesize_record_index_markdown(
                    chapter_id=chapter_source.chapter_id,
                    record_type=record_type,
                    records=full_records,
                )
                warnings.append(
                    f"{task_name} full chapter pass omitted {index_section_name}; synthesized an index from explicit records."
                )
            return (
                _PacketDocument(
                    metadata=dict(full_packet.metadata),
                    sections={index_section_name: full_index_markdown},
                    records=full_records,
                ),
                warnings,
            )
        warnings.append(
            f"{task_name} returned no usable {record_type} records on the full chapter pass; retrying with overlapping half-chapter chunks."
        )
        repair_packet, repair_warnings = _repair_record_extraction_packet(
            client=client,
            project_dir=project_dir,
            project_slug=project_slug,
            chapter_source=chapter_source,
            chapter_summary_markdown=chapter_summary_markdown,
            task_name=task_name,
            record_type=record_type,
            index_section_name=index_section_name,
            existing_index_markdown=full_index_markdown,
        )
        warnings.extend(repair_warnings)
        if repair_packet is not None:
            repair_records, repair_record_warnings, repair_index_markdown = _extract_usable_records_from_packet(
                packet=repair_packet,
                record_type=record_type,
                index_section_name=index_section_name,
            )
            warnings.extend(repair_record_warnings)
            if repair_records:
                if not repair_index_markdown.strip():
                    repair_index_markdown = _synthesize_record_index_markdown(
                        chapter_id=chapter_source.chapter_id,
                        record_type=record_type,
                        records=repair_records,
                    )
                    warnings.append(
                        f"{task_name} repair pass omitted {index_section_name}; synthesized an index from explicit records."
                    )
                warnings.append(f"{task_name} recovered usable {record_type} records from a focused repair pass before chunking.")
                return (
                    _PacketDocument(
                        metadata=dict(repair_packet.metadata),
                        sections={index_section_name: repair_index_markdown},
                        records=repair_records,
                    ),
                    warnings,
                )

    chunk_texts = _split_text_into_fallback_chunks(chapter_source.full_markdown)
    merged_records_by_asset_id: dict[str, _PacketRecord] = {}
    merged_sections_by_asset_id: dict[str, list[str]] = {}
    chunk_successes = 0

    for chunk_index, chunk_text in enumerate(chunk_texts, start=1):
        chunk_prompt = "\n\n".join(
            [
                f"Fallback extraction chunk {chunk_index}/{len(chunk_texts)} for {task_name}.",
                "Use only the chapter excerpt below for this pass.",
                chunk_text,
            ]
        )
        try:
            chunk_packet = _call_packet_task(
                client=client,
                project_dir=project_dir,
                task_name=task_name,
                system_prompt=authoring_prompts.analysis_system_prompt(),
                user_prompt=prompt_builder(
                    project_slug=project_slug,
                    chapter_source=chapter_source,
                    chapter_summary=chunk_prompt,
                ),
                degraded_user_prompt=degraded_prompt_builder(
                    project_slug=project_slug,
                    chapter_source=chapter_source,
                    chapter_summary=chunk_prompt,
                    degraded=True,
                ),
            )
        except LMStudioError as exc:
            warnings.append(f"{task_name} chunk {chunk_index}/{len(chunk_texts)} failed: {exc}")
            continue

        chunk_records, chunk_warnings, chunk_index_markdown = _extract_usable_records_from_packet(
            packet=chunk_packet,
            record_type=record_type,
            index_section_name=index_section_name,
        )
        warnings.extend(chunk_warnings)
        if chunk_records:
            chunk_successes += 1
        for record in chunk_records:
            asset_id = _normalize_asset_id(_require_record_field(record, "asset_id"), fallback_prefix=record_type)
            if asset_id not in merged_records_by_asset_id:
                merged_records_by_asset_id[asset_id] = record
                merged_sections_by_asset_id[asset_id] = [record.sections.get("markdown", "").strip()]
                continue
            merged_records_by_asset_id[asset_id] = _merge_record_entries(
                merged_records_by_asset_id[asset_id],
                record,
                record_type=record_type,
            )
            if record.sections.get("markdown", "").strip():
                merged_sections_by_asset_id.setdefault(asset_id, [])
                merged_sections_by_asset_id[asset_id].append(record.sections["markdown"].strip())
        if not chunk_records:
            warnings.append(
                f"{task_name} chunk {chunk_index}/{len(chunk_texts)} produced no usable {record_type} records after validation."
            )

    merged_records = []
    for asset_id, record in merged_records_by_asset_id.items():
        merged_markdown_parts = []
        for markdown_part in merged_sections_by_asset_id.get(asset_id, []):
            if markdown_part and markdown_part not in merged_markdown_parts:
                merged_markdown_parts.append(markdown_part)
        merged_sections = dict(record.sections)
        if merged_markdown_parts:
            merged_sections["markdown"] = "\n\n---\n\n".join(merged_markdown_parts).strip()
        merged_records.append(_PacketRecord(fields=record.fields, sections=merged_sections))

    if not merged_records:
        failure_reason = f"{task_name} could not recover any usable {record_type} records from chunked fallback."
        warnings.append(failure_reason)
        if full_packet is None:
            raise LMStudioError(failure_reason)
        raise LMStudioError(failure_reason)

    synthesized_index_markdown = _synthesize_record_index_markdown(
        chapter_id=chapter_source.chapter_id,
        record_type=record_type,
        records=merged_records,
    )
    warnings.append(
        f"{task_name} recovered {len(merged_records)} usable {record_type} record(s) across {chunk_successes} successful chunk pass(es)."
    )
    return (
        _PacketDocument(
            metadata={"task": task_name, "version": PACKET_VERSION, "source_mode": "chunked_fallback"},
            sections={index_section_name: synthesized_index_markdown},
            records=merged_records,
        ),
        warnings,
    )


def _repair_record_extraction_packet(
    *,
    client: LMStudioClient,
    project_dir: Path,
    project_slug: str,
    chapter_source: _ChapterSource,
    chapter_summary_markdown: str,
    task_name: str,
    record_type: str,
    index_section_name: str,
    existing_index_markdown: str,
) -> tuple[_PacketDocument | None, list[str]]:
    warnings: list[str] = []
    candidate_summaries = _record_repair_candidate_summaries(
        project_slug=project_slug,
        chapter_id=chapter_source.chapter_id,
        record_type=record_type,
        existing_index_markdown=existing_index_markdown,
    )
    repair_prompt = _record_extraction_repair_prompt(
        project_slug=project_slug,
        chapter_id=chapter_source.chapter_id,
        chapter_summary=chapter_summary_markdown,
        task_name=task_name,
        record_type=record_type,
        index_section_name=index_section_name,
        existing_index_markdown=existing_index_markdown,
        chapter_markdown=chapter_source.full_markdown,
        candidate_summaries=candidate_summaries,
    )
    try:
        repair_packet = _call_packet_task(
            client=client,
            project_dir=project_dir,
            task_name=task_name,
            system_prompt=authoring_prompts.analysis_system_prompt(),
            user_prompt=repair_prompt,
            degraded_user_prompt=_record_extraction_repair_prompt(
                project_slug=project_slug,
                chapter_id=chapter_source.chapter_id,
                chapter_summary=chapter_summary_markdown,
                task_name=task_name,
                record_type=record_type,
                index_section_name=index_section_name,
                existing_index_markdown=existing_index_markdown,
                chapter_markdown=chapter_source.full_markdown,
                candidate_summaries=candidate_summaries,
                degraded=True,
            ),
        )
    except LMStudioError as exc:
        warnings.append(f"{task_name} focused repair pass failed: {exc}")
        return None, warnings
    return repair_packet, warnings


def _call_chapter_summary_with_chunked_fallback(
    *,
    client: LMStudioClient,
    project_dir: Path,
    project_slug: str,
    chapter_source: _ChapterSource,
) -> tuple[_PacketDocument, list[str]]:
    warnings: list[str] = []
    full_packet: _PacketDocument | None = None
    try:
        full_packet = _call_packet_task(
            client=client,
            project_dir=project_dir,
            task_name="chapter_summary",
            system_prompt=authoring_prompts.analysis_system_prompt(),
            user_prompt=authoring_prompts.chapter_summary_user_prompt(project_slug, chapter_source),
            degraded_user_prompt=authoring_prompts.chapter_summary_user_prompt(project_slug, chapter_source, degraded=True),
        )
    except LMStudioError as exc:
        warnings.append(f"chapter_summary full chapter pass failed: {exc}")
    else:
        project_summary_markdown = _require_packet_section(full_packet, "project_summary_markdown", allow_empty=True)
        chapter_summary_markdown = _require_packet_section(full_packet, "chapter_summary_markdown", allow_empty=True)
        if project_summary_markdown and chapter_summary_markdown:
            return (
                _PacketDocument(
                    metadata=dict(full_packet.metadata),
                    sections={
                        "project_summary_markdown": project_summary_markdown,
                        "chapter_summary_markdown": chapter_summary_markdown,
                    },
                    records=full_packet.records,
                ),
                warnings,
            )
        missing_sections = [
            section_name
            for section_name, section_value in (
                ("project_summary_markdown", project_summary_markdown),
                ("chapter_summary_markdown", chapter_summary_markdown),
            )
            if not section_value.strip()
        ]
        warnings.append(
            "chapter_summary full chapter pass was missing required summary sections: "
            + ", ".join(missing_sections)
        )
        if len(missing_sections) == 1:
            repair_packet, repair_warnings = _repair_chapter_summary_sections(
                client=client,
                project_dir=project_dir,
                project_slug=project_slug,
                chapter_source=chapter_source,
                missing_sections=missing_sections,
                existing_sections={
                    "project_summary_markdown": project_summary_markdown,
                    "chapter_summary_markdown": chapter_summary_markdown,
                },
            )
            warnings.extend(repair_warnings)
            if repair_packet is not None:
                repaired_sections = {
                    "project_summary_markdown": project_summary_markdown or _require_packet_section(
                        repair_packet,
                        "project_summary_markdown",
                    ),
                    "chapter_summary_markdown": chapter_summary_markdown or _require_packet_section(
                        repair_packet,
                        "chapter_summary_markdown",
                    ),
                }
                warnings.append(
                    f"chapter_summary repaired missing section(s) from a smaller repair pass: {', '.join(missing_sections)}"
                )
                return (
                    _PacketDocument(
                        metadata=dict(full_packet.metadata),
                        sections=repaired_sections,
                        records=full_packet.records,
                    ),
                    warnings,
                )

    chunk_texts = _split_text_into_fallback_chunks(chapter_source.full_markdown)
    chunk_packets: list[_PacketDocument] = []
    for chunk_index, chunk_text in enumerate(chunk_texts, start=1):
        chunk_label = f"{chunk_index}/{len(chunk_texts)}"
        try:
            chunk_packet = _call_packet_task(
                client=client,
                project_dir=project_dir,
                task_name="chapter_summary",
                system_prompt=authoring_prompts.analysis_system_prompt(),
                user_prompt=_chapter_summary_chunk_prompt(
                    project_slug=project_slug,
                    chapter_id=chapter_source.chapter_id,
                    chunk_label=chunk_label,
                    chunk_markdown=chunk_text,
                ),
                degraded_user_prompt=_chapter_summary_chunk_prompt(
                    project_slug=project_slug,
                    chapter_id=chapter_source.chapter_id,
                    chunk_label=chunk_label,
                    chunk_markdown=chunk_text,
                    degraded=True,
                ),
            )
        except LMStudioError as exc:
            warnings.append(f"chapter_summary chunk {chunk_label} failed: {exc}")
            continue

        try:
            _require_packet_section(chunk_packet, "project_summary_markdown")
            _require_packet_section(chunk_packet, "chapter_summary_markdown")
        except LMStudioError as exc:
            warnings.append(f"chapter_summary chunk {chunk_label} missing summary sections: {exc}")
            continue
        chunk_packets.append(chunk_packet)

    if not chunk_packets:
        failure_reason = "chapter_summary could not recover any usable summary packets from chunked fallback."
        warnings.append(failure_reason)
        raise LMStudioError(failure_reason)

    try:
        synthesis_packet = _call_packet_task(
            client=client,
            project_dir=project_dir,
            task_name="chapter_summary",
            system_prompt=authoring_prompts.analysis_system_prompt(),
            user_prompt=_chapter_summary_synthesis_prompt(
                project_slug=project_slug,
                chapter_id=chapter_source.chapter_id,
                chunk_packets=chunk_packets,
            ),
            degraded_user_prompt=_chapter_summary_synthesis_prompt(
                project_slug=project_slug,
                chapter_id=chapter_source.chapter_id,
                chunk_packets=chunk_packets,
                degraded=True,
            ),
        )
        project_summary_markdown = _require_packet_section(synthesis_packet, "project_summary_markdown")
        chapter_summary_markdown = _require_packet_section(synthesis_packet, "chapter_summary_markdown")
        warnings.append(
            f"chapter_summary recovered from {len(chunk_packets)} chunk summary packet(s) and synthesized a final summary."
        )
        return (
            _PacketDocument(
                metadata=dict(synthesis_packet.metadata),
                sections={
                    "project_summary_markdown": project_summary_markdown,
                    "chapter_summary_markdown": chapter_summary_markdown,
                },
                records=synthesis_packet.records,
            ),
            warnings,
        )
    except LMStudioError as exc:
        warnings.append(f"chapter_summary synthesis pass failed: {exc}; falling back to deterministic chunk merge.")
        merged_project_summary = _merge_summary_texts(
            title="Project Summary",
            texts=[_require_packet_section(packet, "project_summary_markdown") for packet in chunk_packets],
        )
        merged_chapter_summary = _merge_summary_texts(
            title="Chapter Summary",
            texts=[_require_packet_section(packet, "chapter_summary_markdown") for packet in chunk_packets],
        )
    return (
        _PacketDocument(
            metadata={"task": "chapter_summary", "version": PACKET_VERSION, "source_mode": "chunked_merge"},
            sections={
                "project_summary_markdown": merged_project_summary,
                    "chapter_summary_markdown": merged_chapter_summary,
                },
                records=[],
        ),
        warnings,
    )


def _repair_chapter_summary_sections(
    *,
    client: LMStudioClient,
    project_dir: Path,
    project_slug: str,
    chapter_source: _ChapterSource,
    missing_sections: list[str],
    existing_sections: dict[str, str],
) -> tuple[_PacketDocument | None, list[str]]:
    warnings: list[str] = []
    existing_section_names = [
        section_name
        for section_name, section_value in existing_sections.items()
        if section_value.strip()
    ]
    try:
        repair_packet = _call_packet_task(
            client=client,
            project_dir=project_dir,
            task_name="chapter_summary",
            system_prompt=authoring_prompts.analysis_system_prompt(),
            user_prompt=_chapter_summary_repair_prompt(
                project_slug=project_slug,
                chapter_id=chapter_source.chapter_id,
                missing_sections=missing_sections,
                existing_sections=existing_section_names,
                chapter_markdown=chapter_source.full_markdown,
            ),
            degraded_user_prompt=_chapter_summary_repair_prompt(
                project_slug=project_slug,
                chapter_id=chapter_source.chapter_id,
                missing_sections=missing_sections,
                existing_sections=existing_section_names,
                chapter_markdown=chapter_source.full_markdown,
                degraded=True,
            ),
        )
    except LMStudioError as exc:
        warnings.append(f"chapter_summary repair pass failed: {exc}")
        return None, warnings

    for section_name in missing_sections:
        try:
            _require_packet_section(repair_packet, section_name)
        except LMStudioError as exc:
            warnings.append(f"chapter_summary repair pass still missing {section_name}: {exc}")
            return None, warnings
    return repair_packet, warnings


def _chat_completion_result(
    *,
    client: LMStudioClient,
    system_prompt: str,
    user_prompt: str,
    temperature: float,
) -> object:
    if hasattr(client, "chat_completion_result"):
        return client.chat_completion_result(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            temperature=temperature,
        )

    text = client.chat_completion(
        system_prompt=system_prompt,
        user_prompt=user_prompt,
        temperature=temperature,
    )
    return SimpleNamespace(
        status="success",
        text=text,
        error_message=None,
        is_success=True,
    )


def _chapter_summary_chunk_prompt(*, project_slug: str, chapter_id: str, chunk_label: str, chunk_markdown: str, degraded: bool = False) -> str:
    requirements = [
        f"- this is only chunk {chunk_label} of the chapter source",
        "- summarize only the information present in this chunk",
        "- keep the project summary reusable across chapters",
        "- keep the chapter summary focused on events, characters, and settings present in this chunk",
        "- treat the chapter summary as production evidence rather than a reader synopsis: preserve every distinct filmable event, entrance, exit, reveal, decision, object interaction, location/subzone shift, visual continuity state, and uncertainty that later scene, shot, descriptor, or prompt stages would need",
    ]
    if degraded:
        requirements = [
            f"- this is only chunk {chunk_label} of the chapter source",
            "- keep both summaries concise but useful",
            "- preserve major events and named entities from this chunk",
        ]
    return "\n\n".join(
        [
            f"Project slug: {project_slug}",
            f"Chapter id: {chapter_id}",
            "Task: write project summary plus chapter summary for later scene extraction.",
            _packet_contract_block(task_name="chapter_summary", section_names=["project_summary_markdown", "chapter_summary_markdown"]),
            "",
            f"Chunk label: {chunk_label}",
            "Requirements:",
            *requirements,
            "",
            "Chapter source markdown:",
            chunk_markdown,
        ]
    )


def _chapter_summary_repair_prompt(
    *,
    project_slug: str,
    chapter_id: str,
    missing_sections: list[str],
    existing_sections: list[str],
    chapter_markdown: str,
    degraded: bool = False,
) -> str:
    try:
        chapter_body = chapter_text(project_slug, chapter_id) or chapter_markdown
    except FileNotFoundError:
        chapter_body = chapter_markdown
    missing_section_list = "\n".join(f"- {section_name}" for section_name in missing_sections)
    existing_section_list = "\n".join(f"- {section_name}" for section_name in existing_sections) or "- none"
    requirements = [
        "- repair only the missing summary section(s)",
        "- do not rewrite the section(s) that are already present unless absolutely necessary",
        "- keep the summary grounded in the chapter source",
        "- return a valid FilmCreator packet with the requested markdown sections only",
    ]
    if degraded:
        requirements = [
            "- keep the repair concise",
            "- supply only the missing section body or bodies",
        ]
    return "\n\n".join(
        [
            f"Project slug: {project_slug}",
            f"Chapter id: {chapter_id}",
            "Task: repair missing chapter-summary section(s) after a partial packet response.",
            _packet_contract_block(task_name="chapter_summary", section_names=["project_summary_markdown", "chapter_summary_markdown"]),
            "",
            "Existing sections already present in the prior packet:",
            existing_section_list,
            "",
            "Missing sections to supply:",
            missing_section_list,
            "",
            "Requirements:",
            *requirements,
            "",
            "Chapter source markdown:",
            chapter_body,
        ]
    )


def _record_extraction_repair_prompt(
    *,
    project_slug: str,
    chapter_id: str,
    chapter_summary: str,
    task_name: str,
    record_type: str,
    index_section_name: str,
    existing_index_markdown: str,
    chapter_markdown: str,
    candidate_summaries: list[str] | None = None,
    degraded: bool = False,
) -> str:
    try:
        chapter_body = chapter_text(project_slug, chapter_id) or chapter_markdown
    except FileNotFoundError:
        chapter_body = chapter_markdown
    record_label = {
        "character": "character",
        "environment": "environment",
        "scene": "scene",
    }.get(record_type, "record")
    requirements = [
        f"- repair only the missing explicit {record_label} record blocks",
        "- keep the response grounded in the supplied chapter summary and source text",
        "- preserve any working index markdown if it already exists",
        "- do not invent new record types",
        "- return a valid FilmCreator packet using the requested task name",
    ]
    if degraded:
        requirements = [
            f"- keep the repair concise and emit only the missing explicit {record_label} records",
            "- preserve the existing index markdown if possible",
        ]
    existing_index_text = existing_index_markdown.strip() or "(missing)"
    candidate_summary_text = "\n".join(candidate_summaries or []).strip()
    return "\n\n".join(
        [
            f"Project slug: {project_slug}",
            f"Chapter id: {chapter_id}",
            f"Task: repair the {task_name} packet by emitting missing explicit {record_label} records.",
            _packet_contract_block(task_name=task_name, section_names=[index_section_name], record_templates=[(record_label, ["asset_id"], ["markdown"])]),
            "",
            "Existing index markdown from the prior packet:",
            existing_index_text,
            *( ["", "Candidate matches from the existing index markdown:", candidate_summary_text] if candidate_summary_text else [] ),
            "",
            "Requirements:",
            *requirements,
            "",
            "Chapter summary:",
            chapter_summary,
            "",
            "Chapter source markdown:",
            chapter_body,
        ]
    )


def _record_repair_candidate_summaries(
    *,
    project_slug: str,
    chapter_id: str,
    record_type: str,
    existing_index_markdown: str,
) -> list[str]:
    if not existing_index_markdown.strip():
        return []
    if record_type == "character":
        records = _extract_character_records_from_index_markdown(existing_index_markdown)
        finder = find_character_match_candidates
    elif record_type == "environment":
        records = _extract_environment_records_from_index_markdown(existing_index_markdown)
        finder = find_environment_match_candidates
    else:
        records = _extract_scene_records_from_index_markdown(existing_index_markdown)
        finder = None
    if not records:
        return []

    summaries: list[str] = []
    for record in records[:3]:
        try:
            asset_id = _normalize_asset_id(_require_record_field(record, "asset_id"), fallback_prefix=record_type)
            markdown = _require_record_section(record, "markdown")
        except LMStudioError:
            continue
        if finder is None:
            continue
        candidates = finder(
            project_slug=project_slug,
            asset_id=asset_id,
            markdown=markdown,
            top_n=2,
        )
        if not candidates:
            continue
        summaries.append(f"## {asset_id}")
        for candidate in candidates:
            snippet = candidate.context_snippets[0] if candidate.context_snippets else ""
            snippet_text = f" Example context: {snippet}" if snippet else ""
            summaries.append(
                f"- {candidate.canonical_id} (score {candidate.score}; chapters: {', '.join(candidate.source_chapters[:2]) or 'no source chapter'}; aliases: {', '.join(candidate.aliases[:4]) or '-'}){snippet_text}"
            )
    return summaries


def _chapter_summary_synthesis_prompt(*, project_slug: str, chapter_id: str, chunk_packets: list[_PacketDocument], degraded: bool = False) -> str:
    project_sections = [
        _require_packet_section(packet, "project_summary_markdown")
        for packet in chunk_packets
    ]
    chapter_sections = [
        _require_packet_section(packet, "chapter_summary_markdown")
        for packet in chunk_packets
    ]
    requirements = [
        "- merge the partial summaries into one coherent reusable project summary",
        "- merge the partial chapter summaries into one coherent chapter summary",
        "- do not mention that the summaries came from chunks",
        "- keep the result grounded and concise",
        "- treat the merged chapter summary as production evidence rather than a reader synopsis: preserve every distinct filmable event, entrance, exit, reveal, decision, object interaction, location/subzone shift, visual continuity state, and uncertainty that later scene, shot, descriptor, or prompt stages would need",
    ]
    if degraded:
        requirements = [
            "- keep the merged summaries concise",
            "- preserve named entities and major events",
        ]
    return "\n\n".join(
        [
            f"Project slug: {project_slug}",
            f"Chapter id: {chapter_id}",
            "Task: combine partial chapter summaries into one final project summary and chapter summary.",
            _packet_contract_block(task_name="chapter_summary", section_names=["project_summary_markdown", "chapter_summary_markdown"]),
            "",
            "Requirements:",
            *requirements,
            "",
            "Partial project summaries:",
            *[f"## Chunk {index + 1}\n{section}" for index, section in enumerate(project_sections)],
            "",
            "Partial chapter summaries:",
            *[f"## Chunk {index + 1}\n{section}" for index, section in enumerate(chapter_sections)],
        ]
    )


def _merge_summary_texts(*, title: str, texts: list[str]) -> str:
    parts: list[str] = []
    for text in texts:
        normalized = text.strip()
        if normalized and normalized not in parts:
            parts.append(normalized)
    if not parts:
        return f"# {title}\n"
    if len(parts) == 1:
        return parts[0]
    lines = [f"# {title}"]
    for index, part in enumerate(parts, start=1):
        lines.extend(["", f"## Chunk {index}", part])
    return "\n".join(lines).strip()


def _extract_usable_records_from_packet(
    *,
    packet: _PacketDocument,
    record_type: str,
    index_section_name: str,
) -> tuple[list[_PacketRecord], list[str], str]:
    warnings: list[str] = []
    try:
        records = _require_packet_records(packet, record_type=record_type)
    except LMStudioError:
        records = []
    try:
        index_markdown = _require_packet_section(packet, index_section_name)
    except LMStudioError:
        index_markdown = ""
    if records:
        return records, warnings, index_markdown
    if record_type == "character":
        records = _extract_character_records_from_index_markdown(index_markdown)
    elif record_type == "environment":
        records = _extract_environment_records_from_index_markdown(index_markdown)
    elif record_type == "scene":
        records = _extract_scene_records_from_index_markdown(index_markdown)
    else:
        records = []
    if records:
        warnings.append(
            f"Recovered {len(records)} usable {record_type} record(s) from {index_section_name} salvage output."
        )
    return records, warnings, index_markdown


def _split_text_into_fallback_chunks(text: str) -> list[str]:
    normalized_text = text.strip()
    if not normalized_text:
        return [normalized_text]
    lines = normalized_text.splitlines()
    if len(lines) < 8:
        midpoint = max(1, len(normalized_text) // 2)
        first = normalized_text[: midpoint + 1].strip()
        second = normalized_text[max(0, midpoint - 1) :].strip()
        chunks = [chunk for chunk in (first, second) if chunk]
        return chunks or [normalized_text]
    midpoint = max(1, len(lines) // 2)
    overlap = min(3, max(1, midpoint // 8))
    first = "\n".join(lines[: midpoint + overlap]).strip()
    second = "\n".join(lines[max(0, midpoint - overlap) :]).strip()
    chunks = [chunk for chunk in (first, second) if chunk]
    return chunks or [normalized_text]


def _merge_record_entries(base: _PacketRecord, incoming: _PacketRecord, *, record_type: str) -> _PacketRecord:
    fields = dict(base.fields)
    for key, value in incoming.fields.items():
        incoming_value = value.strip()
        if not incoming_value:
            continue
        existing_value = fields.get(key, "").strip()
        if not existing_value:
            fields[key] = incoming_value
            continue
        if key in {"aliases", "clarification_reason", "clarification_question", "manual_description_reason", "description", "role"}:
            fields[key] = _merge_text_values(existing_value, incoming_value)
            continue
        if key in {"manual_description_required", "clarification_required"}:
            fields[key] = "true" if _parse_packet_bool(existing_value) or _parse_packet_bool(incoming_value) else "false"
            continue
        if key in {"canonical_character_id"}:
            if len(incoming_value) > len(existing_value):
                fields[key] = incoming_value
            continue
        if len(incoming_value) > len(existing_value):
            fields[key] = incoming_value

    sections = dict(base.sections)
    base_markdown = sections.get("markdown", "").strip()
    incoming_markdown = incoming.sections.get("markdown", "").strip()
    if incoming_markdown and incoming_markdown not in base_markdown:
        sections["markdown"] = _merge_markdown_blocks(base_markdown, incoming_markdown, record_type=record_type)
    return _PacketRecord(fields=fields, sections=sections)


def _merge_text_values(existing: str, incoming: str) -> str:
    values: list[str] = []
    for value in (existing, incoming):
        normalized = value.strip()
        if normalized and normalized not in values:
            values.append(normalized)
    return "\n".join(values)


def _merge_markdown_blocks(existing: str, incoming: str, *, record_type: str) -> str:
    parts: list[str] = []
    for block in (existing.strip(), incoming.strip()):
        if block and block not in parts:
            parts.append(block)
    if not parts:
        return ""
    if len(parts) == 1:
        return parts[0]
    heading = "# Character Merge" if record_type == "character" else "# Environment Merge" if record_type == "environment" else "# Record Merge"
    return "\n\n".join([heading, *[f"## Chunk {index + 1}\n{part}" for index, part in enumerate(parts)]])


def _synthesize_record_index_markdown(*, chapter_id: str, record_type: str, records: list[_PacketRecord]) -> str:
    if record_type == "character":
        lines = [
            f"# Character Index - {chapter_id}",
            "",
            "## Visible Characters",
            "",
            "| Asset ID | Canonical Character ID | Aliases | Fully Identified | Manual Description Required | Clarification Required | Description |",
            "|---|---|---|---|---|---|---|",
        ]
        for record in records:
            fields = record.fields
            lines.append(
                "| {asset_id} | {canonical} | {aliases} | {identified} | {manual} | {clarify} | {description} |".format(
                    asset_id=_markdown_table_cell(fields.get("asset_id", "")),
                    canonical=_markdown_table_cell(fields.get("canonical_character_id", "")),
                    aliases=_markdown_table_cell(fields.get("aliases", "")),
                    identified=_markdown_table_cell(fields.get("is_fully_identified", "")),
                    manual=_markdown_table_cell(fields.get("manual_description_required", "")),
                    clarify=_markdown_table_cell(fields.get("clarification_required", "")),
                    description=_markdown_table_cell(fields.get("description", "")),
                )
            )
        return "\n".join(lines)
    lines = [
        f"# Environment Index - {chapter_id}",
        "",
        "## Visible Environments",
        "",
        "| Asset ID | Role | Geography | Lighting | Atmosphere | Scale | Anchors | Description |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for record in records:
        fields = record.fields
        lines.append(
            "| {asset_id} | {role} | {geography} | {lighting} | {atmosphere} | {scale} | {anchors} | {description} |".format(
                asset_id=_markdown_table_cell(fields.get("asset_id", "")),
                role=_markdown_table_cell(fields.get("role", "")),
                geography=_markdown_table_cell(fields.get("geography", "")),
                lighting=_markdown_table_cell(fields.get("lighting", "")),
                atmosphere=_markdown_table_cell(fields.get("atmosphere", "")),
                scale=_markdown_table_cell(fields.get("scale", "")),
                anchors=_markdown_table_cell(fields.get("anchors", "")),
                description=_markdown_table_cell(fields.get("description", "")),
            )
        )
    return "\n".join(lines)


def _markdown_table_cell(value: str) -> str:
    normalized = value.replace("|", r"\|").replace("\n", " ").strip()
    return normalized or "-"


def _structured_prompt_draft(record: _PacketRecord, *, asset_id: str, asset_type: str) -> _StructuredPromptDraft:
    parsed_inputs = _parse_markdown_key_value_items(_require_record_section(record, "inputs_markdown", allow_empty=True), asset_id=asset_id, asset_type=asset_type)
    return _StructuredPromptDraft(asset_id=_require_record_field(record, "asset_id"), purpose=_require_record_section(record, "purpose"), positive_prompt=_require_record_section(record, "positive_prompt"), negative_prompt=_require_record_section(record, "negative_prompt"), inputs=parsed_inputs.items, continuity_notes=_parse_markdown_list(_require_record_section(record, "continuity_notes_markdown")), repair_notes=_parse_markdown_list(_require_record_section(record, "repair_notes_markdown")), warnings=parsed_inputs.warnings)


def _build_prompt_package(*, path: Path, title: str, prompt_id: str, workflow_type: str, draft: _StructuredPromptDraft, sources: list[str]) -> PromptPackage:
    return PromptPackage(path=path, title=title, prompt_id=prompt_id, purpose=draft.purpose, workflow_type=workflow_type, positive_prompt=draft.positive_prompt, negative_prompt=draft.negative_prompt, inputs_markdown="\n".join(f"- {key}: {value}" for key, value in draft.inputs.items()), continuity_notes_markdown="\n".join(f"- {item}" for item in draft.continuity_notes), repair_notes_markdown="\n".join(f"- {item}" for item in draft.repair_notes), sources_markdown="\n".join(f"- {source}" for source in sources))


def _append_character_identity_section(*, markdown: str, aliases: str, canonical_character_id: str, is_fully_identified: str) -> str:
    suffix = "\n\n".join(["# Aliases", aliases or "None", "", "# Canonical Character ID", canonical_character_id or "", "", "# Fully Identified", is_fully_identified, ""])
    return markdown.rstrip() + "\n\n" + suffix


def _append_manual_description_section(*, markdown: str, manual_required: bool, manual_reason: str) -> str:
    suffix = "\n\n".join(["# Manual Description Input Required", "Yes" if manual_required else "No", "", "# Manual Description Reason", manual_reason or "None", ""])
    return markdown.rstrip() + "\n\n" + suffix


def _manual_character_description_placeholder(*, asset_id: str, reason: str) -> str:
    return "\n".join([MANUAL_PLACEHOLDER_MARKER, "", "# Asset ID", asset_id, "", "# Purpose", "Paste a stable manual visual description for this character so later shared reference generation can use it.", "", "# Why This Is Needed", reason, "", "# Guidance", "- describe face, hair, body type, age impression, silhouette, skin tone, costume logic, and any continuity-critical marks", "- prefer visible facts over backstory", "- if multiple looks exist, describe the default look for this chapter", "", "# Manual Description", ""])


def _character_clarification_placeholder(*, asset_id: str, reason: str, question: str, candidate_summaries: tuple[str, ...] = ()) -> str:
    lines = [
        CLARIFICATION_PLACEHOLDER_MARKER,
        "",
        "# Asset ID",
        asset_id,
        "",
        "# Why This Needs Clarification",
        reason,
        "",
        "# Question",
        question,
    ]
    if candidate_summaries:
        lines.extend([
            "",
            "# Candidate Matches",
            *candidate_summaries,
        ])
    lines.extend([
        "",
        "# Guidance",
        "- answer briefly and concretely",
        "- if another chapter already describes the character, note that source chapter",
        "- if the character is never described well, say whether FilmCreator should generate a reusable film-wide default description",
        "",
        "# Clarification Response",
        "",
    ])
    return "\n".join(lines)


def _environment_clarification_placeholder(*, asset_id: str, reason: str, question: str, candidate_summaries: tuple[str, ...] = ()) -> str:
    lines = [
        CLARIFICATION_PLACEHOLDER_MARKER,
        "",
        "# Asset ID",
        asset_id,
        "",
        "# Why This Needs Clarification",
        reason,
        "",
        "# Question",
        question,
    ]
    if candidate_summaries:
        lines.extend([
            "",
            "# Candidate Matches",
            *candidate_summaries,
        ])
    lines.extend([
        "",
        "# Guidance",
        "- answer briefly and concretely",
        "- if another chapter already describes the setting, note that source chapter",
        "- if the environment is broader than the current chapter's label, say whether FilmCreator should keep it as a reusable canonical setting or split it into narrower sub-locations",
        "",
        "# Clarification Response",
        "",
    ])
    return "\n".join(lines)


def _manual_description_path(*, project_dir: Path, asset_id: str) -> Path:
    return project_dir / "01_source" / "character_descriptions" / f"{asset_id}_manual_description.md"


def _character_clarification_path(*, project_dir: Path, asset_id: str) -> Path:
    return project_dir / "01_source" / "character_descriptions" / f"{asset_id}_clarification.md"


def _environment_clarification_path(*, project_dir: Path, asset_id: str) -> Path:
    return project_dir / "01_source" / "environment_descriptions" / f"{asset_id}_clarification.md"


def _reconcile_manual_character_description_placeholders(*, project_dir: Path, active_requests: dict[str, str]) -> list[Path]:
    manual_dir = project_dir / "01_source" / "character_descriptions"
    ensure_dir(manual_dir)
    written_paths: list[Path] = []
    for path in sorted(manual_dir.glob("*_manual_description.md")):
        asset_id = path.stem.removesuffix("_manual_description")
        if asset_id in active_requests:
            continue
        if _is_generated_manual_placeholder(path) and not _manual_description_has_user_content(path):
            try:
                remove_path_within_project(path, project_root=project_dir.resolve(), missing_ok=True)
            except PermissionError:
                continue
    for asset_id, reason in active_requests.items():
        path = _manual_description_path(project_dir=project_dir, asset_id=asset_id)
        if path.exists() and _manual_description_has_user_content(path):
            continue
        content = _manual_character_description_placeholder(asset_id=asset_id, reason=reason)
        if path.exists() and path.read_text(encoding="utf-8") == content:
            continue
        _write_text(path, content)
        written_paths.append(path)
    return written_paths


def _reconcile_character_clarification_placeholders(*, project_dir: Path, active_requests: dict[str, CharacterClarificationRequest]) -> list[Path]:
    clarification_dir = project_dir / "01_source" / "character_descriptions"
    ensure_dir(clarification_dir)
    written_paths: list[Path] = []
    for asset_id, request in active_requests.items():
        path = _character_clarification_path(project_dir=project_dir, asset_id=asset_id)
        if path.exists() and _clarification_has_user_content(path):
            continue
        content = _character_clarification_placeholder(
            asset_id=asset_id,
            reason=request.reason,
            question=request.question,
            candidate_summaries=request.candidate_summaries,
        )
        if path.exists() and path.read_text(encoding="utf-8") == content:
            continue
        _write_text(path, content)
        written_paths.append(path)
    return written_paths


def _reconcile_environment_clarification_placeholders(*, project_dir: Path, active_requests: dict[str, EnvironmentClarificationRequest]) -> list[Path]:
    clarification_dir = project_dir / "01_source" / "environment_descriptions"
    ensure_dir(clarification_dir)
    written_paths: list[Path] = []
    for asset_id, request in active_requests.items():
        path = _environment_clarification_path(project_dir=project_dir, asset_id=asset_id)
        if path.exists() and _clarification_has_user_content(path):
            continue
        content = _environment_clarification_placeholder(
            asset_id=asset_id,
            reason=request.reason,
            question=request.question,
            candidate_summaries=request.candidate_summaries,
        )
        if path.exists() and path.read_text(encoding="utf-8") == content:
            continue
        _write_text(path, content)
        written_paths.append(path)
    return written_paths


def _is_generated_manual_placeholder(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    return MANUAL_PLACEHOLDER_MARKER in text or ("Paste a stable manual visual description for this character" in text and "# Manual Description" in text)


def _manual_description_has_user_content(path: Path) -> bool:
    sections = _split_sections(path.read_text(encoding="utf-8"))
    return bool(sections.get("Manual Description", "").strip())


def _clarification_has_user_content(path: Path) -> bool:
    sections = _split_sections(path.read_text(encoding="utf-8"))
    return bool(sections.get("Clarification Response", "").strip())


def _write_authoring_exchange_log(*, project_dir: Path, task_name: str, system_prompt: str, user_prompt: str, response: str) -> Path:
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    log_path = project_dir / "02_story_analysis" / "logs" / f"{timestamp}_{task_name}.md"
    log_body = "\n".join(["# LM Studio Authoring Exchange", f"- timestamp_utc: {datetime.now(timezone.utc).isoformat()}", f"- task: {task_name}", "", "## System Prompt", "````text", system_prompt, "````", "", "## User Prompt", "````text", user_prompt, "````", "", "## Raw Response", "````text", response, "````", ""])
    _write_text(log_path, log_body)
    return log_path


def _write_authoring_failure_artifact(*, project_dir: Path, task_name: str, asset_id: str | None, reason: str) -> Path:
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    slug = asset_id or "task"
    path = project_dir / "02_story_analysis" / "logs" / "failures" / f"{timestamp}_{task_name}_{slug}.md"
    body = "\n".join(["# FilmCreator Authoring Failure", f"- timestamp_utc: {datetime.now(timezone.utc).isoformat()}", f"- task: {task_name}", f"- asset_id: {asset_id or ''}", "", "## Reason", reason, ""])
    _write_text(path, body)
    return path


def _parse_packet_document(response: str, *, expected_task: str | None = None) -> _PacketDocument:
    packet_body = _extract_packet_body(_strip_markdown_fences(response))
    packet = _parse_packet_body(packet_body)
    if expected_task is not None:
        actual_task = packet.metadata.get("task", "")
        if actual_task != expected_task:
            raise LMStudioError(f"LM Studio returned packet task '{actual_task or '(missing)'}' but expected '{expected_task}'.")
    version = packet.metadata.get("version", "")
    if version != PACKET_VERSION:
        raise LMStudioError(f"LM Studio returned packet version '{version or '(missing)'}' but expected '{PACKET_VERSION}'.")
    return packet


def _extract_packet_body(response: str) -> str:
    cleaned = _sanitize_llm_text(response)
    lines = cleaned.splitlines()
    start_index = next((index for index, line in enumerate(lines) if line.strip() == PACKET_START_TAG), -1)
    end_index = next((index for index in range(len(lines) - 1, -1, -1) if lines[index].strip() == PACKET_END_TAG), -1)
    if start_index == -1 or end_index == -1 or end_index <= start_index:
        start = cleaned.find(PACKET_START_TAG)
        end = cleaned.rfind(PACKET_END_TAG)
        if start == -1 or end == -1 or end <= start:
            if start_index != -1:
                body_lines = lines[start_index + 1 :]
                while body_lines and not body_lines[-1].strip():
                    body_lines.pop()
                while body_lines and body_lines[-1].strip() == PACKET_START_TAG:
                    body_lines.pop()
                if body_lines:
                    return "\n".join(body_lines).strip()
            raise LMStudioError("LM Studio did not return a FILMCREATOR packet envelope.")
        return cleaned[start + len(PACKET_START_TAG) : end].strip()
    return "\n".join(lines[start_index + 1 : end_index]).strip()


def _sanitize_llm_text(text: str) -> str:
    cleaned_chars: list[str] = []
    for ch in text:
        if ch in "\n\r\t":
            cleaned_chars.append(ch)
            continue
        if unicodedata.category(ch) == "Cf":
            continue
        cleaned_chars.append(ch)
    return "".join(cleaned_chars).strip()


def _strip_markdown_fences(response: str) -> str:
    cleaned = response.strip()
    if not cleaned.startswith("```"):
        return cleaned
    lines = cleaned.splitlines()
    if lines and lines[0].startswith("```"):
        lines = lines[1:]
    if lines and lines[-1].startswith("```"):
        lines = lines[:-1]
    return "\n".join(lines).strip()


def _parse_packet_body(packet_body: str) -> _PacketDocument:
    metadata: dict[str, str] = {}
    sections: dict[str, str] = {}
    records: list[_PacketRecord] = []
    lines = packet_body.splitlines()
    index = 0
    while index < len(lines):
        stripped = lines[index].strip()
        if not stripped:
            index += 1
            continue
        if stripped == SECTION_END_TAG:
            index += 1
            continue
        if stripped == RECORD_START_TAG:
            record_lines, index = _collect_tagged_block(lines, index, RECORD_START_TAG, RECORD_END_TAG, fallback_start_tag=RECORD_START_TAG)
            records.append(_parse_packet_record(record_lines))
            continue
        section_match = SECTION_TAG_PATTERN.fullmatch(stripped)
        if section_match:
            section_name = section_match.group(1).lower()
            section_lines, index = _collect_tagged_block(lines, index, stripped, SECTION_END_TAG, fallback_stop_any_tag=True)
            sections[section_name] = "\n".join(section_lines).strip()
            continue
        key, value = _split_packet_key_value(stripped)
        metadata[key] = value
        index += 1
    return _PacketDocument(metadata=metadata, sections=sections, records=records)


def _parse_packet_record(record_lines: list[str]) -> _PacketRecord:
    fields: dict[str, str] = {}
    sections: dict[str, str] = {}
    index = 0
    while index < len(record_lines):
        stripped = record_lines[index].strip()
        if not stripped:
            index += 1
            continue
        if stripped == SECTION_END_TAG:
            index += 1
            continue
        section_match = SECTION_TAG_PATTERN.fullmatch(stripped)
        if section_match:
            section_name = section_match.group(1).lower()
            section_body, index = _collect_tagged_block(record_lines, index, stripped, SECTION_END_TAG, fallback_stop_any_tag=True)
            sections[section_name] = "\n".join(section_body).strip()
            continue
        key, value = _split_packet_key_value(stripped)
        fields[key] = value
        index += 1
    record_type = fields.get("type", "")
    if not record_type:
        raise LMStudioError("Packet record is missing required field 'type'.")
    return _PacketRecord(fields=fields, sections=sections)


def _collect_tagged_block(lines: list[str], start_index: int, start_tag: str, end_tag: str, *, fallback_start_tag: str | None = None, fallback_stop_any_tag: bool = False) -> tuple[list[str], int]:
    if lines[start_index].strip() != start_tag:
        raise LMStudioError(f"Expected start tag '{start_tag}' but found '{lines[start_index].strip()}'.")
    body: list[str] = []
    index = start_index + 1
    while index < len(lines):
        stripped = lines[index].strip()
        if stripped == end_tag:
            return body, index + 1
        if fallback_start_tag is not None and stripped == fallback_start_tag:
            return body, index
        if fallback_stop_any_tag and _is_structural_packet_tag(stripped):
            return body, index
        body.append(lines[index])
        index += 1
    return body, index


def _is_structural_packet_tag(stripped: str) -> bool:
    return (
        stripped in {PACKET_START_TAG, PACKET_END_TAG, RECORD_START_TAG, RECORD_END_TAG, SECTION_END_TAG}
        or SECTION_TAG_PATTERN.fullmatch(stripped) is not None
    )


def _clean_section_text(value: str) -> str:
    cleaned = value.strip()
    inline_match = re.fullmatch(r"\[\[SECTION\s+(.*?)\s*\[\[/SECTION\]\]", cleaned, flags=re.DOTALL)
    if inline_match:
        return inline_match.group(1).strip()

    lines = cleaned.splitlines()
    while lines and lines[0].strip() == "[[SECTION":
        lines = lines[1:]
    while lines and lines[-1].strip() == SECTION_END_TAG:
        lines = lines[:-1]
    return "\n".join(lines).strip()


def _split_packet_key_value(line: str) -> tuple[str, str]:
    if ":" not in line:
        raise LMStudioError(f"Expected 'key: value' packet line but got '{line}'.")
    key, value = line.split(":", 1)
    normalized_key = key.strip().lower()
    if not normalized_key:
        raise LMStudioError(f"Invalid empty packet key in line '{line}'.")
    return normalized_key, value.strip()


def _require_packet_section(packet: _PacketDocument, section_name: str, *, allow_empty: bool = False) -> str:
    value = _clean_section_text(packet.sections.get(section_name.lower(), ""))
    if not value and not allow_empty:
        raise LMStudioError(f"Packet is missing required section '{section_name}'.")
    return value


def _require_packet_records(packet: _PacketDocument, *, record_type: str) -> list[_PacketRecord]:
    matching_records = [record for record in packet.records if record.fields.get("type") == record_type]
    if not matching_records:
        raise LMStudioError(f"Packet did not contain any '{record_type}' records.")
    return matching_records


def _require_single_packet_record(packet: _PacketDocument, *, record_type: str) -> _PacketRecord:
    records = _require_packet_records(packet, record_type=record_type)
    if len(records) != 1:
        raise LMStudioError(f"Packet was expected to contain exactly one '{record_type}' record but found {len(records)}.")
    return records[0]


def _require_record_field(record: _PacketRecord, field_name: str, *, allow_empty: bool = False) -> str:
    value = record.fields.get(field_name.lower(), "").strip()
    if not value and not allow_empty:
        raise LMStudioError(f"Packet record is missing required field '{field_name}'.")
    return value


def _require_record_section(record: _PacketRecord, section_name: str, *, allow_empty: bool = False) -> str:
    value = _clean_section_text(record.sections.get(section_name.lower(), ""))
    if not value and not allow_empty:
        raise LMStudioError(f"Packet record is missing required section '{section_name}'.")
    return value


def _validate_scene_decomposition(*, chapter_id: str, scene_records: list[_PacketRecord]) -> list[str]:
    warnings: list[str] = []
    if not scene_records:
        raise LMStudioError(f"Scene decomposition for {chapter_id} returned no usable scenes.")

    if len(scene_records) < PREFERRED_SCENE_COUNT:
        warnings.append(
            f"Scene decomposition for {chapter_id} returned only {len(scene_records)} scenes; preferred minimum is {PREFERRED_SCENE_COUNT}."
        )

    emotional_shifts: list[str] = []
    thin_scene_count = 0
    normalized_summaries: list[str] = []
    for record in scene_records:
        markdown = _require_record_section(record, "markdown")
        normalized = markdown.lower()
        summary = _scene_record_summary_line(markdown)
        normalized_summaries.append(re.sub(r"[^a-z0-9]+", " ", summary.lower()).strip())
        if len(normalized.strip()) < THIN_SCENE_MARKDOWN_THRESHOLD:
            thin_scene_count += 1
        if "aftermath" in normalized or "payoff" in normalized or "helplessness" in normalized or "reveal" in normalized:
            emotional_shifts.append("aftermath")
        if "battle" in normalized or "attack" in normalized or "destruction" in normalized or "boarding" in normalized:
            emotional_shifts.append("action")
        if "introduce" in normalized or "setup" in normalized or "return" in normalized or "arrival" in normalized:
            emotional_shifts.append("setup")

    if thin_scene_count:
        warnings.append(
            f"Scene decomposition for {chapter_id} has {thin_scene_count} thin scene markdown block(s) below the preferred detail threshold."
        )

    if len(scene_records) <= 2 and len({summary for summary in normalized_summaries if summary}) <= 1:
        warnings.append(
            f"Scene decomposition for {chapter_id} may be repetitive: the scene summaries are too similar across the small scene set."
        )

    if len(scene_records) <= 2 and not {"action", "aftermath", "setup"} & set(emotional_shifts):
        warnings.append(
            f"Scene decomposition for {chapter_id} has only {len(scene_records)} scenes and no strong transition markers; review the split for possible collapse."
        )

    if "action" in emotional_shifts and "aftermath" not in emotional_shifts:
        warnings.append("Scene decomposition may have collapsed aftermath/reveal material into action scenes; no aftermath-like scene language detected.")
    return warnings


def _extract_clip_beat_refs(markdown: str) -> set[str]:
    refs: set[str] = set()
    for match in re.finditer(r"BT\d{3}", markdown.upper()):
        refs.add(match.group(0))
    return refs


def _scene_allows_single_clip(scene_markdown: str) -> bool:
    normalized = scene_markdown.lower()
    return "single-shot" in normalized or "single shot" in normalized


def _validate_scene_duration_sanity(*, scene_id: str, beat_ids: list[str], clip_ids: list[str]) -> list[str]:
    warnings: list[str] = []
    estimated_duration_seconds = len(clip_ids) * 5
    if len(beat_ids) >= 4 and estimated_duration_seconds < 15:
        warnings.append(f"{scene_id} may be under-covered: {len(beat_ids)} beats mapped to only {len(clip_ids)} clips (~{estimated_duration_seconds}s).")
    if len(clip_ids) >= 10 and estimated_duration_seconds > 60:
        warnings.append(f"{scene_id} may be over-segmented: {len(clip_ids)} clips (~{estimated_duration_seconds}s).")
    return warnings


def _validate_clip_plan(*, scene_id: str, scene_markdown: str, beat_ids: list[str], clip_ids: list[str], clip_markdowns: dict[str, str], roster_markdown: str, strict_missing_beats: bool = False) -> list[str]:
    warnings: list[str] = []
    if len(clip_ids) < 2 and not _scene_allows_single_clip(scene_markdown):
        raise LMStudioError(f"Clip plan for {scene_id} produced only {len(clip_ids)} clip(s), but the scene is not marked as a valid single-shot scene.")
    covered_beats: set[str] = set()
    for markdown in clip_markdowns.values():
        covered_beats.update(_extract_clip_beat_refs(markdown))
    missing_beats = [beat_id for beat_id in beat_ids if beat_id not in covered_beats]
    if missing_beats:
        message = f"Clip plan for {scene_id} does not explicitly reference all beats. Missing beat refs: {', '.join(missing_beats)}"
        if strict_missing_beats:
            raise LMStudioError(message)
        warnings.append(message)
    roster_ids = re.findall(r"\bCL\d{3}\b", roster_markdown.upper())
    if roster_ids and len(set(roster_ids)) != len(clip_ids):
        warnings.append(f"Clip roster / clip file parity mismatch in {scene_id}: roster shows {len(set(roster_ids))} clip ids but {len(clip_ids)} clip files were created.")
    if len(beat_ids) >= 3 and len(clip_ids) == 1:
        raise LMStudioError(f"Clip plan for {scene_id} compressed {len(beat_ids)} beats into a single clip, which is not allowed.")
    warnings.extend(_validate_scene_duration_sanity(scene_id=scene_id, beat_ids=beat_ids, clip_ids=clip_ids))
    return warnings


def _parse_confidence(value: str) -> float:
    """Parse confidence value from string."""
    try:
        conf = float(value.strip())
        return max(0.0, min(1.0, conf))
    except (ValueError, TypeError):
        return 0.0


def _parse_list_field(value: str) -> list[str]:
    """Parse comma or semicolon separated list field."""
    if not value or not value.strip():
        return []
    import re
    items = re.split(r'[;,]', value)
    return [item.strip() for item in items if item.strip()]


def _parse_packet_bool(value: str) -> bool:
    normalized = value.strip().lower()
    if normalized in {"true", "yes", "1"}:
        return True
    if normalized in {"false", "no", "0"}:
        return False
    raise LMStudioError(f"Expected boolean packet field but got '{value}'.")


def _parse_markdown_key_value_items(markdown: str, *, asset_id: str, asset_type: str) -> _ParsedInputsMarkdown:
    values: dict[str, str] = {}
    warnings: list[str] = []
    current_key: str | None = None
    for line in markdown.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith(("- ", "* ")):
            stripped = stripped[2:].strip()
        if ":" in stripped:
            key, value = stripped.split(":", 1)
            normalized_key = key.strip()
            if normalized_key:
                values[normalized_key] = value.strip()
                current_key = normalized_key
                continue
            warnings.append(f"Ignored inputs_markdown line with empty key: {line.strip()}")
            continue
        if current_key is not None:
            values[current_key] = f"{values[current_key]}\n{stripped}" if values[current_key] else stripped
            continue
        if re.search(r"[\\/].+\.[a-z0-9]+$", stripped, re.IGNORECASE):
            generated_key = f"source_{len(values) + 1}"
            values[generated_key] = stripped
            current_key = generated_key
            continue
        if stripped:
            generated_key = f"note_{len(values) + 1}"
            values[generated_key] = stripped
            current_key = generated_key
            warnings.append(f"Salvaged freeform inputs_markdown line into {generated_key}: {line.strip()}")
    if not values:
        values = {"project_asset": f"{asset_type}:{asset_id}", "asset_id": asset_id}
        warnings.append("Synthesized minimal inputs_markdown because no usable lines were returned.")
    return _ParsedInputsMarkdown(items=values, warnings=warnings)


def _parse_markdown_list(markdown: str) -> list[str]:
    items: list[str] = []
    for line in markdown.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith(("- ", "* ")):
            stripped = stripped[2:].strip()
        items.append(stripped)
    if not items:
        raise LMStudioError("Expected at least one list item in Markdown list content.")
    return items


def _split_sections(text: str) -> dict[str, str]:
    matches = list(HEADING_PATTERN.finditer(text))
    if not matches:
        return {}
    sections: dict[str, str] = {}
    for index, match in enumerate(matches):
        heading = match.group(1).strip()
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        sections[heading] = text[start:end].strip()
    return sections


def _chapter_id_from_name(name: str) -> str:
    match = CHAPTER_ID_PATTERN.search(name)
    return match.group(1).upper() if match else ""


def _normalize_scene_id(value: str) -> str:
    normalized = value.strip().upper()
    if not SCENE_ID_PATTERN.fullmatch(normalized):
        raise LMStudioError(f"Invalid scene id returned by LM Studio: {value}")
    return validate_scene_id(normalized)


def _normalize_beat_id(value: str) -> str:
    normalized = value.strip().upper()
    if not re.fullmatch(r"BT\d{3}", normalized):
        raise LMStudioError(f"Invalid beat id returned by LM Studio: {value}")
    return normalized


def _is_hierarchical_clip_id(value: str) -> bool:
    normalized = value.strip().upper().replace("-", "_").replace(" ", "")
    return bool(re.fullmatch(r"CL(?:IP)?_?\d{1,3}_(\d{1,3}|[A-Z])", normalized))


def _normalize_clip_id(value: str, *, promoted_hierarchical_map: dict[str, str] | None = None, hierarchical_sequence_seen: int = 0) -> tuple[str, str | None]:
    original = value.strip()
    normalized = original.upper().replace("-", "_").replace(" ", "")
    direct_match = re.fullmatch(r"CL(?:IP)?_?(\d{1,3})", normalized)
    subclip_match = re.fullmatch(r"CL(?:IP)?_?(\d{1,3})_(\d{1,3}|[A-Z])", normalized)
    suffixed_match = re.fullmatch(r"CL(?:IP)?_?(\d{1,3})([A-Z])", normalized)
    plain_number_match = re.fullmatch(r"\d{1,3}", normalized)
    compound_number_match = re.fullmatch(r"(\d{1,3})_(\d{1,3})", normalized)
    warning = None
    if subclip_match:
        if promoted_hierarchical_map is None:
            promoted_hierarchical_map = {}
        if normalized not in promoted_hierarchical_map:
            promoted_hierarchical_map[normalized] = f"CL{hierarchical_sequence_seen + 1:03d}"
        coerced = promoted_hierarchical_map[normalized]
        warning = f"Promoted hierarchical clip id '{value}' to top-level canonical clip id '{coerced}'."
    elif plain_number_match:
        coerced = f"CL{int(normalized):03d}"
    elif direct_match:
        coerced = f"CL{int(direct_match.group(1)):03d}"
    elif suffixed_match:
        coerced = f"CL{int(suffixed_match.group(1)):03d}"
        warning = f"Normalized suffixed non-canonical clip id '{value}' to '{coerced}'."
    elif compound_number_match:
        coerced = f"CL{int(compound_number_match.group(1)):03d}"
        warning = f"Normalized compound non-canonical clip id '{value}' to '{coerced}'."
    else:
        raise LMStudioError(f"Invalid clip id returned by LM Studio: {value}")
    if warning is None and coerced != original.upper():
        warning = f"Normalized non-canonical clip id '{value}' to '{coerced}'."
    return validate_clip_id(coerced), warning


def _normalize_asset_id(value: str, *, fallback_prefix: str) -> str:
    normalized = re.sub(r"[^a-z0-9]+", "_", value.strip().lower()).strip("_")
    if not normalized:
        normalized = fallback_prefix
    if not ASSET_ID_PATTERN.fullmatch(normalized):
        raise LMStudioError(f"Invalid asset id returned by LM Studio: {value}")
    return normalized


def _markdown_bundle(*, directory: Path, exclude_names: set[str]) -> str:
    chunks: list[str] = []
    for path in sorted(directory.glob("*.md")):
        if path.name in exclude_names:
            continue
        chunks.append(f"## {path.name}\n{path.read_text(encoding='utf-8').strip()}")
    return "\n\n".join(chunks)


def _prune_markdown_dir(directory: Path, *, keep_names: set[str]) -> None:
    if not directory.exists():
        return
    project_root = find_project_root(directory)
    if project_root is None:
        raise ValueError(f"Refusing to prune markdown outside a project directory: {directory}")
    for path in directory.glob("*.md"):
        if path.name in keep_names:
            continue
        try:
            remove_path_within_project(path, project_root=project_root, missing_ok=True)
        except PermissionError:
            continue


def _write_text(path: Path, content: str) -> None:
    ensure_dir(path.parent)
    text = content.rstrip() + "\n"
    path.write_text(text, encoding="utf-8")


# Bind the pure parsing and validation helpers to the feature module so the
# orchestration code uses the extracted implementation while keeping this file
# backward compatible during the refactor.
_parse_packet_document = authoring_packets.parse_packet_document
_extract_packet_body = authoring_packets.extract_packet_body
_sanitize_llm_text = authoring_packets.sanitize_llm_text
_strip_markdown_fences = authoring_packets.strip_markdown_fences
_parse_packet_body = authoring_packets.parse_packet_body
_parse_packet_record = authoring_packets.parse_packet_record
_collect_tagged_block = authoring_packets.collect_tagged_block
_split_packet_key_value = authoring_packets.split_packet_key_value
_require_packet_section = authoring_packets.require_packet_section
_require_packet_records = authoring_packets.require_packet_records
_require_single_packet_record = authoring_packets.require_single_packet_record
_require_record_field = authoring_packets.require_record_field
_require_record_section = authoring_packets.require_record_section
_extract_character_records_from_index_markdown = authoring_packets.extract_character_records_from_index_markdown
_extract_environment_records_from_index_markdown = authoring_packets.extract_environment_records_from_index_markdown
_extract_scene_records_from_index_markdown = authoring_packets.extract_scene_records_from_index_markdown
_validate_scene_decomposition = authoring_packets.validate_scene_decomposition
_extract_clip_beat_refs = authoring_packets.extract_clip_beat_refs
_scene_allows_single_clip = authoring_packets.scene_allows_single_clip
_validate_clip_plan = authoring_packets.validate_clip_plan
_parse_packet_bool = authoring_packets.parse_packet_bool
_parse_markdown_key_value_items = authoring_packets.parse_markdown_key_value_items
_parse_markdown_list = authoring_packets.parse_markdown_list
_split_sections = authoring_packets.split_sections
_chapter_id_from_name = authoring_packets.chapter_id_from_name
_normalize_scene_id = authoring_packets.normalize_scene_id
_normalize_beat_id = authoring_packets.normalize_beat_id
_is_hierarchical_clip_id = authoring_packets.is_hierarchical_clip_id
_normalize_clip_id = authoring_packets.normalize_clip_id
_normalize_asset_id = authoring_packets.normalize_asset_id
_scene_record_summary_line = authoring_packets.scene_record_summary_line
_markdown_bundle = authoring_packets.markdown_bundle
_prune_markdown_dir = authoring_packets.prune_markdown_dir
_write_text = authoring_packets.write_text
