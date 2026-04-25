# Visual Fallbacks, Descriptor Repair, and Chapter-Slice Reference Prep Spec

## Purpose

This spec defines the next quality pass for FilmCreator's visual prompt pipeline. The goal is to prevent weak, generic, or unresolved prompt packages from producing bad reference assets such as modern business portraits for ambiguous characters or generic landscapes for specific environments.

The spec covers:

1. `VISUAL_FALLBACKS.json` generation
2. Character descriptor repair
3. Environment descriptor repair
4. Prompt-prep fallback injection
5. Phase 12/13 recommended-warning behavior
6. Chapter-aware test-slice selection
7. Quick-test BAT updates

## Problem Summary

Recent Phase 12/13 tests exposed two major failures.

### Character failure

`ape_man_1` generated as modern portrait subjects, including corporate-style clothing. The repository shows `ape_man_1` has an unresolved clarification file and may match other existing identities. It should not have been treated as a stable canonical character reference target by default.

Root causes:

- unresolved identity entered reference generation
- missing or weak character descriptors reached prompt prep
- missing costume fields allowed modern clothing drift
- no project-level visual/wardrobe fallback was available

### Environment failure

`arizona_mountain_cave` generated as generic open hills/grassland instead of a cave reference.

Root causes:

- missing environment fields reached prompt prep
- the positive prompt relied on generic language like `described environment with stable spatial anchors`
- no specific cave landmark, cliff face, rocky threshold, or shadowed interior was injected
- no project-level environment fallback existed

## Design Principles

- Base prompt packages should contain canonical source-aware visual context.
- Booster packs remain generation-time experimental modifiers, not the source of canon.
- Missing required fields block generation.
- Missing recommended fields warn and trigger repair/fallback, but do not block by themselves.
- Fallback text must be marked as inferred or fallback, not treated as explicit book canon.
- The book title may be stored as provenance, but prompts must use visual descriptors that do not depend on the model knowing the book.
- Chapter test slices should select characters/environments from the chosen chapters, not arbitrary global entries.

---

# Phase Placement

## Phase 10.5: Visual Fallback Synthesis

Add a lightweight visual fallback synthesis layer before descriptor enrichment and prompt preparation.

### Output artifact

```text
projects/<project>/02_story_analysis/world/global/VISUAL_FALLBACKS.json
```

### Inputs

Use existing project artifacts where available:

```text
book/project summary
chapter summaries
continuity summaries
world snapshots
character bibles
environment bibles
```

The first implementation should prioritize a book-level fallback. Chapter-level fallbacks may be added later, but are not required for the first pass.

### Required JSON shape

```json
{
  "schema_version": "2026-04-visual-fallbacks-v1",
  "project_slug": "princess_of_mars_test",
  "source_title": "A Princess of Mars",
  "book_visual_context": "early pulp planetary-romance adventure, frontier desert realism, non-modern clothing, weathered natural materials, ancient alien-world culture, cinematic readable reference lighting",
  "character_fallbacks": {
    "general": "non-modern pulp adventure wardrobe and readable cinematic reference styling",
    "earth_human": "late-19th-century frontier adventure clothing, weathered natural fabrics, belts, boots, simple utilitarian garments, no modern suit or tie unless explicitly described",
    "barsoom_humanoid": "ancient alien-world planetary-romance wardrobe, harnesses, ornaments, tribal or gladiatorial elements, no modern Earth clothing",
    "creature_or_primitive": "feral or primitive non-modern appearance, rough natural materials if clothed, no tailored business attire",
    "group_or_horde": "coherent group visual language using non-modern tribal, frontier, or alien-world materials as appropriate"
  },
  "environment_fallbacks": {
    "general": "clear cinematic location reference with explicit landmarks, scale, materials, lighting, and atmosphere",
    "desert_mountain": "rugged desert mountain terrain, dry scrub, weathered rock, clear horizon, readable distance and scale",
    "cave_or_cliffside": "visible cave mouth, cliffside rock face, rocky threshold, shadowed interior, weathered stone, readable entrance landmark",
    "interior": "clear room or chamber layout, foreground/midground/background separation, pathways, anchor objects, visible scale",
    "wilderness": "natural terrain with distinct foreground, midground, background, landmarks, lighting, and weather atmosphere"
  },
  "negative_terms": {
    "character_wardrobe": [
      "modern suit",
      "necktie",
      "business attire",
      "office clothing",
      "corporate headshot",
      "passport photo",
      "turtleneck",
      "modern athletic shirt"
    ],
    "environment": [
      "generic meadow",
      "open grassy field",
      "rolling green hills",
      "no cave",
      "hidden landmark",
      "modern road",
      "cars",
      "modern buildings"
    ]
  }
}
```

