# Title
SH001 Shot Prompt - Alternate Angle

# ID
CH011_SC002_SH001_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for ancient opulent quarters. Use image4 as the identity reference for an additional visible subject. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. Characters move into opulent ancient apartments overlooking a vast plaza. The subject from image1 is john carter, midground inside marble fresco zone, height of ceiling vs character height, front three-quarter right toward the scene action, characters entering frame. The subject from image2 is john carter plays against dejah thoris, sola in the same frame. Preserve the environment from image3 monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, broad processional paths and stairs, especially marble fresco zone. wide, low angle, wide lens, pan, deep focus, soft even. Wide composition across placed for immediate spatial orientation. Characters enter the opulent quarters. marble fresco zone. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH011_SC002; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris; sola
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
- scene_id: CH011_SC002
- chapter_id: CH011
- shot_type: establishing_wide
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across ancient_opulent_quarters with john_carter, dejah_thoris, sola placed for immediate spatial orientation.
- shot_size: wide
- camera_angle: low_angle
- camera_motion: pan
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: soft_even
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: front_three_quarter_right
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: dejah_thoris; sola
- primary_subject_frame_position: midground inside marble_fresco_zone
- primary_subject_scale_relation: height of ceiling vs character height
- primary_subject_facing_direction: front three-quarter right toward the scene action
- primary_subject_pose_description: characters entering frame
- subject_relation_summary: john_carter plays against dejah_thoris, sola in the same frame
- scene_short_description: Characters move into opulent ancient apartments overlooking a vast plaza.
- shot_moment_summary: Characters enter the opulent quarters
- required_environment_anchor_1: marble_fresco_zone
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: height of ceiling vs character height
- camera_package_description: wide, low angle, wide lens, pan, deep focus, soft even
- environment_subzone: marble_fresco_zone
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; dejah_thoris; sola; ancient_opulent_quarters; DESC_CH011_SC002; DESC_CH011_SC002_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: identity reference for the secondary visible subject
- image2_asset: dejah thoris
- image3_role: environment reference for the scene location
- image3_asset: ancient opulent quarters
- image4_role: identity reference for an additional visible subject
- image4_asset: sola

# Continuity Notes
- Scene: CH011_SC002 / SC002.
- Variant: Alternate Angle.
- Transition from harsh exterior lighting to soft, luxurious interior lighting
- Character placement within the new quarters relative to the plaza view
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH011\CH011_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH011\CH011_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH011\CH011_SC002\SH001\DIALOGUE.json
