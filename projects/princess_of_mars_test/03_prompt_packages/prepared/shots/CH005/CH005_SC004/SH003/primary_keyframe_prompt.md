# Title
SH003 Shot Prompt - Primary Keyframe

# ID
CH005_SC004_SH003_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for the scene location. Primary keyframe with balanced composition and clear subject placement.. A desperate leap toward a high window ends in an interception by a massive white creature.. The subject from image1 is described character with stable costume and silhouette, foreground inside valley_overlook_exterior, Human-sized protagonist vs. colossal, ape-like creature., facing directly toward camera, contact made. The subject from image2 is described character with stable costume and silhouette, protagonist plays against the_colossal_creature in the same frame. Preserve described environment with stable spatial continuity from image3, especially valley_overlook_exterior. Human-sized protagonist vs. colossal, ape-like creature.. extreme-close-up, eye level, portrait lens, handheld, zoom subtle in, shallow subject, hard directional. Intimate composition that isolates, against to capture the beat's emotional turn.. extreme close up of protagonist's face during grab. Keep continuity exact across costume, silhouette, lighting, and spatial relationships.. Avoid proper nouns in the prompt body unless text is meant to appear on screen.. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH005_SC004; SHOT_INDEX; DIALOGUE; protagonist; the_watch_dog; the_colossal_creature
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
- scene_id: CH005_SC004
- chapter_id: CH005
- shot_type: reaction_closeup
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates protagonist, the_colossal_creature against valley_overlook_exterior to capture the beat's emotional turn.
- shot_size: extreme_close_up
- camera_angle: eye_level
- camera_motion: handheld
- zoom_behavior: subtle_in
- focus_strategy: shallow_subject
- lighting_style: hard_directional
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front
- visible_primary_subject_id: protagonist
- visible_secondary_subject_ids: the_colossal_creature
- primary_subject_frame_position: foreground inside valley_overlook_exterior
- primary_subject_scale_relation: Human-sized protagonist vs. colossal, ape-like creature.
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: contact made
- subject_relation_summary: protagonist plays against the_colossal_creature in the same frame
- scene_short_description: A desperate leap toward a high window ends in an interception by a massive white creature.
- shot_moment_summary: extreme close up of protagonist's face during grab
- required_environment_anchor_1: valley_overlook_exterior
- required_scale_proof_detail: Human-sized protagonist vs. colossal, ape-like creature.
- camera_package_description: extreme-close-up, eye level, portrait lens, handheld, zoom subtle in, shallow subject, hard directional
- environment_subzone: valley_overlook_exterior
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; the_colossal_creature; valley_overlook_exterior; DESC_CH005_SC004; DESC_CH005_SC004_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: protagonist
- image2_role: identity reference for the secondary visible subject
- image2_asset: the colossal creature
- image3_role: environment reference for the scene location
- image3_asset: valley overlook exterior

# Continuity Notes
- Scene: CH005_SC004 / SC004.
- Variant: Primary Keyframe.
- Window height must remain fixed at thirty feet above ground
- Physical contact point between protagonist and the_colossal_creature
- Lighting shift from bright city streets to dark captive_chamber_murals
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH005\CH005_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH005\CH005_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH005\CH005_SC004\SH003\DIALOGUE.json
