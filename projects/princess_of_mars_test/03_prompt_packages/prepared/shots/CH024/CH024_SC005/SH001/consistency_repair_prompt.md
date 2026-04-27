# Title
SH001 Shot Prompt - Consistency Repair

# ID
CH024_SC005_SH001_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the environment reference for zodanga walled city. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. A small group scales massive dark walls under moonlight to infiltrate a city. The subject from image1 is Small Group of Tharks, midground inside zodanga walled city/wall exterior, height of wall vs character height, profile left toward the scene action, low angle at base. Preserve the environment from image2 Fortified perimeter with massive walls surrounding a central palace complex., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially zodanga walled city/wall exterior. Keep one readable subject anchor: carborundum wall surface. wide, low angle, wide lens, tilt, deep focus, low key night. Wide composition across placed for immediate spatial orientation. Characters begin forming the ladder at the wall base. /wall exterior. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH024_SC005; SHOT_INDEX; DIALOGUE; john_carter
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: wide
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
- scene_id: CH024_SC005
- chapter_id: CH024
- shot_type: establishing_wide
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across zodanga_walled_city with Small Group of Tharks, john_carter placed for immediate spatial orientation.
- shot_size: wide
- camera_angle: low_angle
- camera_motion: tilt
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: low_key_night
- subject_visibility: silhouette
- narration_mode: none
- primary_subject_angle: profile_left
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: midground inside zodanga_walled_city/wall_exterior
- primary_subject_scale_relation: height of wall vs character height
- primary_subject_facing_direction: profile left toward the scene action
- primary_subject_pose_description: low angle at base
- subject_relation_summary: Small Group of Tharks carries the frame alone
- scene_short_description: A small group scales massive dark walls under moonlight to infiltrate a city.
- shot_moment_summary: Characters begin forming the ladder at the wall base
- required_environment_anchor_1: zodanga_walled_city/wall_exterior
- required_subject_anchor_1: carborundum wall surface
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: height of wall vs character height
- camera_package_description: wide, low angle, wide lens, tilt, deep focus, low key night
- environment_subzone: zodanga_walled_city/wall_exterior
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; zodanga_walled_city; DESC_CH024_SC005; DESC_CH024_SC005_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: environment reference for the scene location
- image2_asset: zodanga walled city

# Continuity Notes
- Scene: CH024_SC005 / SC005.
- Variant: Consistency Repair.
- Moonlight direction and shadow consistency
- Height scale of carborundum walls relative to characters
- Physical placement and stability of the human ladder elements
- Formation of the human ladder at the wall base
- Resolve Small Group of Tharks -> Small Group of Tharks
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH024\CH024_SC005.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH024\CH024_SC005\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH024\CH024_SC005\SH001\DIALOGUE.json
