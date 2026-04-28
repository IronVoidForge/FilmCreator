from __future__ import annotations

import json
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

from .character_references import run_character_reference_generation, run_character_reference_planning
from .production_cleanup import create_cleanup_plan, execute_cleanup_plan, format_cleanup_execution, format_cleanup_plan
from .environment_references import run_environment_reference_generation, run_environment_reference_planning
from .production_pipeline import (
    CHAPTER_SCOPED_PHASES,
    DOWNSTREAM_PHASES,
    OPERATOR_PHASE_ORDER,
    PROJECT_WIDE_PHASES,
    format_production_run_summary,
    plan_trusted_resume_pipeline,
    run_quicktest_composite,
    run_downstream_production,
    run_full_production_pipeline,
    run_phase_range,
    run_post_taxonomy_pipeline,
    run_prompt_prep_refresh,
    run_story_analysis_pipeline,
)
from .production_run_state import persist_run_summary
from .production_status import format_production_status, get_production_status
from .settings import DEFAULT_LLM_MODEL, DEFAULT_LMSTUDIO_TIMEOUT_SECONDS, STARTUP_LLM_MODELS


InputFn = Callable[[str], str]
OutputFn = Callable[[str], None]


@dataclass
class PipelineMenuState:
    project_slug: str = "princess_of_mars_test"
    chapters: str | None = None
    mode: str = "resume"
    lmstudio_model: str = DEFAULT_LLM_MODEL
    lmstudio_timeout_seconds: float = DEFAULT_LMSTUDIO_TIMEOUT_SECONDS
    character_reference_limit: int = 1
    environment_reference_limit: int = 1
    last_cleanup_scope: str | None = None


def run_pipeline_menu(
    *,
    initial_project: str = "princess_of_mars_test",
    initial_chapters: str | None = None,
    initial_mode: str = "resume",
    prompt_on_start: bool = False,
    input_fn: InputFn = input,
    output_fn: OutputFn = print,
    projects_root: Path | None = None,
) -> PipelineMenuState:
    state = PipelineMenuState(
        project_slug=initial_project,
        chapters=initial_chapters,
        mode=initial_mode,
        lmstudio_model=os.environ.get("FILMCREATOR_LMSTUDIO_MODEL") or DEFAULT_LLM_MODEL,
        lmstudio_timeout_seconds=float(os.environ.get("FILMCREATOR_LMSTUDIO_TIMEOUT_SECONDS", str(DEFAULT_LMSTUDIO_TIMEOUT_SECONDS))),
    )
    root = projects_root or (Path.cwd() / "projects")
    if prompt_on_start:
        _select_startup_scope(state, root, input_fn, output_fn)
    _apply_runtime_model(state)

    while True:
        _write_main_menu(state, output_fn)
        choice = input_fn("Choose: ").strip()
        if choice == "1":
            _select_project(state, root, input_fn, output_fn)
        elif choice == "2":
            _select_chapters(state, input_fn, output_fn)
        elif choice == "3":
            _select_mode(state, input_fn, output_fn)
        elif choice == "4":
            _show_status(state, output_fn)
        elif choice == "5":
            _run_full_pipeline(state, output_fn)
        elif choice == "6":
            _run_story_analysis(state, input_fn, output_fn)
        elif choice == "7":
            _run_post_taxonomy(state, input_fn, output_fn)
        elif choice == "8":
            _run_downstream(state, input_fn, output_fn)
        elif choice == "9":
            _run_prompt_refresh(state, input_fn, output_fn)
        elif choice == "10":
            _run_character_references(state, input_fn, output_fn)
        elif choice == "11":
            _run_environment_references(state, input_fn, output_fn)
        elif choice == "12":
            _run_cleanup(state, input_fn, output_fn)
        elif choice == "13":
            _run_advanced_range(state, input_fn, output_fn)
        elif choice == "14":
            output_fn("Exiting pipeline menu.")
            return state
        else:
            output_fn("Invalid choice. Please select one of the numbered options.")


