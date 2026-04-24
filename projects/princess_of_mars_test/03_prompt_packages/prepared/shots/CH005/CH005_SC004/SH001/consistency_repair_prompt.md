# Title
SH001 Shot Prompt - Consistency Repair

# ID
CH005_SC004_SH001_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for the scene location. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships.. A desperate leap toward a high window ends in an interception by a massive white creature.. The subject from image1 is described character with stable costume and silhouette, midground inside valley_overlook_exterior, 30ft height relative to ground, profile left toward the scene action, protagonist running. The subject from image2 is described character with stable costume and silhouette, protagonist plays against the_watch_dog in the same frame. Preserve described environment with stable spatial continuity from image3, especially valley_overlook_exterior. 30ft height relative to ground. wide, low angle, wide lens, track, deep focus, hard directional. Dynamic composition in with clear pursuit vectors and readable movement for, .. protagonist leaps toward the window. Keep continuity exact across costume, silhouette, lighting, and spatial relationships.. Avoid proper nouns in the prompt body unless text is meant to appear on screen.. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH005_SC004; SHOT_INDEX; DIALOGUE; protagonist; the_watch_dog; the_colossal_creature
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: wide
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
- scene_id: CH005_SC004
- chapter_id: CH005
- shot_type: action
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: Dynamic composition in valley_overlook_exterior with clear pursuit vectors and readable movement for protagonist, the_watch_dog.
- shot_size: wide
- camera_angle: low_angle
- camera_motion: track
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: hard_directional
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: profile_left
- visible_primary_subject_id: protagonist
- visible_secondary_subject_ids: the_watch_dog
- primary_subject_frame_position: midground inside valley_overlook_exterior
- primary_subject_scale_relation: 30ft height relative to ground
- primary_subject_facing_direction: profile left toward the scene action
- primary_subject_pose_description: protagonist running
- subject_relation_summary: protagonist plays against the_watch_dog in the same frame
- scene_short_description: A desperate leap toward a high window ends in an interception by a massive white creature.
- shot_moment_summary: protagonist leaps toward the window
- required_environment_anchor_1: valley_overlook_exterior
- required_scale_proof_detail: 30ft height relative to ground
- camera_package_description: wide, low angle, wide lens, track, deep focus, hard directional
- environment_subzone: valley_overlook_exterior
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; the_watch_dog; valley_overlook_exterior; DESC_CH005_SC004; DESC_CH005_SC004_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: protagonist
- image2_role: identity reference for the secondary visible subject
- image2_asset: the watch dog
- image3_role: environment reference for the scene location
- image3_asset: valley overlook exterior

# Continuity Notes
- Scene: CH005_SC004 / SC004.
- Variant: Consistency Repair.
- Window height must remain fixed at thirty feet above ground
- Physical contact point between protagonist and the_colossal_creature
- Lighting shift from bright city streets to dark captive_chamber_murals
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH005\CH005_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH005\CH005_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH005\CH005_SC004\SH001\DIALOGUE.json
