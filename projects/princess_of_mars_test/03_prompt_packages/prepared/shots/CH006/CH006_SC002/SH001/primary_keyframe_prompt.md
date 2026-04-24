# Title
SH001 Shot Prompt - Primary Keyframe

# ID
CH006_SC002_SH001_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for the scene location. Primary keyframe with balanced composition and clear subject placement.. An Earthman uses a cudgel and precise strikes to kill two aggressive apes in a chamber.. The subject from image1 is described character with stable costume and silhouette, foreground entry line within wounded_zone, preserve readable body-to-environment scale in frame, front three-quarter left toward the scene action, protagonist panicking. The subject from image2 is described character with stable costume and silhouette, protagonist plays against watch_thing in the same frame. Preserve described environment with stable spatial continuity from image3, especially wounded_zone. preserve readable body-to-environment scale in frame. medium-full, eye level, normal lens, handheld, shallow subject, low key night. Readable medium composition in featuring, .. protagonist sees watch_thing losing. wounded_zone. Keep continuity exact across costume, silhouette, lighting, and spatial relationships.. Avoid proper nouns in the prompt body unless text is meant to appear on screen.. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH006_SC002; SHOT_INDEX; DIALOGUE; protagonist; watch_thing
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
- scene_id: CH006_SC002
- chapter_id: CH006
- shot_type: medium
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in martian_interior_chamber featuring protagonist, watch_thing.
- shot_size: medium_full
- camera_angle: eye_level
- camera_motion: handheld
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: low_key_night
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_left
- visible_primary_subject_id: protagonist
- visible_secondary_subject_ids: watch_thing
- primary_subject_frame_position: foreground entry line within wounded_zone
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: front three-quarter left toward the scene action
- primary_subject_pose_description: protagonist panicking
- subject_relation_summary: protagonist plays against watch_thing in the same frame
- scene_short_description: An Earthman uses a cudgel and precise strikes to kill two aggressive apes in a chamber.
- shot_moment_summary: protagonist sees watch_thing losing
- required_environment_anchor_1: wounded_zone
- required_scale_proof_detail: preserve readable body-to-environment scale in frame
- camera_package_description: medium-full, eye level, normal lens, handheld, shallow subject, low key night
- environment_subzone: wounded_zone
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; watch_thing; martian_interior_chamber; DESC_CH006_SC002; DESC_CH006_SC002_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: protagonist
- image2_role: identity reference for the secondary visible subject
- image2_asset: watch thing
- image3_role: environment reference for the scene location
- image3_asset: martian interior chamber

# Continuity Notes
- Scene: CH006_SC002 / SC002.
- Variant: Primary Keyframe.
- Direction of cudgel swings
- Blood splatter patterns
- Protagonist physical exhaustion levels
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH006\CH006_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH006\CH006_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH006\CH006_SC002\SH001\DIALOGUE.json
