from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .book_authoring import _chapter_id_from_path, _read_manifest_chapter_paths, analyze_book
from .book_ingest import ensure_book_ingested
from .authoring import lmstudio_check
from .character_bible import run_character_bible_synthesis
from .character_visual_evidence_refinement import run_character_visual_evidence_refinement
from .character_taxonomy import run_character_taxonomy
from .chapter_selection import parse_chapter_selector
from .descriptor_enrichment import run_descriptor_enrichment
from .dialogue_timeline import run_dialogue_timeline
from .downstream_pipeline import run_downstream_pipeline
from .environment_bible import run_environment_bible_synthesis
from .identity_refinement import run_identity_refinement
from .overnight_pipeline_resume_check import find_first_incomplete_stage
from .prompt_preparation import run_prompt_preparation
from .production_status import get_production_status
from .quality_grading import run_quality_grading
from .resume_book_analysis import run_resume_book_analysis
from .scene_bindings import run_scene_binding_synthesis
from .scene_contracts import run_scene_contract_synthesis
from .shot_planner import run_shot_planning
from .visual_fallbacks import run_visual_fallback_synthesis


PRE_DOWNSTREAM_PHASES = [
    "character_taxonomy",
    "identity_refinement",
    "character_bibles",
    "character_visual_evidence",
    "environment_bibles",
    "visual_fallbacks",
]
DOWNSTREAM_PHASES = [
    "scene_contracts",
    "scene_bindings",
    "shot_packages",
    "dialogue_timeline",
    "descriptor_enrichment",
    "prompt_preparation",
]
FULL_PRODUCTION_PHASES = PRE_DOWNSTREAM_PHASES + DOWNSTREAM_PHASES + ["quality_grading"]
PROMPT_REFRESH_PHASES = ["descriptor_enrichment", "prompt_preparation"]
RUN_MODES = {"resume", "force"}
OPERATOR_PHASE_ORDER = [
    "story_analysis",
    "character_taxonomy",
    "identity_refinement_plan",
    "identity_refinement_apply",
    "character_bibles",
    "character_visual_evidence",
    "environment_bibles",
    "visual_fallbacks",
    "scene_contracts",
    "scene_bindings",
    "shot_packages",
    "dialogue_timeline",
    "descriptor_enrichment",
    "prompt_preparation",
    "quality_grading",
]
PROJECT_WIDE_PHASES = {
    "character_taxonomy",
    "identity_refinement_plan",
    "identity_refinement_apply",
    "character_bibles",
    "character_visual_evidence",
    "environment_bibles",
    "visual_fallbacks",
    "quality_grading",
}
CHAPTER_SCOPED_PHASES = {
    "story_analysis",
    "scene_contracts",
    "scene_bindings",
    "shot_packages",
    "dialogue_timeline",
    "descriptor_enrichment",
    "prompt_preparation",
}
TRUSTED_RESUME_PHASE_ORDER = [
    "lmstudio_check",
    "story_analysis",
    "character_taxonomy",
    "identity_refinement_plan",
    "identity_refinement_apply",
    "character_bibles",
    "character_visual_evidence",
    "environment_bibles",
    "visual_fallbacks",
    "scene_contracts",
    "scene_bindings",
    "shot_packages",
    "dialogue_timeline",
    "descriptor_enrichment",
    "prompt_preparation",
    "quality_grading",
]
RESUME_STAGE_TO_TRUSTED_PHASE = {
    "story_analysis": "lmstudio_check",
    "character_taxonomy": "character_taxonomy",
    "identity_refinement": "identity_refinement_plan",
    "character_bibles": "character_bibles",
    "character_visual_evidence": "character_visual_evidence",
    "environment_bibles": "environment_bibles",
    "visual_fallbacks": "visual_fallbacks",
    "scene_contracts": "scene_contracts",
    "scene_bindings": "scene_bindings",
    "shot_packages": "shot_packages",
    "dialogue_timeline": "dialogue_timeline",
    "descriptor_enrichment": "descriptor_enrichment",
    "prompt_preparation": "prompt_preparation",
    "quality_grading": "quality_grading",
}