def _select_startup_scope(state: PipelineMenuState, projects_root: Path, input_fn: InputFn, output_fn: OutputFn) -> None:
    output_fn("")
    output_fn("FilmCreator startup scope")
    _select_startup_project(state, projects_root, input_fn, output_fn)
    chapters = input_fn("Chapters to run, e.g. 2-3 or 22-25 [Enter for ALL]: ").strip()
    state.chapters = chapters or None
    _select_model_on_startup(state, input_fn, output_fn)
    _select_timeout_on_startup(state, input_fn, output_fn)
    output_fn(f"Project set to: {state.project_slug}")
    output_fn(f"Chapters set to: {state.chapters or 'ALL'}")
    output_fn(f"Model set to: {state.lmstudio_model}")
    output_fn(f"LM Studio timeout: {state.lmstudio_timeout_seconds:g}s")


def _select_startup_project(state: PipelineMenuState, projects_root: Path, input_fn: InputFn, output_fn: OutputFn) -> None:
    detected = []
    if projects_root.exists():
        detected = sorted(path.name for path in projects_root.iterdir() if path.is_dir())
    if not detected:
        project = input_fn(f"Project slug [{state.project_slug}]: ").strip()
        if project:
            state.project_slug = project
        return

    output_fn("Available projects:")
    for index, slug in enumerate(detected, start=1):
        default_note = " [default]" if slug == state.project_slug else ""
        output_fn(f"{index}. {slug}{default_note}")
    manual_choice = len(detected) + 1
    output_fn(f"{manual_choice}. Enter project slug manually")
    raw = input_fn(f"Choose project [Enter for {state.project_slug}]: ").strip()
    if not raw:
        return
    if raw.isdigit():
        selected = int(raw)
        if 1 <= selected <= len(detected):
            state.project_slug = detected[selected - 1]
            return
        if selected == manual_choice:
            manual_slug = input_fn("Project slug: ").strip()
            if manual_slug:
                state.project_slug = manual_slug
            return
    output_fn(f"Invalid project selection. Keeping: {state.project_slug}")


def _select_model_on_startup(state: PipelineMenuState, input_fn: InputFn, output_fn: OutputFn) -> None:
    output_fn("LM Studio model")
    for index, model_name in enumerate(STARTUP_LLM_MODELS, start=1):
        default_note = " [default]" if model_name == state.lmstudio_model else ""
        output_fn(f"{index}. {model_name}{default_note}")
    raw = input_fn(f"Choose model [Enter for {state.lmstudio_model}]: ").strip()
    if not raw:
        return
    if raw.isdigit():
        selected = int(raw)
        if 1 <= selected <= len(STARTUP_LLM_MODELS):
            state.lmstudio_model = STARTUP_LLM_MODELS[selected - 1]
            return
    if raw in STARTUP_LLM_MODELS:
        state.lmstudio_model = raw
        return
    output_fn(f"Invalid model selection. Keeping: {state.lmstudio_model}")


def _apply_runtime_model(state: PipelineMenuState) -> None:
    os.environ["FILMCREATOR_LMSTUDIO_MODEL"] = state.lmstudio_model
    os.environ["FILMCREATOR_LMSTUDIO_TIMEOUT_SECONDS"] = f"{state.lmstudio_timeout_seconds:g}"


def _select_timeout_on_startup(state: PipelineMenuState, input_fn: InputFn, output_fn: OutputFn) -> None:
    raw = input_fn(f"LM Studio timeout seconds [Enter for {state.lmstudio_timeout_seconds:g}]: ").strip()
    if not raw:
        return
    try:
        parsed = float(raw)
    except ValueError:
        output_fn(f"Invalid timeout. Keeping: {state.lmstudio_timeout_seconds:g}s")
        return
    if parsed <= 0:
        output_fn(f"Invalid timeout. Keeping: {state.lmstudio_timeout_seconds:g}s")
        return
    state.lmstudio_timeout_seconds = parsed


def _write_main_menu(state: PipelineMenuState, output_fn: OutputFn) -> None:
    output_fn("")
    output_fn("FilmCreator Pipeline Menu")
    output_fn(f"Project:  {state.project_slug}")
    output_fn(f"Chapters: {state.chapters or 'ALL'}")
    output_fn(f"Mode:     {state.mode}")
    output_fn(f"Model:    {state.lmstudio_model}")
    output_fn(f"Timeout:  {state.lmstudio_timeout_seconds:g}s")
    output_fn("")
    output_fn("1. Select project")
    output_fn("2. Select chapters / ALL")
    output_fn("3. Select run mode")
    output_fn("4. Project status / resume report")
    output_fn("5. Run full production pipeline")
    output_fn("6. Run story analysis / chapter summaries")
    output_fn("7. Run taxonomy and everything downstream")
    output_fn("8. Run downstream phases only")
    output_fn("9. Run prompt-prep refresh only")
    output_fn("10. Run Phase 12 character references")
    output_fn("11. Run Phase 13 environment references")
    output_fn("12. Clear artifacts")
    output_fn("13. Advanced phase range")
    output_fn("14. Exit")


