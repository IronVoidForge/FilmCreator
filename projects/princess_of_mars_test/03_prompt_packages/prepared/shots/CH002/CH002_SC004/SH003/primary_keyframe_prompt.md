# Title
SH003 Shot Prompt - Primary Keyframe

# ID
CH002_SC004_SH003_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for protagonist. Use image2 as the environment reference for arizona mountain cave. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. A naked figure stands in a cave, looking down at his own clothed, armed corpse. The subject from image1 is The Protagonist's Body (Lifeless shell), midground inside rocky floor zone, Vertical hierarchy between the standing spirit and the prone physical body, profile left toward the scene action, high angle looking down. Preserve the environment from image2 Subterranean cave structure., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially rocky floor zone. wide, high angle, ultra-wide lens, pan, deep focus, low key night. Wide composition across placed for immediate spatial orientation. camera reveals the dead body. rocky floor zone. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH002_SC004; SHOT_INDEX; DIALOGUE; protagonist
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: ultra_wide
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
- scene_id: CH002_SC004
- chapter_id: CH002
- shot_type: establishing_wide
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across arizona_mountain_cave with The Protagonist's Body (Lifeless shell), protagonist placed for immediate spatial orientation.
- shot_size: wide
- camera_angle: high_angle
- camera_motion: pan
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: low_key_night
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: profile_left
- visible_primary_subject_id: protagonist
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: midground inside rocky_floor_zone
- primary_subject_scale_relation: Vertical hierarchy between the standing spirit and the prone physical body.
- primary_subject_facing_direction: profile left toward the scene action
- primary_subject_pose_description: high angle looking down
- subject_relation_summary: The Protagonist's Body (Lifeless shell) carries the frame alone
- scene_short_description: A naked figure stands in a cave, looking down at his own clothed, armed corpse.
- shot_moment_summary: camera reveals the dead body
- required_environment_anchor_1: rocky_floor_zone
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: Vertical hierarchy between the standing spirit and the prone physical body.
- camera_package_description: wide, high angle, ultra-wide lens, pan, deep focus, low key night
- environment_subzone: rocky_floor_zone
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; arizona_mountain_cave; DESC_CH002_SC004; DESC_CH002_SC004_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: protagonist
- image2_role: environment reference for the scene location
- image2_asset: arizona mountain cave

# Continuity Notes
- Scene: CH002_SC004 / SC004.
- Variant: Primary Keyframe.
- Exact spatial distance between naked protagonist and clothed/armed dead body
- Clothing and weapon placement on The Protagonist's Body (Lifeless shell)
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH002\CH002_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH002\CH002_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH002\CH002_SC004\SH003\DIALOGUE.json
