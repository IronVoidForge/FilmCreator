from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from .common import ROOT, read_json, repo_relative
from .lmstudio_client import LMStudioCheckSummary, LMStudioClient, LMStudioError
from .prompt_package import PromptPackage, parse_prompt_package, write_prompt_package
from .scaffold import create_clip, create_scene
from .settings import load_runtime_settings
from .state import load_clip_state, write_clip_state


@dataclass(frozen=True)
class PromptWriteResult:
    stage: str
    path: str
    workflow_type: str
    model: str

    def to_dict(self) -> dict[str, object]:
        return {
            "stage": self.stage,
            "path": self.path,
            "workflow_type": self.workflow_type,
            "model": self.model,
        }


@dataclass(frozen=True)
class PromptWriteSummary:
    project_slug: str
    scene_id: str
    clip_ids: list[str]
    model: str
    written_files: list[PromptWriteResult]

    def to_dict(self) -> dict[str, object]:
        return {
            "project_slug": self.project_slug,
            "scene_id": self.scene_id,
            "clip_ids": self.clip_ids,
            "model": self.model,
            "written_files": [item.to_dict() for item in self.written_files],
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
    settings = load_runtime_settings()
    client = LMStudioClient(settings)
    resolved_model = client.resolve_model()

    target_clip_ids = _resolve_clip_ids(project_slug, scene_id, clip_id)
    written_files: list[PromptWriteResult] = []

    for current_clip_id in target_clip_ids:
        clip_context = _load_clip_context(project_slug, scene_id, current_clip_id)
        targets = list(_prompt_targets(project_slug, scene_id, current_clip_id))
        for target in targets:
            existing = _load_existing_prompt(target.path)
            response = client.chat_completion(
                system_prompt=_authoring_system_prompt(target),
                user_prompt=_authoring_user_prompt(
                    project_slug=project_slug,
                    scene_id=scene_id,
                    clip_id=current_clip_id,
                    target=target,
                    clip_context=clip_context,
                    existing_prompt=existing,
                ),
            )
            package = _build_prompt_package_from_llm(
                response=response,
                target=target,
                existing_prompt=existing,
            )
            write_prompt_package(target.path, package)
            written_files.append(
                PromptWriteResult(
                    stage=target.stage,
                    path=target.path.relative_to(ROOT).as_posix(),
                    workflow_type=target.workflow_type,
                    model=resolved_model,
                )
            )
        _record_prompt_packages_in_clip_state(
            project_slug=project_slug,
            scene_id=scene_id,
            clip_id=current_clip_id,
            targets=targets,
        )

    return PromptWriteSummary(
        project_slug=project_slug,
        scene_id=scene_id,
        clip_ids=target_clip_ids,
        model=resolved_model,
        written_files=written_files,
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
    clip_plan_path = ROOT / "projects" / project_slug / "02_story_analysis" / "clip_plans" / scene_id / f"{clip_id}.md"
    clip_plan = clip_plan_path.read_text(encoding="utf-8") if clip_plan_path.exists() else ""
    scene_breakdown_path = project_root / "02_story_analysis" / "scene_breakdowns" / f"{scene_id}.md"
    scene_breakdown = scene_breakdown_path.read_text(encoding="utf-8") if scene_breakdown_path.exists() else ""
    clip_roster_path = project_root / "02_story_analysis" / "clip_plans" / scene_id / f"{scene_id}_clip_roster.md"
    clip_roster = clip_roster_path.read_text(encoding="utf-8") if clip_roster_path.exists() else ""
    clip_state_path = clip_dir / "clip_state.json"
    clip_state = clip_state_path.read_text(encoding="utf-8") if clip_state_path.exists() else ""

    sections: list[str] = []
    if clip_plan.strip():
        sections.extend(["## Clip Plan", clip_plan.strip()])
    if scene_breakdown.strip():
        sections.extend(["## Scene Breakdown", scene_breakdown.strip()])
    if clip_roster.strip():
        sections.extend(["## Clip Roster", clip_roster.strip()])
    sections.extend(["## Clip State", clip_state.strip() or "(missing)"])
    return "\n\n".join(sections).strip()


def _prompt_targets(project_slug: str, scene_id: str, clip_id: str) -> Iterable[PromptTarget]:
    project_root = ROOT / "projects" / project_slug
    clip_plan_source = f"projects/{project_slug}/02_story_analysis/clip_plans/{scene_id}/{clip_id}.md"
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
            sources=[clip_plan_source],
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
            sources=[clip_plan_source],
        ),
        PromptTarget(
            stage="still_fix",
            path=project_root / "03_prompt_packages" / "fixes" / scene_id / clip_id / f"{scene_id}_{clip_id}_fix_01_prompt.md",
            title=f"{scene_id} {clip_id} Fix 01 Prompt",
            prompt_id=f"{scene_id}_{clip_id}_fix_01_prompt",
            workflow_type="still.scene_insert.two_ref.klein.distilled",
            guidance=(
                "Write a corrective still-generation prompt that preserves composition and look while fixing local issues. "
                "Assume image_1 is the approved still base and image_2 is a secondary reference when needed."
            ),
            sources=[clip_plan_source],
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
            sources=[clip_plan_source],
        ),
    ]


