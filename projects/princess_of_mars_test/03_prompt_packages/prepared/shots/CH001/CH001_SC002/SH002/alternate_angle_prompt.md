# Title
SH002 Shot Prompt - Alternate Angle

# ID
CH001_SC002_SH002_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for the scene location. Alternate angle with the same beat and preserved continuity.. Two men discover a massive gold-bearing quartz vein in the remote Arizona hills.. The subject from image1 is described character with stable costume and silhouette, foreground inside arizona_gold_vein_claim, The scale of the quartz vein relative to the human prospectors., facing directly toward camera, blurred quartz. The subject from image2 is described character with stable costume and silhouette, gold_vein plays against john_carter, james_k_powell in the same frame. Preserve described environment with stable spatial continuity from image3, especially arizona_gold_vein_claim. The scale of the quartz vein relative to the human prospectors.. extreme-close-up, eye level, telephoto lens, locked off, shallow subject, hard directional. Intimate composition that isolates, against to capture the beat's emotional turn.. close up of gold in quartz. Keep continuity exact across costume, silhouette, lighting, and spatial relationships.. Avoid proper nouns in the prompt body unless text is meant to appear on screen.. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH001_SC002; SHOT_INDEX; DIALOGUE; john_carter; james_k_powell
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: telephoto
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
- scene_id: CH001_SC002
- chapter_id: CH001
- shot_type: reaction_closeup
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates john_carter, james_k_powell against arizona_gold_vein_claim to capture the beat's emotional turn.
- shot_size: extreme_close_up
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: hard_directional
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: james_k_powell
- primary_subject_frame_position: foreground inside arizona_gold_vein_claim
- primary_subject_scale_relation: The scale of the quartz vein relative to the human prospectors.
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: blurred quartz
- subject_relation_summary: gold_vein plays against john_carter, james_k_powell in the same frame
- scene_short_description: Two men discover a massive gold-bearing quartz vein in the remote Arizona hills.
- shot_moment_summary: close up of gold in quartz
- required_environment_anchor_1: arizona_gold_vein_claim
- required_scale_proof_detail: The scale of the quartz vein relative to the human prospectors.
- camera_package_description: extreme-close-up, eye level, telephoto lens, locked off, shallow subject, hard directional
- environment_subzone: arizona_gold_vein_claim
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; james_k_powell; arizona_gold_vein_claim; DESC_CH001_SC002; DESC_CH001_SC002_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: identity reference for the secondary visible subject
- image2_asset: james k powell
- image3_role: environment reference for the scene location
- image3_asset: arizona gold vein claim

# Continuity Notes
- Scene: CH001_SC002 / SC002.
- Variant: Alternate Angle.
- Appearance of the gold vein within quartz
- 1865 prospector gear and clothing
- Bright desert sun lighting
- Inspection and triumph
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH001\CH001_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH001\CH001_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH001\CH001_SC002\SH002\DIALOGUE.json
