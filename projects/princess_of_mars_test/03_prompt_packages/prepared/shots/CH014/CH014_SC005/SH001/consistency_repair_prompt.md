# Title
SH001 Shot Prompt - Consistency Repair

# ID
CH014_SC005_SH001_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for sarkoja. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for duel arena open plains. Use image4 as the identity reference for an additional visible subject. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. A chaotic duel in the open plains erupts into sudden violence leaving two characters wounded. The subject from image1 is dej thoris, foreground entry line within duel arena open plains center, preserve readable body-to-environment scale in frame, front three-quarter right toward the scene action, active combat. The subject from image2 is dej thoris plays against sola, john carter in the same frame. Preserve the environment from image3 A wide combat clearing providing sufficient space for chariot maneuvering and formal dueling., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially duel arena open plains center. Keep one readable subject anchor: Dejah and Sarkoja face off; Sola enters the gap. medium-full, eye level, wide lens, handheld, shallow subject, diffuse ambient. Wide composition across placed for immediate spatial orientation. Dejah Thoris confronts Sarkoja amidst the duel. center. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH014_SC005; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris; sola; sarkoja; zad
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
- scene_id: CH014_SC005
- chapter_id: CH014
- shot_type: establishing_wide
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across duel_arena_open_plains with sarkoja, sola, john_carter placed for immediate spatial orientation.
- shot_size: medium_full
- camera_angle: eye_level
- camera_motion: handheld
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: front_three_quarter_right
- visible_primary_subject_id: sarkoja
- visible_secondary_subject_ids: sola; john_carter
- primary_subject_frame_position: foreground entry line within duel_arena_open_plains center
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: front three-quarter right toward the scene action
- primary_subject_pose_description: active combat
- subject_relation_summary: dej_thoris plays against sola, john_carter in the same frame
- scene_short_description: A chaotic duel in the open plains erupts into sudden violence leaving two characters wounded.
- shot_moment_summary: Dejah Thoris confronts Sarkoja amidst the duel
- required_environment_anchor_1: duel_arena_open_plains center
- required_subject_anchor_1: Dejah and Sarkoja face off; Sola enters the gap
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: preserve readable body-to-environment scale in frame
- camera_package_description: medium-full, eye level, wide lens, handheld, shallow subject, diffuse ambient
- environment_subzone: duel_arena_open_plains center
- prompt_family: shot_prompt
- reference_asset_ids: sarkoja; sola; john_carter; duel_arena_open_plains; DESC_CH014_SC005; DESC_CH014_SC005_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: sarkoja
- image2_role: identity reference for the secondary visible subject
- image2_asset: sola
- image3_role: environment reference for the scene location
- image3_asset: duel arena open plains
- image4_role: identity reference for an additional visible subject
- image4_asset: john carter

# Continuity Notes
- Scene: CH014_SC005 / SC005.
- Variant: Consistency Repair.
- Blood splatter and wound locations on Sola and Carter
- Character positions during the melee transition
- Lighting shifts if sun position changes significantly
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH014\CH014_SC005.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH014\CH014_SC005\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH014\CH014_SC005\SH001\DIALOGUE.json