def _load_existing_prompt(path: Path) -> PromptPackage | None:
    if not path.exists():
        return None
    return parse_prompt_package(path)


def _authoring_system_prompt(target: PromptTarget) -> str:
    return "\n".join(
        [
            "You are writing one FilmCreator prompt package section set for a local generation pipeline.",
            "Return only valid JSON.",
            "Do not use markdown fences.",
            "Use descriptive noun phrases and avoid proper nouns in prompt text.",
            "Keep duration and workflow metadata in inputs, not in the prompt body.",
            f"Target stage: {target.stage}",
            f"Stage guidance: {target.guidance}",
            "Required JSON keys: purpose, positive_prompt, negative_prompt, inputs, continuity_notes, repair_notes.",
            "The inputs value must be an object whose values are plain strings.",
            "The continuity_notes and repair_notes values must be arrays of strings.",
        ]
    )


def _authoring_user_prompt(
    *,
    project_slug: str,
    scene_id: str,
    clip_id: str,
    target: PromptTarget,
    clip_context: str,
    existing_prompt: PromptPackage | None,
) -> str:
    existing_markdown = existing_prompt.to_markdown() if existing_prompt else "(none)"
    return "\n\n".join(
        [
            f"Project: {project_slug}",
            f"Scene: {scene_id}",
            f"Clip: {clip_id}",
            f"Prompt title: {target.title}",
            f"Prompt id: {target.prompt_id}",
            f"Workflow type: {target.workflow_type}",
            "",
            "Write improved content for this canonical prompt package.",
            "Keep the prompt aligned with the clip context and current workflow type.",
            "",
            clip_context,
            "",
            "## Existing Prompt Draft",
            existing_markdown,
        ]
    )


def _build_prompt_package_from_llm(
    *,
    response: str,
    target: PromptTarget,
    existing_prompt: PromptPackage | None,
) -> PromptPackage:
    payload = _parse_llm_json(response)
    purpose = _require_string(payload, "purpose")
    positive_prompt = _require_string(payload, "positive_prompt")
    negative_prompt = _require_string(payload, "negative_prompt")
    continuity_notes = _require_string_list(payload, "continuity_notes")
    repair_notes = _require_string_list(payload, "repair_notes")

    inputs = _merge_inputs(existing_prompt.inputs if existing_prompt else {}, payload.get("inputs"))
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


def _sources_markdown(existing_prompt: PromptPackage | None, target: PromptTarget) -> str:
    if existing_prompt and existing_prompt.sources:
        return "\n".join(f"- {source}" for source in existing_prompt.sources)
    return "\n".join(f"- {source}" for source in target.sources)


def _merge_inputs(existing_inputs: dict[str, str], raw_inputs: object) -> dict[str, str]:
    merged = dict(existing_inputs)
    if isinstance(raw_inputs, dict):
        for key, value in raw_inputs.items():
            if isinstance(key, str):
                merged[key] = "" if value is None else str(value)
    return merged


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
            raise LMStudioError("LM Studio did not return valid JSON for prompt writing.")
        payload = json.loads(cleaned[start : end + 1])

    if not isinstance(payload, dict):
        raise LMStudioError("LM Studio prompt-writing response must be a JSON object.")
    return payload


def _require_string(payload: dict[str, object], key: str) -> str:
    value = payload.get(key)
    if not isinstance(value, str) or not value.strip():
        raise LMStudioError(f"LM Studio prompt-writing response is missing a non-empty string for '{key}'.")
    return value.strip()


def _require_string_list(payload: dict[str, object], key: str) -> list[str]:
    value = payload.get(key)
    if not isinstance(value, list):
        raise LMStudioError(f"LM Studio prompt-writing response is missing a list for '{key}'.")
    items = [item.strip() for item in value if isinstance(item, str) and item.strip()]
    if not items:
        raise LMStudioError(f"LM Studio prompt-writing response did not provide any values for '{key}'.")
    return items


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
