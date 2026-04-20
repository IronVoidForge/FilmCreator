# Refactor Progress Plan

## Goal

Turn the current flat `orchestrator` package into a maintainable feature-based codebase with clear boundaries between:

- CLI entrypoints
- domain/application services
- shared core utilities
- external adapters

The main objective is to make the codebase easier to extend without creating more monolithic modules.

## Progress Snapshot

Completed:

- `story_authoring.py` split into feature modules and compatibility wrappers
- `world_global.py` split into feature modules and compatibility wrappers
- `runner.py` split into feature modules and compatibility wrappers
- `batch_runner.py` split into feature modules and compatibility wrappers
- `scaffold.py` split into feature modules and compatibility wrappers
- `state.py` split into feature modules and compatibility wrappers
- `review_tools.py` split into feature modules and compatibility wrappers
- `book_ingest.py` now writes `book_index.json`
- `common.py` has been reduced into `core/` helpers
- authoring parser/repair hardening is in place
- chapter-summary, character, environment, and scene recovery flows are in place
- book librarian retrieval and character/environment matching helpers are in place

Still in progress:

- `authoring.py`
- `book_authoring.py`
- `cli.py`
- `workflow_patcher.py`
- final cleanup and import consolidation

## Refactor Principles

1. Keep `cli.py` thin.
2. Keep pure transformations separate from file I/O and network calls.
3. Prefer feature packages over a single utility-heavy package.
4. Introduce classes only where they clarify a workflow or boundary.
5. Preserve existing behavior first, then improve structure.
6. Move in small steps so tests stay meaningful at each stage.

## Proposed Target Layout

```text
orchestrator/
  cli.py
  core/
    paths.py
    json_io.py
    validation.py
    settings.py
    prompt_package.py
    style_profiles.py
  adapters/
    comfy_client.py
    lmstudio_client.py
    video_utils.py
    registry_loader.py
  features/
    authoring/
      chapter_analysis.py
      scene_planning.py
      shared_prompts.py
      continuity.py
      prompt_writer.py
      packet_parser.py
    world/
      character_registry.py
      environment_registry.py
      snapshots.py
      sequence.py
      failure_log.py
    runs/
      still_run.py
      batch_run.py
      workflow_resolution.py
      output_routing.py
    projects/
      bootstrap.py
      manifests.py
      promotion.py
    review/
      candidate_catalog.py
      review_service.py
      interactive_session.py
    book/
      ingest.py
      analysis.py
```

## File Size Targets

These numbers are meant to be practical budgets, not hard law. The goal is to keep individual files small enough that they can be understood and changed without constantly scrolling through unrelated code.

For the large current files, the target is to split them into smaller files in the new package layout. For modules that remain mostly intact, the target is to keep them compact and single-purpose.

| File | Current lines | Target lines after refactor | Status | Notes |
|---|---:|---:|---|---|
| `orchestrator/story_authoring.py` | 2,593 | 250-500 per file | COMPLETE | Split into authoring feature modules. |
| `orchestrator/authoring.py` | 855 | 250-400 per file | IN PROGRESS | Split prompt writing concerns into dedicated authoring submodules. |
| `orchestrator/world_global.py` | 778 | 200-450 per file | COMPLETE | Split registry, snapshot, and sequence logic. |
| `orchestrator/runner.py` | 722 | 200-350 per file | COMPLETE | Split planning, execution, routing, and cleanup. |
| `orchestrator/batch_runner.py` | 511 | 180-300 per file | COMPLETE | Split batch planning from batch execution. |
| `orchestrator/scaffold.py` | 501 | 150-300 per file | COMPLETE | Split project bootstrap, manifests, and promotion. |
| `orchestrator/cli.py` | 390 | 120-220 per file | IN PROGRESS | Keep thin; if it stays one file, stay under the target budget. |
| `orchestrator/state.py` | 315 | 120-250 per file | COMPLETE | Split normalization, continuity, and review state handling. |
| `orchestrator/world_registry.py` | 271 | 150-250 per file | IN PROGRESS | Likely stay mostly intact or split lightly if needed. |
| `orchestrator/workflow_patcher.py` | 253 | 180-260 | IN PROGRESS | Can remain a single utility module unless new patching formats grow. |
| `orchestrator/lmstudio_client.py` | 247 | 180-260 | IN PROGRESS | Keep as one adapter unless transport behavior expands. |
| `orchestrator/review_tools.py` | 231 | 120-220 per file | COMPLETE | Split review catalog, service, and interactive flow. |
| `orchestrator/book_authoring.py` | 727 | 150-300 per file | IN PROGRESS | Now includes resilient book-run tracking, failed-chapter retry, and refinement entrypoints; should be split once the new batch flow settles. |
| `orchestrator/prompt_package.py` | 159 | 120-200 | IN PROGRESS | Fine as a compact parser/serializer. |
| `orchestrator/book_ingest.py` | 136 | 100-180 | COMPLETE | Fine as a compact ingestion helper. |
| `orchestrator/comfy_client.py` | 132 | 100-180 | IN PROGRESS | Keep as a single adapter. |
| `orchestrator/style_profiles.py` | 126 | 100-180 | IN PROGRESS | Keep as a single policy module. |
| `orchestrator/video_utils.py` | 104 | 80-150 | IN PROGRESS | Keep as a single adapter unless more extraction backends are added. |
| `orchestrator/common.py` | 59 | 40-120 per file | COMPLETE | This has been decomposed into core utility modules. |

