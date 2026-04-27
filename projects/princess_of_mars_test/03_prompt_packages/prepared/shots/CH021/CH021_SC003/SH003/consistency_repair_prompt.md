# Title
SH003 Shot Prompt - Consistency Repair

# ID
CH021_SC003_SH003_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for kantos kan. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for zodanga central plaza. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. Two men meet amidst the heavy foot traffic of a massive Martian urban plaza. The subject from image1 is kantos kan, foreground inside zodanga central plaza open floor, Large scale urban architecture vs intimate political dialogue, profile left toward the scene action, tense facial expression [[SH003 START]]. The subject from image2 is kantos kan plays against john carter in the same frame. Preserve the environment from image3 Central gathering space surrounded by palaces, mechanical cafes, and high-rise metal residences., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially zodanga central plaza open floor. medium-close, eye level, portrait lens, locked off, rack focus, high contrast ceremonial. Over-the-shoulder composition in sharing the frame for dialogue or tension. Over-the-shoulder shot as the conversation turns to Sab Than and Dejah Thoris. open floor. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH021_SC003; SHOT_INDEX; DIALOGUE; john_carter; kantos_kan
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: portrait
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
- scene_id: CH021_SC003
- chapter_id: CH021
- shot_type: over_the_shoulder
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Shoulder-level conversational framing with visible foreground presence.
- composition: Over-the-shoulder composition in zodanga_central_plaza with kantos_kan, john_carter sharing the frame for dialogue or tension.
- shot_size: medium_close
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: none
- focus_strategy: rack_focus
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: profile_left
- visible_primary_subject_id: kantos_kan
- visible_secondary_subject_ids: john_carter
- primary_subject_frame_position: foreground inside zodanga_central_plaza_open_floor
- primary_subject_scale_relation: Large scale urban architecture vs intimate political dialogue.
- primary_subject_facing_direction: profile left toward the scene action
- primary_subject_pose_description: tense facial expression [[SH003_START]]
- subject_relation_summary: kantos_kan plays against john_carter in the same frame
- scene_short_description: Two men meet amidst the heavy foot traffic of a massive Martian urban plaza.
- shot_moment_summary: Over-the-shoulder shot as the conversation turns to Sab Than and Dejah Thoris
- required_environment_anchor_1: zodanga_central_plaza_open_floor
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: Large scale urban architecture vs intimate political dialogue.
- camera_package_description: medium-close, eye level, portrait lens, locked off, rack focus, high contrast ceremonial
- environment_subzone: zodanga_central_plaza_open_floor
- prompt_family: shot_prompt
- reference_asset_ids: kantos_kan; john_carter; zodanga_central_plaza; DESC_CH021_SC003; DESC_CH021_SC003_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: kantos kan
- image2_role: identity reference for the secondary visible subject
- image2_asset: john carter
- image3_role: environment reference for the scene location
- image3_asset: zodanga central plaza

# Continuity Notes
- Scene: CH021_SC003 / SC003.
- Variant: Consistency Repair.
- Background crowd movement density
- Character positioning relative to plaza landmarks
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH021\CH021_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH021\CH021_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH021\CH021_SC003\SH003\DIALOGUE.json
