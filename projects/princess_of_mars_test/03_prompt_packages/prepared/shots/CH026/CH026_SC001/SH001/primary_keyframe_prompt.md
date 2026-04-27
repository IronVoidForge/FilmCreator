# Title
SH001 Shot Prompt - Primary Keyframe

# ID
CH026_SC001_SH001_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for tars tarkas. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for aerial battle skies. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. Massive aerial fleets clash in the Martian skies before a ritualistic surrender. The subject from image1 is Thark fleet, midground inside aerial battle skies combat zone, Fleet size vs sky expanse, facing directly toward camera, distant fleets approaching. The subject from image2 is Thark fleet plays against kantos kan in the same frame. Preserve the environment from image3 High-altitude, expansive vertical combat space., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially aerial battle skies combat zone. extreme-wide, eye level, ultra-wide lens, pan, deep focus, diffuse ambient. Dynamic composition in clear pursuit vectors and readable movement. Thark fleet encounters Zodangan siege force. combat zone. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH026_SC001; SHOT_INDEX; DIALOGUE; john_carter; tars_tarkas; kantos_kan
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: ultra_wide
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
- scene_id: CH026_SC001
- chapter_id: CH026
- shot_type: action
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: Dynamic composition in aerial_battle_skies with clear pursuit vectors and readable movement for tars_tarkas, kantos_kan, Zodangan Commanders.
- shot_size: extreme_wide
- camera_angle: eye_level
- camera_motion: pan
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front
- visible_primary_subject_id: tars_tarkas
- visible_secondary_subject_ids: kantos_kan
- primary_subject_frame_position: midground inside aerial_battle_skies_combat_zone
- primary_subject_scale_relation: Fleet size vs sky expanse
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: distant fleets approaching
- subject_relation_summary: Thark fleet plays against kantos_kan in the same frame
- scene_short_description: Massive aerial fleets clash in the Martian skies before a ritualistic surrender.
- shot_moment_summary: Thark fleet encounters Zodangan siege force
- required_environment_anchor_1: aerial_battle_skies_combat_zone
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: Fleet size vs sky expanse
- camera_package_description: extreme-wide, eye level, ultra-wide lens, pan, deep focus, diffuse ambient
- environment_subzone: aerial_battle_skies_combat_zone
- prompt_family: shot_prompt
- reference_asset_ids: tars_tarkas; kantos_kan; aerial_battle_skies; DESC_CH026_SC001; DESC_CH026_SC001_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: tars tarkas
- image2_role: identity reference for the secondary visible subject
- image2_asset: kantos kan
- image3_role: environment reference for the scene location
- image3_asset: aerial battle skies

# Continuity Notes
- Scene: CH026_SC001 / SC001.
- Variant: Primary Keyframe.
- Vessel positions in the sky relative to fleet formation
- Total count of remaining ships during melee
- Direction of flight paths during combat maneuvers
- Fleet interception
- Resolve Zodangan Commanders -> Zodangan Commanders
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH026\CH026_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH026\CH026_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH026\CH026_SC001\SH001\DIALOGUE.json
