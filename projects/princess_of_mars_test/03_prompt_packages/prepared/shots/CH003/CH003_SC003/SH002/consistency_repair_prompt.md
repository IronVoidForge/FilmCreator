# Title
SH002 Shot Prompt - Consistency Repair

# ID
CH003_SC003_SH002_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for the scene location. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. A hidden figure watches as a massive cavalry of twenty warriors thunders through yellowish moss. The subject from image1 is described character with stable costume and silhouette, midground inside circular_moss_basin, preserve readable body-to-environment scale in frame, front three-quarter right toward the scene action, mounts appearing on horizon. The subject from image2 is described character with stable costume and silhouette, martian_warriors plays against protagonist in the same frame. Preserve described environment with stable spatial anchors from image3, especially circular_moss_basin. preserve readable body-to-environment scale in frame. wide, low angle, ultra-wide lens, track, deep focus, diffuse ambient. Wide composition across with, placed for immediate spatial orientation. cavalcade enters view. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH003_SC003; SHOT_INDEX; DIALOGUE; protagonist; martian_warriors
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
- scene_id: CH003_SC003
- chapter_id: CH003
- shot_type: establishing_wide
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across circular_moss_basin with martian_warriors, protagonist placed for immediate spatial orientation.
- shot_size: wide
- camera_angle: low_angle
- camera_motion: track
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_right
- visible_primary_subject_id: martian_warriors
- visible_secondary_subject_ids: protagonist
- primary_subject_frame_position: midground inside circular_moss_basin
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: front three-quarter right toward the scene action
- primary_subject_pose_description: mounts appearing on horizon
- subject_relation_summary: martian_warriors plays against protagonist in the same frame
- scene_short_description: A hidden figure watches as a massive cavalry of twenty warriors thunders through yellowish moss.
- shot_moment_summary: cavalcade enters view
- required_environment_anchor_1: circular_moss_basin
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: preserve readable body-to-environment scale in frame
- camera_package_description: wide, low angle, ultra-wide lens, track, deep focus, diffuse ambient
- environment_subzone: circular_moss_basin
- prompt_family: shot_prompt
- reference_asset_ids: martian_warriors; protagonist; circular_moss_basin; DESC_CH003_SC003; DESC_CH003_SC003_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: martian warriors
- image2_role: identity reference for the secondary visible subject
- image2_asset: protagonist
- image3_role: environment reference for the scene location
- image3_asset: circular moss basin

# Continuity Notes
- Scene: CH003_SC003 / SC003.
- Variant: Consistency Repair.
- Rhythmic speed of the twenty mounted warriors
- Physical proximity distance between spear tip and protagonist
- Realization of approaching warriors
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH003\CH003_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC003\SH002\DIALOGUE.json
