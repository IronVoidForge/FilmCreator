from __future__ import annotations

import re
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from types import SimpleNamespace
from typing import Iterable

from .core.json_io import read_json
from .core.paths import ROOT, repo_relative
from .lmstudio_client import LMStudioCheckSummary, LMStudioClient, LMStudioError
from .prompt_package import PromptPackage, parse_prompt_package, write_prompt_package
from .scaffold import create_clip, create_scene
from .settings import load_runtime_settings
from .state import load_clip_state, write_clip_state

PACKET_START_TAG = "[[FILMCREATOR_PACKET]]"
PACKET_END_TAG = "[[/FILMCREATOR_PACKET]]"
SECTION_END_TAG = "[[/SECTION]]"
SECTION_TAG_PATTERN = re.compile(r"^\[\[SECTION ([a-z0-9_]+)\]\]$", re.IGNORECASE)
PACKET_VERSION = "1"
MINIMUM_VIABLE_STAGES = {"keyframe", "cut_motion"}


@dataclass(frozen=True)
class PromptWriteResult:
    clip_id: str
    stage: str
    path: str
    workflow_type: str
    model: str
    duration_seconds: float

    def to_dict(self) -> dict[str, object]:
        return {
            "clip_id": self.clip_id,
            "stage": self.stage,
            "path": self.path,
            "workflow_type": self.workflow_type,
            "model": self.model,
            "duration_seconds": self.duration_seconds,
        }


@dataclass(frozen=True)
class PromptWriteFailure:
    clip_id: str
    stage: str
    reason: str
    log_path: str
    failure_artifact_path: str

    def to_dict(self) -> dict[str, object]:
        return {
            "clip_id": self.clip_id,
            "stage": self.stage,
            "reason": self.reason,
            "log_path": self.log_path,
            "failure_artifact_path": self.failure_artifact_path,
        }


@dataclass(frozen=True)
class PromptWriteSummary:
    project_slug: str
    scene_id: str
    clip_ids: list[str]
    model: str
    written_files: list[PromptWriteResult]
    warnings: list[str]
    failures: list[PromptWriteFailure]
    failed_clips: list[str]

    def to_dict(self) -> dict[str, object]:
        return {
            "project_slug": self.project_slug,
            "scene_id": self.scene_id,
            "clip_ids": self.clip_ids,
            "model": self.model,
            "written_files": [item.to_dict() for item in self.written_files],
            "warnings": self.warnings,
            "failures": [item.to_dict() for item in self.failures],
            "failed_clips": self.failed_clips,
        }


@dataclass(frozen=True)
class PromptTarget:
    stage: str
    path: Path
    title: str
    prompt_id: str
    workflow_type: str
    guidance: str
    sources: list[str]


@dataclass(frozen=True)
class _PacketDocument:
    metadata: dict[str, str]
    sections: dict[str, str]


def lmstudio_check() -> LMStudioCheckSummary:
    settings = load_runtime_settings()
    client = LMStudioClient(settings)
    return client.check()