def _select_project(state: PipelineMenuState, projects_root: Path, input_fn: InputFn, output_fn: OutputFn) -> None:
    detected = []
    if projects_root.exists():
        detected = sorted(path.name for path in projects_root.iterdir() if path.is_dir())
    output_fn("")
    output_fn("Select project")
    for index, slug in enumerate(detected, start=1):
        output_fn(f"{index}. {slug}")
    manual_choice = len(detected) + 1
    back_choice = len(detected) + 2
    output_fn(f"{manual_choice}. Enter project slug manually")
    output_fn(f"{back_choice}. Back")
    raw = input_fn("Choose: ").strip()
    if not raw.isdigit():
        output_fn("Project selection expects a number.")
        return
    selected = int(raw)
    if 1 <= selected <= len(detected):
        state.project_slug = detected[selected - 1]
        output_fn(f"Project updated to: {state.project_slug}")
    elif selected == manual_choice:
        manual_slug = input_fn("Project slug: ").strip()
        if manual_slug:
            state.project_slug = manual_slug
            output_fn(f"Project updated to: {state.project_slug}")
    elif selected == back_choice:
        return
    else:
        output_fn("Invalid project selection.")


def _select_chapters(state: PipelineMenuState, input_fn: InputFn, output_fn: OutputFn) -> None:
    output_fn("")
    output_fn("Chapter selection")
    output_fn(f"Current: {state.chapters or 'ALL'}")
    output_fn("1. ALL chapters")
    output_fn("2. Quick slice: 2-3")
    output_fn("3. Enter custom range")
    output_fn("4. Back")
    choice = input_fn("Choose: ").strip()
    if choice == "1":
        state.chapters = None
        output_fn("Chapters updated to: ALL")
    elif choice == "2":
        state.chapters = "2-3"
        output_fn("Chapters updated to: 2-3")
    elif choice == "3":
        custom = input_fn("Enter chapters: ").strip()
        if custom:
            state.chapters = custom
            output_fn(f"Chapters updated to: {state.chapters}")
    elif choice == "4":
        return
    else:
        output_fn("Invalid chapter selection.")


def _select_mode(state: PipelineMenuState, input_fn: InputFn, output_fn: OutputFn) -> None:
    output_fn("")
    output_fn("Run mode")
    output_fn(f"Current: {state.mode}")
    output_fn("1. Resume / reuse existing complete artifacts")
    output_fn("2. Force regenerate selected phases")
    output_fn("3. Clean selected artifacts first, then run")
    output_fn("4. Back")
    choice = input_fn("Choose: ").strip()
    if choice == "1":
        state.mode = "resume"
        output_fn("Run mode updated to: resume")
    elif choice == "2":
        state.mode = "force"
        output_fn("Run mode updated to: force")
    elif choice == "3":
        output_fn("Clean mode is intentionally not wired yet. The first menu slice keeps destructive operations disabled.")
    elif choice == "4":
        return
    else:
        output_fn("Invalid mode selection.")


def _show_status(state: PipelineMenuState, output_fn: OutputFn) -> None:
    summary = get_production_status(state.project_slug, chapters=state.chapters)
    run_path = persist_run_summary(
        project_slug=state.project_slug,
        run_type="project_status",
        payload=summary.to_dict(),
    )
    for line in format_production_status(summary):
        output_fn(line)
    output_fn(f"Run record: {run_path}")


def _run_full_pipeline(state: PipelineMenuState, output_fn: OutputFn) -> None:
    if state.mode == "resume":
        plan = plan_trusted_resume_pipeline(
            state.project_slug,
            chapters=state.chapters,
        )
        output_fn("Trusted overnight resume behavior is active for resume mode.")
        _emit_summary(plan.to_dict(), output_fn, formatted_lines=format_production_run_summary(plan))
    summary = run_full_production_pipeline(
        state.project_slug,
        chapters=state.chapters,
        mode=state.mode,
    )
    _emit_summary(summary.to_dict(), output_fn, formatted_lines=format_production_run_summary(summary))


