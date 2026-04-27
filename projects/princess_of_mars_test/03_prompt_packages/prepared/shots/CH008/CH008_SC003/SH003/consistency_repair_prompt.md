# Title
SH003 Shot Prompt - Consistency Repair

# ID
CH008_SC003_SH003_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for green martian warriors. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for deserted martian city plaza. Use image4 as the identity reference for an additional visible subject. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. A protagonist observes a reddish-skinned woman being forcibly removed from a drifting craft by green guards. The subject from image1 is green martian warriors, foreground right within plaza open space, preserve readable body-to-environment scale in frame, profile left toward the scene action, guards pulling captive woman. The subject from image2 is green martian warriors plays against captive woman, protagonist in the same frame. Preserve the environment from image3 monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, broad processional paths and stairs, especially plaza open space. medium, eye level, wide lens, track, deep focus, diffuse ambient. Readable medium composition in featuring. guards drag woman away. plaza open space. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH008_SC003; SHOT_INDEX; DIALOGUE; protagonist; captive_woman; green_martian_warriors; sola
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: wide
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: consistency_repair
- review_notes: Prompt body is missing the required subject anchor for an on-screen shot.
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH008_SC003
- chapter_id: CH008
- shot_type: medium
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in deserted_martian_city_plaza featuring green_martian_warriors, captive_woman, protagonist.
- shot_size: medium
- camera_angle: eye_level
- camera_motion: track
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: profile_left
- visible_primary_subject_id: green_martian_warriors
- visible_secondary_subject_ids: captive_woman; protagonist
- primary_subject_frame_position: foreground right within plaza_open_space
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: profile left toward the scene action
- primary_subject_pose_description: guards pulling captive_woman
- subject_relation_summary: green_martian_warriors plays against captive_woman, protagonist in the same frame
- scene_short_description: A protagonist observes a reddish-skinned woman being forcibly removed from a drifting craft by green guards.
- shot_moment_summary: guards drag woman away
- required_environment_anchor_1: plaza_open_space
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: preserve readable body-to-environment scale in frame
- camera_package_description: medium, eye level, wide lens, track, deep focus, diffuse ambient
- environment_subzone: plaza_open_space
- prompt_family: shot_prompt
- reference_asset_ids: green_martian_warriors; captive_woman; protagonist; deserted_martian_city_plaza; DESC_CH008_SC003; DESC_CH008_SC003_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: green martian warriors
- image2_role: identity reference for the secondary visible subject
- image2_asset: captive woman
- image3_role: environment reference for the scene location
- image3_asset: deserted martian city plaza
- image4_role: identity reference for an additional visible subject
- image4_asset: protagonist

# Continuity Notes
- Scene: CH008_SC003 / SC003.
- Variant: Consistency Repair.
- Visual skin tone distinction: reddish-copper (captive_woman) vs. green (green_martian_warriors)
- The Missed Connection
- Specificity of the silent pleading gesture motion
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH008\CH008_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH008\CH008_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH008\CH008_SC003\SH003\DIALOGUE.json
