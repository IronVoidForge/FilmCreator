# Title
SH003 Shot Prompt - Alternate Angle

# ID
CH001_SC003_SH003_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for apache warriors. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for apache plateau camp. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. A lone man charges a massive plateau encampment with revolvers, inciting chaos among hundreds. The subject from image1 is apache warriors, midground inside tepee clusters, preserve readable body-to-environment scale in frame, profile left toward the scene action, sudden panic. The subject from image2 is apache warriors plays against john carter in the same frame. Preserve the environment from image3 High, expansive plateau overlooking a valley, open terrain suitable for large encampments., monumental scale, dry open Martian terrain, especially apache plateau camp tepees. dust clouds from horses. wide, eye level, ultra-wide lens, handheld, environment priority, high contrast ceremonial. Wide composition across placed for immediate spatial orientation. Warriors reacting to gunfire. tepee clusters. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH001_SC003; SHOT_INDEX; DIALOGUE; john_carter; apache_warriors
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: ultra_wide
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
- scene_id: CH001_SC003
- chapter_id: CH001
- shot_type: establishing_wide
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across apache_plateau_camp with apache_warriors, john_carter placed for immediate spatial orientation.
- shot_size: wide
- camera_angle: eye_level
- camera_motion: handheld
- zoom_behavior: none
- focus_strategy: environment_priority
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: profile_left
- visible_primary_subject_id: apache_warriors
- visible_secondary_subject_ids: john_carter
- primary_subject_frame_position: midground inside tepee clusters
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: profile left toward the scene action
- primary_subject_pose_description: sudden panic
- subject_relation_summary: apache_warriors plays against john_carter in the same frame
- scene_short_description: A lone man charges a massive plateau encampment with revolvers, inciting chaos among hundreds.
- shot_moment_summary: Warriors reacting to gunfire
- required_environment_anchor_1: apache_plateau_camp tepees
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: dust clouds from horses
- camera_package_description: wide, eye level, ultra-wide lens, handheld, environment priority, high contrast ceremonial
- environment_subzone: tepee clusters
- prompt_family: shot_prompt
- reference_asset_ids: apache_warriors; john_carter; apache_plateau_camp; DESC_CH001_SC003; DESC_CH001_SC003_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: apache warriors
- image2_role: identity reference for the secondary visible subject
- image2_asset: john carter
- image3_role: environment reference for the scene location
- image3_asset: apache plateau camp

# Continuity Notes
- Scene: CH001_SC003 / SC003.
- Variant: Alternate Angle.
- Total count of apache_warriors visible in wide shots
- Revolver ammunition depletion tracking
- Dust cloud density from horse movement
- Mass confusion
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH001\CH001_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH001\CH001_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH001\CH001_SC003\SH003\DIALOGUE.json
