# FilmCreator Implementation Roadmap

## Goal

Ship a local-first, cut-oriented pipeline that can:

1. plan a full scene into clips and prompt packages,
2. render review batches for each clip without hand-editing workflow JSONs,
3. record review decisions and approvals in state,
4. generate motion from approved keyframes,
5. run large scene batches overnight in stage-separated passes,
6. evolve cleanly into a persistent multi-chapter world model without discarding the file-first workflow.

## Working Principles

- Local generation is the product core.
- LM Studio and ComfyUI are separate phases on VRAM-constrained hardware.
- `clip = cut` in the working implementation.
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

## Current Project Status

- `analyze-chapter` and `plan-scene` are working and now have live task timing output.
- Shared character/environment prompt writing is running one asset per LM Studio call.
- Clip prompt writing has been migrated to tagged Markdown packet output with local parsing.
- Scene planning is now tolerant of several non-canonical clip-id formats and duplicate post-normalization collisions.
- The project is still intentionally file-first; SQLite remains deferred until the world model is stable enough to avoid churn.

## Current Risks And Known Gaps

- We still need repeated full checkpoint validation to prove the current chapter pipeline can complete end-to-end without throwing.
- The next quality-focused change is the character split:
  - roster / identity pass
  - per-character detail pass
- Shared prompt generation and clip prompt writing may still need prompt tuning to reduce retries and malformed packet edge cases.
- We do not yet have a reviewer/rework loop for weak but syntactically valid outputs.
- The SQLite relational layer is still a future migration, not a current implementation target.
- The multi-chapter world model is planned, but should not begin until the current single-chapter pipeline is consistently boring and reliable.

## Agreed Sequencing From Here

This is the authoritative order we want to follow.

### Stage A – Stabilize The Single-Chapter Checkpoint

#### Goal

Get the current `princess_of_mars_test` checkpoint to run end-to-end reliably with no hard failures from packet drift, clip-id formatting, or malformed clip prompt output.

#### Work In Scope

- finish hardening chapter analysis, scene planning, shared prompt writing, and clip prompt writing
- keep all LLM output in tagged Markdown packet form
- keep all rigid structure generation in local parsers
- improve logging, retry visibility, and failure artifacts until debugging is straightforward

#### Verification

We do **not** move on until all of the following are true:

- 2-3 consecutive full checkpoint runs complete without an uncaught exception
- any malformed clip or prompt target is either:
  - recovered,
  - skipped with a warning,
  - or recorded as a bounded failure artifact
- CLI output shows start / finish / retry / timing for essentially every LM Studio call
- final summary clearly reports warnings, failures, and failed clips

#### Useful Future Hooks To Preserve Now

- packet parsing helpers should remain reusable by future authoring commands
- clip/state warnings should remain machine-readable for later QA/rework logic
- failure artifacts should preserve enough context to support later replay / rework tools

### Stage B – Character Split (Quality Upgrade)

#### Goal

Improve character quality by separating discovery/identity work from detailed character authoring.

#### New Flow

1. character roster / identity pass
2. per-character detail pass
3. clarification/manual-description generation per character when needed

#### Why This Happens Before Multi-Chapter

- character identity is the first domain that must be stable before persistence exists
- the multi-chapter system will depend on clean canonical character entities
- this reduces the risk of building a persistent world model on top of noisy first-pass character records

#### Verification

- no duplicate canonical characters from one chapter unless explicitly unresolved
- aliases are captured consistently
- weakly identified characters become clarification requests instead of muddy canonical entries
- per-character markdown quality improves relative to the one-shot extraction version

#### Suggested Future Functions / Modules

- `build_character_roster_packet(...)`
- `parse_character_roster_packet(...)`
- `author_character_detail_packet(...)`
- `parse_character_detail_packet(...)`
- `review_character_roster(...)`

### Stage C – Output Review / Rework Layer

#### Goal

Add quality control after syntax stability is proven.

#### Planned Capabilities

- reviewer pass for character roster quality
- reviewer pass for scene/clip planning quality
- targeted rework for weak outputs
- automated retry reasons plus optional reviewer explanation

#### Verification

- weak outputs are flagged before they pollute downstream prompt writing
- rework targets only the broken items, not entire chapters/scenes
- reviewer outputs remain tagged Markdown packets

#### Suggested Future Functions / Modules

- `review_packet_quality(...)`
- `parse_review_packet(...)`
- `apply_rework_request(...)`
- `should_accept_packet(...)`

### Stage D – File-First Multi-Chapter World Model (Wave 1)

