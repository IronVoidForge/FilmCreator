Status: 70%

# 3.2 Scene Build and Golden Frame

## Goal

Create the opening still for a clip-shot, then promote one selected image to the golden frame.

This is the first concrete Phase 14 still-generation path. It covers independent openers first, then expands to image-to-image alternate-angle openers when the clip plan requires continuity from the previous approved video last frame.

## Current Position

This stage is not active yet. The operator layer, prompt-package schema, smart resume path, reference approval flow, and artifact lifecycle core are now far enough along that scene-build can be designed against real upstream contracts instead of a hypothetical pipeline.

The next implementation should start only after:

- a nonzero Phase 1-11 slice is validated end to end
- Phase 12 and 13 have produced at least one approved and locked reference asset in a real run
- prompt-preparation outputs are confirmed usable for the target scene or shot slice

Before perfecting this stage, run one complete pipeline pass far enough to see real downstream artifacts. Character/environment/keyframe quality can be imperfect during that first end-to-end validation; the purpose is to expose missing dependencies and weak gates before deep prompt refinement.

## Flow

- Run the clip shot-opener scene-build prompt against the correct scene-build workflow.
- Route candidates into `stills/scene_build/`.
- Review candidates manually.
- Promote the selected image to `stills/golden_frame/` as `SC###_CL###_GF01.png`.
- Update `clip_state.json` with the approved golden frame path and mark it as the current continuity source.

For dependent next-shot openers:

- wait for the previous clip's approved video last frame
- use that frame as an image-to-image source
- generate several alternate camera/zoom candidates
- route candidates into `stills/alternate_angle_openers/`
- approve one as this clip's golden/opening frame
- only then allow the I2V clip job to run

## Required Inputs

- approved character reference assets from Phase 12 when characters are present
- approved environment reference assets from Phase 13 when scene context depends on them
- shot package and prompt package outputs for the target scene and clip
- source lineage metadata showing which subject, scene, shot, and prompt variant drove the generation
- workflow registry entry for the scene-build workflow
- `opening_keyframe_strategy` from the clip plan
- previous approved video last frame when `opening_keyframe_strategy=previous_last_frame_reframe`

## Suggested Artifact Layout

- `projects/<project>/04_stills/<scene>/<clip>/scene_build/`
- `projects/<project>/04_stills/<scene>/<clip>/golden_frame/`
- `projects/<project>/04_stills/<scene>/<clip>/clip_state.json`

If `04_stills` proves too narrow later, that can still be revised, but scene-build and golden-frame artifacts should live outside the reference-asset tree and outside prompt-package folders.

## Suggested Operator Surface

The future CLI shape should be explicit and conservative:

- `python -m orchestrator run-scene-build <project> --scene ... --clip ...`
- `python -m orchestrator run-opener-reframe <project> --scene ... --clip ... --source previous-last-frame`
- `python -m orchestrator register-scene-build-candidate <project> ...`
- `python -m orchestrator approve-golden-frame <project> ...`
- `python -m orchestrator lock-golden-frame <project> ...`
- `python -m orchestrator request-frame-regeneration <project> ... --reason ... --notes ...`
- `python -m orchestrator clip-status <project> --scene ... --clip ...`

Golden-frame promotion should remain a distinct approval step, not an implicit side effect of generation.

## Lifecycle and Review Rules

- scene-build candidates may be regenerated freely until one is approved
- approved golden frames should carry artifact lifecycle metadata
- locked golden frames must survive ordinary reruns
- continuation stages should read the approved golden frame from clip state rather than guessing from directory contents
- rerun logic should be able to mark a golden frame stale without deleting it automatically

## Non-Goals for the First Implementation

- no interval continuation generation yet
- no anchor-frame chain yet
- no image-to-video generation yet
- no attempt to infer continuity state purely from filenames
- no hidden auto-promotion of best candidate
- no automatic final approval by image-review LLM

## Validation Plan

The first implementation should be validated without requiring a full book rerun:

1. use existing approved Phase 12/13 assets from a small validated slice
2. run one scene-build generation for one scene and clip
3. register multiple candidates
4. approve one candidate as the golden frame
5. lock it
6. verify `clip_state.json` points to the approved artifact
7. verify a later ordinary rerun does not overwrite the locked golden frame

## Dependencies on Current Work

- relies on the current prompt-package schema, including `Repair Notes`
- benefits from smart resume validation so partial prompt-prep outputs do not get treated as complete
- should reuse the artifact lifecycle core already introduced for reference assets and prompt packages
- should mirror the reference-approval flow instead of inventing a second approval model

## Acceptance

- Golden-frame promotion is a distinct step, not an implied side effect.
- Downstream continuation generation reads the approved golden frame from clip state until a newer approved frame replaces it.
- The operator can inspect, approve, and lock a golden frame without editing workflow JSON by hand.
- The first scene-build implementation can be tested on a tiny validated slice without restarting the whole upstream pipeline.
- Dependent next-shot openers remain blocked until required previous-video last-frame inputs exist.
