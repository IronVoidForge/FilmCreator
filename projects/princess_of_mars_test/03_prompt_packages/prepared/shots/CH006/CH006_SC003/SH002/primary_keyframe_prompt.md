# Title
SH002 Shot Prompt - Primary Keyframe

# ID
CH006_SC003_SH002_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for the scene location. Use image4 as the identity reference for an additional visible subject. Primary keyframe with balanced composition and clear subject placement.. Martian warriors arrive at a threshold to applaud a survivor amidst the remains of combat.. The subject from image1 is described character with stable costume and silhouette, foreground right within martian_interior_chamber threshold, low angle height vs protagonist, facing directly toward camera, warriors entering frame. The subject from image2 is described character with stable costume and silhouette, tars_tarkas plays against martian_warriors, protagonist in the same frame. Preserve described environment with stable spatial continuity from image3, especially plaza threshold. low angle height vs protagonist. full, low angle, wide lens, pan, deep focus, high contrast ceremonial. Readable medium composition in featuring, .. tars_tarkas and warriors arrive. threshold. Keep continuity exact across costume, silhouette, lighting, and spatial relationships.. Avoid proper nouns in the prompt body unless text is meant to appear on screen.. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH006_SC003; SHOT_INDEX; DIALOGUE; protagonist; tars_tarkas; sola; martian_warriors
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
- scene_id: CH006_SC003
- chapter_id: CH006
- shot_type: medium
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in martian_interior_chamber featuring tars_tarkas, martian_warriors, protagonist.
- shot_size: full
- camera_angle: low_angle
- camera_motion: pan
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: front
- visible_primary_subject_id: tars_tarkas
- visible_secondary_subject_ids: martian_warriors; protagonist
- primary_subject_frame_position: foreground right within martian_interior_chamber threshold
- primary_subject_scale_relation: low angle height vs protagonist
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: warriors entering frame
- subject_relation_summary: tars_tarkas plays against martian_warriors, protagonist in the same frame
- scene_short_description: Martian warriors arrive at a threshold to applaud a survivor amidst the remains of combat.
- shot_moment_summary: tars_tarkas and warriors arrive
- required_environment_anchor_1: plaza threshold
- required_scale_proof_detail: low angle height vs protagonist
- camera_package_description: full, low angle, wide lens, pan, deep focus, high contrast ceremonial
- environment_subzone: martian_interior_chamber threshold
- prompt_family: shot_prompt
- reference_asset_ids: tars_tarkas; martian_warriors; protagonist; martian_interior_chamber; DESC_CH006_SC003; DESC_CH006_SC003_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: tars tarkas
- image2_role: identity reference for the secondary visible subject
- image2_asset: martian warriors
- image3_role: environment reference for the scene location
- image3_asset: martian interior chamber
- image4_role: identity reference for an additional visible subject
- image4_asset: protagonist

# Continuity Notes
- Scene: CH006_SC003 / SC003.
- Variant: Primary Keyframe.
- Protagonist blood and dirt levels must match combat aftermath
- Proximity of dead apes to the character group
- warriors arrive and applaud
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH006\CH006_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH006\CH006_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH006\CH006_SC003\SH002\DIALOGUE.json
