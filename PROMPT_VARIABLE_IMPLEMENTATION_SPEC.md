# Prompt Variable Implementation Spec

This document turns the prompt-package reference ideas into an implementation plan:

- what variables to add
- which pipeline stage should create them
- which data should be derived deterministically
- what prompts to feed the LLM
- where the added data comes from

This is aimed at the current downstream pipeline for:
- characters
- environments
- scenes
- shots
- prompt preparation
- later image-to-video prompt generation

## Core Design Decision

Do **not** ask the LLM to write the final prompt package prose as one freeform paragraph.

Instead:

1. produce structured visual variables
2. validate them
3. render deterministic prompt templates from them
4. only optionally polish the final text if needed

That means most of the new work belongs in:
- scene contracts
- shot planner
- prompt preparation

not in a final “write the whole prompt” LLM pass.

## Implementation Principles

### 1. Prompt-ready fragments, not summaries

New variables should be:
- short
- visual
- concrete
- one idea per field
- free of markdown
- free of names in model-facing strings
- reusable in template rendering

Good:
- `foreground right at base of dais`
- `visibly smaller than escort and ruler`
- `upright but tense after forced presentation`

Bad:
- `Primary subject placement should remain readable`
- `Continue the established scene action`
- `This emphasizes hierarchy and emotional tension`

### 2. Ask the LLM only for what must be inferred

Do **not** use the LLM for:
- enum defaults that can be mapped from shot type
- field normalization
- visible-vs-offscreen narrator rules
- image mapping order
- template assembly

Do use the LLM for:
- shot-specific action moment
- subject relation
- pose and body language
- frame position
- required environmental proof detail
- motion continuation intent

### 3. Separate still-image prompts from image-to-video prompts

Still-image keyframe prompts and one-image image-to-video prompts are different products.

Still-image keyframe prompts need:
- multi-image reference mapping
- exact frame composition

Image-to-video prompts need:
- movement continuation from one frame
- camera movement and end-state guidance

These should be separate prompt package types.

## Stage-by-Stage Ownership

### Character Layer

Producer:
- descriptor enrichment

Consumer:
- prompt preparation

Purpose:
- provide stable portrait-ready variables

### Environment Layer

Producer:
- descriptor enrichment

Consumer:
- prompt preparation

Purpose:
- provide stable environment-reference variables

### Scene Layer

Producer:
- scene contracts

Consumer:
- shot planner
- later prompt preparation

Purpose:
- produce scene-level visual intent and shot seed context

### Shot Layer

Producer:
- shot planner

Consumer:
- prompt preparation
- later image-to-video prompt generation

Purpose:
- produce exact prompt-ready visual/action variables

### Prompt Package Layer

Producer:
- prompt preparation

Purpose:
- deterministic template rendering from upstream variables

## Variables To Add

## 1. Character Variables

These should be produced mostly from character descriptors.

### Add / normalize to character descriptor output

- `character_short_description`
  - Example: `rugged adult human frontier soldier`
- `character_size_description`
  - Example: `tall human-scale figure`
- `character_build_description`
  - Example: `lean battle-tested build`
- `character_skin_description`
  - Example: `sun-weathered human skin`
- `character_face_description`
  - Example: `weathered angular face`
- `character_hair_description`
  - Example: `dark practical short hair`
- `character_eye_description`
  - Example: `dark steady eyes`
- `character_facial_hair_description`
  - Example: `clean-shaven or short field stubble`
- `character_posture_description`
  - Example: `upright but controlled posture`
- `character_expression_description`
  - Example: `restrained alert expression`
- `character_costume_description`
  - Example: `worn frontier cavalry clothing with leather gear`
- `character_silhouette_description`
  - Example: `simple survival-ready silhouette`
- `character_reference_lighting_default`
  - Example: `even readable lighting`
- `character_view_angle_default`
  - Example: `front_three_quarter_left`

### Source of truth

Comes from:
- descriptor fields already present:
  - `identity_baseline`
  - `height`
  - `build`
  - `skin_tone`
  - `face_shape`
  - `hair_color`
  - `hair_style`
  - `eye_color`
  - `facial_hair`
  - `posture`
  - `expression_tendency`
  - `costume_signature`
  - `costume_layers`
  - `silhouette_notes`

### Implementation note

Most of these do **not** require a new LLM call if the descriptor is already decent.
They can be assembled by deterministic normalization helpers.

## 2. Environment Variables

These should be produced mostly from environment descriptors.

### Add / normalize to environment descriptor output

- `environment_short_description`
  - Example: `ancient Martian grand audience chamber`
