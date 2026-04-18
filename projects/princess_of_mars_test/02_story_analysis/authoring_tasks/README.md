# Princess Of Mars Authoring Task Pack

## Goal

Turn one pasted public-domain chapter into:

- project story summary context
- character and environment breakdowns
- one or more scene breakdowns
- beat bundles
- clip rosters
- clip plans
- shared reference prompt packages
- clip-local prompt packages for at least 1-2 test clips

## Working Rule

- This test run happens before SQLite implementation.
- Files are the source of truth for this test pass.
- We only move to SQLite after we can prove:
  - chapter -> scene breakdown
  - character/environment extraction
  - clip planning
  - prompt writing
  - at least 1-2 shot-ready clip plans from a scene

## Implementation Order

1. `T001_chapter_intake_and_summary.md`
2. `T002_character_extraction.md`
3. `T003_environment_extraction.md`
4. `T004_scene_decomposition.md`
5. `T005_scene_breakdown_and_beats.md`
6. `T006_clip_roster_and_clip_plans.md`
7. `T007_shared_reference_prompt_writing.md`
8. `T008_clip_prompt_writing.md`

## Handoffs

- Chapter source -> analysis
- Analysis -> scene and beat structure
- Scene and beat structure -> clip plans
- Clip plans + shared assets -> prompt packages
- Prompt packages -> render runner

## Output Targets

- `02_story_analysis/story_summary/project_summary.md`
- `02_story_analysis/character_breakdowns/*.md`
- `02_story_analysis/environment_breakdowns/*.md`
- `02_story_analysis/scene_breakdowns/*.md`
- `02_story_analysis/beat_bundles/<scene_id>/*.md`
- `02_story_analysis/clip_plans/<scene_id>/<scene_id>_clip_roster.md`
- `02_story_analysis/clip_plans/<scene_id>/<clip_id>.md`
- `03_prompt_packages/characters/<asset_id>/<asset_id>_ref_prompt.md`
- `03_prompt_packages/environments/<asset_id>/<asset_id>_ref_prompt.md`
- `03_prompt_packages/scenes/<scene_id>/<clip_id>/<scene_id>_<clip_id>_scene_stage_prompt.md`
- `03_prompt_packages/keyframes/<scene_id>/<clip_id>/<scene_id>_<clip_id>_keyframe_prompt.md`
- `03_prompt_packages/cut_motion/<scene_id>/<clip_id>/<scene_id>_<clip_id>_cut_motion_prompt.md`

## Prompting Rules

- For analysis tasks:
  - proper nouns are allowed
  - return structured Markdown or JSON exactly as requested
  - be explicit about uncertainty instead of guessing hidden facts
- For render-facing prompt writing:
  - avoid proper nouns in the final prompt body
  - use descriptive noun phrases
  - keep duration in metadata, not the prompt body
  - preserve the approved keyframe look unless the plan explicitly calls for a lighting transition
