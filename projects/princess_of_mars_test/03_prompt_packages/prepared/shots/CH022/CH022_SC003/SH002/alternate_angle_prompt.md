# Title
SH002 Shot Prompt - Alternate Angle

# ID
CH022_SC003_SH002_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for dejah thoris. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for zodanga palace interior. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. A wounded man finds a woman in a private palace corridor, only to be met with tragic news. The subject from image1 is dejah thoris, foreground right within zodanga palace interior antechamber area, distance between faces, facing directly toward camera, eye contact. The subject from image2 is dejah thoris plays against john carter in the same frame. Preserve the environment from image3 monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, broad processional paths and stairs, especially antechamber threshold. Keep one readable subject anchor: eye contact. medium, eye level, normal lens, locked off, zoom subtle in, deep focus, soft even. Readable medium composition in featuring. The look of recognition and shared love. antechamber area. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH022_SC003; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: normal
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: alternate_angle
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH022_SC003
- chapter_id: CH022
- shot_type: medium
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in zodanga_palace_interior featuring dejah_thoris, john_carter.
- shot_size: medium
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: subtle_in
- focus_strategy: deep_focus
- lighting_style: soft_even
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: front
- visible_primary_subject_id: dejah_thoris
- visible_secondary_subject_ids: john_carter
- primary_subject_frame_position: foreground right within zodanga_palace_interior antechamber area
- primary_subject_scale_relation: distance between faces
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: eye contact
- subject_relation_summary: dejah_thoris plays against john_carter in the same frame
- scene_short_description: A wounded man finds a woman in a private palace corridor, only to be met with tragic news.
- shot_moment_summary: The look of recognition and shared love
- required_environment_anchor_1: antechamber threshold
- required_subject_anchor_1: eye contact
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: distance between faces
- camera_package_description: medium, eye level, normal lens, locked off, zoom subtle in, deep focus, soft even
- environment_subzone: zodanga_palace_interior antechamber area
- prompt_family: shot_prompt
- reference_asset_ids: dejah_thoris; john_carter; zodanga_palace_interior; DESC_CH022_SC003; DESC_CH022_SC003_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: dejah thoris
- image2_role: identity reference for the secondary visible subject
- image2_asset: john carter
- image3_role: environment reference for the scene location
- image3_asset: zodanga palace interior

# Continuity Notes
- Scene: CH022_SC003 / SC003.
- Variant: Alternate Angle.
- john_carter physical condition: sweat and blood from recent fight
- dejah_thoris emotional state: tearful makeup and facial distress
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH022\CH022_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH022\CH022_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH022\CH022_SC003\SH002\DIALOGUE.json
