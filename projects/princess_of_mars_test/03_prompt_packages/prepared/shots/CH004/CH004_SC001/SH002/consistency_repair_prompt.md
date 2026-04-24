# Title
SH002 Shot Prompt - Consistency Repair

# ID
CH004_SC001_SH002_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for the scene location. Use image4 as the identity reference for an additional visible subject. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships.. A small figure and a large companion enter a massive marble and gold plaza filled with hundreds of Martians.. The subject from image1 is described character with stable costume and silhouette, foreground right within central_plaza_floor, Martian height/presence relative to Narrator, front three-quarter right toward the scene action, Walking into plaza. The subject from image2 is described character with stable costume and silhouette, Various Martians (crowd) plays against The Narrator, tars_tarkas in the same frame. Preserve described environment with stable spatial continuity from image3, especially central_plaza_floor. Martian height/presence relative to Narrator. full, low angle, wide lens, track, environment priority, high contrast ceremonial. Readable medium composition in featuring, .. Low angle view of Martians towering over the protagonists. central_plaza_floor. Keep continuity exact across costume, silhouette, lighting, and spatial relationships.. Avoid proper nouns in the prompt body unless text is meant to appear on screen.. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH004_SC001; SHOT_INDEX; DIALOGUE; tars_tarkas
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
- scene_id: CH004_SC001
- chapter_id: CH004
- shot_type: medium
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in ancient_martian_city_plaza featuring Various Martians (crowd), The Narrator, tars_tarkas.
- shot_size: full
- camera_angle: low_angle
- camera_motion: track
- zoom_behavior: none
- focus_strategy: environment_priority
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_right
- visible_primary_subject_id: various martians (crowd)
- visible_secondary_subject_ids: the narrator; tars_tarkas
- primary_subject_frame_position: foreground right within central_plaza_floor
- primary_subject_scale_relation: Martian height/presence relative to Narrator
- primary_subject_facing_direction: front three-quarter right toward the scene action
- primary_subject_pose_description: Walking into plaza
- subject_relation_summary: Various Martians (crowd) plays against The Narrator, tars_tarkas in the same frame
- scene_short_description: A small figure and a large companion enter a massive marble and gold plaza filled with hundreds of Martians.
- shot_moment_summary: Low angle view of Martians towering over the protagonists
- required_environment_anchor_1: central_plaza_floor
- required_scale_proof_detail: Martian height/presence relative to Narrator
- camera_package_description: full, low angle, wide lens, track, environment priority, high contrast ceremonial
- environment_subzone: central_plaza_floor
- prompt_family: shot_prompt
- reference_asset_ids: tars_tarkas; ancient_martian_city_plaza; DESC_CH004_SC001; DESC_CH004_SC001_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: various martians crowd
- image2_role: identity reference for the secondary visible subject
- image2_asset: the narrator
- image3_role: environment reference for the scene location
- image3_asset: ancient martian city plaza
- image4_role: identity reference for an additional visible subject
- image4_asset: tars tarkas

# Continuity Notes
- Scene: CH004_SC001 / SC001.
- Variant: Consistency Repair.
- Architecture and prop scale relative to The Narrator
- Movement patterns and density of Various Martians (crowd)
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH004\CH004_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH004\CH004_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH004\CH004_SC001\SH002\DIALOGUE.json
