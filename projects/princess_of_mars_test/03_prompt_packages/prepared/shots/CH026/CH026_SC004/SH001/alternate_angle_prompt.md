# Title
SH001 Shot Prompt - Alternate Angle

# ID
CH026_SC004_SH001_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for tars tarkas. Use image2 as the environment reference for helium city interior. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. A grand triumphal procession enters the city of Helium under the shadow of red towers. The subject from image1 is procession, midground inside helium city interior gates, The scale shifts from individual soldier grit to the massive architectural grandeur of the Heliumite palace grounds, facing directly toward camera, distant movement. Preserve the environment from image2 Features wide ceremonial streets, royal halls, and majestic palaces., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially helium city interior gates. wide, eye level, ultra-wide lens, track, deep focus, diffuse ambient. Dynamic composition in clear pursuit vectors and readable movement. Wide view of the procession entering Helium. gates. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH026_SC004; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris; tardos_mors; mors_kajak; tars_tarkas
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: ultra_wide
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: alternate_angle
- review_notes: Prompt body is missing the required subject anchor for an on-screen shot.
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH026_SC004
- chapter_id: CH026
- shot_type: action
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: Dynamic composition in helium_city_interior with clear pursuit vectors and readable movement for tars_tarkas.
- shot_size: wide
- camera_angle: eye_level
- camera_motion: track
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front
- visible_primary_subject_id: tars_tarkas
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: midground inside helium_city_interior_gates
- primary_subject_scale_relation: The scale shifts from individual soldier grit to the massive architectural grandeur of the Heliumite palace grounds.
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: distant movement
- subject_relation_summary: procession carries the frame alone
- scene_short_description: A grand triumphal procession enters the city of Helium under the shadow of red towers.
- shot_moment_summary: Wide view of the procession entering Helium
- required_environment_anchor_1: helium_city_interior_gates
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: The scale shifts from individual soldier grit to the massive architectural grandeur of the Heliumite palace grounds.
- camera_package_description: wide, eye level, ultra-wide lens, track, deep focus, diffuse ambient
- environment_subzone: helium_city_interior_gates
- prompt_family: shot_prompt
- reference_asset_ids: tars_tarkas; helium_city_interior; DESC_CH026_SC004; DESC_CH026_SC004_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: tars tarkas
- image2_role: environment reference for the scene location
- image2_asset: helium city interior

# Continuity Notes
- Scene: CH026_SC004 / SC004.
- Variant: Alternate Angle.
- Heliumite royal attire and regalia must be pristine and ceremonial
- Procession soldiers must maintain visible dirt and blood from recent combat
- The procession enters Helium
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH026\CH026_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH026\CH026_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH026\CH026_SC004\SH001\DIALOGUE.json
