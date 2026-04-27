# Title
SH001 Shot Prompt - Primary Keyframe

# ID
CH028_SC002_SH001_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the environment reference for arizona cave system. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. A man explores a dark cave discovering ritualistic remains and hanging human skeletons. The subject from image1 is john carter, foreground entry line within cave interior, Human scale discovery within vast, oppressive cave darkness, profile right toward the scene action, walking in dark. Preserve the environment from image2 monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, broad processional paths and stairs, especially arizona cave system. medium-full, eye level, wide lens, track, shallow subject, low key night. Readable medium composition in featuring. john carter moving through darkness. cave interior. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH028_SC002; SHOT_INDEX; DIALOGUE; john_carter; mummified_woman
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
- scene_id: CH028_SC002
- chapter_id: CH028
- shot_type: medium
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in arizona_cave_system featuring john_carter.
- shot_size: medium_full
- camera_angle: eye_level
- camera_motion: track
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: low_key_night
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: profile_right
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground entry line within cave interior
- primary_subject_scale_relation: Human scale discovery within vast, oppressive cave darkness.
- primary_subject_facing_direction: profile right toward the scene action
- primary_subject_pose_description: walking in dark
- subject_relation_summary: john_carter carries the frame alone
- scene_short_description: A man explores a dark cave discovering ritualistic remains and hanging human skeletons.
- shot_moment_summary: john_carter moving through darkness
- required_environment_anchor_1: arizona_cave_system
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: Human scale discovery within vast, oppressive cave darkness.
- camera_package_description: medium-full, eye level, wide lens, track, shallow subject, low key night
- environment_subzone: cave interior
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; arizona_cave_system; DESC_CH028_SC002; DESC_CH028_SC002_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: environment reference for the scene location
- image2_asset: arizona cave system

# Continuity Notes
- Scene: CH028_SC002 / SC002.
- Variant: Primary Keyframe.
- mummified_woman position relative to john_carter
- lighting source from charcoal burner
- exploration of cave interior
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH028\CH028_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH028\CH028_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH028\CH028_SC002\SH001\DIALOGUE.json
