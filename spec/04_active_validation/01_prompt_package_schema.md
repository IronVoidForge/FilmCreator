Status: 100%

# 1.4 Prompt Package Schema

## Goal

Define one Markdown contract that both manual authoring and later LLM authoring can produce.

## Current Implementation Note

The active parser and writer now enforce this schema in `orchestrator/prompt_package.py`.

- `Repair Notes` is part of the required heading set.
- The parser raises a clear error when a required heading is missing.
- `Repair Notes` may be present but empty.
- Tracked templates and sample prompt packages have been backfilled to the current schema.

## Required Headings

- `Title`
- `ID`
- `Purpose`
- `Workflow Type`
- `Positive Prompt`
- `Negative Prompt`
- `Inputs`
- `Continuity Notes`
- `Repair Notes`
- `Sources`

## Rules

- Prompt packages are Markdown first and machine-parseable second.
- The runner reads the sections it needs and ignores the rest.
- The authoring layer must write the same headings every time.
- Sources should point back to the analysis files used to build the prompt.
- `Inputs` and `Continuity Notes` should declare source-frame expectations for continuation stages, even when the runner resolves the exact path from clip state.
- `Inputs` should be able to carry planning-time shot-start decisions such as continuity mode, composition type, dependency policy, and fallback strategy.
- `Inputs` should also be able to declare optional corrective automation such as identity-consistency and anatomy-repair assists.
- `Inputs` should also be able to declare owner metadata such as owner type, owner id, primary subject type, primary subject id, and variant role.
- `Continuity Notes` should be able to explain whether the clip is an independent reframe, a reblock, an insert, a cutaway, or a rare direct continuity follow.
- `Continuity Notes` should also be able to explain whether motion is expected to preserve the approved keyframe look or perform an explicit lighting or grade transition.
- `Repair Notes` should be able to explain whether the package is preserving composition while tightening character identity, repairing anatomy, or escalating to a more targeted fallback.
- `Sources` should preserve shared-asset lineage links when a prompt is derived from a character, environment, key item, scene, or shot.
- Shot-oriented prompt packages should also preserve adjacent-shot lineage in `Inputs` or `Sources` so the workflow can traverse previous/current/next shot context without hard-coding image paths into the prompt body.
- The same schema must support both shot openers and 3-5 second continuation intervals without introducing a second prompt format.

## Acceptance

- A human can open the file and edit it comfortably.
- The parser can detect missing sections with a clear error.
- Old prompt packages missing `Repair Notes` no longer silently pass as current schema.
- The same contract works for characters, environments, shot openers, reframed coverage, inserts, cutaways, anchors, interval continuations, and later video.
- The same contract can also describe optional identity-consistency and anatomy-repair assists without introducing a second prompt format.
- The same contract can also carry owner/subject lineage without introducing a second prompt format.
