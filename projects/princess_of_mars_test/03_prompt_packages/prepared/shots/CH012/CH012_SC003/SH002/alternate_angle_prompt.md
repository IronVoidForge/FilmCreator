# Title
SH002 Shot Prompt - Alternate Angle

# ID
CH012_SC003_SH002_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for tars tarkas. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for carters quarters building. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. Two figures navigate a multi-story structure to select a strategic living quarter. The subject from image1 is tars tarkas, foreground right within carters quarters building interior, preserve readable body-to-environment scale in frame, front three-quarter right toward the scene action, entering stairs. The subject from image2 is tars tarkas plays against john carter in the same frame. Preserve the environment from image3 Multi-story verticality centered around a recurring courtyard with fountains and statues., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially carters quarters building interior. medium-full, low angle, normal lens, track, shallow subject, diffuse ambient. Readable medium composition in featuring. ascending the building levels. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH012_SC003; SHOT_INDEX; DIALOGUE; john_carter; tars_tarkas
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
- scene_id: CH012_SC003
- chapter_id: CH012
- shot_type: medium
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in carters_quarters_building featuring tars_tarkas, john_carter.
- shot_size: medium_full
- camera_angle: low_angle
- camera_motion: track
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: front_three_quarter_right
- visible_primary_subject_id: tars_tarkas
- visible_secondary_subject_ids: john_carter
- primary_subject_frame_position: foreground right within carters_quarters_building_interior
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: front three-quarter right toward the scene action
- primary_subject_pose_description: entering stairs
- subject_relation_summary: tars_tarkas plays against john_carter in the same frame
- scene_short_description: Two figures navigate a multi-story structure to select a strategic living quarter.
- shot_moment_summary: ascending the building levels
- required_environment_anchor_1: carters_quarters_building_interior
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: preserve readable body-to-environment scale in frame
- camera_package_description: medium-full, low angle, normal lens, track, shallow subject, diffuse ambient
- environment_subzone: carters_quarters_building_interior
- prompt_family: shot_prompt
- reference_asset_ids: tars_tarkas; john_carter; carters_quarters_building; DESC_CH012_SC003; DESC_CH012_SC003_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: tars tarkas
- image2_role: identity reference for the secondary visible subject
- image2_asset: john carter
- image3_role: environment reference for the scene location
- image3_asset: carters quarters building

# Continuity Notes
- Scene: CH012_SC003 / SC003.
- Variant: Alternate Angle.
- Precise height/floor level selection (Third Floor)
- Visual relationship between building elevation and prisoner locations
- Ascend through the building levels
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH012\CH012_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH012\CH012_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH012\CH012_SC003\SH002\DIALOGUE.json
