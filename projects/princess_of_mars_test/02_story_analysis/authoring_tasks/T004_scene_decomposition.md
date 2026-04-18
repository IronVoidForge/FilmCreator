# Task
T004 Scene Decomposition

## Objective

Break the chapter into discrete scenes that can later be planned into beats and clips.

## Inputs

- `01_source/chapters/CH001_a_princess_of_mars_ch08.md`
- `02_story_analysis/chapter_analysis/CH001_summary.md`
- `02_story_analysis/character_breakdowns/CHARACTER_INDEX.md`
- `02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md`

## Output Files

- `02_story_analysis/scene_breakdowns/SCENE_INDEX.md`
- `02_story_analysis/scene_breakdowns/<scene_id>.md` for each extracted scene

## Response Contract

Return one tagged Markdown packet only:

- packet task: `scene_decomposition`
- top-level sections:
  - `scene_index_markdown`
- repeated record type:
  - `scene`
- each `scene` record must contain fields:
  - `scene_id`
- each `scene` record must contain sections:
  - `markdown`

## Required Coverage

- scene purpose
- scene summary
- participating characters
- participating environments
- dominant emotional shift
- likely visual coverage families
- likely continuity sensitivities

## Rules

- scene IDs must use `SC###`
- prefer a small number of coherent scenes over excessive fragmentation
- scene boundaries should be driven by dramatic and staging changes, not every paragraph break
- do not create clip plans yet

## Scene Boundary Guidance

- create a new scene when one or more of these changes materially:
  - location or environment family
- dramatic goal
- major action phase
- dominant staging problem
- emotional beat family
- keep this pass focused on chapter-to-scene decomposition only, not beat or clip planning
