# Title
SH002 Shot Prompt - Consistency Repair

# ID
CH005_SC004_SH002_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for the scene location. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships.. A desperate leap toward a high window ends in an interception by a massive white creature.. The subject from image1 is described character with stable costume and silhouette, foreground right within valley_overlook_exterior, massive hand vs human body, front three-quarter right toward the scene action, protagonist reaching window. The subject from image2 is described character with stable costume and silhouette, the_colossal_creature plays against protagonist in the same frame. Preserve described environment with stable spatial continuity from image3, especially valley_overlook_exterior. massive hand vs human body. medium-full, low angle, normal lens, handheld, shallow subject, high contrast ceremonial. Readable medium composition in featuring, .. the_colossal_creature grabs protagonist. Keep continuity exact across costume, silhouette, lighting, and spatial relationships.. Avoid proper nouns in the prompt body unless text is meant to appear on screen.. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH005_SC004; SHOT_INDEX; DIALOGUE; protagonist; the_watch_dog; the_colossal_creature
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: normal
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
- scene_id: CH005_SC004
- chapter_id: CH005
- shot_type: medium
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in valley_overlook_exterior featuring the_colossal_creature, protagonist.
- shot_size: medium_full
- camera_angle: low_angle
- camera_motion: handheld
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_right
- visible_primary_subject_id: the_colossal_creature
- visible_secondary_subject_ids: protagonist
- primary_subject_frame_position: foreground right within valley_overlook_exterior
- primary_subject_scale_relation: massive hand vs human body
- primary_subject_facing_direction: front three-quarter right toward the scene action
- primary_subject_pose_description: protagonist reaching window
- subject_relation_summary: the_colossal_creature plays against protagonist in the same frame
- scene_short_description: A desperate leap toward a high window ends in an interception by a massive white creature.
- shot_moment_summary: the_colossal_creature grabs protagonist
- required_environment_anchor_1: valley_overlook_exterior
- required_scale_proof_detail: massive hand vs human body
- camera_package_description: medium-full, low angle, normal lens, handheld, shallow subject, high contrast ceremonial
- environment_subzone: valley_overlook_exterior
- prompt_family: shot_prompt
- reference_asset_ids: the_colossal_creature; protagonist; valley_overlook_exterior; DESC_CH005_SC004; DESC_CH005_SC004_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: the colossal creature
- image2_role: identity reference for the secondary visible subject
- image2_asset: protagonist
- image3_role: environment reference for the scene location
- image3_asset: valley overlook exterior

# Continuity Notes
- Scene: CH005_SC004 / SC004.
- Variant: Consistency Repair.
- Window height must remain fixed at thirty feet above ground
- Physical contact point between protagonist and the_colossal_creature
- Lighting shift from bright city streets to dark captive_chamber_murals
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH005\CH005_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH005\CH005_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH005\CH005_SC004\SH002\DIALOGUE.json
