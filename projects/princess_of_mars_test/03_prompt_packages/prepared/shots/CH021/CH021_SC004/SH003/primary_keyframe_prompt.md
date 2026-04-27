# Title
SH003 Shot Prompt - Primary Keyframe

# ID
CH021_SC004_SH003_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the environment reference for zodangan aviation training grounds. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. A montage of technical training involving Martian aviation mechanics and air vessel operation. The subject from image1 is sky, midground inside Air vessels, Human scale interaction with large-scale eighth-ray propulsion machinery, facing directly toward camera, view of ground. Preserve the environment from image2 Defined by high-altitude flight corridors, aerial maneuvering zones, and eighth-ray propulsion mechanics., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially Air vessels. wide, eye level, ultra-wide lens, track, deep focus, backlit. Dynamic composition in clear pursuit vectors and readable movement. POV of flight through clouds. Air vessels. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH021_SC004; SHOT_INDEX; DIALOGUE; john_carter; kantos_kan
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
- scene_id: CH021_SC004
- chapter_id: CH021
- shot_type: action
- previous_shot_id: SH002
- next_shot_id: SH004
- shot_lineage_ids: SH002; SH003; SH004
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: Dynamic composition in zodangan_aviation_training_grounds with clear pursuit vectors and readable movement for john_carter.
- shot_size: wide
- camera_angle: eye_level
- camera_motion: track
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: backlit
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: midground inside Air vessels
- primary_subject_scale_relation: Human scale interaction with large-scale eighth-ray propulsion machinery.
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: view of ground
- subject_relation_summary: sky carries the frame alone
- scene_short_description: A montage of technical training involving Martian aviation mechanics and air vessel operation.
- shot_moment_summary: POV of flight through clouds
- required_environment_anchor_1: Air vessels
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: Human scale interaction with large-scale eighth-ray propulsion machinery.
- camera_package_description: wide, eye level, ultra-wide lens, track, deep focus, backlit
- environment_subzone: Air vessels
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; zodangan_aviation_training_grounds; DESC_CH021_SC004; DESC_CH021_SC004_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: environment reference for the scene location
- image2_asset: zodangan aviation training grounds

# Continuity Notes
- Scene: CH021_SC004 / SC004.
- Variant: Primary Keyframe.
- Progression of john_carter physical fatigue (sweat, grime, posture)
- Shifting weather and sky conditions across training days
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH021\CH021_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH021\CH021_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH021\CH021_SC004\SH003\DIALOGUE.json
