# Title
SH002 Shot Prompt - Consistency Repair

# ID
CH003_SC002_SH002_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the environment reference for the scene location. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. A transformed man investigates a glass-roofed incubator filled with large white eggs and multi-limbed creatures. The foreground detail is large white eggs, foreground right within incubator interior, egg size relative to hatchlings, facing directly toward camera, static egg shot. Preserve the environment from image1 especially incubator interior. insert-detail, high angle, telephoto lens, locked off, zoom subtle in, shallow subject, diffuse ambient. Detail composition centered on the key physical action or prop inside. macro view of large white eggs. incubator interior. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH003_SC002; SHOT_INDEX; DIALOGUE; protagonist
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
- scene_id: CH003_SC002
- chapter_id: CH003
- shot_type: insert_detail
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Tight detail framing focused on a single visual object or gesture.
- composition: Detail composition centered on the key physical action or prop inside circular_moss_basin.
- shot_size: insert_detail
- camera_angle: high_angle
- camera_motion: locked_off
- zoom_behavior: subtle_in
- focus_strategy: shallow_subject
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front
- visible_primary_subject_id: (none)
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground right within incubator_interior
- primary_subject_scale_relation: egg size relative to hatchlings
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: static egg shot
- subject_relation_summary: large_white_eggs carries the frame alone
- scene_short_description: A transformed man investigates a glass-roofed incubator filled with large white eggs and multi-limbed creatures.
- shot_moment_summary: macro view of large white eggs
- required_environment_anchor_1: incubator_interior
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: egg size relative to hatchlings
- camera_package_description: insert-detail, high angle, telephoto lens, locked off, zoom subtle in, shallow subject, diffuse ambient
- environment_subzone: incubator_interior
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; circular_moss_basin; DESC_CH003_SC002; DESC_CH003_SC002_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: environment reference for the scene location
- image1_asset: circular moss basin

# Continuity Notes
- Scene: CH003_SC002 / SC002.
- Variant: Consistency Repair.
- Hatchling movement patterns (multi-limbed coordination)
- Light refraction/intensity through the glass roof
- discovery of large white eggs
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH003\CH003_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC002\SH002\DIALOGUE.json
