# Title
SH002 Shot Prompt - Alternate Angle

# ID
CH001_SC001_SH002_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the environment reference for arizona quartz vein location. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. Two men discover a massive gold-bearing quartz vein amidst rugged Arizona hills. The subject from image1 is gold vein, foreground right within arizona quartz vein location, vein size vs hand/tool, facing directly toward camera, focus on rock face. Preserve the environment from image2 Vast mountain ranges containing localized mineral deposits and rocky terrain., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially gold-bearing quartz vein. Keep one readable subject anchor: focus on rock face. insert-detail, eye level, normal lens, locked off, zoom subtle in, shallow subject, high contrast ceremonial. Detail composition centered on the key physical action or prop inside. the gold vein is visible. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH001_SC001; SHOT_INDEX; DIALOGUE; john_carter; james_k_powell
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
- scene_id: CH001_SC001
- chapter_id: CH001
- shot_type: insert_detail
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Tight detail framing focused on a single visual object or gesture.
- composition: Detail composition centered on the key physical action or prop inside arizona_quartz_vein_location.
- shot_size: insert_detail
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: subtle_in
- focus_strategy: shallow_subject
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground right within arizona_quartz_vein_location
- primary_subject_scale_relation: vein size vs hand/tool
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: focus on rock face
- subject_relation_summary: gold vein carries the frame alone
- scene_short_description: Two men discover a massive gold-bearing quartz vein amidst rugged Arizona hills.
- shot_moment_summary: the gold vein is visible
- required_environment_anchor_1: gold-bearing quartz vein
- required_subject_anchor_1: focus on rock face
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: vein size vs hand/tool
- camera_package_description: insert-detail, eye level, normal lens, locked off, zoom subtle in, shallow subject, high contrast ceremonial
- environment_subzone: arizona_quartz_vein_location
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; arizona_quartz_vein_location; DESC_CH001_SC001; DESC_CH001_SC001_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: environment reference for the scene location
- image2_asset: arizona quartz vein location

# Continuity Notes
- Scene: CH001_SC001 / SC001.
- Variant: Alternate Angle.
- Physical appearance of the gold vein
- Specific tools and gear used by prospectors
- The discovery of the gold vein
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH001\CH001_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH001\CH001_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH001\CH001_SC001\SH002\DIALOGUE.json
