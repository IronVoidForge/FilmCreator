# Title
SH001 Shot Prompt - Primary Keyframe

# ID
CH012_SC004_SH001_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the environment reference for carters quarters building. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. A third-floor room fills with spoils of war and servants as a commander establishes his base. The subject from image1 is central court, midground inside carters quarters building, height of third floor relative to ground, facing directly toward camera, static view of courtyard. Preserve the environment from image2 Multi-story verticality centered around a recurring courtyard with fountains and statues., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially carters quarters building. wide, high angle, wide lens, tilt, deep focus, diffuse ambient. Wide composition across placed for immediate spatial orientation. Wide view of the overgrown central court and fountains below the window. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH012_SC004; SHOT_INDEX; DIALOGUE; john_carter
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
- scene_id: CH012_SC004
- chapter_id: CH012
- shot_type: establishing_wide
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across carters_quarters_building with john_carter placed for immediate spatial orientation.
- shot_size: wide
- camera_angle: high_angle
- camera_motion: tilt
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: midground inside carters_quarters_building
- primary_subject_scale_relation: height of third floor relative to ground
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: static view of courtyard
- subject_relation_summary: central court carries the frame alone
- scene_short_description: A third-floor room fills with spoils of war and servants as a commander establishes his base.
- shot_moment_summary: Wide view of the overgrown central court and fountains below the window
- required_environment_anchor_1: carters_quarters_building
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: height of third floor relative to ground
- camera_package_description: wide, high angle, wide lens, tilt, deep focus, diffuse ambient
- environment_subzone: carters_quarters_building
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; carters_quarters_building; DESC_CH012_SC004; DESC_CH012_SC004_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: environment reference for the scene location
- image2_asset: carters quarters building

# Continuity Notes
- Scene: CH012_SC004 / SC004.
- Variant: Primary Keyframe.
- Incremental accumulation of physical items (weapons, silks, furs, food) in the room
- Specific inventory count of goods being moved
- Changing density of Tharkian retainues within the quarters
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH012\CH012_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH012\CH012_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH012\CH012_SC004\SH001\DIALOGUE.json
