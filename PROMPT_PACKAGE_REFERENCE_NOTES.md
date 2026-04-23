# Prompt Package Reference Notes

This file is a working reference for what we want prompt packages to become.

It is grounded in:
- the current local book text and artifacts in `projects/princess_of_mars_test`
- Qwen official docs and model guidance
- ComfyUI Qwen multi-image edit workflow guidance

## Research Conclusions

### 1. Prompt length

For Qwen in ComfyUI, the best prompt is not the shortest possible prompt and not a giant undifferentiated paragraph.

Best fit:
- a compact but explicit prompt
- around one dense paragraph or a few short instruction lines
- enough detail to specify identity, scene, camera, pose, relation, and continuity
- not so long that it repeats the same facts in multiple ways

Good rule:
- keep portrait and environment prompts compact
- make multi-image scene and keyframe prompts more explicit, but still structured and direct

### 2. Should we reference `image1`, `image2`, `image3`?

Yes.

For the Qwen multi-image edit path, explicit ordered image references are the right pattern.

Official and workflow guidance supports this:
- Qwen image-edit docs explicitly use image-order instructions like "the girl in image 1 wears the black dress from image 2 and sits in the pose from image 3"
- ComfyUI Qwen edit utilities explicitly expose `image1` through `image5`

So for multi-image edit prompts, this is preferred:
- "Use image1 as the identity reference for the man"
- "Use image2 as the pose reference"
- "Use image3 as the environment reference"

This is better than:
- fully re-describing all three images from scratch every time

### 3. Should we include names in the prompt?

No, not in the positive prompt body.

Use:
- "the man from image1"
- "the green Martian woman from image2"
- "the chamber from image3"

Avoid:
- "John Carter"
- "Sola"
- "Tars Tarkas"

Names are still useful in:
- prompt package metadata
- source artifact ids
- internal mapping tables

But not in the final model-facing positive prompt unless visible text is intentionally wanted on screen.

### 4. Should `prompt_extend` be on?

For these detailed controlled prompts, no.

Qwen guidance indicates prompt extension is useful when the input prompt is short or vague.
For highly specific prompts that already control:
- subject identity
- subject relation
- camera language
- pose
- environment
- continuity

we should prefer:
- `prompt_extend = false`

Otherwise the LLM may over-expand or blur the intended control.

### 5. Should we generate the whole prompt in one shot?

Probably not.

Best future shape:
- generate structured sections first
- assemble the final prompt from those sections

Recommended prompt sections:
- `subject_identity_section`
- `environment_section`
- `camera_section`
- `blocking_section`
- `continuity_section`
- `render_constraints_section`

That will be easier to validate than a single giant prose prompt.

### 6. How the current implementation works

Right now prompt prep is still mostly building one compact positive prompt string per package.

Current code path:
- `orchestrator/prompt_preparation.py`
- `_package_for_character(...)`
- `_package_for_environment(...)`
- `_package_for_shot(...)`

Current behavior:
- build a prose prompt from a few selected fields
- compact it aggressively
- for shot prompts, currently cap it at a relatively short length

That is fine for:
- compact single-subject reference prompts
- rough still prompt seeds

It is probably not ideal for:
- multi-image Qwen edit prompts
- relational scene prompts
- exact shot keyframes
- downstream one-image image-to-video prompts

So the next likely architecture is:
- keep prompt packages generated automatically
- but generate them from structured variables and template rules, not from one freeform prose synthesis step

## Template-First Prompt Strategy

The user idea here is good:
- large parts of the prompt can be deterministic template assembly
- only a few scene-specific text fields need to stay open-ended

This is likely more efficient and more controllable than asking an LLM to write every final prompt from scratch.

### What can be fully templated

These sections can be almost fully generated from variables:

- character portrait prompts
- environment reference prompts
- still-image keyframe prompts
- image-to-video continuation prompts

### What should stay partially open-text

These fields still need good authored scene/shot data:

- short character description
- short environment description
- action moment description
- subject interaction description
- continuity handoff description
- movement continuation description for video

So the best future system is:
- structured variables upstream
- template rendering downstream
- minimal optional LLM pass only when a required open-text field is missing

## Prompt Structure We Want

### Character portrait prompt

Should include:
- role and species
- body build and silhouette
- face and hair
- costume
- neutral camera/reference framing
- readable lighting

Should not include:
- scene-specific action
- environment-specific geography
- proper names

### Environment prompt