## Priority Plan

### P0 - Highest Value, Highest Risk

These are the first changes to make because they remove the biggest maintenance bottlenecks.

#### 1. Split `orchestrator/story_authoring.py` [COMPLETE]

- Priority: `P0`
- Difficulty: `Hard`
- Why first: this is the largest and most complex module in the repository.
- Main extraction targets:
  - `ChapterAnalysisService`
  - `ScenePlanningService`
  - `SharedPromptService`
  - `ChapterContinuityService`
  - `PromptPacketParser`
  - `PromptArtifactWriter`
  - `AssetIdNormalizer`
  - `MarkdownBundleReader`

Suggested file split:

- `orchestrator/features/authoring/chapter_analysis.py`
- `orchestrator/features/authoring/scene_planning.py`
- `orchestrator/features/authoring/shared_prompts.py`
- `orchestrator/features/authoring/continuity.py`
- `orchestrator/features/authoring/prompt_writer.py`
- `orchestrator/features/authoring/packet_parser.py`

Notes:

- Keep the dataclasses for public summaries in the feature package.
- Move pure parsing helpers first, then move orchestration logic.
- Keep prompt templates and packet parsing testable without filesystem setup where possible.

#### 2. Split `orchestrator/world_global.py` [COMPLETE]

- Priority: `P0`
- Difficulty: `Hard`
- Why second: it mixes registry mutation, snapshot projection, and persistence.
- Main extraction targets:
  - `WorldPathResolver`
  - `CharacterRegistryService`
  - `EnvironmentRegistryService`
  - `WorldSnapshotService`
  - `WorldSequenceService`
  - `WorldFailureLogService`

Suggested file split:

- `orchestrator/features/world/character_registry.py`
- `orchestrator/features/world/environment_registry.py`
- `orchestrator/features/world/snapshots.py`
- `orchestrator/features/world/sequence.py`
- `orchestrator/features/world/failure_log.py`

Notes:

- Keep normalization and visibility/projection rules separate from file writing.
- Preserve provenance logic as explicit service methods.

#### 3. Split `orchestrator/runner.py` [COMPLETE]

- Priority: `P0`
- Difficulty: `Hard`
- Why third: it is a core execution path and currently combines planning, patching, execution, routing, and cleanup.
- Main extraction targets:
  - `StillRunPlanner`
  - `RunExecutor`
  - `WorkflowResolver`
  - `OutputRouter`
  - `StagingManager`

Suggested file split:

- `orchestrator/features/runs/still_run.py`
- `orchestrator/features/runs/workflow_resolution.py`
- `orchestrator/features/runs/output_routing.py`

Notes:

- Keep `PreparedRun` and `RunSummary` close to the planner/executor.
- Preserve the existing behavior around blockers and warnings.

### P1 - Strong ROI, Medium Risk

These modules are easier than the P0 group and should be done once the new package structure exists.

#### 4. Split `orchestrator/batch_runner.py` [COMPLETE]

- Priority: `P1`
- Difficulty: `Medium`
- Main extraction targets:
  - `BatchPromptPlanner`
  - `BatchCandidateBuilder`
  - `BatchRunExecutor`
  - `BatchWorkflowResolver`

Suggested file split:

- `orchestrator/features/batches/batch_plan.py`
- `orchestrator/features/batches/batch_execute.py`

Notes:

- This module is already a clean pipeline and should become a smaller set of explicit steps.

#### 5. Split `orchestrator/scaffold.py` [COMPLETE]

- Priority: `P1`
- Difficulty: `Medium`
- Main extraction targets:
  - `ProjectBootstrapper`
  - `SceneBootstrapper`
  - `ClipBootstrapper`
  - `RunManifestFactory`
  - `AssetPromoter`
  - `VideoFrameSyncService`

Suggested file split:

- `orchestrator/features/projects/bootstrap.py`
- `orchestrator/features/projects/manifests.py`
- `orchestrator/features/projects/promotion.py`

