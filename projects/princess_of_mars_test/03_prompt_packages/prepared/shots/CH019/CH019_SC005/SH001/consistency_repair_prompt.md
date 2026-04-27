# Title
SH001 Shot Prompt - Consistency Repair

# ID
CH019_SC005_SH001_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for kantos kan. Use image2 as the environment reference for warhoon eastern hills. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. A man slips through dark shadows toward distant hills while a figure claims freedom in the background. The subject from image1 is kantos kan, midground inside Arena perimeter, distance between kan and carter, back to camera with head turned toward the action, distant silhouette in torchlight. Preserve the environment from image2 Functions as an escape route or transit corridor., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially Arena perimeter. Keep one readable subject anchor: distant silhouette in torchlight. wide, low angle, wide lens, pan, deep focus, torch firelight. Wide composition across placed for immediate spatial orientation. kantos kan claims freedom amidst arena chaos. Arena perimeter. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH019_SC005; SHOT_INDEX; DIALOGUE; john_carter; kantos_kan
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: wide
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: consistency_repair
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH019_SC005
- chapter_id: CH019
- shot_type: establishing_wide
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across warhoon_eastern_hills with kantos_kan placed for immediate spatial orientation.
- shot_size: wide
- camera_angle: low_angle
- camera_motion: pan
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: torch_firelight
- subject_visibility: silhouette
- narration_mode: none
- primary_subject_angle: back
- visible_primary_subject_id: kantos_kan
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: midground inside Arena perimeter
- primary_subject_scale_relation: distance between kan and carter
- primary_subject_facing_direction: back to camera with head turned toward the action
- primary_subject_pose_description: distant silhouette in torchlight
- subject_relation_summary: kantos_kan carries the frame alone
- scene_short_description: A man slips through dark shadows toward distant hills while a figure claims freedom in the background.
- shot_moment_summary: kantos_kan claims freedom amidst arena chaos
- required_environment_anchor_1: Arena perimeter
- required_subject_anchor_1: distant silhouette in torchlight
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: distance between kan and carter
- camera_package_description: wide, low angle, wide lens, pan, deep focus, torch firelight
- environment_subzone: Arena perimeter
- prompt_family: shot_prompt
- reference_asset_ids: kantos_kan; warhoon_eastern_hills; DESC_CH019_SC005; DESC_CH019_SC005_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: kantos kan
- image2_role: environment reference for the scene location
- image2_asset: warhoon eastern hills

# Continuity Notes
- Scene: CH019_SC005 / SC005.
- Variant: Consistency Repair.
- Lighting consistency between moonlight and torchlight sources
- Physical condition of john_carter (injuries from previous scenes)
- Kantos Kan claims freedom in the distance
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH019\CH019_SC005.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH019\CH019_SC005\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH019\CH019_SC005\SH001\DIALOGUE.json
