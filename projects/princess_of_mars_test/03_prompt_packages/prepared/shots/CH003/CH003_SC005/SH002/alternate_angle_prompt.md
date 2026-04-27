# Title
SH002 Shot Prompt - Alternate Angle

# ID
CH003_SC005_SH002_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for protagonist. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for arizona quartz vein basin. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. A disarmed leader offers a metal armlet to a naked protagonist before he is mounted. The subject from image1 is protagonist, foreground right within arizona quartz vein basin center, protagonist height relative to mount, facing directly toward camera, Protagonist reaching for armlet. The subject from image2 is protagonist plays against martian warriors in the same frame. Preserve the environment from image3 Circular basin geometry, rugged terrain with high visibility and open spaces suitable for large leaps., monumental scale, dry open Martian terrain, especially arizona quartz vein basin center. medium, low angle, wide lens, track, deep focus, diffuse ambient. Readable medium composition featuring, and. Protagonist takes the armlet and is hoisted onto a Martian mount. center. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH003_SC005; SHOT_INDEX; DIALOGUE; protagonist; martian_warriors
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
- scene_id: CH003_SC005
- chapter_id: CH003
- shot_type: medium
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition featuring protagonist, martian_warriors, and The Leader.
- shot_size: medium
- camera_angle: low_angle
- camera_motion: track
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front
- visible_primary_subject_id: protagonist
- visible_secondary_subject_ids: martian_warriors
- primary_subject_frame_position: foreground right within arizona_quartz_vein_basin_center
- primary_subject_scale_relation: protagonist height relative to mount
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: Protagonist reaching for armlet
- subject_relation_summary: protagonist plays against martian_warriors in the same frame
- scene_short_description: A disarmed leader offers a metal armlet to a naked protagonist before he is mounted.
- shot_moment_summary: Protagonist takes the armlet and is hoisted onto a Martian mount
- required_environment_anchor_1: arizona_quartz_vein_basin_center
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: protagonist height relative to mount
- camera_package_description: medium, low angle, wide lens, track, deep focus, diffuse ambient
- environment_subzone: arizona_quartz_vein_basin_center
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; martian_warriors; arizona_quartz_vein_basin; DESC_CH003_SC005; DESC_CH003_SC005_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: protagonist
- image2_role: identity reference for the secondary visible subject
- image2_asset: martian warriors
- image3_role: environment reference for the scene location
- image3_asset: arizona quartz vein basin

# Continuity Notes
- Scene: CH003_SC005 / SC005.
- Variant: Alternate Angle.
- Armlet must remain visible on protagonist's arm after acceptance
- Resolve The Leader -> The Leader
- Cavalry direction of travel must be consistent toward distant hills
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH003\CH003_SC005.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC005\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC005\SH002\DIALOGUE.json
