# Title
SH002 Shot Prompt - Primary Keyframe

# ID
CH019_SC002_SH002_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for kantos kan. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for subterranean amphitheater arena. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. A prisoner meets a padwar in a ruined subterranean amphitheater cell. The subject from image1 is kantos kan, foreground right within subterranean amphitheater arena/cell, height of Kan vs cell opening, profile right toward the scene action, Kan enters frame. The subject from image2 is kantos kan plays against john carter in the same frame. Preserve the environment from image3 monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, broad processional paths and stairs, especially cell threshold. medium, eye level, normal lens, pan, deep focus, low key night. Readable medium composition in featuring. Kan appears at the cell. /cell. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH019_SC002; SHOT_INDEX; DIALOGUE; john_carter; kantos_kan
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: normal
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
- scene_id: CH019_SC002
- chapter_id: CH019
- shot_type: medium
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in subterranean_amphitheater_arena featuring kantos_kan, john_carter.
- shot_size: medium
- camera_angle: eye_level
- camera_motion: pan
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: low_key_night
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: profile_right
- visible_primary_subject_id: kantos_kan
- visible_secondary_subject_ids: john_carter
- primary_subject_frame_position: foreground right within subterranean_amphitheater_arena/cell
- primary_subject_scale_relation: height of Kan vs cell opening
- primary_subject_facing_direction: profile right toward the scene action
- primary_subject_pose_description: Kan enters frame
- subject_relation_summary: kantos_kan plays against john_carter in the same frame
- scene_short_description: A prisoner meets a padwar in a ruined subterranean amphitheater cell.
- shot_moment_summary: Kan appears at the cell
- required_environment_anchor_1: cell threshold
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: height of Kan vs cell opening
- camera_package_description: medium, eye level, normal lens, pan, deep focus, low key night
- environment_subzone: subterranean_amphitheater_arena/cell
- prompt_family: shot_prompt
- reference_asset_ids: kantos_kan; john_carter; subterranean_amphitheater_arena; DESC_CH019_SC002; DESC_CH019_SC002_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: kantos kan
- image2_role: identity reference for the secondary visible subject
- image2_asset: john carter
- image3_role: environment reference for the scene location
- image3_asset: subterranean amphitheater arena

# Continuity Notes
- Scene: CH019_SC002 / SC002.
- Variant: Primary Keyframe.
- Character positioning relative to cell boundaries
- Lighting consistency between subsequent scenes
- Kantos Kan arrives
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH019\CH019_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH019\CH019_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH019\CH019_SC002\SH002\DIALOGUE.json
