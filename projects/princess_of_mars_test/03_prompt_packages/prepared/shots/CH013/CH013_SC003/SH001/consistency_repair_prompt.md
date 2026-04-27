# Title
SH001 Shot Prompt - Consistency Repair

# ID
CH013_SC003_SH001_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for martian night plaza. Use image4 as the identity reference for an additional visible subject. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. A reunion in a Martian plaza under two moons turns into a revelation of sabotage. The subject from image1 is john carter, foreground entry line within martian night plaza center, distance between Carter and the women, front three-quarter right toward the scene action, Carter walking into frame. The subject from image2 is john carter plays against dejah thoris, sola in the same frame. Preserve the environment from image3 Expansive open spaces with large-scale architecture casting shadows., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially martian night plaza center. medium-full, eye level, wide lens, track, deep focus, low key night. Readable medium composition in featuring. Carter approaches Dejah and Sola. center. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH013_SC003; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris; sola
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
- scene_id: CH013_SC003
- chapter_id: CH013
- shot_type: medium
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in martian_night_plaza featuring john_carter, dejah_thoris, sola.
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
- visible_secondary_subject_ids: dejah_thoris; sola
- primary_subject_frame_position: foreground entry line within martian_night_plaza center
- primary_subject_scale_relation: distance between Carter and the women
- primary_subject_facing_direction: front three-quarter right toward the scene action
- primary_subject_pose_description: Carter walking into frame
- subject_relation_summary: john_carter plays against dejah_thoris, sola in the same frame
- scene_short_description: A reunion in a Martian plaza under two moons turns into a revelation of sabotage.
- shot_moment_summary: Carter approaches Dejah and Sola
- required_environment_anchor_1: martian_night_plaza center
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: distance between Carter and the women
- camera_package_description: medium-full, eye level, wide lens, track, deep focus, low key night
- environment_subzone: martian_night_plaza center
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; dejah_thoris; sola; martian_night_plaza; DESC_CH013_SC003; DESC_CH013_SC003_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: identity reference for the secondary visible subject
- image2_asset: dejah thoris
- image3_role: environment reference for the scene location
- image3_asset: martian night plaza
- image4_role: identity reference for an additional visible subject
- image4_asset: sola

# Continuity Notes
- Scene: CH013_SC003 / SC003.
- Variant: Consistency Repair.
- Dejah Thoris physical signs of fatigue and labor (sweat, grime, exhaustion)
- Proximity of Sola to Dejah
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH013\CH013_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH013\CH013_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH013\CH013_SC003\SH001\DIALOGUE.json
