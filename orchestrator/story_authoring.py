from __future__ import annotations

import json
import re
import time
import unicodedata
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

from .authoring import PromptWriteSummary, write_prompts
from .common import ensure_dir, repo_relative, validate_clip_id, validate_scene_id
from .lmstudio_client import LMStudioClient, LMStudioError
from .prompt_package import PromptPackage, write_prompt_package
from .scaffold import create_clip, create_project, create_scene
from .settings import load_runtime_settings
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

    def to_dict(self) -> dict[str, str]:
        return {
            "asset_id": self.asset_id,
            "source_path": self.source_path,
            "reason": self.reason,
            "question": self.question,
        }


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


@dataclass(frozen=True)
class _TaskFailure:
    task_name: str
    message: str
    attempts: list[_TaskAttempt]
    failure_artifact_path: str


def analyze_chapter(*, project_slug: str, chapter: str | None = None) -> StoryAnalysisSummary:
    started = time.perf_counter()
    print(f"[authoring] Starting chapter analysis for {project_slug}...")
    client, resolved_model = _client_and_model()
    project_dir = create_project(project_slug)
    chapter_source = _resolve_chapter_source(project_slug, chapter)
    _prune_markdown_dir(
        project_dir / "02_story_analysis" / "character_breakdowns",
        keep_names={"README.md", "CHARACTER_INDEX.md"},
    )
    _prune_markdown_dir(
        project_dir / "02_story_analysis" / "environment_breakdowns",
        keep_names={"README.md", "ENVIRONMENT_INDEX.md"},
    )
    _prune_markdown_dir(
        project_dir / "02_story_analysis" / "scene_breakdowns",
        keep_names={"README.md", "SCENE_INDEX.md"},
    )

    written_files: list[str] = []
    manual_requests: list[ManualCharacterDescriptionRequest] = []
    clarification_requests: list[CharacterClarificationRequest] = []
    warnings: list[str] = []

    summary_packet = _call_packet_task(
        client=client,
        project_dir=project_dir,
        task_name="chapter_summary",
        system_prompt=_analysis_system_prompt(),
        user_prompt=_chapter_summary_user_prompt(project_slug, chapter_source),
        degraded_user_prompt=_chapter_summary_user_prompt(project_slug, chapter_source, degraded=True),
    )
    project_summary_markdown = _require_packet_section(summary_packet, "project_summary_markdown")
    chapter_summary_markdown = _require_packet_section(summary_packet, "chapter_summary_markdown")

    project_summary_path = project_dir / "02_story_analysis" / "story_summary" / "project_summary.md"
    chapter_summary_path = (
        project_dir / "02_story_analysis" / "chapter_analysis" / f"{chapter_source.chapter_id}_summary.md"
    )
    _write_text(project_summary_path, project_summary_markdown)
    _write_text(chapter_summary_path, chapter_summary_markdown)
    written_files.extend([repo_relative(project_summary_path), repo_relative(chapter_summary_path)])

    character_packet = _call_packet_task(
        client=client,
        project_dir=project_dir,
        task_name="character_extraction",
        system_prompt=_analysis_system_prompt(),
        user_prompt=_character_extraction_user_prompt(
            project_slug=project_slug,
            chapter_source=chapter_source,
            chapter_summary=chapter_summary_markdown,
        ),
        degraded_user_prompt=_character_extraction_user_prompt(
            project_slug=project_slug,
            chapter_source=chapter_source,
            chapter_summary=chapter_summary_markdown,
            degraded=True,
        ),
    )
    character_index_markdown = _require_packet_section(character_packet, "character_index_markdown")
    character_index_path = project_dir / "02_story_analysis" / "character_breakdowns" / "CHARACTER_INDEX.md"
    _write_text(character_index_path, character_index_markdown)
    written_files.append(repo_relative(character_index_path))

    canonical_lookup = _existing_character_lookup(project_dir=project_dir)
    active_manual_description_requests: dict[str, str] = {}
    active_clarification_requests: dict[str, tuple[str, str]] = {}
    usable_character_count = 0

    for index, raw_character in enumerate(_require_packet_records(character_packet, record_type="character"), start=1):
        try:
            asset_id = _normalize_asset_id(
                _require_record_field(raw_character, "asset_id"),
                fallback_prefix="character",
            )
            markdown = _require_record_section(raw_character, "markdown")
            manual_description_required = _parse_packet_bool(
                _require_record_field(raw_character, "manual_description_required")
            )
            manual_description_reason = _require_record_field(
                raw_character,
                "manual_description_reason",
                allow_empty=not manual_description_required,
            )
            clarification_required = _parse_packet_bool(
                _require_record_field(raw_character, "clarification_required", allow_empty=True) or "false"
            )
            clarification_reason = _require_record_field(raw_character, "clarification_reason", allow_empty=True)
            clarification_question = _require_record_field(raw_character, "clarification_question", allow_empty=True)
            if clarification_required:
                if not clarification_reason:
                    clarification_reason = "The character record indicates clarification is needed, but LM Studio did not supply a reason."
                    warnings.append(f"Synthesized clarification_reason for character '{asset_id}'.")
                if not clarification_question:
                    clarification_question = (
                        "This character appears to need clarification. Can you identify the missing canonical identity or provide the missing visual facts?"
                    )
                    warnings.append(f"Synthesized clarification_question for character '{asset_id}'.")
            aliases = _require_record_field(raw_character, "aliases", allow_empty=True)
            canonical_character_id = _require_record_field(raw_character, "canonical_character_id", allow_empty=True)
            is_fully_identified = _require_record_field(raw_character, "is_fully_identified", allow_empty=True) or "false"
        except LMStudioError as exc:
            warnings.append(
                f"Skipped malformed character record #{index}: {exc}. "
                f"Fields present: {sorted(raw_character.fields.keys())}. "
                f"Sections present: {sorted(raw_character.sections.keys())}."
            )
            continue

        resolved_asset_id, inferred_clarification = _resolve_character_identity(
            asset_id=asset_id,
            canonical_character_id=canonical_character_id,
            aliases=aliases,
            markdown=markdown,
            canonical_lookup=canonical_lookup,
        )
        filename = f"{resolved_asset_id}.md"

        if inferred_clarification is not None and not clarification_required:
            clarification_required = True
            clarification_reason = inferred_clarification[0]
            clarification_question = inferred_clarification[1]
            warnings.append(f"Auto-generated clarification request for character '{resolved_asset_id}'.")

        if clarification_required:
            manual_description_required = False
            manual_description_reason = ""

        character_markdown = _append_manual_description_section(
            markdown=_append_character_identity_section(
                markdown=markdown,
                aliases=aliases,
                canonical_character_id=resolved_asset_id,
                is_fully_identified=is_fully_identified,
            ),
            manual_required=manual_description_required,
            manual_reason=manual_description_reason,
        )
        character_path = project_dir / "02_story_analysis" / "character_breakdowns" / filename
        _write_text(character_path, character_markdown)
        written_files.append(repo_relative(character_path))

        if manual_description_required:
            manual_path = _manual_description_path(project_dir=project_dir, asset_id=resolved_asset_id)
            active_manual_description_requests[resolved_asset_id] = manual_description_reason
            manual_requests.append(
                ManualCharacterDescriptionRequest(
                    asset_id=resolved_asset_id,
                    source_path=repo_relative(manual_path),
                    reason=manual_description_reason,
                )
            )

        if clarification_required:
            clarification_path = _character_clarification_path(project_dir=project_dir, asset_id=resolved_asset_id)
            active_clarification_requests[resolved_asset_id] = (clarification_reason, clarification_question)
            clarification_requests.append(
                CharacterClarificationRequest(
                    asset_id=resolved_asset_id,
                    source_path=repo_relative(clarification_path),
                    reason=clarification_reason,
                    question=clarification_question,
                )
            )
        usable_character_count += 1

    if usable_character_count == 0:
        raise LMStudioError("Character extraction returned no usable character records after validation.")

    manual_placeholder_paths = _reconcile_manual_character_description_placeholders(
        project_dir=project_dir,
        active_requests=active_manual_description_requests,
    )
    clarification_placeholder_paths = _reconcile_character_clarification_placeholders(
        project_dir=project_dir,
        active_requests=active_clarification_requests,
    )
    written_files.extend(repo_relative(path) for path in manual_placeholder_paths)
    written_files.extend(repo_relative(path) for path in clarification_placeholder_paths)

    environment_packet = _call_packet_task(
        client=client,
        project_dir=project_dir,
        task_name="environment_extraction",
        system_prompt=_analysis_system_prompt(),
        user_prompt=_environment_extraction_user_prompt(
            project_slug=project_slug,
            chapter_source=chapter_source,
            chapter_summary=chapter_summary_markdown,
        ),
        degraded_user_prompt=_environment_extraction_user_prompt(
            project_slug=project_slug,
            chapter_source=chapter_source,
            chapter_summary=chapter_summary_markdown,
            degraded=True,
        ),
    )
    environment_index_markdown = _require_packet_section(environment_packet, "environment_index_markdown")
    environment_index_path = project_dir / "02_story_analysis" / "environment_breakdowns" / "ENVIRONMENT_INDEX.md"
    _write_text(environment_index_path, environment_index_markdown)
    written_files.append(repo_relative(environment_index_path))

    for raw_environment in _require_packet_records(environment_packet, record_type="environment"):
        asset_id = _normalize_asset_id(
            _require_record_field(raw_environment, "asset_id"),
            fallback_prefix="environment",
        )
        filename = f"{asset_id}.md"
        markdown = _require_record_section(raw_environment, "markdown")
        environment_path = project_dir / "02_story_analysis" / "environment_breakdowns" / filename
        _write_text(environment_path, markdown)
        written_files.append(repo_relative(environment_path))

    scene_packet = _call_packet_task(
        client=client,
        project_dir=project_dir,
        task_name="scene_decomposition",
        system_prompt=_analysis_system_prompt(),
        user_prompt=_scene_decomposition_user_prompt(
            project_slug=project_slug,
            chapter_id=chapter_source.chapter_id,
            chapter_summary=chapter_summary_markdown,
        ),
        degraded_user_prompt=_scene_decomposition_user_prompt(
            project_slug=project_slug,
            chapter_id=chapter_source.chapter_id,
            chapter_summary=chapter_summary_markdown,
            degraded=True,
        ),
    )
    scene_index_markdown = _require_packet_section(scene_packet, "scene_index_markdown")
    scene_index_path = project_dir / "02_story_analysis" / "scene_breakdowns" / "SCENE_INDEX.md"
    _write_text(scene_index_path, scene_index_markdown)
    written_files.append(repo_relative(scene_index_path))

    scene_records = _require_packet_records(scene_packet, record_type="scene")
    scene_validation_warnings = _validate_scene_decomposition(
        chapter_id=chapter_source.chapter_id,
        scene_records=scene_records,
    )
    warnings.extend(scene_validation_warnings)

    scene_ids: list[str] = []
    duplicate_scene_ids: list[str] = []
    for raw_scene in scene_records:
        raw_scene_id = _normalize_scene_id(_require_record_field(raw_scene, "scene_id"))
        scene_id = validate_scene_id(f"{chapter_source.chapter_id}_{raw_scene_id}")
        filename = f"{scene_id}.md"
        markdown = _require_record_section(raw_scene, "markdown")
        create_scene(project_slug, scene_id)
        scene_path = project_dir / "02_story_analysis" / "scene_breakdowns" / filename
        _write_text(scene_path, markdown)
        written_files.append(repo_relative(scene_path))
        if scene_id in scene_ids:
            duplicate_scene_ids.append(scene_id)
        scene_ids.append(scene_id)

    if duplicate_scene_ids:
        for duplicate_scene_id in _ordered_unique(duplicate_scene_ids):
            warnings.append(
                f"Duplicate scene_id detected after normalization: {duplicate_scene_id}. "
                "Keeping first occurrence and skipping later duplicate in chapter summary output."
            )
        scene_ids = _ordered_unique(scene_ids)

    character_breakdown_dir = project_dir / "02_story_analysis" / "character_breakdowns"
    character_breakdowns = sorted(
        path
        for path in character_breakdown_dir.glob("*.md")
        if path.name not in {"CHARACTER_INDEX.md", "README.md"}
    )
    environment_breakdown_dir = project_dir / "02_story_analysis" / "environment_breakdowns"
    environment_breakdowns = sorted(
        path
        for path in environment_breakdown_dir.glob("*.md")
        if path.name not in {"ENVIRONMENT_INDEX.md", "README.md"}
    )
    character_registry = resolve_character_registry(project_slug, character_breakdowns)
    environment_registry = resolve_environment_registry(project_slug, environment_breakdowns)
    canonical_character_ids, provisional_character_ids = summarize_registry_status(character_registry)
    canonical_environment_ids, provisional_environment_ids = summarize_registry_status(environment_registry)
    world_registry_paths = [
        repo_relative(character_registry_path(project_slug)),
        repo_relative(environment_registry_path(project_slug)),
    ]
    written_files.extend(world_registry_paths)

    key_artifacts: list[str] = [
        repo_relative(project_summary_path),
        repo_relative(chapter_summary_path),
        repo_relative(character_index_path),
        repo_relative(environment_index_path),
        repo_relative(scene_index_path),
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
    scene_path = project_dir / "02_story_analysis" / "scene_breakdowns" / f"{scene_id}.md"
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
        system_prompt=_analysis_system_prompt(),
        user_prompt=_scene_beats_user_prompt(
            project_slug=project_slug,
            scene_id=scene_id,
            scene_markdown=_scene_brief_markdown(scene_path),
        ),
        degraded_user_prompt=_scene_beats_user_prompt(
            project_slug=project_slug,
            scene_id=scene_id,
            scene_markdown=_scene_brief_markdown(scene_path),
            degraded=True,
        ),
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
        filename = f"{beat_id}.md"
        markdown = _require_record_section(raw_beat, "markdown")
        beat_path = beat_dir / filename
        _write_text(beat_path, markdown)
        written_files.append(repo_relative(beat_path))
        beat_ids.append(beat_id)

    clip_dir = project_dir / "02_story_analysis" / "clip_plans" / scene_id
    ensure_dir(clip_dir)
    _prune_markdown_dir(clip_dir, keep_names=set())
    scene_markdown_for_validation = _scene_brief_markdown(scene_path)

    clip_attempt_specs = [
        {
            "label": "normal",
            "scene_markdown": scene_markdown_for_validation,
            "degraded": False,
        },
        {
            "label": "repair_retry",
            "scene_markdown": scene_markdown_for_validation
            + "\n\n# Repair Instruction\n"
            + "Rebuild this clip roster so every beat is covered and every shot has a unique top-level CL### id. "
            + "Do not compress multiple beats into one clip unless the scene is explicitly single-shot.",
            "degraded": True,
        },
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
            system_prompt=_analysis_system_prompt(),
            user_prompt=_clip_planning_user_prompt(
                project_slug=project_slug,
                scene_id=scene_id,
                scene_markdown=attempt["scene_markdown"],
                beat_index_path=beat_index_path,
                degraded=attempt["degraded"],
            ),
            degraded_user_prompt=_clip_planning_user_prompt(
                project_slug=project_slug,
                scene_id=scene_id,
                scene_markdown=attempt["scene_markdown"],
                beat_index_path=beat_index_path,
                degraded=True,
            ),
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
                clip_id, clip_warning = _normalize_clip_id(
                    raw_clip_id,
                    promoted_hierarchical_map=promoted_hierarchical_map,
                    hierarchical_sequence_seen=hierarchical_sequence_seen,
                )
                if _is_hierarchical_clip_id(raw_clip_id):
                    hierarchical_sequence_seen += 1
            except LMStudioError as exc:
                attempt_warnings.append(f"Skipped clip record with unusable clip_id '{raw_clip_id}': {exc}")
                continue

            if clip_warning:
                attempt_warnings.append(clip_warning)

            if clip_id in seen_clip_ids:
                attempt_warnings.append(
                    f"Skipped duplicate clip record after normalization: '{raw_clip_id}' resolved to '{clip_id}', which already exists."
                )
                continue

            filename = f"{clip_id}.md"
            markdown = _require_record_section(raw_clip, "markdown")
            create_clip(project_slug, scene_id, clip_id)
            clip_path = clip_dir / filename
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
            validation_warnings = _validate_clip_plan(
                scene_id=scene_id,
                scene_markdown=scene_markdown_for_validation,
                beat_ids=beat_ids,
                clip_ids=clip_ids,
                clip_markdowns=clip_markdowns,
                roster_markdown=clip_roster_markdown,
                strict_missing_beats=attempt["degraded"],
            )
            attempt_warnings.extend(validation_warnings)
            missing_beat_warning = next(
                (warning for warning in validation_warnings if "does not explicitly reference all beats" in warning),
                None,
            )
            if missing_beat_warning and not attempt["degraded"]:
                last_validation_error = missing_beat_warning
                attempt_warnings.append(
                    f"Clip plan for {scene_id} will be retried because beat coverage is incomplete on the first pass."
                )
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
        raise LMStudioError(
            last_validation_error or f"Clip planning for {scene_id} failed validation after retries."
        )

    written_files.extend(accepted_written_files)
    warnings.extend(accepted_clip_warnings)
    clip_ids = accepted_clip_ids

    scene_artifacts: list[str] = [
        repo_relative(scene_path),
        repo_relative(beat_index_path),
        repo_relative(clip_dir / f"{scene_id}_clip_roster.md"),
    ]
    _print_saved_artifacts(f"[authoring] Saved scene planning artifacts for {scene_id}:", scene_artifacts)
    print(f"[authoring] Planned {len(clip_ids)} clips for {scene_id}: {', '.join(clip_ids)}")

    elapsed = time.perf_counter() - started
    print(f"[authoring] Finished scene planning for {scene_id} in {elapsed:.1f}s")
    return ScenePlanningSummary(
        project_slug=project_slug,
        scene_id=scene_id,
        model=resolved_model,
        written_files=written_files,
        beat_ids=beat_ids,
        clip_ids=clip_ids,
        warnings=warnings,
    )


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
        print(
            f"[authoring] Finished scene cascade {scene_id} in {scene_elapsed:.1f}s "
            f"({succeeded} prompt targets succeeded, {failed} failed)"
        )
    shared_prompts = write_shared_prompts(project_slug=project_slug)
    elapsed = time.perf_counter() - started
    print(f"[authoring] Finished chapter authoring cascade in {elapsed:.1f}s")
    return ChapterAuthoringSummary(
        analysis=analysis,
        scene_runs=scene_runs,
        shared_prompts=shared_prompts,
    )


def write_shared_prompts(*, project_slug: str) -> SharedPromptSummary:
    started = time.perf_counter()
    print(f"[authoring] Starting shared prompt writing for {project_slug}...")
    client, resolved_model = _client_and_model()
    project_dir = create_project(project_slug)
    character_index_path = project_dir / "02_story_analysis" / "character_breakdowns" / "CHARACTER_INDEX.md"
    environment_index_path = project_dir / "02_story_analysis" / "environment_breakdowns" / "ENVIRONMENT_INDEX.md"
    written_files: list[str] = []
    warnings: list[str] = []
    failures: list[SharedPromptFailure] = []
    character_breakdown_dir = project_dir / "02_story_analysis" / "character_breakdowns"
    character_breakdowns = sorted(
        path
        for path in character_breakdown_dir.glob("*.md")
        if path.name not in {"CHARACTER_INDEX.md", "README.md"}
    )
    for character_breakdown_path in character_breakdowns:
        asset_id = _normalize_asset_id(character_breakdown_path.stem, fallback_prefix="character")
        manual_description_path = _manual_description_path(project_dir=project_dir, asset_id=asset_id)
        try:
            character_packet = _call_packet_task(
                client=client,
                project_dir=project_dir,
                task_name="character_shared_prompts",
                system_prompt=_analysis_system_prompt(),
                user_prompt=_character_shared_prompt_user_prompt(
                    project_slug=project_slug,
                    asset_id=asset_id,
                    character_breakdown_path=character_breakdown_path,
                    manual_description_path=manual_description_path,
                ),
                degraded_user_prompt=_character_shared_prompt_user_prompt(
                    project_slug=project_slug,
                    asset_id=asset_id,
                    character_breakdown_path=character_breakdown_path,
                    manual_description_path=manual_description_path,
                    degraded=True,
                ),
            )
            raw_prompt = _require_single_packet_record(character_packet, record_type="character_prompt")
            record_asset_id = _normalize_asset_id(
                _require_record_field(raw_prompt, "asset_id"),
                fallback_prefix="character",
            )
            if record_asset_id != asset_id:
                raise LMStudioError(
                    f"LM Studio returned character prompt for '{record_asset_id}' when '{asset_id}' was requested."
                )
            draft = _structured_prompt_draft(raw_prompt, asset_id=asset_id, asset_type="character")
            warnings.extend(f"{asset_id}: {warning}" for warning in draft.warnings)
            prompt_path = (
                project_dir / "03_prompt_packages" / "characters" / asset_id / f"{asset_id}_ref_prompt.md"
            )
            sources = [repo_relative(character_index_path), repo_relative(character_breakdown_path)]
            if manual_description_path.exists():
                sources.append(repo_relative(manual_description_path))
            write_prompt_package(
                prompt_path,
                _build_prompt_package(
                    path=prompt_path,
                    title=f"{asset_id} Character Reference Prompt",
                    prompt_id=f"{asset_id}_ref_prompt",
                    workflow_type="still.t2i.klein.distilled",
                    draft=draft,
                    sources=sources,
                ),
            )
            written_files.append(repo_relative(prompt_path))
        except LMStudioError as exc:
            failure_path = _write_authoring_failure_artifact(
                project_dir=project_dir,
                task_name="character_shared_prompts",
                asset_id=asset_id,
                reason=str(exc),
            )
            failures.append(
                SharedPromptFailure(
                    asset_id=asset_id,
                    asset_type="character",
                    reason=str(exc),
                    failure_artifact_path=repo_relative(failure_path),
                )
            )

    environment_breakdown_dir = project_dir / "02_story_analysis" / "environment_breakdowns"
    environment_breakdowns = sorted(
        path
        for path in environment_breakdown_dir.glob("*.md")
        if path.name not in {"ENVIRONMENT_INDEX.md", "README.md"}
    )
    for environment_breakdown_path in environment_breakdowns:
        asset_id = _normalize_asset_id(environment_breakdown_path.stem, fallback_prefix="environment")
        try:
            environment_packet = _call_packet_task(
                client=client,
                project_dir=project_dir,
                task_name="environment_shared_prompts",
                system_prompt=_analysis_system_prompt(),
                user_prompt=_environment_shared_prompt_user_prompt(
                    project_slug=project_slug,
                    asset_id=asset_id,
                    environment_breakdown_path=environment_breakdown_path,
                ),
                degraded_user_prompt=_environment_shared_prompt_user_prompt(
                    project_slug=project_slug,
                    asset_id=asset_id,
                    environment_breakdown_path=environment_breakdown_path,
                    degraded=True,
                ),
            )
            raw_prompt = _require_single_packet_record(environment_packet, record_type="environment_prompt")
            record_asset_id = _normalize_asset_id(
                _require_record_field(raw_prompt, "asset_id"),
                fallback_prefix="environment",
            )
            if record_asset_id != asset_id:
                raise LMStudioError(
                    f"LM Studio returned environment prompt for '{record_asset_id}' when '{asset_id}' was requested."
                )
            draft = _structured_prompt_draft(raw_prompt, asset_id=asset_id, asset_type="environment")
            warnings.extend(f"{asset_id}: {warning}" for warning in draft.warnings)
            prompt_path = (
                project_dir / "03_prompt_packages" / "environments" / asset_id / f"{asset_id}_ref_prompt.md"
            )
            sources = [repo_relative(environment_index_path), repo_relative(environment_breakdown_path)]
            write_prompt_package(
                prompt_path,
                _build_prompt_package(
                    path=prompt_path,
                    title=f"{asset_id} Environment Reference Prompt",
                    prompt_id=f"{asset_id}_ref_prompt",
                    workflow_type="still.t2i.klein.distilled",
                    draft=draft,
                    sources=sources,
                ),
            )
            written_files.append(repo_relative(prompt_path))
        except LMStudioError as exc:
            failure_path = _write_authoring_failure_artifact(
                project_dir=project_dir,
                task_name="environment_shared_prompts",
                asset_id=asset_id,
                reason=str(exc),
            )
            failures.append(
                SharedPromptFailure(
                    asset_id=asset_id,
                    asset_type="environment",
                    reason=str(exc),
                    failure_artifact_path=repo_relative(failure_path),
                )
            )

    elapsed = time.perf_counter() - started
    print(f"[authoring] Finished shared prompt writing in {elapsed:.1f}s")
    return SharedPromptSummary(
        project_slug=project_slug,
        model=resolved_model,
        written_files=written_files,
        warnings=warnings,
        failures=failures,
    )


def build_chapter_continuity(
    *,
    project_slug: str,
    analysis: StoryAnalysisSummary,
    snapshot_data: dict | None = None,
) -> ChapterContinuitySummary:
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

    summary_markdown = "\n".join(
        [
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
        ]
    )
    _write_text(summary_path, summary_markdown)
    _print_saved_artifacts(
        f"[authoring] Saved chapter continuity artifacts for {analysis.chapter_id}:",
        [repo_relative(state_path), repo_relative(summary_path)],
    )
    return ChapterContinuitySummary(
        chapter_id=analysis.chapter_id,
        state_path=repo_relative(state_path),
        summary_path=repo_relative(summary_path),
        known_characters=known_characters,
        known_environments=known_environments,
        unresolved_character_ids=unresolved_character_ids,
        scene_order=scene_order,
    )


def authoring_checkpoint(
    *,
    project_slug: str,
    chapter: str | None = None,
    scene_id: str | None = None,
) -> AuthoringCheckpointSummary:
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
    return AuthoringCheckpointSummary(
        analysis=analysis,
        planning=planning,
        shared_prompts=shared_prompts,
        clip_prompts=clip_prompts,
    )


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
    return _ChapterSource(
        path=chapter_path,
        chapter_id=chapter_id,
        title=title,
        full_markdown=full_markdown,
        text=text,
    )


def _existing_character_lookup(*, project_dir: Path) -> dict[str, str]:
    lookup: dict[str, str] = {}
    character_dir = project_dir / "02_story_analysis" / "character_breakdowns"
    if not character_dir.exists():
        return lookup
    for path in sorted(character_dir.glob("*.md")):
        if path.name in {"CHARACTER_INDEX.md", "README.md"}:
            continue
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


def _resolve_character_identity(
    *,
    asset_id: str,
    canonical_character_id: str,
    aliases: str,
    markdown: str,
    canonical_lookup: dict[str, str],
) -> tuple[str, tuple[str, str] | None]:
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

    generic_labels = {"narrator", "captain", "captive", "guard", "woman", "man", "girl", "boy", "hound"}
    if any(label in asset_id for label in generic_labels):
        question = (
            "This character is named or role-labeled but not fully identified. Can you find a stronger canonical identity from another chapter, "
            "or should FilmCreator keep this as a scene-local provisional character?"
        )
        return asset_id, (
            "The extracted character id appears generic or role-based rather than clearly canonical.",
            question,
        )

    sections = _split_sections(markdown)
    description_blob = "\n".join(sections.values()).lower()
    if "no physical description" in description_blob or "uncertain" in description_blob:
        question = (
            "This character is named but lacks a stable visual description. Can you find a description from another source chapter, "
            "or should FilmCreator generate a reusable film-wide description?"
        )
        return asset_id, (
            "The character is not fully identified from this chapter alone.",
            question,
        )

    return asset_id, None


def _analysis_system_prompt() -> str:
    return "\n".join(
        [
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
        ]
    )


def _packet_contract_block(
    *,
    task_name: str,
    section_names: list[str],
    record_templates: list[tuple[str, list[str], list[str]]] | None = None,
) -> str:
    lines = [
        "Return exactly one Markdown packet using this outer envelope:",
        PACKET_START_TAG,
        f"task: {task_name}",
        f"version: {PACKET_VERSION}",
    ]
    for section_name in section_names:
        lines.extend(
            [
                "",
                f"[[SECTION {section_name}]]",
                f"...{section_name} content...",
                SECTION_END_TAG,
            ]
        )
    if record_templates:
        lines.extend(
            [
                "",
                "Repeat one FILMCREATOR_RECORD block for every extracted item of that type.",
            ]
        )
    for record_type, field_names, record_section_names in record_templates or []:
        lines.extend(
            [
                "",
                RECORD_START_TAG,
                f"type: {record_type}",
            ]
        )
        for field_name in field_names:
            lines.append(f"{field_name}: <value>")
        for record_section_name in record_section_names:
            lines.extend(
                [
                    "",
                    f"[[SECTION {record_section_name}]]",
                    f"...{record_section_name} content...",
                    SECTION_END_TAG,
                ]
            )
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
        requirements = [
            "- keep both sections short and concrete",
            "- avoid flourish and avoid hidden assumptions",
            "- if uncertain, state uncertainty briefly and continue",
        ]
    return "\n\n".join(
        [
            f"Project slug: {project_slug}",
            f"Chapter id: {chapter_source.chapter_id}",
            "Task: write project summary plus chapter summary for later scene extraction.",
            _packet_contract_block(
                task_name="chapter_summary",
                section_names=["project_summary_markdown", "chapter_summary_markdown"],
            ),
            "",
            "Requirements:",
            *requirements,
            "",
            "Chapter source markdown:",
            chapter_source.full_markdown,
        ]
    )


def _character_extraction_user_prompt(
    *,
    project_slug: str,
    chapter_source: _ChapterSource,
    chapter_summary: str,
    degraded: bool = False,
) -> str:
    record_fields = [
        "asset_id",
        "canonical_character_id",
        "aliases",
        "is_fully_identified",
        "manual_description_required",
        "manual_description_reason",
        "clarification_required",
        "clarification_reason",
        "clarification_question",
    ]
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
        body_requirements = [
            "- keep one record per meaningful character mention",
            "- prefer short facts over long prose",
            "- if uncertain, use clarification_required instead of guessing",
            "- if clarification is not required, still include clarification_reason and clarification_question as empty values",
        ]
    return "\n\n".join(
        [
            f"Project slug: {project_slug}",
            f"Chapter id: {chapter_source.chapter_id}",
            "Task: extract visible and referenced characters into a character index plus one Markdown file per character.",
            _packet_contract_block(
                task_name="character_extraction",
                section_names=["character_index_markdown"],
                record_templates=[("character", record_fields, ["markdown"])],
            ),
            "",
            "Important rules:",
            *body_requirements,
            "",
            "Asset id rules:",
            "- lowercase snake_case",
            "- stable across later reruns",
            "",
            "Each character Markdown file should include:",
            "- display name and chapter role",
            "- whether the character is physically present, referenced, or uncertain",
            "- physical description that is actually supported by the source",
            "- costume, silhouette, and continuity-critical traits when known",
            "- useful descriptive noun phrases for later render-facing prompt writing",
            "- explicit uncertainty notes when important details are missing",
            "",
            "Chapter summary:",
            chapter_summary,
        ]
    )


def _environment_extraction_user_prompt(
    *,
    project_slug: str,
    chapter_source: _ChapterSource,
    chapter_summary: str,
    degraded: bool = False,
) -> str:
    notes = [
        "- include stable environment families rather than every one-off mention",
        "- prefer visible geography and atmosphere over literary abstraction",
    ]
    if degraded:
        notes = [
            "- keep the environment set small and useful",
            "- use concise visible descriptions",
        ]
    return "\n\n".join(
        [
            f"Project slug: {project_slug}",
            f"Chapter id: {chapter_source.chapter_id}",
            "Task: extract environment families into an environment index plus one Markdown file per environment family.",
            _packet_contract_block(
                task_name="environment_extraction",
                section_names=["environment_index_markdown"],
                record_templates=[("environment", ["asset_id"], ["markdown"])],
            ),
            "",
            "Asset id rules:",
            "- lowercase snake_case",
            "- stable across later reruns",
            *notes,
            "",
            "Each environment Markdown file should include:",
            "- environment role such as primary, secondary, or transit setting",
            "- architecture or geography",
            "- lighting and atmosphere cues",
            "- scale cues and recurring environmental anchors",
            "- useful descriptive noun phrases for later render-facing prompt writing",
            "",
            "Chapter summary:",
            chapter_summary,
        ]
    )


def _scene_decomposition_user_prompt(
    *,
    project_slug: str,
    chapter_id: str,
    chapter_summary: str,
    degraded: bool = False,
) -> str:
    extra_rules = [
        "Prefer dramatic and staging boundaries, not every paragraph break.",
        "Preserve major narrative function changes as separate scenes.",
        "Do not merge setup, escalation, climax, and aftermath into one scene if they have different emotional or staging functions.",
        "If the chapter includes a reveal, aftermath, or emotional payoff after action, give that material its own scene when possible.",
        "Use a new scene when location, primary objective, or emotional mode changes significantly.",
        "For action chapters, prefer a sequence like: setup scene, escalation scene, climax/action consequence scene, aftermath/reveal scene when the source supports it.",
    ]
    if degraded:
        extra_rules = [
            "Keep scene count practical, but do not collapse the ending payoff into the action scene.",
            "Prefer 4 strong scenes over 3 merged scenes when the chapter clearly contains setup, escalation, consequence, and aftermath.",
            "Create a new scene when a new emotional function begins.",
        ]
    return "\n\n".join(
        [
            f"Project slug: {project_slug}",
            f"Chapter id: {chapter_id}",
            "Task: break the chapter into a small number of coherent scenes for later beat and clip planning.",
            _packet_contract_block(
                task_name="scene_decomposition",
                section_names=["scene_index_markdown"],
                record_templates=[("scene", ["scene_id"], ["markdown"])],
            ),
            "",
            "Scene id rules:",
            "- use SC### only inside the packet",
            "- start at SC001 for this chapter",
            "- do not include the chapter prefix in scene_id values",
            "- the chapter prefix will be applied externally by FilmCreator",
            *extra_rules,
            "Each scene Markdown file should include:",
            "- scene purpose",
            "- scene summary",
            "- participating characters",
            "- participating environments",
            "- dominant emotional shift",
            "- likely visual coverage families",
            "- likely continuity sensitivities",
            "",
            "Chapter summary:",
            chapter_summary,
        ]
    )


def _scene_beats_user_prompt(
    *,
    project_slug: str,
    scene_id: str,
    scene_markdown: str,
    degraded: bool = False,
) -> str:
    extra_rules = [
        "- keep beats reusable for later coverage planning",
    ]
    if degraded:
        extra_rules = [
            "- keep beats short and practical",
        ]
    return "\n\n".join(
        [
            f"Project slug: {project_slug}",
            f"Scene id: {scene_id}",
            "Task: deepen one scene into reusable beat bundles and update the scene breakdown with clearer staging facts.",
            _packet_contract_block(
                task_name="scene_beats",
                section_names=["updated_scene_markdown", "beat_index_markdown"],
                record_templates=[("beat", ["beat_id"], ["markdown"])],
            ),
            "",
            "Beat id rules:",
            "- use BT### within the scene",
            *extra_rules,
            "Each beat Markdown file should include:",
            "- beat purpose",
            "- beat start state and end state",
            "- character placement and movement logic",
            "- geography, axis, or eyeline facts when relevant",
            "- prop, vehicle, crowd, and environmental state that affects continuity",
            "- likely coverage families",
            "",
            "Scene breakdown markdown:",
            scene_markdown,
        ]
    )


def _clip_planning_user_prompt(
    *,
    project_slug: str,
    scene_id: str,
    scene_markdown: str,
    beat_index_path: Path,
    degraded: bool = False,
) -> str:
    beat_bundle_dir = beat_index_path.parent
    beat_bundles = _markdown_bundle(
        directory=beat_bundle_dir,
        exclude_names={"BEAT_INDEX.md", "README.md"},
    )
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
        clip_rules = [
            "- keep the first clip roster small and testable",
            "- prefer independent clips",
            "- use simple canonical ids only, such as CL001, CL002, CL003",
            "- never use hierarchical ids like CL001_001 or CL001-A",
            "- do not add suffixes or variants to clip ids",
            "- keep metadata concise but complete",
        ]
    return "\n\n".join(
        [
            f"Project slug: {project_slug}",
            f"Scene id: {scene_id}",
            "Task: turn the scene and beat bundles into an ordered clip roster and one clip plan per clip.",
            _packet_contract_block(
                task_name="clip_planning",
                section_names=["clip_roster_markdown"],
                record_templates=[("clip", ["clip_id"], ["markdown"])],
            ),
            "",
            "Clip planning rules:",
            *clip_rules,
            "",
            "Scene breakdown markdown:",
            scene_markdown,
            "",
            f"Beat index path: {repo_relative(beat_index_path)}",
            beat_index_path.read_text(encoding="utf-8"),
            "",
            "Beat bundle files:",
            beat_bundles or "(none)",
        ]
    )


def _character_shared_prompt_user_prompt(
    *,
    project_slug: str,
    asset_id: str,
    character_breakdown_path: Path,
    manual_description_path: Path,
    degraded: bool = False,
) -> str:
    character_markdown = character_breakdown_path.read_text(encoding="utf-8")
    manual_description = manual_description_path.read_text(encoding="utf-8") if manual_description_path.exists() else ""
    rules = [
        "- purpose and inputs may use stable asset ids",
        "- final positive and negative prompt bodies should avoid proper nouns and use descriptive noun phrases",
        "- keep prompts concrete and visible",
        "- prefer stable face, hair, body type, costume logic, silhouette, and recurring materials over scene-specific blocking",
    ]
    if degraded:
        rules = [
            "- keep the sections short and usable",
            "- preserve only the most stable visible traits",
            "- if uncertain, leave a short continuity note instead of inventing detail",
        ]
    return "\n\n".join(
        [
            f"Project slug: {project_slug}",
            f"Asset id: {asset_id}",
            "Task: write one reusable shared character-reference prompt draft for stable local generation.",
            _packet_contract_block(
                task_name="character_shared_prompts",
                section_names=[],
                record_templates=[
                    (
                        "character_prompt",
                        ["asset_id"],
                        [
                            "purpose",
                            "positive_prompt",
                            "negative_prompt",
                            "inputs_markdown",
                            "continuity_notes_markdown",
                            "repair_notes_markdown",
                        ],
                    )
                ],
            ),
            "",
            "Rules:",
            *rules,
            "",
            f"Character breakdown path: {repo_relative(character_breakdown_path)}",
            character_markdown,
            "",
            f"Manual character description path: {repo_relative(manual_description_path)}",
            manual_description or "(missing)",
        ]
    )


def _environment_shared_prompt_user_prompt(
    *,
    project_slug: str,
    asset_id: str,
    environment_breakdown_path: Path,
    degraded: bool = False,
) -> str:
    environment_markdown = environment_breakdown_path.read_text(encoding="utf-8")
    rules = [
        "- purpose and inputs may use stable asset ids",
        "- final positive and negative prompt bodies should avoid proper nouns and use descriptive noun phrases",
        "- keep prompts concrete and visible",
        "- emphasize stable architecture, geography, scale, atmosphere, and recurring environmental anchors",
    ]
    if degraded:
        rules = [
            "- keep the environment identity compact and stable",
            "- use short visible descriptors only",
        ]
    return "\n\n".join(
        [
            f"Project slug: {project_slug}",
            f"Asset id: {asset_id}",
            "Task: write one reusable shared environment-reference prompt draft for stable local generation.",
            _packet_contract_block(
                task_name="environment_shared_prompts",
                section_names=[],
                record_templates=[
                    (
                        "environment_prompt",
                        ["asset_id"],
                        [
                            "purpose",
                            "positive_prompt",
                            "negative_prompt",
                            "inputs_markdown",
                            "continuity_notes_markdown",
                            "repair_notes_markdown",
                        ],
                    )
                ],
            ),
            "",
            "Rules:",
            *rules,
            "",
            f"Environment breakdown path: {repo_relative(environment_breakdown_path)}",
            environment_markdown,
        ]
    )


def _scene_brief_markdown(scene_path: Path) -> str:
    sections = _split_sections(scene_path.read_text(encoding="utf-8"))
    desired_headings = [
        "Scene Purpose",
        "Scene Summary",
        "Participating Characters",
        "Participating Environments",
        "Dominant Emotional Shift",
        "Likely Visual Coverage Families",
        "Likely Continuity Sensitivities",
    ]
    parts: list[str] = []
    for heading in desired_headings:
        value = sections.get(heading, "").strip()
        if value:
            parts.extend([f"# {heading}", value, ""])
    if parts:
        return "\n".join(parts).strip()
    return scene_path.read_text(encoding="utf-8")


def _call_packet_task(
    *,
    client: LMStudioClient,
    project_dir: Path,
    task_name: str,
    system_prompt: str,
    user_prompt: str,
    degraded_user_prompt: str,
) -> _PacketDocument:
    task_started = time.perf_counter()
    print(f"[authoring] Task {task_name} started...")
    attempts: list[_TaskAttempt] = []
    for kind, active_user_prompt in [
        ("normal", user_prompt),
        ("same_prompt_retry", user_prompt),
        ("degraded_retry", degraded_user_prompt),
    ]:
        if kind != "normal":
            print(f"[authoring] Task {task_name} retrying with {kind}...")
        result = client.chat_completion_result(
            system_prompt=system_prompt,
            user_prompt=active_user_prompt,
            temperature=0.2,
        )
        log_path = _write_authoring_exchange_log(
            project_dir=project_dir,
            task_name=task_name,
            system_prompt=system_prompt,
            user_prompt=active_user_prompt,
            response=result.text,
        )
        if result.is_success:
            try:
                packet = _parse_packet_document(result.text, expected_task=task_name)
                elapsed = time.perf_counter() - task_started
                print(f"[authoring] Task {task_name} finished in {elapsed:.1f}s")
                return packet
            except LMStudioError as exc:
                attempts.append(
                    _TaskAttempt(
                        kind=kind,
                        status="parse_failed",
                        log_path=repo_relative(log_path),
                        message=str(exc),
                    )
                )
                continue
        attempts.append(
            _TaskAttempt(
                kind=kind,
                status=result.status,
                log_path=repo_relative(log_path),
                message=result.error_message or "Unspecified LM Studio authoring failure.",
            )
        )

    failure_path = _write_authoring_failure_artifact(
        project_dir=project_dir,
        task_name=task_name,
        asset_id=None,
        reason="; ".join(f"{attempt.kind}:{attempt.status}:{attempt.message}" for attempt in attempts),
    )
    raise LMStudioError(
        f"Authoring task '{task_name}' failed after retries. Failure artifact: {repo_relative(failure_path)}"
    )


def _structured_prompt_draft(record: _PacketRecord, *, asset_id: str, asset_type: str) -> _StructuredPromptDraft:
    parsed_inputs = _parse_markdown_key_value_items(
        _require_record_section(record, "inputs_markdown", allow_empty=True),
        asset_id=asset_id,
        asset_type=asset_type,
    )
    return _StructuredPromptDraft(
        asset_id=_require_record_field(record, "asset_id"),
        purpose=_require_record_section(record, "purpose"),
        positive_prompt=_require_record_section(record, "positive_prompt"),
        negative_prompt=_require_record_section(record, "negative_prompt"),
        inputs=parsed_inputs.items,
        continuity_notes=_parse_markdown_list(_require_record_section(record, "continuity_notes_markdown")),
        repair_notes=_parse_markdown_list(_require_record_section(record, "repair_notes_markdown")),
        warnings=parsed_inputs.warnings,
    )


def _build_prompt_package(
    *,
    path: Path,
    title: str,
    prompt_id: str,
    workflow_type: str,
    draft: _StructuredPromptDraft,
    sources: list[str],
) -> PromptPackage:
    return PromptPackage(
        path=path,
        title=title,
        prompt_id=prompt_id,
        purpose=draft.purpose,
        workflow_type=workflow_type,
        positive_prompt=draft.positive_prompt,
        negative_prompt=draft.negative_prompt,
        inputs_markdown="\n".join(f"- {key}: {value}" for key, value in draft.inputs.items()),
        continuity_notes_markdown="\n".join(f"- {item}" for item in draft.continuity_notes),
        repair_notes_markdown="\n".join(f"- {item}" for item in draft.repair_notes),
        sources_markdown="\n".join(f"- {source}" for source in sources),
    )


def _append_character_identity_section(
    *,
    markdown: str,
    aliases: str,
    canonical_character_id: str,
    is_fully_identified: str,
) -> str:
    suffix = "\n\n".join(
        [
            "# Aliases",
            aliases or "None",
            "",
            "# Canonical Character ID",
            canonical_character_id or "",
            "",
            "# Fully Identified",
            is_fully_identified,
            "",
        ]
    )
    return markdown.rstrip() + "\n\n" + suffix


def _append_manual_description_section(
    *,
    markdown: str,
    manual_required: bool,
    manual_reason: str,
) -> str:
    suffix = "\n\n".join(
        [
            "# Manual Description Input Required",
            "Yes" if manual_required else "No",
            "",
            "# Manual Description Reason",
            manual_reason or "None",
            "",
        ]
    )
    return markdown.rstrip() + "\n\n" + suffix


def _manual_character_description_placeholder(*, asset_id: str, reason: str) -> str:
    return "\n".join(
        [
            MANUAL_PLACEHOLDER_MARKER,
            "",
            "# Asset ID",
            asset_id,
            "",
            "# Purpose",
            "Paste a stable manual visual description for this character so later shared reference generation can use it.",
            "",
            "# Why This Is Needed",
            reason,
            "",
            "# Guidance",
            "- describe face, hair, body type, age impression, silhouette, skin tone, costume logic, and any continuity-critical marks",
            "- prefer visible facts over backstory",
            "- if multiple looks exist, describe the default look for this chapter",
            "",
            "# Manual Description",
            "",
        ]
    )


def _character_clarification_placeholder(*, asset_id: str, reason: str, question: str) -> str:
    return "\n".join(
        [
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
            "",
            "# Guidance",
            "- answer briefly and concretely",
            "- if another chapter already describes the character, note that source chapter",
            "- if the character is never described well, say whether FilmCreator should generate a reusable film-wide default description",
            "",
            "# Clarification Response",
            "",
        ]
    )


def _manual_description_path(*, project_dir: Path, asset_id: str) -> Path:
    return project_dir / "01_source" / "character_descriptions" / f"{asset_id}_manual_description.md"


def _character_clarification_path(*, project_dir: Path, asset_id: str) -> Path:
    return project_dir / "01_source" / "character_descriptions" / f"{asset_id}_clarification.md"


def _reconcile_manual_character_description_placeholders(
    *,
    project_dir: Path,
    active_requests: dict[str, str],
) -> list[Path]:
    manual_dir = project_dir / "01_source" / "character_descriptions"
    ensure_dir(manual_dir)
    written_paths: list[Path] = []

    for path in sorted(manual_dir.glob("*_manual_description.md")):
        asset_id = path.stem.removesuffix("_manual_description")
        if asset_id in active_requests:
            continue
        if _is_generated_manual_placeholder(path) and not _manual_description_has_user_content(path):
            try:
                path.unlink(missing_ok=True)
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


def _reconcile_character_clarification_placeholders(
    *,
    project_dir: Path,
    active_requests: dict[str, tuple[str, str]],
) -> list[Path]:
    clarification_dir = project_dir / "01_source" / "character_descriptions"
    ensure_dir(clarification_dir)
    written_paths: list[Path] = []
    for asset_id, (reason, question) in active_requests.items():
        path = _character_clarification_path(project_dir=project_dir, asset_id=asset_id)
        if path.exists() and _clarification_has_user_content(path):
            continue
        content = _character_clarification_placeholder(asset_id=asset_id, reason=reason, question=question)
        if path.exists() and path.read_text(encoding="utf-8") == content:
            continue
        _write_text(path, content)
        written_paths.append(path)
    return written_paths


def _is_generated_manual_placeholder(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    return MANUAL_PLACEHOLDER_MARKER in text or (
        "Paste a stable manual visual description for this character" in text
        and "# Manual Description" in text
    )


def _manual_description_has_user_content(path: Path) -> bool:
    sections = _split_sections(path.read_text(encoding="utf-8"))
    manual_description = sections.get("Manual Description", "").strip()
    return bool(manual_description)


def _clarification_has_user_content(path: Path) -> bool:
    sections = _split_sections(path.read_text(encoding="utf-8"))
    return bool(sections.get("Clarification Response", "").strip())


def _write_authoring_exchange_log(
    *,
    project_dir: Path,
    task_name: str,
    system_prompt: str,
    user_prompt: str,
    response: str,
) -> Path:
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    log_path = project_dir / "02_story_analysis" / "logs" / f"{timestamp}_{task_name}.md"
    log_body = "\n".join(
        [
            "# LM Studio Authoring Exchange",
            f"- timestamp_utc: {datetime.now(timezone.utc).isoformat()}",
            f"- task: {task_name}",
            "",
            "## System Prompt",
            "````text",
            system_prompt,
            "````",
            "",
            "## User Prompt",
            "````text",
            user_prompt,
            "````",
            "",
            "## Raw Response",
            "````text",
            response,
            "````",
            "",
        ]
    )
    _write_text(log_path, log_body)
    return log_path


def _write_authoring_failure_artifact(
    *,
    project_dir: Path,
    task_name: str,
    asset_id: str | None,
    reason: str,
) -> Path:
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    slug = asset_id or "task"
    path = project_dir / "02_story_analysis" / "logs" / "failures" / f"{timestamp}_{task_name}_{slug}.md"
    body = "\n".join(
        [
            "# FilmCreator Authoring Failure",
            f"- timestamp_utc: {datetime.now(timezone.utc).isoformat()}",
            f"- task: {task_name}",
            f"- asset_id: {asset_id or ''}",
            "",
            "## Reason",
            reason,
            "",
        ]
    )
    _write_text(path, body)
    return path


def _parse_packet_document(response: str, *, expected_task: str | None = None) -> _PacketDocument:
    packet_body = _extract_packet_body(_strip_markdown_fences(response))
    packet = _parse_packet_body(packet_body)
    if expected_task is not None:
        actual_task = packet.metadata.get("task", "")
        if actual_task != expected_task:
            raise LMStudioError(
                f"LM Studio returned packet task '{actual_task or '(missing)'}' but expected '{expected_task}'."
            )
    version = packet.metadata.get("version", "")
    if version != PACKET_VERSION:
        raise LMStudioError(
            f"LM Studio returned packet version '{version or '(missing)'}' but expected '{PACKET_VERSION}'."
        )
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
        if stripped == RECORD_START_TAG:
            record_lines, index = _collect_tagged_block(
                lines,
                index,
                RECORD_START_TAG,
                RECORD_END_TAG,
                fallback_start_tag=RECORD_START_TAG,
            )
            records.append(_parse_packet_record(record_lines))
            continue
        section_match = SECTION_TAG_PATTERN.fullmatch(stripped)
        if section_match:
            section_name = section_match.group(1).lower()
            section_lines, index = _collect_tagged_block(
                lines,
                index,
                stripped,
                SECTION_END_TAG,
                fallback_stop_any_tag=True,
            )
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
        section_match = SECTION_TAG_PATTERN.fullmatch(stripped)
        if section_match:
            section_name = section_match.group(1).lower()
            section_body, index = _collect_tagged_block(
                record_lines,
                index,
                stripped,
                SECTION_END_TAG,
                fallback_stop_any_tag=True,
            )
            sections[section_name] = "\n".join(section_body).strip()
            continue
        key, value = _split_packet_key_value(stripped)
        fields[key] = value
        index += 1

    record_type = fields.get("type", "")
    if not record_type:
        raise LMStudioError("Packet record is missing required field 'type'.")
    return _PacketRecord(fields=fields, sections=sections)


def _collect_tagged_block(
    lines: list[str],
    start_index: int,
    start_tag: str,
    end_tag: str,
    *,
    fallback_start_tag: str | None = None,
    fallback_stop_any_tag: bool = False,
) -> tuple[list[str], int]:
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
        if fallback_stop_any_tag and stripped.startswith("[[") and stripped.endswith("]]"):
            return body, index
        body.append(lines[index])
        index += 1
    return body, index


def _split_packet_key_value(line: str) -> tuple[str, str]:
    if ":" not in line:
        raise LMStudioError(f"Expected 'key: value' packet line but got '{line}'.")
    key, value = line.split(":", 1)
    normalized_key = key.strip().lower()
    if not normalized_key:
        raise LMStudioError(f"Invalid empty packet key in line '{line}'.")
    return normalized_key, value.strip()


def _require_packet_section(packet: _PacketDocument, section_name: str, *, allow_empty: bool = False) -> str:
    value = packet.sections.get(section_name.lower(), "").strip()
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
        raise LMStudioError(
            f"Packet was expected to contain exactly one '{record_type}' record but found {len(records)}."
        )
    return records[0]


def _require_record_field(record: _PacketRecord, field_name: str, *, allow_empty: bool = False) -> str:
    value = record.fields.get(field_name.lower(), "").strip()
    if not value and not allow_empty:
        raise LMStudioError(f"Packet record is missing required field '{field_name}'.")
    return value


def _require_record_section(record: _PacketRecord, section_name: str, *, allow_empty: bool = False) -> str:
    value = record.sections.get(section_name.lower(), "").strip()
    if not value and not allow_empty:
        raise LMStudioError(f"Packet record is missing required section '{section_name}'.")
    return value


def _validate_scene_decomposition(
    *,
    chapter_id: str,
    scene_records: list[_PacketRecord],
) -> list[str]:
    warnings: list[str] = []
    if len(scene_records) < 3:
        raise LMStudioError(
            f"Scene decomposition for {chapter_id} returned only {len(scene_records)} scenes; minimum expected is 3."
        )

    emotional_shifts: list[str] = []
    for record in scene_records:
        markdown = _require_record_section(record, "markdown")
        normalized = markdown.lower()

        if "aftermath" in normalized or "payoff" in normalized or "helplessness" in normalized or "reveal" in normalized:
            emotional_shifts.append("aftermath")
        if "battle" in normalized or "attack" in normalized or "destruction" in normalized or "boarding" in normalized:
            emotional_shifts.append("action")
        if "introduce" in normalized or "setup" in normalized or "return" in normalized or "arrival" in normalized:
            emotional_shifts.append("setup")

    if "action" in emotional_shifts and "aftermath" not in emotional_shifts:
        warnings.append(
            "Scene decomposition may have collapsed aftermath/reveal material into action scenes; no aftermath-like scene language detected."
        )

    return warnings


def _extract_clip_beat_refs(markdown: str) -> set[str]:
    refs: set[str] = set()
    for match in re.finditer(r"BT\d{3}", markdown.upper()):
        refs.add(match.group(0))
    return refs


def _scene_allows_single_clip(scene_markdown: str) -> bool:
    normalized = scene_markdown.lower()
    return "single-shot" in normalized or "single shot" in normalized


def _validate_scene_duration_sanity(
    *,
    scene_id: str,
    beat_ids: list[str],
    clip_ids: list[str],
) -> list[str]:
    warnings: list[str] = []
    estimated_duration_seconds = len(clip_ids) * 5

    if len(beat_ids) >= 4 and estimated_duration_seconds < 15:
        warnings.append(
            f"{scene_id} may be under-covered: {len(beat_ids)} beats mapped to only {len(clip_ids)} clips (~{estimated_duration_seconds}s)."
        )

    if len(clip_ids) >= 10 and estimated_duration_seconds > 60:
        warnings.append(
            f"{scene_id} may be over-segmented: {len(clip_ids)} clips (~{estimated_duration_seconds}s)."
        )

    return warnings


def _validate_clip_plan(
    *,
    scene_id: str,
    scene_markdown: str,
    beat_ids: list[str],
    clip_ids: list[str],
    clip_markdowns: dict[str, str],
    roster_markdown: str,
    strict_missing_beats: bool = False,
) -> list[str]:
    warnings: list[str] = []

    if len(clip_ids) < 2 and not _scene_allows_single_clip(scene_markdown):
        raise LMStudioError(
            f"Clip plan for {scene_id} produced only {len(clip_ids)} clip(s), but the scene is not marked as a valid single-shot scene."
        )

    covered_beats: set[str] = set()
    for markdown in clip_markdowns.values():
        covered_beats.update(_extract_clip_beat_refs(markdown))

    missing_beats = [beat_id for beat_id in beat_ids if beat_id not in covered_beats]
    if missing_beats:
        message = (
            f"Clip plan for {scene_id} does not explicitly reference all beats. Missing beat refs: {', '.join(missing_beats)}"
        )
        if strict_missing_beats:
            raise LMStudioError(message)
        warnings.append(message)

    roster_ids = re.findall(r"\bCL\d{3}\b", roster_markdown.upper())
    if roster_ids and len(set(roster_ids)) != len(clip_ids):
        warnings.append(
            f"Clip roster / clip file parity mismatch in {scene_id}: roster shows {len(set(roster_ids))} clip ids but {len(clip_ids)} clip files were created."
        )

    if len(beat_ids) >= 3 and len(clip_ids) == 1:
        raise LMStudioError(
            f"Clip plan for {scene_id} compressed {len(beat_ids)} beats into a single clip, which is not allowed."
        )

    warnings.extend(
        _validate_scene_duration_sanity(
            scene_id=scene_id,
            beat_ids=beat_ids,
            clip_ids=clip_ids,
        )
    )
    return warnings


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
        values = {
            "project_asset": f"{asset_type}:{asset_id}",
            "asset_id": asset_id,
        }
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


def _normalize_clip_id(
    value: str,
    *,
    promoted_hierarchical_map: dict[str, str] | None = None,
    hierarchical_sequence_seen: int = 0,
) -> tuple[str, str | None]:
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
        warning = (
            f"Promoted hierarchical clip id '{value}' to top-level canonical clip id '{coerced}'."
        )
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


def _first_existing_path(directory: Path, *, pattern: str) -> Path:
    matches = sorted(directory.glob(pattern))
    if not matches:
        raise FileNotFoundError(f"No files matching {pattern} found under {directory}")
    return matches[0]


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
    for path in directory.glob("*.md"):
        if path.name in keep_names:
            continue
        try:
            path.unlink(missing_ok=True)
        except PermissionError:
            continue


def _write_text(path: Path, content: str) -> None:
    ensure_dir(path.parent)
    text = content.rstrip() + "\n"
    path.write_text(text, encoding="utf-8")
