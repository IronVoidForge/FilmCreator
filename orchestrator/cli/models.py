from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


ARTIFACT_STATES = {
    "missing",
    "generated",
    "review-needed",
    "blocked",
    "approved",
    "stale",
    "superseded",
    "locked",
    "placeholder",
}


@dataclass(frozen=True)
class CliContext:
    project_slug: str
    repo_root: Path
    project_root: Path
    chapters: str | None = None
    dry_run: bool = False


@dataclass(frozen=True)
class StageDefinition:
    phase: str
    key: str
    label: str
    command: str | None
    artifact_family: str
    dependencies: tuple[str, ...] = ()
    implemented: bool = True


@dataclass(frozen=True)
class ArtifactStatus:
    phase: str
    family: str
    state: str
    path: str
    detail: str = ""
    dependency_hint: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "phase": self.phase,
            "family": self.family,
            "state": self.state,
            "path": self.path,
            "detail": self.detail,
            "dependency_hint": self.dependency_hint,
        }


@dataclass(frozen=True)
class RerunStep:
    phase: str
    command: str
    reason: str
    implemented: bool = True

    def to_dict(self) -> dict[str, Any]:
        return {
            "phase": self.phase,
            "command": self.command,
            "reason": self.reason,
            "implemented": self.implemented,
        }


@dataclass(frozen=True)
class CliSummary:
    command: str
    project_slug: str
    status: str = "ok"
    message: str = ""
    data: dict[str, Any] = field(default_factory=dict)
    warnings: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "command": self.command,
            "project_slug": self.project_slug,
            "status": self.status,
            "message": self.message,
            "data": self.data,
            "warnings": self.warnings,
        }
