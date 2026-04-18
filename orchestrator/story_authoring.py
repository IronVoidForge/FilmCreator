from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

from .authoring import PromptWriteSummary, write_prompts
from .common import ensure_dir, repo_relative, validate_clip_id, validate_scene_id
from .lmstudio_client import LMStudioClient, LMStudioError
from .prompt_package import PromptPackage, write_prompt_package
from .scaffold import create_clip, create_project, create_scene
from .settings import load_runtime_settings


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
class StoryAnalysisSummary:
    project_slug: str
    chapter_path: str
    chapter_id: str
    model: str
    written_files: list[str]
    scene_ids: list[str]
    manual_character_description_requests: list[ManualCharacterDescriptionRequest]

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
        }


@dataclass(frozen=True)
class ScenePlanningSummary:
    project_slug: str
    scene_id: str
    model: str
    written_files: list[str]
    beat_ids: list[str]
    clip_ids: list[str]

    def to_dict(self) -> dict[str, object]:
        return {
            "project_slug": self.project_slug,
            "scene_id": self.scene_id,
            "model": self.model,
            "written_files": self.written_files,
            "beat_ids": self.beat_ids,
            "clip_ids": self.clip_ids,
        }


@dataclass(frozen=True)
class SharedPromptSummary:
    project_slug: str
    model: str
    written_files: list[str]

    def to_dict(self) -> dict[str, object]:
        return {
            "project_slug": self.project_slug,
            "model": self.model,
            "written_files": self.written_files,
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
class _StructuredPromptDraft:
    asset_id: str
    purpose: str
    positive_prompt: str
    negative_prompt: str
    inputs: dict[str, str]
    continuity_notes: list[str]
    repair_notes: list[str]


@dataclass(frozen=True)
class _PacketRecord:
    fields: dict[str, str]
    sections: dict[str, str]


@dataclass(frozen=True)
class _PacketDocument:
    metadata: dict[str, str]
    sections: dict[str, str]
    records: list[_PacketRecord]


def analyze_chapter(*, project_slug: str, chapter: str | None = None) -> StoryAnalysisSummary:
    client, resolved_model = _client_and_model()
    project_dir = create_project(project_slug)
    chapter_source = _resolve_chapter_source(project_slug, chapter)
    _prune_markdown_dir(
        project_dir / "02_story_analysis" / "character_breakdowns",
        keep_names={"README.md"},
    )
    _prune_markdown_dir(
        project_dir / "02_story_analysis" / "environment_breakdowns",
        keep_names={"README.md"},
    )
    _prune_markdown_dir(
        project_dir / "02_story_analysis" / "scene_breakdowns",
        keep_names={"README.md"},
    )

    written_files: list[str] = []
    manual_requests: list[ManualCharacterDescriptionRequest] = []

    summary_packet = _call_packet_task(
        client=client,
        project_dir=project_dir,
        task_name="chapter_summary",
        system_prompt=_analysis_system_prompt(),
        user_prompt=_chapter_summary_user_prompt(project_slug, chapter_source),
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
    )
    character_index_markdown = _require_packet_section(character_packet, "character_index_markdown")
    character_index_path = project_dir / "02_story_analysis" / "character_breakdowns" / "CHARACTER_INDEX.md"
    _write_text(character_index_path, character_index_markdown)
    written_files.append(repo_relative(character_index_path))

    active_manual_description_requests: dict[str, str] = {}
    for raw_character in _require_packet_records(character_packet, record_type="character"):
        asset_id = _normalize_asset_id(
            _require_record_field(raw_character, "asset_id"),
            fallback_prefix="character",
        )
        filename = f"{asset_id}.md"
        markdown = _require_record_section(raw_character, "markdown")
        manual_description_required = _parse_packet_bool(
            _require_record_field(raw_character, "manual_description_required")
        )
        manual_description_reason = _require_record_field(
            raw_character,
            "manual_description_reason",
            allow_empty=not manual_description_required,
        )

        character_markdown = _append_manual_description_section(
            markdown=markdown,
            manual_required=manual_description_required,
            manual_reason=manual_description_reason,
        )
        character_path = project_dir / "02_story_analysis" / "character_breakdowns" / filename
        _write_text(character_path, character_markdown)
        written_files.append(repo_relative(character_path))

        if manual_description_required:
            manual_path = _manual_description_path(project_dir=project_dir, asset_id=asset_id)
            active_manual_description_requests[asset_id] = manual_description_reason
            manual_requests.append(
                ManualCharacterDescriptionRequest(
                    asset_id=asset_id,
                    source_path=repo_relative(manual_path),
                    reason=manual_description_reason,
                )
            )

    manual_placeholder_paths = _reconcile_manual_character_description_placeholders(
        project_dir=project_dir,
        active_requests=active_manual_description_requests,
    )
    written_files.extend(repo_relative(path) for path in manual_placeholder_paths)

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
            chapter_source=chapter_source,
            chapter_summary=chapter_summary_markdown,
            character_index_path=character_index_path,
            environment_index_path=environment_index_path,
        ),
    )
    scene_index_markdown = _require_packet_section(scene_packet, "scene_index_markdown")
    scene_index_path = project_dir / "02_story_analysis" / "scene_breakdowns" / "SCENE_INDEX.md"
    _write_text(scene_index_path, scene_index_markdown)
    written_files.append(repo_relative(scene_index_path))

    scene_ids: list[str] = []
    for raw_scene in _require_packet_records(scene_packet, record_type="scene"):
        scene_id = _normalize_scene_id(_require_record_field(raw_scene, "scene_id"))
        filename = f"{scene_id}.md"
        markdown = _require_record_section(raw_scene, "markdown")
        create_scene(project_slug, scene_id)
        scene_path = project_dir / "02_story_analysis" / "scene_breakdowns" / filename
        _write_text(scene_path, markdown)
        written_files.append(repo_relative(scene_path))
        scene_ids.append(scene_id)

    return StoryAnalysisSummary(
        project_slug=project_slug,
        chapter_path=repo_relative(chapter_source.path),
        chapter_id=chapter_source.chapter_id,
        model=resolved_model,
        written_files=written_files,
        scene_ids=scene_ids,
        manual_character_description_requests=manual_requests,
    )


