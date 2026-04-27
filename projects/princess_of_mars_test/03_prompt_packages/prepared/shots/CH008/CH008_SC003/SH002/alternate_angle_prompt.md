# Title
SH002 Shot Prompt - Alternate Angle

# ID
CH008_SC003_SH002_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the secondary visible subject. Use image2 as the environment reference for deserted martian city plaza. Use image3 as the identity reference for an additional visible subject. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. A protagonist observes a reddish-skinned woman being forcibly removed from a drifting craft by green guards. The visible subject is foreground inside drifting craft apron, preserve readable body-to-environment scale in frame, facing directly toward camera, captive woman making eye contact. The subject from image1 is captive woman plays against captive woman, protagonist in the same frame. Preserve the environment from image2 monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, broad processional paths and stairs, especially drifting craft apron. Keep one readable subject anchor: captive woman making eye contact. extreme-close-up, eye level, portrait lens, locked off, zoom subtle in, shallow subject, hard directional. Intimate composition that isolates, against to capture the beat's emotional turn. captive woman makes silent plea. drifting craft apron. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH008_SC003; SHOT_INDEX; DIALOGUE; protagonist; captive_woman; green_martian_warriors; sola
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: portrait
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: alternate_angle
- review_notes: SH002: visible primary subject id is missing for an on-screen shot.
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH008_SC003
- chapter_id: CH008
- shot_type: reaction_closeup
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates captive_woman, protagonist against deserted_martian_city_plaza to capture the beat's emotional turn.
- shot_size: extreme_close_up
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: subtle_in
- focus_strategy: shallow_subject
- lighting_style: hard_directional
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front
- visible_primary_subject_id: (none)
- visible_secondary_subject_ids: captive_woman; protagonist
- primary_subject_frame_position: foreground inside drifting_craft_apron
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: captive_woman making eye contact
- subject_relation_summary: captive_woman plays against captive_woman, protagonist in the same frame
- scene_short_description: A protagonist observes a reddish-skinned woman being forcibly removed from a drifting craft by green guards.
- shot_moment_summary: captive_woman makes silent plea
- required_environment_anchor_1: drifting_craft_apron
- required_subject_anchor_1: captive_woman making eye contact
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: preserve readable body-to-environment scale in frame
- camera_package_description: extreme-close-up, eye level, portrait lens, locked off, zoom subtle in, shallow subject, hard directional
- environment_subzone: drifting_craft_apron
- prompt_family: shot_prompt
- reference_asset_ids: captive_woman; protagonist; deserted_martian_city_plaza; DESC_CH008_SC003; DESC_CH008_SC003_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the secondary visible subject
- image1_asset: captive woman
- image2_role: environment reference for the scene location
- image2_asset: deserted martian city plaza
- image3_role: identity reference for an additional visible subject
- image3_asset: protagonist

# Continuity Notes
- Scene: CH008_SC003 / SC003.
- Variant: Alternate Angle.
- Visual skin tone distinction: reddish-copper (captive_woman) vs. green (green_martian_warriors)
- Specificity of the silent pleading gesture motion
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH008\CH008_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH008\CH008_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH008\CH008_SC003\SH002\DIALOGUE.json
