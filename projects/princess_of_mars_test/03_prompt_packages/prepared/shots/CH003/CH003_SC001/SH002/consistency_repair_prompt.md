# Title
SH002 Shot Prompt - Consistency Repair

# ID
CH003_SC001_SH002_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the environment reference for the scene location. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships.. A naked man wakes up in a yellowish mossy basin under a glass roof.. The subject from image1 is described character with stable costume and silhouette, foreground inside moss_basin_floor, Protagonist is small relative to the circular basin and Martian horizon., front three-quarter right toward the scene action, sitting up. Preserve described environment with stable spatial continuity from image2, especially yellowish moss. Protagonist is small relative to the circular basin and Martian horizon.. medium-close, eye level, normal lens, handheld, shallow subject, diffuse ambient. Intimate composition that isolates against to capture the beat's emotional turn.. protagonist struggling to sit up. moss_basin_floor. Keep continuity exact across costume, silhouette, lighting, and spatial relationships.. Avoid proper nouns in the prompt body unless text is meant to appear on screen.. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH003_SC001; SHOT_INDEX; DIALOGUE; protagonist
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
- scene_id: CH003_SC001
- chapter_id: CH003
- shot_type: reaction_closeup
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates protagonist against circular_moss_basin to capture the beat's emotional turn.
- shot_size: medium_close
- camera_angle: eye_level
- camera_motion: handheld
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_right
- visible_primary_subject_id: protagonist
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground inside moss_basin_floor
- primary_subject_scale_relation: Protagonist is small relative to the circular basin and Martian horizon.
- primary_subject_facing_direction: front three-quarter right toward the scene action
- primary_subject_pose_description: sitting up
- subject_relation_summary: protagonist carries the frame alone
- scene_short_description: A naked man wakes up in a yellowish mossy basin under a glass roof.
- shot_moment_summary: protagonist struggling to sit up
- required_environment_anchor_1: yellowish moss
- required_scale_proof_detail: Protagonist is small relative to the circular basin and Martian horizon.
- camera_package_description: medium-close, eye level, normal lens, handheld, shallow subject, diffuse ambient
- environment_subzone: moss_basin_floor
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; circular_moss_basin; DESC_CH003_SC001; DESC_CH003_SC001_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: protagonist
- image2_role: environment reference for the scene location
- image2_asset: circular moss basin

# Continuity Notes
- Scene: CH003_SC001 / SC001.
- Variant: Consistency Repair.
- Protagonist remains naked throughout
- Leap height and distance must remain consistent for physics logic
- Attempting to orient and stand
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH003\CH003_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC001\SH002\DIALOGUE.json