### Generation method

The first implementation may be deterministic for known project types, but the intended implementation is:

1. Read the book/project summary.
2. Ask the configured LLM to synthesize a short, descriptor-heavy `book_visual_context`.
3. Ask for generic character and environment fallback buckets.
4. Validate the JSON shape.
5. Fall back to deterministic defaults if the LLM call fails.

The prompt to the LLM should explicitly say:

```text
Do not rely on the model knowing the source title. Produce visual descriptors that can guide image generation directly.
```

---

# Phase 11: Descriptor Enrichment Repair

Phase 11 should repair visual reference fields before Phase 11.5 prompt preparation writes prompt packages.

## Character descriptor repair

### Fields to repair

```text
identity_descriptor
body_descriptor
face_descriptor
costume_descriptor
posture_descriptor
expression_descriptor
locked_fields
source_visual_context
subject_visual_context
```

### Weak values

Treat these as weak:

```text
blank
unknown
n/a
none
null
[]
described character with stable costume and silhouette
metadata-only summaries
```

### Repair sources

Use, in priority order:

1. descriptor record supported/generated values
2. character bible fields
3. character clarification/source description, if resolved
4. book visual context from `VISUAL_FALLBACKS.json`
5. selected fallback bucket from `character_fallbacks`
6. safe reference defaults

### Required behavior

If costume is weak, write a fallback sentence such as:

```text
Costume not specifically described; use project visual fallback: non-modern pulp adventure clothing, weathered natural materials, frontier or alien-world styling as appropriate. Avoid modern business clothing, suits, ties, turtlenecks, athletic catalog styling, and corporate portrait styling.
```

If posture is weak:

```text
Neutral readable reference posture unless chapter context specifies action.
```

If expression is weak:

```text
Neutral readable expression unless chapter context specifies fear, aggression, grief, exhaustion, or another clear emotion.
```

If locked fields are weak:

```text
Preserve confirmed species or body type, skin tone, silhouette, costume era, and any source-supported distinguishing traits.
```

### Storage

Do not overwrite raw extraction. Store repaired values under a clear key, for example:

```json
{
  "reference_repair": {
    "costume_descriptor": "...",
    "posture_descriptor": "...",
    "expression_descriptor": "...",
    "locked_fields": "...",
    "source_visual_context": "...",
    "subject_visual_context": "...",
    "repair_sources": ["VISUAL_FALLBACKS.json", "character bible"]
  }
}
```

If the existing descriptor schema already uses `generated_field_values`, repaired values may be mirrored there, but the repair source should remain explicit.

## Environment descriptor repair

### Fields to repair

```text
layout_descriptor
scale_descriptor
architecture_descriptor
landmark_descriptor
lighting_descriptor
mood_descriptor
locked_fields
source_visual_context
subject_visual_context
```

### Weak values

Treat these as weak:

```text
blank
unknown
n/a
none
null
[]
described environment with stable spatial anchors
described environment with stable spatial continuity
metadata-like internal tokens without natural-language visual anchors
```

### Repair sources

Use, in priority order:

