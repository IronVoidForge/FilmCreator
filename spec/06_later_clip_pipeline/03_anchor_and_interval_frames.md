# 3.3 Anchor and Interval Frames

## Goal

Reserve optional continuity-recovery tools without making them the default path for normal short movie cuts.

## Flow

- Resolve the latest approved continuity source from `clip_state.json`. At the start this is the approved golden frame. Later it can be the most recently approved anchor, interval, or approved video last frame.
- Use that continuity source for anchor or interval generation only when the clip plan explicitly calls for continuity repair, conservative bridging, or a later multi-segment handoff.
- Route anchor candidates into `stills/anchor_frames/`.
- Promote the selected anchor into `SC###_CL###_AF01.png`.
- Optionally generate interval frames into `stills/interval_frames/` for planned 3-5 second beats.
- Update `clip_state.json` after each approved promotion so the next generation step inherits the newest approved frame.

## Acceptance

- Continuation prompts do not restage the whole scene from scratch unless the clip plan explicitly calls for a new shot opener.
- Every continuation step can determine its source frame from state alone.
- Camera, identity, and environment continuity remain clip-local and state-driven.
- Normal short cuts can proceed from approved keyframe to cut motion without requiring anchor or interval generation first.
