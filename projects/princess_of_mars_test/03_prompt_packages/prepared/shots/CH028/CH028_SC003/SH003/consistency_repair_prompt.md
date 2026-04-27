# Title
SH003 Shot Prompt - Consistency Repair

# ID
CH028_SC003_SH003_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the environment reference for arizona desert landscape. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. A man emerges from a dark cave into the blinding, vast expanse of the Arizona desert. The subject from image1 is arizona desert landscape, midground inside arizona desert landscape, preserve readable body-to-environment scale in frame, rear three-quarter left away from camera, subject in frame. Preserve the environment from image2 monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, broad processional paths and stairs, especially arizona desert landscape. wide, low angle, ultra-wide lens, pull back, deep focus, hard directional. Wide composition across placed for immediate spatial orientation. wide view of the desert landscape. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH028_SC003; SHOT_INDEX; DIALOGUE; john_carter
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
- scene_id: CH028_SC003
- chapter_id: CH028
- shot_type: establishing_wide
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across arizona_desert_landscape with john_carter placed for immediate spatial orientation.
- shot_size: wide
- camera_angle: low_angle
- camera_motion: pull_back
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: hard_directional
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: rear_three_quarter_left
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: midground inside arizona_desert_landscape
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: rear three-quarter left away from camera
- primary_subject_pose_description: subject in frame
- subject_relation_summary: arizona_desert_landscape carries the frame alone
- scene_short_description: A man emerges from a dark cave into the blinding, vast expanse of the Arizona desert.
- shot_moment_summary: wide view of the desert landscape
- required_environment_anchor_1: arizona_desert_landscape
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: preserve readable body-to-environment scale in frame
- camera_package_description: wide, low angle, ultra-wide lens, pull back, deep focus, hard directional
- environment_subzone: arizona_desert_landscape
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; arizona_desert_landscape; DESC_CH028_SC003; DESC_CH028_SC003_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: environment reference for the scene location
- image2_asset: arizona desert landscape

# Continuity Notes
- Scene: CH028_SC003 / SC003.
- Variant: Consistency Repair.
- Rapid exposure shift from dark cave to high-key desert sunlight
- Physical state and clothing condition of john_carter post-cave exit
- Realization of Earth
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH028\CH028_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH028\CH028_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH028\CH028_SC003\SH003\DIALOGUE.json