1. descriptor record supported/generated values
2. environment bible fields
3. scene contracts and bindings
4. book visual context from `VISUAL_FALLBACKS.json`
5. selected fallback bucket from `environment_fallbacks`
6. safe reference defaults

### Required behavior

For a cave/cliffside environment, repair should explicitly include:

```text
visible cave mouth
cliffside rock face
rocky threshold
shadowed interior
weathered stone
readable entrance landmark
```

For `arizona_mountain_cave`, repaired fields should resemble:

```json
{
  "layout_descriptor": "rugged Arizona desert mountain slope with a cave entrance set into a cliffside rock face; rocky cave threshold in the foreground and distant desert landscape beyond",
  "scale_descriptor": "human-scale cave mouth within a larger mountain or cliff formation",
  "architecture_descriptor": "natural weathered stone cave, irregular rock walls, rough cave floor, dark interior opening",
  "landmark_descriptor": "clearly visible dark cave mouth in the cliffside, strong rock silhouette around the entrance",
  "lighting_descriptor": "bright Arizona daylight outside with deep cool shadow inside the cave entrance",
  "mood_descriptor": "lonely, mysterious, frontier desert discovery",
  "locked_fields": "preserve cave mouth, cliffside rock face, desert mountain setting, shadowed interior, rocky threshold"
}
```

---

# Phase 11.5: Prompt Preparation Fallback Injection

Prompt preparation must consume repaired descriptor values before writing prompt packages.

## New prompt package inputs

Add these inputs where applicable:

```text
source_visual_context
subject_visual_context
fallback_fields_used
```

### Source visual context

This is book/project-level visual style, not a plot summary.

Good:

```text
early pulp planetary-romance adventure, frontier desert realism, non-modern clothing, weathered natural materials, ancient alien-world culture, cinematic readable reference lighting
```

Bad:

```text
A Princess of Mars chapter 2 where John Carter enters the cave and later travels to Mars
```

The source title may appear in metadata or sources, but the actual prompt body should be descriptor-heavy and not depend on model knowledge of the book.

### Subject visual context

This is a compact sentence describing what the subject must look like or preserve.

Character example:

```text
Rugged non-modern adventure figure; preserve confirmed traits and use era/world-appropriate clothing, not contemporary portrait styling.
```

Environment example:

```text
Frontier desert mountain cave landmark; make the cave mouth, cliffside rock face, rocky threshold, and shadowed interior visually explicit.
```

## Character prompt rules

Character positive prompts should include:

```text
source_visual_context
subject_visual_context
identity/body descriptor
face descriptor
costume descriptor or wardrobe fallback
posture/expression
locked visual fields
reference composition
```

Character positive prompts should not contain raw `unknown` or generic placeholders.

Character negative prompts should include wardrobe drift blockers from `VISUAL_FALLBACKS.json`.

## Environment prompt rules

Environment positive prompts should include:

```text
source_visual_context
subject_visual_context
layout descriptor
scale descriptor
architecture or terrain descriptor
landmark descriptor
lighting descriptor
mood descriptor
locked fields
reference composition
```

Environment positive prompts should not rely on `described environment with stable spatial anchors` when a fallback can be generated.

Environment negative prompts should include environment drift blockers from `VISUAL_FALLBACKS.json`.

---

# Phase 12/13 Recommended-Warning Behavior

## Current issue

Recommended input warnings can currently turn entries into blocked generation requests. This is too strict.

## New behavior

For character and environment reference generation:

```text
missing required inputs = blocked
missing recommended inputs = warnings only
```

Store both:

```json
{
  "blocking_warnings": [],
  "recommended_warnings": ["recommended input `face_descriptor` is missing"],
  "warnings": []
}
```

If Phase 11 repair is working, recommended warnings should become rare. If they remain, they should show up in reports and review queues without blocking generation.

## Unresolved identity guard

Characters with unresolved clarification files should not generate by default.

Default:

```text
identity_review_required = true
skip generation
```

Optional override:

```text
--include-unresolved-identities
```

This prevents provisional or ambiguous IDs like `ape_man_1` from becoming accidental canonical references.

---

# Chapter-Aware Test-Slice Selection

## Current issue

Test-slice selection caps entries but does not guarantee the selected entries are useful subjects from the chosen chapters.

## Desired behavior

Default test-slice for selected chapters:

```text
--chapters 2-3 --test-slice
```

should select:

```text
2 eligible characters from chapters 2-3
2 eligible environments from chapters 2-3
```

not arbitrary global entries.

If a user supplies:

```text
--limit 8
```

then test-slice should select up to 8 eligible subjects from the selected chapters.

## Selection ranking

For characters:

1. chapter match
2. resolved/canonical identity
3. film-facing individual before group/provisional entries
4. protagonist/main/major role signals
5. descriptor completeness
6. recurrence / scene count
7. stable ID and non-placeholder name

For environments:

1. chapter match
2. bound to scenes/shots in selected chapters
3. landmark/location specificity
4. descriptor completeness
5. recurrence / scene count
6. stable ID and non-placeholder name

## Implementation detail

Do not double-limit. In test-slice mode:

```text
slice_limit = user limit if provided, else 2
apply chapter filter and ranking
apply slice_limit
```

Do not apply both the hard validation cap and `eligible[:limit]` afterward.

---

# Quick-Test BAT Updates

## General rules

All quick-test BATs that generate or refresh artifacts should default to:

```bat
set "CHAPTERS=2-3"
```

They should pass:

```bat
--chapters %CHAPTERS%
```

to artifact-producing commands.

The global deletion BAT may remain global, but should warn that it is not chapter-scoped.

## Character prompt-only BAT

Should run:

```bat
python -m orchestrator synthesize-visual-fallbacks %PROJECT_SLUG% --force
python -m orchestrator synthesize-character-bibles %PROJECT_SLUG% --chapters %CHAPTERS% --force
python -m orchestrator synthesize-descriptor-enrichment %PROJECT_SLUG% --chapters %CHAPTERS% --force
python -m orchestrator synthesize-prompt-preparation %PROJECT_SLUG% --chapters %CHAPTERS% --force
```

No image generation.

## Environment prompt-only BAT

Should run:

```bat
python -m orchestrator synthesize-visual-fallbacks %PROJECT_SLUG% --force
python -m orchestrator synthesize-environment-bibles %PROJECT_SLUG% --chapters %CHAPTERS% --force
python -m orchestrator synthesize-descriptor-enrichment %PROJECT_SLUG% --chapters %CHAPTERS% --force
python -m orchestrator synthesize-prompt-preparation %PROJECT_SLUG% --chapters %CHAPTERS% --force
```

No image generation.

## Character image test BAT

Should default to two chapter characters:

```bat
python -m orchestrator generate-character-references %PROJECT_SLUG% ^
  --chapters %CHAPTERS% ^
  --test-slice ^
  --variant bust_portrait ^
  --prompt-variant character_readability ^
  --limit %LIMIT% ^
  --execute
```

Default:

```bat
set "LIMIT=2"
```

## Environment image test BAT

Should default to two chapter environments:

```bat
python -m orchestrator generate-environment-references %PROJECT_SLUG% ^
  --chapters %CHAPTERS% ^
  --test-slice ^
  --variant establishing_wide ^
  --prompt-variant environment_readability ^
  --limit %LIMIT% ^
  --execute
```

Default:

```bat
set "LIMIT=2"
```

---

# Files To Modify

## New files

```text
orchestrator/visual_fallbacks.py
orchestrator/character_descriptor_repair.py
orchestrator/environment_descriptor_repair.py
spec/VISUAL_FALLBACKS_DESCRIPTOR_REPAIR_AND_CHAPTER_SLICE_SPEC.md
```

