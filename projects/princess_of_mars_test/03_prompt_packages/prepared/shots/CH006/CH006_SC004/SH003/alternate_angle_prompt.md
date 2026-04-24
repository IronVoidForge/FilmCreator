# Title
SH003 Shot Prompt - Alternate Angle

# ID
CH006_SC004_SH003_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for the scene location. Use image4 as the identity reference for an additional visible subject. Alternate angle with the same beat and preserved continuity.. A warrior attempts to execute a wounded beast before the protagonist intervenes physically.. The subject from image1 is described character with stable costume and silhouette, midground inside plaza, preserve readable body-to-environment scale in frame, rear three-quarter left away from camera, group at threshold. The subject from image2 is described character with stable costume and silhouette, protagonist plays against sola, martian_warrior in the same frame. Preserve described environment with stable spatial continuity from image3, especially exit threshold. light transition. wide, eye level, wide lens, track, deep focus, backlit. Wide composition across with, placed for immediate spatial orientation.. group exits to plaza. plaza. Keep continuity exact across costume, silhouette, lighting, and spatial relationships.. Avoid proper nouns in the prompt body unless text is meant to appear on screen.. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH006_SC004; SHOT_INDEX; DIALOGUE; protagonist; sola; martian_warrior; watch_thing
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
- scene_id: CH006_SC004
- chapter_id: CH006
- shot_type: establishing_wide
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across martian_interior_chamber with protagonist, sola, martian_warrior placed for immediate spatial orientation.
- shot_size: wide
- camera_angle: eye_level
- camera_motion: track
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: backlit
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: rear_three_quarter_left
- visible_primary_subject_id: protagonist
- visible_secondary_subject_ids: sola; martian_warrior
- primary_subject_frame_position: midground inside plaza
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: rear three-quarter left away from camera
- primary_subject_pose_description: group at threshold
- subject_relation_summary: protagonist plays against sola, martian_warrior in the same frame
- scene_short_description: A warrior attempts to execute a wounded beast before the protagonist intervenes physically.
- shot_moment_summary: group exits to plaza
- required_environment_anchor_1: exit threshold
- required_scale_proof_detail: light transition
- camera_package_description: wide, eye level, wide lens, track, deep focus, backlit
- environment_subzone: plaza
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; sola; martian_warrior; martian_interior_chamber; DESC_CH006_SC004; DESC_CH006_SC004_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: protagonist
- image2_role: identity reference for the secondary visible subject
- image2_asset: sola
- image3_role: environment reference for the scene location
- image3_asset: martian interior chamber
- image4_role: identity reference for an additional visible subject
- image4_asset: martian warrior

# Continuity Notes
- Scene: CH006_SC004 / SC004.
- Variant: Alternate Angle.
- Physical mobility status of watch_thing (wounded state)
- Lighting transition from martian_interior_chamber to exterior Martian light
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH006\CH006_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH006\CH006_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH006\CH006_SC004\SH003\DIALOGUE.json
