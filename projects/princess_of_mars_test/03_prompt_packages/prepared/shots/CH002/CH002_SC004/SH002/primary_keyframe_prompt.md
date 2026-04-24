# Title
SH002 Shot Prompt - Primary Keyframe

# ID
CH002_SC004_SH002_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the environment reference for the scene location. Primary keyframe with balanced composition and clear subject placement.. A naked man flees a dark cavern into the vast, moonlit Arizona mountain night.. The subject from image1 is described character with stable costume and silhouette, foreground right within Cave Interior (Transitioning), silhouette against moonlight, profile right toward the scene action, silhouette at cave mouth. Preserve described environment with stable spatial continuity from image2, especially Cave Interior (Transitioning). silhouette against moonlight. full, eye level, ultra-wide lens, push in, rack focus, high contrast ceremonial. Readable medium composition in featuring .. protagonist crossing the threshold. Cave Interior (Transitioning). Keep continuity exact across costume, silhouette, lighting, and spatial relationships.. Avoid proper nouns in the prompt body unless text is meant to appear on screen.. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH002_SC004; SHOT_INDEX; DIALOGUE; protagonist
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: ultra_wide
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
- scene_id: CH002_SC004
- chapter_id: CH002
- shot_type: medium
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in rocky_gorge_canyon featuring protagonist.
- shot_size: full
- camera_angle: eye_level
- camera_motion: push_in
- zoom_behavior: none
- focus_strategy: rack_focus
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: profile_right
- visible_primary_subject_id: protagonist
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground right within Cave Interior (Transitioning)
- primary_subject_scale_relation: silhouette against moonlight
- primary_subject_facing_direction: profile right toward the scene action
- primary_subject_pose_description: silhouette at cave mouth
- subject_relation_summary: protagonist carries the frame alone
- scene_short_description: A naked man flees a dark cavern into the vast, moonlit Arizona mountain night.
- shot_moment_summary: protagonist crossing the threshold
- required_environment_anchor_1: Cave Interior (Transitioning)
- required_scale_proof_detail: silhouette against moonlight
- camera_package_description: full, eye level, ultra-wide lens, push in, rack focus, high contrast ceremonial
- environment_subzone: Cave Interior (Transitioning)
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; rocky_gorge_canyon; DESC_CH002_SC004; DESC_CH002_SC004_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: protagonist
- image2_role: environment reference for the scene location
- image2_asset: rocky gorge canyon

# Continuity Notes
- Scene: CH002_SC004 / SC004.
- Variant: Primary Keyframe.
- Protagonist nudity and physical state across light level shifts
- Physical condition post-gas paralysis
- Crossing the threshold from cave to canyon
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH002\CH002_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH002\CH002_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH002\CH002_SC004\SH002\DIALOGUE.json
