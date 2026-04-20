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
    from ..batch_runner import plan_prompt_batch as _impl
    return _impl(
        project_slug=project_slug,
        stage=stage,
        prompt_file=prompt_file,
        scene_id=scene_id,
        clip_id=clip_id,
        workflow_id=workflow_id,
        batch_size=batch_size,
        seed=seed,
    )


def run_prompt_batch(*, batch_manifest_path: str, ref_args: list[str] | None = None, seed_base: int | None = None, execute: bool = False) -> BatchRunSummary:
    from ..batch_runner import run_prompt_batch as _impl
    return _impl(batch_manifest_path=batch_manifest_path, ref_args=ref_args, seed_base=seed_base, execute=execute)