Should include:
- environment identity
- layout
- scale
- materials
- lighting
- recurring anchors
- mood

Should not include:
- character names
- scene-specific blocking

### Scene assembly prompt

Should include:
- `image1`, `image2`, `image3`, etc. mapping
- subject placement
- subject size relationship
- subject facing direction
- environment location and subzone
- shot framing and lens intent
- emotional purpose

### Keyframe prompt

Should include:
- all of the above
- exact chosen shot moment
- exact mid-frame read
- one proof-of-story visual detail that must be visible

## Provisional Prompt Templates

These are provisional template shapes that can be rendered from variables.

### Character portrait template

```text
Full-body character reference portrait of ({character_short_description}), ({character_size_description}), ({character_build_description}), ({character_skin_description}), ({character_face_description}), ({character_hair_description}), ({character_eye_description}), ({character_facial_hair_description}), ({character_posture_description}), ({character_expression_description}). Wearing ({character_costume_description}), ({character_silhouette_description}), neutral reference background, ({character_view_angle}), full body visible, ({lighting_style_reference}), ({detail_quality_clause}).
```

### Environment reference template

```text
Wide cinematic environment reference of ({environment_short_description}), ({environment_layout_description}), ({environment_scale_description}), ({environment_architecture_description}), ({environment_materials_description}), ({environment_anchor_1}), ({environment_anchor_2}), ({environment_anchor_3}), ({environment_lighting_description}), ({environment_mood_description}), readable foreground midground background layering, ({environment_depth_description}), ({detail_quality_clause}).
```

### Scene assembly template for Qwen multi-image edit

Best for 2 to 4 input images.

```text
Use image1 as the identity reference for ({image1_subject_role}). Use image2 as the identity or pose reference for ({image2_subject_role}). Use image3 as the environment reference for ({image3_environment_role}). {optional_image4_mapping}

Build ({scene_short_description}). The subject from image1 is ({character_1_frame_position}), ({character_1_scale_relation}), ({character_1_facing_direction}), ({character_1_pose_description}), ({character_1_expression_description}). The subject from image2 is ({character_2_frame_position}), ({character_2_scale_relation}), ({character_2_facing_direction}), ({character_2_pose_description}), ({character_2_relation_to_character_1}). Preserve ({environment_subzone_description}) from image3, including ({required_environment_anchor_1}) and ({required_environment_anchor_2}). ({camera_package_description}). ({emotional_read_description}). ({detail_quality_clause}).
```

### Still-image shot keyframe template

Best for the current prompt packages when generating a key still from multiple reference images.

```text
Use image1 as the identity reference for ({image1_subject_role}). Use image2 as the identity reference for ({image2_subject_role}). Use image3 as the environment reference for ({image3_environment_role}). {optional_image4_mapping}

Generate a cinematic keyframe of ({shot_moment_summary}). The subject from image1 is ({character_1_frame_position}), ({character_1_framing_description}), ({character_1_facing_direction}), ({character_1_pose_description}), ({character_1_expression_description}). The subject from image2 is ({character_2_frame_position}), ({character_2_framing_description}), ({character_2_facing_direction}), ({character_2_pose_description}), ({character_2_relation_to_character_1}). Keep ({environment_subzone_description}) from image3 exact, with ({required_environment_anchor_1}) clearly visible. ({camera_package_description}). ({continuity_note}). ({detail_quality_clause}).
```

### One-image image-to-video continuation template

This is different from the still keyframe prompt.
Here the model only receives one input image, so the prompt has to describe movement continuation rather than scene assembly from multiple refs.

```text
Use the input image as the exact visual starting frame. Preserve identity, costume, environment, spatial layout, and camera framing from the input image.

Continue the shot by showing ({video_motion_summary}). The primary subject should ({primary_subject_motion_description}), while ({secondary_subject_motion_description}). Maintain ({environment_motion_constraints}) and preserve ({required_environment_anchor_1}) as a stable background reference. Motion should feel ({motion_style_description}), with ({camera_motion_description}), ({continuity_behavior_description}), and ({ending_pose_description}) by the end of the clip.
```

## Recommended Variable Sets

These are the variables most worth adding to upstream artifacts so prompts can be assembled deterministically.

### Character variables

Recommended additions or normalizations for character prompt rendering:

- `character_short_description`
- `character_size_description`
- `character_build_description`
- `character_skin_description`
- `character_face_description`
- `character_hair_description`
- `character_eye_description`
- `character_facial_hair_description`
- `character_posture_description`
- `character_expression_description`
- `character_costume_description`
- `character_silhouette_description`
- `character_view_angle_default`
- `character_reference_lighting_default`

