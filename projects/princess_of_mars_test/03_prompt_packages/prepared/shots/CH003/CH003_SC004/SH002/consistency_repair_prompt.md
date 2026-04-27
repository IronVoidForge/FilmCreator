# Title
SH002 Shot Prompt - Consistency Repair

# ID
CH003_SC004_SH002_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for protagonist. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for martian incubator enclosure. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. A naked, agile fighter leaps thirty feet over a glass enclosure to escape a spear. The subject from image1 is protagonist, midground inside martian incubator enclosure, 30ft arc height, rear three-quarter left away from camera, takeoff. The subject from image2 is protagonist plays against martian warriors in the same frame. Preserve the environment from image3 Low walled enclosure containing an incubator area., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially martian incubator enclosure. extreme-wide, eye level, ultra-wide lens, crane, deep focus, diffuse ambient. Dynamic composition in clear pursuit vectors and readable movement. protagonist mid-air over enclosure. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH003_SC004; SHOT_INDEX; DIALOGUE; protagonist; martian_warriors
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: ultra_wide
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
- scene_id: CH003_SC004
- chapter_id: CH003
- shot_type: action
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: Dynamic composition in martian_incubator_enclosure with clear pursuit vectors and readable movement for protagonist, martian_warriors.
- shot_size: extreme_wide
- camera_angle: eye_level
- camera_motion: crane
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: rear_three_quarter_left
- visible_primary_subject_id: protagonist
- visible_secondary_subject_ids: martian_warriors
- primary_subject_frame_position: midground inside martian_incubator_enclosure
- primary_subject_scale_relation: 30ft arc height
- primary_subject_facing_direction: rear three-quarter left away from camera
- primary_subject_pose_description: takeoff
- subject_relation_summary: protagonist plays against martian_warriors in the same frame
- scene_short_description: A naked, agile fighter leaps thirty feet over a glass enclosure to escape a spear.
- shot_moment_summary: protagonist mid-air over enclosure
- required_environment_anchor_1: martian_incubator_enclosure
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: 30ft arc height
- camera_package_description: extreme-wide, eye level, ultra-wide lens, crane, deep focus, diffuse ambient
- environment_subzone: martian_incubator_enclosure
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; martian_warriors; martian_incubator_enclosure; DESC_CH003_SC004; DESC_CH003_SC004_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: protagonist
- image2_role: identity reference for the secondary visible subject
- image2_asset: martian warriors
- image3_role: environment reference for the scene location
- image3_asset: martian incubator enclosure

# Continuity Notes
- Scene: CH003_SC004 / SC004.
- Variant: Consistency Repair.
- Precise landing point relative to the jump origin
- Proximity of spear tip to protagonist during flight
- Trajectory arc height over martian_incubator_enclosure
- The massive leap
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH003\CH003_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC004\SH002\DIALOGUE.json
