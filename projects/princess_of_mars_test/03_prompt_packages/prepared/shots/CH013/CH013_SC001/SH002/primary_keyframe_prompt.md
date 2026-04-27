# Title
SH002 Shot Prompt - Primary Keyframe

# ID
CH013_SC001_SH002_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the environment reference for green martian city complex. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. A human man uses gentle authority to tame large, aggressive Martian beasts within a city complex. The subject from image1 is john carter, foreground inside training arena, hand size vs beast hide, profile right toward the scene action, reaching out. Preserve the environment from image2 Features wide thoroughfares, central leadership hubs, and large-scale enclosures/pens for beasts., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially training arena. Keep one readable subject anchor: Carter close to beast head/neck. close-up, eye level, portrait lens, locked off, zoom subtle in, shallow subject, soft even. Detail composition centered on the key physical action or prop inside. Carter's hands and face during taming. training arena. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH013_SC001; SHOT_INDEX; DIALOGUE; john_carter; tars_tarkas; green_martian_warriors
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: portrait
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: primary_keyframe
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH013_SC001
- chapter_id: CH013
- shot_type: insert_detail
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Tight detail framing focused on a single visual object or gesture.
- composition: Detail composition centered on the key physical action or prop inside green_martian_city_complex.
- shot_size: close_up
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: subtle_in
- focus_strategy: shallow_subject
- lighting_style: soft_even
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: profile_right
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground inside training_arena
- primary_subject_scale_relation: hand size vs beast hide
- primary_subject_facing_direction: profile right toward the scene action
- primary_subject_pose_description: reaching out
- subject_relation_summary: john_carter carries the frame alone
- scene_short_description: A human man uses gentle authority to tame large, aggressive Martian beasts within a city complex.
- shot_moment_summary: Carter's hands and face during taming
- required_environment_anchor_1: training_arena
- required_subject_anchor_1: Carter close to beast head/neck
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: hand size vs beast hide
- camera_package_description: close-up, eye level, portrait lens, locked off, zoom subtle in, shallow subject, soft even
- environment_subzone: training_arena
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; green_martian_city_complex; DESC_CH013_SC001; DESC_CH013_SC001_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: environment reference for the scene location
- image2_asset: green martian city complex

# Continuity Notes
- Scene: CH013_SC001 / SC001.
- Variant: Primary Keyframe.
- Physical behavior shift of thoats from wild to docile
- Carter's training attire consistency
- Specific hand/body movements used in taming process
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH013\CH013_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH013\CH013_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH013\CH013_SC001\SH002\DIALOGUE.json
