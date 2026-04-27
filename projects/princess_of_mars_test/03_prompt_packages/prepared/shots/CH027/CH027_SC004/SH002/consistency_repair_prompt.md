# Title
SH002 Shot Prompt - Consistency Repair

# ID
CH027_SC004_SH002_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the environment reference for helium palace sunken gardens. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. A stripped air-scout machine flies through turbulent, thinning atmosphere toward a distant plant. The subject from image1 is Air-scout Machine, midground inside The sky over Barsoom, machine size relative to vast sky, profile right toward the scene action, Machine lifting off. Preserve the environment from image2 Large-scale terraced gardens with tiered palace terraces, includes royal seating areas and central botanical anchors., monumental scale, dry open Martian terrain, especially The sky over Barsoom. wide, low angle, ultra-wide lens, track, deep focus, diffuse ambient. Wide composition across placed for immediate spatial orientation. Machine accelerating through the sky. The sky over Barsoom. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH027_SC004; SHOT_INDEX; DIALOGUE; john_carter
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: ultra_wide
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: consistency_repair
- review_notes: Environment reference conflict: prompt variables align more with `none` than bound `helium_palace_sunken_gardens`.; Prompt body is missing the required subject anchor for an on-screen shot.
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH027_SC004
- chapter_id: CH027
- shot_type: establishing_wide
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across helium_palace_sunken_gardens with john_carter placed for immediate spatial orientation.
- shot_size: wide
- camera_angle: low_angle
- camera_motion: track
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: profile_right
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: midground inside The sky over Barsoom
- primary_subject_scale_relation: machine size relative to vast sky
- primary_subject_facing_direction: profile right toward the scene action
- primary_subject_pose_description: Machine lifting off
- subject_relation_summary: Air-scout Machine carries the frame alone
- scene_short_description: A stripped air-scout machine flies through turbulent, thinning atmosphere toward a distant plant.
- shot_moment_summary: Machine accelerating through the sky
- required_environment_anchor_1: The sky over Barsoom
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: machine size relative to vast sky
- camera_package_description: wide, low angle, ultra-wide lens, track, deep focus, diffuse ambient
- environment_subzone: The sky over Barsoom
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; helium_palace_sunken_gardens; DESC_CH027_SC004; DESC_CH027_SC004_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: environment reference for the scene location
- image2_asset: helium palace sunken gardens

# Continuity Notes
- Scene: CH027_SC004 / SC004.
- Variant: Consistency Repair.
- Machine must show progressively removed components/stripped weight
- John Carter exhibits increasing respiratory struggle/difficulty breathing
- Launch and acceleration
- Resolve The sky over Barsoom -> The sky over Barsoom
- Resolve Air-scout Machine -> Air-scout Machine
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH027\CH027_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH027\CH027_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH027\CH027_SC004\SH002\DIALOGUE.json
