# Story Analysis Workspace

## Purpose

This folder is the file-first authoring workspace for the pre-SQL test run.

The goal is to take one pasted public-domain chapter and turn it into:

- story and chapter summaries
- character and environment breakdowns
- scene breakdowns and beat bundles
- clip rosters and clip plans
- shared reference prompt packages
- clip-local prompt packages for initial test clips
- manual character-description placeholders when the chapter does not describe a character well enough

## Current Status

- Chapter intake, character extraction, environment extraction, scene decomposition, beat bundling, and clip planning are working on the live `Princess of Mars` chapter pilot.
- `plan-scene` now produces canonical scene, beat, and clip files for `SC001`.
- Shared prompt generation is partially working, but some character assets still return empty or malformed LM Studio output and need a final robustness pass.
- SQLite has not been implemented yet; the file-first authoring pass is still the source of truth.

## Pre-SQL Rule

- Files are the source of truth in this phase.
- We do not migrate to SQLite until this workspace can reliably produce:
  - chapter analysis
  - scene decomposition
  - beat bundles
  - clip plans
  - prompt packages for at least one or two clips

## Implementation Sequence

1. Chapter intake and summary
2. Character extraction
3. Environment extraction
4. Scene decomposition
5. Scene-level beat bundles
6. Clip roster and clip plans
7. Shared character and environment prompt writing
8. Clip-local prompt writing

## First Real Testable Milestone

The first meaningful pre-SQL checkpoint is:

- one chapter analyzed
- one scene decomposed
- one scene clip roster written
- one or two clip plans written
- canonical prompt packages written for those clips
- shared character/environment prompt generation should succeed for the same scene without blocking the whole run

At that point we can verify the authoring handoff end to end before database work.

## Implementation Notes

- LM Studio side:
  - every LM Studio invocation should perform one bounded task only
  - convenience commands may chain multiple single-purpose LM Studio calls, but should not ask the model to do chapter analysis, scene planning, cut planning, and prompt writing in one response
  - prefer tagged Markdown packet outputs for chapter analysis, scene planning, and shared prompt drafting
  - use parser-side validation and conversion instead of trusting nested JSON from the local model
  - keep temperatures low for reproducible extraction and file regeneration
  - current difficulty: shared prompt drafting still sometimes returns empty or malformed packets for manual-description-required characters
- ComfyUI side:
  - treat workflows as node graphs with known patch points, not as freeform prompt blobs
  - keep authoring outputs workflow-aware by naming required reference slots like `image_1` or `source_frame`
  - avoid baking concrete runtime file paths into canonical prompt packages
- Pipeline rule:
  - analysis and planning may use proper nouns
  - final render-facing prompt bodies should prefer descriptive noun phrases instead

## Output Map

- `story_summary/`
- `chapter_analysis/`
- `character_breakdowns/`
- `environment_breakdowns/`
- `scene_breakdowns/`
- `beat_bundles/`
- `clip_plans/`
- `../01_source/character_descriptions/`
- later handoff into `../03_prompt_packages/`