#### Goal

Support ingestion of a full book, chapter splitting, chapter manifests, and chapter-by-chapter world updates while remaining file-first.

#### Work In Scope

- full-book ingestion
- table-of-contents skipping
- chapter boundary detection
- chapter file generation
- book manifest creation
- project-level chapter processing loop

#### Why This Starts Here

- by this point the single-chapter flow should be stable
- character extraction should already be split and improved
- we can reuse packet parsing and review patterns instead of inventing them during the migration

#### Verification

- a full-book source can be split into chapter files with a parse report
- front matter and table of contents are not misinterpreted as chapter bodies
- chapter order is stable and auditable
- re-running the chapter splitter is deterministic or clearly reports ambiguities

#### Suggested Future Functions / Modules

- `parse_full_book_to_chapter_candidates(...)`
- `write_book_manifest(...)`
- `write_book_parse_report(...)`
- `reconcile_chapter_boundaries_with_llm(...)`
- `parse_book_boundary_packet(...)`

### Stage E – Persistent Character / Environment World Model (Wave 2)

#### Goal

Introduce persistent world state while still keeping Markdown files as the human-editable source of truth.

#### Work In Scope

- canonical character registry
- canonical environment registry
- alias resolution across chapters
- layered description model
- deferred clarification that can resolve later
- chapter-to-world update flow

#### Verification

- later chapters can refine earlier unresolved character descriptions
- chapter-specific and forward-from state changes are represented distinctly
- canonical ids remain stable across updates
- contradictions are logged, not silently overwritten

#### Suggested Future Functions / Modules

- `load_world_state(...)`
- `update_world_from_chapter(...)`
- `merge_character_update(...)`
- `merge_environment_update(...)`
- `resolve_alias_candidates(...)`
- `write_world_index_markdown(...)`
- `write_world_index_json(...)`

### Stage F – Revision / Timeline / Snapshot Layer (Wave 3)

#### Goal

Support long-form continuity and future scene generation from time-correct state.

#### Work In Scope

- revision log
- contradiction detection
- character evolution timeline
- environment state changes over time
- chapter/scene state snapshots
- prompt generation from frozen chapter/scene state only

#### Verification

- later reveals do not silently corrupt earlier chapter prompts
- a scene generated from CH003 does not leak CH009 state
- revisions are auditable
- continuity questions are queryable from the file-first world model

#### Suggested Future Functions / Modules

- `detect_world_contradictions(...)`
- `write_revision_entry(...)`
- `build_chapter_state_snapshot(...)`
- `build_scene_state_snapshot(...)`
- `resolve_prompt_state_at_chapter(...)`

### Stage G – SQLite Migration

#### Goal

Add a queryable relational layer **after** the file-first world model is stable.

#### Rule

SQLite does not become the source of truth first. It becomes a synced, queryable acceleration layer after the file structures and semantics are proven.

#### Start SQLite Only When

- single-chapter checkpoint is stable
- character split is complete
- file-first multi-chapter ingest exists
- persistent world model exists
- layered descriptions and alias resolution have settled enough to stop thrashing the schema

#### Verification

- the SQLite schema can be derived cleanly from working file-first artifacts
- sync from files to SQLite is deterministic
- the most useful queries are known from actual workflow pain points, not guessed in advance

#### Suggested Future Functions / Modules

- `db_init(...)`
- `db_upgrade(...)`
- `db_sync_from_files(...)`
- `db_validate_against_files(...)`
- `query_character_timeline(...)`
- `query_scene_state(...)`
- `query_alias_history(...)`

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

These are the checks we should run before moving beyond the current single-chapter stabilization work.

### Verification Group 1 – End-to-End Stability

- full authoring checkpoint completes without uncaught exception
- output summary is produced
- warnings/failures are bounded and inspectable

### Verification Group 2 – Clip Planning Robustness

- non-canonical clip ids are normalized or skipped with warnings
- duplicate normalized ids do not corrupt outputs
- at least one usable clip remains when clip planning succeeds semantically

### Verification Group 3 – Prompt Writing Robustness

- clip prompt writing uses tagged Markdown packets only
- malformed packet responses create retries and failure artifacts, not raw JSON crashes
- minimum viable clip-stage policy behaves as expected

### Verification Group 4 – Logging / Debuggability

- every LM Studio call logs start and finish
- retries log a reason
- durations are visible
- relevant log files exist on disk

## End-To-End Delivery Plan

### Phase 0: Stabilize The Validated Keyframe Batch

#### Goal

Turn the first successful keyframe render into a clean, repeatable baseline.

