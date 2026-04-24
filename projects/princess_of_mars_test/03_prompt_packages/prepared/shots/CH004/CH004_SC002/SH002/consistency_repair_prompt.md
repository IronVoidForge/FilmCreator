# Title
SH002 Shot Prompt - Consistency Repair

# ID
CH004_SC002_SH002_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the environment reference for the scene location. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships.. A small figure is presented within a massive, ancient hall filled with oversized marble and gold furniture.. The subject from image1 is described character with stable costume and silhouette, foreground right within throne_platform, regalia detail vs character size, front three-quarter right toward the scene action, Medium shot of chieftain. Preserve described environment with stable spatial continuity from image2, especially throne_platform. regalia detail vs character size. medium, eye level, normal lens, locked off, shallow subject, high contrast ceremonial. Readable medium composition in featuring, .. The Chieftain is revealed in regalia. throne_platform. Keep continuity exact across costume, silhouette, lighting, and spatial relationships.. Avoid proper nouns in the prompt body unless text is meant to appear on screen.. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH004_SC002; SHOT_INDEX; DIALOGUE; tars_tarkas; chieftain
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
- scene_id: CH004_SC002
- chapter_id: CH004
- shot_type: medium
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in grand_audience_chamber featuring the_chieftain, Martian Court, The Narrator.
- shot_size: medium
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_right
- visible_primary_subject_id: chieftain
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground right within throne_platform
- primary_subject_scale_relation: regalia detail vs character size
- primary_subject_facing_direction: front three-quarter right toward the scene action
- primary_subject_pose_description: Medium shot of chieftain
- subject_relation_summary: chieftain plays against Martian Court, The Narrator in the same frame
- scene_short_description: A small figure is presented within a massive, ancient hall filled with oversized marble and gold furniture.
- shot_moment_summary: The Chieftain is revealed in regalia
- required_environment_anchor_1: throne_platform
- required_scale_proof_detail: regalia detail vs character size
- camera_package_description: medium, eye level, normal lens, locked off, shallow subject, high contrast ceremonial
- environment_subzone: throne_platform
- prompt_family: shot_prompt
- reference_asset_ids: chieftain; grand_audience_chamber; DESC_CH004_SC002; DESC_CH004_SC002_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: chieftain
- image2_role: environment reference for the scene location
- image2_asset: grand audience chamber

# Continuity Notes
- Scene: CH004_SC002 / SC002.
- Variant: Consistency Repair.
- Visual consistency of the Chieftain's specific regalia details
- Resolve The Narrator -> The Narrator
- Resolve Martian Court -> Martian Court
- Precise spatial placement of the Narrator relative to massive chamber dimensions
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH004\CH004_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH004\CH004_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH004\CH004_SC002\SH002\DIALOGUE.json
