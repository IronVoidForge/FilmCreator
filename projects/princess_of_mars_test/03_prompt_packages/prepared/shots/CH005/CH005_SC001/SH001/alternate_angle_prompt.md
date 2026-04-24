# Title
SH001 Shot Prompt - Alternate Angle

# ID
CH005_SC001_SH001_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for the scene location. Use image4 as the identity reference for an additional visible subject. Alternate angle with the same beat and preserved continuity.. The protagonist observes his surroundings, noting the murals of landscapes devoid of life. He experiences the care provided by Sola, learning about.... The subject from image1 is described character with stable costume and silhouette, foreground entry line within primary scene playing area, keep primary scene playing area readable as the scale anchor, front three-quarter left toward the scene action, Observing murals of landscapes devoid of life.. The subject from image2 is described character with stable costume and silhouette, protagonist, sola, and the_watch_dog in same frame for spatial orientation.. Preserve described environment with stable spatial continuity from image3, especially primary scene playing area. keep primary scene playing area readable as the scale anchor. medium, eye level, normal lens, locked off, deep focus, hard directional. Wide composition across with, and placed for immediate spatial orientation.. The protagonist observes his surroundings, noting murals of life-less landscapes while Sola and the Watch Dog are present.. primary scene playing area. Keep continuity exact across costume, silhouette, lighting, and spatial relationships.. Avoid proper nouns in the prompt body unless text is meant to appear on screen.. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH005_SC001; SHOT_INDEX; DIALOGUE; protagonist; sola; the_watch_dog
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: normal
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
- scene_id: CH005_SC001
- chapter_id: CH005
- shot_type: establishing_wide
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Wide establishing frame with a steady camera.
- composition: Wide composition across captive_chamber_murals with protagonist, sola, and the_watch_dog placed for immediate spatial orientation.
- shot_size: medium
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: hard_directional
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_left
- visible_primary_subject_id: protagonist
- visible_secondary_subject_ids: sola; the_watch_dog
- primary_subject_frame_position: foreground entry line within primary scene playing area
- primary_subject_scale_relation: keep primary scene playing area readable as the scale anchor
- primary_subject_facing_direction: front three-quarter left toward the scene action
- primary_subject_pose_description: Observing murals of landscapes devoid of life.
- subject_relation_summary: protagonist, sola, and the_watch_dog in same frame for spatial orientation.
- scene_short_description: The protagonist observes his surroundings, noting the murals of landscapes devoid of life. He experiences the care provided by Sola, learning about...
- shot_moment_summary: The protagonist observes his surroundings, noting murals of life-less landscapes while Sola and the Watch Dog are present.
- required_environment_anchor_1: primary scene playing area
- required_scale_proof_detail: keep primary scene playing area readable as the scale anchor
- camera_package_description: medium, eye level, normal lens, locked off, deep focus, hard directional
- environment_subzone: primary scene playing area
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; sola; the_watch_dog; captive_chamber_murals; DESC_CH005_SC001; DESC_CH005_SC001_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: protagonist
- image2_role: identity reference for the secondary visible subject
- image2_asset: sola
- image3_role: environment reference for the scene location
- image3_asset: captive chamber murals
- image4_role: identity reference for an additional visible subject
- image4_asset: the watch dog

# Continuity Notes
- Scene: CH005_SC001 / Establish the protagonist's status as a captive, introduce the Martia....
- Variant: Alternate Angle.
- Lighting changes based on moon cycles
- amount/type of food provided by Sola
- position of the Watch Dog near the door.
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH005\CH005_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH005\CH005_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH005\CH005_SC001\SH001\DIALOGUE.json
