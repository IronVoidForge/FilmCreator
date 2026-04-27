# Title
SH001 Shot Prompt - Primary Keyframe

# ID
CH006_SC002_SH001_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for watch thing. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for martian interior chamber. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. A desperate struggle against a massive ape ends with a lethal blow from a stone weapon. The subject from image1 is Bull Ape 1, foreground entry line within central combat floor, ape size vs watch thing, profile left toward the scene action, struggle in progress. The subject from image2 is Bull Ape 1 plays against protagonist in the same frame. Preserve the environment from image3 monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, broad processional paths and stairs, especially central combat floor. medium-full, eye level, wide lens, handheld, shallow subject, low key night. Readable medium composition in that keeps, together so the physical effort stays obvious. watch thing struggling against ape strength. central combat floor. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH006_SC002; SHOT_INDEX; DIALOGUE; protagonist; watch_thing
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: wide
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: primary_keyframe
- review_notes: Prompt body is missing the required subject anchor for an on-screen shot.
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH006_SC002
- chapter_id: CH006
- shot_type: medium
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in martian_interior_chamber that keeps Bull Ape 1, watch_thing, protagonist together so the physical effort stays obvious.
- shot_size: medium_full
- camera_angle: eye_level
- camera_motion: handheld
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: low_key_night
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: profile_left
- visible_primary_subject_id: watch_thing
- visible_secondary_subject_ids: protagonist
- primary_subject_frame_position: foreground entry line within central combat floor
- primary_subject_scale_relation: ape size vs watch_thing
- primary_subject_facing_direction: profile left toward the scene action
- primary_subject_pose_description: struggle in progress
- subject_relation_summary: Bull Ape 1 plays against protagonist in the same frame
- scene_short_description: A desperate struggle against a massive ape ends with a lethal blow from a stone weapon.
- shot_moment_summary: watch_thing struggling against ape strength
- required_environment_anchor_1: central combat floor
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: ape size vs watch_thing
- camera_package_description: medium-full, eye level, wide lens, handheld, shallow subject, low key night
- environment_subzone: central combat floor
- prompt_family: shot_prompt
- reference_asset_ids: watch_thing; protagonist; martian_interior_chamber; DESC_CH006_SC002; DESC_CH006_SC002_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: watch thing
- image2_role: identity reference for the secondary visible subject
- image2_asset: protagonist
- image3_role: environment reference for the scene location
- image3_asset: martian interior chamber

# Continuity Notes
- Scene: CH006_SC002 / SC002.
- Variant: Primary Keyframe.
- Blood and gore accumulation from the skull crush
- Physical wound state of watch_thing
- watch_thing loses struggle against Bull Ape 1
- Resolve Bull Ape 1 -> Bull Ape 1
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH006\CH006_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH006\CH006_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH006\CH006_SC002\SH001\DIALOGUE.json
