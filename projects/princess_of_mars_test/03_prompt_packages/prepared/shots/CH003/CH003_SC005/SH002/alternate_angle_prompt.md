# Title
SH002 Shot Prompt - Alternate Angle

# ID
CH003_SC005_SH002_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for protagonist. Use image2 as the environment reference for arizona quartz vein basin. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. A leader offers a metal armlet to a naked man before he is mounted and led away. The subject from image1 is protagonist, foreground inside arizona quartz vein basin center, preserve readable body-to-environment scale in frame, facing directly toward camera, hand reaching for armlet. Preserve the environment from image2 Circular basin geometry, rugged terrain with high visibility and open spaces suitable for long-range sightlines and large leaps., monumental scale, dry open Martian terrain, especially quartz bearing rock outcropping. Keep one readable subject anchor: hand reaching for armlet. medium-close, eye level, normal lens, push in, rack focus, diffuse ambient. Intimate composition that isolates, against to capture the beat's emotional turn. Protagonist takes the armlet and puts it on. center. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH003_SC005; SHOT_INDEX; DIALOGUE; protagonist; martian_warriors
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: normal
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: alternate_angle
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH003_SC005
- chapter_id: CH003
- shot_type: reaction_closeup
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates protagonist, The Leader against arizona_quartz_vein_basin to capture the beat's emotional turn.
- shot_size: medium_close
- camera_angle: eye_level
- camera_motion: push_in
- zoom_behavior: none
- focus_strategy: rack_focus
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front
- visible_primary_subject_id: protagonist
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground inside arizona_quartz_vein_basin_center
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: hand reaching for armlet
- subject_relation_summary: protagonist carries the frame alone
- scene_short_description: A leader offers a metal armlet to a naked man before he is mounted and led away.
- shot_moment_summary: Protagonist takes the armlet and puts it on
- required_environment_anchor_1: quartz_bearing_rock_outcropping
- required_subject_anchor_1: hand reaching for armlet
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: preserve readable body-to-environment scale in frame
- camera_package_description: medium-close, eye level, normal lens, push in, rack focus, diffuse ambient
- environment_subzone: arizona_quartz_vein_basin_center
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; arizona_quartz_vein_basin; DESC_CH003_SC005; DESC_CH003_SC005_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: protagonist
- image2_role: environment reference for the scene location
- image2_asset: arizona quartz vein basin

# Continuity Notes
- Scene: CH003_SC005 / SC005.
- Variant: Alternate Angle.
- Armlet must remain visible on protagonist's arm after acceptance
- Cavalry direction of travel must be consistent toward distant hills
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH003\CH003_SC005.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC005\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC005\SH002\DIALOGUE.json