def _run_story_analysis(state: PipelineMenuState, input_fn: InputFn, output_fn: OutputFn) -> None:
    output_fn("")
    output_fn("Story analysis / chapter summaries")
    output_fn("1. Resume full-book story analysis")
    output_fn("2. Run selected chapter slice")
    output_fn("3. Run full-book analysis from manifest")
    output_fn("4. Back")
    choice = input_fn("Choose: ").strip()
    if choice == "1":
        summary = run_story_analysis_pipeline(
            state.project_slug,
            chapters=None,
            mode="resume",
        )
        formatted = format_production_run_summary(summary) if hasattr(summary, "profile") else None
        _emit_summary(_to_dict(summary), output_fn, formatted_lines=formatted)
    elif choice == "2":
        summary = run_story_analysis_pipeline(
            state.project_slug,
            chapters=state.chapters,
            mode=state.mode,
        )
        formatted = format_production_run_summary(summary) if hasattr(summary, "profile") else None
        _emit_summary(_to_dict(summary), output_fn, formatted_lines=formatted)
    elif choice == "3":
        summary = run_story_analysis_pipeline(
            state.project_slug,
            chapters=None,
            mode="force",
        )
        formatted = format_production_run_summary(summary) if hasattr(summary, "profile") else None
        _emit_summary(_to_dict(summary), output_fn, formatted_lines=formatted)
    elif choice != "4":
        output_fn("Invalid story analysis selection.")


def _run_post_taxonomy(state: PipelineMenuState, input_fn: InputFn, output_fn: OutputFn) -> None:
    output_fn("")
    output_fn("Taxonomy and downstream")
    output_fn("1. Start at character taxonomy")
    output_fn("2. Start after character taxonomy")
    output_fn("3. Back")
    choice = input_fn("Choose: ").strip()
    if choice == "1":
        summary = run_post_taxonomy_pipeline(
            state.project_slug,
            chapters=state.chapters,
            mode=state.mode,
            include_taxonomy=True,
        )
        _emit_summary(summary.to_dict(), output_fn, formatted_lines=format_production_run_summary(summary))
    elif choice == "2":
        summary = run_post_taxonomy_pipeline(
            state.project_slug,
            chapters=state.chapters,
            mode=state.mode,
            include_taxonomy=False,
        )
        _emit_summary(summary.to_dict(), output_fn, formatted_lines=format_production_run_summary(summary))
    elif choice != "3":
        output_fn("Invalid selection.")


def _run_downstream(state: PipelineMenuState, input_fn: InputFn, output_fn: OutputFn) -> None:
    options = {
        "1": ("phase", "scene_contracts"),
        "2": ("phase", "scene_contracts"),
        "3": ("phase", "scene_bindings"),
        "4": ("phase", "shot_packages"),
        "5": ("phase", "dialogue_timeline"),
        "6": ("phase", "descriptor_enrichment"),
        "7": ("phase", "prompt_preparation"),
        "8": ("composite", "09_to_14"),
        "9": ("composite", "11_to_14"),
        "10": ("composite", "13_to_14"),
    }
    output_fn("")
    output_fn("Downstream phases")
    output_fn("1. Run all downstream phases")
    output_fn("2. Start at scene contracts")
    output_fn("3. Start at scene bindings")
    output_fn("4. Start at shot packages")
    output_fn("5. Start at dialogue timeline")
    output_fn("6. Start at descriptor enrichment")
    output_fn("7. Start at prompt preparation")
    output_fn("8. Quicktest composite 09 to 14")
    output_fn("9. Quicktest composite 11 to 14")
    output_fn("10. Quicktest composite 13 to 14")
    output_fn("11. Back")
    choice = input_fn("Choose: ").strip()
    if choice == "11":
        return
    selected = options.get(choice)
    if selected is None:
        output_fn("Invalid downstream selection.")
        return
    kind, value = selected
    if kind == "composite":
        summary = run_quicktest_composite(
            state.project_slug,
            chapters=state.chapters or "2-3",
            composite=value,
        )
    else:
        summary = run_downstream_production(
            state.project_slug,
            chapters=state.chapters,
            start_phase=value,
            mode=state.mode,
        )
    formatted = format_production_run_summary(summary) if hasattr(summary, "project_slug") else None
    _emit_summary(_to_dict(summary), output_fn, formatted_lines=formatted)


