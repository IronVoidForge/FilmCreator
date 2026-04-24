# Title
SH001 Shot Prompt - Primary Keyframe

# ID
CH002_SC002_SH001_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for the scene location. Primary keyframe with balanced composition and clear subject placement. Apache warriors approach a cave entrance under moonlight before fleeing in terror from an unseen sound. The subject from image1 is described character with stable costume and silhouette, midground inside rocky_gorge_canyon floor, warriors appear small against gorge walls, front three-quarter right toward the scene action, warriors walking. The subject from image2 is described character with stable costume and silhouette, apache_warriors plays against protagonist in the same frame. Preserve described environment with stable spatial anchors from image3, especially rocky_gorge_canyon floor. warriors appear small against gorge walls. wide, low angle, wide lens, track, deep focus, low key night. Wide composition across with, placed for immediate spatial orientation. warriors move toward cave mouth. floor. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH002_SC002; SHOT_INDEX; DIALOGUE; protagonist; apache_warriors
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
- scene_id: CH002_SC002
- chapter_id: CH002
- shot_type: establishing_wide
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across rocky_gorge_canyon with apache_warriors, protagonist placed for immediate spatial orientation.
- shot_size: wide
- camera_angle: low_angle
- camera_motion: track
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: low_key_night
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_right
- visible_primary_subject_id: apache_warriors
- visible_secondary_subject_ids: protagonist
- primary_subject_frame_position: midground inside rocky_gorge_canyon floor
- primary_subject_scale_relation: warriors appear small against gorge walls
- primary_subject_facing_direction: front three-quarter right toward the scene action
- primary_subject_pose_description: warriors walking
- subject_relation_summary: apache_warriors plays against protagonist in the same frame
- scene_short_description: Apache warriors approach a cave entrance under moonlight before fleeing in terror from an unseen sound.
- shot_moment_summary: warriors move toward cave mouth
- required_environment_anchor_1: rocky_gorge_canyon floor
- required_subject_anchor_1: cave mouth
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: warriors appear small against gorge walls
- camera_package_description: wide, low angle, wide lens, track, deep focus, low key night
- environment_subzone: rocky_gorge_canyon floor
- prompt_family: shot_prompt
- reference_asset_ids: apache_warriors; protagonist; rocky_gorge_canyon; DESC_CH002_SC002; DESC_CH002_SC002_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: apache warriors
- image2_role: identity reference for the secondary visible subject
- image2_asset: protagonist
- image3_role: environment reference for the scene location
- image3_asset: rocky gorge canyon

# Continuity Notes
- Scene: CH002_SC002 / SC002.
- Variant: Primary Keyframe.
- Distance between apache_warriors and cave mouth
- Timing of moaning sound relative to character reaction
- Apache warriors approach the cave entrance
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH002\CH002_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH002\CH002_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH002\CH002_SC002\SH001\DIALOGUE.json