Most of these can map cleanly from current descriptor fields:
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
- `silhouette_notes`

### Environment variables

Recommended environment variables:

- `environment_short_description`
- `environment_layout_description`
- `environment_scale_description`
- `environment_architecture_description`
- `environment_materials_description`
- `environment_lighting_description`
- `environment_mood_description`
- `environment_depth_description`
- `environment_anchor_1`
- `environment_anchor_2`
- `environment_anchor_3`
- `environment_reference_lens_default`

These can largely map from:
- `layout`
- `scale`
- `architecture`
- `materials`
- `lighting`
- `mood`
- `camera_friendly_landmarks`
- `depth_cues`

### Scene variables

Scene prompts should probably not be fully free-written.
We should add a scene-level package that seeds shot prompts.

Recommended scene variables:

- `scene_short_description`
- `scene_emotional_read`
- `scene_environment_subzone_catalog`
- `scene_primary_scale_story_point`
- `scene_required_anchor_catalog`
- `scene_subject_visibility_rules`
- `scene_reference_image_plan`
- `scene_default_camera_package`

More specifically, the scene should help define:
- which subjects are likely image1/image2/image4
- which environment is image3
- which environmental proof details matter in this scene

### Shot variables

Shot variables are the most important.

Recommended shot prompt variables:

- `shot_moment_summary`
- `shot_story_purpose`
- `shot_emotional_read`
- `shot_primary_subject_id`
- `shot_secondary_subject_ids`
- `shot_primary_subject_role`
- `shot_secondary_subject_roles`
- `shot_primary_subject_frame_position`
- `shot_secondary_subject_frame_positions`
- `shot_primary_subject_facing_direction`
- `shot_secondary_subject_facing_directions`
- `shot_primary_subject_pose`
- `shot_secondary_subject_poses`
- `shot_primary_subject_expression`
- `shot_secondary_subject_expressions`
- `shot_primary_subject_scale_relation`
- `shot_secondary_subject_scale_relations`
- `shot_relation_summary`
- `shot_environment_subzone`
- `shot_required_environment_anchor_1`
- `shot_required_environment_anchor_2`
- `shot_required_scale_proof_detail`
- `shot_continuity_note`

And then the cinematic enums we already started adding:
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

### Video continuation variables

For one-image image-to-video prompts, add:

- `video_motion_summary`
- `video_primary_subject_motion`
- `video_secondary_subject_motion`
- `video_environment_motion_constraints`
- `video_camera_motion_description`
- `video_motion_style_description`
- `video_continuity_behavior_description`
- `video_ending_pose_description`

This is important because still-image keyframes and image-to-video prompts are not the same problem.

## Efficient Generation Strategy

Most efficient future design:

### Step 1

Generate or derive structured fields into:
- characters
- environments
- scenes
- shots

### Step 2

Render deterministic template prompts for:
- character reference
- environment reference
- scene assembly
- still-image keyframe
- one-image image-to-video continuation

### Step 3

Optionally run a very small polishing pass only if needed:
- remove awkward phrasing
- collapse redundant commas
- shorten overlong prompts

That is much cheaper and more controllable than:
- one big LLM-written final prompt per artifact

## What We Should Probably Change In Prompt Prep

Prompt prep should eventually output either:

### Option A: final prompt text only

This is simplest, but hardest to debug.

### Option B: structured prompt sections plus final prompt text

This is probably better.

Example:
- `prompt_mapping_section`
- `prompt_subject_section`
- `prompt_environment_section`
- `prompt_camera_section`
- `prompt_continuity_section`
- `prompt_final_positive`

This will make it much easier to compare:
- ideal prompt design
- generated prompt design

and to spot exactly what part is weak.

## Scene Exercise 1

### Source Scene

Book:
- `projects/princess_of_mars_test/01_source/chapters/CH004_chapter_iv.md`

Pipeline scene:
- `projects/princess_of_mars_test/02_story_analysis/contracts/scenes/CH004/CH004_SC002.json`

Pipeline shots:
- `projects/princess_of_mars_test/02_story_analysis/contracts/shots/CH004/CH004_SC002/SHOT_INDEX.json`

### Real scene truth from the book

