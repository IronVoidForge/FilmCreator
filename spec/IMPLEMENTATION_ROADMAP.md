# FilmCreator Implementation Roadmap

## Goal

Ship a local-first, reviewable, resumable film pipeline that can:

1. ingest a book into stable chapter, scene, and world-state artifacts,
2. synthesize canonical character and environment bibles from accumulated evidence,
3. generate continuity-aware scene production contracts,
4. derive ordered shot packages and prompt-ready shot plans,
5. layer dialogue, timing, and edit-aware sequencing on top of shot structure,
6. drive downstream image, audio, and video generation from approved structured contracts,
7. preserve user-reviewed work through non-destructive reruns and dependency-aware rebuilds.

## Current State

- `main` and `origin/main` are synced at commit `db5cf7be57d4656ee271e4592a28b0fa7959ec95`.
- The refactor branch has effectively become `main`.
- The active spec tree now lives under `spec/`.
- The latest full `princess_of_mars_test` run completed `28/28` chapters with `0` failures.
- Multi-chapter authoring now produces stable analysis artifacts, world registries, continuity state, and run-level failure/retry tracking.
- The librarian/index layer exists and can now serve as the retrieval backbone for synthesis stages.
- Phase 8 environment bible synthesis is now implemented and runnable through the CLI and launcher.
- Repair-first retries and chunk fallback are active and materially improved authoring stability.

## Working Principles

- Local generation remains the product core.
- The system is file-first until data semantics stabilize enough to justify a relational sync layer.
- Markdown remains the primary human review surface; JSON remains the machine contract surface.
- All LLM output remains tagged Markdown packet output or packet-compatible text parsed locally.
- Forgiving local parsers remain the authority for rigid structure.
- Every major phase must be reviewable before expensive downstream generation.
- Human approval and locking are first-class workflow concepts, not afterthoughts.
- Reruns must be non-destructive by default.
- Existing valid artifacts should be reviewed/reused when current, marked stale when outdated, and regenerated only when necessary.
- Characters and environments are special incremental assets: later chapters may add evidence, so these artifacts must support evolving synthesis rather than naive overwrite.
- New implementation work should prefer small, composable modules rather than further bloating the large authoring files.

## What Is Complete Enough To Build On

### Phase 1 – Ingest and World Extraction (complete enough)

The project now has a working ingest and extraction foundation:

- chapter summaries
- chapter-scoped character, environment, and scene breakdowns
- canonical/global registries
- chapter-local registries
- world snapshots
- continuity summaries and state files
- resilient book-run orchestration
- failed-chapter retry support
- book librarian/index artifacts

This phase is no longer the main bottleneck.

## What Is Partially Complete But Not The Final Target

### Identity refinement foundation

Identity refinement now exists as a separate post-pass concern and should remain separate from chapter ingest. However, it is not yet the final production-facing identity layer until refinement results are consistently reflected in later synthesis and planning phases.

### Review and recovery operations

The pipeline can recover from many malformed or partial LLM outputs, and book-level failures are no longer all-or-nothing. This is sufficient to move on, though future quality tooling should still improve targeted rework and review ergonomics.

## Current Active Direction

The project has moved from analysis hardening into **canonical synthesis and production contracts**.

The next major work is no longer “make chapter analysis run.”
The next major work is “turn stable analysis into film-usable, reviewable, non-destructive production assets.”

## Authoritative Phase Order From Here

### Phase 7 – Character Bible Synthesis

#### Goal

Turn registry-level character identity and evidence into stable, film-usable canonical character bibles.

#### Inputs

- global character registry
- chapter-local character registries
- chapter character breakdowns
- continuity snapshots and summaries
- refinement decisions
- librarian retrieval of all supporting mentions
- existing character bible if present
- manual overrides / locked fields if present

#### Outputs

- per-character markdown bibles
- per-character JSON contracts
- character bible index
- character review queue
- revision history and evidence references

#### Why It Is Next

Character identity is already strong enough for synthesis, and downstream scene and shot planning improve dramatically once canonical character contracts exist.

### Phase 8 – Environment Bible Synthesis

#### Goal

Turn fragmented environment evidence into stable, reusable, film-usable canonical environment bibles.

#### Inputs

- global environment registry
- chapter-local environment registries
- environment breakdowns
- continuity snapshots and summaries
- scene references
- refinement decisions
- existing environment bible if present
- manual overrides / locked fields if present

#### Outputs

- per-environment markdown bibles
- per-environment JSON contracts
- environment bible index
- environment review queue
- hierarchy-aware continuity notes

#### Why It Follows Phase 7

Scenes and shots need stable people and stable places before they can become production-ready contracts.

#### Current Status

Implemented and runnable.

### Phase 9 – Scene Production Contracts

#### Goal

