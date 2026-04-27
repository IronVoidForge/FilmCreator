# Title
SH002 Shot Prompt - Primary Keyframe

# ID
CH001_SC003_SH002_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for apache plateau camp. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. A lone man charges a massive plateau encampment with revolvers, inciting chaos among hundreds. The subject from image1 is john carter, foreground inside open plateau floor, preserve readable body-to-environment scale in frame, front three-quarter right toward the scene action, running charge. The subject from image2 is john carter plays against apache warriors in the same frame. Preserve the environment from image3 High, expansive plateau overlooking a valley, open terrain suitable for large encampments., monumental scale, dry open Martian terrain, especially open plateau floor. ammunition count/shell casings. medium-close, low angle, normal lens, handheld, shallow subject, high contrast ceremonial. Intimate composition that isolates, against to capture the beat's emotional turn. Carter fires revolvers during charge. open plateau floor. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH001_SC003; SHOT_INDEX; DIALOGUE; john_carter; apache_warriors
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
- scene_id: CH001_SC003
- chapter_id: CH001
- shot_type: reaction_closeup
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates john_carter, apache_warriors against apache_plateau_camp to capture the beat's emotional turn.
- shot_size: medium_close
- camera_angle: low_angle
- camera_motion: handheld
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_right
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: apache_warriors
- primary_subject_frame_position: foreground inside open plateau floor
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: front three-quarter right toward the scene action
- primary_subject_pose_description: running charge
- subject_relation_summary: john_carter plays against apache_warriors in the same frame
- scene_short_description: A lone man charges a massive plateau encampment with revolvers, inciting chaos among hundreds.
- shot_moment_summary: Carter fires revolvers during charge
- required_environment_anchor_1: open plateau floor
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: ammunition count/shell casings
- camera_package_description: medium-close, low angle, normal lens, handheld, shallow subject, high contrast ceremonial
- environment_subzone: open plateau floor
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; apache_warriors; apache_plateau_camp; DESC_CH001_SC003; DESC_CH001_SC003_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: identity reference for the secondary visible subject
- image2_asset: apache warriors
- image3_role: environment reference for the scene location
- image3_asset: apache plateau camp

# Continuity Notes
- Scene: CH001_SC003 / SC003.
- Variant: Primary Keyframe.
- Total count of apache_warriors visible in wide shots
- Revolver ammunition depletion tracking
- Dust cloud density from horse movement
- The violent charge
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH001\CH001_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH001\CH001_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH001\CH001_SC003\SH002\DIALOGUE.json
