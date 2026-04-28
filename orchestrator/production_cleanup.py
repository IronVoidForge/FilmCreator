from __future__ import annotations

import json
from hashlib import sha256
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .core.validation import validate_project_slug
from .delete_safety import resolve_project_target, validate_project_relative_path, remove_path_within_project


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
    "story_analysis_and_downstream": {
        "dirs": [
            "02_story_analysis/chapter_analysis",
            "02_story_analysis/story_summary",
            "02_story_analysis/character_breakdowns",
            "02_story_analysis/environment_breakdowns",
            "02_story_analysis/scene_breakdowns",
            "02_story_analysis/beat_bundles",
            "02_story_analysis/clip_plans",
            "02_story_analysis/world",
            "02_story_analysis/taxonomy",
            "02_story_analysis/bibles",
            "02_story_analysis/contracts",
            "02_story_analysis/timelines",
            "02_story_analysis/descriptors",
            "02_story_analysis/grading",
            "02_story_analysis/dialogue_enrichment",
            "02_story_analysis/logs",
            "02_story_analysis/runs",
            "03_prompt_packages/prepared",
        ],
        "files": [],
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
    project_slug = validate_project_slug(project_slug)
    if scope not in CLEANUP_SCOPES:
        raise ValueError(f"Unsupported cleanup scope: {scope}")
    root = (repo_root or Path.cwd()).resolve()
    project_root = root / "projects" / project_slug
    if not project_root.exists():
        raise FileNotFoundError(f"Project root not found: {project_root}")

    targets: list[dict[str, Any]] = []
    scope_config = CLEANUP_SCOPES[scope]
    for relative in scope_config["dirs"]:
        normalized = validate_project_relative_path(relative)
        absolute = resolve_project_target(project_root=project_root, relative_path=normalized)
        targets.append(
            {
                "relative_path": normalized,
                "kind": "dir",
                "exists": absolute.exists(),
            }
        )
    for relative in scope_config["files"]:
        normalized = validate_project_relative_path(relative)
        absolute = resolve_project_target(project_root=project_root, relative_path=normalized)
        targets.append(
            {
                "relative_path": normalized,
                "kind": "file",
                "exists": absolute.exists(),
            }
        )

    plan_path = _cleanup_plan_path(project_root)
    plan_signature = _cleanup_plan_signature(project_slug=project_slug, project_root=project_root, scope=scope, targets=targets)
    plan_payload = {
        "project_slug": project_slug,
        "project_root": str(project_root),
        "scope": scope,
        "signature": plan_signature,
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
    project_slug = validate_project_slug(project_slug)
    root = (repo_root or Path.cwd()).resolve()
    project_root = root / "projects" / project_slug
    plan_path = _cleanup_plan_path(project_root)
    if not plan_path.exists():
        raise FileNotFoundError(f"Cleanup plan not found: {plan_path}")

    payload = json.loads(plan_path.read_text(encoding="utf-8"))
    if str(payload.get("project_slug") or "").strip() != project_slug:
        raise ValueError("Cleanup plan project slug does not match the requested project.")
    planned_project_root = Path(str(payload.get("project_root") or "")).resolve()
    if planned_project_root != project_root.resolve():
        raise ValueError(f"Cleanup plan project root mismatch: {planned_project_root} != {project_root.resolve()}")
    scope = str(payload.get("scope") or "").strip()
    targets = payload.get("targets", [])
    signature = str(payload.get("signature") or "").strip()
    if not isinstance(targets, list):
        raise ValueError("Cleanup plan targets are invalid.")
    if scope not in CLEANUP_SCOPES:
        raise ValueError(f"Cleanup plan scope is invalid: {scope}")

    expected_targets = _expected_scope_targets(project_root=project_root, scope=scope)
    actual_targets = _normalized_plan_targets(targets)
    if actual_targets != expected_targets:
        raise ValueError("Cleanup plan targets do not exactly match the allowed scope targets.")
    expected_signature = _cleanup_plan_signature(project_slug=project_slug, project_root=project_root, scope=scope, targets=targets)
    if signature != expected_signature:
        raise ValueError("Cleanup plan signature mismatch. Refusing to execute a tampered cleanup plan.")

    deleted: list[str] = []
    skipped_missing: list[str] = []
    verification_failed: list[str] = []

    for target in targets:
        if not isinstance(target, dict):
            continue
        relative_path = target.get("relative_path")
        kind = target.get("kind")
        if not isinstance(relative_path, str) or kind not in {"dir", "file"}:
            continue
        absolute = resolve_project_target(project_root=project_root, relative_path=relative_path)
        if not absolute.exists():
            skipped_missing.append(str(absolute))
            continue
        remove_path_within_project(absolute, project_root=project_root)
        deleted.append(str(absolute))

    for target in targets:
        if not isinstance(target, dict) or not isinstance(target.get("relative_path"), str):
            continue
        absolute = resolve_project_target(project_root=project_root, relative_path=target["relative_path"])
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


def format_cleanup_execution(summary: CleanupExecutionSummary) -> list[str]:
    lines = [
        f"Project: {summary.project_slug}",
        f"Scope: {summary.scope}",
        f"Deleted targets: {len(summary.deleted)}",
        f"Skipped missing: {len(summary.skipped_missing)}",
        f"Verification failures: {len(summary.verification_failed)}",
    ]
    return lines


def _cleanup_plan_path(project_root: Path) -> Path:
    return project_root / "02_story_analysis" / "cleanup" / "last_cleanup_plan.json"


def _expected_scope_targets(*, project_root: Path, scope: str) -> set[tuple[str, str]]:
    scope_config = CLEANUP_SCOPES[scope]
    expected: set[tuple[str, str]] = set()
    for relative in scope_config["dirs"]:
        normalized = validate_project_relative_path(relative)
        resolve_project_target(project_root=project_root, relative_path=normalized)
        expected.add((normalized, "dir"))
    for relative in scope_config["files"]:
        normalized = validate_project_relative_path(relative)
        resolve_project_target(project_root=project_root, relative_path=normalized)
        expected.add((normalized, "file"))
    return expected


def _normalized_plan_targets(targets: list[dict[str, Any]]) -> set[tuple[str, str]]:
    normalized: set[tuple[str, str]] = set()
    for target in targets:
        if not isinstance(target, dict):
            raise ValueError("Cleanup plan target entry is invalid.")
        relative_path = target.get("relative_path")
        kind = target.get("kind")
        if not isinstance(relative_path, str) or kind not in {"dir", "file"}:
            raise ValueError("Cleanup plan target entry is missing required fields.")
        normalized.add((validate_project_relative_path(relative_path), kind))
    return normalized


def _cleanup_plan_signature(
    *,
    project_slug: str,
    project_root: Path,
    scope: str,
    targets: list[dict[str, Any]],
) -> str:
    canonical_targets = [
        {
            "relative_path": validate_project_relative_path(str(target.get("relative_path", ""))),
            "kind": str(target.get("kind", "")),
        }
        for target in targets
        if isinstance(target, dict)
    ]
    canonical_targets.sort(key=lambda item: (item["relative_path"], item["kind"]))
    payload = {
        "project_slug": project_slug,
        "project_root": str(project_root.resolve()),
        "scope": scope,
        "targets": canonical_targets,
    }
    return sha256(json.dumps(payload, sort_keys=True).encode("utf-8")).hexdigest()
