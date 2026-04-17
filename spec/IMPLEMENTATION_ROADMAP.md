# FilmCreator Implementation Roadmap

## Goal

Ship a local-first, cut-oriented pipeline that can:

1. plan a full scene into clips and prompt packages,
2. render review batches for each clip without hand-editing workflow JSONs,
3. record review decisions and approvals in state,
4. generate motion from approved keyframes,
5. run large scene batches overnight in stage-separated passes.

## Working Principles

- Local generation is the product core.
- LM Studio and ComfyUI are separate phases on VRAM-constrained hardware.
- `clip = cut` in the working implementation.
- Previous-shot video last frame is an optional continuity tool, not the universal default next-shot source.
- Every generated stage is batch-first and review-gated.
- The next stage only advances from one approved primary candidate.
- Overnight runs are stage-bounded. Human review remains the boundary between stage families unless we later add an explicit auto-advance mode.
- Optional post-keyframe identity-consistency and anatomy-repair assists should plug in as corrective still passes, not as hidden replacements for the base keyframe stage.

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
  - update `clip_state.json` so continuity resolves from the approved keyframe.

## Known Gaps At This Checkpoint

- `still_fix` has not yet been run from a reviewed prior stage.
- The repaired manifest-backed cut-motion review launcher has not yet been live-validated after the folder-counting bug fix.
- The current short-cut motion path appears to introduce an unwanted blue-shift relative to the approved keyframe and needs look-preservation tuning.
- Longer 10-second clips are not yet represented as explicit multi-segment motion plans.
- approved video last-frame extraction now exists in code, but it has not yet been live-validated on a reviewed motion approval.
- LM Studio authoring is still manual-file driven rather than automated.
- The planning-time shot-start decision model is not yet implemented:
  - continuity mode
  - composition type
  - dependency policy
  - review fallback strategy
- Optional identity-consistency assist after keyframe generation is not yet implemented:
  - character-ref mapping
  - safe multi-character targeting
  - low-denoise reference-guided still correction
- Experimental motion-time hand-fix LoRA support is not yet implemented or validated.
- Scene-wide overnight batching is not yet implemented as a first-class orchestration mode.
- The desktop/custom-node Comfy runtime on `8188` still fails inside the `comfyui_manager` logging path, so the clean render path remains the recommended smoke-test runtime.

## Next Immediate Step

Validate the next two workflow checkpoints:

1. run the repaired `test_review_and_approve_pilot_cut_motion.bat` launcher and confirm:
   - the manifest-backed candidate list opens correctly even when older videos exist in the folder
   - `approved_video` is recorded in clip state
   - `approved_video_last_frame` is extracted into the clip still hierarchy
2. run the new `run_pilot_scene_still_fix_batch_clean_8190.bat` smoke path and confirm:
   - a reviewed prior still is used as the automatic base image
   - the secondary reference image patches into the two-ref workflow
   - 3-4 corrective still candidates land under `stills/fixes/`

That pair of validations closes the motion review handoff and opens the first real corrective still stage.

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
  - review decision
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

#### Handoff

- input: story analysis and scene intent
- output: Markdown prompt packages and clip plans that the existing runner consumes unchanged

#### Test Point

- with LM Studio running and ComfyUI closed, one scene can generate all required planning and prompt files automatically

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

1. Validate repaired cut-motion review plus approved-video last-frame extraction.
2. Validate `still_fix` from an approved keyframe.
3. Tune the short-cut motion path to preserve keyframe look without the current blue-shift.
4. Add LM Studio planning and prompt writing.
5. Validate `still_fix` as a corrective stage, including optional identity-consistency assist.
6. Add scene-wide planning.
7. Add scene-wide stage-bounded overnight rendering.
8. Add explicit multi-segment clip rules for longer cuts.
9. Reserve LongLook for extended-cut workflows after the short-cut path is stable.
10. Add cross-cut continuity rules and scene-scale video completion.
