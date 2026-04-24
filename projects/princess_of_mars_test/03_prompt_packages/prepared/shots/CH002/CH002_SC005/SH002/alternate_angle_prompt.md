# Title
SH002 Shot Prompt - Alternate Angle

# ID
CH002_SC005_SH002_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the environment reference for the scene location. Alternate angle with the same beat and preserved continuity. A man gazes at a red star before being violently pulled into a dark cosmic void. The subject from image1 is An Earthman undergoing a supernatural transformation., readable production detail, agile and capable of high-intensity physical exertion., Earthman in a low-gravity environment, foreground inside rocky_gorge_canyon, Transition from terrestrial scale (mountain landscape) to infinite cosmic scale (deep space), facing directly toward camera, eyes open. Preserve described environment with stable spatial continuity from image2 especially rocky_gorge_canyon. Keep one readable subject anchor: protagonist eyes. Keep celestial anchor eyes reflecting the the red star stable in the frame. Transition from terrestrial scale (mountain landscape) to infinite cosmic scale (deep space). extreme-close-up, eye level, portrait lens, locked off, zoom subtle in, shallow subject, high contrast ceremonial. Intimate composition that isolates against to capture the beat's emotional turn. eyes reflecting the red star. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH002_SC005; SHOT_INDEX; DIALOGUE; protagonist
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: portrait
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
- scene_id: CH002_SC005
- chapter_id: CH002
- shot_type: reaction_closeup
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates protagonist against rocky_gorge_canyon to capture the beat's emotional turn.
- shot_size: extreme_close_up
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: subtle_in
- focus_strategy: shallow_subject
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front
- visible_primary_subject_id: protagonist
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground inside rocky_gorge_canyon
- primary_subject_scale_relation: Transition from terrestrial scale (mountain landscape) to infinite cosmic scale (deep space).
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: eyes open
- subject_relation_summary: protagonist carries the frame alone
- scene_short_description: A man gazes at a red star before being violently pulled into a dark cosmic void.
- shot_moment_summary: eyes reflecting the red star
- required_environment_anchor_1: rocky_gorge_canyon
- required_subject_anchor_1: protagonist eyes
- required_celestial_anchor_1: eyes reflecting the red star
- required_scale_proof_detail: Transition from terrestrial scale (mountain landscape) to infinite cosmic scale (deep space).
- camera_package_description: extreme-close-up, eye level, portrait lens, locked off, zoom subtle in, shallow subject, high contrast ceremonial
- environment_subzone: rocky_gorge_canyon
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; rocky_gorge_canyon; DESC_CH002_SC005; DESC_CH002_SC005_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: protagonist
- image2_role: environment reference for the scene location
- image2_asset: rocky gorge canyon

# Continuity Notes
- Scene: CH002_SC005 / SC005.
- Variant: Alternate Angle.
- Visual brightness and position of Mars in the sky
- Seamless transition from rocky_gorge_canyon to deep_space_void
- The mesmerized trance
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH002\CH002_SC005.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH002\CH002_SC005\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH002\CH002_SC005\SH002\DIALOGUE.json
