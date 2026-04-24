# Title
SH003 Shot Prompt - Consistency Repair

# ID
CH004_SC002_SH003_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the environment reference for the scene location. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships.. A small figure is presented within a massive, ancient hall filled with oversized marble and gold furniture.. The subject from image1 is described character with stable costume and silhouette, foreground right within throne_platform, furniture vs Martian hand/body, profile left toward the scene action, Detail shot focus. Preserve described environment with stable spatial continuity from image2, especially throne_platform. furniture vs Martian hand/body. insert-detail, eye level, telephoto lens, locked off, rack focus, hard directional. Detail composition centered on the key physical action or prop inside .. Close up of oversized furniture detail. throne_platform. Keep continuity exact across costume, silhouette, lighting, and spatial relationships.. Avoid proper nouns in the prompt body unless text is meant to appear on screen.. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH004_SC002; SHOT_INDEX; DIALOGUE; tars_tarkas; chieftain
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
- scene_id: CH004_SC002
- chapter_id: CH004
- shot_type: insert_detail
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Tight detail framing focused on a single visual object or gesture.
- composition: Detail composition centered on the key physical action or prop inside grand_audience_chamber.
- shot_size: insert_detail
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: none
- focus_strategy: rack_focus
- lighting_style: hard_directional
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: profile_left
- visible_primary_subject_id: null
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground right within throne_platform
- primary_subject_scale_relation: furniture vs Martian hand/body
- primary_subject_facing_direction: profile left toward the scene action
- primary_subject_pose_description: Detail shot focus
- subject_relation_summary: ancient furniture plays against The Narrator in the same frame
- scene_short_description: A small figure is presented within a massive, ancient hall filled with oversized marble and gold furniture.
- shot_moment_summary: Close up of oversized furniture detail
- required_environment_anchor_1: throne_platform
- required_scale_proof_detail: furniture vs Martian hand/body
- camera_package_description: insert-detail, eye level, telephoto lens, locked off, rack focus, hard directional
- environment_subzone: throne_platform
- prompt_family: shot_prompt
- reference_asset_ids: grand_audience_chamber; DESC_CH004_SC002; DESC_CH004_SC002_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: null
- image2_role: environment reference for the scene location
- image2_asset: grand audience chamber

# Continuity Notes
- Scene: CH004_SC002 / SC002.
- Variant: Consistency Repair.
- The Narrator notices the mismatch between biology and architecture
- Resolve The Narrator -> The Narrator
- Resolve Martian Court -> Martian Court
- Precise spatial placement of the Narrator relative to massive chamber dimensions
- Visual consistency of the Chieftain's specific regalia details
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH004\CH004_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH004\CH004_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH004\CH004_SC002\SH003\DIALOGUE.json
