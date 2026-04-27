# Title
SH002 Shot Prompt - Primary Keyframe

# ID
CH013_SC003_SH002_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for dejah thoris. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for martian night plaza. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. A reunion in a Martian plaza under two moons turns into a revelation of sabotage. The subject from image1 is dejah thoris, foreground inside martian night plaza center, preserve readable body-to-environment scale in frame, facing directly toward camera, Dejah looking up. The subject from image2 is dejah thoris plays against john carter in the same frame. Preserve the environment from image3 Expansive open spaces with large-scale architecture casting shadows., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially martian night plaza center. Keep one readable subject anchor: dejah thoris hands. close-up, eye level, portrait lens, locked off, zoom subtle in, shallow subject, low key night. Detail composition centered on the key physical action or prop inside. Close up on Dejah's weary face and hands. center. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH013_SC003; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris; sola
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
- scene_id: CH013_SC003
- chapter_id: CH013
- shot_type: insert_detail
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Tight detail framing focused on a single visual object or gesture.
- composition: Detail composition centered on the key physical action or prop inside martian_night_plaza.
- shot_size: close_up
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: subtle_in
- focus_strategy: shallow_subject
- lighting_style: low_key_night
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: front
- visible_primary_subject_id: dejah_thoris
- visible_secondary_subject_ids: john_carter
- primary_subject_frame_position: foreground inside martian_night_plaza center
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: Dejah looking up
- subject_relation_summary: dejah_thoris plays against john_carter in the same frame
- scene_short_description: A reunion in a Martian plaza under two moons turns into a revelation of sabotage.
- shot_moment_summary: Close up on Dejah's weary face and hands
- required_environment_anchor_1: martian_night_plaza center
- required_subject_anchor_1: dejah_thoris hands
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: preserve readable body-to-environment scale in frame
- camera_package_description: close-up, eye level, portrait lens, locked off, zoom subtle in, shallow subject, low key night
- environment_subzone: martian_night_plaza center
- prompt_family: shot_prompt
- reference_asset_ids: dejah_thoris; john_carter; martian_night_plaza; DESC_CH013_SC003; DESC_CH013_SC003_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: dejah thoris
- image2_role: identity reference for the secondary visible subject
- image2_asset: john carter
- image3_role: environment reference for the scene location
- image3_asset: martian night plaza

# Continuity Notes
- Scene: CH013_SC003 / SC003.
- Variant: Primary Keyframe.
- Dejah Thoris physical signs of fatigue and labor (sweat, grime, exhaustion)
- Proximity of Sola to Dejah
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH013\CH013_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH013\CH013_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH013\CH013_SC003\SH002\DIALOGUE.json
