# Title
SH003 Shot Prompt - Consistency Repair

# ID
CH005_SC002_SH003_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for the scene location. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships.. A captive attempts to exit a mural-decorated room before being pursued by a fast guard beast.. The subject from image1 is described character with stable costume and silhouette, foreground right within immediate hallway/threshold, distance between subjects, back to camera with head turned toward the action, protagonist turning to run. The subject from image2 is described character with stable costume and silhouette, protagonist plays against the_watch_dog in the same frame. Preserve described environment with stable spatial continuity from image3, especially immediate hallway/threshold. distance between subjects. medium-full, eye level, wide lens, handheld, deep focus, diffuse ambient. Dynamic composition in with clear pursuit vectors and readable movement for, .. protagonist running away from the beast. immediate hallway/threshold. Keep continuity exact across costume, silhouette, lighting, and spatial relationships.. Avoid proper nouns in the prompt body unless text is meant to appear on screen.. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH005_SC002; SHOT_INDEX; DIALOGUE; protagonist; the_watch_dog
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
- scene_id: CH005_SC002
- chapter_id: CH005
- shot_type: action
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: Dynamic composition in captive_chamber_murals with clear pursuit vectors and readable movement for protagonist, the_watch_dog.
- shot_size: medium_full
- camera_angle: eye_level
- camera_motion: handheld
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: back
- visible_primary_subject_id: protagonist
- visible_secondary_subject_ids: the_watch_dog
- primary_subject_frame_position: foreground right within immediate hallway/threshold
- primary_subject_scale_relation: distance between subjects
- primary_subject_facing_direction: back to camera with head turned toward the action
- primary_subject_pose_description: protagonist turning to run
- subject_relation_summary: protagonist plays against the_watch_dog in the same frame
- scene_short_description: A captive attempts to exit a mural-decorated room before being pursued by a fast guard beast.
- shot_moment_summary: protagonist running away from the beast
- required_environment_anchor_1: immediate hallway/threshold
- required_scale_proof_detail: distance between subjects
- camera_package_description: medium-full, eye level, wide lens, handheld, deep focus, diffuse ambient
- environment_subzone: immediate hallway/threshold
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; the_watch_dog; captive_chamber_murals; DESC_CH005_SC002; DESC_CH005_SC002_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: protagonist
- image2_role: identity reference for the secondary visible subject
- image2_asset: the watch dog
- image3_role: environment reference for the scene location
- image3_asset: captive chamber murals

# Continuity Notes
- Scene: CH005_SC002 / SC002.
- Variant: Consistency Repair.
- Physical distance between protagonist and the_watch_dog
- Direction of the chase through the threshold
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH005\CH005_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH005\CH005_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH005\CH005_SC002\SH003\DIALOGUE.json
