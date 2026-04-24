# Title
SH003 Shot Prompt - Primary Keyframe

# ID
CH003_SC003_SH003_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for the scene location. Primary keyframe with balanced composition and clear subject placement.. A lone figure hides in yellowish moss as a cavalry of twenty warriors thunders past.. The subject from image1 is described character with stable costume and silhouette, foreground inside circular_moss_basin, distance between metal and skin, profile right toward the scene action, spear descending. The subject from image2 is described character with stable costume and silhouette, spear tip plays against martian_warriors, protagonist in the same frame. Preserve described environment with stable spatial continuity from image3, especially circular_moss_basin. distance between metal and skin. extreme-close-up, low angle, portrait lens, handheld, shallow subject, high contrast ceremonial. Intimate composition that isolates, against to capture the beat's emotional turn.. spear narrowly misses protagonist. Keep continuity exact across costume, silhouette, lighting, and spatial relationships.. Avoid proper nouns in the prompt body unless text is meant to appear on screen.. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH003_SC003; SHOT_INDEX; DIALOGUE; protagonist; martian_warriors
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
- scene_id: CH003_SC003
- chapter_id: CH003
- shot_type: reaction_closeup
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates martian_warriors, protagonist against circular_moss_basin to capture the beat's emotional turn.
- shot_size: extreme_close_up
- camera_angle: low_angle
- camera_motion: handheld
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: profile_right
- visible_primary_subject_id: martian_warriors
- visible_secondary_subject_ids: protagonist
- primary_subject_frame_position: foreground inside circular_moss_basin
- primary_subject_scale_relation: distance between metal and skin
- primary_subject_facing_direction: profile right toward the scene action
- primary_subject_pose_description: spear descending
- subject_relation_summary: spear tip plays against martian_warriors, protagonist in the same frame
- scene_short_description: A lone figure hides in yellowish moss as a cavalry of twenty warriors thunders past.
- shot_moment_summary: spear narrowly misses protagonist
- required_environment_anchor_1: circular_moss_basin
- required_scale_proof_detail: distance between metal and skin
- camera_package_description: extreme-close-up, low angle, portrait lens, handheld, shallow subject, high contrast ceremonial
- environment_subzone: circular_moss_basin
- prompt_family: shot_prompt
- reference_asset_ids: martian_warriors; protagonist; circular_moss_basin; DESC_CH003_SC003; DESC_CH003_SC003_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: martian warriors
- image2_role: identity reference for the secondary visible subject
- image2_asset: protagonist
- image3_role: environment reference for the scene location
- image3_asset: circular moss basin

# Continuity Notes
- Scene: CH003_SC003 / SC003.
- Variant: Primary Keyframe.
- Rhythmic speed and cadence of the twenty mounted warriors
- Physical proximity distance between spear tip and protagonist
- leader's spear narrowly misses the protagonist
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH003\CH003_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC003\SH003\DIALOGUE.json
