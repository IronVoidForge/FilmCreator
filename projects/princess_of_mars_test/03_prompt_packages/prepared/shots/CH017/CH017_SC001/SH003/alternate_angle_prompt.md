# Title
SH003 Shot Prompt - Alternate Angle

# ID
CH017_SC001_SH003_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for dejah thoris. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for thark city interior. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. An infiltrator strikes a tyrant to rescue a captive princess from her quarters. The subject from image1 is dejah thoris, foreground right within city of thark, preserve readable body-to-environment scale in frame, rear three-quarter left away from camera, Group gathers near Dejah. The subject from image2 is dejah thoris plays against sola in the same frame. Preserve the environment from image3 Features an immense circular hall and large-scale architectural elements belonging to the Jeddak's palace., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially city of thark. full, eye level, wide lens, handheld, deep focus, diffuse ambient. Dynamic composition in clear pursuit vectors and readable movement. The group flees the apartments. city of thark. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH017_SC001; SHOT_INDEX; DIALOGUE; dejah_thoris; sola; tal_hajus; tars_tarkas
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
- scene_id: CH017_SC001
- chapter_id: CH017
- shot_type: action
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: Dynamic composition in thark_city_interior with clear pursuit vectors and readable movement for dejah_thoris, The Narrator, sola.
- shot_size: full
- camera_angle: eye_level
- camera_motion: handheld
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: rear_three_quarter_left
- visible_primary_subject_id: dejah_thoris
- visible_secondary_subject_ids: sola
- primary_subject_frame_position: foreground right within city_of_thark
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: rear three-quarter left away from camera
- primary_subject_pose_description: Group gathers near Dejah
- subject_relation_summary: dejah_thoris plays against sola in the same frame
- scene_short_description: An infiltrator strikes a tyrant to rescue a captive princess from her quarters.
- shot_moment_summary: The group flees the apartments
- required_environment_anchor_1: city_of_thark
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: preserve readable body-to-environment scale in frame
- camera_package_description: full, eye level, wide lens, handheld, deep focus, diffuse ambient
- environment_subzone: city_of_thark
- prompt_family: shot_prompt
- reference_asset_ids: dejah_thoris; sola; thark_city_interior; DESC_CH017_SC001; DESC_CH017_SC001_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: dejah thoris
- image2_role: identity reference for the secondary visible subject
- image2_asset: sola
- image3_role: environment reference for the scene location
- image3_asset: thark city interior

# Continuity Notes
- Scene: CH017_SC001 / SC001.
- Variant: Alternate Angle.
- Lighting consistency within the Thark apartments
- Character positioning relative to Tal Hajus prior to the physical strike
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH017\CH017_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH017\CH017_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH017\CH017_SC001\SH003\DIALOGUE.json