def write_prompts(
    *,
    project_slug: str,
    scene_id: str,
    clip_id: str | None = None,
) -> PromptWriteSummary:
    started = time.perf_counter()
    settings = load_runtime_settings()
    client = LMStudioClient(settings)
    resolved_model = client.resolve_model()

    target_clip_ids = _resolve_clip_ids(project_slug, scene_id, clip_id)
    written_files: list[PromptWriteResult] = []
    warnings: list[str] = []
    failures: list[PromptWriteFailure] = []
    failed_clips: list[str] = []

    total_targets = len(target_clip_ids) * 4
    completed_targets = 0
    successful_targets = 0
    failed_targets = 0
    print(f"[authoring] Starting clip prompt writing for {project_slug}/{scene_id}: {len(target_clip_ids)} clips, {total_targets} targets total...")

    for current_clip_id in target_clip_ids:
        clip_context = _load_clip_context(project_slug, scene_id, current_clip_id)
        targets = list(_prompt_targets(project_slug, scene_id, current_clip_id))
        clip_successful_stages: set[str] = set()
        clip_failures: list[PromptWriteFailure] = []
        clip_completed = 0
        clip_succeeded = 0

        for target in targets:
            completed_targets += 1
            clip_completed += 1
            existing = _load_existing_prompt(target.path)
            print(f"[authoring] Clip prompt {completed_targets}/{total_targets} started: {scene_id}/{current_clip_id} {target.stage}")
            package, local_warnings, log_path, duration_seconds = _write_prompt_target_with_retries(
                client=client,
                project_slug=project_slug,
                scene_id=scene_id,
                clip_id=current_clip_id,
                target=target,
                clip_context=clip_context,
                existing_prompt=existing,
            )
            warnings.extend(f"{current_clip_id}:{target.stage}: {warning}" for warning in local_warnings)
            if package is None:
                failure_reason = local_warnings[-1] if local_warnings else "LM Studio prompt-writing retries exhausted."
                failure_path = _write_prompt_failure_artifact(
                    project_slug=project_slug,
                    scene_id=scene_id,
                    clip_id=current_clip_id,
                    stage=target.stage,
                    reason=failure_reason,
                )
                failure = PromptWriteFailure(
                    clip_id=current_clip_id,
                    stage=target.stage,
                    reason=failure_reason,
                    log_path=repo_relative(log_path),
                    failure_artifact_path=repo_relative(failure_path),
                )
                failures.append(failure)
                clip_failures.append(failure)
                failed_targets += 1
                print(f"[authoring] Clip prompt {scene_id}/{current_clip_id} {target.stage} failed after retries; continuing")
                continue

            write_prompt_package(target.path, package)
            written_files.append(
                PromptWriteResult(
                    clip_id=current_clip_id,
                    stage=target.stage,
                    path=target.path.relative_to(ROOT).as_posix(),
                    workflow_type=target.workflow_type,
                    model=resolved_model,
                    duration_seconds=duration_seconds,
                )
            )
            clip_successful_stages.add(target.stage)
            successful_targets += 1
            clip_succeeded += 1
            print(f"[authoring] Clip prompt {scene_id}/{current_clip_id} {target.stage} finished in {duration_seconds:.1f}s")

        missing_required = sorted(MINIMUM_VIABLE_STAGES - clip_successful_stages)
        if missing_required:
            failed_clips.append(current_clip_id)
            warnings.append(
                f"{current_clip_id}: failed minimum viable stage set; missing {', '.join(missing_required)}"
            )
            print(
                f"[authoring] Clip {scene_id}/{current_clip_id} failed minimum viable set because it is missing {', '.join(missing_required)}"
            )
        else:
            _record_prompt_packages_in_clip_state(
                project_slug=project_slug,
                scene_id=scene_id,
                clip_id=current_clip_id,
                targets=targets,
            )
        print(
            f"[authoring] Clip {scene_id}/{current_clip_id} summary: {clip_succeeded}/{clip_completed} targets succeeded, {len(clip_failures)} failed"
        )
        print(
            f"[authoring] Clip prompt progress: {completed_targets}/{total_targets} complete, {successful_targets} succeeded, {failed_targets} failed"
        )

    elapsed = time.perf_counter() - started
    print(f"[authoring] Finished clip prompt writing in {elapsed:.1f}s")
    return PromptWriteSummary(
        project_slug=project_slug,
        scene_id=scene_id,
        clip_ids=target_clip_ids,
        model=resolved_model,
        written_files=written_files,
        warnings=warnings,
        failures=failures,
        failed_clips=failed_clips,
    )


def _resolve_clip_ids(project_slug: str, scene_id: str, clip_id: str | None) -> list[str]:
    if clip_id:
        create_clip(project_slug, scene_id, clip_id)
        return [clip_id]

    scene_dir = create_scene(project_slug, scene_id)
    scene_state_path = scene_dir / "scene_state.json"
    if scene_state_path.exists():
        scene_state = read_json(scene_state_path)
        clip_ids = list(scene_state.get("clip_ids", []))
        if clip_ids:
            return sorted(clip_ids)

    clips_dir = scene_dir / "clips"
    if clips_dir.exists():
        found = sorted(path.name for path in clips_dir.iterdir() if path.is_dir() and path.name.startswith("CL"))
        if found:
            return found

    raise FileNotFoundError(f"No clips were found for {project_slug}/{scene_id}")


