# Task
T005 Scene Breakdown And Beats

## Objective

Take one extracted scene and deepen it into a staging-focused scene file plus reusable beat bundles that later clip plans can inherit from.

## Inputs

- `01_source/chapters/CH008_a_princess_of_mars_ch08.md`
- `02_story_analysis/chapter_analysis/CH008_summary.md`
- `02_story_analysis/character_breakdowns/CHARACTER_INDEX.md`
- `02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md`
- `02_story_analysis/scene_breakdowns/<scene_id>.md`

## Output Files

- updated `02_story_analysis/scene_breakdowns/<scene_id>.md`
- `02_story_analysis/beat_bundles/<scene_id>/BEAT_INDEX.md`
- `02_story_analysis/beat_bundles/<scene_id>/<beat_id>.md` for each beat in the scene

## Response Contract

Return one tagged Markdown packet only:

- packet task: `scene_beats`
- top-level sections:
  - `updated_scene_markdown`
  - `beat_index_markdown`
- repeated record type:
  - `beat`
- each `beat` record must contain fields:
  - `beat_id`
- each `beat` record must contain sections:
  - `markdown`

## Required Coverage

- ordered beat list for the scene
- dramatic purpose of each beat
- beat start state and end state
- character placement and movement logic
- room or geography facts that multiple clips will need
- axis, eyeline, and screen-direction risks when relevant
- prop, vehicle, crowd, and environmental state that affects continuity
- likely coverage families for each beat
- which beats are most likely to yield the first 1-2 test clips

## Rules

- keep the same `scene_id`
- use beat IDs in `BT###` form within the scene
- if the scene is simple, still emit at least `BT001`
- proper nouns are allowed in analysis output
- write staging facts and continuity facts separately from interpretation when possible
- do not create clip IDs yet
- do not write render-facing prompt text yet

## Local LLM Guidance

- prefer explicit staging and geography over literary paraphrase
- favor deterministic extraction over creative expansion
- if the chapter is ambiguous, record the ambiguity instead of forcing false precision
- keep this pass focused on scene-to-beat decomposition only, not clip or prompt writing
