# Title
SH001 Shot Prompt - Primary Keyframe

# ID
CH014_SC001_SH001_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for martian plains and march route. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. A group marches across open Martian plains toward Thark under shifting light. The subject from image1 is marching group, midground inside martian plains and march route, horizon line vs group size, front three-quarter right toward the scene action, wide vista. The subject from image2 is marching group plays against dejah thoris in the same frame. Preserve the environment from image3 Continuous stretch of undulating terrain, long-distance vistas., monumental scale, dry open Martian terrain, especially martian plains and march route. wide, eye level, wide lens, track, deep focus, diffuse ambient. Wide composition across placed for immediate spatial orientation. wide view of the group moving across the plains. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH014_SC001; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris; tars_tarkas; sarkoja
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
- scene_id: CH014_SC001
- chapter_id: CH014
- shot_type: establishing_wide
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across martian_plains_and_march_route with john_carter, dejah_thoris placed for immediate spatial orientation.
- shot_size: wide
- camera_angle: eye_level
- camera_motion: track
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_right
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: dejah_thoris
- primary_subject_frame_position: midground inside martian_plains_and_march_route
- primary_subject_scale_relation: horizon line vs group size
- primary_subject_facing_direction: front three-quarter right toward the scene action
- primary_subject_pose_description: wide vista
- subject_relation_summary: marching_group plays against dejah_thoris in the same frame
- scene_short_description: A group marches across open Martian plains toward Thark under shifting light.
- shot_moment_summary: wide view of the group moving across the plains
- required_environment_anchor_1: martian_plains_and_march_route
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: horizon line vs group size
- camera_package_description: wide, eye level, wide lens, track, deep focus, diffuse ambient
- environment_subzone: martian_plains_and_march_route
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; dejah_thoris; martian_plains_and_march_route; DESC_CH014_SC001; DESC_CH014_SC001_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: identity reference for the secondary visible subject
- image2_asset: dejah thoris
- image3_role: environment reference for the scene location
- image3_asset: martian plains and march route

# Continuity Notes
- Scene: CH014_SC001 / SC001.
- Variant: Primary Keyframe.
- Position and rattling of Dejah's chains
- Variable distance between characters in the march line
- Lighting/time of day progression during the trek
- Carter reflects on his feelings and cultural barriers
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH014\CH014_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH014\CH014_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH014\CH014_SC001\SH001\DIALOGUE.json
