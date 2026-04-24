# Title
SH001 Shot Prompt - Primary Keyframe

# ID
CH003_SC001_SH001_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the environment reference for the scene location. Primary keyframe with balanced composition and clear subject placement. A naked man wakes in a yellowish mossy basin and leaps uncontrollably due to low gravity. The subject from image1 is protagonist, midground inside circular moss basin, subject size relative to basin width, front three-quarter left toward the scene action, eyes closed, prone. Preserve the environment from image2 especially circular moss basin. Keep one readable subject anchor: eyes closed, prone. wide, high angle, wide lens, locked off, deep focus, diffuse ambient. Wide composition across placed for immediate spatial orientation. protagonist lying naked in moss. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH003_SC001; SHOT_INDEX; DIALOGUE; protagonist
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: wide
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: primary_keyframe
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH003_SC001
- chapter_id: CH003
- shot_type: establishing_wide
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across circular_moss_basin with protagonist placed for immediate spatial orientation.
- shot_size: wide
- camera_angle: high_angle
- camera_motion: locked_off
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_left
- visible_primary_subject_id: protagonist
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: midground inside circular_moss_basin
- primary_subject_scale_relation: subject size relative to basin width
- primary_subject_facing_direction: front three-quarter left toward the scene action
- primary_subject_pose_description: eyes closed, prone
- subject_relation_summary: protagonist carries the frame alone
- scene_short_description: A naked man wakes in a yellowish mossy basin and leaps uncontrollably due to low gravity.
- shot_moment_summary: protagonist lying naked in moss
- required_environment_anchor_1: circular_moss_basin
- required_subject_anchor_1: eyes closed, prone
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: subject size relative to basin width
- camera_package_description: wide, high angle, wide lens, locked off, deep focus, diffuse ambient
- environment_subzone: circular_moss_basin
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; circular_moss_basin; DESC_CH003_SC001; DESC_CH003_SC001_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: protagonist
- image2_role: environment reference for the scene location
- image2_asset: circular moss basin

# Continuity Notes
- Scene: CH003_SC001 / SC001.
- Variant: Primary Keyframe.
- Subject nudity/exposure state
- Leap height and distance consistency
- Awakening in the moss
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH003\CH003_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC001\SH001\DIALOGUE.json
