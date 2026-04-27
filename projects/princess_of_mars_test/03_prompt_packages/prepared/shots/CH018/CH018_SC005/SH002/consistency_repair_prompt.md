# Title
SH002 Shot Prompt - Consistency Repair

# ID
CH018_SC005_SH002_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for protagonist. Use image2 as the environment reference for warhoon subterranean dungeon. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. A naked man ambushes a deliverer with a heavy chain in a pitch-black dungeon. The subject from image1 is protagonist, foreground right within subterranean dungeon floor, preserve readable body-to-environment scale in frame, front three-quarter right toward the scene action, chain swing begins. Preserve the environment from image2 Underground prison structure, specific spatial dimensions are unstated., monumental scale, dry open Martian terrain, especially subterranean dungeon floor. medium, eye level, wide lens, handheld, deep focus, high contrast ceremonial. Dynamic composition in clear pursuit vectors and readable movement. ambush with chain. subterranean dungeon floor. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH018_SC005; SHOT_INDEX; DIALOGUE; protagonist
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: wide
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
- scene_id: CH018_SC005
- chapter_id: CH018
- shot_type: action
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: Dynamic composition in warhoon_subterranean_dungeon with clear pursuit vectors and readable movement for protagonist, Jailer (deceased).
- shot_size: medium
- camera_angle: eye_level
- camera_motion: handheld
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_right
- visible_primary_subject_id: protagonist
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground right within subterranean_dungeon_floor
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: front three-quarter right toward the scene action
- primary_subject_pose_description: chain swing begins
- subject_relation_summary: protagonist carries the frame alone
- scene_short_description: A naked man ambushes a deliverer with a heavy chain in a pitch-black dungeon.
- shot_moment_summary: ambush with chain
- required_environment_anchor_1: subterranean_dungeon_floor
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: preserve readable body-to-environment scale in frame
- camera_package_description: medium, eye level, wide lens, handheld, deep focus, high contrast ceremonial
- environment_subzone: subterranean_dungeon_floor
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; warhoon_subterranean_dungeon; DESC_CH018_SC005; DESC_CH018_SC005_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: protagonist
- image2_role: environment reference for the scene location
- image2_asset: warhoon subterranean dungeon

# Continuity Notes
- Scene: CH018_SC005 / SC005.
- Variant: Consistency Repair.
- Heavy chain weapon state and handling
- Precise positioning of jailer's keys after kill
- Timing of glowing eyes relative to protagonist movement
- Violent ambush and killing
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH018\CH018_SC005.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH018\CH018_SC005\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH018\CH018_SC005\SH002\DIALOGUE.json
