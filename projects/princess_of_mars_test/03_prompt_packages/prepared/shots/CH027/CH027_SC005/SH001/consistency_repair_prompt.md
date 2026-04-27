# Title
SH001 Shot Prompt - Consistency Repair

# ID
CH027_SC005_SH001_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the environment reference for atmosphere plant complex. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. A protagonist navigates mechanical locks to open massive doors before collapsing from exhaustion. The subject from image1 is john carter, midground inside lock interface, Massive industrial scale of the Atmosphere Plant vs human physical frailty, front three-quarter right toward the scene action, walking into frame. Preserve the environment from image2 Massive scale, includes three great mechanical doors (locks), heavy industrial pumps, and high-speed air-scout flight paths leading to the facility., monumental scale, dry open Martian terrain. wide, eye level, wide lens, track, deep focus, low key night. Wide composition across placed for immediate spatial orientation. John enters the graveyard of workers. lock interface. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH027_SC005; SHOT_INDEX; DIALOGUE; john_carter
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: wide
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: consistency_repair
- review_notes: SH001: environment anchor is typed like a subject/celestial detail instead of a set anchor.; Prompt body is missing the required subject anchor for an on-screen shot.
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH027_SC005
- chapter_id: CH027
- shot_type: establishing_wide
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across atmosphere_plant_complex with john_carter placed for immediate spatial orientation.
- shot_size: wide
- camera_angle: eye_level
- camera_motion: track
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: low_key_night
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: front_three_quarter_right
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: midground inside lock_interface
- primary_subject_scale_relation: Massive industrial scale of the Atmosphere Plant vs human physical frailty.
- primary_subject_facing_direction: front three-quarter right toward the scene action
- primary_subject_pose_description: walking into frame
- subject_relation_summary: john_carter carries the frame alone
- scene_short_description: A protagonist navigates mechanical locks to open massive doors before collapsing from exhaustion.
- shot_moment_summary: John enters the graveyard of workers
- required_environment_anchor_1: lock_interface
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: Massive industrial scale of the Atmosphere Plant vs human physical frailty.
- camera_package_description: wide, eye level, wide lens, track, deep focus, low key night
- environment_subzone: lock_interface
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; atmosphere_plant_complex; DESC_CH027_SC005; DESC_CH027_SC005_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: environment reference for the scene location
- image2_asset: atmosphere plant complex

# Continuity Notes
- Scene: CH027_SC005 / SC005.
- Variant: Consistency Repair.
- Sequential unlocking of three specific doors
- Physical state/condition of Surviving Worker
- Arrival at the plant and discovery of workers
- Resolve Surviving Worker -> Surviving Worker
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH027\CH027_SC005.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH027\CH027_SC005\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH027\CH027_SC005\SH001\DIALOGUE.json
