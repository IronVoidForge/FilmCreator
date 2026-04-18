# Task
T002 Character Extraction

## Objective

Extract the visible and referenced characters from the chapter and normalize them into stable character breakdown files plus a chapter-local character roster.

## Inputs

- `01_source/chapters/CH001_a_princess_of_mars_ch08.md`
- `02_story_analysis/chapter_analysis/CH001_summary.md`

## Output Files

- `02_story_analysis/character_breakdowns/CHARACTER_INDEX.md`
- `02_story_analysis/character_breakdowns/<asset_id>.md` for each extracted character

## Response Contract

Return one tagged Markdown packet only:

- packet task: `character_extraction`
- top-level sections:
  - `character_index_markdown`
- repeated record type:
  - `character`
- each `character` record must contain fields:
  - `asset_id`
  - `manual_description_required`
  - `manual_description_reason`
- each `character` record must contain sections:
  - `markdown`

## Required Coverage

- name and role in the chapter
- whether the character is physically present, only referenced, or uncertain
- physical description
- silhouette or costume clues
- continuity-critical traits
- useful descriptive noun phrases for later render-facing prompt writing

## Rules

- proper nouns are allowed in analysis output
- normalize one stable `asset_id` per character
- mark uncertainty when a character is present but underdescribed
- include character relationships when they matter to staging
- do not write final image prompts yet
- if a character lacks enough stable visual description for dependable later generation, set `manual_description_required: true`
- when `manual_description_required` is true, explain why in `manual_description_reason`
- do not invent ornate missing visual details just to avoid raising the flag

## Character Extraction Notes

- prioritize characters who are visually present in the chapter
- separate named characters from unnamed groups such as crew, warriors, or civilians
- only create separate asset IDs for unnamed groups if they are likely to matter as recurring visual entities
- flagged characters should later receive a manual pasted description under `01_source/character_descriptions/`
- keep this as one single-purpose LM Studio call rather than bundling later scene or shot planning into the same response
