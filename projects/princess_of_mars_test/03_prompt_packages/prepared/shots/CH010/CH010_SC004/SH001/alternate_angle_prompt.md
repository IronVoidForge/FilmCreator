# Title
SH001 Shot Prompt - Alternate Angle

# ID
CH010_SC004_SH001_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for lorquas ptomel audience chamber. Use image4 as the identity reference for an additional visible subject. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. A warrior acquires ceremonial regalia and weapons within a massive stone audience chamber. The subject from image1 is john carter, foreground entry line within combat aftermath zone, regalia size relative to Carter hands, front three-quarter right toward the scene action, Carter standing over spoils. The subject from image2 is john carter plays against lorquas ptomel, tars tarkas in the same frame. Preserve the environment from image3 Large scale, centered around a focal point for the presiding chieftain., monumental scale, dry open Martian terrain, especially combat aftermath zone. medium, eye level, normal lens, push in, shallow subject, high contrast ceremonial. Readable medium composition in featuring. Carter reaches for the deceased warrior's weapons. combat aftermath zone. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH010_SC004; SHOT_INDEX; DIALOGUE; john_carter; lorquas_ptomel; tars_tarkas
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: normal
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: alternate_angle
- review_notes: Prompt body is missing the required subject anchor for an on-screen shot.
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH010_SC004
- chapter_id: CH010
- shot_type: medium
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in lorquas_ptomel_audience_chamber featuring john_carter, lorquas_ptomel, tars_tarkas.
- shot_size: medium
- camera_angle: eye_level
- camera_motion: push_in
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: front_three_quarter_right
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: lorquas_ptomel; tars_tarkas
- primary_subject_frame_position: foreground entry line within combat aftermath zone
- primary_subject_scale_relation: regalia size relative to Carter hands
- primary_subject_facing_direction: front three-quarter right toward the scene action
- primary_subject_pose_description: Carter standing over spoils
- subject_relation_summary: john_carter plays against lorquas_ptomel, tars_tarkas in the same frame
- scene_short_description: A warrior acquires ceremonial regalia and weapons within a massive stone audience chamber.
- shot_moment_summary: Carter reaches for the deceased warrior's weapons
- required_environment_anchor_1: combat aftermath zone
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: regalia size relative to Carter hands
- camera_package_description: medium, eye level, normal lens, push in, shallow subject, high contrast ceremonial
- environment_subzone: combat aftermath zone
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; lorquas_ptomel; tars_tarkas; lorquas_ptomel_audience_chamber; DESC_CH010_SC004; DESC_CH010_SC004_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: identity reference for the secondary visible subject
- image2_asset: lorquas ptomel
- image3_role: environment reference for the scene location
- image3_asset: lorquas ptomel audience chamber
- image4_role: identity reference for an additional visible subject
- image4_asset: tars tarkas

# Continuity Notes
- Scene: CH010_SC004 / SC004.
- Variant: Alternate Angle.
- Specific weapons and regalia items held or worn by john_carter
- Physical state of john_carter post-combat
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH010\CH010_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH010\CH010_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH010\CH010_SC004\SH001\DIALOGUE.json
