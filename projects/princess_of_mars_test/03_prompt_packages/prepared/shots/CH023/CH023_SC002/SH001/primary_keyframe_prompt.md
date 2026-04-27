# Title
SH001 Shot Prompt - Primary Keyframe

# ID
CH023_SC002_SH001_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the environment reference for zodanga urban complex. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. A climber scales a massive vertical structure to infiltrate a roof and steal machinery. The subject from image1 is john carter, midground inside barracks exterior wall, Extreme wide shot showing tiny figure against 1,000ft wall, profile right toward the scene action, climbing motion. Preserve the environment from image2 Dense urban layout with significant vertical scale, dominated by massive barracks and palace towers creating deep canyons., monumental scale, dry open Martian terrain, especially Zodangan Barracks exterior wall. extreme-wide, low angle, ultra-wide lens, tilt, deep focus, low key night. Wide composition across placed for immediate spatial orientation. john carter climbing the massive wall. barracks exterior wall. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH023_SC002; SHOT_INDEX; DIALOGUE; john_carter; zodangan_sentry
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: ultra_wide
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
- scene_id: CH023_SC002
- chapter_id: CH023
- shot_type: establishing_wide
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across zodanga_urban_complex with john_carter placed for immediate spatial orientation.
- shot_size: extreme_wide
- camera_angle: low_angle
- camera_motion: tilt
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: low_key_night
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: profile_right
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: midground inside barracks_exterior_wall
- primary_subject_scale_relation: Extreme wide shot showing tiny figure against 1,000ft wall
- primary_subject_facing_direction: profile right toward the scene action
- primary_subject_pose_description: climbing motion
- subject_relation_summary: john_carter carries the frame alone
- scene_short_description: A climber scales a massive vertical structure to infiltrate a roof and steal machinery.
- shot_moment_summary: john_carter climbing the massive wall
- required_environment_anchor_1: Zodangan Barracks exterior wall
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: Extreme wide shot showing tiny figure against 1,000ft wall
- camera_package_description: extreme-wide, low angle, ultra-wide lens, tilt, deep focus, low key night
- environment_subzone: barracks_exterior_wall
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; zodanga_urban_complex; DESC_CH023_SC002; DESC_CH023_SC002_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: environment reference for the scene location
- image2_asset: zodanga urban complex

# Continuity Notes
- Scene: CH023_SC002 / SC002.
- Variant: Primary Keyframe.
- Vertical height/scale perception relative to ground
- Wind direction and intensity on exterior surfaces
- Position of the incapacitated sentry hanging over edge
- The climb up the exterior wall
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH023\CH023_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH023\CH023_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH023\CH023_SC002\SH001\DIALOGUE.json