@dataclass(frozen=True)
class ProductionRunSummary:
    profile: str
    project_slug: str
    chapters: str | None
    mode: str
    completed_phases: list[str]
    phase_summaries: dict[str, Any] = field(default_factory=dict)
    warnings: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "profile": self.profile,
            "project_slug": self.project_slug,
            "chapters": self.chapters,
            "mode": self.mode,
            "completed_phases": self.completed_phases,
            "phase_summaries": self.phase_summaries,
            "warnings": self.warnings,
        }


def run_story_analysis_pipeline(
    project_slug: str,
    *,
    chapters: str | None = None,
    mode: str = "resume",
) -> ProductionRunSummary:
    _validate_mode(mode)
    ingest_summary = ensure_book_ingested(project_slug=project_slug)
    if mode == "resume" and not chapters:
        summary = run_resume_book_analysis(project_slug=project_slug, fail_fast=False)
        phase_summaries: dict[str, Any] = {"story_analysis": summary}
        if ingest_summary is not None:
            phase_summaries["book_ingest"] = ingest_summary.to_dict()
        return ProductionRunSummary(
            profile="story_analysis",
            project_slug=project_slug,
            chapters=chapters,
            mode=mode,
            completed_phases=["story_analysis"],
            phase_summaries=phase_summaries,
        )

    requested_paths = _resolve_story_analysis_chapter_paths(project_slug, chapters)
    summary = analyze_book(
        project_slug=project_slug,
        chapters=[str(path) for path in requested_paths] if requested_paths else None,
        fail_fast=False,
    )
    warnings: list[str] = []
    if mode == "resume" and chapters:
        warnings.append(
            "Story analysis resume mode with a chapter slice runs the selected chapters directly instead of using the full resume planner."
        )
    phase_summaries = {"story_analysis": _to_dict(summary)}
    if ingest_summary is not None:
        phase_summaries["book_ingest"] = ingest_summary.to_dict()
    return ProductionRunSummary(
        profile="story_analysis",
        project_slug=project_slug,
        chapters=chapters,
        mode=mode,
        completed_phases=["story_analysis"],
        phase_summaries=phase_summaries,
        warnings=warnings,
    )


def plan_trusted_resume_pipeline(
    project_slug: str,
    *,
    chapters: str | None = None,
) -> ProductionRunSummary:
    resume_stage = find_first_incomplete_stage(project_slug, chapters or "") or "complete"
    if resume_stage == "complete":
        return ProductionRunSummary(
            profile="trusted_resume_plan",
            project_slug=project_slug,
            chapters=chapters,
            mode="resume",
            completed_phases=[],
            phase_summaries={"resume_stage": "complete", "planned_phases": []},
        )

    start_phase = _resolve_trusted_resume_start_phase(resume_stage)
    planned_phases = TRUSTED_RESUME_PHASE_ORDER[
        TRUSTED_RESUME_PHASE_ORDER.index(start_phase) :
    ]
    warnings: list[str] = []
    if "story_analysis" in planned_phases:
        warnings.append(
            "The trusted overnight BAT does not execute story analysis in its downstream resume path; it starts with LM Studio check and then taxonomy onward."
        )
    return ProductionRunSummary(
        profile="trusted_resume_plan",
        project_slug=project_slug,
        chapters=chapters,
        mode="resume",
        completed_phases=[],
        phase_summaries={
            "resume_stage": resume_stage,
            "start_phase": start_phase,
            "planned_phases": planned_phases,
        },
        warnings=warnings,
    )


def run_trusted_resume_pipeline(
    project_slug: str,
    *,
    chapters: str | None = None,
) -> ProductionRunSummary:
    plan = plan_trusted_resume_pipeline(project_slug, chapters=chapters)
    planned = plan.phase_summaries.get("planned_phases", [])
    if not isinstance(planned, list) or not planned:
        return ProductionRunSummary(
            profile="trusted_resume_run",
            project_slug=project_slug,
            chapters=chapters,
            mode="resume",
            completed_phases=[],
            phase_summaries=dict(plan.phase_summaries),
            warnings=list(plan.warnings),
        )

    phase_summaries: dict[str, Any] = {
        "resume_stage": plan.phase_summaries.get("resume_stage"),
        "start_phase": plan.phase_summaries.get("start_phase"),
        "planned_phases": planned,
    }
    completed_phases: list[str] = []
    warnings = list(plan.warnings)

    for phase_name in planned:
        if phase_name == "lmstudio_check":
            summary = lmstudio_check()
        elif phase_name == "story_analysis":
            warnings.append(
                "Story analysis remains excluded from trusted downstream resume execution, matching the overnight BAT."
            )
            continue
        else:
            summary = _run_trusted_phase(project_slug, phase_name, chapters=chapters)
        phase_summaries[phase_name] = _to_dict(summary)
        completed_phases.append(phase_name)

    return ProductionRunSummary(
        profile="trusted_resume_run",
        project_slug=project_slug,
        chapters=chapters,
        mode="resume",
        completed_phases=completed_phases,
        phase_summaries=phase_summaries,
        warnings=warnings,
    )


