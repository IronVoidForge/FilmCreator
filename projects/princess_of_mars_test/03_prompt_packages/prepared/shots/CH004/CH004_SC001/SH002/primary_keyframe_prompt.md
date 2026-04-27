# Title
SH002 Shot Prompt - Primary Keyframe

# ID
CH004_SC001_SH002_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for tars tarkas. Use image2 as the environment reference for ancient martian city ruins. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. A duo traverses a massive white marble city inlaid with gold while observing callous Martian crowds. The subject from image1 is tars tarkas, foreground right within Grand Streets, Architecture and Martians are oversized relative to the narrator, front three-quarter right toward the scene action, medium shot of duo. Preserve the environment from image2 monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, broad processional paths and stairs, especially Grand Streets. medium-full, eye level, wide lens, track, shallow subject, diffuse ambient. Readable medium composition in featuring. Duo walking through the street. Grand Streets. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH004_SC001; SHOT_INDEX; DIALOGUE; tars_tarkas
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
- scene_id: CH004_SC001
- chapter_id: CH004
- shot_type: medium
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in ancient_martian_city_ruins featuring tars_tarkas, * The Narrator.
- shot_size: medium_full
- camera_angle: eye_level
- camera_motion: track
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_right
- visible_primary_subject_id: tars_tarkas
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground right within Grand Streets
- primary_subject_scale_relation: Architecture and Martians are oversized relative to the narrator.
- primary_subject_facing_direction: front three-quarter right toward the scene action
- primary_subject_pose_description: medium shot of duo
- subject_relation_summary: tars_tarkas carries the frame alone
- scene_short_description: A duo traverses a massive white marble city inlaid with gold while observing callous Martian crowds.
- shot_moment_summary: Duo walking through the street
- required_environment_anchor_1: Grand Streets
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: Architecture and Martians are oversized relative to the narrator.
- camera_package_description: medium-full, eye level, wide lens, track, shallow subject, diffuse ambient
- environment_subzone: Grand Streets
- prompt_family: shot_prompt
- reference_asset_ids: tars_tarkas; ancient_martian_city_ruins; DESC_CH004_SC001; DESC_CH004_SC001_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: tars tarkas
- image2_role: environment reference for the scene location
- image2_asset: ancient martian city ruins

# Continuity Notes
- Scene: CH004_SC001 / SC001.
- Variant: Primary Keyframe.
- Scale comparison between narrator and oversized architecture/Martians
- Lighting consistency in the open plaza
- Walking through the streets
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH004\CH004_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH004\CH004_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH004\CH004_SC001\SH002\DIALOGUE.json
