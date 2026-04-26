# Deferred: KupkaProd Cinema Pipeline Lessons and FilmCreator Integration Plan

## Source Reviewed

External reference repo:

```text
https://github.com/Matticusnicholas/KupkaProd-Cinema-Pipeline
```

This document captures what FilmCreator can learn from KupkaProd, what we should not copy, and how each lesson maps into our file-first phased pipeline.

## Executive Summary

KupkaProd is strongest at getting from a prompt/script to a complete local video quickly. Its pipeline emphasizes self-contained scene prompts, style locks, keyframe review, video takes, prompt rewriting after failures, and final assembly.

FilmCreator is stronger at long-form canon management: registries, aliases, bibles, prompt packages, reference approval/locking, selective reruns, and reusable assets.

The best path is not to copy KupkaProd architecture wholesale. Instead, pull in targeted lessons that improve prompt quality and downstream video validation while preserving FilmCreator's staged file-first design.

## High-Value Lessons

| Lesson | Value to FilmCreator | Integration Difficulty | Priority |
|---|---:|---:|---:|
| Full world reconstruction in every generation prompt | Very high | Medium | Immediate |
| Project-level style lock | Very high | Low-Medium | Immediate |
| Rich character/environment descriptor minimums | Very high | Medium | Immediate |
| Strict visual candidate evaluation rubric | High | Medium | Near-term |
| Failure-driven prompt repair | High | Medium-High | Near-term |
| Dialogue timing from word count/WPM | Medium-High | Medium | Near-term |
| Multiple takes per shot/scene | Medium-High | Medium | Phase 14/16 |
| Keyframe-to-video vertical validation lane | High | Medium-High | Phase 14 |
| GUI-style review flow | Medium | High | Later |
| Voice/audio bibles | Medium | Medium | Phase 15 |

---

# 1. Full World Reconstruction

## Lesson

KupkaProd assumes the model has no memory between scenes. Every prompt fully rebuilds the character, setting, lighting, camera, action, sound, and style from scratch.

## Why It Matters

FilmCreator already stores all the parts, but final generation prompts can still become too abstract if they rely on IDs, summaries, or previous context.

Scene/keyframe/video prompts must never depend on phrases like:

```text
same character
same outfit
same location
continues from previous scene
as before
```

## FilmCreator Integration

Add a rule to Phase 14 prompt assembly:

```text
Every final generation prompt must be self-contained and include all active character, environment, style, camera, lighting, action, and continuity details.
```

## Files / Modules Likely Affected

```text
spec/phases/PHASE_14_SHOT_KEYFRAME_GENERATION.md
orchestrator/prompt_preparation.py
future orchestrator/shot_keyframes.py
```

## Implementation Steps

1. Add a `world_reconstruction_required` flag to scene/shot prompt packages.
2. In final keyframe generation prompt assembly, expand IDs into full text summaries.
3. Include approved reference IDs and short reference descriptors.
4. Add validation that rejects prompts containing weak continuity phrases like `same as before`.

## Difficulty

Medium. The data exists, but final prompt assembly needs discipline and validation.

---

# 2. Project-Level Style Lock

## Lesson

KupkaProd creates a short style anchor and injects it into every scene prompt.

## Why It Matters

FilmCreator needs consistent visual direction across character refs, environment refs, keyframes, and video. Without a style lock, each phase may drift.

## FilmCreator Integration

Create a file-first style lock artifact:

```text
projects/<project>/02_story_analysis/world/global/STYLE_LOCK.json
```

Suggested fields:

```json
{
  "rendering_style": "photoreal cinematic adventure illustration",
  "color_palette": "warm ochres, dusty reds, muted golds, deep blue shadows",
  "lighting_style": "naturalistic cinematic lighting with readable faces",
  "camera_style": "classic widescreen adventure framing",
  "texture_finish": "film-quality detail, not painterly unless requested",
  "negative_style_rules": ["no modern UI text", "no inconsistent cartoon style"]
}
```

## Files / Modules Likely Affected

