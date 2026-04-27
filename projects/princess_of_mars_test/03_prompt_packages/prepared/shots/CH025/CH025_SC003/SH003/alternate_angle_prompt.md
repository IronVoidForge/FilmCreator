# Title
SH003 Shot Prompt - Alternate Angle

# ID
CH025_SC003_SH003_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for tars tarkas. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for audience chamber. Use image4 as the identity reference for an additional visible subject. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. A chaotic skirmish erupts in a grand hall, ending with a fatal strike and heavy silence. The subject from image1 is tars tarkas, midground inside throne platform, Tars Tarkas dominance over the platform, facing directly toward camera, combat ceases. The subject from image2 is tars tarkas plays against john carter, dejah thoris in the same frame. Preserve the environment from image3 monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, broad processional paths and stairs, especially throne platform. wide, eye level, ultra-wide lens, pan, deep focus, high contrast ceremonial. Wide composition across placed for immediate spatial orientation. Tars Tarkas arrives to secure the area. throne platform. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH025_SC003; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris; sab_than; tars_tarkas
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: ultra_wide
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
- scene_id: CH025_SC003
- chapter_id: CH025
- shot_type: establishing_wide
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across audience_chamber with tars_tarkas, john_carter, dejah_thoris placed for immediate spatial orientation.
- shot_size: wide
- camera_angle: eye_level
- camera_motion: pan
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front
- visible_primary_subject_id: tars_tarkas
- visible_secondary_subject_ids: john_carter; dejah_thoris
- primary_subject_frame_position: midground inside throne_platform
- primary_subject_scale_relation: Tars Tarkas dominance over the platform
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: combat ceases
- subject_relation_summary: tars_tarkas plays against john_carter, dejah_thoris in the same frame
- scene_short_description: A chaotic skirmish erupts in a grand hall, ending with a fatal strike and heavy silence.
- shot_moment_summary: Tars Tarkas arrives to secure the area
- required_environment_anchor_1: throne_platform
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: Tars Tarkas dominance over the platform
- camera_package_description: wide, eye level, ultra-wide lens, pan, deep focus, high contrast ceremonial
- environment_subzone: throne_platform
- prompt_family: shot_prompt
- reference_asset_ids: tars_tarkas; john_carter; dejah_thoris; audience_chamber; DESC_CH025_SC003; DESC_CH025_SC003_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: tars tarkas
- image2_role: identity reference for the secondary visible subject
- image2_asset: john carter
- image3_role: environment reference for the scene location
- image3_asset: audience chamber
- image4_role: identity reference for an additional visible subject
- image4_asset: dejah thoris

# Continuity Notes
- Scene: CH025_SC003 / SC003.
- Variant: Alternate Angle.
- Blood splatter patterns on floor and characters
- Weapon damage/integrity after melee
- Character proximity to throne vs Dejah Thoris
- Tars Tarkas secures the platform
- Resolve Thark Warriors -> Thark Warriors
- Resolve Zodangan Guards -> Zodangan Guards
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH025\CH025_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH025\CH025_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH025\CH025_SC003\SH003\DIALOGUE.json
