# Title
SH003 Shot Prompt - Primary Keyframe

# ID
CH003_SC004_SH003_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for the scene location. Primary keyframe with balanced composition and clear subject placement.. A desperate escape via a massive thirty-foot leap across a mossy circular basin.. The subject from image1 is described character with stable costume and silhouette, foreground right within outer rim, height/size vs protagonist, facing directly toward camera, warriors frozen in observation. The subject from image2 is described character with stable costume and silhouette, martian_warriors plays against protagonist in same frame. Preserve described environment with stable spatial continuity from image3, especially low walled enclosure. height/size vs protagonist. medium-full, eye level, normal lens, locked off, zoom subtle in, shallow subject, diffuse ambient. Closing composition in emphasizing .. martian_warriors witness the landing. outer rim. Keep continuity exact across costume, silhouette, lighting, and spatial relationships.. Avoid proper nouns in the prompt body unless text is meant to appear on screen.. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH003_SC004; SHOT_INDEX; DIALOGUE; protagonist; martian_warriors
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
- scene_id: CH003_SC004
- chapter_id: CH003
- shot_type: closing_reaction
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Controlled closing frame that lands the consequence of the beat.
- composition: Closing composition in circular_moss_basin emphasizing martian observation of the feat.
- shot_size: medium_full
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: subtle_in
- focus_strategy: shallow_subject
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front
- visible_primary_subject_id: martian_warriors
- visible_secondary_subject_ids: protagonist
- primary_subject_frame_position: foreground right within outer rim
- primary_subject_scale_relation: height/size vs protagonist
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: warriors frozen in observation
- subject_relation_summary: martian_warriors plays against protagonist in same frame
- scene_short_description: A desperate escape via a massive thirty-foot leap across a mossy circular basin.
- shot_moment_summary: martian_warriors witness the landing
- required_environment_anchor_1: low walled enclosure
- required_scale_proof_detail: height/size vs protagonist
- camera_package_description: medium-full, eye level, normal lens, locked off, zoom subtle in, shallow subject, diffuse ambient
- environment_subzone: outer rim
- prompt_family: shot_prompt
- reference_asset_ids: martian_warriors; protagonist; circular_moss_basin; DESC_CH003_SC004; DESC_CH003_SC004_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: martian warriors
- image2_role: identity reference for the secondary visible subject
- image2_asset: protagonist
- image3_role: environment reference for the scene location
- image3_asset: circular moss basin

# Continuity Notes
- Scene: CH003_SC004 / SC004.
- Variant: Primary Keyframe.
- Precise trajectory and landing point relative to enclosure walls
- Visual scale relationship between martian_warriors and protagonist
- Precise trajectory and landing point of the jump relative to the enclosure walls
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH003\CH003_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC004\SH003\DIALOGUE.json
