# Title
SH002 Shot Prompt - Primary Keyframe

# ID
CH001_SC004_SH002_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for the scene location. Primary keyframe with balanced composition and clear subject placement.. A man discovers a fallen comrade amidst a skirmish and attempts to flee while being pursued.. The subject from image1 is described character with stable costume and silhouette, foreground right within ambush site debris zone, weight of body vs Carter's injury, profile left toward the scene action, Carter kneeling. The subject from image2 is described character with stable costume and silhouette, john_carter plays against james_k_powell in the same frame. Preserve described environment with stable spatial continuity from image3, especially ambush site debris zone. weight of body vs Carter's injury. medium-full, low angle, wide lens, handheld, deep focus, high contrast ceremonial. Readable medium composition in that keeps, together so the physical effort stays obvious.. Carter lifting the body. ambush site debris zone. Keep continuity exact across costume, silhouette, lighting, and spatial relationships.. Avoid proper nouns in the prompt body unless text is meant to appear on screen.. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH001_SC004; SHOT_INDEX; DIALOGUE; john_carter; james_k_powell; apache_warriors
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
- scene_id: CH001_SC004
- chapter_id: CH001
- shot_type: medium
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in apache_plateau_camp that keeps john_carter, james_k_powell together so the physical effort stays obvious.
- shot_size: medium_full
- camera_angle: low_angle
- camera_motion: handheld
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: profile_left
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: james_k_powell
- primary_subject_frame_position: foreground right within ambush site debris zone
- primary_subject_scale_relation: weight of body vs Carter's injury
- primary_subject_facing_direction: profile left toward the scene action
- primary_subject_pose_description: Carter kneeling
- subject_relation_summary: john_carter plays against james_k_powell in the same frame
- scene_short_description: A man discovers a fallen comrade amidst a skirmish and attempts to flee while being pursued.
- shot_moment_summary: Carter lifting the body
- required_environment_anchor_1: ambush site debris zone
- required_scale_proof_detail: weight of body vs Carter's injury
- camera_package_description: medium-full, low angle, wide lens, handheld, deep focus, high contrast ceremonial
- environment_subzone: ambush site debris zone
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; james_k_powell; apache_plateau_camp; DESC_CH001_SC004; DESC_CH001_SC004_SH002
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
- Retrieval of the body
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH001\CH001_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH001\CH001_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH001\CH001_SC004\SH002\DIALOGUE.json
