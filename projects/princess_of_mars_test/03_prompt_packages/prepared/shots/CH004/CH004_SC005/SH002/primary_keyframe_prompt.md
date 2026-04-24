# Title
SH002 Shot Prompt - Primary Keyframe

# ID
CH004_SC005_SH002_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for the scene location. Primary keyframe with balanced composition and clear subject placement.. A character is led into a decorated sleeping chamber to encounter a strange ten-legged creature.. The subject from image1 is described character with stable costume and silhouette, foreground right within decor zone, Intimate interior scale contrasted against the enormous ancient city architecture., front three-quarter right toward the scene action, narrator entering. The subject from image2 is described character with stable costume and silhouette, The Narrator plays against sola in the same frame. Preserve described environment with stable spatial continuity from image3, especially decor zone. Intimate interior scale contrasted against the enormous ancient city architecture.. medium, eye level, normal lens, pan, environment priority, low key night. Readable medium composition in featuring, .. narrator views the decorated room. decor zone. Keep continuity exact across costume, silhouette, lighting, and spatial relationships.. Avoid proper nouns in the prompt body unless text is meant to appear on screen.. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH004_SC005; SHOT_INDEX; DIALOGUE; sola
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
- scene_id: CH004_SC005
- chapter_id: CH004
- shot_type: medium
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in martian_sleeping_chamber featuring The Narrator, sola.
- shot_size: medium
- camera_angle: eye_level
- camera_motion: pan
- zoom_behavior: none
- focus_strategy: environment_priority
- lighting_style: low_key_night
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_right
- visible_primary_subject_id: the narrator
- visible_secondary_subject_ids: sola
- primary_subject_frame_position: foreground right within decor zone
- primary_subject_scale_relation: Intimate interior scale contrasted against the enormous ancient city architecture.
- primary_subject_facing_direction: front three-quarter right toward the scene action
- primary_subject_pose_description: narrator entering
- subject_relation_summary: The Narrator plays against sola in the same frame
- scene_short_description: A character is led into a decorated sleeping chamber to encounter a strange ten-legged creature.
- shot_moment_summary: narrator views the decorated room
- required_environment_anchor_1: decor zone
- required_scale_proof_detail: Intimate interior scale contrasted against the enormous ancient city architecture.
- camera_package_description: medium, eye level, normal lens, pan, environment priority, low key night
- environment_subzone: decor zone
- prompt_family: shot_prompt
- reference_asset_ids: sola; martian_sleeping_chamber; DESC_CH004_SC005; DESC_CH004_SC005_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: the narrator
- image2_role: identity reference for the secondary visible subject
- image2_asset: sola
- image3_role: environment reference for the scene location
- image3_asset: martian sleeping chamber

# Continuity Notes
- Scene: CH004_SC005 / SC005.
- Variant: Primary Keyframe.
- Small Martian Creature movement and physical appearance
- Ambient light levels within the chamber
- Exploring the chamber
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH004\CH004_SC005.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH004\CH004_SC005\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH004\CH004_SC005\SH002\DIALOGUE.json
