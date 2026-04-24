# Title
SH001 Shot Prompt - Alternate Angle

# ID
CH004_SC004_SH001_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for the scene location. Alternate angle with the same beat and preserved continuity.. A performer refuses to continue until fed, leading to a transfer of care in private quarters.. The subject from image1 is described character with stable costume and silhouette, foreground entry line within grand_audience_chamber, preserve readable body-to-environment scale in frame, front three-quarter right toward the scene action, Narrator standing exhausted. The subject from image2 is described character with stable costume and silhouette, The Narrator plays against tars_tarkas in the same frame. Preserve described environment with stable spatial continuity from image3, especially grand_audience_chamber threshold. massive architecture vs small human figure. medium-full, low angle, wide lens, locked off, shallow subject, high contrast ceremonial. Readable medium composition in featuring, .. The Narrator refuses further performance. Keep continuity exact across costume, silhouette, lighting, and spatial relationships.. Avoid proper nouns in the prompt body unless text is meant to appear on screen.. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH004_SC004; SHOT_INDEX; DIALOGUE; tars_tarkas; sola
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: wide
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
- scene_id: CH004_SC004
- chapter_id: CH004
- shot_type: medium
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in grand_audience_chamber featuring The Narrator, tars_tarkas.
- shot_size: medium_full
- camera_angle: low_angle
- camera_motion: locked_off
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: front_three_quarter_right
- visible_primary_subject_id: the narrator
- visible_secondary_subject_ids: tars_tarkas
- primary_subject_frame_position: foreground entry line within grand_audience_chamber
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: front three-quarter right toward the scene action
- primary_subject_pose_description: Narrator standing exhausted
- subject_relation_summary: The Narrator plays against tars_tarkas in the same frame
- scene_short_description: A performer refuses to continue until fed, leading to a transfer of care in private quarters.
- shot_moment_summary: The Narrator refuses further performance
- required_environment_anchor_1: grand_audience_chamber threshold
- required_scale_proof_detail: massive architecture vs small human figure
- camera_package_description: medium-full, low angle, wide lens, locked off, shallow subject, high contrast ceremonial
- environment_subzone: grand_audience_chamber
- prompt_family: shot_prompt
- reference_asset_ids: tars_tarkas; grand_audience_chamber; DESC_CH004_SC004; DESC_CH004_SC004_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: the narrator
- image2_role: identity reference for the secondary visible subject
- image2_asset: tars tarkas
- image3_role: environment reference for the scene location
- image3_asset: grand audience chamber

# Continuity Notes
- Scene: CH004_SC004 / SC004.
- Variant: Alternate Angle.
- The Narrator's physical state of hunger and fatigue
- Sola's height relative to the Narrator
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH004\CH004_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH004\CH004_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH004\CH004_SC004\SH001\DIALOGUE.json