def run_quicktest_composite(
    project_slug: str,
    *,
    chapters: str | None,
    composite: str,
) -> ProductionRunSummary:
    composite_map = {
        "09_to_14": "scene_contracts",
        "11_to_14": "shot_packages",
        "13_to_14": "descriptor_enrichment",
    }
    start_phase = composite_map.get(composite)
    if start_phase is None:
        raise ValueError(f"Unsupported quicktest composite: {composite}")
    return run_downstream_production(
        project_slug,
        chapters=chapters,
        start_phase=start_phase,
        mode="force",
    )


def run_phase_range(
    project_slug: str,
    *,
    start_phase: str,
    end_phase: str,
    chapters: str | None = None,
    mode: str = "force",
) -> ProductionRunSummary:
    _validate_mode(mode)
    selected = _select_phase_range(start_phase, end_phase)
    phase_summaries: dict[str, Any] = {}
    completed_phases: list[str] = []
    warnings: list[str] = []
    complete_by_phase: dict[str, bool | None] = {}
    if mode == "resume":
        status_summary = get_production_status(project_slug, chapters=chapters)
        complete_by_phase = {
            str(row["phase"]): row["complete"]
            for row in status_summary.phases
            if row.get("complete") is not None
        }

    for phase_name in selected:
        status_key = _status_key_for_phase(phase_name)
        if mode == "resume" and complete_by_phase.get(status_key) is True:
            phase_summaries[phase_name] = {"skipped": True, "reason": "already complete"}
            completed_phases.append(phase_name)
            continue
        summary = _run_operator_phase(project_slug, phase_name, chapters=chapters, mode=mode)
        phase_summaries[phase_name] = _to_dict(summary)
        completed_phases.append(phase_name)

    if chapters:
        warnings.append(
            "Chapter selection only applies to story analysis and phases 09-14; project-wide phases ignore chapter slices."
        )

    return ProductionRunSummary(
        profile="phase_range",
        project_slug=project_slug,
        chapters=chapters,
        mode=mode,
        completed_phases=completed_phases,
        phase_summaries={
            "selected_range": {"start_phase": start_phase, "end_phase": end_phase},
            **phase_summaries,
        },
        warnings=warnings,
    )


def run_prompt_prep_refresh(
    project_slug: str,
    *,
    chapters: str | None = None,
    mode: str = "resume",
    prompt_only: bool = False,
) -> ProductionRunSummary:
    _validate_mode(mode)
    phase_summaries: dict[str, Any] = {}
    completed_phases: list[str] = []
    force = mode == "force"

    if not prompt_only:
        descriptor_summary = run_descriptor_enrichment(
            project_slug,
            use_llm=True,
            force=force,
            chapters=chapters,
        )
        phase_summaries["descriptor_enrichment"] = _to_dict(descriptor_summary)
        completed_phases.append("descriptor_enrichment")

    prompt_summary = run_prompt_preparation(
        project_slug,
        force=force,
        chapters=chapters,
    )
    phase_summaries["prompt_preparation"] = _to_dict(prompt_summary)
    completed_phases.append("prompt_preparation")
    return ProductionRunSummary(
        profile="prompt_refresh",
        project_slug=project_slug,
        chapters=chapters,
        mode=mode,
        completed_phases=completed_phases,
        phase_summaries=phase_summaries,
    )


