# Title
SH001 Shot Prompt - Consistency Repair

# ID
CH002_SC003_SH001_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the environment reference for the scene location. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships.. A man struggles against paralysis before rising to find his clothed corpse lying on the cave floor.. The subject from image1 is described character with stable costume and silhouette, foreground entry line within arizona_mountain_cave_floor, preserve readable body-to-environment scale in frame, front three-quarter left toward the scene action, prone/still. Preserve described environment with stable spatial continuity from image2, especially rocky_cave_floor. preserve readable body-to-environment scale in frame. medium, low angle, normal lens, handheld, shallow subject, low key night. Dynamic composition in with clear pursuit vectors and readable movement for .. protagonist fighting paralysis. _floor. Keep continuity exact across costume, silhouette, lighting, and spatial relationships.. Avoid proper nouns in the prompt body unless text is meant to appear on screen.. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH002_SC003; SHOT_INDEX; DIALOGUE; protagonist
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: normal
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
- scene_id: CH002_SC003
- chapter_id: CH002
- shot_type: action
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: Dynamic composition in arizona_mountain_cave with clear pursuit vectors and readable movement for protagonist.
- shot_size: medium
- camera_angle: low_angle
- camera_motion: handheld
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: low_key_night
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_left
- visible_primary_subject_id: protagonist
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground entry line within arizona_mountain_cave_floor
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: front three-quarter left toward the scene action
- primary_subject_pose_description: prone/still
- subject_relation_summary: protagonist carries the frame alone
- scene_short_description: A man struggles against paralysis before rising to find his clothed corpse lying on the cave floor.
- shot_moment_summary: protagonist fighting paralysis
- required_environment_anchor_1: rocky_cave_floor
- required_scale_proof_detail: preserve readable body-to-environment scale in frame
- camera_package_description: medium, low angle, normal lens, handheld, shallow subject, low key night
- environment_subzone: arizona_mountain_cave_floor
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; arizona_mountain_cave; DESC_CH002_SC003; DESC_CH002_SC003_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: protagonist
- image2_role: environment reference for the scene location
- image2_asset: arizona mountain cave

# Continuity Notes
- Scene: CH002_SC003 / SC003.
- Variant: Consistency Repair.
- Exact spatial placement of old body relative to new self's standing position
- Lighting consistency between the two versions of the character
- Mental struggle to break paralysis
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH002\CH002_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH002\CH002_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH002\CH002_SC003\SH001\DIALOGUE.json
