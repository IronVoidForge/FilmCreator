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

The active multi-chapter launcher set is now ordered by workflow stage:

- `multi_chapter\00_prepare_book_ingest.bat`
  - reads `book_input.txt`, writes the raw book file, and splits chapters
- `multi_chapter\01_reset_downstream_artifacts.bat`
  - removes downstream synthesis artifacts while preserving story analysis and chapter summaries
- `multi_chapter\10_run_full_book_pipeline_from_scratch.bat`
  - runs the full book-to-prompt pipeline from chapter summaries through prompt preparation
- `multi_chapter\11_resume_full_book_pipeline.bat`
  - retries failed book-analysis chapters and resumes from the last partial chapter before running the full pipeline
- `multi_chapter\12_run_dev_slice_downstream_pipeline.bat`
  - runs a chapter-slice downstream pipeline, defaulting to chapters `1-6`, without rerunning character/environment synthesis, and automatically resumes the latest interrupted matching run
- `multi_chapter\13_resume_latest_dev_slice_run.bat`
  - shows the saved `dev_slice_downstream` run summary and resumes the latest matching interrupted dev-slice run
- `multi_chapter\20_run_scene_bindings_only.bat`
  - resolves scene-level cast and environment bindings before shot planning, with an optional chapter filter
- `multi_chapter\21_run_scene_bindings_and_downstream.bat`
  - reruns scene bindings plus all affected downstream stages without rerunning character/environment synthesis, with an optional chapter filter, and automatically resumes the latest interrupted matching run
- `multi_chapter\22_run_dialogue_enrichment_only.bat`
  - enriches dialogue delivery metadata for the existing dialogue timeline
- `multi_chapter\30_run_quality_grading.bat`
  - grades synthesis outputs and writes the selective rerun queue without mutating the source artifacts
- `multi_chapter\31_run_quality_rerun_queue.bat`
  - previews the graded rerun queue and optionally executes queued family reruns after confirmation

Legacy `test_*`, broad cleanup, and older duplicate multi-chapter launchers were removed because they were either superseded by the numbered workflow launchers or tied to outdated pipeline shapes.

## Current pilot assets

- batch manifest: `projects/pilot_scene/05_scenes/SC001/clips/CL001/logs/RUN_0001.json`
- environment ref: `projects/pilot_scene/05_scenes/SC001/clips/CL001/inputs/smoke_env.png`
- character ref: `projects/pilot_scene/05_scenes/SC001/clips/CL001/inputs/smoke_char.png`

## Suggested flow

1. Run `multi_chapter\00_prepare_book_ingest.bat` if the source book still needs ingest
2. Use `multi_chapter\10_run_full_book_pipeline_from_scratch.bat` for a clean full build
3. Use `multi_chapter\11_resume_full_book_pipeline.bat` to continue an interrupted full build
4. Use `multi_chapter\12_run_dev_slice_downstream_pipeline.bat` for fast iteration on a chapter subset
5. Use `multi_chapter\21_run_scene_bindings_and_downstream.bat` when only scene bindings and later stages need refresh
6. Use `multi_chapter\30_run_quality_grading.bat` after a run to inspect weak artifacts
7. For render smoke tests, start with `render\clean_8190\start_render_terminals_clean_8190.bat`
