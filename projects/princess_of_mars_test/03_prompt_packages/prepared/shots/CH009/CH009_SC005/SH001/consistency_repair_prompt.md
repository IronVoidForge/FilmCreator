# Title
SH001 Shot Prompt - Consistency Repair

# ID
CH009_SC005_SH001_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for sarkoja. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for communal sleeping quarters. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. A group of Martian women argue intensely around a central point regarding a captive. The subject from image1 is sarkoja, foreground entry line within communal sleeping quarters center, human scale vs group size, front three-quarter right toward the scene action, shouting begins. The subject from image2 is sarkoja plays against sola in the same frame. Preserve the environment from image3 monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, broad processional paths and stairs, especially communal sleeping quarters center. medium, eye level, normal lens, handheld, deep focus, diffuse ambient. Readable medium composition in featuring. women shouting about the prisoner. center. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH009_SC005; SHOT_INDEX; DIALOGUE; sola; sarkoja; protagonist
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: normal
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
- scene_id: CH009_SC005
- chapter_id: CH009
- shot_type: medium
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in communal_sleeping_quarters featuring sarkoja, Other Female Martians, sola.
- shot_size: medium
- camera_angle: eye_level
- camera_motion: handheld
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: front_three_quarter_right
- visible_primary_subject_id: sarkoja
- visible_secondary_subject_ids: sola
- primary_subject_frame_position: foreground entry line within communal_sleeping_quarters_center
- primary_subject_scale_relation: human scale vs group size
- primary_subject_facing_direction: front three-quarter right toward the scene action
- primary_subject_pose_description: shouting begins
- subject_relation_summary: sarkoja plays against sola in the same frame
- scene_short_description: A group of Martian women argue intensely around a central point regarding a captive.
- shot_moment_summary: women shouting about the prisoner
- required_environment_anchor_1: communal_sleeping_quarters_center
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: human scale vs group size
- camera_package_description: medium, eye level, normal lens, handheld, deep focus, diffuse ambient
- environment_subzone: communal_sleeping_quarters_center
- prompt_family: shot_prompt
- reference_asset_ids: sarkoja; sola; communal_sleeping_quarters; DESC_CH009_SC005; DESC_CH009_SC005_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: sarkoja
- image2_role: identity reference for the secondary visible subject
- image2_asset: sola
- image3_role: environment reference for the scene location
- image3_asset: communal sleeping quarters

# Continuity Notes
- Scene: CH009_SC005 / SC005.
- Variant: Consistency Repair.
- Emotional intensity levels must scale from heated to somber
- Character placement within the circular group formation
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH009\CH009_SC005.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH009\CH009_SC005\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH009\CH009_SC005\SH001\DIALOGUE.json
