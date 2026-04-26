# Title
SH001 Shot Prompt - Consistency Repair

# ID
CH003_SC002_SH001_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for protagonist. Use image2 as the environment reference for arizona quartz vein basin. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. A man approaches a glass-roofed enclosure filled with hundreds of large white eggs and emerging creatures. The subject from image1 is protagonist, midground inside circular basin exterior, protagonist size vs enclosure height, rear three-quarter left away from camera, protagonist in distance. Preserve the environment from image2 Circular basin geometry, rugged terrain with high visibility and open spaces suitable for long-range sightlines and large leaps., monumental scale, dry open Martian terrain, especially circular basin exterior. wide, eye level, wide lens, track, deep focus, diffuse ambient. Wide composition across placed for immediate spatial orientation. protagonist walking through moss toward the structure. circular basin exterior. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH003_SC002; SHOT_INDEX; DIALOGUE; protagonist
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
- scene_id: CH003_SC002
- chapter_id: CH003
- shot_type: establishing_wide
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across arizona_quartz_vein_basin with protagonist placed for immediate spatial orientation.
- shot_size: wide
- camera_angle: eye_level
- camera_motion: track
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: rear_three_quarter_left
- visible_primary_subject_id: protagonist
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: midground inside circular_basin_exterior
- primary_subject_scale_relation: protagonist size vs enclosure height
- primary_subject_facing_direction: rear three-quarter left away from camera
- primary_subject_pose_description: protagonist in distance
- subject_relation_summary: protagonist carries the frame alone
- scene_short_description: A man approaches a glass-roofed enclosure filled with hundreds of large white eggs and emerging creatures.
- shot_moment_summary: protagonist walking through moss toward the structure
- required_environment_anchor_1: circular_basin_exterior
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: protagonist size vs enclosure height
- camera_package_description: wide, eye level, wide lens, track, deep focus, diffuse ambient
- environment_subzone: circular_basin_exterior
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; arizona_quartz_vein_basin; DESC_CH003_SC002; DESC_CH003_SC002_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: protagonist
- image2_role: environment reference for the scene location
- image2_asset: arizona quartz vein basin

# Continuity Notes
- Scene: CH003_SC002 / SC002.
- Variant: Consistency Repair.
- Egg state (hatched vs unhatched) must remain consistent per shot
- Six-limbed creature movement patterns must be uniform
- protagonist approaches the incubator
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH003\CH003_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC002\SH001\DIALOGUE.json
