# Phase B Continuity and Identity Implementation Plan

## Purpose

Phase B moves FilmCreator from a structurally-correct chapter authoring pipeline into a continuity-aware film authoring system.

Phase A established the chapter -> scene -> clip cascade, chapter-scoped scene ids, and scene-level planning and prompt writing. Phase B adds the missing continuity layer:

- canonical character identity
- canonical environment identity
- scene-to-scene continuity inheritance
- chapter-wide continuity summaries and storyboard outputs
- stable authoring contracts for future SQL / database-backed world state

User-facing terminology should prefer **shot** over **clip** in docs and operator language. Internal ids may remain `CL001` until a later refactor.

---

## Phase B goals

1. Resolve provisional scene-local identities into canonical film-wide assets.
2. Preserve continuity from one scene to the next inside a chapter.
3. Reduce duplicated environment and character breakdowns across scenes and chapters.
4. Produce chapter-level storyboard and continuity artifacts that can be reviewed before rendering.
5. Keep all new Phase B behavior compatible with the current Phase A file layout.

---

## What is already complete from Phase A

The following items should be treated as baseline assumptions for Phase B:

- chapter-scoped scene ids are working (`CH008_SC001`)
- scene planning and prompt writing work on scoped scene ids
- chapter analysis returns ordered scene ids
- scene authoring and chapter authoring cascade functions exist
- malformed character records are tolerated at the record level
- current planning outputs produce short, explicit shot/clip rosters with duration targets

Phase B should build on that baseline rather than revisiting Phase A structure.

---

## Phase B workstreams

### B1. Canonical character identity resolution

#### Problem
Current outputs still allow weak or provisional identities such as `carter` or `captive`. These are sufficient for one chapter smoke test but weak for cross-scene and cross-chapter continuity.

#### Goal
Every extracted character should be either:
- resolved to a canonical film-wide character asset id, or
- explicitly marked as provisional with a clarification status

#### Deliverables
- canonical character registry file
- alias index
- character resolution pass after extraction
- clarification status model
- prompt-writing preference for canonical ids over provisional ids

#### Proposed artifacts
- `projects/<project>/02_story_analysis/world/CHARACTER_REGISTRY.md`
- `projects/<project>/02_story_analysis/world/CHARACTER_ALIASES.json`
- `projects/<project>/02_story_analysis/world/character_resolution_log.md`

#### Resolution rules
- if a new scene-local character matches a known alias, merge into canonical asset
- if a scene-local character has stable visual identity but uncertain name, mark provisional and carry a clarification request
- if a character is generic by role only (`guard`, `captive`, `captain`), default to provisional unless explicitly linked
- prompt writing should reference canonical asset folders when canonical resolution exists

#### Minimum implementation steps
1. Add a canonical character registry loader/writer.
2. Add `resolve_character_assets(...)` pass after chapter analysis.
3. Update shared prompt writing to prefer canonical asset ids and sources.
4. Preserve provisional assets but tag them clearly in breakdowns and summary outputs.

---

### B2. Canonical environment identity resolution

#### Problem
Environment extraction is usable but fragmented. Similar locations may be emitted as separate environment assets in different scenes or chapters.

#### Goal
Normalize environment families into film-wide reusable environment assets while still preserving scene-local staging notes.

#### Deliverables
- canonical environment registry file
- environment alias/merge rules
- scene-local staging notes attached to canonical environments

#### Proposed artifacts
- `projects/<project>/02_story_analysis/world/ENVIRONMENT_REGISTRY.md`
- `projects/<project>/02_story_analysis/world/ENVIRONMENT_ALIASES.json`
- `projects/<project>/02_story_analysis/world/environment_resolution_log.md`

#### Resolution rules
- merge environment variants when the physical place is the same and only the camera sub-location differs
- preserve sub-location detail as scene-local notes, not new canonical asset ids
- retain separate canonical ids only when the environment logic is truly distinct

#### Minimum implementation steps
1. Add canonical environment registry loader/writer.
2. Add `resolve_environment_assets(...)` pass after chapter analysis.
3. Update environment shared prompt writing to prefer canonical environment ids.
4. Preserve scene-local sub-location notes in scene breakdowns and shot plans.

---

### B3. Scene-to-scene continuity inheritance

#### Problem
Each scene is currently planned mostly in isolation. Chapter-wide authoring exists, but later scenes do not yet formally inherit prior state.

#### Goal
Each scene planning pass should receive a concise continuity context based on prior scenes in the chapter.

#### Examples
- characters already introduced
- emotional state carried forward
- environmental destruction already established
- assets already approved or visually defined
- prior action consequences that should persist

#### Deliverables
- continuity summary artifact per chapter
- continuity context passed into scene planning and shot prompt writing
- explicit current-state summaries for characters, environments, and major props/vehicles

#### Proposed artifacts
- `projects/<project>/02_story_analysis/world/CH008_CONTINUITY_SUMMARY.md`
- `projects/<project>/02_story_analysis/world/CH008_STATE.json`

#### Minimum implementation steps
1. Build a lightweight `chapter_state` structure after chapter analysis.
2. After each scene authoring pass, update the state with continuity-relevant facts.
3. Pass a scene-local continuity summary into the next scene's planning prompt.
4. Expose this continuity summary in outputs for review.

---

### B4. Chapter storyboard artifact

#### Problem
The pipeline now produces usable scene and shot plans, but review still requires opening multiple files.

#### Goal
Generate a single chapter storyboard artifact that summarizes:
- scenes in order
- shots in order within each scene
- estimated durations
- emotional shifts
- continuity-sensitive assets

#### Deliverables
- markdown storyboard summary
- optional json machine-readable storyboard summary

