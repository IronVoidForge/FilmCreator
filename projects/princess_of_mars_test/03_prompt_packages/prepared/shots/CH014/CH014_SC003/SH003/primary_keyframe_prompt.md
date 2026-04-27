# Title
SH003 Shot Prompt - Primary Keyframe

# ID
CH014_SC003_SH003_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for duel arena open plains. Use image4 as the identity reference for an additional visible subject. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. Two warriors face off in a formal duel within an open Martian plain. The subject from image1 is john carter, foreground right within duel circle, sword grip vs hand size, facing directly toward camera, weapon drawn. The subject from image2 is john carter plays against Zad, tars tarkas in the same frame. Preserve the environment from image3 A wide combat clearing providing sufficient space for chariot maneuvering and formal dueling., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially duel circle. medium-full, eye level, wide lens, track, deep focus, diffuse ambient. Dynamic composition in clear pursuit vectors and readable movement. john carter responds to challenge. duel circle. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH014_SC003; SHOT_INDEX; DIALOGUE; john_carter; zad; tars_tarkas; sarkoja
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: wide
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
- scene_id: CH014_SC003
- chapter_id: CH014
- shot_type: action
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: Dynamic composition in duel_arena_open_plains with clear pursuit vectors and readable movement for john_carter, Zad, tars_tarkas.
- shot_size: medium_full
- camera_angle: eye_level
- camera_motion: track
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: zad; tars_tarkas
- primary_subject_frame_position: foreground right within duel_circle
- primary_subject_scale_relation: sword grip vs hand size
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: weapon drawn
- subject_relation_summary: john_carter plays against Zad, tars_tarkas in the same frame
- scene_short_description: Two warriors face off in a formal duel within an open Martian plain.
- shot_moment_summary: john_carter responds to challenge
- required_environment_anchor_1: duel_circle
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: sword grip vs hand size
- camera_package_description: medium-full, eye level, wide lens, track, deep focus, diffuse ambient
- environment_subzone: duel_circle
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; zad; tars_tarkas; duel_arena_open_plains; DESC_CH014_SC003; DESC_CH014_SC003_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: identity reference for the secondary visible subject
- image2_asset: zad
- image3_role: environment reference for the scene location
- image3_asset: duel arena open plains
- image4_role: identity reference for an additional visible subject
- image4_asset: tars tarkas

# Continuity Notes
- Scene: CH014_SC003 / SC003.
- Variant: Primary Keyframe.
- Weapon types must be long-swords
- Precise positioning of the duel circle/area
- Formal aggression established
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH014\CH014_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH014\CH014_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH014\CH014_SC003\SH003\DIALOGUE.json
