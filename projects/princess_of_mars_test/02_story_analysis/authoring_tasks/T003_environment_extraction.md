# Task
T003 Environment Extraction

## Objective

Extract the environment families from the chapter and normalize them into stable environment breakdown files plus a chapter-local environment roster.

## Inputs

- `01_source/chapters/CH001_a_princess_of_mars_ch08.md`
- `02_story_analysis/chapter_analysis/CH001_summary.md`

## Output Files

- `02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md`
- `02_story_analysis/environment_breakdowns/<asset_id>.md` for each extracted environment family

## Response Contract

Return one tagged Markdown packet only:

- packet task: `environment_extraction`
- top-level sections:
  - `environment_index_markdown`
- repeated record type:
  - `environment`
- each `environment` record must contain fields:
  - `asset_id`
- each `environment` record must contain sections:
  - `markdown`

## Required Coverage

- environment family name
- whether it is a primary setting, secondary setting, or transit setting
- architecture or geography
- lighting and atmosphere cues
- scale cues
- recurring props or vehicles tied to the environment
- useful descriptive noun phrases for later render-facing prompt writing

## Rules

- proper nouns are allowed in analysis output
- normalize one stable `asset_id` per environment family
- prefer reusable environments over one-off micro locations when possible
- do not write final image prompts yet

## Environment Extraction Notes

- separate:
  - airship exterior
  - abandoned Martian city
- plaza/street zones
- valley/plain battlefield zones
- only split environments when later shot planning would genuinely benefit from separate reference stills
- keep this as one single-purpose LM Studio call rather than combining it with scene decomposition
