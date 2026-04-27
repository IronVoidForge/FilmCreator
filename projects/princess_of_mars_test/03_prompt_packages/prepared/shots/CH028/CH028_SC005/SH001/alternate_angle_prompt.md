# Title
SH001 Shot Prompt - Alternate Angle

# ID
CH028_SC005_SH001_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the environment reference for hudson river study. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. A man gazes through a window at a distant red planet while experiencing ethereal visions. The subject from image1 is john carter, foreground entry line within study interior, preserve readable body-to-environment scale in frame, profile left toward the scene action, Carter staring blankly. Preserve the environment from image2 monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, broad processional paths and stairs, especially study interior. medium-full, eye level, normal lens, locked off, shallow subject, low key night. Wide composition across placed for immediate spatial orientation. Carter looking out at the river. study interior. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH028_SC005; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris
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
- scene_id: CH028_SC005
- chapter_id: CH028
- shot_type: establishing_wide
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across hudson_river_study with john_carter placed for immediate spatial orientation.
- shot_size: medium_full
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: low_key_night
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: profile_left
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground entry line within study interior
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: profile left toward the scene action
- primary_subject_pose_description: Carter staring blankly
- subject_relation_summary: john_carter carries the frame alone
- scene_short_description: A man gazes through a window at a distant red planet while experiencing ethereal visions.
- shot_moment_summary: Carter looking out at the river
- required_environment_anchor_1: study interior
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: preserve readable body-to-environment scale in frame
- camera_package_description: medium-full, eye level, normal lens, locked off, shallow subject, low key night
- environment_subzone: study interior
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; hudson_river_study; DESC_CH028_SC005; DESC_CH028_SC005_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: environment reference for the scene location
- image2_asset: hudson river study

# Continuity Notes
- Scene: CH028_SC005 / SC005.
- Variant: Alternate Angle.
- Visual appearance of Mars in the night sky.
- Lighting balance between interior lamp light and exterior moonlight.
- Carter observes the Hudson River in solitude
- Resolve The Child (Vision/Sensation) -> The Child (Vision/Sensation)
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH028\CH028_SC005.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH028\CH028_SC005\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH028\CH028_SC005\SH001\DIALOGUE.json
