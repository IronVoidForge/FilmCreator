# Title
SH001 Shot Prompt - Primary Keyframe

# ID
CH001_SC004_SH001_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for the scene location. Primary keyframe with balanced composition and clear subject placement.. A man discovers a fallen comrade amidst a skirmish and attempts to flee while being pursued.. The subject from image1 is described character with stable costume and silhouette, foreground inside ambush site debris zone, Individual survival against group pursuit within the narrow trail geography., front three-quarter left toward the scene action, Carter looking around skirmish. The subject from image2 is described character with stable costume and silhouette, john_carter plays against james_k_powell in the same frame. Preserve described environment with stable spatial continuity from image3, especially ambush site debris zone. arrow depth/placement. close-up, eye level, portrait lens, push in, zoom subtle in, shallow subject, high contrast ceremonial. Intimate composition that holds, against while preserving the fallen-body reveal.. Carter sees the arrows in Powell. ambush site debris zone. Keep continuity exact across costume, silhouette, lighting, and spatial relationships.. Avoid proper nouns in the prompt body unless text is meant to appear on screen.. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH001_SC004; SHOT_INDEX; DIALOGUE; john_carter; james_k_powell; apache_warriors
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: portrait
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
- scene_id: CH001_SC004
- chapter_id: CH001
- shot_type: reaction_closeup
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that holds john_carter, james_k_powell against apache_plateau_camp while preserving the fallen-body reveal.
- shot_size: close_up
- camera_angle: eye_level
- camera_motion: push_in
- zoom_behavior: subtle_in
- focus_strategy: shallow_subject
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_left
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: james_k_powell
- primary_subject_frame_position: foreground inside ambush site debris zone
- primary_subject_scale_relation: Individual survival against group pursuit within the narrow trail geography.
- primary_subject_facing_direction: front three-quarter left toward the scene action
- primary_subject_pose_description: Carter looking around skirmish
- subject_relation_summary: john_carter plays against james_k_powell in the same frame
- scene_short_description: A man discovers a fallen comrade amidst a skirmish and attempts to flee while being pursued.
- shot_moment_summary: Carter sees the arrows in Powell
- required_environment_anchor_1: ambush site debris zone
- required_scale_proof_detail: arrow depth/placement
- camera_package_description: close-up, eye level, portrait lens, push in, zoom subtle in, shallow subject, high contrast ceremonial
- environment_subzone: ambush site debris zone
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; james_k_powell; apache_plateau_camp; DESC_CH001_SC004; DESC_CH001_SC004_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: identity reference for the secondary visible subject
- image2_asset: james k powell
- image3_role: environment reference for the scene location
- image3_asset: apache plateau camp

# Continuity Notes
- Scene: CH001_SC004 / SC004.
- Variant: Primary Keyframe.
- Arrow placement on james_k_powell must remain static
- Injury level on john_carter must be consistent during physical exertion
- Proximity distance of apache_warriors to Carter
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH001\CH001_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH001\CH001_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH001\CH001_SC004\SH001\DIALOGUE.json
