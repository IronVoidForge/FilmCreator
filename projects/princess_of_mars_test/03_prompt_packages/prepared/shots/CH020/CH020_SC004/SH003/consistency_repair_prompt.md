# Title
SH003 Shot Prompt - Consistency Repair

# ID
CH020_SC004_SH003_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for ptor family. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for ptor farmstead. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. A rescued traveler receives food and ritualistic grooming within a domestic farmstead setting. The subject from image1 is ptor family, foreground inside grooming station, Domestic scale; human-sized interactions within metal shaft structures, rear three-quarter left away from camera, blade touching hair. The subject from image2 is ptor family plays against john carter in the same frame. Preserve the environment from image3 Clustered farmstead layout on high ground, features elevated homes and wide access roads., monumental scale, dry open Martian terrain, especially grooming station. Keep one readable subject anchor: close proximity to head. extreme-close-up, high angle, telephoto lens, locked off, shallow subject, hard directional. Intimate composition that isolates, against to capture the beat's emotional turn. cutting of hair. grooming station. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH020_SC004; SHOT_INDEX; DIALOGUE; john_carter; ptor_family
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
- scene_id: CH020_SC004
- chapter_id: CH020
- shot_type: reaction_closeup
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates ptor_family, john_carter against ptor_farmstead to capture the beat's emotional turn.
- shot_size: extreme_close_up
- camera_angle: high_angle
- camera_motion: locked_off
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: hard_directional
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: rear_three_quarter_left
- visible_primary_subject_id: ptor_family
- visible_secondary_subject_ids: john_carter
- primary_subject_frame_position: foreground inside grooming station
- primary_subject_scale_relation: Domestic scale; human-sized interactions within metal shaft structures.
- primary_subject_facing_direction: rear three-quarter left away from camera
- primary_subject_pose_description: blade touching hair
- subject_relation_summary: ptor_family plays against john_carter in the same frame
- scene_short_description: A rescued traveler receives food and ritualistic grooming within a domestic farmstead setting.
- shot_moment_summary: cutting of hair
- required_environment_anchor_1: grooming station
- required_subject_anchor_1: close proximity to head
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: Domestic scale; human-sized interactions within metal shaft structures.
- camera_package_description: extreme-close-up, high angle, telephoto lens, locked off, shallow subject, hard directional
- environment_subzone: grooming station
- prompt_family: shot_prompt
- reference_asset_ids: ptor_family; john_carter; ptor_farmstead; DESC_CH020_SC004; DESC_CH020_SC004_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: ptor family
- image2_role: identity reference for the secondary visible subject
- image2_asset: john carter
- image3_role: environment reference for the scene location
- image3_asset: ptor farmstead

# Continuity Notes
- Scene: CH020_SC004 / SC004.
- Variant: Consistency Repair.
- john_carter skin must be coated in red oil
- john_carter hairstyle must be altered/cut
- Final preparation
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH020\CH020_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH020\CH020_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH020\CH020_SC004\SH003\DIALOGUE.json
