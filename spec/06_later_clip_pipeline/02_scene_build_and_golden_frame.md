Status: 45%

# 3.2 Scene Build and Golden Frame

## Goal

Create the opening still for a clip-shot, then promote one selected image to the golden frame.

## Flow

- Run the clip shot-opener scene-build prompt against the correct scene-build workflow.
- Route candidates into `stills/scene_build/`.
- Review candidates manually.
- Promote the selected image to `stills/golden_frame/` as `SC###_CL###_GF01.png`.
- Update `clip_state.json` with the approved golden frame path and mark it as the current continuity source.

## Acceptance

- Golden-frame promotion is a distinct step, not an implied side effect.
- Downstream continuation generation reads the approved golden frame from clip state until a newer approved frame replaces it.