def run_downstream_production(
    project_slug: str,
    *,
    chapters: str | None = None,
    start_phase: str = "scene_contracts",
    mode: str = "resume",
) -> ProductionRunSummary:
    _validate_mode(mode)
    if start_phase not in DOWNSTREAM_PHASES:
        raise ValueError(f"Unsupported downstream start phase: {start_phase}")

    if mode == "resume":
        summary = run_downstream_pipeline(
            project_slug,
            chapters=chapters,
            start_phase=start_phase,
            resume=True,
            use_llm=True,
        )
        return ProductionRunSummary(
            profile="downstream",
            project_slug=project_slug,
            chapters=chapters,
            mode=mode,
            completed_phases=list(summary.completed_phases),
            phase_summaries=dict(summary.phase_summaries),
        )

    phase_summaries: dict[str, Any] = {}
    completed_phases: list[str] = []
    for phase_name in DOWNSTREAM_PHASES[DOWNSTREAM_PHASES.index(start_phase) :]:
        summary = _run_force_phase(project_slug, phase_name, chapters=chapters)
        phase_summaries[phase_name] = _to_dict(summary)
        completed_phases.append(phase_name)
    return ProductionRunSummary(
        profile="downstream",
        project_slug=project_slug,
        chapters=chapters,
        mode=mode,
        completed_phases=completed_phases,
        phase_summaries=phase_summaries,
    )


def run_full_production_pipeline(
    project_slug: str,
    *,
    chapters: str | None = None,
    mode: str = "resume",
    start_phase: str = "character_taxonomy",
) -> ProductionRunSummary:
    _validate_mode(mode)
    ingest_summary = ensure_book_ingested(project_slug=project_slug)
    if mode == "resume":
        summary = run_trusted_resume_pipeline(project_slug, chapters=chapters)
        if ingest_summary is not None:
            return ProductionRunSummary(
                profile=summary.profile,
                project_slug=summary.project_slug,
                chapters=summary.chapters,
                mode=summary.mode,
                completed_phases=summary.completed_phases,
                phase_summaries={"book_ingest": ingest_summary.to_dict(), **summary.phase_summaries},
                warnings=summary.warnings,
            )
        return summary
    if start_phase not in FULL_PRODUCTION_PHASES:
        raise ValueError(f"Unsupported full production start phase: {start_phase}")

    status_summary = get_production_status(project_slug, chapters=chapters)
    complete_by_phase = {
        row["phase"]: row["complete"]
        for row in status_summary.phases
        if row.get("complete") is not None
    }
    warnings: list[str] = []
    phase_summaries: dict[str, Any] = {}
    completed_phases: list[str] = []

    for phase_name in PRE_DOWNSTREAM_PHASES:
        if FULL_PRODUCTION_PHASES.index(phase_name) < FULL_PRODUCTION_PHASES.index(start_phase):
            continue
        if mode == "resume" and complete_by_phase.get(phase_name) is True:
            phase_summaries[phase_name] = {"skipped": True, "reason": "already complete"}
            completed_phases.append(phase_name)
            continue
        summary = _run_project_phase(project_slug, phase_name, mode=mode)
        phase_summaries[phase_name] = _to_dict(summary)
        completed_phases.append(phase_name)

    downstream_start = None
    for phase_name in DOWNSTREAM_PHASES:
        if FULL_PRODUCTION_PHASES.index(phase_name) < FULL_PRODUCTION_PHASES.index(start_phase):
            continue
        if mode == "resume" and complete_by_phase.get(phase_name) is True:
            phase_summaries.setdefault(phase_name, {"skipped": True, "reason": "already complete"})
            completed_phases.append(phase_name)
            continue
        downstream_start = phase_name
        break

    if downstream_start:
        downstream_summary = run_downstream_production(
            project_slug,
            chapters=chapters,
            start_phase=downstream_start,
            mode=mode,
        )
        for phase_name, payload in downstream_summary.phase_summaries.items():
            phase_summaries[phase_name] = payload
        for phase_name in downstream_summary.completed_phases:
            if phase_name not in completed_phases:
                completed_phases.append(phase_name)

    if FULL_PRODUCTION_PHASES.index("quality_grading") >= FULL_PRODUCTION_PHASES.index(start_phase):
        if mode == "resume" and complete_by_phase.get("quality_grading") is True:
            phase_summaries["quality_grading"] = {"skipped": True, "reason": "already complete"}
            completed_phases.append("quality_grading")
        else:
            quality_summary = run_quality_grading(project_slug)
            phase_summaries["quality_grading"] = _to_dict(quality_summary)
            completed_phases.append("quality_grading")

    if chapters:
        warnings.append(
            "Chapter selection only affects chapter-scoped phases; project-wide phases still run at project scope."
        )

    return ProductionRunSummary(
        profile="full_production",
        project_slug=project_slug,
        chapters=chapters,
        mode=mode,
        completed_phases=completed_phases,
        phase_summaries=(
            {"book_ingest": ingest_summary.to_dict(), **phase_summaries}
            if ingest_summary is not None
            else phase_summaries
        ),
        warnings=warnings,
    )


