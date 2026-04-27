from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

from .character_references import run_character_reference_generation, run_character_reference_planning
from .environment_references import run_environment_reference_generation, run_environment_reference_planning
from .production_pipeline import (
    DOWNSTREAM_PHASES,
    run_downstream_production,
    run_full_production_pipeline,
    run_post_taxonomy_pipeline,
    run_prompt_prep_refresh,
)
from .production_status import format_production_status, get_production_status


InputFn = Callable[[str], str]
OutputFn = Callable[[str], None]


@dataclass
class PipelineMenuState:
    project_slug: str = "princess_of_mars_test"
    chapters: str | None = None
    mode: str = "resume"
    character_reference_limit: int = 1
    environment_reference_limit: int = 1


def run_pipeline_menu(
    *,
    initial_project: str = "princess_of_mars_test",
    initial_chapters: str | None = None,
    initial_mode: str = "resume",
    input_fn: InputFn = input,
    output_fn: OutputFn = print,
    projects_root: Path | None = None,
) -> PipelineMenuState:
    state = PipelineMenuState(
        project_slug=initial_project,
        chapters=initial_chapters,
        mode=initial_mode,
    )
    root = projects_root or (Path.cwd() / "projects")

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
            output_fn("Story analysis menu entry is not wired yet. Use the existing story-analysis launcher for now.")
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
            output_fn("Cleanup is planned as a dry-run-first workflow and is not enabled in this first menu slice yet.")
        elif choice == "13":
            output_fn("Advanced phase range is planned next. This first menu slice keeps the predefined safe workflows only.")
        elif choice == "14":
            output_fn("Exiting pipeline menu.")
            return state
        else:
            output_fn("Invalid choice. Please select one of the numbered options.")


def _write_main_menu(state: PipelineMenuState, output_fn: OutputFn) -> None:
    output_fn("")
    output_fn("FilmCreator Pipeline Menu")
    output_fn(f"Project:  {state.project_slug}")
    output_fn(f"Chapters: {state.chapters or 'ALL'}")
    output_fn(f"Mode:     {state.mode}")
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
    for line in format_production_status(summary):
        output_fn(line)


def _run_full_pipeline(state: PipelineMenuState, output_fn: OutputFn) -> None:
    summary = run_full_production_pipeline(
        state.project_slug,
        chapters=state.chapters,
        mode=state.mode,
    )
    _emit_summary(summary.to_dict(), output_fn)


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
        _emit_summary(summary.to_dict(), output_fn)
    elif choice == "2":
        summary = run_post_taxonomy_pipeline(
            state.project_slug,
            chapters=state.chapters,
            mode=state.mode,
            include_taxonomy=False,
        )
        _emit_summary(summary.to_dict(), output_fn)
    elif choice != "3":
        output_fn("Invalid selection.")


def _run_downstream(state: PipelineMenuState, input_fn: InputFn, output_fn: OutputFn) -> None:
    options = {
        "1": "scene_contracts",
        "2": "scene_contracts",
        "3": "scene_bindings",
        "4": "shot_packages",
        "5": "dialogue_timeline",
        "6": "descriptor_enrichment",
        "7": "prompt_preparation",
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
    output_fn("8. Back")
    choice = input_fn("Choose: ").strip()
    if choice == "8":
        return
    start_phase = options.get(choice)
    if start_phase is None:
        output_fn("Invalid downstream selection.")
        return
    summary = run_downstream_production(
        state.project_slug,
        chapters=state.chapters,
        start_phase=start_phase,
        mode=state.mode,
    )
    _emit_summary(summary.to_dict(), output_fn)


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
        _emit_summary(summary.to_dict(), output_fn)
    elif choice == "2":
        summary = run_prompt_prep_refresh(
            state.project_slug,
            chapters=state.chapters,
            mode=state.mode,
            prompt_only=True,
        )
        _emit_summary(summary.to_dict(), output_fn)
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


def _emit_summary(summary: dict[str, object], output_fn: OutputFn) -> None:
    output_fn(json.dumps(summary, indent=2))


def _to_dict(summary: object) -> dict[str, object]:
    if hasattr(summary, "to_dict"):
        return summary.to_dict()
    if isinstance(summary, dict):
        return summary
    return {"result": str(summary)}
