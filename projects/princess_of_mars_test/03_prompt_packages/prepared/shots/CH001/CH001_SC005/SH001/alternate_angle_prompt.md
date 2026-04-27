# Title
SH001 Shot Prompt - Alternate Angle

# ID
CH001_SC005_SH001_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the environment reference for ancient cliffside cave. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. A man leads a horse along a narrow cliffside trail toward an ancient cave entrance. The subject from image1 is john carter, midground inside A narrow trail between a cliff and a ravine, cliff vs ravine depth, profile right toward the scene action, wide view of landscape. Preserve the environment from image2 Narrow trail leads to a large cave, located between steep cliffs and a deep ravine., monumental scale, dry open Martian terrain. Keep one readable subject anchor: A narrow trail between a cliff and a ravine. wide, eye level, wide lens, track, deep focus, hard directional. Wide composition across placed for immediate spatial orientation. horse and rider moving along the cliff edge. A narrow trail between a cliff and a ravine. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH001_SC005; SHOT_INDEX; DIALOGUE; john_carter
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: wide
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: alternate_angle
- review_notes: Environment reference conflict: prompt variables align more with `none` than bound `ancient_cliffside_cave`.; SH001: environment anchor is typed like a subject/celestial detail instead of a set anchor.
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH001_SC005
- chapter_id: CH001
- shot_type: establishing_wide
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across ancient_cliffside_cave with john_carter placed for immediate spatial orientation.
- shot_size: wide
- camera_angle: eye_level
- camera_motion: track
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: hard_directional
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: profile_right
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: midground inside A narrow trail between a cliff and a ravine
- primary_subject_scale_relation: cliff vs ravine depth
- primary_subject_facing_direction: profile right toward the scene action
- primary_subject_pose_description: wide view of landscape
- subject_relation_summary: john_carter carries the frame alone
- scene_short_description: A man leads a horse along a narrow cliffside trail toward an ancient cave entrance.
- shot_moment_summary: horse and rider moving along the cliff edge
- required_environment_anchor_1: A narrow trail between a cliff and a ravine
- required_subject_anchor_1: A narrow trail between a cliff and a ravine
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: cliff vs ravine depth
- camera_package_description: wide, eye level, wide lens, track, deep focus, hard directional
- environment_subzone: A narrow trail between a cliff and a ravine
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; ancient_cliffside_cave; DESC_CH001_SC005; DESC_CH001_SC005_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: environment reference for the scene location
- image2_asset: ancient cliffside cave

# Continuity Notes
- Scene: CH001_SC005 / SC005.
- Variant: Alternate Angle.
- Dimming light levels inside the cave
- Physical state of john_carter (dirt, blood, exhaustion)
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH001\CH001_SC005.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH001\CH001_SC005\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH001\CH001_SC005\SH001\DIALOGUE.json
