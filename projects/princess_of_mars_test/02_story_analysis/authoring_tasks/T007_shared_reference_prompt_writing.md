# Task
T007 Shared Reference Prompt Writing

## Objective

Write the reusable shared character-reference and environment-reference prompt packages that later clip generation can depend on.

## Inputs

- `02_story_analysis/story_summary/project_summary.md`
- `02_story_analysis/chapter_analysis/CH001_summary.md`
- `02_story_analysis/character_breakdowns/CHARACTER_INDEX.md`
- `02_story_analysis/character_breakdowns/<asset_id>.md`
- `02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md`
- `02_story_analysis/environment_breakdowns/<asset_id>.md`

## Output Files

- `03_prompt_packages/characters/<asset_id>/<asset_id>_ref_prompt.md`
- `03_prompt_packages/environments/<asset_id>/<asset_id>_ref_prompt.md`

## Response Contract

Return valid JSON only with these keys:

- `character_prompts`
- `environment_prompts`

Where each array item contains:

- `asset_id`
- `path`
- `workflow_type`
- `markdown`

## Required Coverage

- stable visual identity for recurring characters
- stable geography and lighting identity for recurring environments
- continuity-critical traits that later clips must inherit
- positive prompt
- negative prompt
- inputs section using canonical metadata fields
- continuity notes
- repair notes when useful
- sources section pointing back to analysis files

## Rules

- use the canonical Markdown prompt-package schema
- use workflow type `still.t2i.klein.distilled` for the current shared-reference still path unless a future workflow family replaces it
- proper nouns may appear in titles, purpose text, inputs, and sources
- the final positive and negative prompt bodies should avoid proper nouns and use descriptive noun phrases instead
- optimize for reusable shared refs, not one-off scene staging
- do not leak clip-specific blocking into the shared reference prompts

## Prompt Guidance

- character prompts should emphasize stable face, hair, body type, costume logic, silhouette, and recurring materials
- environment prompts should emphasize stable architecture, geography, scale, atmosphere, and recurring environmental anchors
- keep prompts concrete, visible, and local to what the image should show
- avoid lore-only facts that do not change the pixels

## Local LLM Guidance

- prefer structured JSON output that maps directly to files
- use low temperature and stable wording so reruns preserve asset identity
- if an asset is underdescribed, preserve uncertainty instead of inventing ornate detail
