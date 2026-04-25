# Title
SH003 Shot Prompt - Primary Keyframe

# ID
CH002_SC005_SH003_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the environment reference for the scene location. Primary keyframe with balanced composition and clear subject placement. A man gazes at a bright red star before being violently pulled into the dark void. The subject from image1 is protagonist, foreground right within deep space void, Human scale in rocky gorge vs. infinite cosmic scale of deep space, front three-quarter right toward the scene action, eyes closed. Preserve the environment from image2 especially deep space void. Keep one readable subject anchor: eyes closed. medium-full, dutch, wide lens, track, zoom strong in, environment priority, backlit. Closing composition in that emphasizes the consequence of violent cosmic displacement. violent transport through space. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH002_SC005; SHOT_INDEX; DIALOGUE; protagonist
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
- scene_id: CH002_SC005
- chapter_id: CH002
- shot_type: closing_reaction
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Controlled closing frame that lands the consequence of the beat.
- composition: Closing composition in deep_space_void that emphasizes the consequence of violent cosmic displacement.
- shot_size: medium_full
- camera_angle: dutch
- camera_motion: track
- zoom_behavior: strong_in
- focus_strategy: environment_priority
- lighting_style: backlit
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_right
- visible_primary_subject_id: protagonist
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground right within deep_space_void
- primary_subject_scale_relation: Human scale in rocky gorge vs. infinite cosmic scale of deep space.
- primary_subject_facing_direction: front three-quarter right toward the scene action
- primary_subject_pose_description: eyes closed
- subject_relation_summary: protagonist carries the frame alone
- scene_short_description: A man gazes at a bright red star before being violently pulled into the dark void.
- shot_moment_summary: violent transport through space
- required_environment_anchor_1: deep_space_void
- required_subject_anchor_1: eyes closed
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: Human scale in rocky gorge vs. infinite cosmic scale of deep space.
- camera_package_description: medium-full, dutch, wide lens, track, zoom strong in, environment priority, backlit
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
- Visual brightness and specific hue of Mars in the sky
- Seamless transition from rocky_gorge_canyon to deep_space_void
- Violent cosmic displacement
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH002\CH002_SC005.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH002\CH002_SC005\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH002\CH002_SC005\SH003\DIALOGUE.json
