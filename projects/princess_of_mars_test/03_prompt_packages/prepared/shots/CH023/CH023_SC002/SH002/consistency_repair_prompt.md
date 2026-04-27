# Title
SH002 Shot Prompt - Consistency Repair

# ID
CH023_SC002_SH002_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for zodanga urban complex. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. A climber scales a massive vertical structure to infiltrate a roof and steal machinery. The subject from image1 is john carter, foreground right within barracks roof edge, Height visible below feet, front three-quarter left toward the scene action, confrontation. The subject from image2 is john carter plays against zodangan sentry in the same frame. Preserve the environment from image3 Dense urban layout with significant vertical scale, dominated by massive barracks and palace towers creating deep canyons., monumental scale, dry open Martian terrain, especially barracks roof edge. medium, eye level, normal lens, handheld, shallow subject, low key night. Readable medium composition in featuring. subduing the sentry. barracks roof edge. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH023_SC002; SHOT_INDEX; DIALOGUE; john_carter; zodangan_sentry
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: normal
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
- scene_id: CH023_SC002
- chapter_id: CH023
- shot_type: medium
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in zodanga_urban_complex featuring john_carter, zodangan_sentry.
- shot_size: medium
- camera_angle: eye_level
- camera_motion: handheld
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: low_key_night
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_left
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: zodangan_sentry
- primary_subject_frame_position: foreground right within barracks_roof_edge
- primary_subject_scale_relation: Height visible below feet
- primary_subject_facing_direction: front three-quarter left toward the scene action
- primary_subject_pose_description: confrontation
- subject_relation_summary: john_carter plays against zodangan_sentry in the same frame
- scene_short_description: A climber scales a massive vertical structure to infiltrate a roof and steal machinery.
- shot_moment_summary: subduing the sentry
- required_environment_anchor_1: barracks_roof_edge
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: Height visible below feet
- camera_package_description: medium, eye level, normal lens, handheld, shallow subject, low key night
- environment_subzone: barracks_roof_edge
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; zodangan_sentry; zodanga_urban_complex; DESC_CH023_SC002; DESC_CH023_SC002_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: identity reference for the secondary visible subject
- image2_asset: zodangan sentry
- image3_role: environment reference for the scene location
- image3_asset: zodanga urban complex

# Continuity Notes
- Scene: CH023_SC002 / SC002.
- Variant: Consistency Repair.
- Vertical height/scale perception relative to ground
- Wind direction and intensity on exterior surfaces
- Position of the incapacitated sentry hanging over edge
- Subduing the sentry
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH023\CH023_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH023\CH023_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH023\CH023_SC002\SH002\DIALOGUE.json