def _run_prompt_refresh(state: PipelineMenuState, input_fn: InputFn, output_fn: OutputFn) -> None:
    output_fn("")
    output_fn("Prompt prep refresh")
    output_fn("1. Descriptor enrichment + prompt preparation")
    output_fn("2. Prompt preparation only")
    output_fn("3. Back")
    choice = input_fn("Choose: ").strip()
    if choice == "1":
        summary = run_prompt_prep_refresh(
            state.project_slug,
            chapters=state.chapters,
            mode=state.mode,
            prompt_only=False,
        )
        _emit_summary(summary.to_dict(), output_fn, formatted_lines=format_production_run_summary(summary))
    elif choice == "2":
        summary = run_prompt_prep_refresh(
            state.project_slug,
            chapters=state.chapters,
            mode=state.mode,
            prompt_only=True,
        )
        _emit_summary(summary.to_dict(), output_fn, formatted_lines=format_production_run_summary(summary))
    elif choice != "3":
        output_fn("Invalid prompt refresh selection.")


def _run_character_references(state: PipelineMenuState, input_fn: InputFn, output_fn: OutputFn) -> None:
    output_fn("")
    output_fn("Phase 12 Character References")
    output_fn(f"Project: {state.project_slug}")
    output_fn(f"Chapters: {state.chapters or 'ALL'}")
    output_fn(f"Limit: {state.character_reference_limit}")
    output_fn("1. Run plan/status only")
    output_fn("2. Generate validation slice")
    output_fn("3. Change limit")
    output_fn("4. Back")
    choice = input_fn("Choose: ").strip()
    if choice == "1":
        summary = run_character_reference_planning(
            state.project_slug,
            limit=state.character_reference_limit,
        )
        _emit_summary(_to_dict(summary), output_fn)
    elif choice == "2":
        confirm = input_fn("Type RUN to continue: ").strip()
        if confirm != "RUN":
            output_fn("Character reference generation cancelled.")
            return
        summary = run_character_reference_generation(
            state.project_slug,
            limit=state.character_reference_limit,
            execute=True,
            test_slice=True,
            chapters=state.chapters,
            prompt_variant_id="raw",
        )
        _emit_summary(_to_dict(summary), output_fn)
    elif choice == "3":
        value = input_fn("New limit: ").strip()
        if value.isdigit() and int(value) > 0:
            state.character_reference_limit = int(value)
            output_fn(f"Character reference limit updated to: {state.character_reference_limit}")
        else:
            output_fn("Limit must be a positive integer.")
    elif choice != "4":
        output_fn("Invalid character reference selection.")


def _run_environment_references(state: PipelineMenuState, input_fn: InputFn, output_fn: OutputFn) -> None:
    output_fn("")
    output_fn("Phase 13 Environment References")
    output_fn(f"Project: {state.project_slug}")
    output_fn(f"Chapters: {state.chapters or 'ALL'}")
    output_fn(f"Limit: {state.environment_reference_limit}")
    output_fn("1. Run plan/status only")
    output_fn("2. Generate validation slice")
    output_fn("3. Change limit")
    output_fn("4. Back")
    choice = input_fn("Choose: ").strip()
    if choice == "1":
        summary = run_environment_reference_planning(
            state.project_slug,
            limit=state.environment_reference_limit,
        )
        _emit_summary(_to_dict(summary), output_fn)
    elif choice == "2":
        confirm = input_fn("Type RUN to continue: ").strip()
        if confirm != "RUN":
            output_fn("Environment reference generation cancelled.")
            return
        summary = run_environment_reference_generation(
            state.project_slug,
            limit=state.environment_reference_limit,
            execute=True,
            test_slice=True,
            chapters=state.chapters,
            prompt_variant_id="raw",
        )
        _emit_summary(_to_dict(summary), output_fn)
    elif choice == "3":
        value = input_fn("New limit: ").strip()
        if value.isdigit() and int(value) > 0:
            state.environment_reference_limit = int(value)
            output_fn(f"Environment reference limit updated to: {state.environment_reference_limit}")
        else:
            output_fn("Limit must be a positive integer.")
    elif choice != "4":
        output_fn("Invalid environment reference selection.")


