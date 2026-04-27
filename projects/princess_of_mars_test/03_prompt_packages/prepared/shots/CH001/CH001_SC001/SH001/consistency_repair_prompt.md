# Title
SH001 Shot Prompt - Consistency Repair

# ID
CH001_SC001_SH001_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for arizona quartz vein location. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. Two men discover a massive gold-bearing quartz vein amidst rugged Arizona hills. The subject from image1 is john carter, midground inside arizona quartz vein location, The scale of the gold vein relative to the prospecting tools, front three-quarter left toward the scene action, men swinging/digging. The subject from image2 is john carter plays against james k powell in the same frame. Preserve the environment from image3 Vast mountain ranges containing localized mineral deposits and rocky terrain., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially arizona quartz vein location. Keep one readable subject anchor: standing near rock face. wide, eye level, wide lens, pan, deep focus, hard directional. Wide composition across placed for immediate spatial orientation. men working in the hills. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH001_SC001; SHOT_INDEX; DIALOGUE; john_carter; james_k_powell
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
- scene_id: CH001_SC001
- chapter_id: CH001
- shot_type: establishing_wide
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across arizona_quartz_vein_location with john_carter, james_k_powell placed for immediate spatial orientation.
- shot_size: wide
- camera_angle: eye_level
- camera_motion: pan
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: hard_directional
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: front_three_quarter_left
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: james_k_powell
- primary_subject_frame_position: midground inside arizona_quartz_vein_location
- primary_subject_scale_relation: The scale of the gold vein relative to the prospecting tools.
- primary_subject_facing_direction: front three-quarter left toward the scene action
- primary_subject_pose_description: men swinging/digging
- subject_relation_summary: john_carter plays against james_k_powell in the same frame
- scene_short_description: Two men discover a massive gold-bearing quartz vein amidst rugged Arizona hills.
- shot_moment_summary: men working in the hills
- required_environment_anchor_1: arizona_quartz_vein_location
- required_subject_anchor_1: standing near rock face
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: The scale of the gold vein relative to the prospecting tools.
- camera_package_description: wide, eye level, wide lens, pan, deep focus, hard directional
- environment_subzone: arizona_quartz_vein_location
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; james_k_powell; arizona_quartz_vein_location; DESC_CH001_SC001; DESC_CH001_SC001_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: identity reference for the secondary visible subject
- image2_asset: james k powell
- image3_role: environment reference for the scene location
- image3_asset: arizona quartz vein location

# Continuity Notes
- Scene: CH001_SC001 / SC001.
- Variant: Consistency Repair.
- Physical appearance of the gold vein
- Specific tools and gear used by prospectors
- Hard labor and prospecting
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH001\CH001_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH001\CH001_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH001\CH001_SC001\SH001\DIALOGUE.json
