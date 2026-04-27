Status: 30%

# 3.3 Anchor and Interval Frames

## Goal

Reserve optional continuity-recovery tools without making them the default path for normal short movie cuts.

Also define the related next-shot opener path where an approved previous video last frame is used as an image-to-image source to create a new camera angle or zoom for the first frame of the next shot.

## Flow

- Resolve the latest approved continuity source from `clip_state.json`. At the start this is the approved golden frame. Later it can be the most recently approved anchor, interval, or approved video last frame.
- Use that continuity source for anchor or interval generation only when the clip plan explicitly calls for continuity repair, conservative bridging, or a later multi-segment handoff.
- Route anchor candidates into `stills/anchor_frames/`.
- Promote the selected anchor into `SC###_CL###_AF01.png`.
- Optionally generate interval frames into `stills/interval_frames/` for planned 3-5 second beats.
- Update `clip_state.json` after each approved promotion so the next generation step inherits the newest approved frame.

## Previous Last Frame Reframe

This is distinct from direct continuation.

Flow:

- Resolve `previous_clip.approved_video_last_frame` from clip state.
- Use that frame as the image-to-image source for the next clip opener.
- Prompt for a deliberate camera change such as:
  - reverse angle
  - wider establishing view
  - tighter close-up
  - over-the-shoulder angle
  - lower or higher camera position
  - lens or zoom change
- Preserve identity, wardrobe, environment state, prop positions, lighting continuity, and action state unless the shot package explicitly changes them.
- Write candidates into `stills/alternate_angle_openers/`.
- Promote the selected candidate into the next clip's approved opening keyframe slot.
- Block I2V generation for the dependent next clip until this opener is approved.

This path can create a sequential dependency:

```text
clip N opener -> clip N I2V -> approve clip N last frame -> generate clip N+1 alternate-angle opener -> approve opener -> clip N+1 I2V
```

For some scenes, this means FilmCreator can only safely generate the first shot of a sequence at first. Later shots wait for approved secondary views derived from previous approved output.

## Acceptance

- Continuation prompts do not restage the whole scene from scratch unless the clip plan explicitly calls for a new shot opener.
- Every continuation step can determine its source frame from state alone.
- Camera, identity, and environment continuity remain clip-local and state-driven.
- Normal short cuts can proceed from approved keyframe to cut motion without requiring anchor or interval generation first.
- A dependent next-shot opener can be generated from the previous approved video last frame without forcing the system into direct continuous-follow video.
- The runner can tell the difference between anchor/interval continuity repair and a fresh alternate-angle opener for the next shot.

