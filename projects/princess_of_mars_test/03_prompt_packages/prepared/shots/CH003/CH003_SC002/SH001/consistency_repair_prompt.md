# Title
SH001 Shot Prompt - Consistency Repair

# ID
CH003_SC002_SH001_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the environment reference for the scene location. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. A person investigates a glass-roofed incubator filled with large white eggs and multi-limbed creatures. The subject from image1 is described character with stable costume and silhouette, foreground entry line within moss_basin_perimeter, human height relative to low walled enclosure, profile left toward the scene action, protagonist walking toward basin. Preserve described environment with stable spatial anchors from image2, especially moss_basin_perimeter. human height relative to low walled enclosure. medium-full, eye level, wide lens, push in, deep focus, diffuse ambient. Readable medium composition in featuring . protagonist approaches the glass enclosure. moss_basin_perimeter. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH003_SC002; SHOT_INDEX; DIALOGUE; protagonist
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
- scene_id: CH003_SC002
- chapter_id: CH003
- shot_type: medium
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in circular_moss_basin featuring protagonist.
- shot_size: medium_full
- camera_angle: eye_level
- camera_motion: push_in
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: profile_left
- visible_primary_subject_id: protagonist
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground entry line within moss_basin_perimeter
- primary_subject_scale_relation: human height relative to low walled enclosure
- primary_subject_facing_direction: profile left toward the scene action
- primary_subject_pose_description: protagonist walking toward basin
- subject_relation_summary: protagonist carries the frame alone
- scene_short_description: A person investigates a glass-roofed incubator filled with large white eggs and multi-limbed creatures.
- shot_moment_summary: protagonist approaches the glass enclosure
- required_environment_anchor_1: moss_basin_perimeter
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: human height relative to low walled enclosure
- camera_package_description: medium-full, eye level, wide lens, push in, deep focus, diffuse ambient
- environment_subzone: moss_basin_perimeter
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; circular_moss_basin; DESC_CH003_SC002; DESC_CH003_SC002_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: protagonist
- image2_role: environment reference for the scene location
- image2_asset: circular moss basin

# Continuity Notes
- Scene: CH003_SC002 / SC002.
- Variant: Consistency Repair.
- Hatchling movement patterns must remain consistent across cuts
- Lighting shifts through the glass roof must match sun position/environment
- protagonist approaches the incubator
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH003\CH003_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC002\SH001\DIALOGUE.json
