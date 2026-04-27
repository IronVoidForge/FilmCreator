Status: 95%

# CLI Pipeline Orchestrator Spec

## Purpose

This spec defines the Python CLI layer that replaces launcher-heavy day-to-day pipeline execution.

## Current Implementation Note

The CLI transition is now well underway. The active implementation remains centered in `orchestrator/cli.py`, with supporting modules such as:

- `orchestrator/pipeline_menu.py`
- `orchestrator/production_pipeline.py`
- `orchestrator/production_status.py`
- `orchestrator/production_cleanup.py`
- `orchestrator/production_run_state.py`

The current operator surface already includes:

- `menu`
- `project-status`
- `resume-check`
- `run-production`
- `run-story-analysis`
- `run-quicktest-composite`
- `run-production-range`
- `clear-production`

This means the spec is no longer purely aspirational. The remaining work is refinement, documentation alignment, and future-phase expansion rather than first creation of the CLI layer.

## Goals

1. Provide one consistent command surface for the full local pipeline.
2. Preserve the file-first workflow and keep canonical artifacts on disk.
3. Make quick validation runs possible without manual launcher navigation.
4. Support dependency-aware reruns from any phase.
5. Keep the order of operations explicit and stable.
6. Keep the implementation modular so later phases can be added cleanly.

## Non-Goals

- Replace canonical file artifacts with SQLite.
- Rework upstream chapter ingest.
- Implement final shot keyframe, audio, or video generation in this first pass.
- Hide pipeline state inside launcher-specific behavior.

## Design Principles

- File-first remains canonical.
- The CLI should describe and orchestrate work, not invent new business logic.
- Staleness and dependency state should be visible before any rerun.
- Existing valid artifacts should be reused when current.
- Future phases should be represented explicitly, even if they are placeholders.
- Temporary BATs may remain as wrappers, but they should not be the primary long-term interface.

## Current Situation

The current CLI logic in `orchestrator/cli.py` already exposes:

- project status and resume inspection
- story analysis
- full production orchestration
- downstream quick-test composites
- prompt preparation, descriptor enrichment, and quality grading flows
- character and environment reference planning, generation, and approval
- cleanup planning and execution guards

The menu and direct CLI commands now absorb most of the practical operator work that used to live in launcher folders.

## Package Direction

The long-term package split proposed earlier is still reasonable, but it is no longer a blocker for practical use. The current single-entry CLI plus helper modules is good enough for active operation.

Possible future split:

- `orchestrator/cli/__init__.py`
- `orchestrator/cli/main.py`
- `orchestrator/cli/parser.py`
- `orchestrator/cli/context.py`
- `orchestrator/cli/status.py`
- `orchestrator/cli/rerun.py`
- `orchestrator/cli/reference_assets.py`
- `orchestrator/cli/future/shot_keyframes.py`
- `orchestrator/cli/future/audio.py`
- `orchestrator/cli/future/video.py`

## Command Surface

### Implemented operator commands

- `menu`
- `project-status`
- `resume-check`
- `run-production`
- `run-story-analysis`
- `run-quicktest-composite`
- `run-production-range`
- `clear-production`

These commands already cover the active operator path for planning, resume, cleanup, trusted reruns, and quick validation.

### Existing synthesis and reference commands

- `synthesize-character-bibles`
- `synthesize-environment-bibles`
- `synthesize-scene-contracts`
- `synthesize-scene-bindings`
- `synthesize-shot-packages`
- `synthesize-dialogue-timeline`
- `synthesize-prompt-preparation`
- `synthesize-descriptor-enrichment`
- `grade-artifacts`
- `generate-character-references`
- `generate-environment-references`
- `register-character-reference-candidate`
- `approve-character-reference`
- `lock-character-reference`
- `register-environment-reference-candidate`
- `approve-environment-reference`
- `lock-environment-reference`

The reference asset command family is already live and is now backed by static validation, lifecycle metadata, and approval/locking behavior.

## Stage Order

The active operator model follows this order:

1. story analysis
2. character taxonomy
3. identity refinement
4. character bibles
5. environment bibles
6. visual fallbacks
7. scene contracts
8. scene bindings
9. shot packages
10. dialogue timeline
11. descriptor enrichment
12. prompt preparation
13. quality grading
14. character references
15. environment references

Scene-build, golden-frame, audio, and video remain future phases.

## Migration Status

- The new CLI is already usable as the primary operator path.
- Thin BAT wrappers may remain temporarily for convenience.
- Archived BATs should not be revived when the equivalent CLI command already exists.
- Smart resume is already part of the CLI-era architecture through `resume-check`, `project-status`, and `run-production`.

## Acceptance Criteria

The CLI work is ready for the active still-image pipeline when:

- the current commands still work
- the quick-test workflow can run without legacy BAT logic
- the CLI can print artifact status by phase
- the CLI can rerun from any phase boundary
- the CLI can surface trustworthy resume decisions
- the CLI can plan and manage Phase 12 and 13 reference assets
- the order of operations is readable and consistent

Most of these acceptance criteria are now met for the active Phase 1-13 operator surface. The remaining open area is later clip/keyframe/video expansion, not the core CLI itself.

## Summary

The long-term control surface for FilmCreator is now clearly the Python CLI, with BATs retained only as wrappers or fallback launchers during transition.
