# Title
SH003 Shot Prompt - Alternate Angle

# ID
CH022_SC004_SH003_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for notan. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for zodanga palace interior. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. A man hides inside a large hanging ornament while officials discuss his superhuman threat. The subject from image1 is notan, foreground inside great hall floor, preserve readable body-to-environment scale in frame, profile left toward the scene action, Notan speaking. The subject from image2 is notan plays against than kosis in the same frame. Preserve the environment from image3 monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, broad processional paths and stairs, especially great hall floor. medium-close, eye level, normal lens, locked off, zoom subtle in, shallow subject, high contrast ceremonial. Intimate composition that isolates, against to capture the beat's emotional turn. Notan reports superhuman status. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH022_SC004; SHOT_INDEX; DIALOGUE; john_carter; notan; than_kosis
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: normal
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: alternate_angle
- review_notes: Prompt body is missing the required subject anchor for an on-screen shot.
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH022_SC004
- chapter_id: CH022
- shot_type: reaction_closeup
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates notan, than_kosis against zodanga_palace_interior to capture the beat's emotional turn.
- shot_size: medium_close
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: subtle_in
- focus_strategy: shallow_subject
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: profile_left
- visible_primary_subject_id: notan
- visible_secondary_subject_ids: than_kosis
- primary_subject_frame_position: foreground inside great hall floor
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: profile left toward the scene action
- primary_subject_pose_description: Notan speaking
- subject_relation_summary: notan plays against than_kosis in the same frame
- scene_short_description: A man hides inside a large hanging ornament while officials discuss his superhuman threat.
- shot_moment_summary: Notan reports superhuman status
- required_environment_anchor_1: great hall floor
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: preserve readable body-to-environment scale in frame
- camera_package_description: medium-close, eye level, normal lens, locked off, zoom subtle in, shallow subject, high contrast ceremonial
- environment_subzone: great hall floor
- prompt_family: shot_prompt
- reference_asset_ids: notan; than_kosis; zodanga_palace_interior; DESC_CH022_SC004; DESC_CH022_SC004_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: notan
- image2_role: identity reference for the secondary visible subject
- image2_asset: than kosis
- image3_role: environment reference for the scene location
- image3_asset: zodanga palace interior

# Continuity Notes
- Scene: CH022_SC004 / SC004.
- Variant: Alternate Angle.
- Lighting differential between dark interior ornament and bright Great Hall
- Muffled audio processing for voices heard through ornament walls
- Notan reports the superhuman threat to Than Kosis
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH022\CH022_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH022\CH022_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH022\CH022_SC004\SH003\DIALOGUE.json
