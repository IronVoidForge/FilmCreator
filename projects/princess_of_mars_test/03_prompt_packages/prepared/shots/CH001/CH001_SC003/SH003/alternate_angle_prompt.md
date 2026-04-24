# Title
SH003 Shot Prompt - Alternate Angle

# ID
CH001_SC003_SH003_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for the scene location. Alternate angle with the same beat and preserved continuity.. A lone man tracks movement through a valley before discovering an Apache camp on a high plateau.. The subject from image1 is described character with stable costume and silhouette, foreground right within plateau camp, preserve readable body-to-environment scale in frame, facing directly toward camera, combat engagement. The subject from image2 is described character with stable costume and silhouette, john_carter plays against apache_warriors in the same frame. Preserve described environment with stable spatial continuity from image3, especially plateau edge. preserve readable body-to-environment scale in frame. medium, eye level, normal lens, handheld, rack focus, high contrast ceremonial. Dynamic composition in with clear pursuit vectors and readable movement for, .. skirmish begins. plateau camp. Keep continuity exact across costume, silhouette, lighting, and spatial relationships.. Avoid proper nouns in the prompt body unless text is meant to appear on screen.. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH001_SC003; SHOT_INDEX; DIALOGUE; john_carter; apache_warriors
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
- scene_id: CH001_SC003
- chapter_id: CH001
- shot_type: action
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: Dynamic composition in arizona_gold_vein_claim with clear pursuit vectors and readable movement for john_carter, apache_warriors.
- shot_size: medium
- camera_angle: eye_level
- camera_motion: handheld
- zoom_behavior: none
- focus_strategy: rack_focus
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: apache_warriors
- primary_subject_frame_position: foreground right within plateau camp
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: combat engagement
- subject_relation_summary: john_carter plays against apache_warriors in the same frame
- scene_short_description: A lone man tracks movement through a valley before discovering an Apache camp on a high plateau.
- shot_moment_summary: skirmish begins
- required_environment_anchor_1: plateau edge
- required_scale_proof_detail: preserve readable body-to-environment scale in frame
- camera_package_description: medium, eye level, normal lens, handheld, rack focus, high contrast ceremonial
- environment_subzone: plateau camp
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; apache_warriors; arizona_gold_vein_claim; DESC_CH001_SC003; DESC_CH001_SC003_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: identity reference for the secondary visible subject
- image2_asset: apache warriors
- image3_role: environment reference for the scene location
- image3_asset: arizona gold vein claim

# Continuity Notes
- Scene: CH001_SC003 / SC003.
- Variant: Alternate Angle.
- Exact count of apache_warriors
- Direction of pursuit from valley to plateau
- Weapon handling (rifles and sidearms)
- The skirmish
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH001\CH001_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH001\CH001_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH001\CH001_SC003\SH003\DIALOGUE.json
