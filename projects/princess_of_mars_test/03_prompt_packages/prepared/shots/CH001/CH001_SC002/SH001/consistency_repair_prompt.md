# Title
SH001 Shot Prompt - Consistency Repair

# ID
CH001_SC002_SH001_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for the scene location. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships.. Two men discover a massive gold-bearing quartz vein in the remote Arizona hills.. The subject from image1 is described character with stable costume and silhouette, midground inside hill_plateau, men appear small against the hill, rear three-quarter left away from camera, wide landscape. The subject from image2 is described character with stable costume and silhouette, landscape plays against john_carter, james_k_powell in the same frame. Preserve described environment with stable spatial continuity from image3, especially arizona_gold_vein_claim. men appear small against the hill. wide, eye level, wide lens, pan, deep focus, hard directional. Wide composition across with, placed for immediate spatial orientation.. wide view of the hills and the men finding the vein. hill_plateau. Keep continuity exact across costume, silhouette, lighting, and spatial relationships.. Avoid proper nouns in the prompt body unless text is meant to appear on screen.. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH001_SC002; SHOT_INDEX; DIALOGUE; john_carter; james_k_powell
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: wide
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
- scene_id: CH001_SC002
- chapter_id: CH001
- shot_type: establishing_wide
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across arizona_gold_vein_claim with john_carter, james_k_powell placed for immediate spatial orientation.
- shot_size: wide
- camera_angle: eye_level
- camera_motion: pan
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: hard_directional
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: rear_three_quarter_left
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: james_k_powell
- primary_subject_frame_position: midground inside hill_plateau
- primary_subject_scale_relation: men appear small against the hill
- primary_subject_facing_direction: rear three-quarter left away from camera
- primary_subject_pose_description: wide landscape
- subject_relation_summary: landscape plays against john_carter, james_k_powell in the same frame
- scene_short_description: Two men discover a massive gold-bearing quartz vein in the remote Arizona hills.
- shot_moment_summary: wide view of the hills and the men finding the vein
- required_environment_anchor_1: arizona_gold_vein_claim
- required_scale_proof_detail: men appear small against the hill
- camera_package_description: wide, eye level, wide lens, pan, deep focus, hard directional
- environment_subzone: hill_plateau
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; james_k_powell; arizona_gold_vein_claim; DESC_CH001_SC002; DESC_CH001_SC002_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: identity reference for the secondary visible subject
- image2_asset: james k powell
- image3_role: environment reference for the scene location
- image3_asset: arizona gold vein claim

# Continuity Notes
- Scene: CH001_SC002 / SC002.
- Variant: Consistency Repair.
- Appearance of the gold vein within quartz
- 1865 prospector gear and clothing
- Bright desert sun lighting
- Discovery of the vein
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH001\CH001_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH001\CH001_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH001\CH001_SC002\SH001\DIALOGUE.json