#### Proposed artifacts
- `projects/<project>/02_story_analysis/storyboards/CH008_storyboard.md`
- `projects/<project>/02_story_analysis/storyboards/CH008_storyboard.json`

#### Suggested content
For each scene:
- scene purpose
- scene summary
- total estimated duration
- ordered shot list
- beat-to-shot mapping
- continuity-sensitive characters/environments

#### Minimum implementation steps
1. Add `build_chapter_storyboard(...)` from analysis + scene planning outputs.
2. Write markdown and json versions.
3. Include shot durations from clip roster files.

---

### B5. User-facing terminology transition: clip -> shot

#### Problem
Current code and file ids still use `clip`, but user-facing language should use `shot`.

#### Goal
Adopt `shot` in docs, launcher descriptions, summary outputs, and future specs without breaking current internal ids.

#### Deliverables
- updated docs/help text
- summary output fields that mention shots in explanatory text
- migration note explaining that internal `clip_id` remains canonical for now

#### Rules
- do not rename file paths or ids yet
- do update all user-facing docs/specs to say `shot`
- use phrasing such as `shot (internal clip id CL001)` where useful

---

## Recommended implementation order

### Phase B.1
- canonical character registry
- character resolution pass
- canonical environment registry
- environment resolution pass

### Phase B.2
- chapter continuity state artifact
- scene-to-scene continuity inheritance in scene planning

### Phase B.3
- chapter storyboard artifact
- chapter summary improvements for review

### Phase B.4
- broader terminology cleanup (`clip` -> `shot`) across docs and operator-facing text

This order minimizes risk and ensures continuity state is grounded in canonical identities before trying to summarize or storyboard the chapter globally.

---

## Detailed task checklist

### B1 character identity checklist
- [ ] define canonical character registry format
- [ ] define alias file format
- [ ] add loader/writer utilities
- [ ] add resolution pass after character extraction
- [ ] update summary outputs to include canonical/provisional status
- [ ] update shared prompt writing to use canonical sources where available
- [ ] create regression test for `carter` -> `john_carter` style merge
- [ ] create regression test for unresolved `captive` provisional flow

### B2 environment identity checklist
- [ ] define canonical environment registry format
- [ ] define alias file format
- [ ] add loader/writer utilities
- [ ] add environment resolution pass after extraction
- [ ] preserve scene-local sub-location notes
- [ ] update environment prompt writing to use canonical sources where available
- [ ] create regression test for environment merge behavior

### B3 continuity inheritance checklist
- [ ] define chapter state schema
- [ ] write initial chapter state after analysis
- [ ] update chapter state after each scene authoring pass
- [ ] pass continuity summary into scene planning prompt
- [ ] pass continuity summary into prompt writing prompt context
- [ ] create regression test for state carryover across two scenes

### B4 storyboard checklist
- [ ] define storyboard markdown format
- [ ] define storyboard json schema
- [ ] compute per-scene total duration from shot roster
- [ ] emit ordered shot summaries for all scenes
- [ ] include continuity flags in storyboard output
- [ ] create regression test for storyboard generation

### B5 terminology checklist
- [ ] update specs and docs to use `shot`
- [ ] update launcher README wording
- [ ] update CLI help strings where safe
- [ ] preserve internal `clip_id` semantics

---

## Proposed data model notes

### Character registry entry
- canonical_asset_id
- display_name
- aliases
- stable_visual_description_path
- first_chapter_seen
- clarification_status
- linked_breakdown_paths

### Environment registry entry
- canonical_asset_id
- display_name
- aliases
- canonical_environment_summary_path
- sub_locations
- first_chapter_seen
- linked_breakdown_paths

### Chapter state entry
- chapter_id
- scene_order
- known_characters
- known_environments
- approved_visual_assets
- active_continuity_notes
- unresolved_clarifications

---

## Output contract changes for Phase B

The following summary outputs should be extended:

### `StoryAnalysisSummary`
Add future optional fields:
- canonical_character_ids
- canonical_environment_ids
- provisional_character_ids
- provisional_environment_ids

### `SceneAuthoringSummary`
Add future optional fields:
- continuity_summary_path
- storyboard_scene_path
- estimated_scene_duration_seconds

### `ChapterAuthoringSummary`
Add future optional fields:
- storyboard_markdown_path
- storyboard_json_path
- chapter_state_path
- canonical_registry_paths

---

## Risks and mitigations

### Risk: over-merging identities
Mitigation:
- require explicit alias evidence or stable confirmation rules
- preserve provisional identities instead of forcing bad merges

### Risk: continuity prompts become too long
Mitigation:
- feed only concise chapter-state summaries into scene planning
- keep full detailed registry files on disk for review, not in every prompt

### Risk: environment normalization erases useful staging detail
Mitigation:
- keep canonical environment identity separate from scene-local sub-location notes

### Risk: storyboard generation becomes too verbose
Mitigation:
- use concise shot summaries built from existing clip roster and clip plan metadata

---

## Definition of done for Phase B

Phase B should be considered complete when:

1. Character and environment outputs are resolved to canonical registries or clearly marked provisional.
2. Scene planning uses inherited continuity context from earlier scenes in the same chapter.
3. Chapter authoring produces a storyboard artifact with ordered scenes and shots.
4. Shared prompt writing and shot prompt writing prefer canonical assets when available.
5. Operator-facing docs describe the system in chapter -> scene -> shot terms.

---

## Immediate next recommended coding tasks

1. Add canonical registry utilities for characters and environments.
2. Add post-analysis resolution passes.
3. Extend `author_chapter(...)` to maintain and update `chapter_state` between scenes.
4. Add a storyboard writer that summarizes all scene runs.
5. Update launcher/docs/help text to describe shots rather than clips in user-facing language.
