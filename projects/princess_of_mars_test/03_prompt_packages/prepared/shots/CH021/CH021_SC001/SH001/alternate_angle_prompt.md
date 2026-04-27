# Title
SH001 Shot Prompt - Alternate Angle

# ID
CH021_SC001_SH001_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the environment reference for martian agricultural tracts. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. A traveler moves through advanced irrigation systems across vast cultivated Martian plains. The subject from image1 is john carter, midground inside martian agricultural tracts/irrigation channels, infrastructure vs human size, profile right toward the scene action, wide vista. Preserve the environment from image2 Expansive horizons with a network of underground irrigation systems and rhythmic agricultural patterns., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially martian agricultural tracts/irrigation channels. wide, eye level, ultra-wide lens, track, deep focus, diffuse ambient. Wide composition across placed for immediate spatial orientation. Carter views the vast irrigation systems. /irrigation channels. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH021_SC001; SHOT_INDEX; DIALOGUE; john_carter
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: ultra_wide
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
- scene_id: CH021_SC001
- chapter_id: CH021
- shot_type: establishing_wide
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across martian_agricultural_tracts with john_carter placed for immediate spatial orientation.
- shot_size: wide
- camera_angle: eye_level
- camera_motion: track
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: profile_right
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: midground inside martian_agricultural_tracts/irrigation_channels
- primary_subject_scale_relation: infrastructure vs human size
- primary_subject_facing_direction: profile right toward the scene action
- primary_subject_pose_description: wide vista
- subject_relation_summary: john_carter carries the frame alone
- scene_short_description: A traveler moves through advanced irrigation systems across vast cultivated Martian plains.
- shot_moment_summary: Carter views the vast irrigation systems
- required_environment_anchor_1: martian_agricultural_tracts/irrigation_channels
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: infrastructure vs human size
- camera_package_description: wide, eye level, ultra-wide lens, track, deep focus, diffuse ambient
- environment_subzone: martian_agricultural_tracts/irrigation_channels
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; martian_agricultural_tracts; DESC_CH021_SC001; DESC_CH021_SC001_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: environment reference for the scene location
- image2_asset: martian agricultural tracts

# Continuity Notes
- Scene: CH021_SC001 / SC001.
- Variant: Alternate Angle.
- Travel progression and distance across plains
- Lighting consistency across vast agricultural tracts
- Observation of Martian infrastructure
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH021\CH021_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH021\CH021_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH021\CH021_SC001\SH001\DIALOGUE.json
