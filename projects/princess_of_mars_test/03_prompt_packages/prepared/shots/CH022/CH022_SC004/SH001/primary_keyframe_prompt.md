# Title
SH001 Shot Prompt - Primary Keyframe

# ID
CH022_SC004_SH001_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the environment reference for zodanga palace interior. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. A man hides inside a large hanging ornament while officials discuss his superhuman threat. The subject from image1 is john carter, foreground inside interior of ornament, preserve readable body-to-environment scale in frame, facing directly toward camera, darkness/heavy breath. Preserve the environment from image2 monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, broad processional paths and stairs, especially interior of ornament. close-up, eye level, portrait lens, handheld, shallow subject, low key night. Intimate composition that isolates against to capture the beat's emotional turn. Carter breathing in the dark. interior of ornament. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH022_SC004; SHOT_INDEX; DIALOGUE; john_carter; notan; than_kosis
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: portrait
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
- scene_id: CH022_SC004
- chapter_id: CH022
- shot_type: reaction_closeup
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates john_carter against zodanga_palace_interior to capture the beat's emotional turn.
- shot_size: close_up
- camera_angle: eye_level
- camera_motion: handheld
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: low_key_night
- subject_visibility: partial
- narration_mode: none
- primary_subject_angle: front
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground inside interior of ornament
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: darkness/heavy breath
- subject_relation_summary: john_carter carries the frame alone
- scene_short_description: A man hides inside a large hanging ornament while officials discuss his superhuman threat.
- shot_moment_summary: Carter breathing in the dark
- required_environment_anchor_1: interior of ornament
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: preserve readable body-to-environment scale in frame
- camera_package_description: close-up, eye level, portrait lens, handheld, shallow subject, low key night
- environment_subzone: interior of ornament
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; zodanga_palace_interior; DESC_CH022_SC004; DESC_CH022_SC004_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: environment reference for the scene location
- image2_asset: zodanga palace interior

# Continuity Notes
- Scene: CH022_SC004 / SC004.
- Variant: Primary Keyframe.
- Lighting differential between dark interior ornament and bright Great Hall
- Muffled audio processing for voices heard through ornament walls
- Carter hides in the ornament amidst palace chaos
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH022\CH022_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH022\CH022_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH022\CH022_SC004\SH001\DIALOGUE.json
