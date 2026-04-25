# Title
SH002 Shot Prompt - Alternate Angle

# ID
CH002_SC004_SH002_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the environment reference for the scene location. Alternate angle with the same beat and preserved continuity. A naked man flees a dark cavern into the expansive moonlit rocky gorge. The subject from image1 is protagonist, foreground right within Cave Interior (Transitioning), preserve readable body-to-environment scale in frame, rear three-quarter left away from camera, subject in shadow. Preserve the environment from image2 especially Cave Interior (Transitioning). Keep celestial anchor the moonlight stable in the frame. full, eye level, wide lens, track, deep focus, high contrast ceremonial. Dynamic composition in clear pursuit vectors and readable movement. protagonist breaks into moonlight. Cave Interior (Transitioning). Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH002_SC004; SHOT_INDEX; DIALOGUE; protagonist
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: wide
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: alternate_angle
- review_notes: SH002: subject anchor is missing or not body/detail-specific enough.; Prompt body is using a non-body/detail subject anchor.
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
- camera_angle: eye_level
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
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: rear three-quarter left away from camera
- primary_subject_pose_description: subject in shadow
- subject_relation_summary: protagonist carries the frame alone
- scene_short_description: A naked man flees a dark cavern into the expansive moonlit rocky gorge.
- shot_moment_summary: protagonist breaks into moonlight
- required_environment_anchor_1: Cave Interior (Transitioning)
- required_subject_anchor_1: Cave mouth threshold
- required_celestial_anchor_1: protagonist breaks into moonlight
- required_scale_proof_detail: preserve readable body-to-environment scale in frame
- camera_package_description: full, eye level, wide lens, track, deep focus, high contrast ceremonial
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
- Variant: Alternate Angle.
- Protagonist nudity and physical state across light level transitions
- Physical agility/leaping capabilities during flight
- Flight toward the exit
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH002\CH002_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH002\CH002_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH002\CH002_SC004\SH002\DIALOGUE.json