Turn scene analysis into continuity-aware production contracts that can drive storyboards, shot planning, and downstream generation.

#### Inputs

- scene decomposition outputs
- chapter summaries
- chapter continuity state
- character bibles
- environment bibles
- librarian retrieval
- legacy beat/clip planning artifacts when useful as import seeds

#### Outputs

- per-scene markdown contracts
- per-scene JSON contracts
- scene reference bundles
- chapter storyboard artifacts

#### Why This Is The Bridge Phase

This is the point where FilmCreator stops being “mostly analysis” and becomes a system that can hand structured scene intent to downstream filmmaking steps.

### Phase 10 – Shot Planning and Shot Packages

#### Goal

Convert scene contracts into ordered shot plans and generation-facing shot packages.

- status: `validated`
- evidence: `synthesize-shot-packages` runs end to end, writes per-shot JSON/markdown packages, and produces shot indexes plus review queues for the full `princess_of_mars_test` run
- next validation: tighten shot-to-dialogue and edit-aware sequencing on top of the new shot contract layer

#### Inputs

- scene contracts
- character bibles
- environment bibles
- continuity state
- reusable legacy clip-plan scaffolding where compatible
- style guidance / generation profiles when available

#### Outputs

- shot plans
- shot roster summaries
- shot JSON packages
- shot prompt packages
- shot reference bundles

#### Important Implementation Note

Legacy clip planning should be adapted, not blindly reused as the final architecture. Compatibility adapters are preferred over embedding new logic back into legacy planning code.

### Phase 11.5 â€“ Prompt Preparation and Reference Pack Assembly

#### Goal

Turn canonical bibles, scene contracts, and shot packages into compact, generation-ready prompt bundles for reference-sheet creation and later production prompts.

#### Inputs

- character bibles
- environment bibles
- scene contracts
- shot packages
- continuity state
- style profiles and generation presets
- existing prompt-package schema helpers
- existing shared prompt draft builders

#### Outputs

- per-character reference prompt bundles
- per-environment reference prompt bundles
- per-shot production prompt bundles
- angle and zoom variant bundles
- image-to-image consistency bundles
- prompt package indexes
- prompt review queues

#### Why This Phase Is Needed

The project already knows what the canon is. This phase prepares the prompt families that downstream generation stages can consume without re-deriving prompt structure in multiple places.

#### Current Status

Validated.

### Phase 11.6 â€“ Key Item Index and Reference Pack Assembly

#### Goal

Identify, consolidate, and describe story-significant items that need continuity tracking or future reference-sheet generation.

#### Inputs

- chapter analysis outputs
- scene contracts
- shot packages
- character and environment bibles where items are mentioned
- continuity summaries
- librarian retrieval
- existing prop / item mentions in markdown sources

#### Outputs

- key item registry
- per-item markdown reference notes
- per-item JSON contracts
- key item index
- key item review queue
- chapter mention links
- reference-sheet eligibility flags

#### Why This Phase Is Needed

Some artifacts are neither characters nor environments but still behave like canonical assets. They need their own layer so they can stay visually consistent and can later feed prompt-preparation and reference-sheet work.

#### Current Status

Planned.

### Phase 11 – Dialogue, Timing, and Edit-Aware Sequencing

#### Goal

Add temporal coherence so scenes and shots can support dialogue, audio binding, pacing, and later video assembly.

#### Inputs

- scene contracts
- shot packages
- continuity state
- chapter summaries
- dialogue extraction or inferred dialogue events
- any existing audio placeholders

#### Outputs

- dialogue event maps
- scene dialogue maps
- shot-to-dialogue mappings
- chapter edit timelines
- audio binding placeholders

#### Why This Matters

Without this phase, the system can produce good-looking static structure but not coherent audiovisual sequences.

#### Current Status

Validated.

#### Evidence

- `synthesize-dialogue-timeline` runs end to end
- writes project/chapter dialogue timelines
- writes shot-level dialogue notes and review queues
- preserves unresolved dialogue instead of carrying forward false speakers

### Phase 11.7 – Descriptor Enrichment and Reference Coverage

#### Goal

Turn canonical entities into structured, evidence-grounded descriptor profiles so later prompt preparation can reuse stable visual and scene detail without repeatedly asking the LLM to rediscover it.

#### Inputs

- chapter extraction outputs
- book index and paragraph windows
- character bibles
- environment bibles
- scene contracts
- shot packages
- key-item registry entries when available
- continuity notes and review queues
- librarian retrieval helpers

#### Outputs

- structured character descriptor profiles
- structured environment descriptor profiles
- structured scene descriptor profiles
- structured key-item descriptor profiles
- reference coverage maps
- field-level confidence and provenance records
- review queues for thin or uncertain fields

#### Why This Phase Is Needed

