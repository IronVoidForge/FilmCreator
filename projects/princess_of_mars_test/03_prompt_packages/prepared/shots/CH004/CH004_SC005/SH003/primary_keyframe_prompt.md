# Title
SH003 Shot Prompt - Primary Keyframe

# ID
CH004_SC005_SH003_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the environment reference for the scene location. Primary keyframe with balanced composition and clear subject placement.. A character is led into a decorated sleeping chamber to encounter a strange ten-legged creature.. The subject from image1 is described character with stable costume and silhouette, foreground inside creature sighting zone, Intimate interior scale contrasted against the enormous ancient city architecture., facing directly toward camera, creature stationary. Preserve described environment with stable spatial continuity from image2, especially creature sighting zone. Intimate interior scale contrasted against the enormous ancient city architecture.. close-up, low angle, portrait lens, locked off, zoom subtle in, shallow subject, low key night. Intimate composition that isolates, against to capture the beat's emotional turn.. close up of the ten-legged creature. creature sighting zone. Keep continuity exact across costume, silhouette, lighting, and spatial relationships.. Avoid proper nouns in the prompt body unless text is meant to appear on screen.. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH004_SC005; SHOT_INDEX; DIALOGUE; sola
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
- scene_id: CH004_SC005
- chapter_id: CH004
- shot_type: reaction_closeup
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates Small Martian Creature, The Narrator against martian_sleeping_chamber to capture the beat's emotional turn.
- shot_size: close_up
- camera_angle: low_angle
- camera_motion: locked_off
- zoom_behavior: subtle_in
- focus_strategy: shallow_subject
- lighting_style: low_key_night
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front
- visible_primary_subject_id: small martian creature
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground inside creature sighting zone
- primary_subject_scale_relation: Intimate interior scale contrasted against the enormous ancient city architecture.
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: creature stationary
- subject_relation_summary: Small Martian Creature plays against The Narrator in the same frame
- scene_short_description: A character is led into a decorated sleeping chamber to encounter a strange ten-legged creature.
- shot_moment_summary: close up of the ten-legged creature
- required_environment_anchor_1: creature sighting zone
- required_scale_proof_detail: Intimate interior scale contrasted against the enormous ancient city architecture.
- camera_package_description: close-up, low angle, portrait lens, locked off, zoom subtle in, shallow subject, low key night
- environment_subzone: creature sighting zone
- prompt_family: shot_prompt
- reference_asset_ids: martian_sleeping_chamber; DESC_CH004_SC005; DESC_CH004_SC005_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: small martian creature
- image2_role: environment reference for the scene location
- image2_asset: martian sleeping chamber

# Continuity Notes
- Scene: CH004_SC005 / SC005.
- Variant: Primary Keyframe.
- Small Martian Creature movement and physical appearance
- Ambient light levels within the chamber
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH004\CH004_SC005.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH004\CH004_SC005\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH004\CH004_SC005\SH003\DIALOGUE.json