def _load_clip_context(project_slug: str, scene_id: str, clip_id: str) -> str:
    clip_dir = create_clip(project_slug, scene_id, clip_id)
    project_root = ROOT / "projects" / project_slug
    project_summary_path = project_root / "02_story_analysis" / "story_summary" / "project_summary.md"
    project_summary = project_summary_path.read_text(encoding="utf-8") if project_summary_path.exists() else ""
    chapter_summaries_dir = project_root / "02_story_analysis" / "chapter_analysis"
    chapter_summaries = _markdown_bundle(
        chapter_summaries_dir,
        exclude_names={"README.md"},
    )
    character_index_path = project_root / "02_story_analysis" / "character_breakdowns" / "CHARACTER_INDEX.md"
    character_index = character_index_path.read_text(encoding="utf-8") if character_index_path.exists() else ""
    environment_index_path = project_root / "02_story_analysis" / "environment_breakdowns" / "ENVIRONMENT_INDEX.md"
    environment_index = environment_index_path.read_text(encoding="utf-8") if environment_index_path.exists() else ""
    clip_plan_path = ROOT / "projects" / project_slug / "02_story_analysis" / "clip_plans" / scene_id / f"{clip_id}.md"
    clip_plan = clip_plan_path.read_text(encoding="utf-8") if clip_plan_path.exists() else ""
    scene_breakdown_path = project_root / "02_story_analysis" / "scene_breakdowns" / f"{scene_id}.md"
    scene_breakdown = scene_breakdown_path.read_text(encoding="utf-8") if scene_breakdown_path.exists() else ""
    clip_roster_path = project_root / "02_story_analysis" / "clip_plans" / scene_id / f"{scene_id}_clip_roster.md"
    clip_roster = clip_roster_path.read_text(encoding="utf-8") if clip_roster_path.exists() else ""
    beat_bundle_dir = project_root / "02_story_analysis" / "beat_bundles" / scene_id
    beat_bundles = _markdown_bundle(
        beat_bundle_dir,
        exclude_names={"BEAT_INDEX.md", "README.md"},
    )
    clip_state_path = clip_dir / "clip_state.json"
    clip_state = clip_state_path.read_text(encoding="utf-8") if clip_state_path.exists() else ""

    sections: list[str] = []
    if project_summary.strip():
        sections.extend(["## Project Summary", project_summary.strip()])
    if chapter_summaries.strip():
        sections.extend(["## Chapter Summaries", chapter_summaries.strip()])
    if character_index.strip():
        sections.extend(["## Character Index", character_index.strip()])
    if environment_index.strip():
        sections.extend(["## Environment Index", environment_index.strip()])
    if clip_plan.strip():
        sections.extend(["## Clip Plan", clip_plan.strip()])
    if scene_breakdown.strip():
        sections.extend(["## Scene Breakdown", scene_breakdown.strip()])
    if beat_bundles.strip():
        sections.extend(["## Beat Bundles", beat_bundles.strip()])
    if clip_roster.strip():
        sections.extend(["## Clip Roster", clip_roster.strip()])
    sections.extend(["## Clip State", clip_state.strip() or "(missing)"])
    return "\n\n".join(sections).strip()


