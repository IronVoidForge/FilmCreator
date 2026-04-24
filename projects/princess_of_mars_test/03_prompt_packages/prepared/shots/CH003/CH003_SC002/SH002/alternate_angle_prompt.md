# Title
SH002 Shot Prompt - Alternate Angle

# ID
CH003_SC002_SH002_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the environment reference for the scene location. Alternate angle with the same beat and preserved continuity. A person investigates a glass-roofed incubator filled with large white eggs and multi-limbed creatures. The foreground detail is described character with stable costume and silhouette, foreground right within incubator_interior, egg size vs moss texture, facing directly toward camera, static egg shot. Preserve described environment with stable spatial anchors from image1, especially incubator_interior. Keep one readable subject anchor: gaze directed downward into basin. egg size vs moss texture. insert-detail, eye level, telephoto lens, locked off, shallow subject, diffuse ambient. Detail composition centered on the key physical action or prop inside . macro view of large white eggs. incubator_interior. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH003_SC002; SHOT_INDEX; DIALOGUE; protagonist
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
- scene_id: CH003_SC002
- chapter_id: CH003
- shot_type: insert_detail
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Tight detail framing focused on a single visual object or gesture.
- composition: Detail composition centered on the key physical action or prop inside circular_moss_basin.
- shot_size: insert_detail
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front
- visible_primary_subject_id: (none)
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground right within incubator_interior
- primary_subject_scale_relation: egg size vs moss texture
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: static egg shot
- subject_relation_summary: large_white_eggs carries the frame alone
- scene_short_description: A person investigates a glass-roofed incubator filled with large white eggs and multi-limbed creatures.
- shot_moment_summary: macro view of large white eggs
- required_environment_anchor_1: incubator_interior
- required_subject_anchor_1: gaze directed downward into basin
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: egg size vs moss texture
- camera_package_description: insert-detail, eye level, telephoto lens, locked off, shallow subject, diffuse ambient
- environment_subzone: incubator_interior
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; circular_moss_basin; DESC_CH003_SC002; DESC_CH003_SC002_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: environment reference for the scene location
- image1_asset: circular moss basin

# Continuity Notes
- Scene: CH003_SC002 / SC002.
- Variant: Alternate Angle.
- Hatchling movement patterns must remain consistent across cuts
- Lighting shifts based on light passing through the glass roof
- discovery of the eggs
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH003\CH003_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC002\SH002\DIALOGUE.json