## Existing files

```text
orchestrator/descriptor_enrichment.py
orchestrator/prompt_preparation.py
orchestrator/character_references.py
orchestrator/environment_references.py
orchestrator/cli.py
launchers/quick_pipeline_test/10_generate_chapter_character_prompts_only.bat
launchers/quick_pipeline_test/11_generate_chapter_environment_prompts_only.bat
```

Potentially:

```text
spec/prompt_boosters/character_reference_boosters.json
spec/prompt_boosters/environment_reference_boosters.json
```

Only update booster JSON if generation-time variants need additional anti-drift modifiers. Canonical fallback content belongs in prompt preparation, not boosters.

---

# Commands To Run After Implementation

For the two-chapter validation slice:

```bat
python -m orchestrator synthesize-visual-fallbacks princess_of_mars_test --force
python -m orchestrator synthesize-character-bibles princess_of_mars_test --chapters 2-3 --force
python -m orchestrator synthesize-environment-bibles princess_of_mars_test --chapters 2-3 --force
python -m orchestrator synthesize-descriptor-enrichment princess_of_mars_test --chapters 2-3 --force
python -m orchestrator synthesize-prompt-preparation princess_of_mars_test --chapters 2-3 --force
```

Then dry-run reference generation:

```bat
python -m orchestrator generate-character-references princess_of_mars_test --chapters 2-3 --test-slice --variant bust_portrait --prompt-variant character_readability --limit 2
python -m orchestrator generate-environment-references princess_of_mars_test --chapters 2-3 --test-slice --variant establishing_wide --prompt-variant environment_readability --limit 2
```

Then execute only after prompts are reviewed:

```bat
python -m orchestrator generate-character-references princess_of_mars_test --chapters 2-3 --test-slice --variant bust_portrait --prompt-variant character_readability --limit 2 --execute
python -m orchestrator generate-environment-references princess_of_mars_test --chapters 2-3 --test-slice --variant establishing_wide --prompt-variant environment_readability --limit 2 --execute
```

For all eligible chapter subjects later, increase the limit or add a future explicit option:

```text
--all-chapter-subjects
```

---

# Verification Checklist

## Visual fallback

- `VISUAL_FALLBACKS.json` exists.
- It contains descriptor-heavy visual context, not just the book title.
- It includes character wardrobe and environment fallback buckets.

## Character prompts

- No raw `unknown` appears in positive prompts.
- Weak costume fields are replaced with project fallback language.
- Modern clothing negatives are present.
- Unresolved identities are flagged and skipped by default.

## Environment prompts

- No generic-only environment descriptor appears when a fallback can be made.
- `arizona_mountain_cave` prompt explicitly includes cave mouth, cliffside rock face, rocky threshold, and shadowed interior.
- Environment drift negatives are present.

## Phase 12/13

- Required missing fields block.
- Recommended missing fields warn.
- Test-slice defaults to two eligible chapter subjects.
- `--limit N` selects up to N eligible chapter subjects.

## Quick-test BATs

- Default chapter range is 2-3.
- Artifact-producing commands pass `--chapters %CHAPTERS%`.
- Prompt-only BATs do not run ComfyUI.
- Image BATs default to limit 2 and can be increased by the user.

---

# Acceptance Criteria

This enhancement is complete when:

1. Book-level visual context is generated from project/book summary and stored in `VISUAL_FALLBACKS.json`.
2. Character descriptor repair fills or falls back weak reference fields before prompt prep.
3. Environment descriptor repair fills or falls back weak reference fields before prompt prep.
4. Prompt prep injects source and subject visual context into character/environment prompt packages.
5. Phase 12/13 treat recommended missing fields as warnings, not blockers.
6. Chapter-aware test-slice selects two useful subjects from selected chapters by default.
7. Quick-test BATs regenerate the two-chapter slice without affecting unrelated chapters, except for intentionally global artifacts such as the global visual fallback.