- `environment_layout_description`
  - Example: `cavernous ceremonial hall with raised central dais`
- `environment_scale_description`
  - Example: `monumental interior scale`
- `environment_architecture_description`
  - Example: `white marble architecture with galleries and vaulted ceiling`
- `environment_materials_description`
  - Example: `polished marble, gold inlay, carved wood furnishings`
- `environment_lighting_description`
  - Example: `ceremonial high-contrast interior lighting`
- `environment_mood_description`
  - Example: `formal power and ancient weight`
- `environment_depth_description`
  - Example: `clear layered foreground, midground, and deep background architecture`
- `environment_anchor_1`
  - Example: `raised marble dais`
- `environment_anchor_2`
  - Example: `human-scale carved desk`
- `environment_anchor_3`
  - Example: `gallery-lined upper walls`

### Source of truth

Comes from:
- environment descriptors:
  - `layout`
  - `scale`
  - `architecture`
  - `materials`
  - `lighting`
  - `mood`
  - `camera_friendly_landmarks`
  - `depth_cues`

### Implementation note

These also should mostly be deterministic normalizations.
The biggest quality risk here is wrong generated inference like interior scenes inheriting exterior geography.
So environment descriptor validation needs to strip incompatible generic fields before prompt prep.

## 3. Scene Variables

These belong in scene contracts.

The scene should stop being only a narrative summary and become the visual seed layer for prompts.

### Add to scene contract

- `scene_short_description`
  - One short visual description
  - Example: `a human captive is presented before a giant green Martian ruler in an ancient ceremonial hall`
- `scene_emotional_read`
  - Example: `intimidation shifting into analytical curiosity`
- `scene_primary_scale_story_point`
  - Example: `human-scale furniture looks absurdly small beside giant Martians`
- `scene_environment_subzone_catalog`
  - Example:
    - `base_of_dais`
    - `lower_chamber_floor`
    - `threshold`
    - `gallery_edge`
- `scene_required_anchor_catalog`
  - Example:
    - `raised dais`
    - `human-scale carved desk`
    - `gallery wall`
- `scene_visible_subject_rules`
  - Example:
    - `narrator voiceover may be present but not visible unless resolved to a body`
- `scene_reference_image_plan`
  - Example:
    - `image1 = primary visible human`
    - `image2 = secondary visible character`
    - `image3 = environment`
    - `image4 = optional tertiary authority or creature`
- `scene_default_camera_package`
  - Example: `medium-wide, eye-level to slight low-angle, normal lens, deep focus`

### For each planned shot seed

Add:
- `planned_shot_role`
  - Example: `arrival_hierarchy_reveal`
- `planned_shot_moment_summary`
  - Example: `the captive halts before the dais and realizes the scale mismatch`
- `planned_shot_visible_primary_subject`
- `planned_shot_visible_secondary_subjects`
- `planned_shot_required_anchor_1`
- `planned_shot_required_anchor_2`
- `planned_shot_scale_proof_detail`
- `planned_shot_emotional_read`

### Source of truth

Comes from:
- book chapter text
- chapter summary
- scene breakdown
- resolved characters
- resolved environments
- scene intent

### What should be deterministic

Can derive without LLM:
- default image order plan
- narrator visibility rule
- default camera package by scene type

Needs LLM:
- concise visual scene description
- scale story point
- planned shot moment summaries
- anchor selection per shot

## 4. Shot Variables

This is the most important layer.

The shot planner should output prompt-ready variables instead of summary-like prose.

### Add to shot package

- `shot_moment_summary`
  - short visible frame description
- `shot_story_purpose`
  - short function
- `shot_emotional_read`
  - short emotional read
- `visible_primary_subject_id`
- `visible_secondary_subject_ids`
- `voiceover_subject_id`
- `primary_subject_role`
- `secondary_subject_roles`
- `primary_subject_frame_position`
  - Example: `foreground right at base of dais`
- `secondary_subject_frame_positions`
  - Example:
    - `midground left half a pace behind primary subject`
    - `background center on raised rostrum`
- `primary_subject_scale_relation`
  - Example: `visibly smaller than escort and ruler`
- `secondary_subject_scale_relations`
- `primary_subject_facing_direction`
  - Example: `front_three_quarter_left toward the dais`
- `secondary_subject_facing_directions`
- `primary_subject_pose_description`
  - Example: `upright but tense after forced presentation`
- `secondary_subject_pose_descriptions`
- `primary_subject_expression_description`
  - Example: `controlled wary concentration`
