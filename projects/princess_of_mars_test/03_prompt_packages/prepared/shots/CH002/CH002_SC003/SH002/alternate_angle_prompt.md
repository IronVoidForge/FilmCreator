# Title
SH002 Shot Prompt - Alternate Angle

# ID
CH002_SC003_SH002_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the environment reference for the scene location. Alternate angle with the same beat and preserved continuity. A man struggles to stand in a dark cave only to find his own lifeless, clothed body. The subject from image1 is described character with stable costume and silhouette, midground inside arizona_mountain_cave_floor, height difference between standing and prone bodies, profile left toward the scene action, rising from floor. Preserve described environment with stable spatial anchors from image2, especially arizona_mountain_cave_floor. height difference between standing and prone bodies. wide, eye level, wide lens, pull back, deep focus, low key night. Wide composition across with placed for immediate spatial orientation. standing naked figure vs lying clothed body. _floor. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH002_SC003; SHOT_INDEX; DIALOGUE; protagonist
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: wide
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
- scene_id: CH002_SC003
- chapter_id: CH002
- shot_type: establishing_wide
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across arizona_mountain_cave with protagonist placed for immediate spatial orientation.
- shot_size: wide
- camera_angle: eye_level
- camera_motion: pull_back
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: low_key_night
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: profile_left
- visible_primary_subject_id: protagonist
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: midground inside arizona_mountain_cave_floor
- primary_subject_scale_relation: height difference between standing and prone bodies
- primary_subject_facing_direction: profile left toward the scene action
- primary_subject_pose_description: rising from floor
- subject_relation_summary: protagonist carries the frame alone
- scene_short_description: A man struggles to stand in a dark cave only to find his own lifeless, clothed body.
- shot_moment_summary: standing naked figure vs lying clothed body
- required_environment_anchor_1: arizona_mountain_cave_floor
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: height difference between standing and prone bodies
- camera_package_description: wide, eye level, wide lens, pull back, deep focus, low key night
- environment_subzone: arizona_mountain_cave_floor
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; arizona_mountain_cave; DESC_CH002_SC003; DESC_CH002_SC003_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: protagonist
- image2_role: environment reference for the scene location
- image2_asset: arizona mountain cave

# Continuity Notes
- Scene: CH002_SC003 / SC003.
- Variant: Alternate Angle.
- Exact spatial distance between the standing naked protagonist and the lying clothed body
- Lighting consistency across both versions of the character in a single frame
- The metamorphosis/standing
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH002\CH002_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH002\CH002_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH002\CH002_SC003\SH002\DIALOGUE.json
