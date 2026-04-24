# Title
SH001 Shot Prompt - Alternate Angle

# ID
CH005_SC002_SH001_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the environment reference for the scene location. Alternate angle with the same beat and preserved continuity.. A captive attempts to exit a mural-decorated room before being pursued by a fast guard beast.. The subject from image1 is described character with stable costume and silhouette, foreground entry line within captive_chamber_murals, protagonist height vs mural scale, profile right toward the scene action, protagonist standing still. Preserve described environment with stable spatial continuity from image2, especially captive_chamber_murals. protagonist height vs mural scale. medium-full, eye level, normal lens, push in, shallow subject, diffuse ambient. Readable medium composition in featuring .. protagonist approaches door with purpose. Keep continuity exact across costume, silhouette, lighting, and spatial relationships.. Avoid proper nouns in the prompt body unless text is meant to appear on screen.. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH005_SC002; SHOT_INDEX; DIALOGUE; protagonist; the_watch_dog
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: normal
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: alternate_angle
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH005_SC002
- chapter_id: CH005
- shot_type: medium
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in captive_chamber_murals featuring protagonist.
- shot_size: medium_full
- camera_angle: eye_level
- camera_motion: push_in
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: profile_right
- visible_primary_subject_id: protagonist
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground entry line within captive_chamber_murals
- primary_subject_scale_relation: protagonist height vs mural scale
- primary_subject_facing_direction: profile right toward the scene action
- primary_subject_pose_description: protagonist standing still
- subject_relation_summary: protagonist carries the frame alone
- scene_short_description: A captive attempts to exit a mural-decorated room before being pursued by a fast guard beast.
- shot_moment_summary: protagonist approaches door with purpose
- required_environment_anchor_1: captive_chamber_murals
- required_scale_proof_detail: protagonist height vs mural scale
- camera_package_description: medium-full, eye level, normal lens, push in, shallow subject, diffuse ambient
- environment_subzone: captive_chamber_murals
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; captive_chamber_murals; DESC_CH005_SC002; DESC_CH005_SC002_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: protagonist
- image2_role: environment reference for the scene location
- image2_asset: captive chamber murals

# Continuity Notes
- Scene: CH005_SC002 / SC002.
- Variant: Alternate Angle.
- Physical distance between protagonist and the_watch_dog
- Direction of the chase through the threshold
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH005\CH005_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH005\CH005_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH005\CH005_SC002\SH001\DIALOGUE.json
