# Title
SH001 Shot Prompt - Consistency Repair

# ID
CH014_SC004_SH001_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for duel arena open plains. Use image4 as the identity reference for an additional visible subject. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. A high-intensity sword duel under bright sunlight interrupted by a blinding light reflection. The subject from image1 is john carter, foreground entry line within duel arena open plains, human scale duelists, front three-quarter left toward the scene action, clashing blades. The subject from image2 is john carter plays against Zad, sarkoja in the same frame. Preserve the environment from image3 A wide combat clearing providing sufficient space for chariot maneuvering and formal dueling., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially duel arena open plains. medium-full, eye level, wide lens, track, deep focus, hard directional. Readable medium composition in featuring. Carter and Zad clash swords. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH014_SC004; SHOT_INDEX; DIALOGUE; john_carter; zad; sarkoja
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: wide
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
- scene_id: CH014_SC004
- chapter_id: CH014
- shot_type: medium
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in duel_arena_open_plains featuring john_carter, Zad, sarkoja.
- shot_size: medium_full
- camera_angle: eye_level
- camera_motion: track
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: hard_directional
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: front_three_quarter_left
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: zad; sarkoja
- primary_subject_frame_position: foreground entry line within duel_arena_open_plains
- primary_subject_scale_relation: human scale duelists
- primary_subject_facing_direction: front three-quarter left toward the scene action
- primary_subject_pose_description: clashing blades
- subject_relation_summary: john_carter plays against Zad, sarkoja in the same frame
- scene_short_description: A high-intensity sword duel under bright sunlight interrupted by a blinding light reflection.
- shot_moment_summary: Carter and Zad clash swords
- required_environment_anchor_1: duel_arena_open_plains
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: human scale duelists
- camera_package_description: medium-full, eye level, wide lens, track, deep focus, hard directional
- environment_subzone: duel_arena_open_plains
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; zad; sarkoja; duel_arena_open_plains; DESC_CH014_SC004; DESC_CH014_SC004_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: identity reference for the secondary visible subject
- image2_asset: zad
- image3_role: environment reference for the scene location
- image3_asset: duel arena open plains
- image4_role: identity reference for an additional visible subject
- image4_asset: sarkoja

# Continuity Notes
- Scene: CH014_SC004 / SC004.
- Variant: Consistency Repair.
- Sun angle relative to camera and actors
- Mirror position and reflection trajectory
- Sword positions during the strike
- The duel begins between Carter and Zad
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH014\CH014_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH014\CH014_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH014\CH014_SC004\SH001\DIALOGUE.json
