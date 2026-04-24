# Title
SH001 Shot Prompt - Alternate Angle

# ID
CH006_SC004_SH001_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for the scene location. Alternate angle with the same beat and preserved continuity.. A warrior attempts to execute a wounded beast before the protagonist intervenes physically.. The subject from image1 is described character with stable costume and silhouette, foreground inside martian_interior_chamber, preserve readable body-to-environment scale in frame, profile left toward the scene action, warrior poised to strike. The subject from image2 is described character with stable costume and silhouette, martian_warrior plays against watch_thing in the same frame. Preserve described environment with stable spatial continuity from image3, especially martian_interior_chamber. watch_thing wounded state. medium-close, high angle, normal lens, locked off, shallow subject, low key night. Detail composition centered on the key physical action or prop inside .. martian_warrior prepares to strike watch_thing. Keep continuity exact across costume, silhouette, lighting, and spatial relationships.. Avoid proper nouns in the prompt body unless text is meant to appear on screen.. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH006_SC004; SHOT_INDEX; DIALOGUE; protagonist; sola; martian_warrior; watch_thing
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: normal
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: alternate_angle
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH006_SC004
- chapter_id: CH006
- shot_type: insert_detail
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Tight detail framing focused on a single visual object or gesture.
- composition: Detail composition centered on the key physical action or prop inside martian_interior_chamber.
- shot_size: medium_close
- camera_angle: high_angle
- camera_motion: locked_off
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: low_key_night
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: profile_left
- visible_primary_subject_id: martian_warrior
- visible_secondary_subject_ids: watch_thing
- primary_subject_frame_position: foreground inside martian_interior_chamber
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: profile left toward the scene action
- primary_subject_pose_description: warrior poised to strike
- subject_relation_summary: martian_warrior plays against watch_thing in the same frame
- scene_short_description: A warrior attempts to execute a wounded beast before the protagonist intervenes physically.
- shot_moment_summary: martian_warrior prepares to strike watch_thing
- required_environment_anchor_1: martian_interior_chamber
- required_scale_proof_detail: watch_thing wounded state
- camera_package_description: medium-close, high angle, normal lens, locked off, shallow subject, low key night
- environment_subzone: martian_interior_chamber
- prompt_family: shot_prompt
- reference_asset_ids: martian_warrior; watch_thing; martian_interior_chamber; DESC_CH006_SC004; DESC_CH006_SC004_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: martian warrior
- image2_role: identity reference for the secondary visible subject
- image2_asset: watch thing
- image3_role: environment reference for the scene location
- image3_asset: martian interior chamber

# Continuity Notes
- Scene: CH006_SC004 / SC004.
- Variant: Alternate Angle.
- Physical mobility status of watch_thing (wounded state)
- martian_warrior attempts to execute watch_thing
- Lighting transition from martian_interior_chamber to exterior Martian light
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH006\CH006_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH006\CH006_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH006\CH006_SC004\SH001\DIALOGUE.json
