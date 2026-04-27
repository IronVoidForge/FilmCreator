Status: 70%

# Phase 14 - Frame Generation Strategy

## Goal

Define how FilmCreator creates still frames for later image-to-video work, including independent shot openers and dependent next-shot openers derived from the previous approved video last frame.

This phase produces approved stills. It does not produce video.

## Current Priority

After the current Oz run, the immediate priority is still:

1. finish a complete Phase 1-11 pipeline run
2. confirm all major artifact families exist and are nonzero
3. run Phase 12/13 reference generation enough to prove character/environment reference flow
4. then start refining prompts, start/end states, approval gates, and frame generation

Character references, environment references, and keyframes do not need to be perfect before the first full pipeline validation pass. The first goal is to prove the whole chain can run end to end. Refinement comes after we can see complete outputs and failure patterns.

## Phase Placement

Phase 14 starts after:

- Phase 10 shot packages exist
- Phase 11 dialogue timeline exists when dialogue timing matters
- Phase 11.7 descriptor enrichment exists
- Phase 11.5 prompt preparation exists
- Phase 11.8 quality grading has run or at least produced review warnings
- Phase 12 approved character references exist for visible characters when available
- Phase 13 approved environment references exist for scene environments when available
- workflow preflight has validated the still-generation workflow

Phase 14 outputs are consumed by:

- Phase 16 image-to-video clip generation
- later review/repair stages

## Required Inputs

For every frame-generation job:

- project slug
- scene id
- shot id / clip id
- shot package
- prepared shot prompt package
- descriptor records for active characters/environments when available
- approved character references when visible characters are present and approved
- approved environment reference when available
- style lock when available
- workflow manifest / workflow id
- generation strategy

Additional required input by strategy:

| Strategy | Additional Input |
|---|---|
| `fresh_from_refs` | approved refs or descriptor fallback |
| `soft_scene_reframe` | prior still or scene reference |
| `previous_last_frame_reframe` | previous approved video last frame |
| `direct_continuous_follow` | previous approved frame and explicit continuity reason |
| `manual_keyframe_override` | operator-selected local image |

The runner must validate that the strategy-specific inputs exist before queueing generation.

## Opening Keyframe Strategies

### `fresh_from_refs`

Use for the first shot of a scene or any shot that is visually independent enough to start from approved references, descriptors, and the shot package.

Common examples:

- first shot of a new scene
- new location
- time jump
- intentional discontinuity
- wide establishing shot
- cutaway that does not require exact previous body/prop state

### `soft_scene_reframe`

Use a previous still, environment reference, or scene image as loose guidance. This should preserve broad style/location but does not require exact object or pose continuity.

Common examples:

- same setting, different subject
- similar staging but not exact action continuation
- mood or lighting continuity more important than pose continuity

### `previous_last_frame_reframe`

Use the previous approved video last frame as image-to-image input, but request a deliberate camera/composition change for the next shot opener.

Common changes:

- reverse angle
- over-the-shoulder angle
- wider view
- tighter close-up
- zoom/crop change
- lower or higher camera position
- lens family change

Must preserve:

- character identity
- wardrobe
- environment state
- prop positions unless action explicitly moves them
- lighting continuity
- action start state

This strategy creates a dependency:

```text
shot N opener approved
shot N I2V generated
shot N video approved
shot N last frame registered
shot N+1 alternate-angle opener generated from last frame
shot N+1 opener approved
shot N+1 I2V can run
```

### `direct_continuous_follow`

Use only when the next clip is a true continuation and should not behave like a normal cut. This is not the default path for shot changes.

### `manual_keyframe_override`

Use when the operator supplies a still and marks it as the intended first frame.

## Parallel vs Sequential Generation

The scheduler can parallelize frame generation only when shots are independent.

Independent:

- `fresh_from_refs`
- `soft_scene_reframe` without a specific previous approved video dependency
- manual override already approved

Sequential:

- `previous_last_frame_reframe`
- `direct_continuous_follow`
- any clip whose prompt says exact state continuity is required

For some scenes, FilmCreator may only generate the first shot's opener at first. Later shot openers wait until the prior video output is approved and its last frame is available.

## Candidate Output Layout

Suggested folders:

```text
projects/<project>/04_stills/<scene>/<clip>/scene_build/
projects/<project>/04_stills/<scene>/<clip>/alternate_angle_openers/
projects/<project>/04_stills/<scene>/<clip>/selected/
projects/<project>/04_stills/<scene>/<clip>/clip_state.json
```

Candidate metadata should include:

```json
{
  "candidate_id": "CH001_SC001_SH002_OPENER_C003",
  "phase": "phase_14_frame_generation",
  "scene_id": "CH001_SC001",
  "shot_id": "SH002",
  "clip_id": "CH001_SC001_SH002",
  "strategy": "previous_last_frame_reframe",
  "source_frame_id": "CH001_SC001_SH001_LAST_APPROVED",
  "source_frame_path": "projects/.../last_frames/SH001_last.png",
  "camera_change_request": "reverse angle, medium close",
  "prompt_package_id": "CH001_SC001_SH002_PROMPT",
  "workflow_id": "scene_build_i2i",
  "seed": 12345,
  "prompt_variant": "raw",
  "status": "unreviewed"
}
```

## Approval Gate

Phase 14 does not auto-promote generated stills.

Required operator actions:

- review candidate set
- approve one candidate as the opener/golden frame
- optionally lock it
- optionally reject candidates with reason tags and notes
- optionally request regeneration with repair notes

The selected frame becomes the approved first frame for Phase 16.

## Acceptance Criteria

- The runner can decide whether a shot opener is independent or blocked by previous-video approval.
- A candidate set can contain several image-to-image options for operator review.
- A previous last frame can generate a new camera angle without being treated as direct continuous-follow video.
- Clip state records the approved opener and the dependency source.
- Phase 16 refuses to run I2V when a required opener is missing or unapproved.
