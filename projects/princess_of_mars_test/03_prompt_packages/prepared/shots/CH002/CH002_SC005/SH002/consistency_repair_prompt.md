# Title
SH002 Shot Prompt - Consistency Repair

# ID
CH002_SC005_SH002_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for protagonist. Use image2 as the environment reference for rocky gorge nightscape. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. A man flees a rocky gorge into the desert night before being pulled toward Mars. The subject from image1 is protagonist, foreground right within rocky gorge nightscape, protagonist vs planet size in sky, rear three-quarter left away from camera, running. Preserve the environment from image2 High desert gorge with jagged cliffs and silhouetted mountain ridges., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially rocky gorge nightscape. Keep one readable subject anchor: standing still, head tilted back. Keep celestial anchor the red planet stable in the frame. medium, low angle, ultra-wide lens, locked off, zoom subtle in, deep focus, low key night. Readable medium composition in featuring. protagonist stops and stares at Mars. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH002_SC005; SHOT_INDEX; DIALOGUE; protagonist
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: ultra_wide
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
- scene_id: CH002_SC005
- chapter_id: CH002
- shot_type: medium
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in rocky_gorge_nightscape featuring protagonist.
- shot_size: medium
- camera_angle: low_angle
- camera_motion: locked_off
- zoom_behavior: subtle_in
- focus_strategy: deep_focus
- lighting_style: low_key_night
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: rear_three_quarter_left
- visible_primary_subject_id: protagonist
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground right within rocky_gorge_nightscape
- primary_subject_scale_relation: protagonist vs planet size in sky
- primary_subject_facing_direction: rear three-quarter left away from camera
- primary_subject_pose_description: running
- subject_relation_summary: protagonist carries the frame alone
- scene_short_description: A man flees a rocky gorge into the desert night before being pulled toward Mars.
- shot_moment_summary: protagonist stops and stares at Mars
- required_environment_anchor_1: rocky_gorge_nightscape
- required_subject_anchor_1: standing still, head tilted back
- required_celestial_anchor_1: Mars
- required_scale_proof_detail: protagonist vs planet size in sky
- camera_package_description: medium, low angle, ultra-wide lens, locked off, zoom subtle in, deep focus, low key night
- environment_subzone: rocky_gorge_nightscape
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; rocky_gorge_nightscape; DESC_CH002_SC005; DESC_CH002_SC005_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: protagonist
- image2_role: environment reference for the scene location
- image2_asset: rocky gorge nightscape

# Continuity Notes
- Scene: CH002_SC005 / SC005.
- Variant: Consistency Repair.
- Fixed celestial position of Mars in the sky relative to horizon
- Visual texture/particle behavior of the transportation effect
- Gazing at Mars and feeling the pull
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH002\CH002_SC005.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH002\CH002_SC005\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH002\CH002_SC005\SH002\DIALOGUE.json