def plan_scene(*, project_slug: str, scene_id: str) -> ScenePlanningSummary:
    scene_id = validate_scene_id(scene_id)
    client, resolved_model = _client_and_model()
    project_dir = create_project(project_slug)
    scene_path = project_dir / "02_story_analysis" / "scene_breakdowns" / f"{scene_id}.md"
    if not scene_path.exists():
        raise FileNotFoundError(f"Scene breakdown not found: {scene_path}")

    chapter_summary_path = _first_existing_path(
        project_dir / "02_story_analysis" / "chapter_analysis",
        pattern="CH*_summary.md",
    )
    character_index_path = project_dir / "02_story_analysis" / "character_breakdowns" / "CHARACTER_INDEX.md"
    environment_index_path = project_dir / "02_story_analysis" / "environment_breakdowns" / "ENVIRONMENT_INDEX.md"

    written_files: list[str] = []

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
            scene_path=scene_path,
            chapter_summary_path=chapter_summary_path,
            character_index_path=character_index_path,
            environment_index_path=environment_index_path,
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

    clip_packet = _call_packet_task(
        client=client,
        project_dir=project_dir,
        task_name="clip_planning",
        system_prompt=_analysis_system_prompt(),
        user_prompt=_clip_planning_user_prompt(
            project_slug=project_slug,
            scene_id=scene_id,
            scene_path=scene_path,
            beat_index_path=beat_index_path,
            character_index_path=character_index_path,
            environment_index_path=environment_index_path,
        ),
    )
    clip_roster_markdown = _require_packet_section(clip_packet, "clip_roster_markdown")
    clip_dir = project_dir / "02_story_analysis" / "clip_plans" / scene_id
    ensure_dir(clip_dir)
    _prune_markdown_dir(clip_dir, keep_names=set())
    clip_roster_path = clip_dir / f"{scene_id}_clip_roster.md"
    _write_text(clip_roster_path, clip_roster_markdown)
    written_files.append(repo_relative(clip_roster_path))

    clip_ids: list[str] = []
    for raw_clip in _require_packet_records(clip_packet, record_type="clip"):
        clip_id = _normalize_clip_id(_require_record_field(raw_clip, "clip_id"))
        filename = f"{clip_id}.md"
        markdown = _require_record_section(raw_clip, "markdown")
        create_clip(project_slug, scene_id, clip_id)
        clip_path = clip_dir / filename
        _write_text(clip_path, markdown)
        written_files.append(repo_relative(clip_path))
        clip_ids.append(clip_id)

    return ScenePlanningSummary(
        project_slug=project_slug,
        scene_id=scene_id,
        model=resolved_model,
        written_files=written_files,
        beat_ids=beat_ids,
        clip_ids=clip_ids,
    )