- `secondary_subject_expression_descriptions`
- `subject_relation_summary`
  - Example: `escort stands behind the captive while the ruler dominates from above`
- `environment_subzone_description`
  - Example: `lower chamber floor below the central dais`
- `required_environment_anchor_1`
  - Example: `human-scale carved desk near the captive`
- `required_environment_anchor_2`
  - Example: `raised marble dais behind the ruler`
- `required_scale_proof_detail`
  - Example: `giant Martian beside chair that is too small for him`
- `camera_package_description`
  - Example: `medium-wide, eye-level with slight low-angle feel, normal lens, locked-off camera, deep focus, ceremonial lighting`
- `continuity_note`
  - Example: `preserve the captive's position below the dais from the previous shot`

### Keep existing enum fields

Already added:
- `shot_size`
- `camera_angle`
- `lens_family`
- `camera_motion`
- `zoom_behavior`
- `focus_strategy`
- `lighting_style`
- `subject_visibility`
- `narration_mode`
- `primary_subject_angle`

### Source of truth

Comes from:
- scene contract
- scene planned shots
- scene bindings
- previous shot end state
- character descriptors
- environment descriptors

### What should be deterministic

Can derive:
- `camera_package_description` from enum values
- `voiceover_subject_id` and `subject_visibility` rules
- image mapping order

Needs LLM:
- frame position
- scale relation
- facing direction
- pose
- expression
- subject relation
- required anchor selection
- scale proof detail

## 5. Video Prompt Variables

These should be added later, likely in a separate motion planning layer or in shot planner if we want to seed them early.

### Add

- `video_motion_summary`
- `primary_subject_motion_description`
- `secondary_subject_motion_descriptions`
- `environment_motion_constraints`
- `camera_motion_description`
- `motion_style_description`
- `continuity_behavior_description`
- `ending_pose_description`

### Source of truth

Comes from:
- shot start state
- shot end state
- action during shot
- continuity handoff

### Implementation note

These should not be requested until the still-image keyframe variables are working well.

## Prompts To Feed The LLM

## A. Scene Contract Prompt Additions

Goal:
- produce prompt-ready visual scene variables
- produce shot seed variables

### Add to scene prompt instructions

Tell the LLM:

1. Return short visual fragments, not summaries.
2. Do not use markdown in fragment fields.
3. Do not use proper names in prompt-ready fragment fields.
4. Each fragment should describe one visible fact.
5. Prefer 4 to 12 words for individual fragment fields.

### New scene prompt sections

Add sections like:

```text
[[SECTION scene_prompt_variables]]
scene_short_description: <one short visual line>
scene_emotional_read: <short emotional line>
scene_primary_scale_story_point: <short visible scale fact>
scene_environment_subzone_catalog:
- <subzone 1>
- <subzone 2>
- <subzone 3>
scene_required_anchor_catalog:
- <anchor 1>
- <anchor 2>
- <anchor 3>
scene_reference_image_plan:
- image1 = <type of primary visible subject>
- image2 = <type of secondary visible subject>
- image3 = <environment>
- image4 = <optional third subject or creature>
scene_default_camera_package: <short camera package>
```

And per planned shot:

```text
[[SECTION planned_shot_prompt_variables]]
planned_shot_id: SH001
planned_shot_role: <short role>
planned_shot_moment_summary: <short visible frame summary>
planned_shot_visible_primary_subject: <subject type>
planned_shot_visible_secondary_subjects:
- <subject type>
planned_shot_required_anchor_1: <anchor>
planned_shot_required_anchor_2: <anchor>
planned_shot_scale_proof_detail: <short visible scale proof>
planned_shot_emotional_read: <short emotional read>
```

### Where scene prompt data comes from

Inputs:
- chapter summary
- scene breakdown
- character resolutions
- environment resolutions
- nearby book index hits

## B. Shot Planner Prompt Additions

Goal:
- produce prompt-ready frame variables

### Add to shot planner prompt instructions

Tell the LLM:

1. You are not writing a scene summary.
2. You are writing prompt-ready visual variables for a single frame.
3. Return short physical clauses only.
4. No names in prompt-ready fields.
5. No markdown in fragment fields.
6. No abstract phrases like “readable”, “cinematic”, or “continue the action” unless tied to a visible fact.

### New shot prompt sections

