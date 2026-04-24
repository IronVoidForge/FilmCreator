# Title
SH001 Shot Prompt - Consistency Repair

# ID
CH004_SC001_SH001_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for the scene location. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships.. A small figure and a large companion enter a massive marble and gold plaza filled with hundreds of Martians.. The subject from image1 is described character with stable costume and silhouette, midground inside plaza_threshold, Characters appear tiny against gold architecture, back to camera with head turned toward the action, Wide view of city edge. The subject from image2 is described character with stable costume and silhouette, The Narrator plays against tars_tarkas in the same frame. Preserve described environment with stable spatial continuity from image3, especially plaza_threshold. Characters appear tiny against gold architecture. extreme-wide, eye level, ultra-wide lens, locked off, deep focus, diffuse ambient. Wide composition across with, placed for immediate spatial orientation.. The Narrator and tars_tarkas view the massive city from the edge. plaza_threshold. Keep continuity exact across costume, silhouette, lighting, and spatial relationships.. Avoid proper nouns in the prompt body unless text is meant to appear on screen.. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH004_SC001; SHOT_INDEX; DIALOGUE; tars_tarkas
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
- scene_id: CH004_SC001
- chapter_id: CH004
- shot_type: establishing_wide
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across ancient_martian_city_plaza with The Narrator, tars_tarkas placed for immediate spatial orientation.
- shot_size: extreme_wide
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: back
- visible_primary_subject_id: the narrator
- visible_secondary_subject_ids: tars_tarkas
- primary_subject_frame_position: midground inside plaza_threshold
- primary_subject_scale_relation: Characters appear tiny against gold architecture
- primary_subject_facing_direction: back to camera with head turned toward the action
- primary_subject_pose_description: Wide view of city edge
- subject_relation_summary: The Narrator plays against tars_tarkas in the same frame
- scene_short_description: A small figure and a large companion enter a massive marble and gold plaza filled with hundreds of Martians.
- shot_moment_summary: The Narrator and tars_tarkas view the massive city from the edge
- required_environment_anchor_1: plaza_threshold
- required_scale_proof_detail: Characters appear tiny against gold architecture
- camera_package_description: extreme-wide, eye level, ultra-wide lens, locked off, deep focus, diffuse ambient
- environment_subzone: plaza_threshold
- prompt_family: shot_prompt
- reference_asset_ids: tars_tarkas; ancient_martian_city_plaza; DESC_CH004_SC001; DESC_CH004_SC001_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: the narrator
- image2_role: identity reference for the secondary visible subject
- image2_asset: tars tarkas
- image3_role: environment reference for the scene location
- image3_asset: ancient martian city plaza

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
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH004\CH004_SC001\SH001\DIALOGUE.json
