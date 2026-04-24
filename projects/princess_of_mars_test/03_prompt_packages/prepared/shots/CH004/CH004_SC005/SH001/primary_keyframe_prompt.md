# Title
SH001 Shot Prompt - Primary Keyframe

# ID
CH004_SC005_SH001_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the environment reference for the scene location. Primary keyframe with balanced composition and clear subject placement.. A character is led into a decorated sleeping chamber to encounter a strange ten-legged creature.. The subject from image1 is described character with stable costume and silhouette, foreground entry line within chamber entrance, decor size relative to characters, profile left toward the scene action, characters approaching door. Preserve described environment with stable spatial continuity from image2, especially chamber entrance. decor size relative to characters. medium-full, eye level, wide lens, track, deep focus, low key night. Readable medium composition in featuring, .. sola leads narrator into the chamber. chamber entrance. Keep continuity exact across costume, silhouette, lighting, and spatial relationships.. Avoid proper nouns in the prompt body unless text is meant to appear on screen.. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH004_SC005; SHOT_INDEX; DIALOGUE; sola
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: wide
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: primary_keyframe
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH004_SC005
- chapter_id: CH004
- shot_type: medium
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in martian_sleeping_chamber featuring sola, The Narrator.
- shot_size: medium_full
- camera_angle: eye_level
- camera_motion: track
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: low_key_night
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: profile_left
- visible_primary_subject_id: sola
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground entry line within chamber entrance
- primary_subject_scale_relation: decor size relative to characters
- primary_subject_facing_direction: profile left toward the scene action
- primary_subject_pose_description: characters approaching door
- subject_relation_summary: sola plays against The Narrator in the same frame
- scene_short_description: A character is led into a decorated sleeping chamber to encounter a strange ten-legged creature.
- shot_moment_summary: sola leads narrator into the chamber
- required_environment_anchor_1: chamber entrance
- required_scale_proof_detail: decor size relative to characters
- camera_package_description: medium-full, eye level, wide lens, track, deep focus, low key night
- environment_subzone: chamber entrance
- prompt_family: shot_prompt
- reference_asset_ids: sola; martian_sleeping_chamber; DESC_CH004_SC005; DESC_CH004_SC005_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: sola
- image2_role: environment reference for the scene location
- image2_asset: martian sleeping chamber

# Continuity Notes
- Scene: CH004_SC005 / SC005.
- Variant: Primary Keyframe.
- Small Martian Creature movement and physical appearance
- Ambient light levels within the chamber
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH004\CH004_SC005.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH004\CH004_SC005\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH004\CH004_SC005\SH001\DIALOGUE.json
