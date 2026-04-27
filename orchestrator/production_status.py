from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .overnight_pipeline_resume_check import find_first_incomplete_stage, validation_report


@dataclass(frozen=True)
class ProductionStatusSummary:
    project_slug: str
    chapters: str | None
    resume_from: str
    phases: list[dict[str, Any]]
    notes: list[str]

    def to_dict(self) -> dict[str, Any]:
        return {
            "project_slug": self.project_slug,
            "chapters": self.chapters,
            "resume_from": self.resume_from,
            "phases": self.phases,
            "notes": self.notes,
        }


def get_production_status(project_slug: str, *, chapters: str | None = None) -> ProductionStatusSummary:
    report = validation_report(project_slug, chapters or "")
    phases: list[dict[str, Any]] = []
    for row in report:
        phases.append(
            {
                "phase": row.get("stage"),
                "complete": row.get("complete"),
                "reason": row.get("reason", ""),
                "details": row.get("details", {}),
            }
        )

    notes: list[str] = []
    for phase_name in ("character_references", "environment_references"):
        phases.append(
            {
                "phase": phase_name,
                "complete": None,
                "reason": "Reference status not yet included in the automated resume checker.",
                "details": {},
            }
        )
    notes.append("Reference phase completion is not yet part of the automated resume checker.")

    resume_from = find_first_incomplete_stage(project_slug, chapters or "") or "complete"
    return ProductionStatusSummary(
        project_slug=project_slug,
        chapters=chapters,
        resume_from=resume_from,
        phases=phases,
        notes=notes,
    )


def format_production_status(summary: ProductionStatusSummary) -> list[str]:
    lines = [
        f"Project: {summary.project_slug}",
        f"Chapters: {summary.chapters or 'ALL'}",
        "",
    ]
    for row in summary.phases:
        complete = row.get("complete")
        if complete is True:
            status = "PASS"
        elif complete is False:
            status = "FAIL"
        else:
            status = "PLANNED"
        lines.append(f"{row.get('phase')}: {status} - {row.get('reason', '')}")
    lines.append("")
    lines.append(f"Resume would start at: {summary.resume_from}")
    for note in summary.notes:
        lines.append(f"Note: {note}")
    return lines
