# Title
SH001 Shot Prompt - Primary Keyframe

# ID
CH006_SC004_SH001_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for martian warriors. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for martian interior chamber. Use image4 as the identity reference for an additional visible subject. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. A group of warriors applauds a fighter before attempting to execute a wounded beast. The subject from image1 is martian warriors, midground inside plaza edge overlook, group size vs chamber width, front three-quarter left toward the scene action, warriors entering frame. The subject from image2 is martian warriors plays against tars tarkas, sola in the same frame. Preserve the environment from image3 monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, broad processional paths and stairs, especially plaza edge overlook. wide, eye level, wide lens, pan, deep focus, diffuse ambient. Wide composition across placed for immediate spatial orientation. martian warriors enter applauding prowess. plaza edge overlook. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH006_SC004; SHOT_INDEX; DIALOGUE; protagonist; tars_tarkas; sola; martian_warriors; watch_thing
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: wide
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
- scene_id: CH006_SC004
- chapter_id: CH006
- shot_type: establishing_wide
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across martian_interior_chamber with martian_warriors, tars_tarkas, sola placed for immediate spatial orientation.
- shot_size: wide
- camera_angle: eye_level
- camera_motion: pan
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: front_three_quarter_left
- visible_primary_subject_id: martian_warriors
- visible_secondary_subject_ids: tars_tarkas; sola
- primary_subject_frame_position: midground inside plaza_edge_overlook
- primary_subject_scale_relation: group size vs chamber width
- primary_subject_facing_direction: front three-quarter left toward the scene action
- primary_subject_pose_description: warriors entering frame
- subject_relation_summary: martian_warriors plays against tars_tarkas, sola in the same frame
- scene_short_description: A group of warriors applauds a fighter before attempting to execute a wounded beast.
- shot_moment_summary: martian_warriors enter applauding prowess
- required_environment_anchor_1: plaza_edge_overlook
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: group size vs chamber width
- camera_package_description: wide, eye level, wide lens, pan, deep focus, diffuse ambient
- environment_subzone: plaza_edge_overlook
- prompt_family: shot_prompt
- reference_asset_ids: martian_warriors; tars_tarkas; sola; martian_interior_chamber; DESC_CH006_SC004; DESC_CH006_SC004_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: martian warriors
- image2_role: identity reference for the secondary visible subject
- image2_asset: tars tarkas
- image3_role: environment reference for the scene location
- image3_asset: martian interior chamber
- image4_role: identity reference for an additional visible subject
- image4_asset: sola

# Continuity Notes
- Scene: CH006_SC004 / SC004.
- Variant: Primary Keyframe.
- Weapon positions/readiness of martian_warriors
- Visible wound locations on watch_thing
- Protagonist physical state (nakedness vs clothing)
- Arrival and applause
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH006\CH006_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH006\CH006_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH006\CH006_SC004\SH001\DIALOGUE.json
