# Title
SH003 Shot Prompt - Alternate Angle

# ID
CH023_SC004_SH003_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the environment reference for desolate martian wasteland. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. A pilot survives a crash and realizes his navigation tools are broken while flying over wasteland. The subject from image1 is john carter, foreground right within air machine cockpit, preserve readable body-to-environment scale in frame, profile left toward the scene action, looking at horizon. Preserve the environment from image2 Immense scale with vast arid plains and widely dispersed ruins., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially air machine cockpit. medium, eye level, portrait lens, push in, zoom subtle in, shallow subject, low key night. Closing composition in that emphasizes the consequence of realization of being lost. Carter realizes he is lost. air machine cockpit. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH023_SC004; SHOT_INDEX; DIALOGUE; john_carter
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: portrait
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
- scene_id: CH023_SC004
- chapter_id: CH023
- shot_type: closing_reaction
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Controlled closing frame that lands the consequence of the beat.
- composition: Closing composition in desolate_martian_wasteland that emphasizes the consequence of realization of being lost.
- shot_size: medium
- camera_angle: eye_level
- camera_motion: push_in
- zoom_behavior: subtle_in
- focus_strategy: shallow_subject
- lighting_style: low_key_night
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: profile_left
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground right within air_machine_cockpit
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: profile left toward the scene action
- primary_subject_pose_description: looking at horizon
- subject_relation_summary: john_carter carries the frame alone
- scene_short_description: A pilot survives a crash and realizes his navigation tools are broken while flying over wasteland.
- shot_moment_summary: Carter realizes he is lost
- required_environment_anchor_1: air_machine_cockpit
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: preserve readable body-to-environment scale in frame
- camera_package_description: medium, eye level, portrait lens, push in, zoom subtle in, shallow subject, low key night
- environment_subzone: air_machine_cockpit
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; desolate_martian_wasteland; DESC_CH023_SC004; DESC_CH023_SC004_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: environment reference for the scene location
- image2_asset: desolate martian wasteland

# Continuity Notes
- Scene: CH023_SC004 / SC004.
- Variant: Alternate Angle.
- Time of day progression over several hours
- Physical state of the damaged air machine
- Direction of travel relative to Helium
- Realization of being lost
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH023\CH023_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH023\CH023_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH023\CH023_SC004\SH003\DIALOGUE.json
