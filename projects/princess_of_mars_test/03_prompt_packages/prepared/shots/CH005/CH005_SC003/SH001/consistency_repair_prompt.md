# Title
SH001 Shot Prompt - Consistency Repair

# ID
CH005_SC003_SH001_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for the scene location. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships.. A frantic chase through deserted Martian streets involving high-altitude jumping and relentless pursuit.. The subject from image1 is described character with stable costume and silhouette, foreground entry line within martian_city_streets, distance to next building, profile right toward the scene action, sprint begins. The subject from image2 is described character with stable costume and silhouette, protagonist plays against the_watch_dog in the same frame. Preserve described environment with stable spatial continuity from image3, especially martian_city_streets. distance to next building. full, eye level, wide lens, track, shallow subject, diffuse ambient. Dynamic composition in with clear pursuit vectors and readable movement for, .. protagonist sprints past a street corner. Keep continuity exact across costume, silhouette, lighting, and spatial relationships.. Avoid proper nouns in the prompt body unless text is meant to appear on screen.. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH005_SC003; SHOT_INDEX; DIALOGUE; protagonist; the_watch_dog
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
- scene_id: CH005_SC003
- chapter_id: CH005
- shot_type: action
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: Dynamic composition in martian_city_streets with clear pursuit vectors and readable movement for protagonist, the_watch_dog.
- shot_size: full
- camera_angle: eye_level
- camera_motion: track
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: profile_right
- visible_primary_subject_id: protagonist
- visible_secondary_subject_ids: the_watch_dog
- primary_subject_frame_position: foreground entry line within martian_city_streets
- primary_subject_scale_relation: distance to next building
- primary_subject_facing_direction: profile right toward the scene action
- primary_subject_pose_description: sprint begins
- subject_relation_summary: protagonist plays against the_watch_dog in the same frame
- scene_short_description: A frantic chase through deserted Martian streets involving high-altitude jumping and relentless pursuit.
- shot_moment_summary: protagonist sprints past a street corner
- required_environment_anchor_1: martian_city_streets
- required_scale_proof_detail: distance to next building
- camera_package_description: full, eye level, wide lens, track, shallow subject, diffuse ambient
- environment_subzone: martian_city_streets
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; the_watch_dog; martian_city_streets; DESC_CH005_SC003; DESC_CH005_SC003_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: protagonist
- image2_role: identity reference for the secondary visible subject
- image2_asset: the watch dog
- image3_role: environment reference for the scene location
- image3_asset: martian city streets

# Continuity Notes
- Scene: CH005_SC003 / SC003.
- Variant: Consistency Repair.
- Precise height and distance measurements for all jumps
- Timing of the_watch_dog arrival at street corners relative to protagonist position
- Initial sprint through streets
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH005\CH005_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH005\CH005_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH005\CH005_SC003\SH001\DIALOGUE.json
