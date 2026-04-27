from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


PRESERVED_PATHS = [
    "01_source",
    "02_story_analysis/chapter_analysis",
    "02_story_analysis/character_breakdowns",
    "02_story_analysis/environment_breakdowns",
    "02_story_analysis/world/chapters",
    "03_reference_assets",
]

CLEANUP_SCOPES: dict[str, dict[str, list[str]]] = {
    "prompt_prep_only": {
        "dirs": [
            "02_story_analysis/descriptors",
            "03_prompt_packages/prepared",
        ],
        "files": [],
    },
    "downstream_only": {
        "dirs": [
            "02_story_analysis/contracts",
            "02_story_analysis/timelines",
            "02_story_analysis/descriptors",
            "02_story_analysis/grading",
            "02_story_analysis/dialogue_enrichment",
            "03_prompt_packages/prepared",
        ],
        "files": [],
    },
    "taxonomy_and_downstream": {
        "dirs": [
            "02_story_analysis/taxonomy",
            "02_story_analysis/world/refinement",
            "02_story_analysis/bibles",
            "02_story_analysis/contracts",
            "02_story_analysis/timelines",
            "02_story_analysis/descriptors",
            "02_story_analysis/grading",
            "02_story_analysis/dialogue_enrichment",
            "03_prompt_packages/prepared",
        ],
        "files": [
            "02_story_analysis/world/global/VISUAL_FALLBACKS.json",
        ],
    },
}


@dataclass(frozen=True)
class CleanupPlanSummary:
    project_slug: str
    scope: str
    dry_run: bool
    plan_path: str
    targets: list[dict[str, Any]]
    preserved: list[str]

    def to_dict(self) -> dict[str, Any]:
        return {
            "project_slug": self.project_slug,
            "scope": self.scope,
            "dry_run": self.dry_run,
            "plan_path": self.plan_path,
            "targets": self.targets,
            "preserved": self.preserved,
        }


@dataclass(frozen=True)
class CleanupExecutionSummary:
    project_slug: str
    scope: str
    plan_path: str
    deleted: list[str]
    skipped_missing: list[str]
    verification_failed: list[str]

    def to_dict(self) -> dict[str, Any]:
        return {
            "project_slug": self.project_slug,
            "scope": self.scope,
            "plan_path": self.plan_path,
            "deleted": self.deleted,
            "skipped_missing": self.skipped_missing,
            "verification_failed": self.verification_failed,
        }


def create_cleanup_plan(project_slug: str, *, scope: str, repo_root: Path | None = None) -> CleanupPlanSummary:
    if scope not in CLEANUP_SCOPES:
        raise ValueError(f"Unsupported cleanup scope: {scope}")
    root = (repo_root or Path.cwd()).resolve()
    project_root = root / "projects" / project_slug
    if not project_root.exists():
        raise FileNotFoundError(f"Project root not found: {project_root}")

    targets: list[dict[str, Any]] = []
    scope_config = CLEANUP_SCOPES[scope]
    for relative in scope_config["dirs"]:
        absolute = project_root / Path(relative)
        targets.append(
            {
                "path": str(absolute),
                "relative_path": relative.replace("\\", "/"),
                "kind": "dir",
                "exists": absolute.exists(),
            }
        )
    for relative in scope_config["files"]:
        absolute = project_root / Path(relative)
        targets.append(
            {
                "path": str(absolute),
                "relative_path": relative.replace("\\", "/"),
                "kind": "file",
                "exists": absolute.exists(),
            }
        )

    plan_path = _cleanup_plan_path(project_root)
    plan_payload = {
        "project_slug": project_slug,
        "scope": scope,
        "targets": targets,
        "preserved": PRESERVED_PATHS,
    }
    plan_path.parent.mkdir(parents=True, exist_ok=True)
    plan_path.write_text(json.dumps(plan_payload, indent=2), encoding="utf-8")
    return CleanupPlanSummary(
        project_slug=project_slug,
        scope=scope,
        dry_run=True,
        plan_path=str(plan_path),
        targets=targets,
        preserved=list(PRESERVED_PATHS),
    )


def execute_cleanup_plan(project_slug: str, *, repo_root: Path | None = None) -> CleanupExecutionSummary:
    root = (repo_root or Path.cwd()).resolve()
    project_root = root / "projects" / project_slug
    plan_path = _cleanup_plan_path(project_root)
    if not plan_path.exists():
        raise FileNotFoundError(f"Cleanup plan not found: {plan_path}")

    payload = json.loads(plan_path.read_text(encoding="utf-8"))
    scope = str(payload.get("scope") or "").strip()
    targets = payload.get("targets", [])
    if not isinstance(targets, list):
        raise ValueError("Cleanup plan targets are invalid.")

    deleted: list[str] = []
    skipped_missing: list[str] = []
    verification_failed: list[str] = []

    for target in targets:
        if not isinstance(target, dict):
            continue
        raw_path = target.get("path")
        kind = target.get("kind")
        if not isinstance(raw_path, str) or kind not in {"dir", "file"}:
            continue
        absolute = Path(raw_path).resolve()
        _ensure_within(project_root, absolute)
        if not absolute.exists():
            skipped_missing.append(str(absolute))
            continue
        if kind == "dir":
            for child in sorted(absolute.iterdir(), reverse=True):
                _remove_path(child)
            absolute.rmdir()
        else:
            absolute.unlink()
        deleted.append(str(absolute))

    for target in targets:
        if not isinstance(target, dict) or not isinstance(target.get("path"), str):
            continue
        absolute = Path(target["path"]).resolve()
        if absolute.exists():
            verification_failed.append(str(absolute))

    return CleanupExecutionSummary(
        project_slug=project_slug,
        scope=scope,
        plan_path=str(plan_path),
        deleted=deleted,
        skipped_missing=skipped_missing,
        verification_failed=verification_failed,
    )


def format_cleanup_plan(summary: CleanupPlanSummary) -> list[str]:
    lines = [
        f"Project: {summary.project_slug}",
        f"Scope: {summary.scope}",
        f"Plan path: {summary.plan_path}",
        "Preserved paths:",
    ]
    for preserved in summary.preserved:
        lines.append(f"- {preserved}")
    lines.append("Planned targets:")
    for target in summary.targets:
        exists_text = "EXISTS" if target["exists"] else "missing"
        lines.append(f"- {target['kind']}: {target['relative_path']} ({exists_text})")
    return lines


def _cleanup_plan_path(project_root: Path) -> Path:
    return project_root / "02_story_analysis" / "cleanup" / "last_cleanup_plan.json"


def _ensure_within(project_root: Path, target: Path) -> None:
    project_root = project_root.resolve()
    target = target.resolve()
    if project_root not in target.parents and target != project_root:
        raise ValueError(f"Cleanup target escapes project root: {target}")


def _remove_path(path: Path) -> None:
    if path.is_dir():
        for child in sorted(path.iterdir(), reverse=True):
            _remove_path(child)
        path.rmdir()
    else:
        path.unlink()
