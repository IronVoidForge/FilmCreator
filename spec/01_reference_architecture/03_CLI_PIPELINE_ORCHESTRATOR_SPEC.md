Status: 85%

# CLI Pipeline Orchestrator Spec

## Purpose

This spec defines the Python CLI layer that will eventually replace the temporary launcher bats for day-to-day pipeline execution.

The CLI must:

- run the same compact post-bible quick test as the current quick-test folder
- report which artifacts are present, stale, blocked, missing, or approved
- rerun from any phase or stage boundary
- optionally refresh a small slice of character and environment bibles
- optionally generate and manage Phase 12 and Phase 13 reference assets
- leave explicit placeholders for future phases such as shot keyframes, audio, and video

The CLI should become the source of truth for pipeline execution. The bats remain temporary wrappers during the transition, not the long-term interface.

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
- Temporary bats may remain as wrappers, but they should not be the primary long-term interface.

## Current Situation

The current CLI logic lives in `orchestrator/cli.py`, which already exposes:

- bible synthesis
- scene contracts
- scene binding
- shot planning
- dialogue timeline
- dialogue enrichment
- prompt preparation
- descriptor enrichment
- quality grading
- selective rerun
- character and environment reference planning and approval
- downstream pipeline orchestration

The current quick-test bats already mirror the downstream pipeline on a limited slice, but they are still launcher files. The new CLI package should absorb that behavior so the pipeline can be run directly from Python.

## Proposed Package Layout

The CLI should move from a single module into a package:

- `orchestrator/cli/__init__.py`
- `orchestrator/cli/main.py`
- `orchestrator/cli/app.py`
- `orchestrator/cli/parser.py`
- `orchestrator/cli/context.py`
- `orchestrator/cli/models.py`
- `orchestrator/cli/stages.py`
- `orchestrator/cli/status.py`
- `orchestrator/cli/rerun.py`
- `orchestrator/cli/test_pipeline.py`
- `orchestrator/cli/bibles.py`
- `orchestrator/cli/reference_assets.py`
- `orchestrator/cli/future/shot_keyframes.py`
- `orchestrator/cli/future/audio.py`
- `orchestrator/cli/future/video.py`

## Module Responsibilities

### `main.py`

CLI entrypoint.

- parse arguments
- create app context
- dispatch commands

### `app.py`

Top-level orchestration object.

- wire parser, status, rerun, and execution paths together
- keep shared config in one place

### `parser.py`

Argparse configuration.

- register subcommands
- define common options
- expose phase-specific flags

### `context.py`

Runtime context and path resolution.

- project slug resolution
- repo root resolution
- chapter slice parsing
- default values
- run configuration

### `models.py`

Shared dataclasses or lightweight models.

- run config
- stage result
- artifact status
- rerun plan
- review state

### `stages.py`

Canonical stage registry and order.

- define phase order
- define stage names
- define expected artifact families
- define dependencies
- define staleness rules
- define future placeholders

### `status.py`

Artifact status inspection.

- tell whether an artifact is present, missing, stale, blocked, review-needed, approved, or locked
- summarize project readiness
- report by phase and artifact family

### `rerun.py`

Dependency-aware rerun planning.

- determine the first phase to rerun
- stop at an optional target phase
- optionally rerun only stale artifacts
- optionally filter by chapters or entity limits

### `test_pipeline.py`

Compact quick-test orchestration.

- clear downstream artifacts
- optionally refresh a small bible slice
- run scene contracts, scene bindings, shot packages, dialogue timeline, descriptor enrichment, prompt preparation, and quality grading
- mirror the current quick-test folder behavior

### `bibles.py`

Limited bible refresh helpers.

- character bibles
- environment bibles
- small-slice refresh support

### `reference_assets.py`

Phase 12 and Phase 13 support.

- character reference planning
- environment reference planning
- candidate registration
- approval
- rejection
- locking
- manifest reporting

### `future/*`

Explicit placeholders for later phases.

- shot keyframe generation
- audio generation / recording integration
- video generation and assembly

## Stage Order

The CLI stage registry should follow this order:

1. Phase 1 - ingest and upstream book extraction
2. Phase 7 - character bible synthesis
3. Phase 8 - environment bible synthesis
4. Phase 9 - scene contracts
5. Phase 9.5 - scene binding and environment selection
6. Phase 10 - shot planning and shot packages
7. Phase 11 - dialogue, timing, and edit-aware sequencing
8. Phase 11.5 - prompt preparation and reference pack assembly
9. Phase 11.7 - descriptor enrichment and reference coverage
10. Phase 11.8 - quality grading and selective reruns
11. Phase 12 - character sheet generation and approval
12. Phase 13 - environment reference generation and approval
13. Phase 14 - scene and shot keyframe generation placeholder
14. Phase 15 - audio placeholder
15. Phase 16 - video placeholder
16. Phase 17 - review, lock, and regenerate workflow

Phase 1 remains upstream and is usually skipped in the quick test. Phases 14-17 are placeholders until those systems are implemented.

## Command Surface

The CLI should expose the following families of commands:

### Pipeline commands

