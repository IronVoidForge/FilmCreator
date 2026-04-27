# Title
SH002 Shot Prompt - Consistency Repair

# ID
CH023_SC004_SH002_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the environment reference for desolate martian wasteland. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. A pilot survives a crash and realizes his navigation tools are broken while flying over wasteland. The subject from image1 is air machine, midground inside desolate martian wasteland, tiny machine against massive landscape, rear three-quarter left away from camera, machine moving across frame. Preserve the environment from image2 Immense scale with vast arid plains and widely dispersed ruins., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially desolate martian wasteland. extreme-wide, high angle, ultra-wide lens, pan, deep focus, diffuse ambient. Dynamic composition in clear pursuit vectors and readable movement. The air machine flying over the vast wasteland. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH023_SC004; SHOT_INDEX; DIALOGUE; john_carter
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: ultra_wide
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
- scene_id: CH023_SC004
- chapter_id: CH023
- shot_type: action
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: Dynamic composition in desolate_martian_wasteland with clear pursuit vectors and readable movement for john_carter.
- shot_size: extreme_wide
- camera_angle: high_angle
- camera_motion: pan
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: rear_three_quarter_left
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: midground inside desolate_martian_wasteland
- primary_subject_scale_relation: tiny machine against massive landscape
- primary_subject_facing_direction: rear three-quarter left away from camera
- primary_subject_pose_description: machine moving across frame
- subject_relation_summary: air_machine carries the frame alone
- scene_short_description: A pilot survives a crash and realizes his navigation tools are broken while flying over wasteland.
- shot_moment_summary: The air machine flying over the vast wasteland
- required_environment_anchor_1: desolate_martian_wasteland
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: tiny machine against massive landscape
- camera_package_description: extreme-wide, high angle, ultra-wide lens, pan, deep focus, diffuse ambient
- environment_subzone: desolate_martian_wasteland
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; desolate_martian_wasteland; DESC_CH023_SC004; DESC_CH023_SC004_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: environment reference for the scene location
- image2_asset: desolate martian wasteland

# Continuity Notes
- Scene: CH023_SC004 / SC004.
- Variant: Consistency Repair.
- Time of day progression over several hours
- Physical state of the damaged air machine
- Direction of travel relative to Helium
- Blind flight across the landscape
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH023\CH023_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH023\CH023_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH023\CH023_SC004\SH002\DIALOGUE.json
