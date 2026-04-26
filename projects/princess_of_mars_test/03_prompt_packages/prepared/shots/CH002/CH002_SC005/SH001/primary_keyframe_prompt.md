# Title
SH001 Shot Prompt - Primary Keyframe

# ID
CH002_SC005_SH001_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for protagonist. Use image2 as the environment reference for rocky gorge nightscape. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. A naked man flees a rocky gorge into the desert night before being pulled toward Mars. The subject from image1 is protagonist, midground inside rocky gorge rim, human vs gorge size, rear three-quarter left away from camera, running from darkness. Preserve the environment from image2 High desert gorge with jagged cliffs and silhouetted mountain ridges., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially rocky gorge rim. wide, low angle, wide lens, track, deep focus, low key night. Dynamic composition in clear pursuit vectors and readable movement. protagonist running from cave into night. rocky gorge rim. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH002_SC005; SHOT_INDEX; DIALOGUE; protagonist
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: wide
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: primary_keyframe
- review_notes: SH001: subject anchor is missing or not body/detail-specific enough.; Prompt body is using a non-body/detail subject anchor.
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH002_SC005
- chapter_id: CH002
- shot_type: action
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: Dynamic composition in rocky_gorge_nightscape with clear pursuit vectors and readable movement for protagonist.
- shot_size: wide
- camera_angle: low_angle
- camera_motion: track
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: low_key_night
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: rear_three_quarter_left
- visible_primary_subject_id: protagonist
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: midground inside rocky_gorge_rim
- primary_subject_scale_relation: human vs gorge size
- primary_subject_facing_direction: rear three-quarter left away from camera
- primary_subject_pose_description: running from darkness
- subject_relation_summary: protagonist carries the frame alone
- scene_short_description: A naked man flees a rocky gorge into the desert night before being pulled toward Mars.
- shot_moment_summary: protagonist running from cave into night
- required_environment_anchor_1: rocky_gorge_rim
- required_subject_anchor_1: cave mouth
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: human vs gorge size
- camera_package_description: wide, low angle, wide lens, track, deep focus, low key night
- environment_subzone: rocky_gorge_rim
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; rocky_gorge_nightscape; DESC_CH002_SC005; DESC_CH002_SC005_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: protagonist
- image2_role: environment reference for the scene location
- image2_asset: rocky gorge nightscape

# Continuity Notes
- Scene: CH002_SC005 / SC005.
- Variant: Primary Keyframe.
- Fixed celestial position of Mars relative to horizon/protagonist
- Visual texture and particle behavior of the transportation effect
- Fleeing the cave into the night
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH002\CH002_SC005.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH002\CH002_SC005\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH002\CH002_SC005\SH001\DIALOGUE.json
