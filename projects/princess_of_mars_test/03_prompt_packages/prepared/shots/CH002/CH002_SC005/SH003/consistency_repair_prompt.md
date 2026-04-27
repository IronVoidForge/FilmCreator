# Title
SH003 Shot Prompt - Consistency Repair

# ID
CH002_SC005_SH003_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for protagonist. Use image2 as the environment reference for deep space void. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. A man flees a rocky gorge into the desert night before being pulled toward Mars. The subject from image1 is protagonist, foreground right within deep space void, Human scale vs. planetary scale, back to camera with head turned toward the action, gazing at Mars. Preserve the environment from image2 monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, broad processional paths and stairs, especially deep space void. Keep one readable subject anchor: back to camera with head turned toward the action. full, low angle, wide lens, crane, zoom strong in, rack focus, backlit. Closing composition in that emphasizes the consequence of whisked away into the void. protagonist is whisked into the void. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH002_SC005; SHOT_INDEX; DIALOGUE; protagonist
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
- scene_id: CH002_SC005
- chapter_id: CH002
- shot_type: closing_reaction
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Controlled closing frame that lands the consequence of the beat.
- composition: Closing composition in deep_space_void that emphasizes the consequence of whisked away into the void.
- shot_size: full
- camera_angle: low_angle
- camera_motion: crane
- zoom_behavior: strong_in
- focus_strategy: rack_focus
- lighting_style: backlit
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: back
- visible_primary_subject_id: protagonist
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground right within deep_space_void
- primary_subject_scale_relation: Human scale vs. planetary scale.
- primary_subject_facing_direction: back to camera with head turned toward the action
- primary_subject_pose_description: gazing at Mars
- subject_relation_summary: protagonist carries the frame alone
- scene_short_description: A man flees a rocky gorge into the desert night before being pulled toward Mars.
- shot_moment_summary: protagonist is whisked into the void
- required_environment_anchor_1: deep_space_void
- required_subject_anchor_1: back to camera with head turned toward the action
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: Human scale vs. planetary scale.
- camera_package_description: full, low angle, wide lens, crane, zoom strong in, rack focus, backlit
- environment_subzone: deep_space_void
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; deep_space_void; DESC_CH002_SC005; DESC_CH002_SC005_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: protagonist
- image2_role: environment reference for the scene location
- image2_asset: deep space void

# Continuity Notes
- Scene: CH002_SC005 / SC005.
- Variant: Consistency Repair.
- Fixed celestial position of Mars in the sky relative to horizon
- Visual texture/particle behavior of the transportation effect
- Whisked away into the void
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH002\CH002_SC005.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH002\CH002_SC005\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH002\CH002_SC005\SH003\DIALOGUE.json