def run_post_taxonomy_pipeline(
    project_slug: str,
    *,
    chapters: str | None = None,
    mode: str = "resume",
    include_taxonomy: bool = True,
) -> ProductionRunSummary:
    if mode == "resume":
        return run_trusted_resume_pipeline(project_slug, chapters=chapters)
    start_phase = "character_taxonomy" if include_taxonomy else "character_bibles"
    return run_full_production_pipeline(
        project_slug,
        chapters=chapters,
        mode=mode,
        start_phase=start_phase,
    )


def format_production_run_summary(summary: ProductionRunSummary) -> list[str]:
    lines = [
        f"Profile: {summary.profile}",
        f"Project: {summary.project_slug}",
        f"Chapters: {summary.chapters or 'ALL'}",
        f"Mode: {summary.mode}",
        f"Completed phases: {', '.join(summary.completed_phases) if summary.completed_phases else 'none'}",
    ]
    if summary.phase_summaries.get("selected_range"):
        selected = summary.phase_summaries["selected_range"]
        if isinstance(selected, dict):
            lines.append(
                f"Range: {selected.get('start_phase', '')} -> {selected.get('end_phase', '')}"
            )
    planned = summary.phase_summaries.get("planned_phases")
    if isinstance(planned, list):
        lines.append(f"Planned phases: {', '.join(str(item) for item in planned) if planned else 'none'}")
    if summary.warnings:
        for warning in summary.warnings:
            lines.append(f"Warning: {warning}")
    return lines


def _run_project_phase(project_slug: str, phase_name: str, *, mode: str) -> Any:
    force = mode == "force"
    if phase_name == "character_taxonomy":
        return run_character_taxonomy(project_slug, force=force)
    if phase_name == "identity_refinement":
        return run_identity_refinement(project_slug, use_llm=True, apply_merge=True)
    if phase_name == "character_bibles":
        return run_character_bible_synthesis(project_slug, use_llm=True, force=force)
    if phase_name == "character_visual_evidence":
        return run_character_visual_evidence_refinement(project_slug, force=force)
    if phase_name == "environment_bibles":
        return run_environment_bible_synthesis(project_slug, use_llm=True, force=force)
    if phase_name == "visual_fallbacks":
        return run_visual_fallback_synthesis(project_slug, force=force)
    raise ValueError(f"Unsupported project phase: {phase_name}")


def _run_operator_phase(project_slug: str, phase_name: str, *, chapters: str | None, mode: str) -> Any:
    if phase_name == "story_analysis":
        return run_story_analysis_pipeline(project_slug, chapters=chapters, mode=mode)
    if phase_name == "character_taxonomy":
        return run_character_taxonomy(project_slug, force=mode == "force")
    if phase_name == "identity_refinement_plan":
        return run_identity_refinement(project_slug, use_llm=True, apply_merge=False)
    if phase_name == "identity_refinement_apply":
        return run_identity_refinement(project_slug, use_llm=True, apply_merge=True)
    if phase_name == "character_bibles":
        return run_character_bible_synthesis(project_slug, use_llm=True, force=mode == "force")
    if phase_name == "character_visual_evidence":
        return run_character_visual_evidence_refinement(project_slug, force=mode == "force")
    if phase_name == "environment_bibles":
        return run_environment_bible_synthesis(project_slug, use_llm=True, force=mode == "force")
    if phase_name == "visual_fallbacks":
        return run_visual_fallback_synthesis(project_slug, force=mode == "force")
    if phase_name == "quality_grading":
        return run_quality_grading(project_slug)
    if phase_name in DOWNSTREAM_PHASES:
        if mode == "resume":
            return run_downstream_production(
                project_slug,
                chapters=chapters,
                start_phase=phase_name,
                mode="resume",
            )
        return _run_force_phase(project_slug, phase_name, chapters=chapters)
    raise ValueError(f"Unsupported operator phase: {phase_name}")