```text
orchestrator/prompt_preparation.py
orchestrator/descriptor_enrichment.py
orchestrator/quality_grading.py
spec/IMPLEMENTATION_ROADMAP.md
```

## Implementation Steps

1. Add a style lock synthesis step or simple default generator.
2. Store style lock in global story analysis.
3. Include style lock in character/environment/scene prompt packages.
4. Let prompt booster variants append to style, but never replace it.

## Difficulty

Low-Medium. This is mostly artifact creation and prompt-prep inclusion.

---

# 3. Rich Descriptor Minimums

## Lesson

KupkaProd requires concrete descriptor fields for characters and settings. Characters include face, hair, build, clothing, mannerisms. Settings include room/location, props, surfaces, background, lighting, and atmosphere.

## Why It Matters

FilmCreator's first generated refs exposed the weakness of generic descriptors like:

```text
described character with stable costume and silhouette
```

Prompt packages need enough visible detail to generate consistent assets.

## FilmCreator Integration

Strengthen descriptor enrichment and prompt-prep validation.

### Character Minimum Fields

```text
age_or_life_stage
species_or_body_type
build_and_height
face_structure
skin_or_surface_detail
hair_or_head_detail
eyes_or_gaze
costume_layers
accessories
posture_or_mannerism
silhouette_anchors
locked_visual_fields
```

### Environment Minimum Fields

```text
location_type
layout
foreground_midground_background
scale
landmarks
materials
props_or_set_dressing
lighting
atmosphere
camera_readability_notes
locked_visual_fields
```

## Files / Modules Likely Affected

```text
orchestrator/descriptor_enrichment.py
orchestrator/prompt_preparation.py
orchestrator/quality_grading.py
spec/phases/PHASE_11_DESCRIPTOR_ENRICHMENT.md
```

## Implementation Steps

1. Update descriptor enrichment prompts to require minimum fields.
2. Add prompt-prep warnings when required visual fields are blank or generic.
3. Add quality grading rule for weak descriptors.
4. Block or review Phase 12/13 generation if visual descriptors are too thin.

## Difficulty

Medium. Requires prompt tuning and validation rules, but not major architecture changes.

---

# 4. Strict Visual Candidate Evaluation Rubric

## Lesson

KupkaProd evaluates keyframes with explicit categories and hard fail rules.

## Why It Matters

FilmCreator needs consistent manual and future AI-assisted candidate review. The ranking system should not be just `good/bad`; it should store why.

## FilmCreator Integration

Extend reference candidate metadata with a structured review rubric.

Suggested categories:

```text
character_accuracy
environment_accuracy
composition
lighting_mood
image_quality
continuity
downstream_usability
```

Suggested values:

```text
good
fair
poor
unknown
```

Suggested fail rules:

```text
character_accuracy poor = fail for character/scene refs
environment_accuracy poor = fail for environment/scene refs
image_quality poor = fail
any hard continuity mismatch = fail
two or more fair scores = review-needed or fail
```

## Files / Modules Likely Affected

```text
orchestrator/reference_assets.py
orchestrator/character_references.py
orchestrator/environment_references.py
spec/deferred/REFERENCE_CANDIDATE_RANKING_AND_PROMPT_VARIATION.md
```

## Implementation Steps

1. Add optional `review_rubric` object to candidate records.
2. Add CLI/manual fields for score and tags.
3. Add markdown review index displaying rubric fields.
4. Later add AI/vision evaluator that populates a first-pass rubric.

## Difficulty

Medium. Candidate metadata changes are straightforward, but UX/reporting needs care.

---

# 5. Failure-Driven Prompt Repair

## Lesson

KupkaProd collects keyframe failure reasons and rewrites prompts based on those failures.

## Why It Matters

FilmCreator already has repair notes in prompt packages. We should turn rejection data into structured repair notes and prompt variants.

## FilmCreator Integration

Add a repair loop:

```text
candidate rejected
  -> rejection tags + notes
  -> repair note synthesis
  -> repaired generation prompt variant
  -> regenerate candidate
```

Example mapping:

