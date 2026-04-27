# Title
SH003 Shot Prompt - Primary Keyframe

# ID
CH010_SC005_SH003_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for lorquas ptomel audience chamber. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. A Thark leader confronts a human chieftain within a massive ceremonial audience chamber. The subject from image1 is john carter, foreground inside thark audience chamber dais area, Chapter-local beat subzone match for 'thark audience chamber dais area', facing directly toward camera, Carter meeting gaze. The subject from image2 is john carter plays against tars tarkas in the same frame. Preserve the environment from image3 Large scale, centered around a focal point for the presiding chieftain., monumental scale, dry open Martian terrain, especially thark audience chamber central dais. Keep one readable subject anchor: Carter meeting gaze. close-up, eye level, portrait lens, locked off, shallow subject, high contrast ceremonial. Intimate composition that isolates, against to capture the beat's emotional turn. Carter declares protection of Dejah Thoris. thark audience chamber dais area. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH010_SC005; SHOT_INDEX; DIALOGUE; john_carter; tars_tarkas
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
- scene_id: CH010_SC005
- chapter_id: CH010
- shot_type: reaction_closeup
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates john_carter, tars_tarkas against lorquas_ptomel_audience_chamber to capture the beat's emotional turn.
- shot_size: close_up
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: front
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: tars_tarkas
- primary_subject_frame_position: foreground inside thark_audience_chamber dais area
- primary_subject_scale_relation: Chapter-local beat subzone match for 'thark_audience_chamber dais area'.
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: Carter meeting gaze
- subject_relation_summary: john_carter plays against tars_tarkas in the same frame
- scene_short_description: A Thark leader confronts a human chieftain within a massive ceremonial audience chamber.
- shot_moment_summary: Carter declares protection of Dejah Thoris
- required_environment_anchor_1: thark_audience_chamber central dais
- required_subject_anchor_1: Carter meeting gaze
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: Chapter-local beat subzone match for 'thark_audience_chamber dais area'.
- camera_package_description: close-up, eye level, portrait lens, locked off, shallow subject, high contrast ceremonial
- environment_subzone: thark_audience_chamber dais area
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; tars_tarkas; lorquas_ptomel_audience_chamber; DESC_CH010_SC005; DESC_CH010_SC005_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: identity reference for the secondary visible subject
- image2_asset: tars tarkas
- image3_role: environment reference for the scene location
- image3_asset: lorquas ptomel audience chamber

# Continuity Notes
- Scene: CH010_SC005 / SC005.
- Variant: Primary Keyframe.
- Carter chieftain regalia
- Carter asserts his moral code and intent to protect Dejah Thoris
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH010\CH010_SC005.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH010\CH010_SC005\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH010\CH010_SC005\SH003\DIALOGUE.json
