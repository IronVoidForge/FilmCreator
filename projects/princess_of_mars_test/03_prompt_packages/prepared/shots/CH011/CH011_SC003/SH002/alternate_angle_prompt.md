# Title
SH002 Shot Prompt - Alternate Angle

# ID
CH011_SC003_SH002_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the environment reference for ancient opulent quarters. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. A quiet moment in opulent quarters is broken by an external messenger's summons. The subject from image1 is john carter, foreground inside seating area, preserve readable body-to-environment scale in frame, facing directly toward camera, alertness. Preserve the environment from image2 monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, broad processional paths and stairs, especially doorway/threshold. Keep one readable subject anchor: remains in place but shifts posture. close-up, eye level, portrait lens, push in, zoom subtle in, shallow subject, high contrast ceremonial. Intimate composition that isolates, against to capture the beat's emotional turn. Carter receiving the news of Lorquas Ptomel's summons. seating area. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH011_SC003; SHOT_INDEX; DIALOGUE; john_carter; lorquas_ptomel
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
- scene_id: CH011_SC003
- chapter_id: CH011
- shot_type: reaction_closeup
- previous_shot_id: SH001
- next_shot_id: (none)
- shot_lineage_ids: SH001; SH002
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates john_carter, Messenger (implied/off-screen) against ancient_opulent_quarters to capture the beat's emotional turn.
- shot_size: close_up
- camera_angle: eye_level
- camera_motion: push_in
- zoom_behavior: subtle_in
- focus_strategy: shallow_subject
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground inside seating area
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: alertness
- subject_relation_summary: john_carter carries the frame alone
- scene_short_description: A quiet moment in opulent quarters is broken by an external messenger's summons.
- shot_moment_summary: Carter receiving the news of Lorquas Ptomel's summons
- required_environment_anchor_1: doorway/threshold
- required_subject_anchor_1: remains in place but shifts posture
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: preserve readable body-to-environment scale in frame
- camera_package_description: close-up, eye level, portrait lens, push in, zoom subtle in, shallow subject, high contrast ceremonial
- environment_subzone: seating area
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; ancient_opulent_quarters; DESC_CH011_SC003; DESC_CH011_SC003_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: environment reference for the scene location
- image2_asset: ancient opulent quarters

# Continuity Notes
- Scene: CH011_SC003 / SC003.
- Variant: Alternate Angle.
- Timing of summons must immediately follow the conclusion of SC002 conversation
- The summons arrives
- Resolve Messenger (implied/off-screen) -> Messenger (implied/off-screen)
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH011\CH011_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH011\CH011_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH011\CH011_SC003\SH002\DIALOGUE.json
