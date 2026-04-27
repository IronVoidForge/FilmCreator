# Title
SH002 Shot Prompt - Consistency Repair

# ID
CH026_SC004_SH002_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for helium city interior. Use image4 as the identity reference for an additional visible subject. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. A grand triumphal procession enters the city of Helium under the shadow of red towers. The subject from image1 is john carter, foreground right within helium city interior palace grounds, Carter framed against the royal regalia, front three-quarter right toward the scene action, Carter approaching dais. The subject from image2 is Human male of high status., Elder., lean but durable soldier's frame, Ruler status implied, john carter plays against tardos mors, dejah thoris in the same frame. Preserve the environment from image3 Features wide ceremonial streets, royal halls, and majestic palaces., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially royal dais. medium-full, low angle, normal lens, push in, zoom subtle in, shallow subject, high contrast ceremonial. Readable medium composition in featuring. Low angle shot of Carter being honored. palace grounds. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH026_SC004; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris; tardos_mors; mors_kajak; tars_tarkas
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
- scene_id: CH026_SC004
- chapter_id: CH026
- shot_type: medium
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in helium_city_interior featuring john_carter, tardos_mors, dejah_thoris.
- shot_size: medium_full
- camera_angle: low_angle
- camera_motion: push_in
- zoom_behavior: subtle_in
- focus_strategy: shallow_subject
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: front_three_quarter_right
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: tardos_mors; dejah_thoris
- primary_subject_frame_position: foreground right within helium_city_interior_palace_grounds
- primary_subject_scale_relation: Carter framed against the royal regalia
- primary_subject_facing_direction: front three-quarter right toward the scene action
- primary_subject_pose_description: Carter approaching dais
- subject_relation_summary: john_carter plays against tardos_mors, dejah_thoris in the same frame
- scene_short_description: A grand triumphal procession enters the city of Helium under the shadow of red towers.
- shot_moment_summary: Low angle shot of Carter being honored
- required_environment_anchor_1: royal dais
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: Carter framed against the royal regalia
- camera_package_description: medium-full, low angle, normal lens, push in, zoom subtle in, shallow subject, high contrast ceremonial
- environment_subzone: helium_city_interior_palace_grounds
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; tardos_mors; dejah_thoris; helium_city_interior; DESC_CH026_SC004; DESC_CH026_SC004_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: identity reference for the secondary visible subject
- image2_asset: tardos mors
- image3_role: environment reference for the scene location
- image3_asset: helium city interior
- image4_role: identity reference for an additional visible subject
- image4_asset: dejah thoris

# Continuity Notes
- Scene: CH026_SC004 / SC004.
- Variant: Consistency Repair.
- Heliumite royal attire and regalia must be pristine and ceremonial
- Procession soldiers must maintain visible dirt and blood from recent combat
- Formal recognition of John Carter
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH026\CH026_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH026\CH026_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH026\CH026_SC004\SH002\DIALOGUE.json