The Earthman is escorted into a monumental audience chamber.
Tars Tarkas brings him before the green Martian ruler.
The ruler is elevated on a dais and visually dominant.
The chamber is ancient, marble, grand, and full of human-scale furniture that is absurdly too small for the giant Martians.
The emotional turn is intimidation shifting into analytical observation.

### Character references

Internal mapping only:
- `image1` = Earthman captive / John Carter type reference
- `image2` = Tars Tarkas type escort reference
- `image3` = grand audience chamber environment reference
- `image4` = chieftain ruler reference

### Character portrait prompt: Earthman captive

Use this to build the human reference image.

```text
Full-body character reference portrait of a rugged adult human male frontier soldier, tall lean battle-tested build, sun-weathered skin, dark practical short hair, angular weathered face, dark steady eyes, clean-shaven or short field stubble, upright controlled posture, restrained alert expression. He wears worn frontier cavalry clothing with leather gear and practical boots, simple silhouette, survival-ready, no ornate fantasy armor, no decorative jewelry, neutral reference background, front three-quarter view, full body visible, even readable lighting, highly detailed fabric and leather texture, Ultra HD, 4K, cinematic composition.
```

### Character portrait prompt: Tars Tarkas type escort

```text
Full-body character reference portrait of a towering green Martian warrior leader, much larger than a human, massive war-ready build, deep green skin, severe planar face, mostly bare scalp, no facial hair, stern disciplined expression, dominant upright posture. He wears Martian warrior gear made of hides, leather, metal fittings, and war equipment, imposing desert-warrior silhouette, front three-quarter view, full body visible, neutral reference background, even readable lighting, strong silhouette clarity, Ultra HD, 4K, cinematic composition.
```

### Character portrait prompt: chieftain ruler

```text
Full-body character reference portrait of an enormous green Martian chieftain ruler, broad and towering, severe planar Martian facial structure, deep green skin, no facial hair, intimidating sovereign presence. He wears heavy metal ornaments, bright feathers, jeweled leather trappings, and a short white fur cape lined with vivid scarlet silk. Formal dominant posture, ceremonial authority, front three-quarter view, full body visible, readable hierarchy in costume and silhouette, neutral reference background, dramatic ceremonial lighting, Ultra HD, 4K, cinematic composition.
```

### Environment prompt: grand audience chamber

```text
Wide cinematic environment reference of an ancient Martian grand audience chamber, gleaming white marble architecture with gold and jewel inlay, enormous ceremonial hall ringed by galleries, high vaulted ceilings, central rostrum and raised dais, monumental scale, oversized carved desks and chairs that look human-sized inside a hall occupied by giant Martians, heavy ancient grandeur, strong shadow play across polished stone, formal political atmosphere, readable foreground midground background layering, symmetrical processional composition, Ultra HD, 4K, cinematic composition.
```

### Scene assembly prompt

Use when assembling the scene from references.

```text
Use image1 as the identity reference for the human captive. Use image2 as the identity reference for the towering green Martian escort. Use image3 as the environment reference for the grand audience chamber. Use image4 as the identity and costume reference for the ruler on the dais.

Build a cinematic political arrival scene inside the chamber. The man from image1 stands on the lower chamber floor in the foreground right of center, visibly human-scale and smaller than everyone else, facing left toward the dais at a front_three_quarter_left angle, posture upright but tense, expression controlled and wary. The green Martian from image2 stands slightly behind and to the left of the man in an escort position, much taller, protective but authoritative, profile_right or front_three_quarter_right to camera. The ruler from image4 is elevated in the background center on the dais, seated or squatting in command posture, visually dominant through height, placement, and ornament.

Preserve the exact hall from image3: white marble, gold detail, galleries, central rostrum, and especially the too-small carved desks and chairs. Show the absurd scale relationship clearly by including one human-scale desk or chair in the same frame as the giant Martians. Ceremonial high-contrast lighting, deep architectural shadows, medium-wide composition, eye-level to slightly low-angle, normal lens, locked-off camera, deep focus, Ultra HD, 4K, cinematic composition.
```

### Three ideal shot prompts

#### Shot 1: entrance before the dais

```text
Use image1 as the identity reference for the human captive, image2 for the green Martian escort, image3 for the chamber, and image4 for the ruler.

Generate a medium-wide cinematic shot of the first presentation before power. The man from image1 is foreground right, full body visible, front_three_quarter_left, just halted at the foot of the main chamber floor. The green Martian from image2 stands slightly behind him on the left, larger and watchful. The ruler from image4 is elevated in the background center on the dais. Keep the white marble galleries and central rostrum from image3 exact. One carved chair or desk must be visible to prove the absurd mismatch of scale. Eye-level with a slight low-angle feel, normal lens, locked-off camera, deep focus, ceremonial lighting with heavy shadows, intimidation dominant over curiosity.
```

