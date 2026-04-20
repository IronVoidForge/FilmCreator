# Spec Progress

## Current Refactor Status

The orchestration refactor is now mostly complete:

- completed: `story_authoring.py`, `world_global.py`, `runner.py`, `batch_runner.py`, `scaffold.py`, `state.py`, `review_tools.py`, `book_ingest.py`, `common.py`
- in progress: `authoring.py`, `book_authoring.py`, `cli.py`, `workflow_patcher.py`, final cleanup
- the live refactor tracker lives in [`00_refactor_PROGRESS.md`](./00_refactor_PROGRESS.md)

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
  - evidence: runtime scene work, authoring outputs, and render-stage clip folders are all using the canonical project hierarchy under `projects/<project_slug>/...`, including scoped story scenes and clip-local render units
  - next validation: keep the same hierarchy guarantees while adding chapter-wide continuity artifacts and storyboard outputs

- `1.2` IDs, filenames, and naming rules
  - status: `validated`
  - evidence: chapter authoring now emits chapter-scoped scene ids such as `CH008_SC001`, while render-stage clip assets still use canonical filenames such as `SC001_CL001_KF01_v001.png`
  - next validation: validate the same naming rules across chapter-wide scene cascades and future canonical character/environment registries

- `1.3` workflow catalog and registry contract
  - status: `complete`
  - evidence: `RUN_0001` prepare-only run resolved `character_reference` to `still.t2i.klein.distilled` entirely through the registry after canonical API workflow swaps

- `1.4` prompt package schema
  - status: `validated`
  - evidence: packetized authoring and prompt-package writing are both live; prompt-package parsing and scaffold templates support the expanded prompt contract including optional `Repair Notes`
  - next validation: consume the same expanded schema in a live still-fix or cut-motion run end to end

- `1.5` project, scene, and clip state contracts
  - status: `validated`
  - evidence: `clip_state.json` now records approved assets, review history, current continuity source, and canonical prompt-package paths; authoring outputs also populate scene-scoped planning and prompt-package paths consistently
  - next validation: extend state contracts with chapter-wide continuity summaries and canonical identity registries

- `1.6` SQLite relational model
  - status: `planned`
  - evidence: the relational design, setup plan, table map, sync direction, and implementation timing have now been specified for a per-project SQLite database
  - next validation: implement the first read-side database phase with `db-init`, `db-upgrade`, and `db-sync-from-files`

- `2.1` character reference generation
  - status: `validated`
  - evidence: shared character prompt writing now completes inside the live Chapter VIII authoring checkpoint for `princess_of_mars_test`, producing character reference prompt packages from chapter analysis outputs
  - next validation: resolve provisional identities like `carter` and `captive` into canonical character assets through the Phase B.1 registry layer

- `2.2` environment reference generation
  - status: `validated`
  - evidence: shared environment prompt writing now completes inside the live Chapter VIII authoring checkpoint and writes reusable environment prompt packages under `03_prompt_packages/environments/`
  - next validation: normalize environment families into canonical reusable environment assets through the Phase B.1 registry layer

- `2.3` shared ref promotion and reuse
  - status: `implemented`
  - evidence: promotion logic exists in the scaffold layer for character and environment refs
  - next validation: promote a live output into project references and confirm review copies plus state updates

- `3.1` clip input contract
  - status: `validated`
  - evidence: the validated keyframe batch consumed clip-scoped prompt packages and routed clip-local outputs without ad hoc filenames; chapter authoring also now emits explicit 5-second clip/shot rosters for planned scenes
  - next validation: validate the same contract across a full chapter-wide authoring cascade

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
  - evidence: `plan-batch` and `run-batch` produced successful live pilot batches, and the authoring layer now includes scene-level and chapter-level cascade functions (`author_scene`, `author_chapter`) on top of the existing checkpoint path
  - next validation: expose the chapter-wide authoring cascade through a stable first-class CLI command and validate it through a launcher-level smoke test

- `4.2` ComfyUI client and workflow patching
  - status: `validated`
  - evidence: the four-ref still workflow and the short-cut Wan 5B motion workflow have both been patched and submitted successfully through their registry-driven paths
  - next validation: validate the two-ref still-fix workflow on the same patch-and-submit path

- `4.3` output routing, logging, and manifests
  - status: `validated`
  - evidence: live keyframe and short-cut motion runs record successful outputs, and authoring now writes one raw LM Studio exchange log per task under the story-analysis logs folder
  - next validation: validate chapter-wide storyboard and continuity manifest outputs in Phase B

- `4.4` automated testing and CI strategy
  - status: `implemented`
  - evidence: unit coverage now includes prompt parsing, review-candidate discovery, review-and-promotion helpers, state normalization, scaffold promotion, workflow patching, LM Studio client discovery, and authoring packet parsing/file generation
  - next validation: expand from unit coverage into launcher-level or smoke-test coverage

- `4.5` resilient chapter batch orchestration and run recovery
  - status: `validated`
  - evidence: `analyze_book` now continues after per-chapter failures by default, writes `BOOK_RUN_latest.json`, `BOOK_RUN_<timestamp>.json`, `failed_chapters.json`, and `FAILED_CHAPTERS_REPORT.md`, and exposes `retry-failed-chapters` for rerunning only the latest failed chapters
  - next validation: run a real manifest with one injected chapter failure, confirm later chapters still complete, then retry the failed chapters from the saved run artifacts

- `5.1` story analysis outputs
  - status: `validated`
  - evidence: the authoring path now has a packetized Markdown contract, per-task LM Studio logging, malformed-character tolerance, manual-description placeholder reconciliation, and live chapter analysis plus four-scene decomposition for `princess_of_mars_test` Chapter VIII
  - next validation: add canonical character/environment resolution and chapter continuity summaries after analysis

- `5.2` clip plan generation
  - status: `validated`
  - evidence: scoped scene planning now writes canonical scene, beat, and clip files such as `CH008_SC001`, and the live Chapter VIII Scene 1 roster produced four explicit 5-second clips/shots with continuity metadata and interval beats
  - next validation: validate stable scene planning across all scenes in a chapter-wide cascade

- `5.3` prompt writer integration
  - status: `validated`
  - evidence: `lmstudio-check` resolves the live local model set, `write-prompts` rewrites canonical prompt packages, and the live Chapter VIII authoring checkpoint completes shared prompt generation plus clip-local prompt generation for Scene 1 end to end
  - next validation: run prompt writing across every scene in a chapter cascade and validate future canonical asset selection during Phase B.1

- `6.1` deferred video motion stage
  - status: `validated`
  - evidence: `RUN_0040` completed a live short-cut Wan 5B motion batch from the approved keyframe, the repaired motion review-and-promotion path selected a primary candidate successfully, and `approved_video` plus `approved_video_last_frame` are now populated after approval
  - next validation: tune look preservation so the short-cut motion path stops introducing the reported blue-shift unless a prompt explicitly asks for it

- `6.2` acceptance test matrix
  - status: `implemented`
  - evidence: it is acting as the checklist for deterministic and live validation
  - next validation: keep advancing it as checkpoints pass
