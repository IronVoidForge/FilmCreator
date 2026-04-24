# Title
SH002 Shot Prompt - Primary Keyframe

# ID
CH006_SC001_SH002_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for the scene location. Use image4 as the identity reference for an additional visible subject. Primary keyframe with balanced composition and clear subject placement.. An Earthman pinned by a massive beast faces execution until a multi-legged creature intervenes.. The subject from image1 is described character with stable costume and silhouette, foreground right within chamber entrance/plaza threshold, cudgel size relative to mate, profile left toward the scene action, mate approaching. The subject from image2 is described character with stable costume and silhouette, The Mate (Bull Ape) plays against protagonist, bull_ape in the same frame. Preserve described environment with stable spatial continuity from image3, especially chamber entrance/plaza threshold. cudgel size relative to mate. medium-full, eye level, wide lens, pan, deep focus, hard directional. Readable medium composition in featuring, .. The Mate (Bull Ape) raising stone cudgel. chamber entrance/plaza threshold. Keep continuity exact across costume, silhouette, lighting, and spatial relationships.. Avoid proper nouns in the prompt body unless text is meant to appear on screen.. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH006_SC001; SHOT_INDEX; DIALOGUE; protagonist; watch_thing; bull_ape
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
- scene_id: CH006_SC001
- chapter_id: CH006
- shot_type: medium
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in martian_interior_chamber featuring The Mate (Bull Ape), protagonist, bull_ape.
- shot_size: medium_full
- camera_angle: eye_level
- camera_motion: pan
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: hard_directional
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: profile_left
- visible_primary_subject_id: the mate (bull ape)
- visible_secondary_subject_ids: protagonist; bull_ape
- primary_subject_frame_position: foreground right within chamber entrance/plaza threshold
- primary_subject_scale_relation: cudgel size relative to mate
- primary_subject_facing_direction: profile left toward the scene action
- primary_subject_pose_description: mate approaching
- subject_relation_summary: The Mate (Bull Ape) plays against protagonist, bull_ape in the same frame
- scene_short_description: An Earthman pinned by a massive beast faces execution until a multi-legged creature intervenes.
- shot_moment_summary: The Mate (Bull Ape) raising stone cudgel
- required_environment_anchor_1: chamber entrance/plaza threshold
- required_scale_proof_detail: cudgel size relative to mate
- camera_package_description: medium-full, eye level, wide lens, pan, deep focus, hard directional
- environment_subzone: chamber entrance/plaza threshold
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; bull_ape; martian_interior_chamber; DESC_CH006_SC001; DESC_CH006_SC001_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: the mate bull ape
- image2_role: identity reference for the secondary visible subject
- image2_asset: protagonist
- image3_role: environment reference for the scene location
- image3_asset: martian interior chamber
- image4_role: identity reference for an additional visible subject
- image4_asset: bull ape

# Continuity Notes
- Scene: CH006_SC001 / SC001.
- Variant: Primary Keyframe.
- location of the fallen stone cudgel
- bull_ape limb positioning during pinning
- physical injury state of watch_thing during fight
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH006\CH006_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH006\CH006_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH006\CH006_SC001\SH002\DIALOGUE.json
