# Title
SH002 Shot Prompt - Primary Keyframe

# ID
CH025_SC001_SH002_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for zodanga palace throne room. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. Fifty Thark warriors lead a charge through palace gates into lush gardens. The subject from image1 is john carter, foreground right within zodanga palace throne room, preserve readable body-to-environment scale in frame, profile left toward the scene action, entering garden edge. The subject from image2 is john carter plays against tars tarkas in the same frame. Preserve the environment from image3 Massive scale with high ceilings, includes a central throne platform/raised dais and wide floor space capable of hosting skirmishes or cavalry charges., monumental scale, dry open Martian terrain, especially zodanga palace throne room. Keep one readable subject anchor: Leaders moving ahead of the massed group. medium, eye level, normal lens, track, shallow subject, diffuse ambient. Readable medium composition in featuring. Carter and Tars Tarkas moving through gardens. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH025_SC001; SHOT_INDEX; DIALOGUE; john_carter; tars_tarkas
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: normal
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: primary_keyframe
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH025_SC001
- chapter_id: CH025
- shot_type: medium
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in zodanga_palace_throne_room featuring john_carter, tars_tarkas, Thark Warriors.
- shot_size: medium
- camera_angle: eye_level
- camera_motion: track
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: profile_left
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: tars_tarkas
- primary_subject_frame_position: foreground right within zodanga_palace_throne_room
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: profile left toward the scene action
- primary_subject_pose_description: entering garden edge
- subject_relation_summary: john_carter plays against tars_tarkas in the same frame
- scene_short_description: Fifty Thark warriors lead a charge through palace gates into lush gardens.
- shot_moment_summary: Carter and Tars Tarkas moving through gardens
- required_environment_anchor_1: zodanga_palace_throne_room
- required_subject_anchor_1: Leaders moving ahead of the massed group
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: preserve readable body-to-environment scale in frame
- camera_package_description: medium, eye level, normal lens, track, shallow subject, diffuse ambient
- environment_subzone: zodanga_palace_throne_room
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; tars_tarkas; zodanga_palace_throne_room; DESC_CH025_SC001; DESC_CH025_SC001_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: identity reference for the secondary visible subject
- image2_asset: tars tarkas
- image3_role: environment reference for the scene location
- image3_asset: zodanga palace throne room

# Continuity Notes
- Scene: CH025_SC001 / SC001.
- Variant: Primary Keyframe.
- Weapon positions during movement
- Thark armor and gear consistency
- Lighting transitions from city streets to garden shadows
- Movement into gardens
- Resolve Thark Warriors -> Thark Warriors
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH025\CH025_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH025\CH025_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH025\CH025_SC001\SH002\DIALOGUE.json
