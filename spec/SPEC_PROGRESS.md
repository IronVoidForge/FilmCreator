# Spec Progress

## Status Legend

- `planned`
  - the spec is accepted as a target but has not been implemented yet
- `implemented`
  - code or structure exists, but the acceptance criteria have not been validated yet
- `validated`
  - at least one real validation checkpoint has passed, but the full acceptance criteria are not complete yet
- `complete`
  - the acceptance criteria have been validated end to end
  - when a spec reaches this state, its filename is renamed with the suffix `__complete.md`

## Current Status

- `1.1` repo, project, scene, and clip hierarchy
  - status: `validated`
  - evidence: the clean keyframe batch wrote four outputs into `projects/pilot_scene/05_scenes/SC001/clips/CL001/stills/keyframes/` with no clip artifact escaping into shared scope
  - next validation: promote approved stills and later video outputs while preserving the same hierarchy guarantees

- `1.2` IDs, filenames, and naming rules
  - status: `validated`
  - evidence: the validated keyframe batch produced canonical filenames such as `SC001_CL001_KF01_v001.png`
  - next validation: validate approved-keyframe promotion naming and later cut-motion naming

- `1.3` workflow catalog and registry contract
  - status: `complete`
  - evidence: `RUN_0001` prepare-only run resolved `character_reference` to `still.t2i.klein.distilled` entirely through the registry after canonical API workflow swaps

- `1.4` prompt package schema
  - status: `validated`
  - evidence: `RUN_0001` parsed `projects/pilot_scene/03_prompt_packages/characters/ulurani3/ulurani3_ref_prompt.md` successfully and patched the workflow from it
  - next validation: consume the same schema in a clip-scoped continuation run

- `1.5` project, scene, and clip state contracts
  - status: `validated`
  - evidence: `clip_state.json` now records the approved keyframe, latest review decision, review batch history, and current continuity source after the live `RUN_0001` approval handoff
  - next validation: let a short-cut cut-motion run resolve its source frame from the approved state without manual ref paths, then record an approved video in clip state after review

- `2.1` character reference generation
  - status: `validated`
  - evidence: `RUN_0001` prepare-only validation succeeded, and `RUN_0003` reached live ComfyUI submission with a recorded runtime failure manifest
  - next validation: successful live ComfyUI execution plus promotion of an approved character ref

- `2.2` environment reference generation
  - status: `implemented`
  - evidence: the same project-scoped runner path supports `environment_reference`
  - next validation: perform an environment prepare-only run and then a live render

- `2.3` shared ref promotion and reuse
  - status: `implemented`
  - evidence: promotion logic exists in the scaffold layer for character and environment refs
  - next validation: promote a live output into project references and confirm review copies plus state updates

- `3.1` clip input contract
  - status: `validated`
  - evidence: the validated keyframe batch consumed clip-scoped prompt packages and routed clip-local outputs without ad hoc filenames
  - next validation: validate a continuation or cut-motion run that resolves its source frame from approved state

- `3.2` scene build and golden frame
  - status: `validated`
  - evidence: a live clip-scoped keyframe batch rendered successfully, review recorded a top 2 and chosen primary, and the chosen still was promoted into the approved keyframe slot
  - next validation: use the approved keyframe as the source for a live short-cut cut-motion smoke run

- `3.3` anchor and interval frames
  - status: `implemented`
  - evidence: continuation workflow registry, continuity-source resolver, and current continuity tracking exist
  - next validation: live continuation run that reuses the approved prior frame

- `3.4` clip review and selection
  - status: `validated`
  - evidence: the live pilot review recorded top 2 plus primary on `RUN_0001`, updated batch candidate review statuses, copied the winner into `06_reviews/selected`, and promoted it to `approved_keyframe`
  - next validation: perform the same review-and-handoff loop on a live cut-motion batch and confirm `approved_video` is recorded

- `4.1` runner CLI and job dispatch
  - status: `validated`
  - evidence: `plan-batch` and `run-batch` produced a successful live keyframe batch for `RUN_0001` through the clean Comfy runtime
  - next validation: extend the same dispatch path to reviewed `still_fix` and later `cut_motion`

- `4.2` ComfyUI client and workflow patching
  - status: `validated`
  - evidence: the four-ref API workflow was patched and submitted successfully through the clean Comfy runtime, and live image outputs were captured into clip-local folders
  - next validation: register and validate the primary short-cut Wan cut-motion workflow with the same registry-driven patching path

- `4.3` output routing, logging, and manifests
  - status: `validated`
  - evidence: `RUN_0001` now records successful clip-local keyframe outputs and batch metadata, and candidate files landed in canonical clip folders
  - next validation: validate short-cut video output routing and confirm successful reruns clear stale candidate error fields

- `4.4` automated testing and CI strategy
  - status: `implemented`
  - evidence: initial unit tests exist for prompt parsing, continuity resolution, and workflow patching
  - next validation: run the tests and expand to integration coverage

- `5.1` story analysis outputs
  - status: `planned`

- `5.2` clip plan generation
  - status: `planned`

- `5.3` prompt writer integration
  - status: `planned`

- `6.1` deferred video motion stage
  - status: `implemented`
  - evidence: the primary `video.cut_motion.wan.i2v` registry entry now points to a short-cut Wan 5B image-to-video workflow, LongLook is preserved under an explicit extended-cut workflow ID, and clip-state support now includes approved video promotion after review
  - next validation: live-validate one short-cut cut-motion batch from an approved keyframe, then review and promote one chosen video candidate

- `6.2` acceptance test matrix
  - status: `implemented`
  - evidence: it is acting as the checklist for deterministic and live validation
  - next validation: keep advancing it as checkpoints pass
