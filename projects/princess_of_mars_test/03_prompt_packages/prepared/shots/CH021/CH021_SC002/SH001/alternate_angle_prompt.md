# Title
SH001 Shot Prompt - Alternate Angle

# ID
CH021_SC002_SH001_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for zodanga city gates. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. A traveler approaches massive city walls and makes the difficult choice to leave a companion behind. The subject from image1 is john carter, midground inside zodanga city gates approach, wall height vs character height, rear three-quarter left away from camera, walking in tandem toward gates. The subject from image2 is john carter plays against woola in the same frame. Preserve the environment from image3 A threshold point marking the boundary between open wild plains and the urban environment of Zodanga., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially zodanga city gates approach. wide, low angle, ultra-wide lens, push in, deep focus, diffuse ambient. Wide composition across placed for immediate spatial orientation. Carter and Woola approach the massive walls. approach. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH021_SC002; SHOT_INDEX; DIALOGUE; john_carter; woola
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
- scene_id: CH021_SC002
- chapter_id: CH021
- shot_type: establishing_wide
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across zodanga_city_gates with john_carter, woola placed for immediate spatial orientation.
- shot_size: wide
- camera_angle: low_angle
- camera_motion: push_in
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: rear_three_quarter_left
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: woola
- primary_subject_frame_position: midground inside zodanga_city_gates_approach
- primary_subject_scale_relation: wall height vs character height
- primary_subject_facing_direction: rear three-quarter left away from camera
- primary_subject_pose_description: walking in tandem toward gates
- subject_relation_summary: john_carter plays against woola in the same frame
- scene_short_description: A traveler approaches massive city walls and makes the difficult choice to leave a companion behind.
- shot_moment_summary: Carter and Woola approach the massive walls
- required_environment_anchor_1: zodanga_city_gates_approach
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: wall height vs character height
- camera_package_description: wide, low angle, ultra-wide lens, push in, deep focus, diffuse ambient
- environment_subzone: zodanga_city_gates_approach
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; woola; zodanga_city_gates; DESC_CH021_SC002; DESC_CH021_SC002_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: identity reference for the secondary visible subject
- image2_asset: woola
- image3_role: environment reference for the scene location
- image3_asset: zodanga city gates

# Continuity Notes
- Scene: CH021_SC002 / SC002.
- Variant: Alternate Angle.
- Woola's physical proximity to Carter
- State of gear and clothing after travel
- Arrival at the Zodangan walls
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH021\CH021_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH021\CH021_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH021\CH021_SC002\SH001\DIALOGUE.json
