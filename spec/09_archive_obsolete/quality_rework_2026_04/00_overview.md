# Quality Rework 2026-04 Overview

Base commit reviewed: `cabce3d9bcf5b658a0daf6899b4e018a7c6bba0a`.

This folder specifies the next quality rework for the FilmCreator downstream prompt pipeline. The goal is to connect systems that already partly exist: strict canon bibles, descriptor supported/generated fields, visual fallback synthesis, prompt package assembly, and quality grading.

## Core finding

The pipeline is producing real artifacts, but the strongest context does not always reach the exact prompt fields used by generation.

Current state:

- `VISUAL_FALLBACKS.json` is strong and project-specific.
- Descriptor enrichment has supported/generated fields and `reference_repair`.
- Prompt preparation defensively synthesizes visual fallbacks if missing.
- Character and environment reference prompts mostly receive book-level context and negative steering.
- Shot prompts have role mapping bugs and weaker fallback injection.
- Character bibles remain too conservative when source evidence is thin.
- Quality grading over-approves prompt packages and misclassifies silent dialogue timelines as failures.

## Spec files

1. `01_CHARACTER_BIBLE_PRODUCTION_FALLBACKS.md`
   - Add strict-canon vs visual-production-fallback separation to character bibles.
   - Avoid unknowns in prompt-facing fallback fields while preserving canon honesty.

2. `02_DESCRIPTOR_PROMPT_NORMALIZATION.md`
   - Make descriptor `reference_repair` and production fallback fields the normalized prompt-facing view.
   - Ensure prompt prep consumes repaired fields before generic generated placeholders.

3. `03_ENVIRONMENT_AND_SHOT_PROMPT_INJECTION.md`
   - Inject bucket-specific environment positive context.
   - Fix shot image role mapping.
   - Add character/environment fallback negative terms to shot prompts.

4. `04_QUALITY_GRADING_CALIBRATION.md`
   - Tighten prompt package grading.
   - Fix dialogue timeline silent-shot semantics.

5. `05_SMART_RESUME_VALIDATION.md`
   - Replace sentinel-only skip logic with artifact validation.

6. `06_TEST_PLAN.md`
   - Unit tests and focused checks that avoid rerunning the whole pipeline.

## Preferred branch sequence

### Branch A: prompt quality injection and grading

Files:

- `orchestrator/prompt_preparation.py`
- `orchestrator/quality_grading.py`
- focused tests

This branch should handle:

- prompt field precedence
- environment fallback bucket injection
- shot image role repair
- shot negative fallback injection
- prompt package grading calibration

### Branch B: character bible production fallback

Files:

- `orchestrator/character_bible.py`
- `orchestrator/character_bible_models.py`
- `orchestrator/descriptor_enrichment.py`
- focused tests

This branch should handle:

- explicit `visual_production_fallback` block
- context-only policy for non-renderable entities
- descriptor ingestion of fallback block

## Do not do this first

Do not add a broad prompt smoothing layer before fixing the deterministic bugs. The current weaknesses are traceable to specific handoff points:

- character bible unknowns
- descriptor repair not dominating prompt-facing fields
- shot prompt image role mismatch
- missing shot fallback negatives
- environment fallback geometry not entering positive prompts
- over-lenient prompt grading

A smoothing layer can be added later as a final polish pass, but it should not be responsible for rescuing broken identity/reference logic.

## Validation philosophy

Each spec includes unit-level or focused artifact checks. Do not validate by rerunning the full pipeline first. Validate functions directly, then use the smart resume runner only after targeted tests pass.
