# Title
SH001 Shot Prompt - Consistency Repair

# ID
CH004_SC002_SH001_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the environment reference for the scene location. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships.. A small figure is presented within a massive, ancient hall filled with oversized marble and gold furniture.. The subject from image1 is described character with stable costume and silhouette, midground inside central_audience_floor, character vs ceiling height, back to camera with head turned toward the action, Narrator at threshold. Preserve described environment with stable spatial continuity from image2, especially central_audience_floor. character vs ceiling height. wide, low angle, ultra-wide lens, push in, environment priority, diffuse ambient. Wide composition across with placed for immediate spatial orientation.. Narrator enters the massive chamber. central_audience_floor. Keep continuity exact across costume, silhouette, lighting, and spatial relationships.. Avoid proper nouns in the prompt body unless text is meant to appear on screen.. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH004_SC002; SHOT_INDEX; DIALOGUE; tars_tarkas; chieftain
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
- scene_id: CH004_SC002
- chapter_id: CH004
- shot_type: establishing_wide
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across grand_audience_chamber with The Narrator placed for immediate spatial orientation.
- shot_size: wide
- camera_angle: low_angle
- camera_motion: push_in
- zoom_behavior: none
- focus_strategy: environment_priority
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: back
- visible_primary_subject_id: null
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: midground inside central_audience_floor
- primary_subject_scale_relation: character vs ceiling height
- primary_subject_facing_direction: back to camera with head turned toward the action
- primary_subject_pose_description: Narrator at threshold
- subject_relation_summary: The Narrator carries the frame alone
- scene_short_description: A small figure is presented within a massive, ancient hall filled with oversized marble and gold furniture.
- shot_moment_summary: Narrator enters the massive chamber
- required_environment_anchor_1: central_audience_floor
- required_scale_proof_detail: character vs ceiling height
- camera_package_description: wide, low angle, ultra-wide lens, push in, environment priority, diffuse ambient
- environment_subzone: central_audience_floor
- prompt_family: shot_prompt
- reference_asset_ids: grand_audience_chamber; DESC_CH004_SC002; DESC_CH004_SC002_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: null
- image2_role: environment reference for the scene location
- image2_asset: grand audience chamber

# Continuity Notes
- Scene: CH004_SC002 / SC002.
- Variant: Consistency Repair.
- Precise spatial placement of the Narrator relative to massive chamber dimensions
- Resolve The Narrator -> The Narrator
- Resolve Martian Court -> Martian Court
- Visual consistency of the Chieftain's specific regalia details
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH004\CH004_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH004\CH004_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH004\CH004_SC002\SH001\DIALOGUE.json
