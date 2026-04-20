# FilmCreator Implementation Roadmap

## Goal

Ship a local-first, shot-oriented pipeline that can:

1. analyze a chapter into an ordered scene list,
2. author every scene in that chapter into shots and prompt packages,
3. render review batches for each internal clip/shot unit without hand-editing workflow JSONs,
4. record review decisions and approvals in state,
5. generate motion from approved keyframes,
6. evolve cleanly into a persistent multi-chapter world model without discarding the file-first workflow.

## Working Principles

- Local generation is the product core.
- LM Studio and ComfyUI are separate phases on VRAM-constrained hardware.
- User-facing language should prefer `shot`, while internal implementation may continue using `clip_id` until a later refactor.
- Previous-shot video last frame is an optional continuity tool, not the universal default next-shot source.
- Every generated stage is batch-first and review-gated.
- The next stage only advances from one approved primary candidate.
- Overnight runs are stage-bounded. Human review remains the boundary between stage families unless we later add an explicit auto-advance mode.
- Optional post-keyframe identity-consistency and anatomy-repair assists should plug in as corrective still passes, not as hidden replacements for the base keyframe stage.
- All LLM output must be tagged Markdown packets, never strict raw JSON.
- All rigid JSON structures must be produced by local forgiving parsers.
- The system remains file-first until the multi-chapter world model stabilizes enough to justify SQLite.

## Current Validated Checkpoint

- A clip-scoped `keyframe` batch can render successfully through the clean Comfy path.
- `RUN_0001` produced four clip-local keyframe candidates in:
  - `projects/pilot_scene/05_scenes/SC001/clips/CL001/stills/keyframes/`
- A short-cut `cut_motion` batch can also render successfully from the approved keyframe.
- `RUN_0040` produced four clip-local short video candidates in:
  - `projects/pilot_scene/05_scenes/SC001/clips/CL001/video/`
- The orchestrator can now:
  - scaffold clip folders and prompt packages,
  - generate 4 style-profile prompt variants,
  - patch the canonical four-ref still workflow,
  - patch the primary Wan 5B short-cut motion workflow,
  - submit live still and short-motion render jobs,
  - route still and video outputs into canonical clip folders,
  - record batch manifests with per-candidate metadata,
  - record top 2 and chosen primary review results for keyframes,
  - promote the chosen keyframe into `approved_keyframe`,
  - update `clip_state.json` so continuity resolves from the approved keyframe,
  - review and approve short-cut motion batches through the manifest-backed review helper,
  - promote the chosen video into `approved_video`,
  - extract `approved_video_last_frame` into the canonical clip still hierarchy.
- Chapter-based authoring for `princess_of_mars_test` is live and substantially more resilient than the original strict-JSON version.
- Chapter-scoped scene ids such as `CH008_SC001` are now live in the authoring outputs.
- Scene-level authoring and chapter-level authoring cascade functions exist.
- Book-level chapter batches now continue after per-chapter failures, write run summaries and failed-chapter artifacts, and support retrying only the latest failed chapters.

## Current Project Status

- `analyze-chapter` and `plan-scene` are working and now have live task timing output.
- Shared character/environment prompt writing is running one asset per LM Studio call.
- Clip/shot prompt writing has been migrated to tagged Markdown packet output with local parsing.
- Scene planning is now tolerant of several non-canonical clip-id formats and duplicate post-normalization collisions.
- The multi-chapter book-run layer now records resilient run state under `02_story_analysis/runs/` and keeps the failure log inspectable without stopping the manifest run.
- The project is still intentionally file-first; SQLite remains deferred until the world model is stable enough to avoid churn.
- Phase B.1 has started with canonical character/environment registry scaffolding.

## Current Risks And Known Gaps

- Canonical identity is not yet fully integrated back into chapter authoring outputs.
- Shared prompt generation still needs to prefer canonical assets where available.
- Scene-to-scene continuity inheritance is not yet active.
- The SQLite relational layer is still a future migration, not a current implementation target.
- Multi-chapter world state should build on top of canonical identity and chapter continuity, not replace them.
- Post-ingest identity refinement is now a separate batch step and should stay separate from chapter ingest.

## Agreed Sequencing From Here

This is the authoritative order we want to follow.

### Stage A – Structural Authoring Backbone (complete enough to build on)

#### Result

The current `princess_of_mars_test` checkpoint now has a real structural backbone:

- chapter-scoped scene ids
- resilient packet parsing and retries
- scene-level planning and prompt writing
- chapter-level scene cascade entrypoints
- bounded malformed-record handling

#### Remaining A-adjacent work

- stable launcher/CLI coverage for chapter-wide scene authoring
- final operator-facing terminology cleanup (`clip` -> `shot`)

### Stage B – Canonical Identity And Continuity

#### Goal

Add the first true film-memory layer to the authoring system.

#### Stage B.1 – Canonical identity registries

##### Scope

- canonical character registry
- canonical environment registry
- provisional identity support
- alias resolution
- post-analysis registry resolution pass
- shared prompt writing preference for canonical assets where available

##### Deliverables

- `02_story_analysis/world/CHARACTER_REGISTRY.json`
- `02_story_analysis/world/ENVIRONMENT_REGISTRY.json`
- canonical/provisional status in authoring summaries
- chapter analysis hooks that write registry artifacts automatically

##### Verification

- obviously duplicated character aliases are merged into one canonical asset
- generic role labels remain provisional unless explicitly resolved
- environment families can be reused without uncontrolled duplication
- shared prompt writing can prefer canonical source sets

#### Stage B.2 – Scene-to-scene continuity inheritance

##### Scope

- chapter continuity state file
- per-scene continuity update pass
- continuity summary fed into later scene planning and shot prompt writing

