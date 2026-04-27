# Title
SH002 Shot Prompt - Primary Keyframe

# ID
CH010_SC002_SH002_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for dejah thoris. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for thark audience chamber. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. A captive woman defends her people before a seated assembly of green warriors. The subject from image1 is dejah thoris, foreground inside prisoner floor, height of Dejah vs Council seats, front three-quarter right toward the scene action, Dejah standing still. The subject from image2 is dejah thoris plays against lorquas ptomel in the same frame. Preserve the environment from image3 Large scale, designed for high-ranking Tharkian leadership and warriors., monumental scale, dry open Martian terrain, especially prisoner floor. medium-close, low angle, portrait lens, push in, zoom subtle in, shallow subject, backlit. Intimate composition that isolates, against to capture the beat's emotional turn. Dejah Thoris arguing for Heliumite role. prisoner floor. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH010_SC002; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris; tars_tarkas; lorquas_ptomel
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
- scene_id: CH010_SC002
- chapter_id: CH010
- shot_type: reaction_closeup
- previous_shot_id: SH001
- next_shot_id: (none)
- shot_lineage_ids: SH001; SH002
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates dejah_thoris, lorquas_ptomel against thark_audience_chamber to capture the beat's emotional turn.
- shot_size: medium_close
- camera_angle: low_angle
- camera_motion: push_in
- zoom_behavior: subtle_in
- focus_strategy: shallow_subject
- lighting_style: backlit
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: front_three_quarter_right
- visible_primary_subject_id: dejah_thoris
- visible_secondary_subject_ids: lorquas_ptomel
- primary_subject_frame_position: foreground inside prisoner_floor
- primary_subject_scale_relation: height of Dejah vs Council seats
- primary_subject_facing_direction: front three-quarter right toward the scene action
- primary_subject_pose_description: Dejah standing still
- subject_relation_summary: dejah_thoris plays against lorquas_ptomel in the same frame
- scene_short_description: A captive woman defends her people before a seated assembly of green warriors.
- shot_moment_summary: Dejah Thoris arguing for Heliumite role
- required_environment_anchor_1: prisoner_floor
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: height of Dejah vs Council seats
- camera_package_description: medium-close, low angle, portrait lens, push in, zoom subtle in, shallow subject, backlit
- environment_subzone: prisoner_floor
- prompt_family: shot_prompt
- reference_asset_ids: dejah_thoris; lorquas_ptomel; thark_audience_chamber; DESC_CH010_SC002; DESC_CH010_SC002_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: dejah thoris
- image2_role: identity reference for the secondary visible subject
- image2_asset: lorquas ptomel
- image3_role: environment reference for the scene location
- image3_asset: thark audience chamber

# Continuity Notes
- Scene: CH010_SC002 / SC002.
- Variant: Primary Keyframe.
- Fixed seating arrangement of Thark leaders
- Dejah Thoris must maintain prisoner positioning relative to the council
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH010\CH010_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH010\CH010_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH010\CH010_SC002\SH002\DIALOGUE.json
