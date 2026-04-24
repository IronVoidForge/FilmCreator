# Title
SH002 Shot Prompt - Primary Keyframe

# ID
CH004_SC004_SH002_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for the scene location. Primary keyframe with balanced composition and clear subject placement.. A performer refuses to continue until fed, leading to a transfer of care in private quarters.. The subject from image1 is described character with stable costume and silhouette, foreground right within grand_audience_chamber, height difference between sola and narrator, profile left toward the scene action, Tars Tarkas speaking. The subject from image2 is described character with stable costume and silhouette, tars_tarkas plays against sola, The Narrator in the same frame. Preserve described environment with stable spatial continuity from image3, especially grand_audience_chamber. height difference between sola and narrator. medium, eye level, normal lens, pan, rack focus, diffuse ambient. Readable medium composition in featuring, .. Tars Tarkas assigns Sola to the Narrator. Keep continuity exact across costume, silhouette, lighting, and spatial relationships.. Avoid proper nouns in the prompt body unless text is meant to appear on screen.. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH004_SC004; SHOT_INDEX; DIALOGUE; tars_tarkas; sola
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: normal
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
- shot_type: medium
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in grand_audience_chamber featuring tars_tarkas, sola, The Narrator.
- shot_size: medium
- camera_angle: eye_level
- camera_motion: pan
- zoom_behavior: none
- focus_strategy: rack_focus
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: profile_left
- visible_primary_subject_id: tars_tarkas
- visible_secondary_subject_ids: sola
- primary_subject_frame_position: foreground right within grand_audience_chamber
- primary_subject_scale_relation: height difference between sola and narrator
- primary_subject_facing_direction: profile left toward the scene action
- primary_subject_pose_description: Tars Tarkas speaking
- subject_relation_summary: tars_tarkas plays against sola, The Narrator in the same frame
- scene_short_description: A performer refuses to continue until fed, leading to a transfer of care in private quarters.
- shot_moment_summary: Tars Tarkas assigns Sola to the Narrator
- required_environment_anchor_1: grand_audience_chamber
- required_scale_proof_detail: height difference between sola and narrator
- camera_package_description: medium, eye level, normal lens, pan, rack focus, diffuse ambient
- environment_subzone: grand_audience_chamber
- prompt_family: shot_prompt
- reference_asset_ids: tars_tarkas; sola; grand_audience_chamber; DESC_CH004_SC004; DESC_CH004_SC004_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: tars tarkas
- image2_role: identity reference for the secondary visible subject
- image2_asset: sola
- image3_role: environment reference for the scene location
- image3_asset: grand audience chamber

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
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH004\CH004_SC004\SH002\DIALOGUE.json
