from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

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

    summary_payload = _call_json_task(
        client=client,
        system_prompt=_analysis_system_prompt(),
        user_prompt=_chapter_summary_user_prompt(project_slug, chapter_source),
    )
    project_summary_markdown = _require_string(summary_payload, "project_summary_markdown")
    chapter_summary_markdown = _require_string(summary_payload, "chapter_summary_markdown")

    project_summary_path = project_dir / "02_story_analysis" / "story_summary" / "project_summary.md"
    chapter_summary_path = (
        project_dir / "02_story_analysis" / "chapter_analysis" / f"{chapter_source.chapter_id}_summary.md"
    )
    _write_text(project_summary_path, project_summary_markdown)
    _write_text(chapter_summary_path, chapter_summary_markdown)
    written_files.extend([repo_relative(project_summary_path), repo_relative(chapter_summary_path)])

    character_payload = _call_json_task(
        client=client,
        system_prompt=_analysis_system_prompt(),
        user_prompt=_character_extraction_user_prompt(
            project_slug=project_slug,
            chapter_source=chapter_source,
            chapter_summary=chapter_summary_markdown,
        ),
    )
    character_index_markdown = _require_string(character_payload, "character_index_markdown")
    character_index_path = project_dir / "02_story_analysis" / "character_breakdowns" / "CHARACTER_INDEX.md"
    _write_text(character_index_path, character_index_markdown)
    written_files.append(repo_relative(character_index_path))

    for raw_character in _require_object_list(character_payload, "characters"):
        asset_id = _normalize_asset_id(
            _require_string(raw_character, "asset_id"),
            fallback_prefix="character",
        )
        filename = f"{asset_id}.md"
        markdown = _require_string(raw_character, "markdown")
        manual_description_required = _require_bool(raw_character, "manual_description_required", default=False)
        manual_description_reason = _require_string(
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
            manual_path = (
                project_dir / "01_source" / "character_descriptions" / f"{asset_id}_manual_description.md"
            )
            _write_text(
                manual_path,
                _manual_character_description_placeholder(
                    asset_id=asset_id,
                    reason=manual_description_reason,
                ),
            )
            written_files.append(repo_relative(manual_path))
            manual_requests.append(
                ManualCharacterDescriptionRequest(
                    asset_id=asset_id,
                    source_path=repo_relative(manual_path),
                    reason=manual_description_reason,
                )
            )

    environment_payload = _call_json_task(
        client=client,
        system_prompt=_analysis_system_prompt(),
        user_prompt=_environment_extraction_user_prompt(
            project_slug=project_slug,
            chapter_source=chapter_source,
            chapter_summary=chapter_summary_markdown,
        ),
    )
    environment_index_markdown = _require_string(environment_payload, "environment_index_markdown")
    environment_index_path = project_dir / "02_story_analysis" / "environment_breakdowns" / "ENVIRONMENT_INDEX.md"
    _write_text(environment_index_path, environment_index_markdown)
    written_files.append(repo_relative(environment_index_path))

    for raw_environment in _require_object_list(environment_payload, "environments"):
        asset_id = _normalize_asset_id(
            _require_string(raw_environment, "asset_id"),
            fallback_prefix="environment",
        )
        filename = f"{asset_id}.md"
        markdown = _require_string(raw_environment, "markdown")
        environment_path = project_dir / "02_story_analysis" / "environment_breakdowns" / filename
        _write_text(environment_path, markdown)
        written_files.append(repo_relative(environment_path))

    scene_payload = _call_json_task(
        client=client,
        system_prompt=_analysis_system_prompt(),
        user_prompt=_scene_decomposition_user_prompt(
            project_slug=project_slug,
            chapter_source=chapter_source,
            chapter_summary=chapter_summary_markdown,
            character_index_path=character_index_path,
            environment_index_path=environment_index_path,
        ),
    )
    scene_index_markdown = _require_string(scene_payload, "scene_index_markdown")
    scene_index_path = project_dir / "02_story_analysis" / "scene_breakdowns" / "SCENE_INDEX.md"
    _write_text(scene_index_path, scene_index_markdown)
    written_files.append(repo_relative(scene_index_path))

    scene_ids: list[str] = []
    for raw_scene in _require_object_list(scene_payload, "scenes"):
        scene_id = _normalize_scene_id(_require_string(raw_scene, "scene_id"))
        filename = f"{scene_id}.md"
        markdown = _require_string(raw_scene, "markdown")
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

    beat_payload = _call_json_task(
        client=client,
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
    updated_scene_markdown = _require_string(beat_payload, "updated_scene_markdown")
    beat_index_markdown = _require_string(beat_payload, "beat_index_markdown")
    _write_text(scene_path, updated_scene_markdown)
    written_files.append(repo_relative(scene_path))

    beat_index_path = beat_dir / "BEAT_INDEX.md"
    _write_text(beat_index_path, beat_index_markdown)
    written_files.append(repo_relative(beat_index_path))

    beat_ids: list[str] = []
    for raw_beat in _require_object_list(beat_payload, "beats"):
        beat_id = _normalize_beat_id(_require_string(raw_beat, "beat_id"))
        filename = f"{beat_id}.md"
        markdown = _require_string(raw_beat, "markdown")
        beat_path = beat_dir / filename
        _write_text(beat_path, markdown)
        written_files.append(repo_relative(beat_path))
        beat_ids.append(beat_id)

    clip_payload = _call_json_task(
        client=client,
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
    clip_roster_markdown = _require_string(clip_payload, "clip_roster_markdown")
    clip_dir = project_dir / "02_story_analysis" / "clip_plans" / scene_id
    ensure_dir(clip_dir)
    _prune_markdown_dir(clip_dir, keep_names=set())
    clip_roster_path = clip_dir / f"{scene_id}_clip_roster.md"
    _write_text(clip_roster_path, clip_roster_markdown)
    written_files.append(repo_relative(clip_roster_path))

    clip_ids: list[str] = []
    for raw_clip in _require_object_list(clip_payload, "clips"):
        clip_id = _normalize_clip_id(_require_string(raw_clip, "clip_id"))
        filename = f"{clip_id}.md"
        markdown = _require_string(raw_clip, "markdown")
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

    payload = _call_json_task(
        client=client,
        system_prompt=_analysis_system_prompt(),
        user_prompt=_shared_prompt_user_prompt(
            project_slug=project_slug,
            project_summary_path=project_summary_path,
            chapter_summary_path=chapter_summary_path,
            character_index_path=character_index_path,
            environment_index_path=environment_index_path,
        ),
    )

    written_files: list[str] = []
    for raw_prompt in _require_object_list(payload, "character_prompts"):
        draft = _structured_prompt_draft(raw_prompt)
        asset_id = _normalize_asset_id(draft.asset_id, fallback_prefix="character")
        prompt_path = (
            project_dir / "03_prompt_packages" / "characters" / asset_id / f"{asset_id}_ref_prompt.md"
        )
        write_prompt_package(
            prompt_path,
            _build_prompt_package(
                path=prompt_path,
                title=f"{asset_id} Character Reference Prompt",
                prompt_id=f"{asset_id}_ref_prompt",
                workflow_type="still.t2i.klein.distilled",
                draft=draft,
                sources=[
                    repo_relative(project_summary_path),
                    repo_relative(chapter_summary_path),
                    repo_relative(character_index_path),
                ],
            ),
        )
        written_files.append(repo_relative(prompt_path))

    for raw_prompt in _require_object_list(payload, "environment_prompts"):
        draft = _structured_prompt_draft(raw_prompt)
        asset_id = _normalize_asset_id(draft.asset_id, fallback_prefix="environment")
        prompt_path = (
            project_dir / "03_prompt_packages" / "environments" / asset_id / f"{asset_id}_ref_prompt.md"
        )
        write_prompt_package(
            prompt_path,
            _build_prompt_package(
                path=prompt_path,
                title=f"{asset_id} Environment Reference Prompt",
                prompt_id=f"{asset_id}_ref_prompt",
                workflow_type="still.t2i.klein.distilled",
                draft=draft,
                sources=[
                    repo_relative(project_summary_path),
                    repo_relative(chapter_summary_path),
                    repo_relative(environment_index_path),
                ],
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
            "Return only valid JSON.",
            "Do not use markdown fences.",
            "Preserve uncertainty instead of inventing hidden facts.",
            "When asked to write Markdown file contents, return complete Markdown strings that can be written directly to files.",
            "When asked to extract render-facing facts, focus on visible, continuity-relevant details.",
        ]
    )


def _chapter_summary_user_prompt(project_slug: str, chapter_source: _ChapterSource) -> str:
    return "\n\n".join(
        [
            f"Project slug: {project_slug}",
            f"Chapter id: {chapter_source.chapter_id}",
            "Task: write project summary plus chapter summary for later scene extraction.",
            "Return valid JSON only with keys:",
            "- project_summary_markdown",
            "- chapter_summary_markdown",
            "",
            "Requirements:",
            "- proper nouns are allowed",
            "- do not mention ComfyUI nodes or workflow patching",
            "- separate visual continuity facts from broad story summary",
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
            "Return valid JSON only with keys:",
            "- character_index_markdown",
            "- characters",
            "",
            "Each item in characters must be an object with keys:",
            "- asset_id",
            "- filename",
            "- markdown",
            "- manual_description_required",
            "- manual_description_reason",
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
            "Return valid JSON only with keys:",
            "- environment_index_markdown",
            "- environments",
            "",
            "Each item in environments must be an object with keys:",
            "- asset_id",
            "- filename",
            "- markdown",
            "",
            "Asset id rules:",
            "- lowercase snake_case",
            "- stable across later reruns",
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
            "Return valid JSON only with keys:",
            "- scene_index_markdown",
            "- scenes",
            "",
            "Each item in scenes must be an object with keys:",
            "- scene_id",
            "- filename",
            "- markdown",
            "",
            "Scene id rules:",
            "- use SC###",
            "- start at SC001 for this chapter",
            "",
            "Prefer dramatic and staging boundaries, not every paragraph break.",
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
            "Return valid JSON only with keys:",
            "- scene_id",
            "- updated_scene_markdown",
            "- beat_index_markdown",
            "- beats",
            "",
            "Each beat item must contain:",
            "- beat_id",
            "- filename",
            "- markdown",
            "",
            "Beat id rules:",
            "- use BT### within the scene",
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
            "Return valid JSON only with keys:",
            "- scene_id",
            "- clip_roster_markdown",
            "- clips",
            "",
            "Each clip item must contain:",
            "- clip_id",
            "- filename",
            "- markdown",
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


def _shared_prompt_user_prompt(
    *,
    project_slug: str,
    project_summary_path: Path,
    chapter_summary_path: Path,
    character_index_path: Path,
    environment_index_path: Path,
) -> str:
    character_breakdowns = _markdown_bundle(
        directory=character_index_path.parent,
        exclude_names={"CHARACTER_INDEX.md", "README.md"},
    )
    environment_breakdowns = _markdown_bundle(
        directory=environment_index_path.parent,
        exclude_names={"ENVIRONMENT_INDEX.md", "README.md"},
    )
    return "\n\n".join(
        [
            f"Project slug: {project_slug}",
            "Task: write reusable shared character and environment prompt drafts for stable local generation.",
            "Return valid JSON only with keys:",
            "- character_prompts",
            "- environment_prompts",
            "",
            "Each prompt object must contain:",
            "- asset_id",
            "- purpose",
            "- positive_prompt",
            "- negative_prompt",
            "- inputs",
            "- continuity_notes",
            "- repair_notes",
            "",
            "Rules:",
            "- purpose and inputs may use stable asset ids",
            "- final positive and negative prompt bodies should avoid proper nouns and use descriptive noun phrases",
            "- keep prompts concrete and visible",
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
            f"Environment index path: {repo_relative(environment_index_path)}",
            environment_index_path.read_text(encoding="utf-8"),
            "",
            "Environment breakdown files:",
            environment_breakdowns or "(none)",
        ]
    )


def _call_json_task(
    *,
    client: LMStudioClient,
    system_prompt: str,
    user_prompt: str,
) -> dict[str, object]:
    response = client.chat_completion(system_prompt=system_prompt, user_prompt=user_prompt, temperature=0.2)
    payload = _parse_llm_json(response)
    if not isinstance(payload, dict):
        raise LMStudioError("LM Studio task response must be a JSON object.")
    return payload


def _structured_prompt_draft(payload: dict[str, object]) -> _StructuredPromptDraft:
    inputs = payload.get("inputs")
    if not isinstance(inputs, dict):
        raise LMStudioError("Shared prompt draft inputs must be a JSON object.")
    normalized_inputs = {str(key): "" if value is None else str(value) for key, value in inputs.items()}
    return _StructuredPromptDraft(
        asset_id=_require_string(payload, "asset_id"),
        purpose=_require_string(payload, "purpose"),
        positive_prompt=_require_string(payload, "positive_prompt"),
        negative_prompt=_require_string(payload, "negative_prompt"),
        inputs=normalized_inputs,
        continuity_notes=_require_string_list(payload, "continuity_notes"),
        repair_notes=_require_string_list(payload, "repair_notes"),
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


def _parse_llm_json(response: str) -> dict[str, object]:
    cleaned = response.strip()
    if cleaned.startswith("```"):
        cleaned = cleaned.strip("`")
        if cleaned.startswith("json"):
            cleaned = cleaned[4:].strip()

    try:
        payload = json.loads(cleaned)
    except json.JSONDecodeError:
        start = cleaned.find("{")
        end = cleaned.rfind("}")
        if start == -1 or end == -1 or end <= start:
            raise LMStudioError("LM Studio did not return valid JSON.")
        payload = json.loads(cleaned[start : end + 1])

    if not isinstance(payload, dict):
        raise LMStudioError("LM Studio task response must be a JSON object.")
    return payload


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


def _normalize_markdown_filename(value: object, *, fallback: str) -> str:
    if isinstance(value, str) and value.strip():
        candidate = Path(value.strip()).name
    else:
        candidate = fallback
    if not candidate.lower().endswith(".md"):
        candidate = f"{candidate}.md"
    return candidate


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


def _require_string(
    payload: dict[str, object],
    key: str,
    *,
    allow_empty: bool = False,
) -> str:
    value = payload.get(key)
    if not isinstance(value, str):
        raise LMStudioError(f"Expected non-empty string for '{key}'.")
    stripped = value.strip()
    if not stripped and not allow_empty:
        raise LMStudioError(f"Expected non-empty string for '{key}'.")
    return stripped


def _require_bool(payload: dict[str, object], key: str, *, default: bool | None = None) -> bool:
    value = payload.get(key, default)
    if not isinstance(value, bool):
        raise LMStudioError(f"Expected boolean for '{key}'.")
    return value


def _require_string_list(payload: dict[str, object], key: str) -> list[str]:
    value = payload.get(key)
    if not isinstance(value, list):
        raise LMStudioError(f"Expected list for '{key}'.")
    items = [item.strip() for item in value if isinstance(item, str) and item.strip()]
    if not items:
        raise LMStudioError(f"Expected at least one string value for '{key}'.")
    return items


def _require_object_list(payload: dict[str, object], key: str) -> list[dict[str, object]]:
    value = payload.get(key)
    if not isinstance(value, list):
        raise LMStudioError(f"Expected list for '{key}'.")
    items: list[dict[str, object]] = []
    for item in value:
        if not isinstance(item, dict):
            raise LMStudioError(f"Expected object items in '{key}'.")
        items.append(item)
    if not items:
        raise LMStudioError(f"Expected at least one object in '{key}'.")
    return items


def _write_text(path: Path, content: str) -> None:
    ensure_dir(path.parent)
    text = content.rstrip() + "\n"
    path.write_text(text, encoding="utf-8")
