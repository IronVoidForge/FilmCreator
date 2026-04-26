# Title
SH003 Shot Prompt - Consistency Repair

# ID
CH002_SC002_SH003_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for apache warriors. Use image2 as the environment reference for rocky gorge nightscape. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. Apache warriors approach a dark cave entrance under starlight before fleeing in terror. The subject from image1 is apache warriors, foreground right within cliffside, preserve readable body-to-environment scale in frame, rear three-quarter left away from camera, running in panic. Preserve the environment from image2 High desert gorge with jagged cliffs and silhouetted mountain ridges., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially cliffside. full, high angle, wide lens, handheld, deep focus, low key night. Dynamic composition in clear pursuit vectors and readable movement. warriors flee and one falls. cliffside. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH002_SC002; SHOT_INDEX; DIALOGUE; apache_warriors; protagonist
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
- scene_id: CH002_SC002
- chapter_id: CH002
- shot_type: action
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: Dynamic composition in rocky_gorge_nightscape with clear pursuit vectors and readable movement for apache_warriors.
- shot_size: full
- camera_angle: high_angle
- camera_motion: handheld
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: low_key_night
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: rear_three_quarter_left
- visible_primary_subject_id: apache_warriors
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground right within cliffside
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: rear three-quarter left away from camera
- primary_subject_pose_description: running in panic
- subject_relation_summary: apache_warriors carries the frame alone
- scene_short_description: Apache warriors approach a dark cave entrance under starlight before fleeing in terror.
- shot_moment_summary: warriors flee and one falls
- required_environment_anchor_1: cliffside
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: preserve readable body-to-environment scale in frame
- camera_package_description: full, high angle, wide lens, handheld, deep focus, low key night
- environment_subzone: cliffside
- prompt_family: shot_prompt
- reference_asset_ids: apache_warriors; rocky_gorge_nightscape; DESC_CH002_SC002; DESC_CH002_SC002_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: apache warriors
- image2_role: environment reference for the scene location
- image2_asset: rocky gorge nightscape

# Continuity Notes
- Scene: CH002_SC002 / SC002.
- Variant: Consistency Repair.
- Starlight lighting consistency across all shots
- Precise synchronization of moaning sound with character reaction beats
- Panic and chaotic flight leads to a fall
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH002\CH002_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH002\CH002_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH002\CH002_SC002\SH003\DIALOGUE.json