- `test-pipeline`
  - run the compact quick test on a small slice
  - include or exclude bible refreshes
  - default to chapters `2-3`
  - default to `princess_of_mars_test`

- `status`
  - show artifact state by phase and family
  - show stale, missing, blocked, and approved items
  - show last update timestamps and dependency hints

- `rerun`
  - rerun from any phase
  - optionally stop at a target phase
  - optionally rerun only stale artifacts
  - optionally limit chapters or entities

### Synthesis commands

- `synthesize-character-bibles`
- `synthesize-environment-bibles`
- `synthesize-scene-contracts`
- `synthesize-scene-bindings`
- `synthesize-shot-packages`
- `synthesize-dialogue-timeline`
- `synthesize-dialogue-enrichment`
- `synthesize-prompt-preparation`
- `synthesize-descriptor-enrichment`

### Reference asset commands

- `plan-character-references`
- `generate-character-references`
- `register-character-reference-candidate`
- `approve-character-reference`
- `reject-character-reference`
- `lock-character-reference`
- `plan-environment-references`
- `generate-environment-references`
- `register-environment-reference-candidate`
- `approve-environment-reference`
- `reject-environment-reference`
- `lock-environment-reference`

### Quality and review commands

- `grade-artifacts`
- `rerun-quality-artifacts`
- `clear-descriptor-artifacts`
- `refine-identities`

## Status Model

The CLI should classify artifacts using a small stable state set:

- `missing`
- `generated`
- `review-needed`
- `blocked`
- `approved`
- `stale`
- `superseded`
- `locked`

The status layer should report:

- artifact path
- artifact family
- last modified time
- upstream dependency state
- whether the artifact can be reused
- whether it must be rebuilt or only reviewed

## Rerun Model

The rerun planner should support:

- rerun from a specific phase
- rerun up to a specific phase
- rerun only stale artifacts
- rerun only missing artifacts
- rerun only failed artifacts
- rerun only a chapter slice
- rerun only a limited set of entities

Reruns should default to non-destructive behavior.

## Quick Test Behavior

The CLI quick-test command should mirror the current quick-test folder:

1. clear downstream artifacts
2. optionally refresh a small slice of character bibles
3. optionally refresh a small slice of environment bibles
4. run scene contracts
5. run scene bindings
6. run shot packages
7. run dialogue timeline
8. run descriptor enrichment
9. run prompt preparation
10. run quality grading

Recommended defaults:

- project slug: `princess_of_mars_test`
- chapters: `2-3`
- character bible limit: `3`
- environment bible limit: `3`
- bible refresh off unless explicitly requested

## Placeholder Future Phases

The CLI package should contain explicit future modules so the pipeline order is visible even before those phases are implemented:

- `future/shot_keyframes.py`
- `future/audio.py`
- `future/video.py`

These modules should not do real work yet. They should define command stubs, help text, and stage metadata so the eventual implementation has a stable place to land.

## Migration Plan

### Step 1: Create the CLI package

Add the new `orchestrator/cli/` package and move parser and dispatch logic into it.

### Step 2: Keep compatibility

Keep `orchestrator/__main__.py` as a thin wrapper into the new package.

### Step 3: Preserve existing behavior

Ensure the new CLI supports all commands currently available through `orchestrator/cli.py`.

### Step 4: Add status and rerun layers

Implement artifact state reporting and dependency-aware rerun planning.

### Step 5: Add the quick-test command

Replace the bat-driven quick test with a CLI command that can be launched directly.

### Step 6: Add Phase 12/13 support

Hook the CLI into character and environment reference planning and generation.

### Step 7: Add future placeholders

Create explicit future command groups for the later production phases.

### Step 8: Deprecate bats gradually

Once the CLI is stable, bats can remain as optional wrappers or be removed later.

## Recommended Implementation Order

1. `context.py`
2. `models.py`
3. `stages.py`
4. `parser.py`
5. `main.py`
6. `status.py`
7. `rerun.py`
8. `test_pipeline.py`
9. `bibles.py`
10. `reference_assets.py`
11. `future/shot_keyframes.py`
12. `future/audio.py`
13. `future/video.py`

## Acceptance Criteria

The CLI work is ready when:

- the current commands still work through the new package
- the quick-test workflow can run without bats
- the CLI can print artifact status by phase
- the CLI can rerun from any phase boundary
- the CLI can refresh a limited slice of bible outputs
- the CLI can plan and manage Phase 12 and 13 reference assets
- the CLI includes explicit placeholders for future phases
- the order of operations is readable and consistent

## Notes on Existing Bats

The current bats are useful as temporary launchers and as a human-friendly safety net. They should eventually become wrappers around the CLI, not parallel implementations of pipeline logic.

## Summary

The long-term control surface for FilmCreator should be a Python CLI package, not a launcher folder.

That CLI should:

- know the pipeline order
- know the artifact lifecycle
- know what is stale and what is reusable
- support quick validation and partial reruns
- support limited bible refreshes
- support Phase 12 and 13 planning and generation
- reserve explicit space for later phases

The bats can remain temporarily, but the CLI should become the authoritative execution path.

