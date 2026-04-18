from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .common import ensure_dir, read_json, write_json
from .prompt_package import PromptPackage, parse_prompt_package, write_prompt_package
from .registry_loader import get_workflow
from .runner import execute_prepared_run, prepare_still_run
from .scaffold import create_clip, create_run_manifest
from .settings import load_runtime_settings
from .state import load_clip_state, path_to_manifest_value, record_clip_run, resolve_user_path
from .style_profiles import (
    build_styled_prompt,
    find_likely_proper_nouns,
    normalize_review_batch_size,
    stage_family,
    style_profiles_for_batch,
    uses_review_batches,
)


STAGE_PROMPT_SUBDIR = {
    "keyframe": "keyframes",
    "still_fix": "fixes",
    "cut_motion": "cut_motion",
}

DEFAULT_PROMPT_FILENAME_BY_STAGE = {
    "keyframe": "{scene_id}_{clip_id}_keyframe_prompt.md",
    "still_fix": "{scene_id}_{clip_id}_fix_01_prompt.md",
    "cut_motion": "{scene_id}_{clip_id}_cut_motion_prompt.md",
}

IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp", ".bmp", ".tif", ".tiff"}


@dataclass(frozen=True)
class BatchPlanSummary:
    stage: str
    workflow_id: str
    batch_manifest_path: Path
    batch_prompt_dir: Path
    base_prompt_file: Path
    candidate_prompt_files: list[str]
    batch_size: int
    warnings: list[str]

    def to_dict(self) -> dict[str, Any]:
        return {
            "stage": self.stage,
            "workflow_id": self.workflow_id,
            "batch_manifest_path": path_to_manifest_value(self.batch_manifest_path),
            "batch_prompt_dir": path_to_manifest_value(self.batch_prompt_dir),
            "base_prompt_file": path_to_manifest_value(self.base_prompt_file),
            "candidate_prompt_files": self.candidate_prompt_files,
            "batch_size": self.batch_size,
            "warnings": self.warnings,
        }


@dataclass(frozen=True)
class BatchRunSummary:
    batch_manifest_path: Path
    stage: str
    execute_requested: bool
    batch_status: str
    candidate_count: int
    completed_candidates: int
    output_files: list[str]
    warnings: list[str]
    blockers: list[str]

    def to_dict(self) -> dict[str, Any]:
        return {
            "batch_manifest_path": path_to_manifest_value(self.batch_manifest_path),
            "stage": self.stage,
            "execute_requested": self.execute_requested,
            "batch_status": self.batch_status,
            "candidate_count": self.candidate_count,
            "completed_candidates": self.completed_candidates,
            "output_files": self.output_files,
            "warnings": self.warnings,
            "blockers": self.blockers,
        }


