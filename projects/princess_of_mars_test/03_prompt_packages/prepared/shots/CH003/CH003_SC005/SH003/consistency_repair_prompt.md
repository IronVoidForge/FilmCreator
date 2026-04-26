# Title
SH003 Shot Prompt - Consistency Repair

# ID
CH003_SC005_SH003_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for protagonist. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for arizona quartz vein basin. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. A leader offers a metal armlet to a naked man before he is mounted and led away. The subject from image1 is protagonist, midground inside arizona quartz vein basin center, rider vs mount size, rear three-quarter left away from camera, protagonist being lifted. The subject from image2 is protagonist plays against martian warriors in the same frame. Preserve the environment from image3 Circular basin geometry, rugged terrain with high visibility and open spaces suitable for long-range sightlines and large leaps., monumental scale, dry open Martian terrain, especially arizona quartz vein basin center to distant hills horizon. wide, low angle, wide lens, pan, deep focus, diffuse ambient. Wide composition across placed for immediate spatial orientation. Protagonist is hoisted onto mount and rides away. center. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH003_SC005; SHOT_INDEX; DIALOGUE; protagonist; martian_warriors
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
- scene_id: CH003_SC005
- chapter_id: CH003
- shot_type: establishing_wide
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across arizona_quartz_vein_basin with protagonist, martian_warriors, The Leader placed for immediate spatial orientation.
- shot_size: wide
- camera_angle: low_angle
- camera_motion: pan
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: rear_three_quarter_left
- visible_primary_subject_id: protagonist
- visible_secondary_subject_ids: martian_warriors
- primary_subject_frame_position: midground inside arizona_quartz_vein_basin_center
- primary_subject_scale_relation: rider vs mount size
- primary_subject_facing_direction: rear three-quarter left away from camera
- primary_subject_pose_description: protagonist being lifted
- subject_relation_summary: protagonist plays against martian_warriors in the same frame
- scene_short_description: A leader offers a metal armlet to a naked man before he is mounted and led away.
- shot_moment_summary: Protagonist is hoisted onto mount and rides away
- required_environment_anchor_1: arizona_quartz_vein_basin_center to distant_hills_horizon
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: rider vs mount size
- camera_package_description: wide, low angle, wide lens, pan, deep focus, diffuse ambient
- environment_subzone: arizona_quartz_vein_basin_center
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; martian_warriors; arizona_quartz_vein_basin; DESC_CH003_SC005; DESC_CH003_SC005_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: protagonist
- image2_role: identity reference for the secondary visible subject
- image2_asset: martian warriors
- image3_role: environment reference for the scene location
- image3_asset: arizona quartz vein basin

# Continuity Notes
- Scene: CH003_SC005 / SC005.
- Variant: Consistency Repair.
- Armlet must remain visible on protagonist's arm after acceptance
- Cavalry direction of travel must be consistent toward distant hills
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH003\CH003_SC005.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC005\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC005\SH003\DIALOGUE.json
