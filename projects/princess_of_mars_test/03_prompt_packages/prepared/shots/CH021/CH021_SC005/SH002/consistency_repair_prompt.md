# Title
SH002 Shot Prompt - Consistency Repair

# ID
CH021_SC005_SH002_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for zodanga central plaza. Use image4 as the identity reference for an additional visible subject. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. Aerial combat between warriors and a scout in the high Martian atmosphere. The subject from image1 is john carter, foreground right within combat skirmish zone, impact force against vessel hulls, front three-quarter left toward the scene action, high-speed approach. The subject from image2 is john carter plays against green warriors, zodangan scout in the same frame. Preserve the environment from image3 Central gathering space surrounded by palaces, mechanical cafes, and high-rise metal residences., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially combat skirmish zone. medium-full, low angle, normal lens, handheld, zoom subtle in, shallow subject, high contrast ceremonial. Dynamic composition in clear pursuit vectors and readable movement. Carter strikes the first warrior. combat skirmish zone. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH021_SC005; SHOT_INDEX; DIALOGUE; john_carter; green_warriors; zodangan_scout
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
- scene_id: CH021_SC005
- chapter_id: CH021
- shot_type: action
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: Dynamic composition in zodanga_central_plaza with clear pursuit vectors and readable movement for john_carter, green_warriors, zodangan_scout.
- shot_size: medium_full
- camera_angle: low_angle
- camera_motion: handheld
- zoom_behavior: subtle_in
- focus_strategy: shallow_subject
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_left
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: green_warriors; zodangan_scout
- primary_subject_frame_position: foreground right within combat_skirmish_zone
- primary_subject_scale_relation: impact force against vessel hulls
- primary_subject_facing_direction: front three-quarter left toward the scene action
- primary_subject_pose_description: high-speed approach
- subject_relation_summary: john_carter plays against green_warriors, zodangan_scout in the same frame
- scene_short_description: Aerial combat between warriors and a scout in the high Martian atmosphere.
- shot_moment_summary: Carter strikes the first warrior
- required_environment_anchor_1: combat_skirmish_zone
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: impact force against vessel hulls
- camera_package_description: medium-full, low angle, normal lens, handheld, zoom subtle in, shallow subject, high contrast ceremonial
- environment_subzone: combat_skirmish_zone
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; green_warriors; zodangan_scout; zodanga_central_plaza; DESC_CH021_SC005; DESC_CH021_SC005_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: identity reference for the secondary visible subject
- image2_asset: green warriors
- image3_role: environment reference for the scene location
- image3_asset: zodanga central plaza
- image4_role: identity reference for an additional visible subject
- image4_asset: zodangan scout

# Continuity Notes
- Scene: CH021_SC005 / SC005.
- Variant: Consistency Repair.
- Flight trajectories of all four vessels
- Damage states to the zodangan_scout vessel
- Relative positioning of green_warriors to the scout
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH021\CH021_SC005.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH021\CH021_SC005\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH021\CH021_SC005\SH002\DIALOGUE.json
