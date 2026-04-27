# Title
SH001 Shot Prompt - Consistency Repair

# ID
CH016_SC003_SH001_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the environment reference for thark city and surroundings. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. A man moves stealthily through dark canals before arriving at an empty, silent meeting point. The subject from image1 is john carter, foreground entry line within thark city and surroundings, thoat size relative to Carter, profile left toward the scene action, shadowed movement. Preserve the environment from image2 Transitions from wide-open sea bottom vistas to dense Thark plazas, includes sprawling canal networks and massive communal spaces., monumental scale, dry open Martian terrain, especially thark city and surroundings. medium-full, eye level, wide lens, handheld, shallow subject, low key night. Wide composition across placed for immediate spatial orientation. Carter moving through shadows with thoats. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH016_SC003; SHOT_INDEX; DIALOGUE; john_carter
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: wide
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: consistency_repair
- review_notes: Prompt body is missing the required subject anchor for an on-screen shot.
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH016_SC003
- chapter_id: CH016
- shot_type: establishing_wide
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across thark_city_and_surroundings with john_carter placed for immediate spatial orientation.
- shot_size: medium_full
- camera_angle: eye_level
- camera_motion: handheld
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: low_key_night
- subject_visibility: silhouette
- narration_mode: none
- primary_subject_angle: profile_left
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground entry line within thark_city_and_surroundings
- primary_subject_scale_relation: thoat size relative to Carter
- primary_subject_facing_direction: profile left toward the scene action
- primary_subject_pose_description: shadowed movement
- subject_relation_summary: john_carter carries the frame alone
- scene_short_description: A man moves stealthily through dark canals before arriving at an empty, silent meeting point.
- shot_moment_summary: Carter moving through shadows with thoats
- required_environment_anchor_1: thark_city_and_surroundings
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: thoat size relative to Carter
- camera_package_description: medium-full, eye level, wide lens, handheld, shallow subject, low key night
- environment_subzone: thark_city_and_surroundings
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; thark_city_and_surroundings; DESC_CH016_SC003; DESC_CH016_SC003_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: environment reference for the scene location
- image2_asset: thark city and surroundings

# Continuity Notes
- Scene: CH016_SC003 / SC003.
- Variant: Consistency Repair.
- Presence/absence of thoats
- Light source balance (moonlight vs. city glow)
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH016\CH016_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH016\CH016_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH016\CH016_SC003\SH001\DIALOGUE.json
