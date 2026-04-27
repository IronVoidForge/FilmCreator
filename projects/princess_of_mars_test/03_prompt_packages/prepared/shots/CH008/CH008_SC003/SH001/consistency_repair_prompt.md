# Title
SH001 Shot Prompt - Consistency Repair

# ID
CH008_SC003_SH001_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for protagonist. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for deserted martian city plaza. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. A protagonist observes a reddish-skinned woman being forcibly removed from a drifting craft by green guards. The subject from image1 is protagonist, foreground inside plaza open space, preserve readable body-to-environment scale in frame, front three-quarter right toward the scene action, protagonist looking toward craft. The subject from image2 is protagonist plays against captive woman in the same frame. Preserve the environment from image3 monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, broad processional paths and stairs, especially plaza open space. medium-close, eye level, normal lens, push in, shallow subject, diffuse ambient. Intimate composition that isolates, against to capture the beat's emotional turn. protagonist spots the reddish skin of the prisoner. plaza open space. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH008_SC003; SHOT_INDEX; DIALOGUE; protagonist; captive_woman; green_martian_warriors; sola
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: normal
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
- shot_type: reaction_closeup
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates protagonist, captive_woman against deserted_martian_city_plaza to capture the beat's emotional turn.
- shot_size: medium_close
- camera_angle: eye_level
- camera_motion: push_in
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_right
- visible_primary_subject_id: protagonist
- visible_secondary_subject_ids: captive_woman
- primary_subject_frame_position: foreground inside plaza_open_space
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: front three-quarter right toward the scene action
- primary_subject_pose_description: protagonist looking toward craft
- subject_relation_summary: protagonist plays against captive_woman in the same frame
- scene_short_description: A protagonist observes a reddish-skinned woman being forcibly removed from a drifting craft by green guards.
- shot_moment_summary: protagonist spots the reddish skin of the prisoner
- required_environment_anchor_1: plaza_open_space
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: preserve readable body-to-environment scale in frame
- camera_package_description: medium-close, eye level, normal lens, push in, shallow subject, diffuse ambient
- environment_subzone: plaza_open_space
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; captive_woman; deserted_martian_city_plaza; DESC_CH008_SC003; DESC_CH008_SC003_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: protagonist
- image2_role: identity reference for the secondary visible subject
- image2_asset: captive woman
- image3_role: environment reference for the scene location
- image3_asset: deserted martian city plaza

# Continuity Notes
- Scene: CH008_SC003 / SC003.
- Variant: Consistency Repair.
- Visual skin tone distinction: reddish-copper (captive_woman) vs. green (green_martian_warriors)
- Discovery of the prisoner
- Specificity of the silent pleading gesture motion
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH008\CH008_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH008\CH008_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH008\CH008_SC003\SH001\DIALOGUE.json
