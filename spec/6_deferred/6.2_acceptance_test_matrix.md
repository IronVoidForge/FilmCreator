# 6.2 Acceptance Test Matrix

## Automation Rule

- Every deterministic check in this matrix should become an automated test.
- Manual review remains required only for creative quality, composition, and subjective approval.
- Live ComfyUI execution should be treated as a separate smoke-test layer, not the default CI requirement.

## Foundation

- Validate that project, scene, and clip folders resolve correctly from IDs.
- Validate that workflow registry entries resolve to the expected canonical workflow filenames.
- Validate that prompt packages fail clearly when required headings are missing.
- Validate that prompt packages can describe both shot openers and continuation intervals without schema changes.
- Validate that workflow patch points still exist in the canonical workflow JSON files.

## Shared Assets

- Validate that character and environment reference jobs route to project-level locations.
- Validate that approved shared refs are promoted once and recorded in `project_state.json`.
- Validate that shared-asset promotions also create the expected review copy in `06_reviews/selected/`.

## Clip Pipeline

- Validate that a scene-build run for `SC001/CL001` writes to `05_scenes/SC001/clips/CL001/stills/scene_build/`.
- Validate that golden-frame promotion creates `SC001_CL001_GF01.png` and updates `clip_state.json`.
- Validate that a continuation run resolves its source frame from `clip_state.json`, defaulting to the golden frame until a newer approved frame exists.
- Validate that anchor promotion creates `SC001_CL001_AF01.png` and preserves continuity inputs.
- Validate that interval-frame promotion creates `SC001_CL001_IF01.png` and updates `clip_state.json`.
- Validate that anchor and interval tools remain optional continuity helpers rather than a required path for a normal short cut.

## Orchestration

- Validate that run manifests capture project, scene, clip, workflow, prompt file, refs, outputs, seed, and timestamp.
- Validate that output routing never writes clip artifacts into the shared reference folders by mistake.
- Validate that CLI commands are idempotent and do not overwrite existing state files unintentionally.
- Validate that invalid scene or clip IDs fail with a clear error.
- Validate that local authoring smoke tests and local ComfyUI smoke tests can be enabled independently on VRAM-constrained machines.

## Authoring

- Validate that LM Studio connectivity settings resolve from local config without requiring ComfyUI to be running at the same time.
- Validate that scene analysis can be decomposed into shot-level clips.
- Validate that scene analysis writes project summary, scene breakdown, character breakdown, environment breakdown, clip roster, and clip plan files into canonical locations.
- Validate that scene analysis can also write beat bundles or staging packets that multiple clips can share.
- Validate that clip plans capture 3-5 second motion-segment breakdowns.
- Validate that a normal cut plan defaults to one short motion segment, while longer cuts can declare multiple segments.
- Validate that clip plans record start mode, continuity mode, composition type, starting-keyframe strategy, dependency policy, fallback strategy, required refs, expected prompt files, and expected outputs.
- Validate that clip plans can record whether motion should preserve the approved keyframe look or perform an explicit lighting transition.
- Validate that clip plans can also record visible character assets, consistency-assist policy, consistency-assist method, and anatomy-repair policy.
- Validate that prompt packages generated from authoring can be consumed by the runner without format changes.
- Validate that clip-plan-derived prompt files land in the expected `03_prompt_packages/<feature>/<scene>/<clip>/` location.
- Validate that generated keyframe, still-fix, and cut-motion prompt bodies avoid proper nouns while analysis files may still use asset IDs and names.
- Validate that generated still-fix prompts can declare which character refs should be used for identity-consistency correction.
- Validate that `duration_seconds` is stored in prompt metadata and not emitted into the cut-motion prompt body.
- Validate that generated cut-motion prompts preserve keyframe look by default and only describe lighting changes when the clip plan explicitly requests them.
- Validate that authoring does not silently route ordinary 5-second cuts into LongLook-style extended workflows.
- Validate that authoring does not silently treat previous approved video last frame as the universal default for starting the next shot.
- Validate that authoring can classify clips as `independent`, `soft_ref_previous`, or `hard_ref_previous`.
- Validate that authoring can mark review-triggered fallback to `previous_video_last_frame_to_reframe` without changing the primary planned mode for the clip.
- Validate that multi-character clips do not force unsafe whole-frame identity correction when region-aware targeting is unavailable.

## Live Smoke

- Validate that a local LM Studio authoring integration can connect when smoke tests are enabled.
- Validate that a live authoring pass can write prompt packages for one clip with ComfyUI closed.
- Validate that a live ComfyUI run can submit at least one text-to-image workflow when smoke tests are enabled.
- Validate that a live ComfyUI run can submit at least one clip-scoped workflow with fixture refs when smoke tests are enabled.
- Validate that a live continuation run can reuse the last approved frame from the clip continuity chain when smoke tests are enabled.
- Validate that a live normal-cut motion run can submit one short image-to-video workflow from an approved keyframe.
- Validate by manual smoke review that a live normal-cut motion run does not introduce an unexplained global blue or cool shift relative to the approved keyframe.
- Validate that LongLook is only used when an extended-cut workflow is explicitly selected.
- Validate that independent and soft-reference next-shot keyframes can be planned without waiting for previous shot video completion.
- Validate that an optional still-image consistency-assist workflow can consume a generated keyframe plus approved character refs and route outputs back into the clip-local still-fix path.
- Validate that any future hand-fix LoRA toggle for motion remains disabled by default and only appears in smoke tests when explicitly requested.