def _prompt_targets(project_slug: str, scene_id: str, clip_id: str) -> Iterable[PromptTarget]:
    project_root = ROOT / "projects" / project_slug
    clip_plan_source = f"projects/{project_slug}/02_story_analysis/clip_plans/{scene_id}/{clip_id}.md"
    scene_breakdown_source = f"projects/{project_slug}/02_story_analysis/scene_breakdowns/{scene_id}.md"
    clip_roster_source = f"projects/{project_slug}/02_story_analysis/clip_plans/{scene_id}/{scene_id}_clip_roster.md"
    character_index_source = f"projects/{project_slug}/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md"
    environment_index_source = f"projects/{project_slug}/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md"
    project_summary_source = f"projects/{project_slug}/02_story_analysis/story_summary/project_summary.md"
    base_sources = [
        clip_plan_source,
        scene_breakdown_source,
        clip_roster_source,
        character_index_source,
        environment_index_source,
        project_summary_source,
    ]
    return [
        PromptTarget(
            stage="scene_stage",
            path=project_root / "03_prompt_packages" / "scenes" / scene_id / clip_id / f"{scene_id}_{clip_id}_scene_stage_prompt.md",
            title=f"{scene_id} {clip_id} Scene Stage Prompt",
            prompt_id=f"{scene_id}_{clip_id}_scene_stage_prompt",
            workflow_type="authoring.scene_stage",
            guidance=(
                "Describe staging intent, subject placement, environmental context, and the intended visible opening frame setup. "
                "This is authoring-only and should not read like a render prompt for a model."
            ),
            sources=base_sources,
        ),
        PromptTarget(
            stage="keyframe",
            path=project_root / "03_prompt_packages" / "keyframes" / scene_id / clip_id / f"{scene_id}_{clip_id}_keyframe_prompt.md",
            title=f"{scene_id} {clip_id} Keyframe Prompt",
            prompt_id=f"{scene_id}_{clip_id}_keyframe_prompt",
            workflow_type="still.scene_build.four_ref.klein.distilled",
            guidance=(
                "Write the exact visible state at cut start as a single frozen still. "
                "Avoid proper nouns. Use descriptive noun phrases only."
            ),
            sources=base_sources,
        ),
        PromptTarget(
            stage="still_fix",
            path=project_root / "03_prompt_packages" / "fixes" / scene_id / clip_id / f"{scene_id}_{clip_id}_fix_01_prompt.md",
            title=f"{scene_id} {clip_id} Fix 01 Prompt",
            prompt_id=f"{scene_id}_{clip_id}_fix_01_prompt",
            workflow_type="still.scene_insert.two_ref.klein.distilled",
            guidance=(
                "Write a corrective still-generation prompt that preserves composition and look while fixing local issues. "
                "Assume image1 is the approved still base and image2 is a secondary reference when needed."
            ),
            sources=base_sources,
        ),
        PromptTarget(
            stage="cut_motion",
            path=project_root / "03_prompt_packages" / "cut_motion" / scene_id / clip_id / f"{scene_id}_{clip_id}_cut_motion_prompt.md",
            title=f"{scene_id} {clip_id} Cut Motion Prompt",
            prompt_id=f"{scene_id}_{clip_id}_cut_motion_prompt",
            workflow_type="video.cut_motion.wan.i2v",
            guidance=(
                "Write a short-cut motion prompt that starts from the approved opening frame. "
                "Preserve the keyframe lighting and grade by default. Focus on visible motion, camera behavior, and environment change."
            ),
            sources=base_sources,
        ),
    ]


def _markdown_bundle(directory: Path, *, exclude_names: set[str]) -> str:
    if not directory.exists():
        return ""
    chunks: list[str] = []
    for path in sorted(directory.glob("*.md")):
        if path.name in exclude_names:
            continue
        chunks.append(f"## {path.name}\n{path.read_text(encoding='utf-8').strip()}")
    return "\n\n".join(chunks)


def _load_existing_prompt(path: Path) -> PromptPackage | None:
    if not path.exists():
        return None
    return parse_prompt_package(path)


def _authoring_system_prompt(target: PromptTarget, degraded: bool = False) -> str:
    lines = [
        "You are writing one FilmCreator prompt package for a local generation pipeline.",
        "Your first output line must be exactly [[FILMCREATOR_PACKET]].",
        "Your last output line must be exactly [[/FILMCREATOR_PACKET]].",
        "Return exactly one FILMCREATOR packet in Markdown.",
        "Do not return JSON.",
        "Do not use markdown fences.",
        "Do not add commentary before or after the packet.",
        "Do not omit the outer packet envelope.",
        f"Target stage: {target.stage}",
        f"Stage guidance: {target.guidance}",
        "Use descriptive noun phrases and avoid proper nouns in prompt text.",
    ]
    if degraded:
        lines.extend(
            [
                "Keep all sections short, concrete, and non-empty.",
                "If uncertain, keep inputs minimal and preserve useful continuity notes.",
            ]
        )
    else:
        lines.extend(
            [
                "Keep duration and workflow metadata in inputs_markdown, not in the prompt body.",
                "Follow the requested section names exactly.",
            ]
        )
    return "\n".join(lines)