def _run_cleanup(state: PipelineMenuState, input_fn: InputFn, output_fn: OutputFn) -> None:
    output_fn("")
    output_fn("Clear artifacts")
    output_fn("1. Dry-run: clear prompt prep and descriptors")
    output_fn("2. Dry-run: clear downstream phases")
    output_fn("3. Dry-run: clear taxonomy and everything downstream")
    output_fn("4. Dry-run: clear story analysis and everything downstream")
    output_fn("5. Execute last dry-run plan")
    output_fn("6. Back")
    choice = input_fn("Choose: ").strip()
    if choice == "1":
        _show_cleanup_plan(state, "prompt_prep_only", output_fn)
    elif choice == "2":
        _show_cleanup_plan(state, "downstream_only", output_fn)
    elif choice == "3":
        _show_cleanup_plan(state, "taxonomy_and_downstream", output_fn)
    elif choice == "4":
        _show_cleanup_plan(state, "story_analysis_and_downstream", output_fn)
    elif choice == "5":
        if state.last_cleanup_scope == "story_analysis_and_downstream":
            confirm = input_fn(f"Type DELETE {state.project_slug} to execute this cleanup: ").strip()
            if confirm != f"DELETE {state.project_slug}":
                output_fn("Cleanup cancelled.")
                return
        else:
            confirm = input_fn("Type DELETE to execute this cleanup: ").strip()
            if confirm != "DELETE":
                output_fn("Cleanup cancelled.")
                return
        summary = execute_cleanup_plan(state.project_slug)
        _emit_summary(summary.to_dict(), output_fn, formatted_lines=format_cleanup_execution(summary))
    elif choice != "6":
        output_fn("Invalid cleanup selection.")


def _show_cleanup_plan(state: PipelineMenuState, scope: str, output_fn: OutputFn) -> None:
    summary = create_cleanup_plan(state.project_slug, scope=scope)
    state.last_cleanup_scope = scope
    for line in format_cleanup_plan(summary):
        output_fn(line)
    persist_run_summary(
        project_slug=state.project_slug,
        run_type=f"cleanup_plan_{scope}",
        payload=_to_dict(summary),
    )


def _run_advanced_range(state: PipelineMenuState, input_fn: InputFn, output_fn: OutputFn) -> None:
    output_fn("")
    output_fn("Advanced phase range")
    for index, phase_name in enumerate(OPERATOR_PHASE_ORDER, start=1):
        scope = "chapter-scoped" if phase_name in CHAPTER_SCOPED_PHASES else "project-wide"
        output_fn(f"{index}. {phase_name} ({scope})")
    start_raw = input_fn("Start phase number: ").strip()
    end_raw = input_fn("End phase number: ").strip()
    if not start_raw.isdigit() or not end_raw.isdigit():
        output_fn("Phase range selection expects numeric choices.")
        return
    start_index = int(start_raw) - 1
    end_index = int(end_raw) - 1
    if not (0 <= start_index < len(OPERATOR_PHASE_ORDER)) or not (0 <= end_index < len(OPERATOR_PHASE_ORDER)):
        output_fn("Phase range selection is out of bounds.")
        return
    start_phase = OPERATOR_PHASE_ORDER[start_index]
    end_phase = OPERATOR_PHASE_ORDER[end_index]
    summary = run_phase_range(
        state.project_slug,
        start_phase=start_phase,
        end_phase=end_phase,
        chapters=state.chapters,
        mode=state.mode,
    )
    formatted = format_production_run_summary(summary) if hasattr(summary, "profile") else None
    _emit_summary(_to_dict(summary), output_fn, formatted_lines=formatted)


def _emit_summary(summary: dict[str, object], output_fn: OutputFn, formatted_lines: list[str] | None = None) -> None:
    project_slug = summary.get("project_slug") if isinstance(summary, dict) else None
    run_type = summary.get("profile") if isinstance(summary, dict) else None
    if isinstance(project_slug, str) and project_slug:
        persist_run_summary(
            project_slug=project_slug,
            run_type=str(run_type or summary.get("command") or "menu_action"),
            payload=summary,
        )
    if formatted_lines:
        for line in formatted_lines:
            output_fn(line)
    output_fn(json.dumps(summary, indent=2))


def _to_dict(summary: object) -> dict[str, object]:
    if hasattr(summary, "to_dict"):
        return summary.to_dict()
    if isinstance(summary, dict):
        return summary
    return {"result": str(summary)}
