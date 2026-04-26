# 1.2 ID Naming and File Conventions

## Goal

Standardize the naming system across project state, prompts, outputs, and reviews.

## Decisions

- Scene IDs use `SC###`.
- Clip IDs use `CL###`.
- Character refs and environment refs use stable asset IDs or slugs.
- Clip-local outputs include both scene and clip IDs in the filename.

## File Naming Rules

- Scene build candidates: `SC001_CL001_SB01_v001.png`
- Golden frame: `SC001_CL001_GF01.png`
- Anchor frame: `SC001_CL001_AF01.png`
- Interval frame: `SC001_CL001_IF01.png`
- Scene prompt file: `SC001_CL001_scene_build_prompt.md`
- Anchor prompt file: `SC001_CL001_anchor_01_prompt.md`
- Video prompt file: `SC001_CL001_video_motion_prompt.md`

## Acceptance

- A filename is enough to identify the owning scene, clip, and stage.
- Humans can scan a folder and understand what is approved versus exploratory.
- The runner can compute the next output name without custom logic per stage.
