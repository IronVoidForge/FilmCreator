# Title
SH001 Shot Prompt - Alternate Angle

# ID
CH020_SC004_SH001_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for ptor farmstead. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. A rescued traveler receives food and ritualistic grooming within a domestic farmstead setting. The subject from image1 is john carter, foreground entry line within eating area, size of food vessels vs john carter, front three-quarter left toward the scene action, john carter reaching for food. The subject from image2 is john carter plays against ptor family in the same frame. Preserve the environment from image3 Clustered farmstead layout on high ground, features elevated homes and wide access roads., monumental scale, dry open Martian terrain, especially eating area. medium, eye level, normal lens, locked off, shallow subject, hard directional. Readable medium composition in featuring. john carter eating food provided by ptor family. eating area. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH020_SC004; SHOT_INDEX; DIALOGUE; john_carter; ptor_family
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
- scene_id: CH020_SC004
- chapter_id: CH020
- shot_type: medium
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in ptor_farmstead featuring john_carter, ptor_family.
- shot_size: medium
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: hard_directional
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: front_three_quarter_left
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: ptor_family
- primary_subject_frame_position: foreground entry line within eating area
- primary_subject_scale_relation: size of food vessels vs john_carter
- primary_subject_facing_direction: front three-quarter left toward the scene action
- primary_subject_pose_description: john_carter reaching for food
- subject_relation_summary: john_carter plays against ptor_family in the same frame
- scene_short_description: A rescued traveler receives food and ritualistic grooming within a domestic farmstead setting.
- shot_moment_summary: john_carter eating food provided by ptor_family
- required_environment_anchor_1: eating area
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: size of food vessels vs john_carter
- camera_package_description: medium, eye level, normal lens, locked off, shallow subject, hard directional
- environment_subzone: eating area
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; ptor_family; ptor_farmstead; DESC_CH020_SC004; DESC_CH020_SC004_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: identity reference for the secondary visible subject
- image2_asset: ptor family
- image3_role: environment reference for the scene location
- image3_asset: ptor farmstead

# Continuity Notes
- Scene: CH020_SC004 / SC004.
- Variant: Alternate Angle.
- john_carter skin must be coated in red oil
- john_carter hairstyle must be altered/cut
- Sustenance and recovery
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH020\CH020_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH020\CH020_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH020\CH020_SC004\SH001\DIALOGUE.json
