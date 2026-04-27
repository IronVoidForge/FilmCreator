# Title
SH003 Shot Prompt - Consistency Repair

# ID
CH010_SC004_SH003_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the environment reference for lorquas ptomel audience chamber. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. A warrior acquires ceremonial regalia and weapons within a massive stone audience chamber. The subject from image1 is john carter, foreground inside regalia presentation zone, Individual human scale vs. the monumental hierarchy of the Thark Council, facing directly toward camera, Carter partially dressed. Preserve the environment from image2 Large scale, centered around a focal point for the presiding chieftain., monumental scale, dry open Martian terrain, especially regalia presentation zone. medium-close, eye level, portrait lens, locked off, zoom subtle in, shallow subject, high contrast ceremonial. Intimate composition that isolates, against to capture the beat's emotional turn. Close up of Carter wearing the regalia. regalia presentation zone. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH010_SC004; SHOT_INDEX; DIALOGUE; john_carter; lorquas_ptomel; tars_tarkas
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: portrait
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
- scene_id: CH010_SC004
- chapter_id: CH010
- shot_type: reaction_closeup
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates john_carter, Thark Council against lorquas_ptomel_audience_chamber to capture the beat's emotional turn.
- shot_size: medium_close
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: subtle_in
- focus_strategy: shallow_subject
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground inside regalia presentation zone
- primary_subject_scale_relation: Individual human scale vs. the monumental hierarchy of the Thark Council.
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: Carter partially dressed
- subject_relation_summary: john_carter carries the frame alone
- scene_short_description: A warrior acquires ceremonial regalia and weapons within a massive stone audience chamber.
- shot_moment_summary: Close up of Carter wearing the regalia
- required_environment_anchor_1: regalia presentation zone
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: Individual human scale vs. the monumental hierarchy of the Thark Council.
- camera_package_description: medium-close, eye level, portrait lens, locked off, zoom subtle in, shallow subject, high contrast ceremonial
- environment_subzone: regalia presentation zone
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; lorquas_ptomel_audience_chamber; DESC_CH010_SC004; DESC_CH010_SC004_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: environment reference for the scene location
- image2_asset: lorquas ptomel audience chamber

# Continuity Notes
- Scene: CH010_SC004 / SC004.
- Variant: Consistency Repair.
- Specific weapons and regalia items held or worn by john_carter
- Physical state of john_carter post-combat
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH010\CH010_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH010\CH010_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH010\CH010_SC004\SH003\DIALOGUE.json
