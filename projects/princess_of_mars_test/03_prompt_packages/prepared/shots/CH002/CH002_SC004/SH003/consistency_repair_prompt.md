# Title
SH003 Shot Prompt - Consistency Repair

# ID
CH002_SC004_SH003_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the environment reference for the scene location. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. A naked man flees a dark cavern into the vast, moonlit rocky gorge. The subject from image1 is protagonist, midground inside rocky gorge canyon, preserve readable body-to-environment scale in frame, front three-quarter right toward the scene action, leaping from cave mouth onto ridge. Preserve the environment from image2 especially rocky gorge canyon rim. Keep celestial anchor the moonlight stable in the frame. vast landscape vs small human. wide, high angle, ultra-wide lens, pull back, deep focus, low key night. Dynamic composition in clear pursuit vectors and readable movement. protagonist emerges into moonlight. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH002_SC004; SHOT_INDEX; DIALOGUE; protagonist
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: ultra_wide
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: consistency_repair
- review_notes: SH003: subject anchor is missing or not body/detail-specific enough.; Prompt body is using a non-body/detail subject anchor.
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH002_SC004
- chapter_id: CH002
- shot_type: action
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: Dynamic composition in rocky_gorge_canyon with clear pursuit vectors and readable movement for protagonist.
- shot_size: wide
- camera_angle: high_angle
- camera_motion: pull_back
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: low_key_night
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_right
- visible_primary_subject_id: protagonist
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: midground inside rocky_gorge_canyon
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: front three-quarter right toward the scene action
- primary_subject_pose_description: leaping from cave mouth onto ridge
- subject_relation_summary: protagonist carries the frame alone
- scene_short_description: A naked man flees a dark cavern into the vast, moonlit rocky gorge.
- shot_moment_summary: protagonist emerges into moonlight
- required_environment_anchor_1: rocky_gorge_canyon rim
- required_subject_anchor_1: leaping from cave mouth onto ridge
- required_celestial_anchor_1: protagonist emerges into moonlight
- required_scale_proof_detail: vast landscape vs small human
- camera_package_description: wide, high angle, ultra-wide lens, pull back, deep focus, low key night
- environment_subzone: rocky_gorge_canyon
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; rocky_gorge_canyon; DESC_CH002_SC004; DESC_CH002_SC004_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: protagonist
- image2_role: environment reference for the scene location
- image2_asset: rocky gorge canyon

# Continuity Notes
- Scene: CH002_SC004 / SC004.
- Variant: Consistency Repair.
- Protagonist nudity and physical state across light levels
- Physical agility/leaping capabilities during flight
- Emergence into the vast canyon
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH002\CH002_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH002\CH002_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH002\CH002_SC004\SH003\DIALOGUE.json