def plan_prompt_batch(
    *,
    project_slug: str,
    stage: str,
    prompt_file: str | None,
    scene_id: str | None,
    clip_id: str | None,
    workflow_id: str | None,
    batch_size: int | None,
    seed: int | None,
) -> BatchPlanSummary:
    if not uses_review_batches(stage):
        raise ValueError(f"Stage '{stage}' does not use review batches")

    workflow = _resolve_workflow_for_stage(stage, workflow_id)
    prompt_path = _resolve_prompt_path(
        project_slug=project_slug,
        stage=stage,
        prompt_file=prompt_file,
        scene_id=scene_id,
        clip_id=clip_id,
    )
    prompt_package = parse_prompt_package(prompt_path)
    if prompt_package.workflow_type != workflow["id"]:
        raise ValueError(
            f"Prompt package workflow type '{prompt_package.workflow_type}' does not match workflow '{workflow['id']}'"
        )

    raw_batch_size = str(batch_size) if batch_size is not None else prompt_package.inputs.get("review_batch_size")
    normalized_batch_size = normalize_review_batch_size(raw_batch_size, stage=stage)
    style_profiles = style_profiles_for_batch(normalized_batch_size)

    if workflow["output_scope"] == "clip":
        if not scene_id or not clip_id:
            raise ValueError(f"Stage '{stage}' requires both --scene and --clip")
        create_clip(project_slug, scene_id, clip_id)

    manifest_path = create_run_manifest(
        project_slug=project_slug,
        workflow_id=workflow["id"],
        stage=stage,
        prompt_file=path_to_manifest_value(prompt_path),
        scene_id=scene_id,
        clip_id=clip_id,
        input_refs=[],
        seed=seed,
    )

    batch_prompt_dir = ensure_dir(prompt_path.parent / "batches" / manifest_path.stem)
    warnings = _collect_batch_warnings(stage=stage, prompt_package=prompt_package, scene_id=scene_id, clip_id=clip_id, project_slug=project_slug)
    generated_candidates = _write_candidate_prompt_packages(
        prompt_package=prompt_package,
        project_slug=project_slug,
        scene_id=scene_id,
        clip_id=clip_id,
        stage=stage,
        batch_prompt_dir=batch_prompt_dir,
        style_profiles=style_profiles,
    )

    manifest = read_json(manifest_path)
    manifest["status"] = "batch_planned"
    manifest["base_prompt_package"] = prompt_package.to_manifest_dict()
    manifest["warnings"] = warnings
    manifest["blockers"] = []
    manifest["batch"] = {
        "stage_family": stage_family(stage),
        "batch_size": normalized_batch_size,
        "batch_prompt_dir": path_to_manifest_value(batch_prompt_dir),
        "review_status": "pending",
        "chosen_primary": None,
        "top_two": [],
        "candidates": generated_candidates,
    }
    write_json(manifest_path, manifest)

    if scene_id and clip_id:
        record_clip_run(
            project_slug,
            scene_id,
            clip_id,
            stage=stage,
            manifest_path=manifest_path,
            prompt_file=prompt_path,
        )

    return BatchPlanSummary(
        stage=stage,
        workflow_id=workflow["id"],
        batch_manifest_path=manifest_path,
        batch_prompt_dir=batch_prompt_dir,
        base_prompt_file=prompt_path,
        candidate_prompt_files=[candidate["prompt_file"] for candidate in generated_candidates],
        batch_size=normalized_batch_size,
        warnings=warnings,
    )


def run_prompt_batch(
    *,
    batch_manifest_path: str,
    ref_args: list[str] | None = None,
    seed_base: int | None = None,
    execute: bool = False,
) -> BatchRunSummary:
    settings = load_runtime_settings()
    manifest_path = resolve_user_path(batch_manifest_path)
    if not manifest_path.exists():
        raise FileNotFoundError(f"Batch manifest not found: {manifest_path}")

    manifest = read_json(manifest_path)
    batch = manifest.get("batch")
    if not isinstance(batch, dict):
        raise ValueError(f"Manifest does not contain a planned prompt batch: {manifest_path}")

    project_slug = manifest["project_id"]
    stage = manifest["stage"]
    scene_id = manifest.get("scene_id")
    clip_id = manifest.get("clip_id")
    workflow_id = manifest.get("workflow_id")

    candidate_entries = list(batch.get("candidates", []))
    all_output_files: list[str] = []
    warnings: list[str] = list(manifest.get("warnings", []))
    blockers: list[str] = []
    completed_candidates = 0

    for candidate in candidate_entries:
        candidate_rank = int(candidate["candidate_rank"])
        candidate_seed = _candidate_seed(seed_base, manifest.get("seed"), candidate_rank)

        try:
            candidate.pop("error", None)
            prepared = prepare_still_run(
                project_slug=project_slug,
                stage=stage,
                prompt_file=candidate["prompt_file"],
                workflow_id=workflow_id,
                scene_id=scene_id,
                clip_id=clip_id,
                asset_id=None,
                ref_args=ref_args or [],
                seed=candidate_seed,
                settings=settings,
                record_clip_run_entry=False,
            )
            candidate["run_manifest_path"] = path_to_manifest_value(prepared.manifest_path)
            candidate["patched_workflow_path"] = path_to_manifest_value(prepared.patched_workflow_path)
            candidate["continuity_source"] = prepared.continuity_source
            candidate["warnings"] = list(prepared.warnings)
            candidate["blockers"] = list(prepared.blockers)
            candidate["seed"] = candidate_seed
            candidate["status"] = "prepared"

            warnings.extend(prepared.warnings)
            blockers.extend(prepared.blockers)

            if execute and not prepared.blockers:
                execute_prepared_run(prepared)
                candidate_manifest = read_json(prepared.manifest_path)
                candidate["status"] = candidate_manifest.get("status", "completed")
                candidate["output_files"] = list(candidate_manifest.get("output_files", []))
                candidate.pop("error", None)
                all_output_files.extend(candidate["output_files"])
                if candidate["output_files"]:
                    completed_candidates += 1
            else:
                candidate["output_files"] = []
        except Exception as exc:
            candidate["status"] = "failed"
            candidate["error"] = str(exc)
            candidate.setdefault("output_files", [])
            blockers.append(str(exc))

    manifest["batch"]["candidates"] = candidate_entries
    manifest["output_files"] = all_output_files
    manifest["warnings"] = _dedupe(warnings)
    manifest["blockers"] = _dedupe(blockers)
    if execute:
        manifest["status"] = "completed" if completed_candidates == len(candidate_entries) else "failed"
    else:
        manifest["status"] = "batch_prepared"
    write_json(manifest_path, manifest)

    return BatchRunSummary(
        batch_manifest_path=manifest_path,
        stage=stage,
        execute_requested=execute,
        batch_status=manifest["status"],
        candidate_count=len(candidate_entries),
        completed_candidates=completed_candidates,
        output_files=all_output_files,
        warnings=manifest["warnings"],
        blockers=manifest["blockers"],
    )


