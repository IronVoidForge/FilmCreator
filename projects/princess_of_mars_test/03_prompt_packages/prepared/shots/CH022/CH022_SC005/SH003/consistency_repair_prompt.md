# Title
SH003 Shot Prompt - Consistency Repair

# ID
CH022_SC005_SH003_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the environment reference for zodanga palace interior. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. A man waits for nightfall before leaping from a high balcony into a dark cityscape. The subject from image1 is john carter, midground inside overlooking Zodangan avenue/cityscape at night, size of city vs character, back to camera with head turned toward the action, falling through frame. Preserve the environment from image2 monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, broad processional paths and stairs, especially overlooking Zodangan avenue/cityscape at night. Keep one readable subject anchor: back to camera with head turned toward the action. extreme-wide, high angle, wide lens, pull back, environment priority, low key night. Wide composition across placed for immediate spatial orientation. Carter landing/disappearing. overlooking Zodangan avenue/cityscape at night. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH022_SC005; SHOT_INDEX; DIALOGUE; john_carter
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: wide
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: consistency_repair
- review_notes: Environment reference conflict: prompt variables align more with `none` than bound `zodanga_palace_interior`.
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH022_SC005
- chapter_id: CH022
- shot_type: establishing_wide
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across zodanga_palace_interior with john_carter placed for immediate spatial orientation.
- shot_size: extreme_wide
- camera_angle: high_angle
- camera_motion: pull_back
- zoom_behavior: none
- focus_strategy: environment_priority
- lighting_style: low_key_night
- subject_visibility: partial
- narration_mode: none
- primary_subject_angle: back
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: midground inside overlooking Zodangan avenue/cityscape at night
- primary_subject_scale_relation: size of city vs character
- primary_subject_facing_direction: back to camera with head turned toward the action
- primary_subject_pose_description: falling through frame
- subject_relation_summary: john_carter carries the frame alone
- scene_short_description: A man waits for nightfall before leaping from a high balcony into a dark cityscape.
- shot_moment_summary: Carter landing/disappearing
- required_environment_anchor_1: overlooking Zodangan avenue/cityscape at night
- required_subject_anchor_1: back to camera with head turned toward the action
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: size of city vs character
- camera_package_description: extreme-wide, high angle, wide lens, pull back, environment priority, low key night
- environment_subzone: overlooking Zodangan avenue/cityscape at night
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; zodanga_palace_interior; DESC_CH022_SC005; DESC_CH022_SC005_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: environment reference for the scene location
- image2_asset: zodanga palace interior

# Continuity Notes
- Scene: CH022_SC005 / SC005.
- Variant: Consistency Repair.
- Nightfall lighting transition
- Contrast between palace interior light and Zodangan avenue glow
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH022\CH022_SC005.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH022\CH022_SC005\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH022\CH022_SC005\SH003\DIALOGUE.json