| Review Tag | Repair Action |
|---|---|
| `too_dark` | Add explicit even lighting and negative underexposure terms |
| `weak_face` | Move face descriptor earlier and add face readability booster |
| `wrong_costume` | Repeat costume fields verbatim and add costume readability booster |
| `bad_environment_layout` | Simplify spatial layout and foreground/midground/background |
| `identity_drift` | Require locked reference image and reinforce identity anchors |

## Files / Modules Likely Affected

```text
orchestrator/prompt_boosters.py
orchestrator/reference_assets.py
orchestrator/character_references.py
orchestrator/environment_references.py
future orchestrator/prompt_repair.py
```

## Implementation Steps

1. Store rejection tags and fail reasons.
2. Add `repair_prompt_variant` generation using the original prompt plus failure notes.
3. Save repaired prompt as a temporary generation prompt, not as the canonical prepared prompt.
4. Track repaired variants in candidate metadata.

## Difficulty

Medium-High. The core is manageable, but we need robust metadata and review discipline.

---

# 6. Dialogue Timing and WPM Estimation

## Lesson

KupkaProd calculates scene duration from dialogue word count, WPM, and action seconds.

## Why It Matters

FilmCreator will need reliable shot durations for image-to-video, audio, and final edit planning.

## FilmCreator Integration

Add timing fields to dialogue timeline, scene contracts, and shot packages.

Suggested fields:

```json
{
  "dialogue_word_count": 42,
  "speaker_wpm": 140,
  "estimated_dialogue_seconds": 18,
  "action_seconds": 4,
  "target_clip_seconds": 22,
  "duration_confidence": "estimated"
}
```

## Files / Modules Likely Affected

```text
orchestrator/dialogue_timeline.py
orchestrator/shot_planner.py
orchestrator/scene_contracts.py
spec/phases/PHASE_15_AUDIO.md
spec/phases/PHASE_16_VIDEO.md
```

## Implementation Steps

1. Add a WPM utility module.
2. Count words in dialogue timeline lines.
3. Estimate clip duration per shot and scene.
4. Use duration targets when generating video clips.

## Difficulty

Medium. Word counting is simple; aligning timing with shot structure is the real work.

---

# 7. Multiple Takes Per Shot / Scene

## Lesson

KupkaProd generates multiple video takes and lets the user pick the best.

## Why It Matters

AI generation is stochastic. One output is rarely enough. FilmCreator's ranking system should apply not only to reference images but also to keyframes and video clips.

## FilmCreator Integration

For Phase 14 and Phase 16, support:

```bash
--takes 3
--seed-mode random
--stop-on-approved
--prompt-variant readability
```

## Files / Modules Likely Affected

```text
future orchestrator/shot_keyframes.py
future orchestrator/video_generation.py
orchestrator/reference_assets.py
orchestrator/prompt_boosters.py
```

## Implementation Steps

1. Treat keyframes/video clips as candidates, like reference assets.
2. Store take number, seed, workflow ID, prompt variant, booster IDs.
3. Add approval/lock behavior for selected keyframes/clips.
4. Add final assembly inputs that use selected clips only.

## Difficulty

Medium. We already have candidate lifecycle patterns from references.

---

# 8. Keyframe-to-Video Vertical Validation Lane

## Lesson

KupkaProd has a short path from storyboard keyframe to video generation.

## Why It Matters

FilmCreator needs to validate the whole stack early, even before perfect art direction.

## FilmCreator Integration

Add a small validation path:

```text
approved character ref
approved environment ref
one shot package
one keyframe
one image-to-video clip
manual review
```

## Files / Modules Likely Affected

```text
future orchestrator/shot_keyframes.py
future orchestrator/video_generation.py
launchers/quick_pipeline_test/
spec/CLI_PIPELINE_ORCHESTRATOR_SPEC.md
```

## Implementation Steps

1. Add `generate-shot-keyframes --validation-slice`.
2. Use approved refs and one shot package.
3. Generate 1-3 keyframe candidates.
4. Approve one keyframe.
5. Run I2V test using that keyframe.

## Difficulty