def _resolve_workflow_for_stage(stage: str, workflow_id: str | None) -> dict[str, Any]:
    if workflow_id:
        workflow = get_workflow(workflow_id)
        if stage not in workflow.get("supported_stages", []):
            raise ValueError(f"Workflow '{workflow_id}' does not support stage '{stage}'")
        return workflow

    if stage == "keyframe":
        return get_workflow("still.scene_build.four_ref.klein.distilled")
    if stage == "still_fix":
        return get_workflow("still.scene_insert.two_ref.klein.distilled")
    if stage == "cut_motion":
        return get_workflow("video.cut_motion.wan.i2v")
    raise KeyError(f"No default workflow is configured for stage '{stage}'")


def _resolve_prompt_path(
    *,
    project_slug: str,
    stage: str,
    prompt_file: str | None,
    scene_id: str | None,
    clip_id: str | None,
) -> Path:
    if prompt_file:
        path = resolve_user_path(prompt_file)
        if not path.exists():
            raise FileNotFoundError(f"Prompt file not found: {path}")
        return path

    if not scene_id or not clip_id:
        raise ValueError(f"Prompt file is required for stage '{stage}' unless both --scene and --clip are provided")

    create_clip(project_slug, scene_id, clip_id)
    prompt_subdir = STAGE_PROMPT_SUBDIR.get(stage)
    filename_template = DEFAULT_PROMPT_FILENAME_BY_STAGE.get(stage)
    if not prompt_subdir or not filename_template:
        raise ValueError(f"No default prompt file mapping is configured for stage '{stage}'")

    path = (
        Path("projects")
        / project_slug
        / "03_prompt_packages"
        / prompt_subdir
        / scene_id
        / clip_id
        / filename_template.format(scene_id=scene_id, clip_id=clip_id)
    )
    resolved = resolve_user_path(str(path))
    if not resolved.exists():
        raise FileNotFoundError(f"Default prompt file not found: {resolved}")
    return resolved


def _write_candidate_prompt_packages(
    *,
    prompt_package: PromptPackage,
    project_slug: str,
    scene_id: str | None,
    clip_id: str | None,
    stage: str,
    batch_prompt_dir: Path,
    style_profiles: list[str],
) -> list[dict[str, Any]]:
    candidates: list[dict[str, Any]] = []
    fix_of = _default_fix_of(project_slug, scene_id, clip_id) if stage == "still_fix" else ""

    for rank, style_profile in enumerate(style_profiles, start=1):
        candidate_package = _build_candidate_prompt_package(
            prompt_package=prompt_package,
            project_slug=project_slug,
            scene_id=scene_id,
            clip_id=clip_id,
            stage=stage,
            rank=rank,
            style_profile=style_profile,
            fix_of=fix_of,
        )
        filename = f"{prompt_package.path.stem}__{rank:02d}_{style_profile}.md"
        candidate_path = batch_prompt_dir / filename
        write_prompt_package(candidate_path, candidate_package)
        candidates.append(
            {
                "candidate_rank": rank,
                "style_profile": style_profile,
                "prompt_file": path_to_manifest_value(candidate_path),
                "status": "planned",
                "review_status": "unreviewed",
                "output_files": [],
            }
        )
    return candidates


