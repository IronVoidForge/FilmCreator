# Title
SH001 Shot Prompt - Primary Keyframe

# ID
CH008_SC001_SH001_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for protagonist. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for deserted martian city plaza. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. A sudden retreat by local warriors precedes a massive aerial assault on a deserted city. The subject from image1 is protagonist, foreground entry line within deserted martian city rooftops, human scale vs building height, front three-quarter right toward the scene action, walking calmly. The subject from image2 is protagonist plays against sola in the same frame. Preserve the environment from image3 monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, broad processional paths and stairs, especially deserted martian city rooftops. medium-full, eye level, normal lens, track, shallow subject, diffuse ambient. Wide composition across placed for immediate spatial orientation. protagonist and sola walking home. deserted martian city rooftops. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH008_SC001; SHOT_INDEX; DIALOGUE; protagonist; sola; green_martian_warriors
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: normal
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: primary_keyframe
- review_notes: Environment reference conflict: prompt variables align more with `deserted_martian_city` than bound `deserted_martian_city_plaza`.; Prompt body is missing the required subject anchor for an on-screen shot.
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH008_SC001
- chapter_id: CH008
- shot_type: establishing_wide
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across deserted_martian_city_plaza with protagonist, sola placed for immediate spatial orientation.
- shot_size: medium_full
- camera_angle: eye_level
- camera_motion: track
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_right
- visible_primary_subject_id: protagonist
- visible_secondary_subject_ids: sola
- primary_subject_frame_position: foreground entry line within deserted_martian_city rooftops
- primary_subject_scale_relation: human scale vs building height
- primary_subject_facing_direction: front three-quarter right toward the scene action
- primary_subject_pose_description: walking calmly
- subject_relation_summary: protagonist plays against sola in the same frame
- scene_short_description: A sudden retreat by local warriors precedes a massive aerial assault on a deserted city.
- shot_moment_summary: protagonist and sola walking home
- required_environment_anchor_1: deserted_martian_city rooftops
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: human scale vs building height
- camera_package_description: medium-full, eye level, normal lens, track, shallow subject, diffuse ambient
- environment_subzone: deserted_martian_city rooftops
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; sola; deserted_martian_city_plaza; DESC_CH008_SC001; DESC_CH008_SC001_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: protagonist
- image2_role: identity reference for the secondary visible subject
- image2_asset: sola
- image3_role: environment reference for the scene location
- image3_asset: deserted martian city plaza

# Continuity Notes
- Scene: CH008_SC001 / SC001.
- Variant: Primary Keyframe.
- Position of protagonist and sola relative to deserted_martian_city structures
- Routine travel of protagonist and sola
- Directional vector of gray vessels vs. green Martian fire trajectories
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH008\CH008_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH008\CH008_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH008\CH008_SC001\SH001\DIALOGUE.json