def _authoring_user_prompt(
    *,
    project_slug: str,
    scene_id: str,
    clip_id: str,
    target: PromptTarget,
    clip_context: str,
    existing_prompt: PromptPackage | None,
    degraded: bool = False,
) -> str:
    existing_markdown = existing_prompt.to_markdown() if existing_prompt else "(none)"
    request = "Write improved content for this canonical prompt package."
    if degraded:
        request = "Write a compact but valid version of this prompt package. Keep every required section non-empty."
    return "\n\n".join(
        [
            f"Project: {project_slug}",
            f"Scene: {scene_id}",
            f"Clip: {clip_id}",
            f"Prompt title: {target.title}",
            f"Prompt id: {target.prompt_id}",
            f"Workflow type: {target.workflow_type}",
            request,
            "Output rules:",
            f"1. First line must be {PACKET_START_TAG}",
            f"2. Last line must be {PACKET_END_TAG}",
            "3. No text before the first line",
            "4. No text after the last line",
            "5. Every required section must appear exactly once",
            "",
            "Use this exact packet envelope and section names:",
            PACKET_START_TAG,
            "task: clip_prompt",
            f"stage: {target.stage}",
            f"version: {PACKET_VERSION}",
            "",
            "[[SECTION purpose]]",
            "...purpose text...",
            SECTION_END_TAG,
            "",
            "[[SECTION positive_prompt]]",
            "...positive prompt text...",
            SECTION_END_TAG,
            "",
            "[[SECTION negative_prompt]]",
            "...negative prompt text...",
            SECTION_END_TAG,
            "",
            "[[SECTION inputs_markdown]]",
            "- key: value",
            SECTION_END_TAG,
            "",
            "[[SECTION continuity_notes_markdown]]",
            "- note",
            SECTION_END_TAG,
            "",
            "[[SECTION repair_notes_markdown]]",
            "- note",
            SECTION_END_TAG,
            PACKET_END_TAG,
            "",
            "Clip context:",
            clip_context,
            "",
            "Existing prompt draft:",
            existing_markdown,
        ]
    )


def _write_prompt_target_with_retries(
    *,
    client: LMStudioClient,
    project_slug: str,
    scene_id: str,
    clip_id: str,
    target: PromptTarget,
    clip_context: str,
    existing_prompt: PromptPackage | None,
) -> tuple[PromptPackage | None, list[str], Path, float]:
    warnings: list[str] = []
    latest_log_path: Path | None = None
    target_started = time.perf_counter()
    for attempt_index, (kind, degraded) in enumerate([("normal", False), ("same_prompt_retry", False), ("degraded_retry", True)], start=1):
        system_prompt = _authoring_system_prompt(target, degraded=degraded)
        user_prompt = _authoring_user_prompt(
            project_slug=project_slug,
            scene_id=scene_id,
            clip_id=clip_id,
            target=target,
            clip_context=clip_context,
            existing_prompt=existing_prompt,
            degraded=degraded,
        )
        if kind != "normal":
            reason = warnings[-1] if warnings else "prior attempt failed"
            print(f"[authoring] Retrying {scene_id}/{clip_id} {target.stage} with {kind} because {reason}")
        result = _chat_completion_result(
            client=client,
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            temperature=0.2,
        )
        latest_log_path = _write_prompt_exchange_log(
            project_slug=project_slug,
            scene_id=scene_id,
            clip_id=clip_id,
            target=target,
            kind=kind,
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            response=result.text,
        )
        if not result.is_success:
            warnings.append(result.error_message or f"{kind} returned {result.status}")
            continue
        try:
            package = _build_prompt_package_from_packet(
                response=result.text,
                target=target,
                existing_prompt=existing_prompt,
            )
            return package, warnings, latest_log_path, time.perf_counter() - target_started
        except LMStudioError as exc:
            warnings.append(str(exc))
            continue

    if latest_log_path is None:
        latest_log_path = _write_prompt_exchange_log(
            project_slug=project_slug,
            scene_id=scene_id,
            clip_id=clip_id,
            target=target,
            kind="failed_without_attempt",
            system_prompt="",
            user_prompt="",
            response="",
        )
    return None, warnings, latest_log_path, time.perf_counter() - target_started


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


