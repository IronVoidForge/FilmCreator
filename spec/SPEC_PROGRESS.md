# Spec Progress

## Current Project Status

The refactor foundation is in place and the project has moved beyond basic ingest hardening.

The latest validated state is:

- the refactor branch has merged into `main`
- multi-chapter analysis for `princess_of_mars_test` completed `28/28` chapters with `0` failures
- chapter analysis, world registries, snapshots, continuity, and librarian/index retrieval are stable enough to build on
- the current bottleneck is no longer extraction correctness
- the current bottleneck is synthesis and production-facing contract generation

## Status Legend

- `planned`
  - the spec is accepted as a target but has not been implemented yet
- `implemented`
  - code or structure exists, but the acceptance criteria have not been validated yet
- `validated`
  - at least one real validation checkpoint has passed, but the full acceptance criteria are not complete yet
- `complete`
  - the acceptance criteria have been validated end to end
  - when a spec reaches this state, its filename may be renamed with the suffix `__complete.md`

## Foundation Status

### 1.1 repo, project, scene, and clip hierarchy
- status: `validated`
- evidence: runtime scene work, authoring outputs, render-stage clip folders, and the refactor launchers all use the canonical hierarchy under `projects/<project_slug>/...`
- next validation: keep the same hierarchy guarantees while adding bible, scene-package, and shot-package layers

### 1.2 IDs, filenames, and naming rules
- status: `validated`
- evidence: chapter-scoped scene ids such as `CH008_SC001` are live while render-stage shot assets still use canonical filenames such as `SC001_CL001_KF01_v001.png`
- next validation: extend naming discipline into character bibles, environment bibles, scene contracts, shot packages, and dialogue timeline artifacts

### 1.3 workflow catalog and registry contract
- status: `complete`
- evidence: live workflow selection continues to resolve through the registry and clean runner paths

### 1.4 prompt package schema
- status: `validated`
- evidence: packetized authoring and prompt-package writing are live and resilient
- next validation: consume expanded prompt schema through the future shot-package and production contract layers

### 1.5 project, scene, and clip state contracts
- status: `validated`
- evidence: `clip_state.json` records approved assets, review history, continuity source, and prompt-package references; book-level run artifacts now also track failed chapter recovery state
- next validation: extend state contracts with artifact lifecycle, staleness, approval, and dependency metadata for synthesis and production phases

### 1.6 SQLite relational model
- status: `planned`
- evidence: SQLite remains deferred until the file-first production contracts stabilize
- next validation: revisit only after phases 7–11 contracts and lifecycle semantics are stable

## Shared Asset Foundation

### 2.1 character reference generation
- status: `validated`
- evidence: shared character prompt writing exists and can operate from analysis outputs
- next validation: upgrade from reference prompt generation into canonical character bible synthesis and approved character reference bundles

### 2.2 environment reference generation
- status: `validated`
- evidence: shared environment prompt writing exists and can operate from analysis outputs
- next validation: upgrade from reference prompt generation into canonical environment bible synthesis and approved environment reference bundles

### 2.3 shared ref promotion and reuse
- status: `implemented`
- evidence: promotion logic exists in scaffold/state flows
- next validation: integrate that logic into future approved bible-driven reference bundle workflows

## Clip / Render Pipeline Foundation

### 3.1 clip input contract
- status: `validated`
- evidence: keyframe and motion batches consume clip-scoped prompt packages and route outputs correctly; chapter authoring also emits explicit clip/shot rosters
- next validation: adapt this contract cleanly into future shot-package architecture rather than leaving it as the final planning abstraction

### 3.2 scene build and golden frame
- status: `validated`
- evidence: live clip-scoped keyframe batch rendered successfully with review and promotion
- next validation: use bible- and scene-contract-driven shot plans to improve generation consistency upstream

### 3.3 anchor and interval frames
- status: `implemented`
- evidence: continuation workflow registry, continuity-source resolver, and current continuity tracking exist
- next validation: tie continuation logic into future edit timeline and shot-sequencing contracts

### 3.4 clip review and selection
- status: `validated`
- evidence: review/promotion helpers work for still and motion batches
- next validation: extend the same approval model upward to scene packages, shot packages, and future character/environment reference bundles

## Orchestration Foundation

### 4.1 runner CLI and job dispatch
- status: `validated`
- evidence: runner commands, scene/chapter authoring entrypoints, and render dispatch are live
- next validation: expose the next synthesis and contract phases as first-class CLI commands

