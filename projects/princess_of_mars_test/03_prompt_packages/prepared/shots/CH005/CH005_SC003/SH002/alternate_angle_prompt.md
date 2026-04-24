# Title
SH002 Shot Prompt - Alternate Angle

# ID
CH005_SC003_SH002_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for the scene location. Alternate angle with the same beat and preserved continuity.. A frantic chase through deserted Martian streets involving high-altitude jumping and relentless pursuit.. The subject from image1 is described character with stable costume and silhouette, midground inside building rooftops/ledges, gap width, rear three-quarter left away from camera, mid-air jump. The subject from image2 is described character with stable costume and silhouette, protagonist plays against the_watch_dog in the same frame. Preserve described environment with stable spatial continuity from image3, especially building rooftops/ledges. gap width. wide, low angle, ultra-wide lens, crane, deep focus, diffuse ambient. Wide composition across with, placed for immediate spatial orientation.. protagonist leaps between two structures. building rooftops/ledges. Keep continuity exact across costume, silhouette, lighting, and spatial relationships.. Avoid proper nouns in the prompt body unless text is meant to appear on screen.. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH005_SC003; SHOT_INDEX; DIALOGUE; protagonist; the_watch_dog
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
- scene_id: CH005_SC003
- chapter_id: CH005
- shot_type: establishing_wide
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across martian_city_streets with protagonist, the_watch_dog placed for immediate spatial orientation.
- shot_size: wide
- camera_angle: low_angle
- camera_motion: crane
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: rear_three_quarter_left
- visible_primary_subject_id: protagonist
- visible_secondary_subject_ids: the_watch_dog
- primary_subject_frame_position: midground inside building rooftops/ledges
- primary_subject_scale_relation: gap width
- primary_subject_facing_direction: rear three-quarter left away from camera
- primary_subject_pose_description: mid-air jump
- subject_relation_summary: protagonist plays against the_watch_dog in the same frame
- scene_short_description: A frantic chase through deserted Martian streets involving high-altitude jumping and relentless pursuit.
- shot_moment_summary: protagonist leaps between two structures
- required_environment_anchor_1: building rooftops/ledges
- required_scale_proof_detail: gap width
- camera_package_description: wide, low angle, ultra-wide lens, crane, deep focus, diffuse ambient
- environment_subzone: building rooftops/ledges
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; the_watch_dog; martian_city_streets; DESC_CH005_SC003; DESC_CH005_SC003_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: protagonist
- image2_role: identity reference for the secondary visible subject
- image2_asset: the watch dog
- image3_role: environment reference for the scene location
- image3_asset: martian city streets

# Continuity Notes
- Scene: CH005_SC003 / SC003.
- Variant: Alternate Angle.
- Precise height and distance measurements for all jumps
- Timing of the_watch_dog arrival at street corners relative to protagonist position
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH005\CH005_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH005\CH005_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH005\CH005_SC003\SH002\DIALOGUE.json
