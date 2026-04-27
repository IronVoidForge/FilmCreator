# Title
SH002 Shot Prompt - Consistency Repair

# ID
CH001_SC002_SH002_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the environment reference for arizona quartz vein location. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. A lone rider observes suspicious valley movements and discovers fresh pony tracks on a desert trail. The subject from image1 is valley movement, midground inside arizona quartz vein location, Small scale human presence vs large scale environmental threat, facing directly toward camera, Carter's gaze. Preserve the environment from image2 Vast mountain ranges containing localized mineral deposits and rocky terrain., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially valley floor. Keep one readable subject anchor: Carter's gaze. extreme-wide, high angle, telephoto lens, pan, zoom subtle in, environment priority, hard directional. Wide composition across placed for immediate spatial orientation. POV of suspicious movement in the valley. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH001_SC002; SHOT_INDEX; DIALOGUE; john_carter
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: telephoto
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
- scene_id: CH001_SC002
- chapter_id: CH001
- shot_type: establishing_wide
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across arizona_quartz_vein_location with john_carter placed for immediate spatial orientation.
- shot_size: extreme_wide
- camera_angle: high_angle
- camera_motion: pan
- zoom_behavior: subtle_in
- focus_strategy: environment_priority
- lighting_style: hard_directional
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: midground inside arizona_quartz_vein_location
- primary_subject_scale_relation: Small scale human presence vs large scale environmental threat.
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: Carter's gaze
- subject_relation_summary: valley_movement carries the frame alone
- scene_short_description: A lone rider observes suspicious valley movements and discovers fresh pony tracks on a desert trail.
- shot_moment_summary: POV of suspicious movement in the valley
- required_environment_anchor_1: valley_floor
- required_subject_anchor_1: Carter's gaze
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: Small scale human presence vs large scale environmental threat.
- camera_package_description: extreme-wide, high angle, telephoto lens, pan, zoom subtle in, environment priority, hard directional
- environment_subzone: arizona_quartz_vein_location
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; arizona_quartz_vein_location; DESC_CH001_SC002; DESC_CH001_SC002_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: environment reference for the scene location
- image2_asset: arizona quartz vein location

# Continuity Notes
- Scene: CH001_SC002 / SC002.
- Variant: Consistency Repair.
- Horse movement direction must remain consistent during pursuit
- Lighting must shift to reflect passing time during the track
- Detection of suspicious movement
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH001\CH001_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH001\CH001_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH001\CH001_SC002\SH002\DIALOGUE.json