Notes:

- This file is doing three distinct jobs today: workspace creation, manifest creation, and asset promotion.

#### 6. Split `orchestrator/state.py` [COMPLETE]

- Priority: `P1`
- Difficulty: `Medium`
- Main extraction targets:
  - `ClipStateRepository`
  - `ClipStateNormalizer`
  - `ContinuitySourceResolver`
  - `ReviewBatchRecorder`
  - `StylePreferenceUpdater`

Suggested file split:

- `orchestrator/features/state/clip_state.py`
- `orchestrator/features/state/continuity.py`
- `orchestrator/features/state/review_batches.py`
- `orchestrator/features/state/style_preferences.py`

Notes:

- The normalization rules should be their own unit-tested module.
- Recording review batches should be a higher-level service on top of state persistence.

#### 7. Split `orchestrator/review_tools.py` [COMPLETE]

- Priority: `P1`
- Difficulty: `Medium`
- Main extraction targets:
  - `ReviewCandidateCatalog`
  - `BatchReviewService`
  - `InteractiveReviewSession`

Suggested file split:

- `orchestrator/features/review/candidate_catalog.py`
- `orchestrator/features/review/review_service.py`
- `orchestrator/features/review/interactive_session.py`

Notes:

- Keep interactive prompting separated from review business rules.

#### 8. Split `orchestrator/authoring.py` [IN PROGRESS]

- Priority: `P1`
- Difficulty: `Medium`
- Main extraction targets:
  - `PromptTargetResolver`
  - `PromptPackageAuthoringService`
  - `PromptPacketParser`
  - `PromptExchangeLogWriter`
  - `PromptFailureArtifactWriter`

Suggested file split:

- `orchestrator/features/authoring/prompt_writer.py`
- `orchestrator/features/authoring/packet_parser.py`

Notes:

- This should live in the same feature area as `story_authoring.py`, but as a separate submodule because clip prompt writing is a distinct use-case.

### P2 - Cleanup and Consolidation

These are worthwhile, but they should come after the major workflow modules are stabilized.

#### 9. Split `orchestrator/book_authoring.py` and `orchestrator/book_ingest.py` [PARTIALLY COMPLETE]

- Priority: `P2`
- Difficulty: `Low to Medium`
- Main extraction targets:
  - `BookIngestor`
  - `BookAnalysisOrchestrator`
  - `BookChapterPipeline`
  - `BookRunSummary`
  - `ChapterRunResult`
  - `FailedChapterRetryService`

Suggested file split:

- `orchestrator/features/book/ingest.py`
- `orchestrator/features/book/analysis.py`
- `orchestrator/features/book/recovery.py`

Notes:

- This is a good final step because it becomes much simpler once authoring and world state are modular.
- The book-analysis module now also owns resilient manifest runs, failed-chapter artifacts, and retry-only recovery, so that behavior should stay stable before extracting more files.

#### 10. Split `orchestrator/common.py` [COMPLETE]

- Priority: `P2`
- Difficulty: `Low`
- Main extraction targets:
  - `paths.py`
  - `json_io.py`
  - `validation.py`

Suggested file split:

- `orchestrator/core/paths.py`
- `orchestrator/core/json_io.py`
- `orchestrator/core/validation.py`

Notes:

- This file is currently a shared utility bucket and should be reduced once the higher-level packages are in place.

## What Should Stay Mostly As-Is

These modules are already reasonably focused and do not need immediate class-heavy refactoring:

- `orchestrator/prompt_package.py`
- `orchestrator/workflow_patcher.py`
- `orchestrator/lmstudio_client.py`
- `orchestrator/comfy_client.py`
- `orchestrator/style_profiles.py`
- `orchestrator/video_utils.py`
- `orchestrator/registry_loader.py`

They may eventually move into `core/` or `adapters/`, but their internal shape is already good.

## Recommended Class Hierarchy

The codebase should use classes where the object represents a workflow boundary, not just a helper namespace.

Good candidates for classes:

- Services that orchestrate multiple steps
- Repositories that load and store state
- Parsers that transform text into structured data
- Writers that persist artifacts and logs
- Clients that talk to external systems

Good candidates for functions:

- Small pure transformations
- Validation helpers
- Path helpers
- String normalization helpers
- Simple data extraction utilities

## Execution Order

1. `story_authoring.py` [COMPLETE]
2. `world_global.py` [COMPLETE]
3. `runner.py` [COMPLETE]
4. `batch_runner.py` [COMPLETE]
5. `scaffold.py` [COMPLETE]
6. `state.py` [COMPLETE]
7. `review_tools.py` [COMPLETE]
8. `authoring.py` [IN PROGRESS]
9. `book_authoring.py` and `book_ingest.py` [PARTIALLY COMPLETE]
10. `common.py` [COMPLETE]

