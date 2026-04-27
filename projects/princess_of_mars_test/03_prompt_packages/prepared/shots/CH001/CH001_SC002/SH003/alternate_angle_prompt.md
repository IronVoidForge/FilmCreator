# Title
SH003 Shot Prompt - Alternate Angle

# ID
CH001_SC002_SH003_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the environment reference for apache plateau camp. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. A lone rider observes suspicious valley movements and discovers fresh pony tracks on a desert trail. The subject from image1 is pony tracks, foreground inside apache plateau trail, track size vs trail width, facing directly toward camera, Horse approaching ground. Preserve the environment from image2 High, expansive plateau overlooking a valley, open terrain suitable for large encampments., monumental scale, dry open Martian terrain, especially apache plateau trail. close-up, low angle, normal lens, track, shallow subject, hard directional. Intimate composition that isolates against to capture the beat's emotional turn. Close up of fresh pony tracks in the dirt. apache plateau trail. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH001_SC002; SHOT_INDEX; DIALOGUE; john_carter
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
- scene_id: CH001_SC002
- chapter_id: CH001
- shot_type: reaction_closeup
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates john_carter against apache_plateau_camp to capture the beat's emotional turn.
- shot_size: close_up
- camera_angle: low_angle
- camera_motion: track
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: hard_directional
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground inside apache_plateau_trail
- primary_subject_scale_relation: track size vs trail width
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: Horse approaching ground
- subject_relation_summary: pony_tracks carries the frame alone
- scene_short_description: A lone rider observes suspicious valley movements and discovers fresh pony tracks on a desert trail.
- shot_moment_summary: Close up of fresh pony tracks in the dirt
- required_environment_anchor_1: apache_plateau_trail
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: track size vs trail width
- camera_package_description: close-up, low angle, normal lens, track, shallow subject, hard directional
- environment_subzone: apache_plateau_trail
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; apache_plateau_camp; DESC_CH001_SC002; DESC_CH001_SC002_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: environment reference for the scene location
- image2_asset: apache plateau camp

# Continuity Notes
- Scene: CH001_SC002 / SC002.
- Variant: Alternate Angle.
- Horse movement direction must remain consistent during pursuit
- Lighting must shift to reflect passing time during the track
- Discovery of pony tracks
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH001\CH001_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH001\CH001_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH001\CH001_SC002\SH003\DIALOGUE.json
