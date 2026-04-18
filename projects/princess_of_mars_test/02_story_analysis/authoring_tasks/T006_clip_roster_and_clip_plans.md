# Task
T006 Clip Roster And Clip Plans

## Objective

Turn one scene plus its beat bundles into an ordered clip roster and one clip-plan file per clip.

## Inputs

- `02_story_analysis/chapter_analysis/CH001_summary.md`
- `02_story_analysis/character_breakdowns/CHARACTER_INDEX.md`
- `02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md`
- `02_story_analysis/scene_breakdowns/<scene_id>.md`
- `02_story_analysis/beat_bundles/<scene_id>/BEAT_INDEX.md`
- `02_story_analysis/beat_bundles/<scene_id>/<beat_id>.md`

## Output Files

- `02_story_analysis/clip_plans/<scene_id>/<scene_id>_clip_roster.md`
- `02_story_analysis/clip_plans/<scene_id>/<clip_id>.md` for each planned clip

## Response Contract

Return one tagged Markdown packet only:

- packet task: `clip_planning`
- top-level sections:
  - `clip_roster_markdown`
- repeated record type:
  - `clip`
- each `clip` record must contain fields:
  - `clip_id`
- each `clip` record must contain sections:
  - `markdown`

## Required Coverage

- ordered clip list for the scene
- one-line purpose for each clip
- beat mapping for each clip
- duration seconds
- composition type
- continuity mode
- starting keyframe strategy
- dependency policy
- auto-advance policy
- review fallback strategy
- look continuity policy
- visible character assets
- shared ref targets
- required refs and optional refs
- opening keyframe intent
- cut motion intent
- interval beats for the clip
- expected prompt files
- expected outputs

## Rules

- clip IDs must use `CL###`
- `clip = cut` in this planning phase
- default most clips to approximately 5 seconds and one short motion segment
- only plan multi-segment motion when the scene genuinely needs a longer clip
- treat `continuous_follow` as rare
- prefer `independent` or `soft_ref_previous` when the shot can be generated without waiting on prior video completion
- separate the opening frozen frame from the later motion description
- note when a clip is a strong candidate for optional identity-consistency assist

## Planning Guidance

- prefer these coverage patterns for normal scene coverage:
  - `reframe_same_moment`
  - `reblock_same_scene`
  - `insert`
  - `cutaway`
- use previous-video-last-frame continuity only when the shot genuinely needs direct carry-forward or when a fallback path should be prepared
- identify the first one or two clips that should become the earliest renderable tests

## Local LLM Guidance

- plan clips scene by scene, not paragraph by paragraph
- be explicit about what must be preserved from beat bundles so later prompt writing does not have to infer it
- keep duration in metadata fields, not later prompt wording
- keep this pass focused on beat-map-to-cut-list planning, not final prompt package wording
