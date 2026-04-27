from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .descriptor_enrichment import DESCRIPTOR_ENRICHMENT_SCHEMA_VERSION, run_descriptor_enrichment
from .dialogue_timeline import DIALOGUE_TIMELINE_SCHEMA_VERSION, run_dialogue_timeline
from .downstream_run_state import DOWNSTREAM_PHASE_ORDER, DownstreamRunTracker
from .prompt_preparation import PROMPT_PREPARATION_SCHEMA_VERSION, run_prompt_preparation
from .scene_bindings import SCENE_BINDING_SCHEMA_VERSION, run_scene_binding_synthesis
from .scene_contracts import SCENE_CONTRACT_SCHEMA_VERSION, run_scene_contract_synthesis
from .shot_planner import SHOT_PLANNER_SCHEMA_VERSION, run_shot_planning


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


@dataclass(frozen=True)
class DownstreamRunStateSummary:
    project_slug: str
    pipeline_key: str
    found: bool
    run_id: str | None
    status: str | None
    current_phase: str | None
    config: dict[str, Any]
    phase_status: list[dict[str, Any]]
    state_path: str | None

    def to_dict(self) -> dict[str, Any]:
        return {
            "project_slug": self.project_slug,
            "pipeline_key": self.pipeline_key,
            "found": self.found,
            "run_id": self.run_id,
            "status": self.status,
            "current_phase": self.current_phase,
            "config": self.config,
            "phase_status": self.phase_status,
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
    coverage_density: str | None = None,
) -> DownstreamPipelineSummary:
    if start_phase not in DOWNSTREAM_PHASE_ORDER:
        raise ValueError(f"Unknown downstream start phase: {start_phase}")

    config = {
        "project_slug": project_slug,
        "chapters": chapters,
        "start_phase": start_phase,
        "use_llm": use_llm,
        "shot_variants": list(shot_variants or []),
        "coverage_density": coverage_density,
        "stage_versions": {
            "scene_contracts": SCENE_CONTRACT_SCHEMA_VERSION,
            "scene_bindings": SCENE_BINDING_SCHEMA_VERSION,
            "shot_packages": SHOT_PLANNER_SCHEMA_VERSION,
            "dialogue_timeline": DIALOGUE_TIMELINE_SCHEMA_VERSION,
            "descriptor_enrichment": DESCRIPTOR_ENRICHMENT_SCHEMA_VERSION,
            "prompt_preparation": PROMPT_PREPARATION_SCHEMA_VERSION,
        },
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
                    coverage_density=coverage_density,
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


def summarize_downstream_run(
    project_slug: str,
    *,
    pipeline_key: str = "downstream_pipeline",
) -> DownstreamRunStateSummary:
    tracker = DownstreamRunTracker.load_latest(project_slug=project_slug, pipeline_key=pipeline_key)
    if tracker is None:
        return DownstreamRunStateSummary(
            project_slug=project_slug,
            pipeline_key=pipeline_key,
            found=False,
            run_id=None,
            status=None,
            current_phase=None,
            config={},
            phase_status=[],
            state_path=None,
        )

    phase_status: list[dict[str, Any]] = []
    for phase_name in DOWNSTREAM_PHASE_ORDER:
        phase = tracker.payload.get("phases", {}).get(phase_name, {})
        items = phase.get("items", {}) if isinstance(phase, dict) else {}
        phase_status.append(
            {
                "phase": phase_name,
                "status": phase.get("status"),
                "total_items": phase.get("total_items"),
                "completed_items": phase.get("completed_items"),
                "recorded_items": len(items) if isinstance(items, dict) else 0,
                "started_at_utc": phase.get("started_at_utc"),
                "completed_at_utc": phase.get("completed_at_utc"),
            }
        )

    return DownstreamRunStateSummary(
        project_slug=project_slug,
        pipeline_key=pipeline_key,
        found=True,
        run_id=tracker.run_id,
        status=str(tracker.payload.get("status", "")).strip() or None,
        current_phase=tracker.current_phase,
        config=tracker.payload.get("config", {}) if isinstance(tracker.payload.get("config", {}), dict) else {},
        phase_status=phase_status,
        state_path=tracker.latest_path.as_posix(),
    )