Medium-High. Requires Phase 14 wiring and workflow validation.

---

# 9. Voice and Audio Bibles

## Lesson

KupkaProd stores voice descriptions with pitch, timbre, accent, cadence, delivery, and verbal tics.

## Why It Matters

FilmCreator's dialogue timeline will eventually need audio generation or voice direction.

## FilmCreator Integration

Add voice bibles as Phase 15 prep.

Suggested artifact:

```text
projects/<project>/02_story_analysis/bibles/voices/VOICE_<character_id>.json
```

Fields:

```text
pitch
timbre
accent_or_dialect
cadence
speaking_pace_wpm
delivery_style
verbal_tics
emotional_range
continuity_notes
```

## Files / Modules Likely Affected

```text
orchestrator/dialogue_timeline.py
future orchestrator/audio.py
spec/phases/PHASE_15_AUDIO.md
```

## Implementation Steps

1. Add deferred spec for voice bibles.
2. Extract voice hints from dialogue and narration.
3. Link voice bibles to character IDs.
4. Use voice bibles in audio/video prompts later.

## Difficulty

Medium. Not urgent until audio/video phase.

---

# 10. GUI Review Flow

## Lesson

KupkaProd includes storyboard and take review GUIs.

## Why It Matters

FilmCreator's file-first review is powerful but slower for visual selection. A simple review UI would help when ranking hundreds of generations.

## FilmCreator Integration

Defer full GUI. First, improve markdown/JSON review reports. Later, build a lightweight local review viewer.

## Files / Modules Likely Affected

```text
orchestrator/reference_assets.py
future review_ui/
```

## Difficulty

High for GUI, low for better reports.

---

# What Not To Copy

Do not copy KupkaProd wholesale.

Avoid importing these architectural choices directly:

- GUI-first orchestration
- run-local state as the main source of truth
- fully autonomous accept/reject behavior
- public-figure-specific voice anchors
- prompt generation that bypasses canonical bibles and registries
- first-pass `PASS` as final production acceptance

FilmCreator should stay:

```text
file-first
review-gated
canon-aware
rerunnable
reference-locked
prompt-package-driven
```

---

# Recommended Implementation Roadmap

## Immediate: Prompt and Descriptor Quality

1. Add style lock artifact.
2. Update descriptor enrichment minimum fields.
3. Add world reconstruction rules to prompt-prep and Phase 14 docs.
4. Keep booster libraries generic and generation-time only.

## Near-Term: Review and Repair

1. Add structured visual candidate rubric.
2. Add manual ranking fields to candidates.
3. Add rejection tags and repair note synthesis.
4. Add prompt repair variants.

## Phase 14 Validation

1. Generate one shot keyframe using approved character/environment refs.
2. Generate multiple keyframe takes with raw/boosted variants.
3. Approve one keyframe.
4. Run one I2V clip.

## Phase 15/16

1. Add dialogue timing estimates.
2. Add voice bibles.
3. Add video take lifecycle.
4. Add final assembly candidate selection.

---

# Proposed New Deferred Specs

Create or update:

```text
spec/deferred/STYLE_LOCK_AND_WORLD_RECONSTRUCTION.md
spec/deferred/VISUAL_CANDIDATE_EVALUATION_RUBRIC.md
spec/deferred/FAILURE_DRIVEN_PROMPT_REPAIR.md
spec/deferred/DIALOGUE_TIMING_AND_TAKE_PLANNING.md
spec/deferred/VOICE_BIBLES_AND_AUDIO_IDENTITY.md
```

---

# Acceptance Criteria For Adoption

FilmCreator successfully incorporates these lessons when:

- Base prompt packages remain canonical and clean.
- Generation prompts are fully self-contained.
- Style lock appears in every visual generation prompt.
- Character/environment descriptors are specific enough to avoid generic outputs.
- Candidate review captures why an output succeeded or failed.
- Rejected candidates become useful prompt repair data.
- Multiple takes can be compared by prompt variant, seed, workflow, and rank.
- A small vertical slice can go from approved refs to keyframe to I2V clip.

