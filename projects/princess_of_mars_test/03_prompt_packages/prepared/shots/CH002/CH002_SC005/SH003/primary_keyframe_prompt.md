# Title
SH003 Shot Prompt - Primary Keyframe

# ID
CH002_SC005_SH003_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the environment reference for the scene location. Primary keyframe with balanced composition and clear subject placement. A man gazes at a red star before being violently pulled into a dark cosmic void. The subject from image1 is An Earthman undergoing a supernatural transformation., readable production detail, agile and capable of high-intensity physical exertion., Earthman in a low-gravity environment, foreground inside deep_space_void, motion blur against darkness, front three-quarter left toward the scene action, blackness/eyes closed. Preserve described environment with stable spatial continuity from image2 especially deep_space_void. Keep one readable subject anchor: blackness/eyes closed. motion blur against darkness. close-up, eye level, portrait lens, push in, zoom subtle in, shallow subject, backlit. Intimate composition that isolates against to capture the beat's emotional turn. violent transport through space. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH002_SC005; SHOT_INDEX; DIALOGUE; protagonist
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: portrait
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
- scene_id: CH002_SC005
- chapter_id: CH002
- shot_type: reaction_closeup
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates protagonist against deep_space_void to capture the beat's emotional turn.
- shot_size: close_up
- camera_angle: eye_level
- camera_motion: push_in
- zoom_behavior: subtle_in
- focus_strategy: shallow_subject
- lighting_style: backlit
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_left
- visible_primary_subject_id: protagonist
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground inside deep_space_void
- primary_subject_scale_relation: motion blur against darkness
- primary_subject_facing_direction: front three-quarter left toward the scene action
- primary_subject_pose_description: blackness/eyes closed
- subject_relation_summary: protagonist carries the frame alone
- scene_short_description: A man gazes at a red star before being violently pulled into a dark cosmic void.
- shot_moment_summary: violent transport through space
- required_environment_anchor_1: deep_space_void
- required_subject_anchor_1: blackness/eyes closed
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: motion blur against darkness
- camera_package_description: close-up, eye level, portrait lens, push in, zoom subtle in, shallow subject, backlit
- environment_subzone: deep_space_void
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; deep_space_void; DESC_CH002_SC005; DESC_CH002_SC005_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: protagonist
- image2_role: environment reference for the scene location
- image2_asset: deep space void

# Continuity Notes
- Scene: CH002_SC005 / SC005.
- Variant: Primary Keyframe.
- Visual brightness and position of Mars in the sky
- Seamless transition from rocky_gorge_canyon to deep_space_void
- Cosmic displacement
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH002\CH002_SC005.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH002\CH002_SC005\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH002\CH002_SC005\SH003\DIALOGUE.json
