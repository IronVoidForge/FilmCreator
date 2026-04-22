from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .descriptor_enrichment import run_descriptor_enrichment
from .dialogue_timeline import run_dialogue_timeline
from .downstream_run_state import DOWNSTREAM_PHASE_ORDER, DownstreamRunTracker
from .prompt_preparation import run_prompt_preparation
from .scene_bindings import run_scene_binding_synthesis
from .scene_contracts import run_scene_contract_synthesis
from .shot_planner import run_shot_planning


@dataclass(frozen=True)
class DownstreamPipelineSummary:
    project_slug: str
    run_id: str
    pipeline_key: str
    resumed: bool
    start_phase: str
    completed_phases: list[str]
    phase_summaries: dict[str, Any]
    state_path: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "project_slug": self.project_slug,
            "run_id": self.run_id,
            "pipeline_key": self.pipeline_key,
            "resumed": self.resumed,
            "start_phase": self.start_phase,
            "completed_phases": self.completed_phases,
            "phase_summaries": self.phase_summaries,
            "state_path": self.state_path,
        }


def run_downstream_pipeline(
    project_slug: str,
    *,
    chapters: str | None = None,
    start_phase: str = "scene_contracts",
    pipeline_key: str = "downstream_pipeline",
    resume: bool = True,
    use_llm: bool = True,
    shot_variants: list[str] | None = None,
) -> DownstreamPipelineSummary:
    if start_phase not in DOWNSTREAM_PHASE_ORDER:
        raise ValueError(f"Unknown downstream start phase: {start_phase}")

    config = {
        "project_slug": project_slug,
        "chapters": chapters,
        "start_phase": start_phase,
        "use_llm": use_llm,
        "shot_variants": list(shot_variants or []),
    }
    tracker = DownstreamRunTracker.start_or_resume(
        project_slug=project_slug,
        pipeline_key=pipeline_key,
        config=config,
        resume=resume,
    )
    resumed = tracker.current_phase is not None
    phase_summaries: dict[str, Any] = {}
    completed_phases: list[str] = []

    phase_order = DOWNSTREAM_PHASE_ORDER[DOWNSTREAM_PHASE_ORDER.index(start_phase) :]
    for phase_name in phase_order:
        if tracker.phase_completed(phase_name):
            completed_phases.append(phase_name)
            continue
        tracker.set_phase_running(phase_name)
        try:
            if phase_name == "scene_contracts":
                summary = run_scene_contract_synthesis(
                    project_slug,
                    use_llm=use_llm,
                    force=False,
                    chapters=chapters,
                    run_tracker=tracker,
                )
            elif phase_name == "scene_bindings":
                summary = run_scene_binding_synthesis(
                    project_slug,
                    force=False,
                    chapters=chapters,
                    run_tracker=tracker,
                )
            elif phase_name == "shot_packages":
                summary = run_shot_planning(
                    project_slug,
                    use_llm=use_llm,
                    force=False,
                    chapters=chapters,
                    run_tracker=tracker,
                )
            elif phase_name == "dialogue_timeline":
                summary = run_dialogue_timeline(
                    project_slug,
                    force=False,
                    chapters=chapters,
                    run_tracker=tracker,
                )
            elif phase_name == "descriptor_enrichment":
                summary = run_descriptor_enrichment(
                    project_slug,
                    use_llm=use_llm,
                    force=False,
                    chapters=chapters,
                    run_tracker=tracker,
                )
            elif phase_name == "prompt_preparation":
                summary = run_prompt_preparation(
                    project_slug,
                    force=False,
                    chapters=chapters,
                    shot_variants=shot_variants,
                    run_tracker=tracker,
                )
            else:  # pragma: no cover
                raise ValueError(f"Unsupported phase: {phase_name}")
        except Exception as exc:
            tracker.mark_failed(phase_name, exc)
            raise
        phase_summaries[phase_name] = summary.to_dict()
        completed_phases.append(phase_name)
        tracker.mark_phase_completed(phase_name, summary=summary.to_dict())

    final_summary = tracker.mark_run_completed()
    return DownstreamPipelineSummary(
        project_slug=project_slug,
        run_id=final_summary.run_id,
        pipeline_key=final_summary.pipeline_key,
        resumed=resumed,
        start_phase=start_phase,
        completed_phases=completed_phases,
        phase_summaries=phase_summaries,
        state_path=final_summary.state_path,
    )
