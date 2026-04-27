# Title
SH002 Shot Prompt - Primary Keyframe

# ID
CH016_SC001_SH002_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the environment reference for thark city and surroundings. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. A weary traveler enters a massive city plaza to find long-awaited companionship. The subject from image1 is john carter, foreground right within Great Plaza of Thark, plaza width vs character stride, front three-quarter right toward the scene action, walking in plaza. Preserve the environment from image2 Transitions from wide-open sea bottom vistas to dense Thark plazas, includes sprawling canal networks and massive communal spaces., monumental scale, dry open Martian terrain, especially Great Plaza of Thark. medium-full, eye level, wide lens, track, shallow subject, diffuse ambient. Readable medium composition in featuring. Carter traverses the vast expanse of the central plaza. Great Plaza of Thark. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH016_SC001; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris; sola
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: wide
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: primary_keyframe
- review_notes: Prompt body is missing the required subject anchor for an on-screen shot.
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH016_SC001
- chapter_id: CH016
- shot_type: medium
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in thark_city_and_surroundings featuring john_carter.
- shot_size: medium_full
- camera_angle: eye_level
- camera_motion: track
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_right
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground right within Great Plaza of Thark
- primary_subject_scale_relation: plaza width vs character stride
- primary_subject_facing_direction: front three-quarter right toward the scene action
- primary_subject_pose_description: walking in plaza
- subject_relation_summary: john_carter carries the frame alone
- scene_short_description: A weary traveler enters a massive city plaza to find long-awaited companionship.
- shot_moment_summary: Carter traverses the vast expanse of the central plaza
- required_environment_anchor_1: Great Plaza of Thark
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: plaza width vs character stride
- camera_package_description: medium-full, eye level, wide lens, track, shallow subject, diffuse ambient
- environment_subzone: Great Plaza of Thark
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; thark_city_and_surroundings; DESC_CH016_SC001; DESC_CH016_SC001_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: environment reference for the scene location
- image2_asset: thark city and surroundings

# Continuity Notes
- Scene: CH016_SC001 / SC001.
- Variant: Primary Keyframe.
- Travel-worn clothing and dirtied appearance for john_carter and companions
- Massive architectural scale relative to character height
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH016\CH016_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH016\CH016_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH016\CH016_SC001\SH002\DIALOGUE.json
