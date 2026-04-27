# Title
SH003 Shot Prompt - Consistency Repair

# ID
CH004_SC003_SH003_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for tars tarkas. Use image2 as the environment reference for chieftain audience chamber. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. A sudden physical clash in a grand hall leads to a massive, gravity-defying leap. The subject from image1 is Martian Crowd, foreground right within audience seating/periphery, crowd density vs hall size, facing directly toward camera, shocked silence. Preserve the environment from image2 monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, broad processional paths and stairs, especially chieftain's dais. medium-full, eye level, wide lens, pan, zoom subtle in, rack focus, diffuse ambient. Closing composition in that emphasizes the consequence of crowd reaction/respect established. Crowd reacts to the landing and feat. audience seating/periphery. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH004_SC003; SHOT_INDEX; DIALOGUE; tars_tarkas; chieftain
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: wide
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
- scene_id: CH004_SC003
- chapter_id: CH004
- shot_type: closing_reaction
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Controlled closing frame that lands the consequence of the beat.
- composition: Closing composition in chieftain_audience_chamber that emphasizes the consequence of crowd reaction/respect established.
- shot_size: medium_full
- camera_angle: eye_level
- camera_motion: pan
- zoom_behavior: subtle_in
- focus_strategy: rack_focus
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front
- visible_primary_subject_id: tars_tarkas
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground right within audience seating/periphery
- primary_subject_scale_relation: crowd density vs hall size
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: shocked silence
- subject_relation_summary: Martian Crowd carries the frame alone
- scene_short_description: A sudden physical clash in a grand hall leads to a massive, gravity-defying leap.
- shot_moment_summary: Crowd reacts to the landing and feat
- required_environment_anchor_1: chieftain's dais
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: crowd density vs hall size
- camera_package_description: medium-full, eye level, wide lens, pan, zoom subtle in, rack focus, diffuse ambient
- environment_subzone: audience seating/periphery
- prompt_family: shot_prompt
- reference_asset_ids: tars_tarkas; chieftain_audience_chamber; DESC_CH004_SC003; DESC_CH004_SC003_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: tars tarkas
- image2_role: environment reference for the scene location
- image2_asset: chieftain audience chamber

# Continuity Notes
- Scene: CH004_SC003 / SC003.
- Variant: Consistency Repair.
- Precise trajectory and landing point of the sak jump
- Crowd movement patterns during the commotion
- Crowd reaction/Respect established
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH004\CH004_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH004\CH004_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH004\CH004_SC003\SH003\DIALOGUE.json
