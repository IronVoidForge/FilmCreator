Status: 70%

# KupkaProd Lessons and FilmCreator Integration Plan

## Source Reviewed

External reference repo:

```text
https://github.com/Matticusnicholas/KupkaProd-Cinema-Pipeline
```

Reviewed against the public README and repository structure on 2026-04-27, plus FilmCreator's current specs for prompt preparation, reference generation, quality grading, and the later clip pipeline.

## Executive Summary

KupkaProd is strongest at practical end-to-end local production: prompt/script intake, scene planning, storyboard keyframes, review, multiple video takes, and final assembly.

FilmCreator is stronger at long-form canon management: project registries, aliases, bibles, source evidence, locked references, selective reruns, prompt packages, and reviewable file-first artifacts.

The right move is not to copy KupkaProd wholesale. FilmCreator should absorb the production lessons that make downstream image/video generation more reliable while preserving its canon-aware, review-gated, rerunnable architecture.

FilmCreator's generation path is different from KupkaProd's because we expect to use image-to-video for most real shots. That means the most important prompt is often not a standalone text-to-video prompt. The critical artifacts are:

- approved character references
- approved environment references
- approved opening keyframes
- approved previous-shot last frames
- image-to-image alternate-angle keyframes
- I2V prompts that explain motion, continuity, and what must change or remain stable

Even with I2V, rich detail still matters. The model needs explicit subject, environment, style, camera, lighting, action, and continuity constraints so the conditioning image does not become the only source of truth.

## Priority Matrix

Difficulty score uses 1-5:

- 1 = small prompt/spec/code addition
- 2 = contained implementation
- 3 = moderate cross-phase wiring
- 4 = complex lifecycle or workflow integration
- 5 = major system/UX change

| Priority | Lesson | Why It Matters | Difficulty |
|---:|---|---|---:|
| 1 | I2V continuity chain with previous-shot last frame to alternate-angle next keyframe | This is the core future shot-to-shot workflow and affects how scenes can be generated, reviewed, and resumed | 4 |
| 2 | Project-level style lock | Prevents style drift across refs, keyframes, I2V, and video clips | 2 |
| 3 | Self-contained generation prompt packs for I2V/keyframes | Conditioning images help, but final prompts still need full world/detail reconstruction | 3 |
| 4 | Rich descriptor minimums before visual generation | Prevents generic characters/environments and weak keyframes | 3 |
| 5 | Workflow preflight for ComfyUI / local model stack | Prevents expensive runs from failing because nodes, models, paths, or dimensions are wrong | 3 |
| 6 | Structured visual candidate evaluation rubric | Makes approval/rejection reproducible and useful for repairs | 3 |
| 7 | Failure-driven prompt and keyframe repair | Converts rejected candidates into targeted regeneration instead of broad reruns | 4 |
| 8 | Multiple takes / candidates with approval and selected outputs | AI generation is stochastic; final production needs choice, not one-shot acceptance | 3 |
| 9 | Dialogue timing from word count, WPM, and action seconds | Needed for I2V clip duration, audio, and assembly | 3 |
| 10 | Vertical validation lane from refs to keyframe to I2V clip | Proves the stack early before a full-book run | 4 |
| 11 | Local model lifecycle / VRAM hygiene | Prevents LM Studio, ComfyUI, and video models from starving or hanging each other | 3 |
| 12 | Workflow template manifests and node validation | Keeps ComfyUI workflow JSONs controllable and portable | 3 |
| 13 | Resolution and frame-count validation | Avoids invalid dimensions or unsupported frame counts before queueing jobs | 2 |
| 14 | Voice/audio bibles | Useful for later synchronized audio and performance continuity | 3 |
| 15 | GUI review flow | Helpful, but file-first reports can carry us for now | 5 |

---

# 1. I2V Continuity Chain: Previous Last Frame to Alternate-Angle Next Keyframe

## Lesson

KupkaProd emphasizes storyboard keyframes before video generation. FilmCreator should go further for I2V: approved video outputs should feed the next still-generation decision when continuity requires it.

The important FilmCreator workflow is:

```text
approved shot N video
  -> extract / register last approved frame
  -> use last frame as image-to-image source
  -> generate alternate-angle / zoom / camera-position candidates for shot N+1 opener
  -> review and approve one secondary view
  -> use approved secondary view as first frame for shot N+1 I2V
```

This is not the same as asking the video model to continuously follow the prior shot. The image-to-image step deliberately creates a new camera view while preserving identity, wardrobe, setting continuity, and state.

## Why It Matters

Many sequences cannot safely generate all first frames independently. The first shot of a scene or shot sequence may be straightforward from references, but later shots may need the approved previous video last frame before they can create a believable next opener.

This creates a real dependency chain:

```text
shot 1 keyframe -> shot 1 video -> approve last frame -> shot 2 alternate-angle opener -> shot 2 video
```

For action scenes, dialogue coverage, reveal shots, and camera push/pull changes, this may be the difference between coherent continuity and visual drift.

## FilmCreator Integration

Add explicit clip/keyframe strategy values:

```text
fresh_from_refs
soft_scene_reframe
previous_last_frame_reframe
direct_continuous_follow
manual_keyframe_override
```

Default guidance:

- Use `fresh_from_refs` for the first shot in a scene or sequence.
- Use `previous_last_frame_reframe` when shot N+1 must preserve exact state but change camera angle, zoom, or composition.
- Use `direct_continuous_follow` only when the next clip is truly a continuation, not a cut.
- Require human approval before a previous-last-frame-derived opener becomes the next shot's first frame.

## Files / Specs Affected

```text
spec/06_later_clip_pipeline/01_clip_input_contract.md
spec/06_later_clip_pipeline/03_anchor_and_interval_frames.md
spec/06_later_clip_pipeline/04_clip_review_and_selection.md
future orchestrator/shot_keyframes.py
future orchestrator/video_generation.py
future orchestrator/clip_state.py
```

## Acceptance Criteria

- Clip state records `approved_video_last_frame`.
- Clip plans can declare `opening_keyframe_strategy: previous_last_frame_reframe`.
- The runner refuses to generate shot N+1 I2V when its required reframe source is missing or unapproved.
- The alternate-angle opener records source frame, camera change request, seed, prompt variant, and approval status.
- Review can approve the secondary view before the next I2V clip starts.

---

# 2. Project-Level Style Lock

## Lesson

KupkaProd stores a short style anchor and injects it into every scene prompt. FilmCreator needs the same concept, but as a file-first artifact shared by refs, keyframes, and video prompts.

## Artifact

```text
projects/<project>/02_story_analysis/world/global/STYLE_LOCK.json
```

Suggested fields:

```json
{
  "rendering_style": "cinematic illustrated realism",
  "color_palette": "project-specific dominant and accent colors",
  "lighting_style": "readable cinematic lighting",
  "camera_style": "widescreen film coverage with clear subject staging",
  "texture_finish": "consistent material detail",
  "negative_style_rules": ["no modern UI text", "no random style shifts"]
}
```

## Integration

- Include style lock in character reference prompts.
- Include style lock in environment reference prompts.
- Include style lock in shot keyframe and I2V prompts.
- Let prompt boosters add local emphasis, but never replace the style lock.

## Difficulty

2. The main work is artifact creation, prompt-prep injection, and quality validation.

---

# 3. Self-Contained Generation Prompt Packs For I2V And Keyframes

## Lesson

KupkaProd's README stresses that every generation prompt rebuilds the scene because video models have no memory. FilmCreator's I2V prompts are different because they have image conditioning, but they still need full production context.

## FilmCreator Rule

Every final visual generation prompt package must include:

- active character identity and locked visual fields
- active environment descriptor and subzone
- style lock
- camera angle, lens, framing, zoom/motion intent
- lighting and mood
- action start and action end
- continuity from previous shot
- what may change from the source image
- what must remain stable from the source image

Avoid weak phrases:

```text
same as before
same character
same outfit
continue the scene
as previously shown
```

For I2V and image-to-image, those phrases should be replaced by explicit continuity fields.

## Difficulty

3. The data mostly exists; the challenge is final assembly and validation discipline.

---

# 4. Rich Descriptor Minimums

