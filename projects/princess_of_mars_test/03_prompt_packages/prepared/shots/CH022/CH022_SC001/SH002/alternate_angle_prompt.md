# Title
SH002 Shot Prompt - Alternate Angle

# ID
CH022_SC001_SH002_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for dejah thoris. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for zodanga palace interior. Use image4 as the identity reference for an additional visible subject. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. A hidden observer watches a royal woman declare her marriage intent within a private chamber. The subject from image1 is dejah thoris, foreground right within zodanga palace interior, regal attire vs chamber scale, front three-quarter right toward the scene action, door opens. The subject from image2 is dejah thoris plays against than kosis, sab than in the same frame. Preserve the environment from image3 monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, broad processional paths and stairs, especially chamber door. medium, eye level, normal lens, pan, deep focus, high contrast ceremonial. Readable medium composition in featuring. Dejah Thoris enters the room. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH022_SC001; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris; than_kosis; sab_than
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
- scene_id: CH022_SC001
- chapter_id: CH022
- shot_type: medium
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in zodanga_palace_interior featuring dejah_thoris, than_kosis, sab_than.
- shot_size: medium
- camera_angle: eye_level
- camera_motion: pan
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: front_three_quarter_right
- visible_primary_subject_id: dejah_thoris
- visible_secondary_subject_ids: than_kosis; sab_than
- primary_subject_frame_position: foreground right within zodanga_palace_interior
- primary_subject_scale_relation: regal attire vs chamber scale
- primary_subject_facing_direction: front three-quarter right toward the scene action
- primary_subject_pose_description: door opens
- subject_relation_summary: dejah_thoris plays against than_kosis, sab_than in the same frame
- scene_short_description: A hidden observer watches a royal woman declare her marriage intent within a private chamber.
- shot_moment_summary: Dejah Thoris enters the room
- required_environment_anchor_1: chamber door
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: regal attire vs chamber scale
- camera_package_description: medium, eye level, normal lens, pan, deep focus, high contrast ceremonial
- environment_subzone: zodanga_palace_interior
- prompt_family: shot_prompt
- reference_asset_ids: dejah_thoris; than_kosis; sab_than; zodanga_palace_interior; DESC_CH022_SC001; DESC_CH022_SC001_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: dejah thoris
- image2_role: identity reference for the secondary visible subject
- image2_asset: than kosis
- image3_role: environment reference for the scene location
- image3_asset: zodanga palace interior
- image4_role: identity reference for an additional visible subject
- image4_asset: sab than

# Continuity Notes
- Scene: CH022_SC001 / SC001.
- Variant: Alternate Angle.
- Carter's physical position relative to the tapestry edge
- Dejah Thoris's regal attire and posture consistency
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH022\CH022_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH022\CH022_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH022\CH022_SC001\SH002\DIALOGUE.json
