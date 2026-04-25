# Title
SH001 Shot Prompt - Primary Keyframe

# ID
CH003_SC005_SH001_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the environment reference for the scene location. Primary keyframe with balanced composition and clear subject placement. An unarmed leader offers a metal armlet to a transformed human in a yellowish moss basin. The subject from image1 is The Leader, foreground inside yellowish moss basin, Leader's unarmed status, front three-quarter left toward the scene action, standing face-to-face, dismounting. Preserve the environment from image2 especially yellowish moss basin. Keep one readable subject anchor: standing face-to-face, dismounting. medium-close, eye level, normal lens, locked off, shallow subject, diffuse ambient. Intimate composition that isolates and against to capture the beat's emotional turn. The Leader offers the metal armlet unarmed. yellowish moss basin. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH003_SC005; SHOT_INDEX; DIALOGUE; protagonist; martian_warriors
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: normal
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
- scene_id: CH003_SC005
- chapter_id: CH003
- shot_type: reaction_closeup
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates The Leader and protagonist against circular_moss_basin to capture the beat's emotional turn.
- shot_size: medium_close
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: front_three_quarter_left
- visible_primary_subject_id: protagonist
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground inside yellowish_moss_basin
- primary_subject_scale_relation: Leader's unarmed status
- primary_subject_facing_direction: front three-quarter left toward the scene action
- primary_subject_pose_description: standing face-to-face, dismounting
- subject_relation_summary: The Leader carries the frame alone
- scene_short_description: An unarmed leader offers a metal armlet to a transformed human in a yellowish moss basin.
- shot_moment_summary: The Leader offers the metal armlet unarmed
- required_environment_anchor_1: yellowish_moss_basin
- required_subject_anchor_1: standing face-to-face, dismounting
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: Leader's unarmed status
- camera_package_description: medium-close, eye level, normal lens, locked off, shallow subject, diffuse ambient
- environment_subzone: yellowish_moss_basin
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; circular_moss_basin; DESC_CH003_SC005; DESC_CH003_SC005_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: protagonist
- image2_role: environment reference for the scene location
- image2_asset: circular moss basin

# Continuity Notes
- Scene: CH003_SC005 / SC005.
- Variant: Primary Keyframe.
- Metal armlet must remain visible on protagonist's arm after acceptance
- Height differential during the lift onto the Martian mount
- The Leader must be unarmed
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH003\CH003_SC005.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC005\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC005\SH001\DIALOGUE.json