## Lesson

KupkaProd keeps concrete character and setting descriptions close to generation prompts. FilmCreator should enforce minimum visual descriptor fields before expensive generation.

## Character Minimum Fields

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

## Environment Minimum Fields

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

## Integration

- Descriptor enrichment should mark missing fields explicitly.
- Prompt preparation should warn on generic descriptors.
- Quality grading should block or review Phase 12/13 and Phase 14 candidates when visual fields are too thin.

## Difficulty

3. This requires prompt tuning, validation, and grading rules.

---

# 5. Workflow Preflight

## Lesson

KupkaProd tells users to dry-run ComfyUI workflows before production. FilmCreator should make this a first-class preflight instead of an operator memory task.

## FilmCreator Integration

Add a preflight command that validates:

- ComfyUI reachable
- required custom nodes present
- workflow JSON loads
- expected node ids or auto-detected nodes exist
- model files resolve
- input/output folders exist
- image dimensions satisfy workflow multiples
- video frame counts are valid

## Difficulty

3. Straightforward, but it touches Comfy client, workflow metadata, and launchers.

---

# 6. Structured Visual Candidate Evaluation Rubric

## Lesson

KupkaProd evaluates storyboard/keyframe candidates before video generation. FilmCreator should store manual and future AI-assisted evaluation as structured data.

## Candidate Rubric

```text
character_accuracy
environment_accuracy
composition
camera_match
lighting_mood
continuity
image_quality
downstream_usability
```

Values:

```text
good
fair
poor
unknown
```

Hard fail rules:

- `character_accuracy=poor` fails character/shot candidates.
- `environment_accuracy=poor` fails environment/shot candidates.
- `continuity=poor` fails sequence-derived keyframes.
- `image_quality=poor` fails.
- Two or more `fair` fields require review.

## Difficulty

3. Candidate metadata is manageable; reporting and review ergonomics need care.

---

# 7. Failure-Driven Prompt And Keyframe Repair

## Lesson

KupkaProd regenerates rejected storyboard images with notes. FilmCreator should turn rejection reasons into targeted repair variants.

## Repair Flow

```text
candidate rejected
  -> rejection tags and notes
  -> repair note synthesis
  -> repaired prompt variant
  -> regenerate candidate
  -> preserve original canonical prompt package
```

Example mappings:

| Review Tag | Repair Action |
|---|---|
| `too_dark` | add explicit readable lighting and underexposure negatives |
| `weak_face` | move face descriptor earlier and add face readability booster |
| `wrong_costume` | repeat locked costume fields verbatim |
| `bad_environment_layout` | simplify foreground / midground / background layout |
| `identity_drift` | require approved character reference image and identity anchors |
| `bad_reframe` | narrow image-to-image change request to angle/zoom only |

## Difficulty

4. The metadata is easy; the lifecycle and variant tracking are the hard part.

---

# 8. Multiple Takes And Candidates

## Lesson

KupkaProd generates multiple takes and lets the user choose. FilmCreator should treat reference images, keyframes, alternate-angle openers, and videos as candidate families.

## Integration

Support:

```bash
--takes 3
--seed-mode random
--stop-on-approved
--prompt-variant readability
```

Candidate metadata should include:

```text
take_number
seed
workflow_id
prompt_variant
booster_ids
source_frame_id
approval_status
selected_for_downstream
```

## Difficulty

3. We already have reference candidate lifecycle patterns.

---

# 9. Dialogue Timing And WPM Estimation

## Lesson

KupkaProd calculates scene duration from dialogue word count plus action time. FilmCreator needs this for I2V clip duration, audio, and final assembly.

## Suggested Fields

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

## Difficulty

3. Word counting is simple; aligning dialogue to shots and motion segments is the real work.

---

# 10. Vertical Validation Lane

## Lesson

KupkaProd proves the stack quickly by going from planning to storyboard to video. FilmCreator should add a small validation lane before full-book production.

## FilmCreator Lane

```text
approved character ref
approved environment ref
one shot package
one opening keyframe
one I2V clip
manual review
optional previous-last-frame reframe into next opener
```

## Difficulty

