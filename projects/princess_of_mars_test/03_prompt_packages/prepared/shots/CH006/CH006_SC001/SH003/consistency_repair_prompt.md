# Title
SH003 Shot Prompt - Consistency Repair

# ID
CH006_SC001_SH003_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for the scene location. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships.. An Earthman pinned by a massive beast faces execution until a multi-legged creature intervenes.. The subject from image1 is described character with stable costume and silhouette, midground inside martian_interior_chamber floor, preserve readable body-to-environment scale in frame, front three-quarter right toward the scene action, watch_thing in motion. The subject from image2 is described character with stable costume and silhouette, watch_thing plays against The Mate (Bull Ape), protagonist in the same frame. Preserve described environment with stable spatial continuity from image3, especially martian_interior_chamber floor. watch_thing legs vs mate mass. wide, low angle, ultra-wide lens, handheld, deep focus, high contrast ceremonial. Wide composition across with, placed for immediate spatial orientation.. watch_thing leaping into combat. floor. Keep continuity exact across costume, silhouette, lighting, and spatial relationships.. Avoid proper nouns in the prompt body unless text is meant to appear on screen.. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH006_SC001; SHOT_INDEX; DIALOGUE; protagonist; watch_thing; bull_ape
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
- scene_id: CH006_SC001
- chapter_id: CH006
- shot_type: establishing_wide
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across martian_interior_chamber with watch_thing, The Mate (Bull Ape), protagonist placed for immediate spatial orientation.
- shot_size: wide
- camera_angle: low_angle
- camera_motion: handheld
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_right
- visible_primary_subject_id: watch_thing
- visible_secondary_subject_ids: protagonist
- primary_subject_frame_position: midground inside martian_interior_chamber floor
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: front three-quarter right toward the scene action
- primary_subject_pose_description: watch_thing in motion
- subject_relation_summary: watch_thing plays against The Mate (Bull Ape), protagonist in the same frame
- scene_short_description: An Earthman pinned by a massive beast faces execution until a multi-legged creature intervenes.
- shot_moment_summary: watch_thing leaping into combat
- required_environment_anchor_1: martian_interior_chamber floor
- required_scale_proof_detail: watch_thing legs vs mate mass
- camera_package_description: wide, low angle, ultra-wide lens, handheld, deep focus, high contrast ceremonial
- environment_subzone: martian_interior_chamber floor
- prompt_family: shot_prompt
- reference_asset_ids: watch_thing; protagonist; martian_interior_chamber; DESC_CH006_SC001; DESC_CH006_SC001_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: watch thing
- image2_role: identity reference for the secondary visible subject
- image2_asset: protagonist
- image3_role: environment reference for the scene location
- image3_asset: martian interior chamber

# Continuity Notes
- Scene: CH006_SC001 / SC001.
- Variant: Consistency Repair.
- physical injury state of watch_thing during fight
- bull_ape limb positioning during pinning
- location of the fallen stone cudgel
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH006\CH006_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH006\CH006_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH006\CH006_SC001\SH003\DIALOGUE.json
