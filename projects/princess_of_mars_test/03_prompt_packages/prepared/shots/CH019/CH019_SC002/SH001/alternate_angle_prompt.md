# Title
SH001 Shot Prompt - Alternate Angle

# ID
CH019_SC002_SH001_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the environment reference for subterranean amphitheater arena. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. A prisoner meets a padwar in a ruined subterranean amphitheater cell. The subject from image1 is john carter, foreground entry line within subterranean amphitheater arena/cell, scale of ruins vs prisoner, front three-quarter left toward the scene action, Carter sitting/standing alone. Preserve the environment from image2 monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, broad processional paths and stairs, especially ruined cell wall. medium-full, eye level, wide lens, locked off, shallow subject, low key night. Readable medium composition in featuring. Carter alone in the cell. /cell. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH019_SC002; SHOT_INDEX; DIALOGUE; john_carter; kantos_kan
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: wide
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
- scene_id: CH019_SC002
- chapter_id: CH019
- shot_type: medium
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in subterranean_amphitheater_arena featuring john_carter.
- shot_size: medium_full
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: low_key_night
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_left
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground entry line within subterranean_amphitheater_arena/cell
- primary_subject_scale_relation: scale of ruins vs prisoner
- primary_subject_facing_direction: front three-quarter left toward the scene action
- primary_subject_pose_description: Carter sitting/standing alone
- subject_relation_summary: john_carter carries the frame alone
- scene_short_description: A prisoner meets a padwar in a ruined subterranean amphitheater cell.
- shot_moment_summary: Carter alone in the cell
- required_environment_anchor_1: ruined cell wall
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: scale of ruins vs prisoner
- camera_package_description: medium-full, eye level, wide lens, locked off, shallow subject, low key night
- environment_subzone: subterranean_amphitheater_arena/cell
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; subterranean_amphitheater_arena; DESC_CH019_SC002; DESC_CH019_SC002_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: environment reference for the scene location
- image2_asset: subterranean amphitheater arena

# Continuity Notes
- Scene: CH019_SC002 / SC002.
- Variant: Alternate Angle.
- Character positioning relative to cell boundaries
- Lighting consistency between subsequent scenes
- Carter's isolation in the cell
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH019\CH019_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH019\CH019_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH019\CH019_SC002\SH001\DIALOGUE.json
