# Launchers

The launcher tree is now grouped by workflow so the root stays readable:

- `authoring/`
  - LM Studio connectivity checks and authoring-side smoke tests
  - `authoring/princess_of_mars/`
    - chapter-analysis and prompt-generation launchers for `princess_of_mars_test`
- `render/8188/`
  - the default ComfyUI runtime and its keyframe review flow
- `render/clean_8190/`
  - the clean ComfyUI runtime and its still-fix workflow
- `render/video_8191/`
  - the video-focused ComfyUI runtime and its cut-motion workflow
- `multi_chapter/`
  - ingest, book-level, and Phase B1 multi-chapter helpers
  - book-to-prompt end-to-end pipeline launcher

## Authoring

- `authoring\start_authoring_terminal.bat`
  - opens a FilmCreator shell for planning or authoring work
- `authoring\test_lmstudio_connectivity.bat`
  - verifies the LM Studio connection before authoring
- `authoring\test_pilot_scene_prompt_writer_lmstudio.bat`
  - rewrites the canonical pilot prompt packages for `SC001/CL001`
- `authoring\princess_of_mars\test_princess_of_mars_authoring_checkpoint.bat`
  - runs the full chapter-to-analysis-to-prompt checkpoint for `princess_of_mars_test`
- `authoring\princess_of_mars\test_princess_of_mars_authoring_checkpoint_ch09.bat`
- `authoring\princess_of_mars\test_princess_of_mars_authoring_checkpoint_ch10.bat`
- `authoring\princess_of_mars\test_princess_of_mars_chapter_analysis_pass.bat`
- `authoring\princess_of_mars\test_princess_of_mars_scene_planning_pass.bat`
- `authoring\princess_of_mars\test_princess_of_mars_shared_prompt_pass.bat`
- `authoring\princess_of_mars\test_princess_of_mars_clip_prompt_pass.bat`
- `authoring\princess_of_mars\test_princess_of_mars_full_chapter_authoring.bat`

## Render

### `render/8188/`

- `start_comfyui_8188.bat`
- `start_render_terminals.bat`
- `run_pilot_scene_keyframe_batch.bat`
- `test_review_and_approve_pilot_keyframe.bat`

### `render/clean_8190/`

- `start_comfyui_clean_8190.bat`
- `start_render_terminals_clean_8190.bat`
- `run_pilot_scene_keyframe_batch_clean_8190.bat`
- `run_pilot_scene_still_fix_batch_clean_8190.bat`
- `test_review_and_approve_pilot_still_fix.bat`

### `render/video_8191/`

- `start_comfyui_video_8191.bat`
- `start_render_terminals_video_8191.bat`
- `run_pilot_scene_cut_motion_batch_video_8191.bat`
- `test_review_and_approve_pilot_cut_motion.bat`

## Multi-Chapter

- `multi_chapter\test_multi_chapter_ingest_setup.bat`
  - reads `book_input.txt`, writes the raw book file, and splits chapters
- `multi_chapter\test_multi_chapter_full_run.bat`
  - runs the multi-chapter analysis pass
- `multi_chapter\run_full_book_to_prompt_pipeline.bat`
  - runs the full book-to-prompt pipeline from chapter summaries through prompt preparation
- `multi_chapter\run_full_book_to_prompt_pipeline_resume.bat`
  - retries failed book-analysis chapters and resumes from the last partial chapter before running the full pipeline
- `multi_chapter\run_quality_grading_and_selective_reruns.bat`
  - grades synthesis outputs and writes the selective rerun queue without mutating the source artifacts
- `multi_chapter\run_quality_rerun_queue.bat`
  - previews the graded rerun queue and optionally executes queued family reruns after confirmation
- `multi_chapter\run_dialogue_enrichment.bat`
  - enriches dialogue delivery metadata for the existing dialogue timeline
- `multi_chapter\clear_downstream_artifacts.bat`
  - removes downstream synthesis artifacts while preserving story analysis and chapter summaries
- `multi_chapter\test_phase_b1_resolution.bat`
  - runs the Phase B1 identity and environment resolution helper

## Current pilot assets

- batch manifest: `projects/pilot_scene/05_scenes/SC001/clips/CL001/logs/RUN_0001.json`
- environment ref: `projects/pilot_scene/05_scenes/SC001/clips/CL001/inputs/smoke_env.png`
- character ref: `projects/pilot_scene/05_scenes/SC001/clips/CL001/inputs/smoke_char.png`

## Suggested flow

1. Run `authoring\test_lmstudio_connectivity.bat`
2. For chapter authoring, use the scripts under `authoring\princess_of_mars\`
3. For render smoke tests, start with `render\clean_8190\start_render_terminals_clean_8190.bat`
4. Then run the matching batch launcher in the same folder
5. Use the review-and-approve launcher in that same runtime folder to validate the handoff
