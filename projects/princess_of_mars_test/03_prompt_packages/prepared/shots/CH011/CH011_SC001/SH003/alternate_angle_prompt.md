# Title
SH003 Shot Prompt - Alternate Angle

# ID
CH011_SC001_SH003_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for sola. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for ancient opulent quarters. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. A human male intervenes in a confrontation to secure a princess and reassign a captive. The subject from image1 is sola, foreground right within captive quarters vicinity, preserve readable body-to-environment scale in frame, facing directly toward camera, Sola as captive. The subject from image2 is sola plays against dejah thoris in the same frame. Preserve the environment from image3 monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, broad processional paths and stairs, especially captive quarters vicinity. medium-full, eye level, wide lens, track, deep focus, diffuse ambient. Closing composition in that emphasizes the consequence of carter assigns as guard and moves the group. Sola assumes guard role. captive quarters vicinity. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH011_SC001; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris; sola; sarkoja
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: wide
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
- shot_type: closing_reaction
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Controlled closing frame that lands the consequence of the beat.
- composition: Closing composition in ancient_opulent_quarters that emphasizes the consequence of carter assigns sola as guard and moves the group.
- shot_size: medium_full
- camera_angle: eye_level
- camera_motion: track
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: front
- visible_primary_subject_id: sola
- visible_secondary_subject_ids: dejah_thoris
- primary_subject_frame_position: foreground right within captive_quarters_vicinity
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: Sola as captive
- subject_relation_summary: sola plays against dejah_thoris in the same frame
- scene_short_description: A human male intervenes in a confrontation to secure a princess and reassign a captive.
- shot_moment_summary: Sola assumes guard role
- required_environment_anchor_1: captive_quarters_vicinity
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: preserve readable body-to-environment scale in frame
- camera_package_description: medium-full, eye level, wide lens, track, deep focus, diffuse ambient
- environment_subzone: captive_quarters_vicinity
- prompt_family: shot_prompt
- reference_asset_ids: sola; dejah_thoris; ancient_opulent_quarters; DESC_CH011_SC001; DESC_CH011_SC001_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: sola
- image2_role: identity reference for the secondary visible subject
- image2_asset: dejah thoris
- image3_role: environment reference for the scene location
- image3_asset: ancient opulent quarters

# Continuity Notes
- Scene: CH011_SC001 / SC001.
- Variant: Alternate Angle.
- Carter's physical proximity and positioning relative to Dejah Thoris
- Sola's transition from prisoner/captive status to guard status
- Carter assigns Sola as guard and moves the group
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH011\CH011_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH011\CH011_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH011\CH011_SC001\SH003\DIALOGUE.json