##### Deliverables

- `02_story_analysis/world/CH###_STATE.json`
- `02_story_analysis/world/CH###_CONTINUITY_SUMMARY.md`
- scene planning prompts that inherit prior-scene state

##### Verification

- later scenes preserve prior events, emotional state, and environmental changes
- state is auditable and scene-bounded
- continuity prompts stay concise enough to remain useful

#### Stage B.3 – Chapter storyboard artifact

##### Scope

- chapter-wide storyboard markdown and json summary
- ordered scenes
- ordered shots per scene
- estimated durations and continuity notes

##### Deliverables

- `02_story_analysis/storyboards/CH###_storyboard.md`
- `02_story_analysis/storyboards/CH###_storyboard.json`

##### Verification

- one file can summarize the whole chapter before rendering begins
- scene and shot timing is reviewable without opening every clip file manually

### Stage C – Output Review / Rework Layer

#### Goal

Add quality control after structural stability and canonical identity are in place.

#### Planned Capabilities

- reviewer pass for character roster quality
- reviewer pass for scene/shot planning quality
- targeted rework for weak outputs
- automated retry reasons plus optional reviewer explanation

### Stage D – File-First Multi-Chapter World Model

#### Goal

Support ingestion of a full book and chapter-by-chapter world updates while remaining file-first.

#### Why It Now Starts Later Than B

- canonical identity and chapter continuity are prerequisites
- the world model should build on stable character and environment entities

### Stage E – Revision / Timeline / Snapshot Layer

#### Goal

Support long-form continuity and future scene generation from time-correct state.

### Stage F – SQLite Migration

#### Goal

Add a queryable relational layer **after** file-first world semantics are stable.

## Database Implementation Timing

- SQLite should be implemented only after the world model semantics are stable enough to deserve schema permanence.
- The first SQLite release should be:
  - per-project
  - SQLite
  - file-synced
  - read-mostly
- Markdown, JSON, and media files remain canonical artifacts in the first database release.
- SQLite should accelerate querying and reporting, not replace the file-first authoring system prematurely.

## Near-Term Verification Matrix

### Verification Group 1 – Chapter Authoring Stability

- chapter analysis completes without uncaught exception
- scene planning completes for scoped scenes
- scene prompt writing completes for planned scenes
- warnings/failures remain bounded and inspectable

### Verification Group 2 – Shot Planning Robustness

- non-canonical clip ids are normalized or skipped with warnings
- duplicate normalized ids do not corrupt outputs
- planned shots stay reviewable and duration-targeted

### Verification Group 3 – Identity Resolution Robustness

- canonical registries are written deterministically
- provisional identities remain explicit instead of forcing bad merges
- shared prompt writing can prefer canonical assets when available

### Verification Group 4 – Logging / Debuggability

- every LM Studio call logs start and finish
- retries log a reason
- durations are visible
- relevant log files exist on disk

## End-To-End Delivery Plan

### Phase 0: Stabilize The Validated Keyframe Batch

#### Goal

Turn the first successful keyframe render into a clean, repeatable baseline.

### Phase 1: Review And Approved Keyframe Handoff

#### Goal

Make the first real human approval step complete and reproducible.

### Phase 2: Still-Fix Loop

#### Goal

Support corrective still batches after keyframe review.

### Phase 3: Short-Cut Motion Smoke Path

#### Goal

Prove one approved keyframe can drive one normal movie-cut video generation without chained follow-on segments.

### Phase 4: Video Review And Last-Frame Continuity Handoff

#### Goal

Close the loop between motion generation and continuity state.

### Phase 5: LM Studio Authoring Integration

#### Goal

Automate planning and prompt writing without changing the runner contract.

#### Current Implementation Note

- `lmstudio-check` is implemented.
- `write-prompts` is implemented for clip-local prompt families.
- chapter-based authoring is active.
- scene-level and chapter-level cascade functions now exist.
- the current next priority is Phase B canonical identity integration and then continuity inheritance.

### Phase 5.1: Chapter-Based Authoring Pilot

#### Goal

Prove the authoring pipeline on a real public-domain chapter before any database migration.

#### Current Reality

- Chapter VIII of `princess_of_mars_test` has live chapter analysis, four-scene decomposition, scoped scene ids, Scene 1 beat/shot planning, and full prompt writing.
- chapter-wide cascade authoring is now the next practical validation layer.

### Phase 5.5: SQLite Relational Layer

#### Goal

Add a queryable local relational layer after authoring, canonical identity, and world-model concepts have stabilized.

### Phase 6: Scene-Wide Planning

#### Goal

Prepare an entire scene in one authoring pass before any rendering begins.

#### Current Reality

- Scene-wide authoring is now structurally available through the scene authoring function and chapter authoring cascade branch work.
- the next missing layer is continuity-aware scene planning, not basic scene planning existence.

### Phase 7: Overnight Scene Batch Rendering

#### Goal

Render a full scene in unattended overnight passes without skipping required human review gates.

### Phase 8: Cross-Cut Continuity And Batch Video Completion

#### Goal

Make scene-wide cut progression robust enough for longer unattended runs.

## Recommended Build Order From Here

1. Finish Phase B.1 registry integration into chapter authoring.
2. Add Phase B.2 scene-to-scene continuity inheritance.
3. Add chapter storyboard generation.
4. Add reviewer / rework support for weak but syntactically valid outputs.
5. Then begin file-first multi-chapter ingest and broader world-state migration.
6. Add revision, contradiction, and snapshot tooling.
7. Only after those stabilize, implement the SQLite read-side sync layer.
8. Continue motion-path and batch-render improvements on top of the stabilized authoring foundation.
