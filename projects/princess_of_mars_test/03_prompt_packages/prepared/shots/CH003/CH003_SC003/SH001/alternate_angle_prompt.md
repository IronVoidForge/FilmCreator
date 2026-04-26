# Title
SH001 Shot Prompt - Alternate Angle

# ID
CH003_SC003_SH001_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for martian warriors. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for arizona quartz vein basin. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. A massive cavalry of twenty Martian warriors on eight-legged mounts approaches a lone figure. The subject from image1 is martian warriors, midground inside arizona quartz vein basin perimeter, 15-foot tall martian warriors vs human-scale protagonist, front three-quarter right toward the scene action, wide vista. The subject from image2 is martian warriors plays against protagonist in the same frame. Preserve the environment from image3 Circular basin geometry, rugged terrain with high visibility and open spaces suitable for long-range sightlines and large leaps., monumental scale, dry open Martian terrain, especially quartz-bearing rock outcroppings. twenty mounts visible. wide, eye level, ultra-wide lens, pan, deep focus, diffuse ambient. Wide composition across placed for immediate spatial orientation. cavalry appears on horizon. perimeter. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH003_SC003; SHOT_INDEX; DIALOGUE; protagonist; martian_warriors
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
- scene_id: CH003_SC003
- chapter_id: CH003
- shot_type: establishing_wide
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across arizona_quartz_vein_basin with martian_warriors, protagonist placed for immediate spatial orientation.
- shot_size: wide
- camera_angle: eye_level
- camera_motion: pan
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_right
- visible_primary_subject_id: martian_warriors
- visible_secondary_subject_ids: protagonist
- primary_subject_frame_position: midground inside arizona_quartz_vein_basin_perimeter
- primary_subject_scale_relation: 15-foot tall martian_warriors vs human-scale protagonist
- primary_subject_facing_direction: front three-quarter right toward the scene action
- primary_subject_pose_description: wide vista
- subject_relation_summary: martian_warriors plays against protagonist in the same frame
- scene_short_description: A massive cavalry of twenty Martian warriors on eight-legged mounts approaches a lone figure.
- shot_moment_summary: cavalry appears on horizon
- required_environment_anchor_1: quartz-bearing rock outcroppings
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: twenty mounts visible
- camera_package_description: wide, eye level, ultra-wide lens, pan, deep focus, diffuse ambient
- environment_subzone: arizona_quartz_vein_basin_perimeter
- prompt_family: shot_prompt
- reference_asset_ids: martian_warriors; protagonist; arizona_quartz_vein_basin; DESC_CH003_SC003; DESC_CH003_SC003_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: martian warriors
- image2_role: identity reference for the secondary visible subject
- image2_asset: protagonist
- image3_role: environment reference for the scene location
- image3_asset: arizona quartz vein basin

# Continuity Notes
- Scene: CH003_SC003 / SC003.
- Variant: Alternate Angle.
- Exact count of twenty martian_warriors
- Proximity/positioning of eight-legged mounts relative to protagonist
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH003\CH003_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC003\SH001\DIALOGUE.json
