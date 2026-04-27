# Title
SH002 Shot Prompt - Alternate Angle

# ID
CH008_SC002_SH002_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for green martian warriors. Use image2 as the environment reference for deserted martian city plaza. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. A damaged gray vessel is looted by green Martians before being set ablaze as a funeral pyre. The subject from image1 is green martian warriors, foreground right within deserted martian city plaza landing zone, amount of loot piles vs ship size, front three-quarter right toward the scene action, warriors surrounding craft. Preserve the environment from image2 monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, broad processional paths and stairs, especially deserted martian city plaza landing zone. medium, eye level, normal lens, track, shallow subject, hard directional. Readable medium composition in featuring. warriors stripping arms, silks, and food. landing zone. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH008_SC002; SHOT_INDEX; DIALOGUE; protagonist; green_martian_warriors; woola
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: normal
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
- scene_id: CH008_SC002
- chapter_id: CH008
- shot_type: medium
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in deserted_martian_city_plaza featuring green_martian_warriors.
- shot_size: medium
- camera_angle: eye_level
- camera_motion: track
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: hard_directional
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_right
- visible_primary_subject_id: green_martian_warriors
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground right within deserted_martian_city_plaza landing zone
- primary_subject_scale_relation: amount of loot piles vs ship size
- primary_subject_facing_direction: front three-quarter right toward the scene action
- primary_subject_pose_description: warriors surrounding craft
- subject_relation_summary: green_martian_warriors carries the frame alone
- scene_short_description: A damaged gray vessel is looted by green Martians before being set ablaze as a funeral pyre.
- shot_moment_summary: warriors stripping arms, silks, and food
- required_environment_anchor_1: deserted_martian_city_plaza landing zone
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: amount of loot piles vs ship size
- camera_package_description: medium, eye level, normal lens, track, shallow subject, hard directional
- environment_subzone: deserted_martian_city_plaza landing zone
- prompt_family: shot_prompt
- reference_asset_ids: green_martian_warriors; deserted_martian_city_plaza; DESC_CH008_SC002; DESC_CH008_SC002_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: green martian warriors
- image2_role: environment reference for the scene location
- image2_asset: deserted martian city plaza

# Continuity Notes
- Scene: CH008_SC002 / SC002.
- Variant: Alternate Angle.
- Intensity and color of fire on the vessel
- Volume of debris and loot being moved from the craft
- Systematic looting of the craft
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH008\CH008_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH008\CH008_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH008\CH008_SC002\SH002\DIALOGUE.json
