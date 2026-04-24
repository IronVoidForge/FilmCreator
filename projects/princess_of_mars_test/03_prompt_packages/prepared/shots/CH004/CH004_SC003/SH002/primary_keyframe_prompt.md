# Title
SH002 Shot Prompt - Primary Keyframe

# ID
CH004_SC003_SH002_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the environment reference for the scene location. Primary keyframe with balanced composition and clear subject placement.. A man punches a warrior in a massive marble hall then performs a long distance leap.. The subject from image1 is described character with stable costume and silhouette, foreground inside grand_audience_chamber plaza, The architecture is far too large for current inhabitants, emphasizing the scale of the jump., profile left toward the scene action, Punch thrown. Preserve described environment with stable spatial continuity from image2, especially grand_audience_chamber plaza. The architecture is far too large for current inhabitants, emphasizing the scale of the jump.. close-up, eye level, portrait lens, handheld, shallow subject, high contrast ceremonial. Intimate composition that isolates, against to capture the beat's emotional turn.. The punch connects with the warrior. plaza. Keep continuity exact across costume, silhouette, lighting, and spatial relationships.. Avoid proper nouns in the prompt body unless text is meant to appear on screen.. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH004_SC003; SHOT_INDEX; DIALOGUE; tars_tarkas; chieftain; martian_warrior
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
- scene_id: CH004_SC003
- chapter_id: CH004
- shot_type: reaction_closeup
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates The Narrator, martian_warrior against grand_audience_chamber to capture the beat's emotional turn.
- shot_size: close_up
- camera_angle: eye_level
- camera_motion: handheld
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: profile_left
- visible_primary_subject_id: martian_warrior
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground inside grand_audience_chamber plaza
- primary_subject_scale_relation: The architecture is far too large for current inhabitants, emphasizing the scale of the jump.
- primary_subject_facing_direction: profile left toward the scene action
- primary_subject_pose_description: Punch thrown
- subject_relation_summary: The Narrator plays against martian_warrior in the same frame
- scene_short_description: A man punches a warrior in a massive marble hall then performs a long distance leap.
- shot_moment_summary: The punch connects with the warrior
- required_environment_anchor_1: grand_audience_chamber plaza
- required_scale_proof_detail: The architecture is far too large for current inhabitants, emphasizing the scale of the jump.
- camera_package_description: close-up, eye level, portrait lens, handheld, shallow subject, high contrast ceremonial
- environment_subzone: grand_audience_chamber plaza
- prompt_family: shot_prompt
- reference_asset_ids: martian_warrior; grand_audience_chamber; DESC_CH004_SC003; DESC_CH004_SC003_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: martian warrior
- image2_role: environment reference for the scene location
- image2_asset: grand audience chamber

# Continuity Notes
- Scene: CH004_SC003 / SC003.
- Variant: Primary Keyframe.
- Physical contact precision during the punch sequence
- Trajectory and landing physics of the sak jump
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH004\CH004_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH004\CH004_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH004\CH004_SC003\SH002\DIALOGUE.json
