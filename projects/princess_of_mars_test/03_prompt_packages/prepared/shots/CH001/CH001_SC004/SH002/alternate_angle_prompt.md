# Title
SH002 Shot Prompt - Alternate Angle

# ID
CH001_SC004_SH002_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for apache plateau camp. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. A soldier discovers a fallen comrade amidst arrows and flees under heavy projectile fire. The subject from image1 is john carter, foreground right within apache plateau camp skirmish zone, Individual survival vs. group skirmish scale, profile right toward the scene action, Carter kneeling by body. The subject from image2 is john carter plays against james k powell in the same frame. Preserve the environment from image3 High, expansive plateau overlooking a valley, open terrain suitable for large encampments., monumental scale, dry open Martian terrain, especially apache plateau camp skirmish zone. medium-full, low angle, wide lens, handheld, deep focus, hard directional. Readable medium composition in that keeps, together so the physical effort stays obvious. Carter lifting the body to protect it. skirmish zone. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH001_SC004; SHOT_INDEX; DIALOGUE; john_carter; james_k_powell; apache_warriors
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
- scene_id: CH001_SC004
- chapter_id: CH001
- shot_type: medium
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in apache_plateau_camp that keeps john_carter, james_k_powell together so the physical effort stays obvious.
- shot_size: medium_full
- camera_angle: low_angle
- camera_motion: handheld
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: hard_directional
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: profile_right
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: james_k_powell
- primary_subject_frame_position: foreground right within apache_plateau_camp skirmish zone
- primary_subject_scale_relation: Individual survival vs. group skirmish scale.
- primary_subject_facing_direction: profile right toward the scene action
- primary_subject_pose_description: Carter kneeling by body
- subject_relation_summary: john_carter plays against james_k_powell in the same frame
- scene_short_description: A soldier discovers a fallen comrade amidst arrows and flees under heavy projectile fire.
- shot_moment_summary: Carter lifting the body to protect it
- required_environment_anchor_1: apache_plateau_camp skirmish zone
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: Individual survival vs. group skirmish scale.
- camera_package_description: medium-full, low angle, wide lens, handheld, deep focus, hard directional
- environment_subzone: apache_plateau_camp skirmish zone
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; james_k_powell; apache_plateau_camp; DESC_CH001_SC004; DESC_CH001_SC004_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: identity reference for the secondary visible subject
- image2_asset: james k powell
- image3_role: environment reference for the scene location
- image3_asset: apache plateau camp

# Continuity Notes
- Scene: CH001_SC004 / SC004.
- Variant: Alternate Angle.
- Exact position and arrow placement on james_k_powell
- Directional trajectory of incoming apache_warriors arrow fire
- Retrieval of the body
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH001\CH001_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH001\CH001_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH001\CH001_SC004\SH002\DIALOGUE.json