#### Deliverables

- clean Comfy runtime launch path is documented and kept as the current smoke-test default
- stale error fields are not retained on successful batch candidates
- manifests clearly distinguish failed historical attempts from successful reruns
- launcher docs explain `8188` desktop path versus `8190` clean path

#### Test Point

- rerunning the same keyframe batch produces clean successful manifests with no contradictory error leftovers

### Phase 1: Review And Approved Keyframe Handoff

#### Goal

Make the first real human approval step complete and reproducible.

#### Deliverables

- use `review-batch` to record:
  - top 2 finalists
  - one chosen primary
- promote the chosen primary into the approved keyframe slot
- update `clip_state.json`:
  - `approved_assets.approved_keyframe`
  - `current_continuity_source`
  - `latest_review_decision`
  - `review_batches[]`
  - `stage_style_preferences.keyframe`

#### Handoff

- input: successful `keyframe` batch manifest
- output: one approved keyframe plus state that downstream stages can trust

#### Test Point

- one chosen keyframe is promoted and later commands can resolve it from clip state without manual path browsing

### Phase 2: Still-Fix Loop

#### Goal

Support corrective still batches after keyframe review.

#### Deliverables

- validate `still_fix` prompt packages and batch planning
- require a reviewed prior stage or explicit `fix_of`
- generate 3-4 `still_fix` variants
- review and approve a corrected still when needed
- preserve the relationship between the fix batch and the asset it is correcting
- define optional corrective intents for `still_fix`:
  - identity consistency against approved character-sheet refs
  - anatomy repair
  - compositional cleanup
- support a recommended safe default mode:
  - review-triggered finalist-only consistency assist
- leave open a later aggressive option:
  - post-batch automatic consistency assist on all keyframe candidates

#### Handoff

- input: approved keyframe or a reviewed prior still candidate
- output: either:
  - approved keyframe stands as-is, or
  - approved still-fix replaces it as the preferred still basis for motion

#### Test Point

- a `still_fix` batch can run from the approved keyframe and record what it was fixing
- a consistency-assist still-fix can run from a generated keyframe plus approved character refs and produce a corrected still without replacing the normal keyframe pipeline

### Phase 3: Short-Cut Motion Smoke Path

#### Goal

Prove one approved keyframe can drive one normal movie-cut video generation without chained follow-on segments.

#### Deliverables

- register a standard Wan single-image-to-video API workflow in the workflow registry as the primary `cut_motion` family for normal cuts
- keep the default short-cut target to one image-to-video generation per candidate for a normal clip, typically around 5 seconds
- do not chain end-frame-to-next-frame generation inside a normal short cut
- allow longer clips, such as around 10 seconds, to be represented as two planned motion segments rather than silently routing them into LongLook
- patch runtime controls for the video workflow:
  - prompt text
  - input image
  - save/output node selection
  - seed
  - any exposed motion-length or generation settings
- tune the short-cut motion workflow and prompt contract so it preserves the approved keyframe look by default instead of drifting toward a cool blue grade
- add `cut_motion` workflow resolution to the runner
- route outputs into the clip `video/` folder
- capture enough metadata to identify the video output and its originating approved keyframe
- explicitly reserve LongLook for extended cuts that are intentionally longer than the standard short-cut window

#### Handoff

- input: one approved keyframe and one `cut_motion` prompt package
- output: one video candidate set for that cut

#### Test Point

- a single clip can run short `cut_motion` from an approved keyframe and write one short video output per candidate into the clip-local video folder

### Phase 4: Video Review And Last-Frame Continuity Handoff

#### Goal

Close the loop between motion generation and continuity state.

#### Deliverables

- manual review outcome for cut-motion runs:
  - approve
  - needs_fix
  - regenerate_batch
- capture approved video metadata in clip state
- support launcher and CLI paths that derive review candidates from the run manifest rather than from a raw folder listing
- record the approved video last frame as a continuity source when appropriate
- if a clip plan explicitly declares multiple motion segments, define how later segments inherit from:
  - the approved keyframe
  - the approved prior segment last frame
  - an explicit future auto-carry mode if we add one
- define whether the next stage uses:
  - approved keyframe
  - approved still fix
  - approved video last frame

#### Handoff

- input: reviewed cut-motion outputs
- output: approved video asset and optional approved last-frame continuity source

#### Test Point

- clip state can hand a reviewed video last frame back into later generation without inventing a second continuity system

### Phase 5: LM Studio Authoring Integration

#### Goal

Automate planning and prompt writing without changing the runner contract.

