# Title
SH001 Shot Prompt - Consistency Repair

# ID
CH010_SC002_SH001_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the environment reference for thark audience chamber. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. A captive woman defends her people before a seated assembly of green warriors. The subject from image1 is john carter, foreground entry line within observation periphery, scale of chamber vs Carter, profile left toward the scene action, Carter looking toward council. Preserve the environment from image2 Large scale, designed for high-ranking Tharkian leadership and warriors., monumental scale, dry open Martian terrain, especially observation periphery. medium-full, eye level, normal lens, locked off, shallow subject, high contrast ceremonial. Wide composition across placed for immediate spatial orientation. Carter watching the trial unfold. observation periphery. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH010_SC002; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris; tars_tarkas; lorquas_ptomel
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: normal
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
- scene_id: CH010_SC002
- chapter_id: CH010
- shot_type: establishing_wide
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across thark_audience_chamber with john_carter, Thark Council members placed for immediate spatial orientation.
- shot_size: medium_full
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: profile_left
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground entry line within observation_periphery
- primary_subject_scale_relation: scale of chamber vs Carter
- primary_subject_facing_direction: profile left toward the scene action
- primary_subject_pose_description: Carter looking toward council
- subject_relation_summary: john_carter carries the frame alone
- scene_short_description: A captive woman defends her people before a seated assembly of green warriors.
- shot_moment_summary: Carter watching the trial unfold
- required_environment_anchor_1: observation_periphery
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: scale of chamber vs Carter
- camera_package_description: medium-full, eye level, normal lens, locked off, shallow subject, high contrast ceremonial
- environment_subzone: observation_periphery
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; thark_audience_chamber; DESC_CH010_SC002; DESC_CH010_SC002_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: environment reference for the scene location
- image2_asset: thark audience chamber

# Continuity Notes
- Scene: CH010_SC002 / SC002.
- Variant: Consistency Repair.
- Fixed seating arrangement of Thark leaders
- Dejah Thoris must maintain prisoner positioning relative to the council
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH010\CH010_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH010\CH010_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH010\CH010_SC002\SH001\DIALOGUE.json
