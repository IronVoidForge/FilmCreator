Status: 95%

# 4.1 Runner CLI and Job Dispatch

## Goal

Provide a local-first runner and operator CLI that can execute, inspect, and resume still-image stages without depending on launcher-specific logic.

## Current Implementation Note

The core operator surface now exists in the Python CLI:

- `python -m orchestrator menu`
- `python -m orchestrator project-status <project>`
- `python -m orchestrator resume-check <project>`
- `python -m orchestrator run-production <project> ...`
- `python -m orchestrator run-story-analysis <project> ...`
- `python -m orchestrator run-quicktest-composite <project> ...`
- `python -m orchestrator run-production-range <project> ...`
- `python -m orchestrator clear-production <project> ...`

Smart resume validation is now part of the CLI-era flow, not only the BAT-era flow. The trusted overnight resume BAT still exists as a fallback, but the authoritative resume logic lives in `overnight_pipeline_resume_check.py` and is surfaced through the CLI.

## Required Commands

- Run and inspect project status
- Ask where resume should start for a project or chapter slice
- Run a trusted production resume plan
- Run a compact downstream quick test on a controlled slice
- Run shared character reference jobs
- Run shared environment reference jobs
- Register, approve, reject, and lock reference assets
- Run a future clip scene-build job
- Run a future opening-frame image-to-image reframe job
- Run a future clip anchor or interval job
- Review, approve, reject, regenerate, and lock future frame candidates
- Block future I2V jobs when their approved opener is missing
- Promote an approved future asset

## Dispatch Rules

- Resolve the project, scene, and clip context from arguments or state.
- Resolve the workflow from the registry.
- Resolve the latest approved continuity source from clip state for continuation jobs.
- Respect `opening_keyframe_strategy`; do not treat every next shot as either fully fresh or direct continuation.
- If `opening_keyframe_strategy=previous_last_frame_reframe`, verify the previous approved video last frame and approved secondary-view opener before I2V dispatch.
- Validate required prompt files and image refs before execution.
- Route outputs according to the declared output scope.
- Authoring and rendering are separate local phases; the runner must not require LM Studio to remain loaded while ComfyUI executes a render job.
- Hosted or proprietary generation APIs are not required for the core pipeline.
- Resume decisions must validate artifact completeness, not only file existence.
- Approval and locking must preserve approved reference assets across ordinary reruns.
- Prompt-package parsing must enforce the current schema, including `Repair Notes`.

## Current Boundaries

- Phase 1-11 orchestration, status, cleanup, and smart resume are active.
- Phase 12 and 13 planning, registration, approval, locking, and static validation are active.
- Scene-build, golden-frame, anchor, interval, and video dispatch are not active yet and remain planned work.
- Existing BATs are now wrappers or fallbacks. They are no longer the preferred long-term control surface.

## Acceptance

- A human can run the current still-image pipeline locally without editing workflow JSONs by hand.
- A human can ask the CLI where resume should begin and get a trustworthy answer.
- The same operator surface can later absorb scene-build and golden-frame work without requiring a second orchestration layer.
- The runner can distinguish independent frame-generation jobs from sequential jobs blocked by prior approved video output.