#### Deliverables

- LM Studio client configuration and connectivity check
- authoring-side CLI commands are defined in the spec before implementation:
  - `lmstudio-check`
  - `analyze-scene`
  - `plan-scene`
  - `write-prompts`
  - later optional `author-scene` convenience wrapper
- analysis outputs written under `02_story_analysis/`:
  - project summary
  - scene breakdown
  - character breakdowns
  - environment breakdowns
  - clip roster
  - clip plans
- one command to plan a scene into clips
- one command to write prompt packages for:
  - character refs
  - environment refs
  - scene stage
  - keyframe
  - still fix
  - cut motion
- the planning layer must decide, per clip:
  - continuity mode
  - composition type
  - starting-keyframe strategy
  - dependency policy
  - auto-advance policy
  - review fallback strategy
- prompt rules enforced in generated output:
  - no proper nouns in prompt text
  - descriptive noun phrases only
  - duration stored in metadata, not body text
  - Wan motion prompts emphasize visible motion and camera behavior rather than restating the entire image
- planning and prompt writing should also be able to declare:
  - visible character assets
  - consistency-assist policy
  - consistency-assist method
  - anatomy-repair policy

#### Current Implementation Note

- `lmstudio-check` is now implemented.
- `write-prompts` is now implemented for clip-local prompt families:
  - `scene_stage`
  - `keyframe`
  - `still_fix`
  - `cut_motion`
- the chapter-based pilot is active.
- shared character/environment prompt writing is active.
- the current remaining priority is full validation and then character-split quality improvements before any multi-chapter migration.

#### Handoff

- input: story analysis and scene intent
- output: Markdown prompt packages and clip plans that the existing runner consumes unchanged

#### Test Point

- with LM Studio running and ComfyUI closed, one scene can generate all required planning and prompt files automatically

### Phase 5.1: Chapter-Based Authoring Pilot

#### Goal

Prove the authoring pipeline on a real public-domain chapter before any database migration.

#### Deliverables

- chapter intake and chapter summary
- character extraction and character index
- environment extraction and environment index
- scene decomposition and scene index
- scene beat bundles
- one scene clip roster
- one or two prompt-ready clip plans
- shared character and environment prompt packages
- clip-local prompt packages for the first scene

#### Test Point

- with LM Studio running and ComfyUI closed, Chapter VIII of `princess_of_mars_test` can be transformed into one scene with one or two prompt-ready clips and their canonical prompt packages

### Phase 5.5: SQLite Relational Layer

#### Goal

Add a queryable local relational layer after authoring, character stability, and world-model concepts have stabilized.

#### Deliverables

- create one project-local SQLite database file
- add schema models and migrations
- add commands:
  - `db-init`
  - `db-upgrade`
  - `db-sync-from-files`
  - `db-validate`
- sync these entities into SQLite:
  - chapters
  - scenes
  - beats
  - clips
  - motion segments
  - characters
  - environments
  - clip-character mappings
  - clip-environment mappings
  - ref bindings
  - prompt packages
  - runs
  - candidates
  - review batches
  - approvals
  - continuity links
- keep Markdown, JSON, and media files as canonical artifacts in the first release

#### Test Point

- one project database can be initialized and synced from the filesystem, and queries can answer which characters, environments, prompts, and approved assets belong to a clip

### Phase 6: Scene-Wide Planning

#### Goal

Prepare an entire scene in one authoring pass before any rendering begins.

#### Deliverables

- scene-level planning command that:
  - decomposes the scene into clips
  - groups clips by beat or shared staging packet when appropriate
  - assigns clip IDs
  - records shot purpose and duration
  - breaks each clip into textual 3-5 second motion segments
  - identifies required shared refs
  - identifies character and environment asset IDs referenced by the scene
  - writes all prompt packages for the scene
- clip plans should prefer `reframe_same_moment`, `reblock_same_scene`, `insert`, and `cutaway` for most coverage
- `continuous_follow` should be rare and intentionally chosen
- the default opening-keyframe plan for most clips should not wait on previous video completion
- a failed keyframe review may escalate into a previous-video-last-frame camera-reposition fallback
- normal clips should plan as one short motion segment by default, while longer clips may declare multiple sequential motion segments such as two segments for an approximately 10-second cut
- scene manifest that records all clips and their current stage readiness

#### Handoff

- input: one story scene
- output: all clip plans and prompt packages for the whole scene

#### Test Point

- a full scene can be planned in one pass with no manual prompt-file creation

### Phase 7: Overnight Scene Batch Rendering

