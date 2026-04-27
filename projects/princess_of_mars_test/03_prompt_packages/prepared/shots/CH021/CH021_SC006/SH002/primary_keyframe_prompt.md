# Title
SH002 Shot Prompt - Primary Keyframe

# ID
CH021_SC006_SH002_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for than kosis. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for zodanga central plaza. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. A massive military ceremony in a walled plaza where a hero is publicly honored by royalty. The subject from image1 is than kosis, foreground right within zodanga central plaza dais, preserve readable body-to-environment scale in frame, facing directly toward camera, Than Kosis standing. The subject from image2 is than kosis plays against john carter in the same frame. Preserve the environment from image3 Central gathering space surrounded by palaces, mechanical cafes, and high-rise metal residences., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially ceremonial dais. medium-full, low angle, normal lens, push in, zoom subtle in, shallow subject, high contrast ceremonial. Readable medium composition in featuring. Than Kosis announces the honor. dais. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH021_SC006; SHOT_INDEX; DIALOGUE; john_carter; than_kosis; sab_than
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: normal
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
- scene_id: CH021_SC006
- chapter_id: CH021
- shot_type: medium
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in zodanga_central_plaza featuring than_kosis, john_carter, Zodangan Military/Crowd.
- shot_size: medium_full
- camera_angle: low_angle
- camera_motion: push_in
- zoom_behavior: subtle_in
- focus_strategy: shallow_subject
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: front
- visible_primary_subject_id: than_kosis
- visible_secondary_subject_ids: john_carter
- primary_subject_frame_position: foreground right within zodanga_central_plaza_dais
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: Than Kosis standing
- subject_relation_summary: than_kosis plays against john_carter in the same frame
- scene_short_description: A massive military ceremony in a walled plaza where a hero is publicly honored by royalty.
- shot_moment_summary: Than Kosis announces the honor
- required_environment_anchor_1: ceremonial dais
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: preserve readable body-to-environment scale in frame
- camera_package_description: medium-full, low angle, normal lens, push in, zoom subtle in, shallow subject, high contrast ceremonial
- environment_subzone: zodanga_central_plaza_dais
- prompt_family: shot_prompt
- reference_asset_ids: than_kosis; john_carter; zodanga_central_plaza; DESC_CH021_SC006; DESC_CH021_SC006_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: than kosis
- image2_role: identity reference for the secondary visible subject
- image2_asset: john carter
- image3_role: environment reference for the scene location
- image3_asset: zodanga central plaza

# Continuity Notes
- Scene: CH021_SC006 / SC006.
- Variant: Primary Keyframe.
- Armor/Uniform state for john_carter
- Crowd density and military formation placement
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH021\CH021_SC006.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH021\CH021_SC006\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH021\CH021_SC006\SH002\DIALOGUE.json