The project already knows the canon and can prepare prompt bundles. This phase adds a reusable descriptor layer so those prompt bundles can be driven by structured fields instead of repeatedly rediscovering the same facts from prose summaries.

#### Current Status

Planned.

### Phase 12 – Character Sheet Generation and Approval (lighter planning for now)

- multi-angle character sheets
- expression and pose variants
- approval/lock workflow for downstream use
- consumes prompt-preparation bundles from Phase 11.5

### Phase 13 – Environment Reference Generation and Approval

- establishing views
- key sub-locations
- lighting and mood variants
- approval/lock workflow
- consumes prompt-preparation bundles from Phase 11.5

### Phase 14 – Scene and Shot Keyframe Generation

- keyframes driven by approved refs plus scene/shot contracts
- reviewable visual candidate batches
- prompt bundles should come from the prompt-preparation layer rather than ad hoc rewriting

### Phase 15 – Audio Generation or Recording Integration

- recorded or synthetic dialogue
- ambience and music placeholders
- asset registry linkage

### Phase 16 – Video Generation and Assembly

- shot video generation
- scene assembly
- preview exports

### Phase 17 – Review, Lock, and Regenerate Workflow

- approve assets
- lock approved artifacts
- selectively regenerate downstream dependents
- preserve reviewed work across reruns

## Natural Review Breakpoints

These are intended user review boundaries and should remain explicit in both implementation and UX.

1. After ingest and chapter analysis
2. After character and environment bible synthesis
3. After scene production contracts and storyboard generation
4. After shot planning
5. After dialogue and timing timeline generation
6. After prompt-preparation and reference-pack generation
7. After character and environment reference approvals
8. After keyframe approvals
9. After audio approval
10. After video assembly preview

## Cross-Cutting Requirements

### Artifact lifecycle

Every artifact should support a lifecycle model such as:

- missing
- generated
- reviewed
- approved
- stale
- superseded
- locked

### Dependency-aware rebuilds

Every artifact should track upstream dependencies so reruns can choose between:

- review existing
- reuse current
- rebuild stale
- force regenerate

### Non-destructive reruns

The pipeline must not blindly overwrite valid outputs.

Default behavior should prefer:

- synthesize missing only
- rebuild stale only
- retry failed only
- review existing only

### Evidence preservation

Synthesis stages must preserve:

- source evidence references
- unresolved ambiguities
- revision history
- manual overrides

### Human approval and locking

Approvals must be explicit. User-reviewed artifacts must survive reruns unless the user explicitly requests a forced regeneration path.

## Suggested Supporting Features

These are not phase blockers, but they are strongly recommended additions to improve user-facing robustness.

### Style bible

A project-level style guide defining:

- visual tone
- palette
- realism/stylization level
- camera defaults
- composition defaults
- rendering consistency rules

### Generation profiles

Named profiles such as:

- storyboard
- cinematic
- speed
- consistency-first
- final-quality

### Staleness dashboard

A report showing:

- current artifacts
- stale artifacts
- locked artifacts
- downstream impact

### Dependency graph explorer

Useful for selective rebuilds, review impact tracing, and debugging downstream regeneration.

### Review queues

Queue artifacts for:

- unresolved characters
- unresolved environments
- weak scene contracts
- weak shot plans
- timing conflicts
- asset approval needs

## Implementation Guidance

### New code should prefer new modules

The next stages should add focused modules for:

- character bible synthesis
- environment bible synthesis
- scene contracts
- shot planning
- dialogue timeline
- lifecycle / dependency / staleness management

Do not continue expanding `story_authoring.py` or `world_registry.py` as catch-all implementation files.

### Existing code should be adapted through interfaces

When older beat/clip planning logic is still useful, wrap it through compatibility adapters rather than folding new architecture back into old assumptions.

## Recommended Build Order From Here

1. Add cross-cutting artifact lifecycle, dependency, and review specs.
2. Phase 7 character bible synthesis is implemented and runnable.
3. Phase 8 environment bible synthesis is implemented and runnable.
4. Phase 9 scene production contracts and chapter storyboard outputs are implemented and runnable.
5. Implement Phase 10 shot planning and shot packages.
6. Implement Phase 11 dialogue, timing, and edit-aware sequencing.
7. Implement Phase 11.5 prompt preparation and reference pack assembly.
8. Implement Phase 11.6 key item index and reference pack assembly.
9. Implement Phase 11.7 descriptor enrichment and reference coverage.
10. Then move into production asset generation phases 12-17.

## Database Timing

SQLite should remain deferred until:

- phase 7-11.7 contracts stabilize,
- lifecycle and dependency semantics stabilize,
- the file-first artifacts are mature enough to sync rather than speculate.

The first SQLite release should remain:

- per-project
- file-synced
- read-mostly
- optimized for querying and reporting rather than replacing canonical file artifacts.

