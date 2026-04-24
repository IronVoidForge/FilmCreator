# Title
SH003 Shot Prompt - Consistency Repair

# ID
CH004_SC003_SH003_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the environment reference for the scene location. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships.. A man punches a warrior in a massive marble hall then performs a long distance leap.. The subject from image1 is described character with stable costume and silhouette, midground inside grand_audience_chamber plaza, distance traveled across marble floor, facing directly toward camera, Narrator crouched for jump. Preserve described environment with stable spatial continuity from image2, especially grand_audience_chamber plaza. distance traveled across marble floor. wide, low angle, ultra-wide lens, pan, deep focus, high contrast ceremonial. Wide composition across with, placed for immediate spatial orientation.. The Narrator performs the sak jump. plaza. Keep continuity exact across costume, silhouette, lighting, and spatial relationships.. Avoid proper nouns in the prompt body unless text is meant to appear on screen.. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH004_SC003; SHOT_INDEX; DIALOGUE; tars_tarkas; chieftain; martian_warrior
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: ultra_wide
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: consistency_repair
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH004_SC003
- chapter_id: CH004
- shot_type: establishing_wide
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across grand_audience_chamber with The Narrator, Martian Crowd, the_chieftain placed for immediate spatial orientation.
- shot_size: wide
- camera_angle: low_angle
- camera_motion: pan
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front
- visible_primary_subject_id: chieftain
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: midground inside grand_audience_chamber plaza
- primary_subject_scale_relation: distance traveled across marble floor
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: Narrator crouched for jump
- subject_relation_summary: The Narrator plays against Martian Crowd, the_chieftain in the same frame
- scene_short_description: A man punches a warrior in a massive marble hall then performs a long distance leap.
- shot_moment_summary: The Narrator performs the sak jump
- required_environment_anchor_1: grand_audience_chamber plaza
- required_scale_proof_detail: distance traveled across marble floor
- camera_package_description: wide, low angle, ultra-wide lens, pan, deep focus, high contrast ceremonial
- environment_subzone: grand_audience_chamber plaza
- prompt_family: shot_prompt
- reference_asset_ids: chieftain; grand_audience_chamber; DESC_CH004_SC003; DESC_CH004_SC003_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: chieftain
- image2_role: environment reference for the scene location
- image2_asset: grand audience chamber

# Continuity Notes
- Scene: CH004_SC003 / SC003.
- Variant: Consistency Repair.
- Physical contact precision during the punch sequence
- Trajectory and landing physics of the sak jump
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH004\CH004_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH004\CH004_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH004\CH004_SC003\SH003\DIALOGUE.json
