# Title
SH003 Shot Prompt - Primary Keyframe

# ID
CH004_SC001_SH003_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for the scene location. Primary keyframe with balanced composition and clear subject placement.. A small figure and a large companion enter a massive marble and gold plaza filled with hundreds of Martians.. The subject from image1 is described character with stable costume and silhouette, foreground right within crowd_density_zone, Crowd density blocking horizon, facing directly toward camera, Looking up at Martians. The subject from image2 is described character with stable costume and silhouette, The Narrator plays against Various Martians (crowd) in the same frame. Preserve described environment with stable spatial continuity from image3, especially crowd_density_zone. Crowd density blocking horizon. medium-full, eye level, normal lens, handheld, shallow subject, diffuse ambient. Closing composition in that emphasizes the consequence of overwhelmed by the crowd.. POV of the overwhelming crowd from Narrator's eye level. crowd_density_zone. Keep continuity exact across costume, silhouette, lighting, and spatial relationships.. Avoid proper nouns in the prompt body unless text is meant to appear on screen.. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH004_SC001; SHOT_INDEX; DIALOGUE; tars_tarkas
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
- scene_id: CH004_SC001
- chapter_id: CH004
- shot_type: closing_reaction
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Controlled closing frame that lands the consequence of the beat.
- composition: Closing composition in ancient_martian_city_plaza that emphasizes the consequence of overwhelmed by the crowd.
- shot_size: medium_full
- camera_angle: eye_level
- camera_motion: handheld
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: internal_monologue
- primary_subject_angle: front
- visible_primary_subject_id: the narrator
- visible_secondary_subject_ids: various martians (crowd)
- primary_subject_frame_position: foreground right within crowd_density_zone
- primary_subject_scale_relation: Crowd density blocking horizon
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: Looking up at Martians
- subject_relation_summary: The Narrator plays against Various Martians (crowd) in the same frame
- scene_short_description: A small figure and a large companion enter a massive marble and gold plaza filled with hundreds of Martians.
- shot_moment_summary: POV of the overwhelming crowd from Narrator's eye level
- required_environment_anchor_1: crowd_density_zone
- required_scale_proof_detail: Crowd density blocking horizon
- camera_package_description: medium-full, eye level, normal lens, handheld, shallow subject, diffuse ambient
- environment_subzone: crowd_density_zone
- prompt_family: shot_prompt
- reference_asset_ids: ancient_martian_city_plaza; DESC_CH004_SC001; DESC_CH004_SC001_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: the narrator
- image2_role: identity reference for the secondary visible subject
- image2_asset: various martians crowd
- image3_role: environment reference for the scene location
- image3_asset: ancient martian city plaza

# Continuity Notes
- Scene: CH004_SC001 / SC001.
- Variant: Primary Keyframe.
- Architecture and prop scale relative to The Narrator
- Movement patterns and density of Various Martians (crowd)
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH004\CH004_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH004\CH004_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH004\CH004_SC001\SH003\DIALOGUE.json
