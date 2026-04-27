# Title
SH002 Shot Prompt - Consistency Repair

# ID
CH022_SC002_SH002_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the environment reference for zodanga palace interior. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. A lone man is intercepted by four armed guards within a winding palace corridor. The subject from image1 is john carter, foreground right within zodanga palace interior antechamber, preserve readable body-to-environment scale in frame, profile left toward the scene action, First strike landed. Preserve the environment from image2 monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, broad processional paths and stairs, especially zodanga palace interior antechamber. Keep one readable subject anchor: floor surface. weapon contact/impacts. medium-full, low angle, normal lens, handheld, shallow subject, high contrast ceremonial. Dynamic composition in clear pursuit vectors and readable movement. The violent melee begins. antechamber. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH022_SC002; SHOT_INDEX; DIALOGUE; john_carter
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: normal
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: consistency_repair
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH022_SC002
- chapter_id: CH022
- shot_type: action
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: Dynamic composition in zodanga_palace_interior with clear pursuit vectors and readable movement for john_carter, Four Guardsmen.
- shot_size: medium_full
- camera_angle: low_angle
- camera_motion: handheld
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: profile_left
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground right within zodanga_palace_interior antechamber
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: profile left toward the scene action
- primary_subject_pose_description: First strike landed
- subject_relation_summary: john_carter carries the frame alone
- scene_short_description: A lone man is intercepted by four armed guards within a winding palace corridor.
- shot_moment_summary: The violent melee begins
- required_environment_anchor_1: zodanga_palace_interior antechamber
- required_subject_anchor_1: floor surface
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: weapon contact/impacts
- camera_package_description: medium-full, low angle, normal lens, handheld, shallow subject, high contrast ceremonial
- environment_subzone: zodanga_palace_interior antechamber
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; zodanga_palace_interior; DESC_CH022_SC002; DESC_CH022_SC002_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: environment reference for the scene location
- image2_asset: zodanga palace interior

# Continuity Notes
- Scene: CH022_SC002 / SC002.
- Variant: Consistency Repair.
- Blood splatter patterns on walls and floor
- Weapon positions post-combat
- Cumulative count of dead guards in frame
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH022\CH022_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH022\CH022_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH022\CH022_SC002\SH002\DIALOGUE.json
