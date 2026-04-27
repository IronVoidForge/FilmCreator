# Title
SH001 Shot Prompt - Alternate Angle

# ID
CH011_SC001_SH001_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for sarkoja. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for ancient opulent quarters. Use image4 as the identity reference for an additional visible subject. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. A human male intervenes in a confrontation to secure a princess and reassign a captive. The subject from image1 is sarkoja, foreground entry line within captive quarters vicinity, distance between Sarkoja and Dejah, profile left toward the scene action, Sarkoja looming over Dejah. The subject from image2 is sarkoja plays against dejah thoris, john carter in the same frame. Preserve the environment from image3 monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, broad processional paths and stairs, especially captive quarters vicinity. medium, eye level, normal lens, locked off, shallow subject, low key night. Wide composition across placed for immediate spatial orientation. Sarkoja mistreating Dejah Thoris. captive quarters vicinity. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH011_SC001; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris; sola; sarkoja
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
- scene_id: CH011_SC001
- chapter_id: CH011
- shot_type: establishing_wide
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across ancient_opulent_quarters with sarkoja, dejah_thoris, john_carter placed for immediate spatial orientation.
- shot_size: medium
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: low_key_night
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: profile_left
- visible_primary_subject_id: sarkoja
- visible_secondary_subject_ids: dejah_thoris; john_carter
- primary_subject_frame_position: foreground entry line within captive_quarters_vicinity
- primary_subject_scale_relation: distance between Sarkoja and Dejah
- primary_subject_facing_direction: profile left toward the scene action
- primary_subject_pose_description: Sarkoja looming over Dejah
- subject_relation_summary: sarkoja plays against dejah_thoris, john_carter in the same frame
- scene_short_description: A human male intervenes in a confrontation to secure a princess and reassign a captive.
- shot_moment_summary: Sarkoja mistreating Dejah Thoris
- required_environment_anchor_1: captive_quarters_vicinity
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: distance between Sarkoja and Dejah
- camera_package_description: medium, eye level, normal lens, locked off, shallow subject, low key night
- environment_subzone: captive_quarters_vicinity
- prompt_family: shot_prompt
- reference_asset_ids: sarkoja; dejah_thoris; john_carter; ancient_opulent_quarters; DESC_CH011_SC001; DESC_CH011_SC001_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: sarkoja
- image2_role: identity reference for the secondary visible subject
- image2_asset: dejah thoris
- image3_role: environment reference for the scene location
- image3_asset: ancient opulent quarters
- image4_role: identity reference for an additional visible subject
- image4_asset: john carter

# Continuity Notes
- Scene: CH011_SC001 / SC001.
- Variant: Alternate Angle.
- Carter's physical proximity and positioning relative to Dejah Thoris
- Sola's transition from prisoner/captive status to guard status
- Carter intervenes in the mistreatment of Dejah Thoris
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH011\CH011_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH011\CH011_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH011\CH011_SC001\SH001\DIALOGUE.json