def write_shared_prompts(*, project_slug: str) -> SharedPromptSummary:
    client, resolved_model = _client_and_model()
    project_dir = create_project(project_slug)
    project_summary_path = project_dir / "02_story_analysis" / "story_summary" / "project_summary.md"
    chapter_summary_path = _first_existing_path(
        project_dir / "02_story_analysis" / "chapter_analysis",
        pattern="CH*_summary.md",
    )
    character_index_path = project_dir / "02_story_analysis" / "character_breakdowns" / "CHARACTER_INDEX.md"
    environment_index_path = project_dir / "02_story_analysis" / "environment_breakdowns" / "ENVIRONMENT_INDEX.md"

    character_packet = _call_packet_task(
        client=client,
        project_dir=project_dir,
        task_name="character_shared_prompts",
        system_prompt=_analysis_system_prompt(),
        user_prompt=_character_shared_prompt_user_prompt(
            project_slug=project_slug,
            project_summary_path=project_summary_path,
            chapter_summary_path=chapter_summary_path,
            character_index_path=character_index_path,
        ),
    )

    written_files: list[str] = []
    for raw_prompt in _require_packet_records(character_packet, record_type="character_prompt"):
        draft = _structured_prompt_draft(raw_prompt)
        asset_id = _normalize_asset_id(draft.asset_id, fallback_prefix="character")
        prompt_path = (
            project_dir / "03_prompt_packages" / "characters" / asset_id / f"{asset_id}_ref_prompt.md"
        )
        character_breakdown_path = (
            project_dir / "02_story_analysis" / "character_breakdowns" / f"{asset_id}.md"
        )
        manual_description_path = _manual_description_path(project_dir=project_dir, asset_id=asset_id)
        sources = [
            repo_relative(project_summary_path),
            repo_relative(chapter_summary_path),
            repo_relative(character_index_path),
        ]
        if character_breakdown_path.exists():
            sources.append(repo_relative(character_breakdown_path))
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

    environment_packet = _call_packet_task(
        client=client,
        project_dir=project_dir,
        task_name="environment_shared_prompts",
        system_prompt=_analysis_system_prompt(),
        user_prompt=_environment_shared_prompt_user_prompt(
            project_slug=project_slug,
            project_summary_path=project_summary_path,
            chapter_summary_path=chapter_summary_path,
            environment_index_path=environment_index_path,
        ),
    )

    for raw_prompt in _require_packet_records(environment_packet, record_type="environment_prompt"):
        draft = _structured_prompt_draft(raw_prompt)
        asset_id = _normalize_asset_id(draft.asset_id, fallback_prefix="environment")
        prompt_path = (
            project_dir / "03_prompt_packages" / "environments" / asset_id / f"{asset_id}_ref_prompt.md"
        )
        environment_breakdown_path = (
            project_dir / "02_story_analysis" / "environment_breakdowns" / f"{asset_id}.md"
        )
        sources = [
            repo_relative(project_summary_path),
            repo_relative(chapter_summary_path),
            repo_relative(environment_index_path),
        ]
        if environment_breakdown_path.exists():
            sources.append(repo_relative(environment_breakdown_path))
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

    return SharedPromptSummary(
        project_slug=project_slug,
        model=resolved_model,
        written_files=written_files,
    )


def authoring_checkpoint(
    *,
    project_slug: str,
    chapter: str | None = None,
    scene_id: str | None = None,
) -> AuthoringCheckpointSummary:
    analysis = analyze_chapter(project_slug=project_slug, chapter=chapter)
    target_scene_id = scene_id or (analysis.scene_ids[0] if analysis.scene_ids else "SC001")
    planning = plan_scene(project_slug=project_slug, scene_id=target_scene_id)
    shared_prompts = write_shared_prompts(project_slug=project_slug)
    clip_prompts = write_prompts(project_slug=project_slug, scene_id=target_scene_id)
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
            raise FileNotFoundError(f"No chapter Markdown files found under {chapter_dir}")
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


