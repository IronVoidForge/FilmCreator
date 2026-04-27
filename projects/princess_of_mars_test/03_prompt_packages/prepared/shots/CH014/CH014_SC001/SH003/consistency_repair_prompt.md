# Title
SH003 Shot Prompt - Consistency Repair

# ID
CH014_SC001_SH003_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for tars tarkas. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for martian plains and march route. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. A group marches across open Martian plains toward Thark under shifting light. The subject from image1 is tars tarkas, foreground right within martian plains and march route, preserve readable body-to-environment scale in frame, front three-quarter left toward the scene action, Dejah walking stiffly. The subject from image2 is tars tarkas plays against dejah thoris in the same frame. Preserve the environment from image3 Continuous stretch of undulating terrain, long-distance vistas., monumental scale, dry open Martian terrain, especially martian plains and march route. medium, low angle, normal lens, pan, rack focus, hard directional. Closing composition in that emphasizes the consequence of manages tension by taking the keys. Tars Tarkas taking custody of the keys. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH014_SC001; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris; tars_tarkas; sarkoja
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: normal
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: consistency_repair
- review_notes: Prompt body is missing the required subject anchor for an on-screen shot.
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH014_SC001
- chapter_id: CH014
- shot_type: closing_reaction
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Controlled closing frame that lands the consequence of the beat.
- composition: Closing composition in martian_plains_and_march_route that emphasizes the consequence of tars tarkas manages tension by taking the keys.
- shot_size: medium
- camera_angle: low_angle
- camera_motion: pan
- zoom_behavior: none
- focus_strategy: rack_focus
- lighting_style: hard_directional
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: front_three_quarter_left
- visible_primary_subject_id: tars_tarkas
- visible_secondary_subject_ids: dejah_thoris
- primary_subject_frame_position: foreground right within martian_plains_and_march_route
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: front three-quarter left toward the scene action
- primary_subject_pose_description: Dejah walking stiffly
- subject_relation_summary: tars_tarkas plays against dejah_thoris in the same frame
- scene_short_description: A group marches across open Martian plains toward Thark under shifting light.
- shot_moment_summary: Tars Tarkas taking custody of the keys
- required_environment_anchor_1: martian_plains_and_march_route
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: preserve readable body-to-environment scale in frame
- camera_package_description: medium, low angle, normal lens, pan, rack focus, hard directional
- environment_subzone: martian_plains_and_march_route
- prompt_family: shot_prompt
- reference_asset_ids: tars_tarkas; dejah_thoris; martian_plains_and_march_route; DESC_CH014_SC001; DESC_CH014_SC001_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: tars tarkas
- image2_role: identity reference for the secondary visible subject
- image2_asset: dejah thoris
- image3_role: environment reference for the scene location
- image3_asset: martian plains and march route

# Continuity Notes
- Scene: CH014_SC001 / SC001.
- Variant: Consistency Repair.
- Position and rattling of Dejah's chains
- Variable distance between characters in the march line
- Lighting/time of day progression during the trek
- Tars Tarkas manages tension by taking the keys
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH014\CH014_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH014\CH014_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH014\CH014_SC001\SH003\DIALOGUE.json
