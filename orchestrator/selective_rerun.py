from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .core.json_io import read_json
from .scaffold import create_project


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


STAGE_COMMANDS: dict[str, list[str]] = {
    "synthesize-character-bibles": ["synthesize-character-bibles"],
    "synthesize-environment-bibles": ["synthesize-environment-bibles"],
    "synthesize-scene-contracts": ["synthesize-scene-contracts"],
    "synthesize-shot-packages": ["synthesize-shot-packages"],
    "synthesize-dialogue-timeline": ["synthesize-dialogue-timeline"],
    "synthesize-descriptor-enrichment": ["synthesize-descriptor-enrichment"],
    "synthesize-prompt-preparation": ["synthesize-prompt-preparation"],
}


@dataclass(frozen=True)
class SelectiveRerunSummary:
    project_slug: str
    generated_at_utc: str
    rerun_queue_path: str
    rerun_items: int
    planned_stages: list[str]
    executed_stages: list[str]
    dry_run: bool
    warnings: list[str]
    written_files: list[str]

    def to_dict(self) -> dict[str, Any]:
        return {
            "project_slug": self.project_slug,
            "generated_at_utc": self.generated_at_utc,
            "rerun_queue_path": self.rerun_queue_path,
            "rerun_items": self.rerun_items,
            "planned_stages": self.planned_stages,
            "executed_stages": self.executed_stages,
            "dry_run": self.dry_run,
            "warnings": self.warnings,
            "written_files": self.written_files,
        }


def _rerun_queue_path(project_dir: Path) -> Path:
    return project_dir / "02_story_analysis" / "grading" / "review" / "QUALITY_RERUN_QUEUE.json"


def _load_queue(project_dir: Path) -> list[dict[str, Any]]:
    path = _rerun_queue_path(project_dir)
    if not path.exists():
        return []
    payload = read_json(path)
    if isinstance(payload, list):
        return [item for item in payload if isinstance(item, dict)]
    return []


def _planned_stages(queue: list[dict[str, Any]]) -> list[str]:
    stages: list[str] = []
    seen: set[str] = set()
    for item in queue:
        stage = str(item.get("rerun_stage", "")).strip()
        if not stage or stage in seen:
            continue
        if stage not in STAGE_COMMANDS:
            continue
        seen.add(stage)
        stages.append(stage)
    return stages


def run_selective_reruns(
    project_slug: str,
    *,
    execute: bool = False,
) -> SelectiveRerunSummary:
    project_dir = create_project(project_slug).resolve()
    queue = _load_queue(project_dir)
    planned = _planned_stages(queue)
    warnings: list[str] = []
    executed: list[str] = []
    written_files: list[str] = []

    if not queue:
        warnings.append("Quality rerun queue is empty or missing.")

    if execute and planned:
        for stage in planned:
            command = [sys.executable, "-m", "orchestrator", STAGE_COMMANDS[stage][0], project_slug, "--force"]
            subprocess.run(command, check=True)
            executed.append(stage)

    summary = SelectiveRerunSummary(
        project_slug=project_slug,
        generated_at_utc=_utc_now(),
        rerun_queue_path=str(_rerun_queue_path(project_dir)),
        rerun_items=len(queue),
        planned_stages=planned,
        executed_stages=executed,
        dry_run=not execute,
        warnings=warnings,
        written_files=written_files,
    )
    return summary