#### Shot 2: observation of absurd scale

```text
Use image1 as the identity reference for the human captive, image3 as the environment reference, and image4 as the ruler reference.

Generate a medium_full keyframe focused on the moment the man from image1 realizes that the giant Martians are occupying a hall furnished for much smaller beings. The man is foreground right of center, medium_full framing, front_three_quarter_left, head lifted toward the dais but eyes also tracking the carved desk in the foreground. The ruler from image4 remains visible but secondary in the background center on the raised rostrum. The hall from image3 must show white marble, galleries, and one obviously human-scale desk or chair near the man. Eye-level slightly low, portrait lens leaning normal, locked-off camera, deep focus, ceremonial light and shadow, emotional transition from intimidation into analytical curiosity.
```

#### Shot 3: ruler dominance insert

```text
Use image4 as the identity and regalia reference for the ruler and image3 as the chamber reference.

Generate a close but still spatially grounded cinematic shot of the ruler from image4 on the dais. The ruler is centered, front_three_quarter_left, dominant and elevated, richly ornamented, severe expression, white fur cape with scarlet lining clearly visible. Include enough of image3 to keep the chamber legible: marble steps of the dais, one section of gallery, and the monumental scale of the hall. Medium_close framing, slight low angle, portrait lens, locked-off camera, shallow_subject focus with readable background architecture, ceremonial high-contrast lighting, power and hierarchy emphasized.
```

## Scene Exercise 2

### Source Scene

Book:
- `projects/princess_of_mars_test/01_source/chapters/CH005_chapter_v.md`

Pipeline scene:
- `projects/princess_of_mars_test/02_story_analysis/contracts/scenes/CH005/CH005_SC001.json`

Pipeline shots:
- `projects/princess_of_mars_test/02_story_analysis/contracts/shots/CH005/CH005_SC001/SHOT_INDEX.json`

### Real scene truth from the book

This is a quieter interaction scene.
The human captive studies the murals in his chamber.
Sola brings him food and drink, watches him, and later covers him with furs when the night turns cold.
The watch dog guards the doorway.
The emotional turn is isolation and uncertainty softening into comfort and observation.

### Character references

Internal mapping only:
- `image1` = human captive / John Carter type reference
- `image2` = Sola reference
- `image3` = decorated captive chamber reference
- `image4` = watch dog / calot reference

### Character portrait prompt: Sola

Use book truth over the currently flawed descriptor if they conflict.

```text
Full-body character reference portrait of a female green Martian caregiver, very tall compared with a human, lean powerful Martian frame, smooth light olive-green skin, severe but sympathetic face, no facial hair, restrained expression with visible intelligence and concern. She wears practical Green Martian attire with leather and minimal ornament, readable silhouette, calm deliberate posture, front three-quarter view, full body visible, neutral reference background, even readable lighting, Ultra HD, 4K, cinematic composition.
```

### Environment prompt: decorated captive chamber

```text
Wide interior environment reference of a decorated Martian sleeping chamber, spacious ancient room with mural paintings and mosaics, painted landscapes with no living creatures, layered silks and furs scattered as bedding, windows admitting hard daylight or cold moonlight, ancient but still beautiful architecture, atmosphere of captivity mixed with strange quiet comfort, clear foreground midground background separation, readable doorway where a guard beast could lie across the threshold, Ultra HD, 4K, cinematic composition.
```

### Character prompt: watch dog / calot

```text
Full-body creature reference portrait of a Martian watch dog, low long body on many short powerful legs, fast predatory build, ferocious tusked mouth, ugly intelligent face, alert guarding posture, alien but loyal, neutral reference background, side three-quarter view, full body visible, readable anatomy and silhouette, Ultra HD, 4K, cinematic composition.
```

### Scene assembly prompt

