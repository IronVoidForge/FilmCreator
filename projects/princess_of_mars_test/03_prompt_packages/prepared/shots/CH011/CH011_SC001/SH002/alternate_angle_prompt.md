# Title
SH002 Shot Prompt - Alternate Angle

# ID
CH011_SC001_SH002_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for ancient opulent quarters. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. A human male intervenes in a confrontation to secure a princess and reassign a captive. The subject from image1 is john carter, foreground inside captive quarters vicinity, preserve readable body-to-environment scale in frame, front three-quarter right toward the scene action, Carter facing Sarkoja. The subject from image2 is john carter plays against sarkoja in the same frame. Preserve the environment from image3 monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, broad processional paths and stairs, especially captive quarters vicinity. Keep one readable subject anchor: Carter dominates the space via eye contact and threat. close-up, low angle, portrait lens, push in, zoom subtle in, shallow subject, hard directional. Intimate composition that isolates, against to capture the beat's emotional turn. Carter issues lethal threat. captive quarters vicinity. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH011_SC001; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris; sola; sarkoja
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: portrait
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
- scene_id: CH011_SC001
- chapter_id: CH011
- shot_type: reaction_closeup
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates john_carter, sarkoja against ancient_opulent_quarters to capture the beat's emotional turn.
- shot_size: close_up
- camera_angle: low_angle
- camera_motion: push_in
- zoom_behavior: subtle_in
- focus_strategy: shallow_subject
- lighting_style: hard_directional
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: front_three_quarter_right
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: sarkoja
- primary_subject_frame_position: foreground inside captive_quarters_vicinity
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: front three-quarter right toward the scene action
- primary_subject_pose_description: Carter facing Sarkoja
- subject_relation_summary: john_carter plays against sarkoja in the same frame
- scene_short_description: A human male intervenes in a confrontation to secure a princess and reassign a captive.
- shot_moment_summary: Carter issues lethal threat
- required_environment_anchor_1: captive_quarters_vicinity
- required_subject_anchor_1: Carter dominates the space via eye contact and threat
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: preserve readable body-to-environment scale in frame
- camera_package_description: close-up, low angle, portrait lens, push in, zoom subtle in, shallow subject, hard directional
- environment_subzone: captive_quarters_vicinity
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; sarkoja; ancient_opulent_quarters; DESC_CH011_SC001; DESC_CH011_SC001_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: identity reference for the secondary visible subject
- image2_asset: sarkoja
- image3_role: environment reference for the scene location
- image3_asset: ancient opulent quarters

# Continuity Notes
- Scene: CH011_SC001 / SC001.
- Variant: Alternate Angle.
- Carter's physical proximity and positioning relative to Dejah Thoris
- Sola's transition from prisoner/captive status to guard status
- Carter issues a lethal threat to Sarkoja
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH011\CH011_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH011\CH011_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH011\CH011_SC001\SH002\DIALOGUE.json