def _analysis_system_prompt() -> str:
    return "\n".join(
        [
            "You are FilmCreator's local authoring analyst.",
            "Return exactly one FILMCREATOR packet in Markdown.",
            "Do not return JSON.",
            "Do not use markdown fences.",
            "Do not add commentary before or after the packet.",
            "Preserve uncertainty instead of inventing hidden facts.",
            "When asked to write Markdown file contents, place the complete file body inside the requested SECTION tags.",
            "When asked to extract render-facing facts, focus on visible, continuity-relevant details.",
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


def _chapter_summary_user_prompt(project_slug: str, chapter_source: _ChapterSource) -> str:
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
            "- proper nouns are allowed",
            "- do not mention ComfyUI nodes or workflow patching",
            "- separate visual continuity facts from broad story summary",
            "- make the project summary reusable across later chapters, not just this one scene",
            "- make the chapter summary specific enough to support later scene decomposition without re-reading the whole chapter",
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
) -> str:
    return "\n\n".join(
        [
            f"Project slug: {project_slug}",
            f"Chapter id: {chapter_source.chapter_id}",
            "Task: extract visible and referenced characters into a character index plus one Markdown file per character.",
            _packet_contract_block(
                task_name="character_extraction",
                section_names=["character_index_markdown"],
                record_templates=[
                    (
                        "character",
                        ["asset_id", "manual_description_required", "manual_description_reason"],
                        ["markdown"],
                    )
                ],
            ),
            "",
            "Important rule:",
            "- if a character does not have enough physical or visual description in the supplied material to support dependable later image generation, set manual_description_required to true",
            "- explain exactly why in manual_description_reason",
            "- do not guess ornate missing details just to avoid the flag",
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
            "",
            "Chapter source markdown:",
            chapter_source.full_markdown,
        ]
    )


def _environment_extraction_user_prompt(
    *,
    project_slug: str,
    chapter_source: _ChapterSource,
    chapter_summary: str,
) -> str:
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
            "",
            "Chapter source markdown:",
            chapter_source.full_markdown,
        ]
    )


def _scene_decomposition_user_prompt(
    *,
    project_slug: str,
    chapter_source: _ChapterSource,
    chapter_summary: str,
    character_index_path: Path,
    environment_index_path: Path,
) -> str:
    return "\n\n".join(
        [
            f"Project slug: {project_slug}",
            f"Chapter id: {chapter_source.chapter_id}",
            "Task: break the chapter into a small number of coherent scenes for later beat and clip planning.",
            _packet_contract_block(
                task_name="scene_decomposition",
                section_names=["scene_index_markdown"],
                record_templates=[("scene", ["scene_id"], ["markdown"])],
            ),
            "",
            "Scene id rules:",
            "- use SC###",
            "- start at SC001 for this chapter",
            "",
            "Prefer dramatic and staging boundaries, not every paragraph break.",
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
            "",
            f"Character index path: {repo_relative(character_index_path)}",
            character_index_path.read_text(encoding="utf-8"),
            "",
            f"Environment index path: {repo_relative(environment_index_path)}",
            environment_index_path.read_text(encoding="utf-8"),
            "",
            "Chapter source markdown:",
            chapter_source.full_markdown,
        ]
    )


def _scene_beats_user_prompt(
    *,
    project_slug: str,
    scene_id: str,
    scene_path: Path,
    chapter_summary_path: Path,
    character_index_path: Path,
    environment_index_path: Path,
) -> str:
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
            "",
            "Each beat Markdown file should include:",
            "- beat purpose",
            "- beat start state and end state",
            "- character placement and movement logic",
            "- geography, axis, or eyeline facts when relevant",
            "- prop, vehicle, crowd, and environmental state that affects continuity",
            "- likely coverage families",
            "",
            f"Chapter summary path: {repo_relative(chapter_summary_path)}",
            chapter_summary_path.read_text(encoding="utf-8"),
            "",
            f"Character index path: {repo_relative(character_index_path)}",
            character_index_path.read_text(encoding="utf-8"),
            "",
            f"Environment index path: {repo_relative(environment_index_path)}",
            environment_index_path.read_text(encoding="utf-8"),
            "",
            f"Scene breakdown path: {repo_relative(scene_path)}",
            scene_path.read_text(encoding="utf-8"),
        ]
    )


