# Title
SH002 Shot Prompt - Consistency Repair

# ID
CH006_SC004_SH002_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for the scene location. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships.. A warrior attempts to execute a wounded beast before the protagonist intervenes physically.. The subject from image1 is described character with stable costume and silhouette, foreground inside martian_interior_chamber, preserve readable body-to-environment scale in frame, front three-quarter right toward the scene action, strike begins. The subject from image2 is described character with stable costume and silhouette, protagonist plays against martian_warrior in the same frame. Preserve described environment with stable spatial continuity from image3, especially martian_interior_chamber. impact force. close-up, eye level, portrait lens, handheld, shallow subject, hard directional. Intimate composition that isolates, against to capture the beat's emotional turn.. protagonist strikes martian_warrior. Keep continuity exact across costume, silhouette, lighting, and spatial relationships.. Avoid proper nouns in the prompt body unless text is meant to appear on screen.. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH006_SC004; SHOT_INDEX; DIALOGUE; protagonist; sola; martian_warrior; watch_thing
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: portrait
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
- scene_id: CH006_SC004
- chapter_id: CH006
- shot_type: reaction_closeup
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates protagonist, martian_warrior against martian_interior_chamber to capture the beat's emotional turn.
- shot_size: close_up
- camera_angle: eye_level
- camera_motion: handheld
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: hard_directional
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: front_three_quarter_right
- visible_primary_subject_id: protagonist
- visible_secondary_subject_ids: martian_warrior
- primary_subject_frame_position: foreground inside martian_interior_chamber
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: front three-quarter right toward the scene action
- primary_subject_pose_description: strike begins
- subject_relation_summary: protagonist plays against martian_warrior in the same frame
- scene_short_description: A warrior attempts to execute a wounded beast before the protagonist intervenes physically.
- shot_moment_summary: protagonist strikes martian_warrior
- required_environment_anchor_1: martian_interior_chamber
- required_scale_proof_detail: impact force
- camera_package_description: close-up, eye level, portrait lens, handheld, shallow subject, hard directional
- environment_subzone: martian_interior_chamber
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; martian_warrior; martian_interior_chamber; DESC_CH006_SC004; DESC_CH006_SC004_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: protagonist
- image2_role: identity reference for the secondary visible subject
- image2_asset: martian warrior
- image3_role: environment reference for the scene location
- image3_asset: martian interior chamber

# Continuity Notes
- Scene: CH006_SC004 / SC004.
- Variant: Consistency Repair.
- Physical mobility status of watch_thing (wounded state)
- protagonist strikes martian_warrior to protect beast
- Lighting transition from martian_interior_chamber to exterior Martian light
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH006\CH006_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH006\CH006_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH006\CH006_SC004\SH002\DIALOGUE.json
