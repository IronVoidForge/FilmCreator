# Title
SH002 Shot Prompt - Consistency Repair

# ID
CH002_SC004_SH002_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the environment reference for the scene location. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. A naked man flees a dark cavern into the vast moonlight of a rocky canyon. The subject from image1 is described character with stable costume and silhouette, foreground right within Cave Interior (Transitioning), narrow passage vs moving body, rear three-quarter left away from camera, protagonist running through shadows. Preserve described environment with stable spatial anchors from image2, especially Cave Interior (Transitioning). narrow passage vs moving body. full, low angle, wide lens, track, deep focus, high contrast ceremonial. Dynamic composition in with clear pursuit vectors and readable movement for . protagonist sprinting toward light. Cave Interior (Transitioning). Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH002_SC004; SHOT_INDEX; DIALOGUE; protagonist
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: wide
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
- scene_id: CH002_SC004
- chapter_id: CH002
- shot_type: action
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: Dynamic composition in rocky_gorge_canyon with clear pursuit vectors and readable movement for protagonist.
- shot_size: full
- camera_angle: low_angle
- camera_motion: track
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: rear_three_quarter_left
- visible_primary_subject_id: protagonist
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground right within Cave Interior (Transitioning)
- primary_subject_scale_relation: narrow passage vs moving body
- primary_subject_facing_direction: rear three-quarter left away from camera
- primary_subject_pose_description: protagonist running through shadows
- subject_relation_summary: protagonist carries the frame alone
- scene_short_description: A naked man flees a dark cavern into the vast moonlight of a rocky canyon.
- shot_moment_summary: protagonist sprinting toward light
- required_environment_anchor_1: Cave Interior (Transitioning)
- required_subject_anchor_1: cave mouth threshold
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: narrow passage vs moving body
- camera_package_description: full, low angle, wide lens, track, deep focus, high contrast ceremonial
- environment_subzone: Cave Interior (Transitioning)
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; rocky_gorge_canyon; DESC_CH002_SC004; DESC_CH002_SC004_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: protagonist
- image2_role: environment reference for the scene location
- image2_asset: rocky gorge canyon

# Continuity Notes
- Scene: CH002_SC004 / SC004.
- Variant: Consistency Repair.
- Protagonist nudity and physical state across light transitions
- Physical condition post-gas paralysis
- Frantic flight through the passage
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH002\CH002_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH002\CH002_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH002\CH002_SC004\SH002\DIALOGUE.json