def _write_prompt_exchange_log(
    *,
    project_slug: str,
    scene_id: str,
    clip_id: str,
    target: PromptTarget,
    kind: str,
    system_prompt: str,
    user_prompt: str,
    response: str,
) -> Path:
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    path = (
        ROOT
        / "projects"
        / project_slug
        / "03_prompt_packages"
        / "logs"
        / scene_id
        / clip_id
        / f"{timestamp}_{target.stage}_{kind}.md"
    )
    body = "\n".join(
        [
            "# FilmCreator Prompt Writing Exchange",
            f"- timestamp_utc: {datetime.now(timezone.utc).isoformat()}",
            f"- stage: {target.stage}",
            f"- clip_id: {clip_id}",
            f"- retry_kind: {kind}",
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
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body + "\n", encoding="utf-8")
    return path


def _write_prompt_failure_artifact(
    *,
    project_slug: str,
    scene_id: str,
    clip_id: str,
    stage: str,
    reason: str,
) -> Path:
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    path = (
        ROOT
        / "projects"
        / project_slug
        / "03_prompt_packages"
        / "logs"
        / scene_id
        / clip_id
        / "failures"
        / f"{timestamp}_{stage}.md"
    )
    body = "\n".join(
        [
            "# FilmCreator Prompt Writing Failure",
            f"- timestamp_utc: {datetime.now(timezone.utc).isoformat()}",
            f"- scene_id: {scene_id}",
            f"- clip_id: {clip_id}",
            f"- stage: {stage}",
            "",
            "## Reason",
            reason,
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body + "\n", encoding="utf-8")
    return path


def _build_prompt_package_from_packet(
    *,
    response: str,
    target: PromptTarget,
    existing_prompt: PromptPackage | None,
) -> PromptPackage:
    packet = _parse_prompt_packet(response)
    purpose = _require_section(packet, "purpose")
    positive_prompt = _require_section(packet, "positive_prompt")
    negative_prompt = _require_section(packet, "negative_prompt")
    continuity_notes = _parse_markdown_list(_require_section(packet, "continuity_notes_markdown"))
    repair_notes = _parse_markdown_list(_require_section(packet, "repair_notes_markdown"))
    inputs = _merge_inputs_from_markdown(existing_prompt.inputs if existing_prompt else {}, _require_section(packet, "inputs_markdown"))
    inputs_markdown = "\n".join(f"- {key}: {value}" for key, value in inputs.items())

    return PromptPackage(
        path=target.path,
        title=target.title,
        prompt_id=target.prompt_id,
        purpose=purpose,
        workflow_type=target.workflow_type,
        positive_prompt=positive_prompt,
        negative_prompt=negative_prompt,
        inputs_markdown=inputs_markdown,
        continuity_notes_markdown="\n".join(f"- {item}" for item in continuity_notes),
        repair_notes_markdown="\n".join(f"- {item}" for item in repair_notes),
        sources_markdown=_sources_markdown(existing_prompt, target),
    )


def _parse_prompt_packet(response: str) -> _PacketDocument:
    cleaned = response.strip()
    if not cleaned:
        raise LMStudioError("LM Studio returned an empty prompt-writing response.")
    cleaned = _strip_markdown_fences(cleaned)
    packet_body = _extract_packet_body(cleaned)
    return _parse_packet_body(packet_body)


def _strip_markdown_fences(text: str) -> str:
    cleaned = text.strip()
    if not cleaned.startswith("```"):
        return cleaned
    lines = cleaned.splitlines()
    if lines and lines[0].startswith("```"):
        lines = lines[1:]
    if lines and lines[-1].startswith("```"):
        lines = lines[:-1]
    return "\n".join(lines).strip()


def _extract_packet_body(response: str) -> str:
    lines = response.splitlines()
    start_index = next((index for index, line in enumerate(lines) if line.strip() == PACKET_START_TAG), -1)
    end_index = next((index for index in range(len(lines) - 1, -1, -1) if lines[index].strip() == PACKET_END_TAG), -1)
    if start_index != -1 and end_index != -1 and end_index > start_index:
        return "\n".join(lines[start_index + 1 : end_index]).strip()

    has_sections = any(SECTION_TAG_PATTERN.fullmatch(line.strip()) for line in lines)
    if has_sections:
        salvaged = "\n".join(
            [
                "task: clip_prompt",
                f"version: {PACKET_VERSION}",
                *lines,
            ]
        )
        return salvaged.strip()

    raise LMStudioError("Prompt-writing response did not include a FILMCREATOR packet envelope.")


def _parse_packet_body(packet_body: str) -> _PacketDocument:
    metadata: dict[str, str] = {}
    sections: dict[str, str] = {}
    lines = packet_body.splitlines()
    index = 0
    while index < len(lines):
        stripped = lines[index].strip()
        if not stripped:
            index += 1
            continue
        section_match = SECTION_TAG_PATTERN.fullmatch(stripped)
        if section_match:
            section_name = section_match.group(1).lower()
            section_lines, index = _collect_section_block(lines, index)
            sections[section_name] = "\n".join(section_lines).strip()
            continue
        if ":" in stripped:
            key, value = stripped.split(":", 1)
            metadata[key.strip().lower()] = value.strip()
            index += 1
            continue
        index += 1
    if metadata.get("task") != "clip_prompt":
        raise LMStudioError("Prompt-writing response packet is missing task: clip_prompt.")
    if metadata.get("version") != PACKET_VERSION:
        raise LMStudioError("Prompt-writing response packet has an unexpected version.")
    return _PacketDocument(metadata=metadata, sections=sections)


def _collect_section_block(lines: list[str], start_index: int) -> tuple[list[str], int]:
    body: list[str] = []
    index = start_index + 1
    while index < len(lines):
        stripped = lines[index].strip()
        if stripped == SECTION_END_TAG:
            return body, index + 1
        if stripped.startswith("[[SECTION ") and stripped.endswith("]]"):
            return body, index
        body.append(lines[index])
        index += 1
    return body, index


def _require_section(packet: _PacketDocument, name: str) -> str:
    value = packet.sections.get(name.lower(), "").strip()
    if not value:
        raise LMStudioError(f"Prompt-writing packet is missing required section '{name}'.")
    return value


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
        raise LMStudioError("Expected at least one list item in markdown section.")
    return items


def _sources_markdown(existing_prompt: PromptPackage | None, target: PromptTarget) -> str:
    merged: list[str] = []
    for source in target.sources:
        if source not in merged:
            merged.append(source)
    if existing_prompt:
        for source in existing_prompt.sources:
            if source not in merged:
                merged.append(source)
    return "\n".join(f"- {source}" for source in merged)


def _merge_inputs_from_markdown(existing_inputs: dict[str, str], markdown: str) -> dict[str, str]:
    merged = dict(existing_inputs)
    parsed = _parse_markdown_key_value_items(markdown)
    merged.update(parsed)
    if not merged:
        merged = {"context": "generated_from_clip_context"}
    return merged


def _parse_markdown_key_value_items(markdown: str) -> dict[str, str]:
    values: dict[str, str] = {}
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
        if current_key is not None:
            values[current_key] = f"{values[current_key]}\n{stripped}" if values[current_key] else stripped
        else:
            values[f"note_{len(values) + 1}"] = stripped
            current_key = f"note_{len(values)}"
    if not values:
        values = {"context": "generated_from_clip_context"}
    return values


def _record_prompt_packages_in_clip_state(
    *,
    project_slug: str,
    scene_id: str,
    clip_id: str,
    targets: Iterable[PromptTarget],
) -> None:
    clip_state = load_clip_state(project_slug, scene_id, clip_id)
    inputs = clip_state.setdefault("inputs", {})

    for target in targets:
        if not target.path.exists():
            continue
        prompt_value = repo_relative(target.path)
        if target.stage == "scene_stage":
            inputs["scene_stage_prompt_package"] = prompt_value
            inputs["scene_prompt_package"] = prompt_value
        elif target.stage == "keyframe":
            inputs["keyframe_prompt_package"] = prompt_value
        elif target.stage == "still_fix":
            fix_prompts = inputs.setdefault("fix_prompt_packages", [])
            if prompt_value not in fix_prompts:
                fix_prompts.append(prompt_value)
        elif target.stage == "cut_motion":
            inputs["cut_motion_prompt_package"] = prompt_value
            inputs["video_prompt_package"] = prompt_value

    write_clip_state(project_slug, scene_id, clip_id, clip_state)
