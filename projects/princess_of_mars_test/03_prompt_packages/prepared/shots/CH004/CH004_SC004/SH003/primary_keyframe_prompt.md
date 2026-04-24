# Title
SH003 Shot Prompt - Primary Keyframe

# ID
CH004_SC004_SH003_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the environment reference for the scene location. Primary keyframe with balanced composition and clear subject placement.. A performer refuses to continue until fed, leading to a transfer of care in private quarters.. The subject from image1 is described character with stable costume and silhouette, foreground inside private_quarters, preserve readable body-to-environment scale in frame, front three-quarter left toward the scene action, Sola approaching with food. Preserve described environment with stable spatial continuity from image2, especially private_quarters. proximity of Sola to Narrator. medium-close, eye level, portrait lens, push in, zoom subtle in, shallow subject, soft even. Intimate composition that ites, against private quarters to capture the beat's emotional turn.. Sola provides sustenance. private_quarters. Keep continuity exact across costume, silhouette, lighting, and spatial relationships.. Avoid proper nouns in the prompt body unless text is meant to appear on screen.. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH004_SC004; SHOT_INDEX; DIALOGUE; tars_tarkas; sola
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: portrait
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
- scene_id: CH004_SC004
- chapter_id: CH004
- shot_type: reaction_closeup
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Close framing that ites reaction and emotional emphasis.
- composition: Intimate composition that isolates sola, The Narrator against private quarters to capture the beat's emotional turn.
- shot_size: medium_close
- camera_angle: eye_level
- camera_motion: push_in
- zoom_behavior: subtle_in
- focus_strategy: shallow_subject
- lighting_style: soft_even
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_left
- visible_primary_subject_id: sola
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground inside private_quarters
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: front three-quarter left toward the scene action
- primary_subject_pose_description: Sola approaching with food
- subject_relation_summary: sola plays against The Narrator in the same frame
- scene_short_description: A performer refuses to continue until fed, leading to a transfer of care in private quarters.
- shot_moment_summary: Sola provides sustenance
- required_environment_anchor_1: private_quarters
- required_scale_proof_detail: proximity of Sola to Narrator
- camera_package_description: medium-close, eye level, portrait lens, push in, zoom subtle in, shallow subject, soft even
- environment_subzone: private_quarters
- prompt_family: shot_prompt
- reference_asset_ids: sola; grand_audience_chamber; DESC_CH004_SC004; DESC_CH004_SC004_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: sola
- image2_role: environment reference for the scene location
- image2_asset: grand audience chamber

# Continuity Notes
- Scene: CH004_SC004 / SC004.
- Variant: Primary Keyframe.
- The Narrator's physical state of hunger and fatigue
- Sola's height relative to the Narrator
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH004\CH004_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH004\CH004_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH004\CH004_SC004\SH003\DIALOGUE.json
