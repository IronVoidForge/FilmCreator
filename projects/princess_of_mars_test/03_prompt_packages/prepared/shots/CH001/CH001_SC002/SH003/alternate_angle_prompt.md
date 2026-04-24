# Title
SH003 Shot Prompt - Alternate Angle

# ID
CH001_SC002_SH003_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for the scene location. Alternate angle with the same beat and preserved continuity.. Two men discover a massive gold-bearing quartz vein in the remote Arizona hills.. The subject from image1 is described character with stable costume and silhouette, foreground right within arizona_gold_vein_claim, The scale of the quartz vein relative to the human prospectors., front three-quarter left toward the scene action, men facing each other. The subject from image2 is described character with stable costume and silhouette, john_carter plays against james_k_powell in the same frame. Preserve described environment with stable spatial continuity from image3, especially arizona_gold_vein_claim. The scale of the quartz vein relative to the human prospectors.. medium, eye level, normal lens, locked off, deep focus, hard directional. Over-the-shoulder composition in with, sharing the frame for dialogue or tension.. two shot of men agreeing on the plan. Keep continuity exact across costume, silhouette, lighting, and spatial relationships.. Avoid proper nouns in the prompt body unless text is meant to appear on screen.. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH001_SC002; SHOT_INDEX; DIALOGUE; john_carter; james_k_powell
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: normal
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
- shot_type: over_the_shoulder
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Shoulder-level conversational framing with visible foreground presence.
- composition: Over-the-shoulder composition in arizona_gold_vein_claim with john_carter, james_k_powell sharing the frame for dialogue or tension.
- shot_size: medium
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: hard_directional
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: front_three_quarter_left
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: james_k_powell
- primary_subject_frame_position: foreground right within arizona_gold_vein_claim
- primary_subject_scale_relation: The scale of the quartz vein relative to the human prospectors.
- primary_subject_facing_direction: front three-quarter left toward the scene action
- primary_subject_pose_description: men facing each other
- subject_relation_summary: john_carter plays against james_k_powell in the same frame
- scene_short_description: Two men discover a massive gold-bearing quartz vein in the remote Arizona hills.
- shot_moment_summary: two shot of men agreeing on the plan
- required_environment_anchor_1: arizona_gold_vein_claim
- required_scale_proof_detail: The scale of the quartz vein relative to the human prospectors.
- camera_package_description: medium, eye level, normal lens, locked off, deep focus, hard directional
- environment_subzone: arizona_gold_vein_claim
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; james_k_powell; arizona_gold_vein_claim; DESC_CH001_SC002; DESC_CH001_SC002_SH003
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
- Tactical planning
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH001\CH001_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH001\CH001_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH001\CH001_SC002\SH003\DIALOGUE.json