## Testing Strategy

Each refactor step should keep or improve test coverage.

- Add or preserve unit tests around pure parsing and normalization logic first.
- Keep integration behavior covered for orchestration services.
- Prefer small tests for service boundaries instead of huge end-to-end tests.
- When a module is split, move its tests to match the new package structure.

## Confidence And Migration Plan

### Confidence Level

- One-shot refactor with only minimal verification: `50-60%`
- Refactor with phased passes and tests after each pass: `85-90%`

The lower one-shot confidence comes from the amount of shared filesystem state, manifest schemas, and cross-module orchestration in this repo.

### Recommended Number Of Passes

Use `4` passes minimum, `5` if we want to be cautious.

Current pass status:

- Pass 1: COMPLETE
- Pass 2: COMPLETE
- Pass 3: COMPLETE
- Pass 4: PARTIALLY COMPLETE
- Pass 5: PENDING

#### Pass 1: Core And Utilities

- Goal: create the new package structure and move low-risk utilities first.
- Main targets:
  - `orchestrator/prompt_package.py`
  - `orchestrator/style_profiles.py`
  - `orchestrator/workflow_patcher.py`
  - `orchestrator/common.py` split into `core/` modules
- Intended outcome:
  - `core/`, `adapters/`, and `features/` exist
  - pure helpers are isolated from feature orchestration

Tests to run:

- `pytest tests/unit/test_prompt_package.py`
- `pytest tests/unit/test_workflow_patcher.py`
- `pytest tests/unit/test_state.py` if shared helpers moved into `core/`
- import smoke tests for the refactored modules

#### Pass 2: Authoring

- Goal: break up `story_authoring.py` and `authoring.py`.
- Main targets:
  - chapter analysis
  - scene planning
  - shared prompt writing
  - prompt parsing
  - prompt artifact writing
- Intended outcome:
  - authoring logic is split into feature modules
  - packet parsing is testable independently

Tests to run:

- `pytest tests/unit/test_story_authoring.py`
- `pytest tests/unit/test_authoring.py`
- any new unit tests created for prompt parsing or prompt artifact writing
- a targeted smoke run for chapter analysis or prompt writing if the environment allows it

#### Pass 3: State, World, And Runs

- Goal: split `world_global.py`, `state.py`, `runner.py`, and `batch_runner.py`.
- Main targets:
  - state normalization and continuity resolution
  - world registries and snapshots
  - still-run planning and execution
  - batch planning and batch execution
- Intended outcome:
  - orchestration logic is separated from persistence and domain rules
  - run execution and batch execution are independently testable

Tests to run:

- `pytest tests/unit/test_state.py`
- `pytest tests/unit/test_runner.py`
- `pytest tests/unit/test_batch_runner.py`
- any tests added for world registry or snapshot services

#### Pass 4: Scaffold, Review, Book, And CLI Wiring

- Goal: split `scaffold.py`, `review_tools.py`, `book_authoring.py`, `book_ingest.py`, and update `cli.py` imports.
- Main targets:
  - project bootstrap
  - run manifest creation
  - asset promotion
  - review catalog and interactive review flow
  - book ingestion and book analysis
- Intended outcome:
  - CLI becomes a thin dispatch layer
  - project-scaffolding responsibilities are explicit
  - review and book workflows have clearer service boundaries

Tests to run:

- `pytest tests/unit/test_scaffold.py`
- `pytest tests/unit/test_review_tools.py`
- any book workflow tests added during the refactor
- CLI smoke tests for the major commands

#### Pass 5: Cleanup And Compatibility Removal

- Goal: remove temporary compatibility shims, flatten imports, tighten names, and simplify the final package surface.
- Intended outcome:
  - no leftover transitional modules unless they serve a deliberate compatibility role
  - package imports are stable and intuitive

Tests to run:

- full `pytest`
- import smoke tests across the package
- one sample-project workflow smoke test covering:
  - project init
  - chapter analysis
  - prompt writing
  - run planning
  - batch planning
  - review recording

### Stop And Check Criteria

Do not move to the next pass until:

- the current pass tests are green
- the public APIs used by the next pass are still working
- no file import paths are broken
- any temporary compatibility layer is documented or removed intentionally

## Success Criteria

The refactor is successful when:

- No feature module exceeds a comfortable size for single-file reasoning.
- Each package has a clear responsibility.
- CLI handlers only parse arguments and call services.
- Parsing, state management, and external I/O are testable independently.
- New feature work can be added without editing a giant central file.
