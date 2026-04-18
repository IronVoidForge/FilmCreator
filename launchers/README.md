# Launchers

These batch files are convenience entry points for the current local workflow split:

- `start_authoring_terminal.bat`
  - opens a FilmCreator shell for the planning or authoring phase
  - intended for the LM Studio side, without ComfyUI loaded at the same time
  - echoes the current `lmstudio-check` and `write-prompts` commands
- `test_lmstudio_connectivity.bat`
  - runs the local LM Studio connectivity smoke test
  - verifies the resolved API base URL and chosen model before authoring
- `test_pilot_scene_prompt_writer_lmstudio.bat`
  - runs `lmstudio-check`, then rewrites the canonical pilot prompt packages for `SC001/CL001`
  - intended to validate the authoring-side prompt writer without loading ComfyUI
- `test_princess_of_mars_authoring_checkpoint.bat`
  - runs the first pre-SQL authoring checkpoint for `princess_of_mars_test`
  - writes chapter analysis, character/environment breakdowns, scene decomposition, beat bundles, clip plans, shared prompts, and clip-local prompts
  - also creates manual character-description placeholder files when the local LLM flags that a character is underdescribed in the chapter source
- `start_comfyui_8188.bat`
  - starts the known-good ComfyUI Python entrypoint on `127.0.0.1:8188`
  - skips launching a duplicate server if `8188` is already responding
- `start_render_terminals.bat`
  - ensures ComfyUI is reachable on `8188`
  - opens a second terminal in `C:\FilmCreator` with the current pilot `run-batch` command echoed for reference
- `run_pilot_scene_keyframe_batch.bat`
  - runs the current pilot keyframe batch directly
  - requires ComfyUI to already be reachable on `8188`
- `test_review_and_approve_pilot_keyframe.bat`
  - opens the current pilot keyframe folder
  - resolves the latest keyframe manifest from clip state
  - prompts for the top 2 finalists and the primary winner through the interactive Python review helper
  - promotes the chosen winner to `approved_keyframe`
  - prints the clip-state and manifest fields that prove the handoff worked
- `start_comfyui_clean_8190.bat`
  - starts a separate clean ComfyUI instance on `127.0.0.1:8190`
  - disables all custom nodes to avoid the current `ComfyUI-Manager` progress/logging failure during sampler execution
  - uses dedicated input, output, and user folders under `C:\FilmCreator\.comfy_clean`
- `start_render_terminals_clean_8190.bat`
  - starts or reuses the clean `8190` server
  - opens a FilmCreator render shell with `FILMCREATOR_COMFY_BASE_URL`, `FILMCREATOR_COMFY_INPUT_DIR`, and `FILMCREATOR_COMFY_OUTPUT_DIR` set for the clean server
- `run_pilot_scene_keyframe_batch_clean_8190.bat`
  - runs the current pilot keyframe batch against the clean `8190` server
  - intended as the recommended smoke-test path while the desktop/custom-node Comfy instance is still failing inside `comfyui_manager`
- `start_comfyui_video_8191.bat`
  - starts a safer video-focused ComfyUI instance on `127.0.0.1:8191`
  - disables all custom nodes, then whitelists only the custom node folders required by the current Wan video workflows
  - uses dedicated input, output, and user folders under `C:\FilmCreator\.comfy_video`
- `start_render_terminals_video_8191.bat`
  - starts or reuses the video `8191` server
  - opens a FilmCreator render shell with the video runtime environment variables already set
- `run_pilot_scene_cut_motion_batch_video_8191.bat`
  - plans and executes the current pilot short-cut `cut_motion` batch against the video `8191` server
  - resolves the current approved continuity source from clip state automatically
  - routes short video candidates into the clip-local `video/` folder
- `test_review_and_approve_pilot_cut_motion.bat`
  - opens the current pilot video candidate folder
  - resolves the latest `cut_motion` manifest from clip state
  - prompts for the top 2 finalists and the primary winner through the interactive Python review helper
  - promotes the chosen winner to `approved_video`
  - extracts the approved video's last frame into clip-local still storage when backend support is available
  - prints the clip-state and manifest fields that prove the handoff worked
- `run_pilot_scene_still_fix_batch_clean_8190.bat`
  - plans and executes the current pilot `still_fix` batch against the clean `8190` server
  - automatically uses the approved keyframe as the base image and `smoke_char.png` as the secondary reference
  - routes corrective still candidates into the clip-local `stills/fixes/` folder
- `test_review_and_approve_pilot_still_fix.bat`
  - opens the current pilot still-fix folder
  - resolves the latest `still_fix` manifest from clip state
  - prompts for the top 2 finalists and the primary winner through the interactive Python review helper
  - promotes the chosen winner to `approved_still_fix`
  - prints the clip-state and manifest fields that prove the handoff worked

Current pilot batch assets:

- batch manifest: `projects/pilot_scene/05_scenes/SC001/clips/CL001/logs/RUN_0001.json`
- environment ref: `projects/pilot_scene/05_scenes/SC001/clips/CL001/inputs/smoke_env.png`
- character ref: `projects/pilot_scene/05_scenes/SC001/clips/CL001/inputs/smoke_char.png`

Recommended usage right now:

1. For authoring-side smoke tests, run `test_lmstudio_connectivity.bat`
2. Run `test_princess_of_mars_authoring_checkpoint.bat` for the new chapter-to-analysis-to-prompt checkpoint
3. Then run `test_pilot_scene_prompt_writer_lmstudio.bat` if you want the smaller pilot clip-only prompt smoke test
4. Preferred for current render smoke tests: run `start_render_terminals_clean_8190.bat`
5. In the FilmCreator shell, either paste the echoed command or run `run_pilot_scene_keyframe_batch_clean_8190.bat`
6. Review generated outputs under the `pilot_scene` project folders
7. Run `test_review_and_approve_pilot_keyframe.bat` to validate review recording and approved-keyframe promotion
8. Run `run_pilot_scene_cut_motion_batch_video_8191.bat` for the short-cut motion smoke test after a keyframe has been approved
9. Run `test_review_and_approve_pilot_cut_motion.bat` to validate the video review-and-approval handoff and last-frame extraction
10. Run `run_pilot_scene_still_fix_batch_clean_8190.bat` for the first corrective still smoke test
11. Run `test_review_and_approve_pilot_still_fix.bat` to validate the still-fix review-and-promotion handoff