4. Requires Phase 14/16 wiring and real workflow validation.

---

# 11. Local Model Lifecycle And VRAM Hygiene

## Lesson

KupkaProd unloads/restarts local models to prevent hangs and free VRAM before ComfyUI work. FilmCreator should have explicit rules for LM Studio, ComfyUI, and video models.

## Integration

- Detect active local model servers.
- Avoid launching heavy generation while LM Studio is still processing synthesis.
- Add operator-visible preflight warnings.
- Record model/process state in run manifests.

## Difficulty

3.

---

# 12. Workflow Template Manifests

## Lesson

KupkaProd ships workflow templates and can export API-format templates from ComfyUI. FilmCreator should treat workflow JSON as versioned artifacts with manifests.

## Integration

Each workflow should have:

```text
workflow_id
workflow_json_path
expected_node_roles
model_requirements
dimension_requirements
known_good_test_output
last_preflight_status
```

## Difficulty

3.

---

# 13. Resolution And Frame Validation

## Lesson

KupkaProd snaps dimensions to workflow-valid multiples. FilmCreator should reject invalid dimensions before queueing.

## Integration

- Validate image dimensions by workflow requirements.
- Validate video dimensions by workflow requirements.
- Validate frame count and FPS.
- Store resolved dimensions in candidate metadata.

## Difficulty

2.

---

# 14. Voice And Audio Bibles

## Lesson

KupkaProd stores voice-style descriptions and uses synchronized audio/video workflows. FilmCreator can defer this until audio phases, but should keep the schema in mind.

## Suggested Artifact

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

## Difficulty

3.

---

# 15. GUI Review Flow

## Lesson

KupkaProd has storyboard and take review GUIs. FilmCreator should eventually have a visual review UI, but the near-term requirement is better JSON/Markdown review reports and stable candidate folders.

## Difficulty

5 for full GUI, 2 for better reports.

---

# What Not To Copy

Do not copy KupkaProd wholesale.

Avoid importing these architectural choices directly:

- GUI-first orchestration
- run-local state as the main source of truth
- fully autonomous accept/reject behavior
- prompt generation that bypasses canonical bibles and registries
- first-pass `PASS` as final production acceptance
- public-figure-specific voice shortcuts
- text-to-video assumptions as the default for FilmCreator

FilmCreator should stay:

```text
file-first
review-gated
canon-aware
rerunnable
reference-locked
prompt-package-driven
I2V-aware
```

---

# Recommended Roadmap

## Immediate After Current Oz Validation

1. Add project-level `STYLE_LOCK.json`.
2. Add descriptor minimum validation before Phase 12/13 generation.
3. Add world-reconstruction checks to final visual prompt packages.
4. Update clip specs and future Phase 14 docs around `previous_last_frame_reframe`.
5. Add workflow preflight planning for ComfyUI/local model readiness.

## Near-Term Reference / Keyframe Work

1. Add structured candidate rubric.
2. Add selected/approved candidate metadata.
3. Add rejection tags and repair variants.
4. Add alternate-angle opener candidates sourced from approved previous video last frames.

## Phase 14/16 Validation

1. Generate one approved first-shot keyframe from refs.
2. Generate one I2V clip.
3. Approve clip and register last frame.
4. Generate next-shot opener via image-to-image reframe.
5. Approve that secondary view.
6. Use it as first frame for the next I2V clip.

## Later

1. Add dialogue timing and WPM estimates.
2. Add video take lifecycle.
3. Add voice bibles.
4. Add lightweight visual review UI.

---

# Acceptance Criteria For Adoption

FilmCreator has incorporated these lessons when:

- Style lock appears in every visual generation package.
- Final generation packages are self-contained and I2V-aware.
- Descriptor minimums prevent generic references and keyframes.
- Candidate review captures why outputs pass or fail.
- Rejected candidates produce targeted repair variants.
- Multiple takes can be compared by seed, workflow, source frame, and prompt variant.
- A previous shot's approved last frame can produce an approved alternate-angle opener for the next shot.
- The runner can block a dependent next shot until its opener is approved.
- Workflow preflight catches missing nodes/models/dimension errors before expensive runs.
