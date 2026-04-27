# Title
SH003 Shot Prompt - Consistency Repair

# ID
CH026_SC004_SH003_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for helium city interior. Use image4 as the identity reference for an additional visible subject. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. A grand triumphal procession enters the city of Helium under the shadow of red towers. The subject from image1 is helium city interior palace grounds, midground inside helium city interior palace grounds, The scale shifts from individual soldier grit to the massive architectural grandeur of the Heliumite palace grounds, facing directly toward camera, ceremony peak. The subject from image2 is helium city interior palace grounds plays against dejah thoris, tardos mors in the same frame. Preserve the environment from image3 Features wide ceremonial streets, royal halls, and majestic palaces., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially helium city interior palace grounds. wide, high angle, wide lens, crane, deep focus, high contrast ceremonial. Wide composition across placed for immediate spatial orientation. Wide shot of the celebration and red towers. palace grounds. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH026_SC004; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris; tardos_mors; mors_kajak; tars_tarkas
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
- scene_id: CH026_SC004
- chapter_id: CH026
- shot_type: establishing_wide
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across helium_city_interior with john_carter, dejah_thoris, tardos_mors placed for immediate spatial orientation.
- shot_size: wide
- camera_angle: high_angle
- camera_motion: crane
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: dejah_thoris; tardos_mors
- primary_subject_frame_position: midground inside helium_city_interior_palace_grounds
- primary_subject_scale_relation: The scale shifts from individual soldier grit to the massive architectural grandeur of the Heliumite palace grounds.
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: ceremony peak
- subject_relation_summary: helium_city_interior_palace_grounds plays against dejah_thoris, tardos_mors in the same frame
- scene_short_description: A grand triumphal procession enters the city of Helium under the shadow of red towers.
- shot_moment_summary: Wide shot of the celebration and red towers
- required_environment_anchor_1: helium_city_interior_palace_grounds
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: The scale shifts from individual soldier grit to the massive architectural grandeur of the Heliumite palace grounds.
- camera_package_description: wide, high angle, wide lens, crane, deep focus, high contrast ceremonial
- environment_subzone: helium_city_interior_palace_grounds
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; dejah_thoris; tardos_mors; helium_city_interior; DESC_CH026_SC004; DESC_CH026_SC004_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: identity reference for the secondary visible subject
- image2_asset: dejah thoris
- image3_role: environment reference for the scene location
- image3_asset: helium city interior
- image4_role: identity reference for an additional visible subject
- image4_asset: tardos mors

# Continuity Notes
- Scene: CH026_SC004 / SC004.
- Variant: Consistency Repair.
- Heliumite royal attire and regalia must be pristine and ceremonial
- Procession soldiers must maintain visible dirt and blood from recent combat
- The celebration of victory and alliance
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH026\CH026_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH026\CH026_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH026\CH026_SC004\SH003\DIALOGUE.json
