# Title
SH001 Shot Prompt - Primary Keyframe

# ID
CH024_SC002_SH001_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for thark city complex. Use image4 as the identity reference for an additional visible subject. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. Two warriors intercept a priestess in a dim interior to force her departure. The subject from image1 is john carter, foreground entry line within thark city interior corridor, height differential between warriors and priestess, front three-quarter right toward the scene action, Carter/Tars moving in shadow. The subject from image2 is john carter plays against tars tarkas, sarkoja in the same frame. Preserve the environment from image3 Massive scale with wide thoroughfares and high-ceilinged communal areas., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially thark city interior corridor. medium-full, eye level, wide lens, track, deep focus, low key night. Readable medium composition in featuring. Carter and Tars Tarkas intercept Sarkoja. thark city interior corridor. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH024_SC002; SHOT_INDEX; DIALOGUE; john_carter; tars_tarkas; sarkoja
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
- scene_id: CH024_SC002
- chapter_id: CH024
- shot_type: medium
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in thark_city_complex featuring john_carter, tars_tarkas, sarkoja.
- shot_size: medium_full
- camera_angle: eye_level
- camera_motion: track
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: low_key_night
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: front_three_quarter_right
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: tars_tarkas; sarkoja
- primary_subject_frame_position: foreground entry line within thark_city_interior_corridor
- primary_subject_scale_relation: height differential between warriors and priestess
- primary_subject_facing_direction: front three-quarter right toward the scene action
- primary_subject_pose_description: Carter/Tars moving in shadow
- subject_relation_summary: john_carter plays against tars_tarkas, sarkoja in the same frame
- scene_short_description: Two warriors intercept a priestess in a dim interior to force her departure.
- shot_moment_summary: Carter and Tars Tarkas intercept Sarkoja
- required_environment_anchor_1: thark_city_interior_corridor
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: height differential between warriors and priestess
- camera_package_description: medium-full, eye level, wide lens, track, deep focus, low key night
- environment_subzone: thark_city_interior_corridor
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; tars_tarkas; sarkoja; thark_city_complex; DESC_CH024_SC002; DESC_CH024_SC002_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: identity reference for the secondary visible subject
- image2_asset: tars tarkas
- image3_role: environment reference for the scene location
- image3_asset: thark city complex
- image4_role: identity reference for an additional visible subject
- image4_asset: sarkoja

# Continuity Notes
- Scene: CH024_SC002 / SC002.
- Variant: Primary Keyframe.
- Thark interior lighting levels
- Character positioning relative to the threat
- Interception of Sarkoja
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH024\CH024_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH024\CH024_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH024\CH024_SC002\SH001\DIALOGUE.json
