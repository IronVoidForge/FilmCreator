# Title
SH002 Shot Prompt - Primary Keyframe

# ID
CH006_SC002_SH002_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the environment reference for the scene location. Primary keyframe with balanced composition and clear subject placement.. An Earthman uses a cudgel and precise strikes to kill two aggressive apes in a chamber.. The subject from image1 is described character with stable costume and silhouette, foreground right within combat_zone, preserve readable body-to-environment scale in frame, profile right toward the scene action, swinging cudgel. Preserve described environment with stable spatial continuity from image2, especially combat_zone. preserve readable body-to-environment scale in frame. medium, low angle, wide lens, handheld, deep focus, low key night. Dynamic composition in with clear pursuit vectors and readable movement for, .. cudgel strike kills first ape. combat_zone. Keep continuity exact across costume, silhouette, lighting, and spatial relationships.. Avoid proper nouns in the prompt body unless text is meant to appear on screen.. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH006_SC002; SHOT_INDEX; DIALOGUE; protagonist; watch_thing
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
- scene_id: CH006_SC002
- chapter_id: CH006
- shot_type: action
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: Dynamic composition in martian_interior_chamber with clear pursuit vectors and readable movement for protagonist, The Mate (Bull Ape).
- shot_size: medium
- camera_angle: low_angle
- camera_motion: handheld
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: low_key_night
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: profile_right
- visible_primary_subject_id: protagonist
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground right within combat_zone
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: profile right toward the scene action
- primary_subject_pose_description: swinging cudgel
- subject_relation_summary: protagonist plays against The Mate (Bull Ape) in the same frame
- scene_short_description: An Earthman uses a cudgel and precise strikes to kill two aggressive apes in a chamber.
- shot_moment_summary: cudgel strike kills first ape
- required_environment_anchor_1: combat_zone
- required_scale_proof_detail: preserve readable body-to-environment scale in frame
- camera_package_description: medium, low angle, wide lens, handheld, deep focus, low key night
- environment_subzone: combat_zone
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; martian_interior_chamber; DESC_CH006_SC002; DESC_CH006_SC002_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: protagonist
- image2_role: environment reference for the scene location
- image2_asset: martian interior chamber

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
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH006\CH006_SC002\SH002\DIALOGUE.json