#### Goal

Render a full scene in unattended overnight passes without skipping required human review gates.

#### Deliverables

- batch runner that can operate at scene scope
- queueing by stage family:
  - pass A: render all keyframe batches for all clips in the scene that are `independent` or `soft_ref_previous`
  - review gate
  - pass B: render all requested still-fix batches and any review-triggered fallback keyframe retries
  - review gate
  - pass C: render all cut-motion batches for approved clips
- explicit dependency handling:
  - clips that are `hard_ref_previous` wait on their required source result
  - clips that are `independent` or `soft_ref_previous` should not be blocked by unfinished earlier videos
- resume and retry behavior:
  - skip already completed batches
  - retry failed clips only
  - continue scene progress without restarting from scratch
- scene-level summary artifacts:
  - pending clips
  - completed clips
  - failed clips
  - blocked clips waiting on review

#### Handoff

- input: a fully planned scene and approved prior-stage decisions
- output: rendered batches across every clip that is eligible for that stage

#### Test Point

- one command can render all keyframe batches for a scene overnight and leave a morning review queue

### Phase 8: Cross-Cut Continuity And Batch Video Completion

#### Goal

Make scene-wide cut progression robust enough for longer unattended runs.

#### Deliverables

- explicit rules for when a new cut starts from:
  - shared refs plus text only
  - prior approved keyframe
  - previous approved video last frame
- explicit rules for when a new cut should instead be treated as:
  - `reframe_same_moment`
  - `reblock_same_scene`
  - `insert`
  - `cutaway`
  - `scene_reset`
- scene-level continuity preferences so adjacent cuts can reuse the right approved source when appropriate
- batch video creation across all cuts in a scene after keyframe approvals are in place
- handoff rules so the next cut knows whether it should inherit continuity or intentionally reset composition

#### Handoff

- input: reviewed outputs from prior cuts plus scene continuity rules
- output: a full scene worth of cut videos that can be generated in batches

#### Test Point

- after review gates are cleared, a scene can run cut-motion generation across all clips in order with no manual path swapping

## Operational Handoffs

### Handoff 1: Authoring To Rendering

- LM Studio on
- ComfyUI off
- output:
  - clip plans
  - prompt packages
  - scene batch plan

### Handoff 2: Rendering To Review

- LM Studio off
- ComfyUI on
- output:
  - candidate stills or videos
  - manifests
  - state-ready batch metadata

### Handoff 3: Review To Promotion

- human selects top 2 and primary
- system records the decision
- approved asset is promoted
- clip state becomes the continuity contract

### Handoff 4: Approved Still To Motion

- approved keyframe or approved still-fix becomes the motion input frame for the first short motion segment
- normal cuts render from one approved still into one short video generation
- if a longer clip is explicitly planned as multiple motion segments, the approved last frame from segment 1 may become the input frame for segment 2
- many next-shot keyframes should be able to generate before those motion results complete, because they are planned as reframes, reblocks, inserts, or cutaways rather than direct continuity follows

### Handoff 5: Approved Video To Later Continuity

- approved video last frame may become the next continuity source when scene logic or a review fallback calls for continuity carry-forward or camera repositioning from the prior cut

## Overnight Batch Strategy

Because review is intentionally required after each generated stage family, the practical overnight model is:

1. overnight authoring pass:
   - plan the whole scene
   - write all prompt packages
2. overnight keyframe render pass:
   - render all clip keyframe batches that do not hard-depend on earlier video results
3. morning review:
   - choose primary keyframes
   - flag clips that need still fixes
4. overnight still-fix render pass:
   - render only the flagged clips and any fallback retries that now require previous-video-last-frame reframing
5. morning review:
   - approve fixes
6. overnight cut-motion render pass:
   - render short-cut videos for all approved clips
   - only use LongLook for clips explicitly marked as extended cuts
7. morning review:
   - approve, retry, or refine only problem cuts

This preserves review quality while still letting you use sleep-time for the expensive rendering passes.

## Recommended Build Order From Here

1. Finish repeated validation of the single-chapter checkpoint until it is boring and reliable.
2. Implement the character split:
   - roster / identity pass
   - per-character detail pass
3. Add reviewer / rework support for weak but syntactically valid outputs.
4. Only then begin file-first multi-chapter ingest and world-state migration.
5. Add persistent character and environment world state.
6. Add revision, contradiction, and snapshot tooling.
7. Only after those stabilize, implement the SQLite read-side sync layer.
8. Continue motion-path and batch-render improvements on top of the stabilized authoring foundation.
