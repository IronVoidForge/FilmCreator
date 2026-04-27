# Title
SH003 Shot Prompt - Primary Keyframe

# ID
CH022_SC001_SH003_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for zodanga palace interior. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. A hidden observer watches a royal woman declare her marriage intent within a private chamber. The subject from image1 is john carter, foreground inside zodanga palace interior, preserve readable body-to-environment scale in frame, facing directly toward camera, Dejah speaks. The subject from image2 is john carter plays against dejah thoris in the same frame. Preserve the environment from image3 monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, broad processional paths and stairs, especially zodanga palace interior. tight framing on eyes. extreme-close-up, eye level, telephoto lens, locked off, zoom subtle in, shallow subject, low key night. Intimate composition that isolates, against to capture the beat's emotional turn. Carter reacts to the betrayal. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH022_SC001; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris; than_kosis; sab_than
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
- scene_id: CH022_SC001
- chapter_id: CH022
- shot_type: reaction_closeup
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates john_carter, dejah_thoris against zodanga_palace_interior to capture the beat's emotional turn.
- shot_size: extreme_close_up
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: subtle_in
- focus_strategy: shallow_subject
- lighting_style: low_key_night
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: dejah_thoris
- primary_subject_frame_position: foreground inside zodanga_palace_interior
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: Dejah speaks
- subject_relation_summary: john_carter plays against dejah_thoris in the same frame
- scene_short_description: A hidden observer watches a royal woman declare her marriage intent within a private chamber.
- shot_moment_summary: Carter reacts to the betrayal
- required_environment_anchor_1: zodanga_palace_interior
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: tight framing on eyes
- camera_package_description: extreme-close-up, eye level, telephoto lens, locked off, zoom subtle in, shallow subject, low key night
- environment_subzone: zodanga_palace_interior
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; dejah_thoris; zodanga_palace_interior; DESC_CH022_SC001; DESC_CH022_SC001_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: identity reference for the secondary visible subject
- image2_asset: dejah thoris
- image3_role: environment reference for the scene location
- image3_asset: zodanga palace interior

# Continuity Notes
- Scene: CH022_SC001 / SC001.
- Variant: Primary Keyframe.
- Carter's physical position relative to the tapestry edge
- Dejah Thoris's regal attire and posture consistency
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH022\CH022_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH022\CH022_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH022\CH022_SC001\SH003\DIALOGUE.json
