# FilmCreator Specs

This folder breaks the project into numbered implementation chunks by feature and handoff boundary.

## Status Rule

- Progress across specs is tracked in `SPEC_PROGRESS.md`.
- A spec file only gets a filename suffix of `__complete.md` after its acceptance criteria have been validated.
- Implemented or partially validated specs keep their normal filenames until they are fully complete.
- Refactor progress is tracked in `00_refactor_PROGRESS.md`.

## Phase Order

1. `1_foundation`
2. `2_shared_assets`
3. `3_clip_pipeline`
4. `4_orchestration`
5. `5_authoring`
6. `6_deferred`

## Spec Index

- `1.1` repo, project, scene, and clip hierarchy
- `1.2` IDs, filenames, and naming rules
- `1.3` workflow catalog and registry contract
- `1.4` prompt package schema
- `1.5` project, scene, and clip state contracts
- `1.6` SQLite relational model
- `2.1` character reference generation
- `2.2` environment reference generation
- `2.3` shared reference promotion and reuse
- `3.1` clip input contract
- `3.2` scene build and golden frame
- `3.3` anchor and interval frames
- `3.4` clip review and selection
- `4.1` runner CLI and job dispatch
- `4.2` ComfyUI client and workflow patching
- `4.3` output routing, logging, and manifests
- `4.4` automated testing and CI strategy
- `4.5` resilient chapter batch orchestration and run recovery
- `5.1` story analysis outputs
- `5.2` clip plan generation
- `5.3` prompt writer integration
- `6.1` deferred video motion stage
- `6.2` acceptance test matrix

## Progress Docs

- `00_refactor_PROGRESS.md` - live refactor status and completed split tracking

## Working Rule

The orchestration layer is the product core. The authoring layer is a producer of structured files that the runner already knows how to consume.

Local generation is the default architecture. Authoring may use a local LLM runtime, and rendering targets a configured local ComfyUI runtime.

Authoring and rendering are separate phases so heavy local services can be run one at a time on VRAM-constrained machines.

## Terminology Rule

User-facing documentation should prefer **shot** language. Internal implementation may continue to use `clip_id`, clip folders, and existing runner semantics until a later refactor.

Recommended user-facing hierarchy:

- chapter
- scene
- shot
- prompt target

Practical compatibility note:

- `shot` = the user-facing term
- `clip` = the current internal render/planning unit and file naming term

## Current Phase Focus

Phase A is now structurally in place:

- chapter-scoped scene ids
- chapter -> scene -> clip/shot cascade entrypoints
- resilient chapter analysis, chapter-batch run tracking, and scene planning
- packetized prompt writing and shared prompt generation

Phase B is now focused on:

- canonical character identity
- canonical environment identity
- chapter continuity state
- chapter storyboard artifacts
- prompt-preparation bridge assets
- key item catalog and reference assets
- post-ingest world refinement for safe duplicate/name/type cleanup
