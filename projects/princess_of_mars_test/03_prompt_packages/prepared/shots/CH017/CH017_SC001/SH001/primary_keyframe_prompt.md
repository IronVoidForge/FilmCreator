# Title
SH001 Shot Prompt - Primary Keyframe

# ID
CH017_SC001_SH001_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for tal hajus. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for thark city interior. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. An infiltrator strikes a tyrant to rescue a captive princess from her quarters. The subject from image1 is tal hajus, foreground entry line within city of thark, low-angle height vs subject, front three-quarter right toward the scene action, Tal Hajus standing over Dejah. The subject from image2 is tal hajus plays against dejah thoris in the same frame. Preserve the environment from image3 Features an immense circular hall and large-scale architectural elements belonging to the Jeddak's palace., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially city of thark. medium-full, low angle, wide lens, locked off, deep focus, high contrast ceremonial. Readable medium composition in featuring. Tal Hajus looms over Dejah Thoris. city of thark. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH017_SC001; SHOT_INDEX; DIALOGUE; dejah_thoris; sola; tal_hajus; tars_tarkas
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: wide
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
- scene_id: CH017_SC001
- chapter_id: CH017
- shot_type: medium
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in thark_city_interior featuring tal_hajus, dejah_thoris, The Narrator.
- shot_size: medium_full
- camera_angle: low_angle
- camera_motion: locked_off
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_right
- visible_primary_subject_id: tal_hajus
- visible_secondary_subject_ids: dejah_thoris
- primary_subject_frame_position: foreground entry line within city_of_thark
- primary_subject_scale_relation: low-angle height vs subject
- primary_subject_facing_direction: front three-quarter right toward the scene action
- primary_subject_pose_description: Tal Hajus standing over Dejah
- subject_relation_summary: tal_hajus plays against dejah_thoris in the same frame
- scene_short_description: An infiltrator strikes a tyrant to rescue a captive princess from her quarters.
- shot_moment_summary: Tal Hajus looms over Dejah Thoris
- required_environment_anchor_1: city_of_thark
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: low-angle height vs subject
- camera_package_description: medium-full, low angle, wide lens, locked off, deep focus, high contrast ceremonial
- environment_subzone: city_of_thark
- prompt_family: shot_prompt
- reference_asset_ids: tal_hajus; dejah_thoris; thark_city_interior; DESC_CH017_SC001; DESC_CH017_SC001_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: tal hajus
- image2_role: identity reference for the secondary visible subject
- image2_asset: dejah thoris
- image3_role: environment reference for the scene location
- image3_asset: thark city interior

# Continuity Notes
- Scene: CH017_SC001 / SC001.
- Variant: Primary Keyframe.
- Lighting consistency within the Thark apartments
- Character positioning relative to Tal Hajus prior to the physical strike
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH017\CH017_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH017\CH017_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH017\CH017_SC001\SH001\DIALOGUE.json
