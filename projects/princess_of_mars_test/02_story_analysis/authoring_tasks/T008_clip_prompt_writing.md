# Task
T008 Clip Prompt Writing

## Objective

Write the canonical clip-local prompt packages for one scene or one clip using the clip plans, scene analysis, and shared asset context.

## Inputs

- `02_story_analysis/story_summary/project_summary.md`
- `02_story_analysis/chapter_analysis/CH001_summary.md`
- `02_story_analysis/character_breakdowns/CHARACTER_INDEX.md`
- `02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md`
- `02_story_analysis/scene_breakdowns/<scene_id>.md`
- `02_story_analysis/beat_bundles/<scene_id>/BEAT_INDEX.md`
- `02_story_analysis/beat_bundles/<scene_id>/<beat_id>.md`
- `02_story_analysis/clip_plans/<scene_id>/<scene_id>_clip_roster.md`
- `02_story_analysis/clip_plans/<scene_id>/<clip_id>.md`

## Output Files

- `03_prompt_packages/scenes/<scene_id>/<clip_id>/<scene_id>_<clip_id>_scene_stage_prompt.md`
- `03_prompt_packages/keyframes/<scene_id>/<clip_id>/<scene_id>_<clip_id>_keyframe_prompt.md`
- `03_prompt_packages/fixes/<scene_id>/<clip_id>/<scene_id>_<clip_id>_fix_01_prompt.md`
- `03_prompt_packages/cut_motion/<scene_id>/<clip_id>/<scene_id>_<clip_id>_cut_motion_prompt.md`

## Response Contract

Return valid JSON only with these keys:

- `scene_id`
- `prompt_files`

Where `prompt_files` is an array of objects containing:

- `clip_id`
- `stage`
- `path`
- `workflow_type`
- `markdown`

## Required Coverage

- one canonical prompt package per prompt role
- scene-stage planning prompt for staging intent only
- keyframe prompt describing the exact visible opening frame
- still-fix prompt describing corrective still intent only
- cut-motion prompt describing visible motion from the approved keyframe
- canonical `Inputs` metadata
- continuity notes tied to the clip plan
- repair notes tied to the stage role
- sources pointing back to the analysis and clip-plan files

## Rules

- use the canonical Markdown prompt-package schema
- stage workflow types should remain canonical:
  - `authoring.scene_stage`
  - `still.scene_build.four_ref.klein.distilled`
  - `still.scene_insert.two_ref.klein.distilled`
  - `video.cut_motion.wan.i2v`
- prompt bodies for keyframe, still-fix, and cut-motion should avoid proper nouns and prefer descriptive noun phrases
- `required_refs` and `optional_refs` should describe slot expectations such as `image_1`, `image_2`, or `source_frame`, not concrete runtime file paths
- keep `duration_seconds` in metadata only, never in the prompt body
- the base prompt writer writes one canonical prompt per role; style-profile variants are created later by the batch planner

## Stage Guidance

- `scene_stage`
  - describe staging intent, subject placement, environmental context, and cut purpose
  - do not write it like a raw render prompt
- `keyframe`
  - describe a single frozen visible state at cut start
  - preserve the chosen starting-keyframe strategy from the clip plan
- `still_fix`
  - preserve composition and look while correcting a specific issue
  - do not redesign the whole shot
- `cut_motion`
  - assume the approved keyframe already carries identity, composition, and base look
  - describe visible subject motion, camera behavior, and environmental change
  - preserve the approved keyframe lighting and color grade unless the clip plan explicitly requests a transition

## Local LLM Guidance

- prefer structured JSON outputs with strict schemas when the local model supports them
- keep temperatures low for deterministic file regeneration
- separate planning logic from final render-facing wording
- if the clip plan and source text conflict, note the conflict in continuity notes rather than silently drifting