def _clip_planning_user_prompt(
    *,
    project_slug: str,
    scene_id: str,
    scene_path: Path,
    beat_index_path: Path,
    character_index_path: Path,
    environment_index_path: Path,
) -> str:
    beat_bundle_dir = beat_index_path.parent
    beat_bundles = _markdown_bundle(
        directory=beat_bundle_dir,
        exclude_names={"BEAT_INDEX.md", "README.md"},
    )
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
            "- clip = cut",
            "- most clips should target around 5 seconds",
            "- treat continuous_follow as rare",
            "- prefer reframe_same_moment, reblock_same_scene, insert, and cutaway when appropriate",
            "- include continuity mode, composition type, starting keyframe strategy, dependency policy, fallback strategy, visible character assets, required refs, optional refs, opening keyframe intent, cut motion intent, and interval beats",
            "- identify one or two strong initial test clips if the scene allows it",
            "",
            f"Character index path: {repo_relative(character_index_path)}",
            character_index_path.read_text(encoding="utf-8"),
            "",
            f"Environment index path: {repo_relative(environment_index_path)}",
            environment_index_path.read_text(encoding="utf-8"),
            "",
            f"Scene breakdown path: {repo_relative(scene_path)}",
            scene_path.read_text(encoding="utf-8"),
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
    project_summary_path: Path,
    chapter_summary_path: Path,
    character_index_path: Path,
) -> str:
    character_breakdowns = _markdown_bundle(
        directory=character_index_path.parent,
        exclude_names={"CHARACTER_INDEX.md", "README.md"},
    )
    manual_descriptions = _markdown_bundle(
        directory=project_summary_path.parents[2] / "01_source" / "character_descriptions",
        exclude_names={"README.md"},
    )
    return "\n\n".join(
        [
            f"Project slug: {project_slug}",
            "Task: write reusable shared character-reference prompt drafts for stable local generation.",
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
            "- purpose and inputs may use stable asset ids",
            "- final positive and negative prompt bodies should avoid proper nouns and use descriptive noun phrases",
            "- keep prompts concrete and visible",
            "- prefer stable face, hair, body type, costume logic, silhouette, and recurring materials over scene-specific blocking",
            "",
            f"Project summary path: {repo_relative(project_summary_path)}",
            project_summary_path.read_text(encoding="utf-8"),
            "",
            f"Chapter summary path: {repo_relative(chapter_summary_path)}",
            chapter_summary_path.read_text(encoding="utf-8"),
            "",
            f"Character index path: {repo_relative(character_index_path)}",
            character_index_path.read_text(encoding="utf-8"),
            "",
            "Character breakdown files:",
            character_breakdowns or "(none)",
            "",
            "Manual character description files:",
            manual_descriptions or "(none)",
        ]
    )


def _environment_shared_prompt_user_prompt(
    *,
    project_slug: str,
    project_summary_path: Path,
    chapter_summary_path: Path,
    environment_index_path: Path,
) -> str:
    environment_breakdowns = _markdown_bundle(
        directory=environment_index_path.parent,
        exclude_names={"ENVIRONMENT_INDEX.md", "README.md"},
    )
    return "\n\n".join(
        [
            f"Project slug: {project_slug}",
            "Task: write reusable shared environment-reference prompt drafts for stable local generation.",
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
            "- purpose and inputs may use stable asset ids",
            "- final positive and negative prompt bodies should avoid proper nouns and use descriptive noun phrases",
            "- keep prompts concrete and visible",
            "- emphasize stable architecture, geography, scale, atmosphere, and recurring environmental anchors",
            "",
            f"Project summary path: {repo_relative(project_summary_path)}",
            project_summary_path.read_text(encoding="utf-8"),
            "",
            f"Chapter summary path: {repo_relative(chapter_summary_path)}",
            chapter_summary_path.read_text(encoding="utf-8"),
            "",
            f"Environment index path: {repo_relative(environment_index_path)}",
            environment_index_path.read_text(encoding="utf-8"),
            "",
            "Environment breakdown files:",
            environment_breakdowns or "(none)",
        ]
    )


