from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

from ..common import ensure_dir, read_json, write_json
from ..prompt_package import PromptPackage, parse_prompt_package, write_prompt_package
from ..registry_loader import get_workflow
from ..runner import execute_prepared_run, prepare_still_run
from ..scaffold import create_clip, create_run_manifest
from ..settings import load_runtime_settings
from ..state import load_clip_state, path_to_manifest_value, record_clip_run, resolve_user_path
from ..style_profiles import (
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


def plan_prompt_batch(*, project_slug: str, stage: str, prompt_file: str | None, scene_id: str | None, clip_id: str | None, workflow_id: str | None, batch_size: int | None, seed: int | None) -> BatchPlanSummary:
    if not uses_review_batches(stage):
        raise ValueError(f"Stage '{stage}' does not use review batches")

    from .. import batch_runner as legacy

    workflow = legacy._resolve_workflow_for_stage(stage, workflow_id)
    prompt_path = legacy._resolve_prompt_path(
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
    warnings = legacy._collect_batch_warnings(
        stage=stage,
        prompt_package=prompt_package,
        scene_id=scene_id,
        clip_id=clip_id,
        project_slug=project_slug,
    )
    generated_candidates = legacy._write_candidate_prompt_packages(
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


def run_prompt_batch(*, batch_manifest_path: str, ref_args: list[str] | None = None, seed_base: int | None = None, execute: bool = False) -> BatchRunSummary:
    from .. import batch_runner as legacy

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
        candidate_seed = legacy._candidate_seed(seed_base, manifest.get("seed"), candidate_rank)

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
    manifest["warnings"] = legacy._dedupe(warnings)
    manifest["blockers"] = legacy._dedupe(blockers)
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