```text
Use image1 as the identity reference for the human captive. Use image2 as the identity reference for the green Martian woman. Use image3 as the environment reference for the decorated chamber. Use image4 as the identity reference for the watch dog guarding the threshold.

Build a quiet cinematic interior scene of care and wary observation. The man from image1 sits or reclines low on silks and furs near the center-right of the room, human-scale, physically tired but alert, facing left toward the murals and occasionally toward the woman from image2. The woman from image2 is midground left, much taller, calm and observant, either kneeling or lowering herself to place food and drink beside him, expression reserved but sympathetic. The creature from image4 lies stretched across the doorway in the background, guarding the exit, body blocking the threshold.

Preserve the room from image3: mural-painted walls showing empty landscapes, mosaics, windows, layered silks and furs, ancient decorated surfaces. The mood is isolation softening into uneasy comfort. Medium-wide interior composition, eye-level, normal lens, locked-off camera, soft but cold directional light, deep focus, Ultra HD, 4K, cinematic composition.
```

### Three ideal shot prompts

#### Shot 1: captive studies the murals

```text
Use image1 as the identity reference for the human captive, image3 as the chamber reference, and image4 as the watch dog reference.

Generate a medium shot of the man from image1 seated low among silks and furs, turned toward the mural-covered wall, front_three_quarter_right to camera, physically exhausted but alert. The murals from image3 must be readable behind him, showing beautiful landscapes with no visible living creatures. The guard creature from image4 lies stretched across the doorway in the background, watching him. Eye-level, normal lens, locked-off camera, deep focus, cool interior light, emotional tone of isolation and curiosity.
```

#### Shot 2: Sola provides care

```text
Use image1 as the identity reference for the human captive, image2 as the identity reference for the green Martian woman, and image3 as the chamber reference.

Generate a medium cinematic interaction shot of the woman from image2 placing food and drink on the floor beside the man from image1. The man is seated or crouched on the right, human-scale, looking up toward her with guarded curiosity. The woman is left of center, much taller, bending or lowering herself with measured careful motion, front_three_quarter_right to camera. Keep the chamber from image3 readable with murals, silks, and windows. Eye-level, portrait-leaning normal lens, locked-off camera, soft directional interior light, deep focus, emotional shift from uncertainty into reluctant comfort.
```

#### Shot 3: night cold and fur covering

```text
Use image1 as the identity reference for the human captive, image2 as the green Martian woman, and image3 as the chamber reference.

Generate a quiet interior nighttime keyframe. The man from image1 lies asleep or half-awake under furs near the room center, small against the ancient chamber. The woman from image2 leans in from the left side of frame to pull another fur across him, her expression controlled but genuinely protective. Preserve the chamber from image3 with dark walls, murals fading into shadow, and cold moonlit or low lamp illumination. Medium shot, eye-level, normal lens, locked-off camera, low-key night lighting, gentle contrast, deep emotional read of alien compassion.
```

## What This Means For Prompt Packages

The future prompt packages should not try to generate the final scene prompt as one unstructured paragraph from scratch.

They should produce at least these sections:

### For character prompts
- identity block
- silhouette block
- costume block
- camera/reference block

### For environment prompts
- layout block
- scale block
- anchor block
- lighting block

### For scene assembly prompts
- input image mapping block
- subject placement block
- subject relation block
- environment preservation block
- camera block
- emotion block

### For keyframe prompts
- chosen moment block
- exact visible proof detail block
- continuity block
- camera block
- render constraints block

## Comparison Checklist

When the current generation run finishes, compare the produced prompt packages against this file and ask:

1. Does the prompt identify what each reference image is for?
2. Does it avoid proper names in the positive prompt body?
3. Does it explicitly place each subject in the frame?
4. Does it specify subject facing direction?
5. Does it make relative scale clear?
6. Does it specify one environmental anchor that must be visible?
7. Does it specify the emotional point of the frame?
8. Does it specify enough camera grammar to be reproducible?
9. Is it direct enough that `prompt_extend` should be off?
10. Does it read like a usable Comfy/Qwen edit instruction rather than a vague description?

## External References

- Qwen Image model card:
  - https://huggingface.co/Qwen/Qwen-Image
- Diffusers QwenImage docs:
  - https://huggingface.co/docs/diffusers/en/api/pipelines/qwenimage
- Aliyun Qwen text-to-image guide:
  - https://help.aliyun.com/zh/model-studio/text-to-image
- Aliyun prompt guide:
  - https://help.aliyun.com/zh/model-studio/text-to-image-prompt
- Aliyun Qwen image edit guide with ordered image references:
  - https://help.aliyun.com/zh/model-studio/qwen-image-edit-guide
- ComfyUI Qwen edit utility with `image1` through `image5`:
  - https://github.com/lrzjason/Comfyui-QwenEditUtils