### 4.2 ComfyUI client and workflow patching
- status: `validated`
- evidence: live still and short-motion workflow patching remain operational
- next validation: consume future shot-package prompt outputs without manual conversion layers

### 4.3 output routing, logging, and manifests
- status: `validated`
- evidence: render outputs, manifests, and per-task LM Studio logs are working
- next validation: extend manifests and routing to support scene packages, shot packages, dialogue timelines, and approval queues

### 4.4 automated testing and CI strategy
- status: `implemented`
- evidence: broad unit coverage exists for core authoring and render support
- next validation: expand smoke tests around synthesis, lifecycle, and dependency-aware rebuild logic

### 4.5 resilient chapter batch orchestration and run recovery
- status: `validated`
- evidence: `analyze_book` continues after per-chapter failures, writes run summaries, failed chapter lists, and supports retrying failed chapters only
- next validation: verify retry/reuse behavior against future synthesis stages and stale rebuild workflows

## Analysis / World Model Foundation

### 5.1 story analysis outputs
- status: `complete_enough_to_build_on`
- evidence: chapter analysis, registries, snapshots, continuity summaries, librarian/indexing, and resilient parsing are all working across a full 28/28 chapter run
- next validation: treat this as an upstream input phase for synthesis rather than continuing to expand it as the main product output

### 5.2 clip plan generation
- status: `validated_but_needs_architecture_upgrade`
- evidence: scoped scene planning writes canonical scene, beat, and clip files and remains useful as a structural predecessor
- next validation: adapt useful parts into future scene-contract and shot-package layers through compatibility adapters rather than treating legacy clip planning as the final design

### 5.3 prompt writer integration
- status: `validated`
- evidence: prompt writing, packet parsing, and local prompt package generation are live end to end
- next validation: make prompt writing consume canonical bibles, scene contracts, and shot packages rather than raw analysis-first sources

## Deferred / Future Production Stages

### 6.1 video motion stage
- status: `validated_foundation`
- evidence: a live short-cut motion batch rendered successfully, review/promotion worked, and approved video state updates are live
- next validation: tie motion generation to future shot contracts, edit timelines, and approved reference bundles instead of isolated clip-local scaffolding

### 6.2 acceptance test matrix
- status: `implemented`
- evidence: it continues to act as the checklist for deterministic and live validation
- next validation: expand it to include synthesis, lifecycle, approval, and dependency-aware rebuild checkpoints

## New Active Roadmap Phases

### Phase 7 – Character Bible Synthesis
- status: `planned`
- evidence: upstream registries, refinement inputs, and librarian retrieval now exist to support this phase
- next validation: produce canonical character bibles with evidence refs, revision history, locked fields, and review queues

### Phase 8 – Environment Bible Synthesis
- status: `planned`
- evidence: upstream registries, continuity state, and retrieval now exist to support this phase
- next validation: produce canonical environment bibles with hierarchy rules, evidence refs, revision history, and review queues

### Phase 9 – Scene Production Contracts
- status: `validated`
- evidence: `synthesize-scene-contracts` runs end to end, writes per-scene JSON/markdown contracts, and produces scene review queues and indexes for the full `princess_of_mars_test` book run
- next validation: keep tuning the scene reference resolution and bridge the contracts into shot planning inputs

### Phase 10 – Shot Planning and Shot Packages
- status: `validated`
- evidence: `synthesize-shot-packages` runs end to end, writes per-shot JSON/markdown packages, and produces shot indexes plus review queues for the full `princess_of_mars_test` run
- next validation: tighten shot-to-dialogue and edit-aware sequencing on top of the new shot contract layer

### Phase 11 – Dialogue, Timing, and Edit-Aware Sequencing
- status: `planned`
- evidence: continuity and shot planning foundations now make a formal timing layer feasible
- next validation: produce dialogue maps, shot-to-dialogue bindings, and chapter edit timeline artifacts

## Cross-Cutting Work Newly Required

### Artifact lifecycle and reuse
- status: `planned`
- evidence: the project now needs approved/locked/stale semantics to avoid destructive reruns in synthesis and generation phases
- next validation: define and implement artifact lifecycle metadata and reuse rules

### Dependency graph and staleness
- status: `planned`
- evidence: future phases 7–11 require selective rebuilds based on upstream changes
- next validation: define dependency tracking and stale propagation rules

### Review and approval model
- status: `planned`
- evidence: render review exists, but synthesis and contract layers now need a broader approval system
- next validation: add review queues and approval states across bibles, scene contracts, shot packages, and later generated assets
