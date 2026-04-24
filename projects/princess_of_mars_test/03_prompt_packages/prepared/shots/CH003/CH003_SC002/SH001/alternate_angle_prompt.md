# Title
SH001 Shot Prompt - Alternate Angle

# ID
CH003_SC002_SH001_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the environment reference for the scene location. Alternate angle with the same beat and preserved continuity. A transformed man investigates a glass-roofed incubator filled with large white eggs and multi-limbed creatures. The subject from image1 is protagonist, foreground entry line within yellowish moss floor, protagonist height vs low wall, profile left toward the scene action, walking toward basin. Preserve the environment from image2 especially yellowish moss floor. medium-full, eye level, wide lens, track, deep focus, diffuse ambient. Wide composition across placed for immediate spatial orientation. protagonist approaches the glass enclosure. yellowish moss floor. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH003_SC002; SHOT_INDEX; DIALOGUE; protagonist
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: wide
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: alternate_angle
- review_notes: Prompt body is missing the required subject anchor for an on-screen shot.
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH003_SC002
- chapter_id: CH003
- shot_type: establishing_wide
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across circular_moss_basin with protagonist placed for immediate spatial orientation.
- shot_size: medium_full
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
- primary_subject_frame_position: foreground entry line within yellowish_moss_floor
- primary_subject_scale_relation: protagonist height vs low wall
- primary_subject_facing_direction: profile left toward the scene action
- primary_subject_pose_description: walking toward basin
- subject_relation_summary: protagonist carries the frame alone
- scene_short_description: A transformed man investigates a glass-roofed incubator filled with large white eggs and multi-limbed creatures.
- shot_moment_summary: protagonist approaches the glass enclosure
- required_environment_anchor_1: yellowish_moss_floor
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: protagonist height vs low wall
- camera_package_description: medium-full, eye level, wide lens, track, deep focus, diffuse ambient
- environment_subzone: yellowish_moss_floor
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; circular_moss_basin; DESC_CH003_SC002; DESC_CH003_SC002_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: protagonist
- image2_role: environment reference for the scene location
- image2_asset: circular moss basin

# Continuity Notes
- Scene: CH003_SC002 / SC002.
- Variant: Alternate Angle.
- Hatchling movement patterns (multi-limbed coordination)
- Light refraction/transmission through the glass roof
- protagonist approaches the incubator
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH003\CH003_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC002\SH001\DIALOGUE.json
