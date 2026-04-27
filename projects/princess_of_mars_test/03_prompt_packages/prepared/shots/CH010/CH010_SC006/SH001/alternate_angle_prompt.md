# Title
SH001 Shot Prompt - Alternate Angle

# ID
CH010_SC006_SH001_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for lorquas ptomel audience chamber. Use image4 as the identity reference for an additional visible subject. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. A group consisting of a man, a woman, and a creature exits a massive ceremonial hall. The subject from image1 is john carter, midground inside thark audience chamber main floor, height of chamber walls vs character height, front three-quarter right toward the scene action, characters standing in tension. The subject from image2 is john carter plays against dejah thoris, woola in the same frame. Preserve the environment from image3 Large scale, centered around a focal point for the presiding chieftain., monumental scale, dry open Martian terrain, especially thark audience chamber exit threshold. wide, low angle, wide lens, pull back, deep focus, high contrast ceremonial. Wide composition across placed for immediate spatial orientation. the group begins to turn away from the throne area. thark audience chamber main floor. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH010_SC006; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris; woola
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: wide
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: alternate_angle
- review_notes: Prompt body is missing the required subject anchor for an on-screen shot.
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH010_SC006
- chapter_id: CH010
- shot_type: establishing_wide
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across lorquas_ptomel_audience_chamber with john_carter, dejah_thoris, woola placed for immediate spatial orientation.
- shot_size: wide
- camera_angle: low_angle
- camera_motion: pull_back
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_right
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: dejah_thoris; woola
- primary_subject_frame_position: midground inside thark_audience_chamber main floor
- primary_subject_scale_relation: height of chamber walls vs character height
- primary_subject_facing_direction: front three-quarter right toward the scene action
- primary_subject_pose_description: characters standing in tension
- subject_relation_summary: john_carter plays against dejah_thoris, woola in the same frame
- scene_short_description: A group consisting of a man, a woman, and a creature exits a massive ceremonial hall.
- shot_moment_summary: the group begins to turn away from the throne area
- required_environment_anchor_1: thark_audience_chamber exit threshold
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: height of chamber walls vs character height
- camera_package_description: wide, low angle, wide lens, pull back, deep focus, high contrast ceremonial
- environment_subzone: thark_audience_chamber main floor
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; dejah_thoris; woola; lorquas_ptomel_audience_chamber; DESC_CH010_SC006; DESC_CH010_SC006_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: identity reference for the secondary visible subject
- image2_asset: dejah thoris
- image3_role: environment reference for the scene location
- image3_asset: lorquas ptomel audience chamber
- image4_role: identity reference for an additional visible subject
- image4_asset: woola

# Continuity Notes
- Scene: CH010_SC006 / SC006.
- Variant: Alternate Angle.
- Tight grouping of john_carter, dejah_thoris, and woola
- Group turns to depart the chamber
- Consistent character spacing during movement through hallways
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH010\CH010_SC006.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH010\CH010_SC006\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH010\CH010_SC006\SH001\DIALOGUE.json
