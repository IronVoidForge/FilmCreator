# Title
SH001 Shot Prompt - Alternate Angle

# ID
CH025_SC003_SH001_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the environment reference for audience chamber. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. A chaotic skirmish erupts in a grand hall, ending with a fatal strike and heavy silence. The subject from image1 is Thark Warriors, midground inside combat floor, The scale shifts from a large-scale melee to a tight, lethal confrontation between Carter and Sab Than, front three-quarter left toward the scene action, clash begins. Preserve the environment from image2 monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, broad processional paths and stairs, especially combat floor. wide, eye level, wide lens, handheld, deep focus, high contrast ceremonial. Dynamic composition in clear pursuit vectors and readable movement. skirmish breaks out between factions. combat floor. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH025_SC003; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris; sab_than; tars_tarkas
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
- scene_id: CH025_SC003
- chapter_id: CH025
- shot_type: action
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: Dynamic composition in audience_chamber with clear pursuit vectors and readable movement for Thark Warriors, Zodangan Guards, john_carter.
- shot_size: wide
- camera_angle: eye_level
- camera_motion: handheld
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: front_three_quarter_left
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: midground inside combat_floor
- primary_subject_scale_relation: The scale shifts from a large-scale melee to a tight, lethal confrontation between Carter and Sab Than.
- primary_subject_facing_direction: front three-quarter left toward the scene action
- primary_subject_pose_description: clash begins
- subject_relation_summary: Thark Warriors carries the frame alone
- scene_short_description: A chaotic skirmish erupts in a grand hall, ending with a fatal strike and heavy silence.
- shot_moment_summary: skirmish breaks out between factions
- required_environment_anchor_1: combat_floor
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: The scale shifts from a large-scale melee to a tight, lethal confrontation between Carter and Sab Than.
- camera_package_description: wide, eye level, wide lens, handheld, deep focus, high contrast ceremonial
- environment_subzone: combat_floor
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; audience_chamber; DESC_CH025_SC003; DESC_CH025_SC003_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: environment reference for the scene location
- image2_asset: audience chamber

# Continuity Notes
- Scene: CH025_SC003 / SC003.
- Variant: Alternate Angle.
- Blood splatter patterns on floor and characters
- Weapon damage/integrity after melee
- Character proximity to throne vs Dejah Thoris
- Skirmish breaks out between Tharks and Zodangan Guards
- Resolve Thark Warriors -> Thark Warriors
- Resolve Zodangan Guards -> Zodangan Guards
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH025\CH025_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH025\CH025_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH025\CH025_SC003\SH001\DIALOGUE.json
