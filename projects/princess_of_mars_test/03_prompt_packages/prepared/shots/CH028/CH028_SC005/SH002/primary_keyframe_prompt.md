# Title
SH002 Shot Prompt - Primary Keyframe

# ID
CH028_SC005_SH002_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the environment reference for hudson river study. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. A man gazes through a window at a distant red planet while experiencing ethereal visions. The subject from image1 is Mars, midground inside exterior night sky, celestial size vs window frame, facing directly toward camera, sky view. Preserve the environment from image2 monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, broad processional paths and stairs, especially exterior night sky. Keep celestial anchor the red planet stable in the frame. wide, eye level, telephoto lens, push in, zoom subtle in, environment priority, diffuse ambient. Wide composition across placed for immediate spatial orientation. Mars appearing in the sky. exterior night sky. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH028_SC005; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: telephoto
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
- scene_id: CH028_SC005
- chapter_id: CH028
- shot_type: establishing_wide
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across hudson_river_study with john_carter placed for immediate spatial orientation.
- shot_size: wide
- camera_angle: eye_level
- camera_motion: push_in
- zoom_behavior: subtle_in
- focus_strategy: environment_priority
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: midground inside exterior night sky
- primary_subject_scale_relation: celestial size vs window frame
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: sky view
- subject_relation_summary: Mars carries the frame alone
- scene_short_description: A man gazes through a window at a distant red planet while experiencing ethereal visions.
- shot_moment_summary: Mars appearing in the sky
- required_environment_anchor_1: exterior night sky
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: Mars
- required_scale_proof_detail: celestial size vs window frame
- camera_package_description: wide, eye level, telephoto lens, push in, zoom subtle in, environment priority, diffuse ambient
- environment_subzone: exterior night sky
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; hudson_river_study; DESC_CH028_SC005; DESC_CH028_SC005_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: environment reference for the scene location
- image2_asset: hudson river study

# Continuity Notes
- Scene: CH028_SC005 / SC005.
- Variant: Primary Keyframe.
- Visual appearance of Mars in the night sky.
- Lighting balance between interior lamp light and exterior moonlight.
- The sight of Mars triggers memory/longing
- Resolve The Child (Vision/Sensation) -> The Child (Vision/Sensation)
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH028\CH028_SC005.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH028\CH028_SC005\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH028\CH028_SC005\SH002\DIALOGUE.json
