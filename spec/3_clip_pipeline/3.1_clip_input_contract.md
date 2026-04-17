# 3.1 Clip Input Contract

## Goal

Define what a clip needs before the runner can generate stills for it.

## Interpretation

- Each clip is one shot-level render unit inside a story scene.
- The clip plan is responsible for breaking that shot into textual 3-5 second motion segments.
- The clip plan is also responsible for deciding how the opening keyframe should be created.
- Continuation stages consume the latest approved continuity frame from clip state only when the clip plan or fallback strategy actually requires it.

## Required Inputs

- `clip_state.json`
- A clip plan in `02_story_analysis/clip_plans/<scene_id>/<clip_id>.md` with a 3-5 second motion-segment breakdown
- A scene build prompt package
- Shared approved refs resolved through project or scene state

## Optional Inputs

- Additional continuity refs
- A beat bundle or staging packet shared with other clips in the same dramatic beat
- A previous approved keyframe as a soft reframing source
- A previous approved video last frame as a camera-repositioning source
- Approved character-sheet reference images for visible characters
- Optional identity-consistency or anatomy-repair settings
- Clip-local character or environment refs when the spec intentionally overrides shared scope

## Continuity Rule

- Most clips should not assume the latest approved video last frame is the default next-shot source.
- Most clips should create a fresh opening keyframe from planning, shared refs, and staging intent.
- Continuation stages use the latest approved frame in the clip continuity chain only when the clip plan or fallback strategy says that source is required.
- Before any later approvals exist, the default approved still source is the approved golden frame or approved keyframe.
- If an approved video segment hands back into still generation later, its last approved frame can become the next continuity source, but only for clips that actually depend on it.
- Optional still correction may also consume approved character-sheet refs when the goal is to tighten identity consistency without replacing the shot design.

## Acceptance

- A clip run can be prepared without inventing ad hoc filenames.
- The runner can validate missing inputs before submitting to ComfyUI.
- A continuation run can determine its source frame from state without manual folder browsing.
- Independent and soft-reference clips can prepare their opening keyframes without waiting for previous cut videos to finish.
- A corrective still pass can declare when it needs character-sheet refs in addition to the current approved still.
