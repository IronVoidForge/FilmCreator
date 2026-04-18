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
  - evidence: `RUN_0001` parsed prompt packages successfully, and the prompt-package parser plus scaffold templates now support the expanded prompt contract including optional `Repair Notes`
  - next validation: consume the same expanded schema in a live still-fix or cut-motion run end to end

- `1.5` project, scene, and clip state contracts
  - status: `validated`
  - evidence: `clip_state.json` now records the approved keyframe, approved video, approved video last frame, latest review decision, review batch history, current continuity source, and canonical prompt-package paths after the live `RUN_0001`, `RUN_0040`, and LM Studio `write-prompts` validation passes
  - next validation: validate that scene-level authoring can refresh state-linked prompt packages for more than one clip without a render run

- `1.6` SQLite relational model
  - status: `planned`
  - evidence: the relational design, setup plan, table map, sync direction, and implementation timing have now been specified for a per-project SQLite database
  - next validation: implement the first read-side database phase with `db-init`, `db-upgrade`, and `db-sync-from-files`

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
  - next validation: validate the new still-fix smoke path, where the approved keyframe auto-fills the base image and the secondary ref is supplied explicitly

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
  - evidence: the live pilot review recorded top 2 plus primary on both `RUN_0001` and `RUN_0040`, and the review path is now hardened through manifest-backed interactive review helpers instead of brittle folder counting
  - next validation: perform the same review-and-handoff loop on a live `still_fix` batch and confirm the approved corrective still is promoted cleanly

- `4.1` runner CLI and job dispatch
  - status: `validated`
  - evidence: `plan-batch` and `run-batch` produced a successful live keyframe batch for `RUN_0001`, and `RUN_0040` produced a successful live short-cut motion batch through the video runtime
  - next validation: validate the same dispatch path on the new `still_fix` smoke workflow

- `4.2` ComfyUI client and workflow patching
  - status: `validated`
  - evidence: the four-ref still workflow and the short-cut Wan 5B motion workflow have both been patched and submitted successfully through their registry-driven paths
  - next validation: validate the two-ref still-fix workflow on the same patch-and-submit path

- `4.3` output routing, logging, and manifests
  - status: `validated`
  - evidence: `RUN_0001` records successful keyframe outputs, `RUN_0040` records four routed short-cut motion outputs under the clip-local `video/` folder, and approved-video promotion now extracts a canonical clip-local last frame
  - next validation: validate the live still-fix batch so routed corrective stills and review metadata cover all three current generated stage families

- `4.4` automated testing and CI strategy
  - status: `implemented`
  - evidence: unit coverage now includes prompt parsing, review-candidate discovery, review-and-promotion helpers, state normalization, scaffold promotion, workflow patching, LM Studio client discovery, and prompt-writer file generation
  - next validation: expand from unit coverage into launcher-level or smoke-test coverage

- `5.1` story analysis outputs
  - status: `validated`
  - evidence: the authoring path now has a packetized Markdown contract, per-task LM Studio logging, manual-description placeholder reconciliation, and live chapter analysis plus scene decomposition for `princess_of_mars_test`
  - current difficulty: shared prompt drafting still has occasional empty or malformed LM Studio responses for some assets, especially when a manual description is required
  - next validation: make shared character/environment prompt generation resilient enough to complete the authoring checkpoint without blocking on one bad asset

- `5.2` clip plan generation
  - status: `validated`
  - evidence: `plan-scene princess_of_mars_test --scene SC001` now writes canonical scene, beat, and clip files from the live chapter pilot
  - current difficulty: the model sometimes emits shorthand clip ids or partial packet wrappers, so parser-side normalization remains important
  - next validation: keep the clip-planning pass stable while shared prompt generation is hardened

- `5.3` prompt writer integration
  - status: `validated`
  - evidence: `lmstudio-check` resolved the live local model set and `write-prompts` rewrote the canonical pilot clip prompt-package files with fresh content while updating clip state with the resulting package paths
  - current difficulty: clip-local prompt writing is stable, but chapter-based shared prompt generation still needs a final robustness pass for per-asset empty responses and malformed `inputs_markdown`
  - next validation: expand the authoring checkpoint so shared character/environment prompt generation completes reliably for every asset in the chapter

- `6.1` deferred video motion stage
  - status: `validated`
  - evidence: `RUN_0040` completed a live short-cut Wan 5B motion batch from the approved keyframe, the repaired motion review-and-promotion path selected a primary candidate successfully, and `approved_video` plus `approved_video_last_frame` are now populated after approval
  - next validation: tune look preservation so the short-cut motion path stops introducing the reported blue-shift unless a prompt explicitly asks for it

- `6.2` acceptance test matrix
  - status: `implemented`
  - evidence: it is acting as the checklist for deterministic and live validation
  - next validation: keep advancing it as checkpoints pass
