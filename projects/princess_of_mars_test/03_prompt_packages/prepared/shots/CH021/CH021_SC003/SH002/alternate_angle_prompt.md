# Title
SH002 Shot Prompt - Alternate Angle

# ID
CH021_SC003_SH002_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for zodanga central plaza. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. Two men meet amidst the heavy foot traffic of a massive Martian urban plaza. The subject from image1 is john carter, foreground right within zodanga central plaza open floor, characters isolated from crowd flow, facing directly toward camera, close proximity [[SH002 START]]. The subject from image2 is john carter plays against kantos kan in the same frame. Preserve the environment from image3 Central gathering space surrounded by palaces, mechanical cafes, and high-rise metal residences., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially zodanga central plaza open floor. Keep one readable subject anchor: standing face-to-face. medium, eye level, normal lens, locked off, zoom subtle in, shallow subject, diffuse ambient. Readable medium composition in featuring. Medium shot of the two men meeting and embracing/greeting. open floor. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH021_SC003; SHOT_INDEX; DIALOGUE; john_carter; kantos_kan
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: normal
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: alternate_angle
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH021_SC003
- chapter_id: CH021
- shot_type: medium
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in zodanga_central_plaza featuring john_carter, kantos_kan.
- shot_size: medium
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: subtle_in
- focus_strategy: shallow_subject
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: front
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: kantos_kan
- primary_subject_frame_position: foreground right within zodanga_central_plaza_open_floor
- primary_subject_scale_relation: characters isolated from crowd flow
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: close proximity [[SH002_START]]
- subject_relation_summary: john_carter plays against kantos_kan in the same frame
- scene_short_description: Two men meet amidst the heavy foot traffic of a massive Martian urban plaza.
- shot_moment_summary: Medium shot of the two men meeting and embracing/greeting
- required_environment_anchor_1: zodanga_central_plaza_open_floor
- required_subject_anchor_1: standing face-to-face
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: characters isolated from crowd flow
- camera_package_description: medium, eye level, normal lens, locked off, zoom subtle in, shallow subject, diffuse ambient
- environment_subzone: zodanga_central_plaza_open_floor
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; kantos_kan; zodanga_central_plaza; DESC_CH021_SC003; DESC_CH021_SC003_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: identity reference for the secondary visible subject
- image2_asset: kantos kan
- image3_role: environment reference for the scene location
- image3_asset: zodanga central plaza

# Continuity Notes
- Scene: CH021_SC003 / SC003.
- Variant: Alternate Angle.
- Background crowd movement density
- Character positioning relative to plaza landmarks
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH021\CH021_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH021\CH021_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH021\CH021_SC003\SH002\DIALOGUE.json
