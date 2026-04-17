# 6.1 Video Motion Stage

## Goal

Define the video-motion contract so normal movie-style cuts can use short image-to-video generation without blocking later extended-cut workflows.

## Rules

- Every clip already has a `video/` folder.
- The primary motion prompt family lives under `03_prompt_packages/cut_motion/<scene_id>/<clip_id>/`.
- A normal cut should default to one short image-to-video generation from one approved keyframe, typically around 5 seconds.
- A normal short cut should not depend on end-frame-stitched follow-on generation.
- A normal short cut should preserve the approved keyframe's lighting direction, color temperature, and overall color grade by default.
- Longer clips may be represented as multiple planned short motion segments, such as two segments for an approximately 10-second cut.
- LongLook is reserved for explicitly extended cuts and is not the default `cut_motion` workflow family.
- Video prompts should describe visible motion, camera behavior, and continuity only.
- If an approved video segment exists, its last approved frame may be promoted back into the clip continuity chain for later segment handoff, later cut continuity work, or a review-triggered camera-reposition fallback.
- Most next-shot keyframes should not wait on previous video completion if they can be planned as reframes, reblocks, inserts, or cutaways.
- Previous-video-last-frame dependencies should be rare and should usually appear only in:
  - `continuous_follow`
  - explicit multi-segment extended clips
  - review-triggered fallback regeneration
- Character identity consistency in video should primarily come from the approved starting still and the motion workflow's conditioning, not from a global post-hoc repair step.
- Global look shifts such as a blue or cool cast should be treated as workflow or prompting defects unless the clip plan explicitly calls for a look transition.
- If optional hand-fix or anatomy LoRAs are added to motion workflows later, they should be:
  - opt-in
  - workflow-specific
  - validated locally before becoming available in unattended scene batches
- Still-image correction should remain the preferred place to repair character identity and obvious anatomy before motion generation begins.
- Video must not become a dependency for completing the still-image pipeline.

## Acceptance

- The primary short-cut video implementation can plug into the existing project, scene, and clip hierarchy without a storage migration.
- A normal cut can render from one approved keyframe to one short video candidate without chained follow-on generation.
- A normal cut preserves the approved keyframe's overall lighting and grade unless the clip plan explicitly requests a lighting transition.
- Longer clips can be represented as multiple planned motion segments without inventing a separate storage model.
- LongLook can later plug in as an extended-cut workflow family without replacing the short-cut default.
- Video handoff can reuse the same clip continuity rules instead of inventing a separate source-frame system.
- Scene coverage can fan out keyframe generation across multiple planned clips before earlier short videos have completed.
- Experimental motion-time hand repair can be layered in later without changing the default short-cut contract.
