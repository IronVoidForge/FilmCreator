# Title
SH002 Shot Prompt - Alternate Angle

# ID
CH009_SC004_SH002_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for sarkoja. Use image2 as the environment reference for communal sleeping quarters. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. A protagonist listens from the shadows as Martian adults discuss an impending execution. The subject from image1 is sarkoja, foreground inside communal gathering area, group size vs communal space, rear three-quarter left away from camera, voices heard. Preserve the environment from image2 monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, broad processional paths and stairs, especially communal gathering area. medium-close, eye level, normal lens, pan, environment priority, low key night. Intimate composition that isolates, against to capture the beat's emotional turn. Sarkoja speaking to others. communal gathering area. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH009_SC004; SHOT_INDEX; DIALOGUE; protagonist; sarkoja
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
- scene_id: CH009_SC004
- chapter_id: CH009
- shot_type: reaction_closeup
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates sarkoja, Other Martians (voices) against communal_sleeping_quarters to capture the beat's emotional turn.
- shot_size: medium_close
- camera_angle: eye_level
- camera_motion: pan
- zoom_behavior: none
- focus_strategy: environment_priority
- lighting_style: low_key_night
- subject_visibility: silhouette
- narration_mode: in_scene_speaker
- primary_subject_angle: rear_three_quarter_left
- visible_primary_subject_id: sarkoja
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground inside communal_gathering_area
- primary_subject_scale_relation: group size vs communal space
- primary_subject_facing_direction: rear three-quarter left away from camera
- primary_subject_pose_description: voices heard
- subject_relation_summary: sarkoja carries the frame alone
- scene_short_description: A protagonist listens from the shadows as Martian adults discuss an impending execution.
- shot_moment_summary: Sarkoja speaking to others
- required_environment_anchor_1: communal_gathering_area
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: group size vs communal space
- camera_package_description: medium-close, eye level, normal lens, pan, environment priority, low key night
- environment_subzone: communal_gathering_area
- prompt_family: shot_prompt
- reference_asset_ids: sarkoja; communal_sleeping_quarters; DESC_CH009_SC004; DESC_CH009_SC004_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: sarkoja
- image2_role: environment reference for the scene location
- image2_asset: communal sleeping quarters

# Continuity Notes
- Scene: CH009_SC004 / SC004.
- Variant: Alternate Angle.
- Dialogue regarding Thark, execution, and Tal Hajus must be audibly distinct
- Protagonist remains in a listening/eavesdropping position throughout the revelation
- Sarkoja discusses the movement of prisoners
- Resolve Other Martians (voices) -> Other Martians (voices)
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH009\CH009_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH009\CH009_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH009\CH009_SC004\SH002\DIALOGUE.json