def _build_candidate_prompt_package(
    *,
    prompt_package: PromptPackage,
    project_slug: str,
    scene_id: str | None,
    clip_id: str | None,
    stage: str,
    rank: int,
    style_profile: str,
    fix_of: str,
) -> PromptPackage:
    inputs = dict(prompt_package.inputs)
    inputs["project_id"] = project_slug
    if scene_id:
        inputs["scene_id"] = scene_id
    if clip_id:
        inputs["clip_id"] = clip_id
    inputs["style_profile"] = style_profile
    inputs["batch_role"] = f"candidate_{rank:02d}"
    if stage == "still_fix" and fix_of and not inputs.get("fix_of"):
        inputs["fix_of"] = fix_of

    positive_prompt = build_styled_prompt(prompt_package.positive_prompt, style_profile)
    continuity_notes = list(prompt_package.sources)
    sources = list(prompt_package.sources)
    continuity_lines = _render_bullets(
        _parse_existing_bullets(prompt_package.continuity_notes_markdown)
        + [f"Generated batch candidate {rank:02d} for style profile '{style_profile}'."]
    )

    return PromptPackage(
        path=prompt_package.path,
        title=f"{prompt_package.title} [{rank:02d} {style_profile}]",
        prompt_id=f"{prompt_package.prompt_id}_{rank:02d}_{style_profile}",
        purpose=prompt_package.purpose,
        workflow_type=prompt_package.workflow_type,
        positive_prompt=positive_prompt,
        negative_prompt=prompt_package.negative_prompt,
        inputs_markdown="\n".join(f"- {key}: {value}" for key, value in inputs.items()),
        continuity_notes_markdown=continuity_lines,
        sources_markdown="\n".join(f"- {source}" for source in sources),
        repair_notes_markdown=prompt_package.repair_notes_markdown,
    )


def _default_fix_of(project_slug: str, scene_id: str | None, clip_id: str | None) -> str:
    if not scene_id or not clip_id:
        return ""
    clip_state = load_clip_state(project_slug, scene_id, clip_id)
    approved_assets = clip_state.get("approved_assets", {})
    candidate_paths = [
        approved_assets.get("still_fixes", [])[-1] if approved_assets.get("still_fixes") else "",
        approved_assets.get("approved_keyframe"),
        approved_assets.get("golden_frame"),
        clip_state.get("current_continuity_source"),
        clip_state.get("approved_video_last_frame"),
    ]

    latest_review = clip_state.get("latest_review_decision") or {}
    candidate_paths.append(latest_review.get("chosen_primary", ""))

    for candidate in candidate_paths:
        if _is_image_reference(candidate):
            return candidate
    return ""


def _collect_batch_warnings(
    *,
    stage: str,
    prompt_package: PromptPackage,
    project_slug: str,
    scene_id: str | None,
    clip_id: str | None,
) -> list[str]:
    warnings: list[str] = []
    proper_nouns = find_likely_proper_nouns(prompt_package.positive_prompt)
    if proper_nouns:
        warnings.append(
            "Generated prompts may still contain likely proper nouns: "
            + ", ".join(proper_nouns)
            + ". Replace them with descriptive noun phrases before final use when possible."
        )

    if stage == "still_fix":
        fix_of = _default_fix_of(project_slug, scene_id, clip_id)
        if not fix_of:
            warnings.append(
                "No reviewed primary candidate or approved keyframe was found for still_fix. "
                "Set Inputs -> fix_of manually or approve a keyframe first."
            )

    return warnings


def _candidate_seed(seed_base: int | None, manifest_seed: Any, candidate_rank: int) -> int | None:
    if seed_base is not None:
        return seed_base + candidate_rank - 1
    if isinstance(manifest_seed, int):
        return manifest_seed + candidate_rank - 1
    return None


def _parse_existing_bullets(markdown: str) -> list[str]:
    items: list[str] = []
    for line in markdown.splitlines():
        stripped = line.strip()
        if stripped.startswith("- "):
            items.append(stripped[2:].strip())
    return items


def _render_bullets(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)


def _dedupe(items: list[str]) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []
    for item in items:
        if item in seen:
            continue
        seen.add(item)
        ordered.append(item)
    return ordered


def _is_image_reference(value: str | None) -> bool:
    if not value:
        return False
    return Path(value).suffix.lower() in IMAGE_SUFFIXES
