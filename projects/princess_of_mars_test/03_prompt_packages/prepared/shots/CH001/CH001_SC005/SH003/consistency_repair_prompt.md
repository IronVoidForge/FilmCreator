# Title
SH003 Shot Prompt - Consistency Repair

# ID
CH001_SC005_SH003_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the environment reference for ancient cliffside cave. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. A man leads a horse along a narrow cliffside trail toward an ancient cave entrance. The subject from image1 is john carter, foreground inside ancient cliffside cave, Chapter-local beat subzone match for 'ancient cliffside cave', front three-quarter left toward the scene action, feeling drowsiness. Preserve the environment from image2 Narrow trail leads to a large cave, located between steep cliffs and a deep ravine., monumental scale, dry open Martian terrain, especially ancient cliffside cave. close-up, eye level, portrait lens, push in, zoom subtle in, shallow subject, hard directional. Intimate composition that isolates against to capture the beat's emotional turn. Mysterious collapse. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH001_SC005; SHOT_INDEX; DIALOGUE; john_carter
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: portrait
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: consistency_repair
- review_notes: Prompt body is missing the required subject anchor for an on-screen shot.
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH001_SC005
- chapter_id: CH001
- shot_type: reaction_closeup
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates john_carter against ancient_cliffside_cave to capture the beat's emotional turn.
- shot_size: close_up
- camera_angle: eye_level
- camera_motion: push_in
- zoom_behavior: subtle_in
- focus_strategy: shallow_subject
- lighting_style: hard_directional
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_left
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground inside ancient_cliffside_cave
- primary_subject_scale_relation: Chapter-local beat subzone match for 'ancient_cliffside_cave'.
- primary_subject_facing_direction: front three-quarter left toward the scene action
- primary_subject_pose_description: feeling drowsiness
- subject_relation_summary: john_carter carries the frame alone
- scene_short_description: A man leads a horse along a narrow cliffside trail toward an ancient cave entrance.
- shot_moment_summary: Mysterious collapse
- required_environment_anchor_1: ancient_cliffside_cave
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: Chapter-local beat subzone match for 'ancient_cliffside_cave'.
- camera_package_description: close-up, eye level, portrait lens, push in, zoom subtle in, shallow subject, hard directional
- environment_subzone: ancient_cliffside_cave
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; ancient_cliffside_cave; DESC_CH001_SC005; DESC_CH001_SC005_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: environment reference for the scene location
- image2_asset: ancient cliffside cave

# Continuity Notes
- Scene: CH001_SC005 / SC005.
- Variant: Consistency Repair.
- Dimming light levels inside the cave
- Physical state of john_carter (dirt, blood, exhaustion)
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH001\CH001_SC005.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH001\CH001_SC005\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH001\CH001_SC005\SH003\DIALOGUE.json
