# Title
SH003 Shot Prompt - Consistency Repair

# ID
CH002_SC002_SH003_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for the scene location. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. Apache warriors approach a cave entrance under moonlight before fleeing in terror from an unseen sound. The subject from image1 is described character with stable costume and silhouette, midground inside rocky ledge/drop-off, preserve readable body-to-environment scale in frame, rear three-quarter left away from camera, running in panic. The subject from image2 is described character with stable costume and silhouette, apache_warriors plays against protagonist in the same frame. Preserve described environment with stable spatial anchors from image3, especially rocky ledge/drop-off. preserve readable body-to-environment scale in frame. wide, high angle, ultra-wide lens, handheld, deep focus, low key night. Dynamic composition in with clear pursuit vectors and readable movement for, . warriors flee and one falls. rocky ledge/drop-off. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH002_SC002; SHOT_INDEX; DIALOGUE; protagonist; apache_warriors
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: ultra_wide
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: consistency_repair
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH002_SC002
- chapter_id: CH002
- shot_type: action
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: Dynamic composition in rocky_gorge_canyon with clear pursuit vectors and readable movement for apache_warriors, protagonist.
- shot_size: wide
- camera_angle: high_angle
- camera_motion: handheld
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: low_key_night
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: rear_three_quarter_left
- visible_primary_subject_id: apache_warriors
- visible_secondary_subject_ids: protagonist
- primary_subject_frame_position: midground inside rocky ledge/drop-off
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: rear three-quarter left away from camera
- primary_subject_pose_description: running in panic
- subject_relation_summary: apache_warriors plays against protagonist in the same frame
- scene_short_description: Apache warriors approach a cave entrance under moonlight before fleeing in terror from an unseen sound.
- shot_moment_summary: warriors flee and one falls
- required_environment_anchor_1: rocky ledge/drop-off
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: preserve readable body-to-environment scale in frame
- camera_package_description: wide, high angle, ultra-wide lens, handheld, deep focus, low key night
- environment_subzone: rocky ledge/drop-off
- prompt_family: shot_prompt
- reference_asset_ids: apache_warriors; protagonist; rocky_gorge_canyon; DESC_CH002_SC002; DESC_CH002_SC002_SH003
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
- Warriors flee in panic; one falls to his death
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH002\CH002_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH002\CH002_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH002\CH002_SC002\SH003\DIALOGUE.json
