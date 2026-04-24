# Title
SH003 Shot Prompt - Alternate Angle

# ID
CH002_SC003_SH003_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the environment reference for the scene location. Alternate angle with the same beat and preserved continuity. A man struggles to stand in a dark cave only to find his original self lying dead nearby. The subject from image1 is An Earthman undergoing a supernatural transformation., readable production detail, agile and capable of high-intensity physical exertion., Earthman in a low-gravity environment, foreground inside arizona_mountain_cave_shadows, The scale relationship between the upright naked figure and the prone clothed body defines the twist, facing directly toward camera, staring down. Preserve described environment with stable spatial continuity from image2 especially arizona_mountain_cave_floor. The scale relationship between the upright naked figure and the prone clothed body defines the twist. close-up, eye level, portrait lens, locked off, zoom subtle in, shallow subject, low key night. Intimate composition that isolates against to capture the beat's emotional turn. extreme shock on face. _shadows. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH002_SC003; SHOT_INDEX; DIALOGUE; protagonist
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: portrait
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
- scene_id: CH002_SC003
- chapter_id: CH002
- shot_type: reaction_closeup
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates protagonist against arizona_mountain_cave to capture the beat's emotional turn.
- shot_size: close_up
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: subtle_in
- focus_strategy: shallow_subject
- lighting_style: low_key_night
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front
- visible_primary_subject_id: protagonist
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground inside arizona_mountain_cave_shadows
- primary_subject_scale_relation: The scale relationship between the upright naked figure and the prone clothed body defines the twist.
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: staring down
- subject_relation_summary: protagonist carries the frame alone
- scene_short_description: A man struggles to stand in a dark cave only to find his original self lying dead nearby.
- shot_moment_summary: extreme shock on face
- required_environment_anchor_1: arizona_mountain_cave_floor
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: The scale relationship between the upright naked figure and the prone clothed body defines the twist.
- camera_package_description: close-up, eye level, portrait lens, locked off, zoom subtle in, shallow subject, low key night
- environment_subzone: arizona_mountain_cave_shadows
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; arizona_mountain_cave; DESC_CH002_SC003; DESC_CH002_SC003_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: protagonist
- image2_role: environment reference for the scene location
- image2_asset: arizona mountain cave

# Continuity Notes
- Scene: CH002_SC003 / SC003.
- Variant: Alternate Angle.
- Exact spatial distance between the old clothed body and the new naked body
- Lighting consistency across both versions of the character in a single frame
- Discovery of metamorphosis
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH002\CH002_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH002\CH002_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH002\CH002_SC003\SH003\DIALOGUE.json