def _call_packet_task(
    *,
    client: LMStudioClient,
    project_dir: Path,
    task_name: str,
    system_prompt: str,
    user_prompt: str,
) -> _PacketDocument:
    response = client.chat_completion(system_prompt=system_prompt, user_prompt=user_prompt, temperature=0.2)
    log_path = _write_authoring_exchange_log(
        project_dir=project_dir,
        task_name=task_name,
        system_prompt=system_prompt,
        user_prompt=user_prompt,
        response=response,
    )
    try:
        return _parse_packet_document(response, expected_task=task_name)
    except LMStudioError as exc:
        raise LMStudioError(
            f"{exc} Raw response saved to {repo_relative(log_path)}"
        ) from exc


def _structured_prompt_draft(record: _PacketRecord) -> _StructuredPromptDraft:
    inputs = _parse_markdown_key_value_items(_require_record_section(record, "inputs_markdown"))
    return _StructuredPromptDraft(
        asset_id=_require_record_field(record, "asset_id"),
        purpose=_require_record_section(record, "purpose"),
        positive_prompt=_require_record_section(record, "positive_prompt"),
        negative_prompt=_require_record_section(record, "negative_prompt"),
        inputs=inputs,
        continuity_notes=_parse_markdown_list(_require_record_section(record, "continuity_notes_markdown")),
        repair_notes=_parse_markdown_list(_require_record_section(record, "repair_notes_markdown")),
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


def _manual_description_path(*, project_dir: Path, asset_id: str) -> Path:
    return project_dir / "01_source" / "character_descriptions" / f"{asset_id}_manual_description.md"


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
            path.unlink(missing_ok=True)

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
    cleaned = response.strip()
    start = cleaned.find(PACKET_START_TAG)
    end = cleaned.rfind(PACKET_END_TAG)
    if start == -1 or end == -1 or end <= start:
        raise LMStudioError("LM Studio did not return a FILMCREATOR packet envelope.")
    return cleaned[start + len(PACKET_START_TAG) : end].strip()


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
            record_lines, index = _collect_tagged_block(lines, index, RECORD_START_TAG, RECORD_END_TAG)
            records.append(_parse_packet_record(record_lines))
            continue
        section_match = SECTION_TAG_PATTERN.fullmatch(stripped)
        if section_match:
            section_name = section_match.group(1).lower()
            section_lines, index = _collect_tagged_block(lines, index, stripped, SECTION_END_TAG)
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
            section_body, index = _collect_tagged_block(record_lines, index, stripped, SECTION_END_TAG)
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
) -> tuple[list[str], int]:
    if lines[start_index].strip() != start_tag:
        raise LMStudioError(f"Expected start tag '{start_tag}' but found '{lines[start_index].strip()}'.")
    body: list[str] = []
    index = start_index + 1
    while index < len(lines):
        stripped = lines[index].strip()
        if stripped == end_tag:
            return body, index + 1
        body.append(lines[index])
        index += 1
    raise LMStudioError(f"Missing closing tag '{end_tag}'.")


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


def _parse_packet_bool(value: str) -> bool:
    normalized = value.strip().lower()
    if normalized in {"true", "yes", "1"}:
        return True
    if normalized in {"false", "no", "0"}:
        return False
    raise LMStudioError(f"Expected boolean packet field but got '{value}'.")


def _parse_markdown_key_value_items(markdown: str) -> dict[str, str]:
    values: dict[str, str] = {}
    for line in markdown.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith(("- ", "* ")):
            stripped = stripped[2:].strip()
        if ":" not in stripped:
            raise LMStudioError(f"Expected '- key: value' line but got '{line}'.")
        key, value = stripped.split(":", 1)
        normalized_key = key.strip()
        if not normalized_key:
            raise LMStudioError(f"Inputs Markdown contained an empty key in line '{line}'.")
        values[normalized_key] = value.strip()
    if not values:
        raise LMStudioError("Inputs Markdown did not contain any 'key: value' lines.")
    return values


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


def _normalize_clip_id(value: str) -> str:
    normalized = value.strip().upper()
    if not CLIP_ID_PATTERN.fullmatch(normalized):
        raise LMStudioError(f"Invalid clip id returned by LM Studio: {value}")
    return validate_clip_id(normalized)


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
        path.unlink(missing_ok=True)


def _write_text(path: Path, content: str) -> None:
    ensure_dir(path.parent)
    text = content.rstrip() + "\n"
    path.write_text(text, encoding="utf-8")
