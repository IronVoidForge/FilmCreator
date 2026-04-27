# Title
SH001 Shot Prompt - Consistency Repair

# ID
CH013_SC001_SH001_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for green martian warriors. Use image2 as the environment reference for green martian city complex. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. A human man uses gentle authority to tame large, aggressive Martian beasts within a city complex. The subject from image1 is thoat, midground inside training arena, thoat height vs warrior height, front three-quarter left toward the scene action, beast lunging. Preserve the environment from image2 Features wide thoroughfares, central leadership hubs, and large-scale enclosures/pens for beasts., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially training arena. wide, low angle, wide lens, handheld, deep focus, diffuse ambient. Wide composition across placed for immediate spatial orientation. wild thoats thrashing in the arena. training arena. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH013_SC001; SHOT_INDEX; DIALOGUE; john_carter; tars_tarkas; green_martian_warriors
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
- scene_id: CH013_SC001
- chapter_id: CH013
- shot_type: establishing_wide
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across green_martian_city_complex with green_martian_warriors placed for immediate spatial orientation.
- shot_size: wide
- camera_angle: low_angle
- camera_motion: handheld
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_left
- visible_primary_subject_id: green_martian_warriors
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: midground inside training_arena
- primary_subject_scale_relation: thoat height vs warrior height
- primary_subject_facing_direction: front three-quarter left toward the scene action
- primary_subject_pose_description: beast lunging
- subject_relation_summary: thoat carries the frame alone
- scene_short_description: A human man uses gentle authority to tame large, aggressive Martian beasts within a city complex.
- shot_moment_summary: wild thoats thrashing in the arena
- required_environment_anchor_1: training_arena
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: thoat height vs warrior height
- camera_package_description: wide, low angle, wide lens, handheld, deep focus, diffuse ambient
- environment_subzone: training_arena
- prompt_family: shot_prompt
- reference_asset_ids: green_martian_warriors; green_martian_city_complex; DESC_CH013_SC001; DESC_CH013_SC001_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: green martian warriors
- image2_role: environment reference for the scene location
- image2_asset: green martian city complex

# Continuity Notes
- Scene: CH013_SC001 / SC001.
- Variant: Consistency Repair.
- Physical behavior shift of thoats from wild to docile
- Carter's training attire consistency
- Specific hand/body movements used in taming process
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH013\CH013_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH013\CH013_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH013\CH013_SC001\SH001\DIALOGUE.json