def _run_trusted_phase(project_slug: str, phase_name: str, *, chapters: str | None) -> Any:
    if phase_name == "character_taxonomy":
        return run_character_taxonomy(project_slug, force=True)
    if phase_name == "identity_refinement_plan":
        return run_identity_refinement(project_slug, use_llm=True, apply_merge=False)
    if phase_name == "identity_refinement_apply":
        return run_identity_refinement(project_slug, use_llm=True, apply_merge=True)
    if phase_name == "character_bibles":
        return run_character_bible_synthesis(project_slug, use_llm=True, force=True)
    if phase_name == "character_visual_evidence":
        return run_character_visual_evidence_refinement(project_slug, force=True)
    if phase_name == "environment_bibles":
        return run_environment_bible_synthesis(project_slug, use_llm=True, force=True)
    if phase_name == "visual_fallbacks":
        return run_visual_fallback_synthesis(project_slug, force=True)
    return _run_force_phase(project_slug, phase_name, chapters=chapters)


def _run_force_phase(project_slug: str, phase_name: str, *, chapters: str | None) -> Any:
    if phase_name == "scene_contracts":
        return run_scene_contract_synthesis(project_slug, use_llm=True, force=True, chapters=chapters)
    if phase_name == "scene_bindings":
        return run_scene_binding_synthesis(project_slug, force=True, chapters=chapters)
    if phase_name == "shot_packages":
        return run_shot_planning(project_slug, use_llm=True, force=True, chapters=chapters)
    if phase_name == "dialogue_timeline":
        return run_dialogue_timeline(project_slug, force=True, chapters=chapters)
    if phase_name == "descriptor_enrichment":
        return run_descriptor_enrichment(project_slug, use_llm=True, force=True, chapters=chapters)
    if phase_name == "prompt_preparation":
        return run_prompt_preparation(project_slug, force=True, chapters=chapters)
    raise ValueError(f"Unsupported force phase: {phase_name}")


def _to_dict(summary: Any) -> dict[str, Any]:
    if hasattr(summary, "to_dict"):
        return summary.to_dict()
    if isinstance(summary, dict):
        return summary
    return {"result": str(summary)}


def _validate_mode(mode: str) -> None:
    if mode not in RUN_MODES:
        raise ValueError(f"Unsupported run mode: {mode}")


def _resolve_trusted_resume_start_phase(resume_stage: str) -> str:
    try:
        return RESUME_STAGE_TO_TRUSTED_PHASE[resume_stage]
    except KeyError as exc:
        raise ValueError(f"Unsupported trusted resume stage: {resume_stage}") from exc


def _select_phase_range(start_phase: str, end_phase: str) -> list[str]:
    if start_phase not in OPERATOR_PHASE_ORDER:
        raise ValueError(f"Unsupported start phase: {start_phase}")
    if end_phase not in OPERATOR_PHASE_ORDER:
        raise ValueError(f"Unsupported end phase: {end_phase}")
    start_index = OPERATOR_PHASE_ORDER.index(start_phase)
    end_index = OPERATOR_PHASE_ORDER.index(end_phase)
    if end_index < start_index:
        raise ValueError("End phase must not come before start phase.")
    return OPERATOR_PHASE_ORDER[start_index : end_index + 1]


def _status_key_for_phase(phase_name: str) -> str:
    if phase_name in {"identity_refinement_plan", "identity_refinement_apply"}:
        return "identity_refinement"
    return phase_name


def _resolve_story_analysis_chapter_paths(project_slug: str, chapters: str | None) -> list[Path]:
    if not chapters:
        return []
    selected_ids = set(parse_chapter_selector(chapters))
    if not selected_ids:
        return []

    project_dir = Path.cwd() / "projects" / project_slug
    manifest_path = project_dir / "01_source" / "book" / "book_manifest.md"
    manifest_paths = _read_manifest_chapter_paths(project_dir=project_dir, manifest_path=manifest_path)
    resolved: list[Path] = []
    for path in manifest_paths:
        if _chapter_id_from_path(path) in selected_ids:
            resolved.append(path)
    return resolved
