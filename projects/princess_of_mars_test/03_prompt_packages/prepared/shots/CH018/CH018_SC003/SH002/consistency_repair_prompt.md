# Title
SH002 Shot Prompt - Consistency Repair

# ID
CH018_SC003_SH002_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for dak kova. Use image2 as the environment reference for martian plains march route. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. A massive horde of ten thousand warriors marches across open plains toward a city. The subject from image1 is dak kova, foreground right within martian plains march route, preserve readable body-to-environment scale in frame, profile left toward the scene action, tracking dak kova. Preserve the environment from image2 Vast, open plains suitable for epic military marches., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially martian plains march route. Keep one readable subject anchor: dak kova at head of column. warrior density. medium-full, eye level, wide lens, track, shallow subject, hard directional. Readable medium composition in featuring. Dak Kova leads the march through the ranks. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH018_SC003; SHOT_INDEX; DIALOGUE; dak_kova
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: wide
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
- scene_id: CH018_SC003
- chapter_id: CH018
- shot_type: medium
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in martian_plains_march_route featuring dak_kova, Warhoon Warriors.
- shot_size: medium_full
- camera_angle: eye_level
- camera_motion: track
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: hard_directional
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: profile_left
- visible_primary_subject_id: dak_kova
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground right within martian_plains_march_route
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: profile left toward the scene action
- primary_subject_pose_description: tracking dak_kova
- subject_relation_summary: dak_kova carries the frame alone
- scene_short_description: A massive horde of ten thousand warriors marches across open plains toward a city.
- shot_moment_summary: Dak Kova leads the march through the ranks
- required_environment_anchor_1: martian_plains_march_route
- required_subject_anchor_1: dak_kova at head of column
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: warrior density
- camera_package_description: medium-full, eye level, wide lens, track, shallow subject, hard directional
- environment_subzone: martian_plains_march_route
- prompt_family: shot_prompt
- reference_asset_ids: dak_kova; martian_plains_march_route; DESC_CH018_SC003; DESC_CH018_SC003_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: dak kova
- image2_role: environment reference for the scene location
- image2_asset: martian plains march route

# Continuity Notes
- Scene: CH018_SC003 / SC003.
- Variant: Consistency Repair.
- Consistent direction of travel toward Warhoon city
- Lighting transition from open Martian plains to subterranean darkness
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH018\CH018_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH018\CH018_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH018\CH018_SC003\SH002\DIALOGUE.json