```text
[[SECTION shot_prompt_variables]]
shot_moment_summary: <short visible frame summary>
shot_story_purpose: <short purpose>
shot_emotional_read: <short emotional read>
visible_primary_subject_id: <canonical id or role token>
visible_secondary_subject_ids:
- <id>
voiceover_subject_id: <id or none>
primary_subject_role: <short role>
secondary_subject_roles:
- <role>
primary_subject_frame_position: <short frame placement>
secondary_subject_frame_positions:
- <short frame placement>
primary_subject_scale_relation: <short scale relation>
secondary_subject_scale_relations:
- <short scale relation>
primary_subject_facing_direction: <short facing direction>
secondary_subject_facing_directions:
- <short facing direction>
primary_subject_pose_description: <short pose>
secondary_subject_pose_descriptions:
- <short pose>
primary_subject_expression_description: <short expression>
secondary_subject_expression_descriptions:
- <short expression>
subject_relation_summary: <short relation>
environment_subzone_description: <short subzone description>
required_environment_anchor_1: <anchor>
required_environment_anchor_2: <anchor>
required_scale_proof_detail: <visible scale proof>
continuity_note: <short continuity note>
```

### Where shot prompt data comes from

Inputs:
- scene contract
- planned shot seed
- scene binding
- shot blueprint
- previous shot end-state summary
- character descriptors
- environment descriptors

## C. Descriptor Enrichment Prompt Additions

This should be lighter.

Main goal:
- ensure descriptors contain prompt-ready short clauses that can be reused directly

### Character descriptor additions

Ask for:
- short physical phrases
- one clause per field
- no abstract commentary

### Environment descriptor additions

Ask for:
- short layout phrase
- short lighting phrase
- short mood phrase
- 3 clear anchor phrases

## Deterministic Derivations

These should be code, not LLM:

### In prompt preparation

Derive:
- `camera_package_description` from enum fields
- image mapping order:
  - `image1 = visible primary subject`
  - `image2 = first visible secondary subject`
  - `image3 = environment`
  - `image4 = optional third subject or creature`
- narrator visibility handling
- final prompt rendering templates

### In shot planner

Derive:
- default enum values if missing
- narrator offscreen restrictions
- continuity inheritance from previous shot

## Prompt Prep Output Types

Prompt prep should eventually produce distinct prompt package types.

## 1. Character Reference Prompt

Template rendered from character variables.

## 2. Environment Reference Prompt

Template rendered from environment variables.

## 3. Scene Assembly Edit Prompt

Template rendered from:
- image mapping
- visible subjects
- frame positions
- relations
- environment anchors
- camera package

## 4. Shot Keyframe Edit Prompt

Template rendered from:
- image mapping
- exact shot moment
- subject positions
- subject relations
- visible anchors
- continuity note
- camera package

## 5. Shot-to-Video Motion Prompt

Template rendered from:
- input frame lock
- movement summary
- camera movement
- end pose
- continuity note

## Validation Requirements

These should be deterministic checks.

## Scene validation

Fail or review if:
- `scene_short_description` is empty
- `scene_primary_scale_story_point` is generic or placeholder
- required anchors are placeholders
- planned shot moment summaries are just repeated scene summary text

## Shot validation

Fail or review if:
- frame position fields are missing
- facing direction fields are missing
- pose fields are missing
- relation field is missing
- required anchor fields are missing
- scale proof detail is missing
- narrator is visible when it should be off-screen
- repeated summary text dominates prompt-ready variables

## Environment validation

Fail or review if:
- interior scene environment includes exterior geography defaults
- anchor fields are generic

## Implementation Order

Recommended sequence:

1. add prompt-ready fragment fields to scene contract schema
2. add prompt-ready fragment fields to shot package schema
3. update scene-contract prompt to produce prompt-ready fragments
4. update shot-planner prompt to produce prompt-ready fragments
5. add deterministic derivation helpers in prompt preparation
6. render new template-based prompt package types
7. compare finished prompts against `PROMPT_PACKAGE_REFERENCE_NOTES.md`

## Minimal First Pass

If we want the smallest viable step first, do this:

### Scene contracts

Add only:
- `scene_short_description`
- `scene_primary_scale_story_point`
- `scene_required_anchor_catalog`
- `planned_shot_moment_summary`
- `planned_shot_required_anchor_1`
- `planned_shot_scale_proof_detail`

### Shot packages

Add only:
- `visible_primary_subject_id`
- `visible_secondary_subject_ids`
- `primary_subject_frame_position`
- `primary_subject_scale_relation`
- `primary_subject_facing_direction`
- `primary_subject_pose_description`
- `subject_relation_summary`
- `required_environment_anchor_1`
- `camera_package_description`

### Prompt prep

Add only:
- deterministic `image1/image2/image3` mapping
- scene assembly template
- keyframe template

That would already be a major quality jump.
