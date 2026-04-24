# Title
SH001 Shot Prompt - Consistency Repair

# ID
CH001_SC003_SH001_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the environment reference for the scene location. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships.. A lone man tracks movement through a valley before discovering an Apache camp on a high plateau.. The subject from image1 is described character with stable costume and silhouette, foreground inside valley floor, distance to valley floor, profile left toward the scene action, john_carter looking down. Preserve described environment with stable spatial continuity from image2, especially quartz vein trail. distance to valley floor. medium-close, eye level, telephoto lens, pan, shallow subject, diffuse ambient. Intimate composition that isolates against to capture the beat's emotional turn.. movement detected in valley. valley floor. Keep continuity exact across costume, silhouette, lighting, and spatial relationships.. Avoid proper nouns in the prompt body unless text is meant to appear on screen.. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH001_SC003; SHOT_INDEX; DIALOGUE; john_carter; apache_warriors
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: telephoto
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
- scene_id: CH001_SC003
- chapter_id: CH001
- shot_type: reaction_closeup
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates john_carter against arizona_gold_vein_claim to capture the beat's emotional turn.
- shot_size: medium_close
- camera_angle: eye_level
- camera_motion: pan
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: profile_left
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground inside valley floor
- primary_subject_scale_relation: distance to valley floor
- primary_subject_facing_direction: profile left toward the scene action
- primary_subject_pose_description: john_carter looking down
- subject_relation_summary: john_carter carries the frame alone
- scene_short_description: A lone man tracks movement through a valley before discovering an Apache camp on a high plateau.
- shot_moment_summary: movement detected in valley
- required_environment_anchor_1: quartz vein trail
- required_scale_proof_detail: distance to valley floor
- camera_package_description: medium-close, eye level, telephoto lens, pan, shallow subject, diffuse ambient
- environment_subzone: valley floor
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; arizona_gold_vein_claim; DESC_CH001_SC003; DESC_CH001_SC003_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: environment reference for the scene location
- image2_asset: arizona gold vein claim

# Continuity Notes
- Scene: CH001_SC003 / SC003.
- Variant: Consistency Repair.
- Exact count of apache_warriors
- Direction of pursuit from valley to plateau
- Weapon handling (rifles and sidearms)
- Detection of movement in the valley
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH001\CH001_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH001\CH001_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH001\CH001_SC003\SH001\DIALOGUE.json
