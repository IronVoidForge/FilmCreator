# Title
SH002 Shot Prompt - Consistency Repair

# ID
CH002_SC002_SH002_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for the scene location. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. Apache warriors approach a dark cave entrance under moonlight before fleeing in terror. The subject from image1 is apache warriors, foreground right within cave mouth, The vastness of the rocky gorge canyon vs the small scale of the approaching group, facing directly toward camera, warriors frozen. The subject from image2 is apache warriors plays against protagonist in the same frame. Preserve the environment from image3 especially cave mouth. medium-full, eye level, normal lens, handheld, zoom subtle in, shallow subject, low key night. Readable medium composition in featuring. terrifying low moan from cave depths. cave mouth. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH002_SC002; SHOT_INDEX; DIALOGUE; protagonist; apache_warriors
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: normal
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: consistency_repair
- review_notes: SH002: subject anchor is missing or not body/detail-specific enough.; Prompt body is using a non-body/detail subject anchor.
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH002_SC002
- chapter_id: CH002
- shot_type: medium
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in rocky_gorge_canyon featuring apache_warriors, protagonist.
- shot_size: medium_full
- camera_angle: eye_level
- camera_motion: handheld
- zoom_behavior: subtle_in
- focus_strategy: shallow_subject
- lighting_style: low_key_night
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: front
- visible_primary_subject_id: apache_warriors
- visible_secondary_subject_ids: protagonist
- primary_subject_frame_position: foreground right within cave_mouth
- primary_subject_scale_relation: The vastness of the rocky_gorge_canyon vs the small scale of the approaching group.
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: warriors frozen
- subject_relation_summary: apache_warriors plays against protagonist in the same frame
- scene_short_description: Apache warriors approach a dark cave entrance under moonlight before fleeing in terror.
- shot_moment_summary: terrifying low moan from cave depths
- required_environment_anchor_1: cave_mouth
- required_subject_anchor_1: cave_mouth
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: The vastness of the rocky_gorge_canyon vs the small scale of the approaching group.
- camera_package_description: medium-full, eye level, normal lens, handheld, zoom subtle in, shallow subject, low key night
- environment_subzone: cave_mouth
- prompt_family: shot_prompt
- reference_asset_ids: apache_warriors; protagonist; rocky_gorge_canyon; DESC_CH002_SC002; DESC_CH002_SC002_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: apache warriors
- image2_role: identity reference for the secondary visible subject
- image2_asset: protagonist
- image3_role: environment reference for the scene location
- image3_asset: rocky gorge canyon

# Continuity Notes
- Scene: CH002_SC002 / SC002.
- Variant: Consistency Repair.
- Distance between apache_warriors and cave mouth
- Timing of moaning sound relative to character reaction
- Directional source of audio from cave depths
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH002\CH002_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH002\CH002_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH002\CH002_SC002\SH002\DIALOGUE.json
