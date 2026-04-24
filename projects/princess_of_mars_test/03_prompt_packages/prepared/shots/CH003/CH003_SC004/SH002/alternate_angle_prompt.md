# Title
SH002 Shot Prompt - Alternate Angle

# ID
CH003_SC004_SH002_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the environment reference for the scene location. Alternate angle with the same beat and preserved continuity. A desperate escape via a massive leap across a mossy circular enclosure. The subject from image1 is described character with stable costume and silhouette, midground inside central moss expanse, 30ft distance relative to ground, profile left toward the scene action, ascending in air. Preserve described environment with stable spatial anchors from image2, especially central moss expanse. 30ft distance relative to ground. wide, eye level, ultra-wide lens, track, deep focus, diffuse ambient. Wide composition across with placed for immediate spatial orientation. mid-air trajectory. central moss expanse. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH003_SC004; SHOT_INDEX; DIALOGUE; protagonist; martian_warriors
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: ultra_wide
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
- scene_id: CH003_SC004
- chapter_id: CH003
- shot_type: establishing_wide
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across circular_moss_basin with protagonist placed for immediate spatial orientation.
- shot_size: wide
- camera_angle: eye_level
- camera_motion: track
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: profile_left
- visible_primary_subject_id: protagonist
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: midground inside central moss expanse
- primary_subject_scale_relation: 30ft distance relative to ground
- primary_subject_facing_direction: profile left toward the scene action
- primary_subject_pose_description: ascending in air
- subject_relation_summary: protagonist carries the frame alone
- scene_short_description: A desperate escape via a massive leap across a mossy circular enclosure.
- shot_moment_summary: mid-air trajectory
- required_environment_anchor_1: central moss expanse
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: 30ft distance relative to ground
- camera_package_description: wide, eye level, ultra-wide lens, track, deep focus, diffuse ambient
- environment_subzone: central moss expanse
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; circular_moss_basin; DESC_CH003_SC004; DESC_CH003_SC004_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: protagonist
- image2_role: environment reference for the scene location
- image2_asset: circular moss basin

# Continuity Notes
- Scene: CH003_SC004 / SC004.
- Variant: Alternate Angle.
- Precise landing point relative to the thirty-foot jump distance
- Visual scale comparison between protagonist and martian_warriors
- The massive thirty-foot leap across the basin
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH003\CH003_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC004\SH002\DIALOGUE.json
