# Title
SH003 Shot Prompt - Primary Keyframe

# ID
CH006_SC003_SH003_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for the scene location. Primary keyframe with balanced composition and clear subject placement.. Martian warriors arrive at a threshold to applaud a survivor amidst the remains of combat.. The subject from image1 is described character with stable costume and silhouette, foreground right within debris zone, Tars Tarkas presence dominates the martial hierarchy while Sola provides emotional scale., profile left toward the scene action, warriors laughing in background. The subject from image2 is described character with stable costume and silhouette, sola plays against protagonist in the same frame. Preserve described environment with stable spatial continuity from image3, especially debris zone. Tars Tarkas presence dominates the martial hierarchy while Sola provides emotional scale.. medium, eye level, portrait lens, push in, zoom subtle in, rack focus, soft even. Closing composition in that emphasizes the consequence of approaches with concern.. sola approaches protagonist. debris zone. Keep continuity exact across costume, silhouette, lighting, and spatial relationships.. Avoid proper nouns in the prompt body unless text is meant to appear on screen.. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH006_SC003; SHOT_INDEX; DIALOGUE; protagonist; tars_tarkas; sola; martian_warriors
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
- scene_id: CH006_SC003
- chapter_id: CH006
- shot_type: closing_reaction
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Controlled closing frame that lands the consequence of the beat.
- composition: Closing composition in martian_interior_chamber that emphasizes the consequence of sola approaches with concern.
- shot_size: medium
- camera_angle: eye_level
- camera_motion: push_in
- zoom_behavior: subtle_in
- focus_strategy: rack_focus
- lighting_style: soft_even
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: profile_left
- visible_primary_subject_id: sola
- visible_secondary_subject_ids: protagonist
- primary_subject_frame_position: foreground right within debris zone
- primary_subject_scale_relation: Tars Tarkas presence dominates the martial hierarchy while Sola provides emotional scale.
- primary_subject_facing_direction: profile left toward the scene action
- primary_subject_pose_description: warriors laughing in background
- subject_relation_summary: sola plays against protagonist in the same frame
- scene_short_description: Martian warriors arrive at a threshold to applaud a survivor amidst the remains of combat.
- shot_moment_summary: sola approaches protagonist
- required_environment_anchor_1: debris zone
- required_scale_proof_detail: Tars Tarkas presence dominates the martial hierarchy while Sola provides emotional scale.
- camera_package_description: medium, eye level, portrait lens, push in, zoom subtle in, rack focus, soft even
- environment_subzone: debris zone
- prompt_family: shot_prompt
- reference_asset_ids: sola; protagonist; martian_interior_chamber; DESC_CH006_SC003; DESC_CH006_SC003_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: sola
- image2_role: identity reference for the secondary visible subject
- image2_asset: protagonist
- image3_role: environment reference for the scene location
- image3_asset: martian interior chamber

# Continuity Notes
- Scene: CH006_SC003 / SC003.
- Variant: Primary Keyframe.
- Protagonist blood and dirt levels must match combat aftermath
- Proximity of dead apes to the character group
- sola approaches with concern
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH006\CH006_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH006\CH006_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH006\CH006_SC003\SH003\DIALOGUE.json
