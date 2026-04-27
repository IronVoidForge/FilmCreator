Status: 55%

# 3.1 Clip Input Contract

## Goal

Define what a clip needs before the runner can generate stills for it.

## Interpretation

- Each clip is one shot-level render unit inside a story scene.
- The clip plan is responsible for breaking that shot into textual 3-5 second motion segments.
- The clip plan is also responsible for deciding how the opening keyframe should be created.
- Continuation stages consume the latest approved continuity frame from clip state only when the clip plan or fallback strategy actually requires it.
- Some shot sequences are dependency chains. A later shot may not be ready to generate until the previous shot has an approved video output and an approved last-frame-derived alternate-angle opener.

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
- A previous approved video last frame as an image-to-image source for a new camera angle, crop, zoom, or lens family
- An approved secondary-view opener generated from that previous last frame
- Approved character-sheet reference images for visible characters
- Optional identity-consistency or anatomy-repair settings
- Clip-local character or environment refs when the spec intentionally overrides shared scope

## Opening Keyframe Strategy

Each clip plan should declare one opening strategy:

- `fresh_from_refs` - create the opener from approved references, shot package, and scene staging.
- `soft_scene_reframe` - use a prior still or scene reference as loose composition guidance.
- `previous_last_frame_reframe` - use the previous approved video last frame in image-to-image to create a different angle, zoom, crop, or camera position for this clip's first frame.
- `direct_continuous_follow` - use the previous approved frame as direct continuity because the clip is not really a cut.
- `manual_keyframe_override` - use a manually selected opener.

If `opening_keyframe_strategy=previous_last_frame_reframe`, the clip runner must not queue the I2V job until:

- the previous clip has an approved video output
- the previous clip has a registered approved last frame
- at least one alternate-angle opener candidate has been generated from that last frame
- one opener candidate has been approved as this clip's first frame

## Continuity Rule

- Most clips should not assume the latest approved video last frame is the default next-shot source.
- Most clips should create a fresh opening keyframe from planning, shared refs, and staging intent.
- Continuation stages use the latest approved frame in the clip continuity chain only when the clip plan or fallback strategy says that source is required.
- Before any later approvals exist, the default approved still source is the approved golden frame or approved keyframe.
- If an approved video segment hands back into still generation later, its last approved frame can become the next continuity source, but only for clips that actually depend on it.
- Optional still correction may also consume approved character-sheet refs when the goal is to tighten identity consistency without replacing the shot design.
- The previous last frame reframe path should change camera angle, lens, zoom, or composition while preserving identity, wardrobe, environment state, object positions, and action continuity.
- This may require generating only the first shot of a scene or shot sequence first, approving its output, then generating dependent secondary-view openers one at a time.

## Acceptance

- A clip run can be prepared without inventing ad hoc filenames.
- The runner can validate missing inputs before submitting to ComfyUI.
- A continuation run can determine its source frame from state without manual folder browsing.
- Independent and soft-reference clips can prepare their opening keyframes without waiting for previous cut videos to finish.
- A corrective still pass can declare when it needs character-sheet refs in addition to the current approved still.
- Dependent clips can declare and enforce that their opener is blocked until the previous approved video last frame and secondary-view opener are available.

