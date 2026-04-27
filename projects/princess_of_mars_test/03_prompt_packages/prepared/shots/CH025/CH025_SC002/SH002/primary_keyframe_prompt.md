# Title
SH002 Shot Prompt - Primary Keyframe

# ID
CH025_SC002_SH002_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the environment reference for audience chamber. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. A formal ceremony is violently interrupted by a man smashing through a window and leaping into the hall. The subject from image1 is john carter, midground inside window perimeter, shattering glass vs room size, profile left toward the scene action, glass integrity. Preserve the environment from image2 monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, broad processional paths and stairs, especially window perimeter. wide, low angle, ultra-wide lens, pan, deep focus, backlit. Wide composition across placed for immediate spatial orientation. window smashing in slow motion. window perimeter. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH025_SC002; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris; sab_than; than_kosis
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
- scene_id: CH025_SC002
- chapter_id: CH025
- shot_type: establishing_wide
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across audience_chamber with john_carter, Zodangan Nobility/Guards placed for immediate spatial orientation.
- shot_size: wide
- camera_angle: low_angle
- camera_motion: pan
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: backlit
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: profile_left
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: midground inside window_perimeter
- primary_subject_scale_relation: shattering glass vs room size
- primary_subject_facing_direction: profile left toward the scene action
- primary_subject_pose_description: glass integrity
- subject_relation_summary: john_carter carries the frame alone
- scene_short_description: A formal ceremony is violently interrupted by a man smashing through a window and leaping into the hall.
- shot_moment_summary: window smashing in slow motion
- required_environment_anchor_1: window_perimeter
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: shattering glass vs room size
- camera_package_description: wide, low angle, ultra-wide lens, pan, deep focus, backlit
- environment_subzone: window_perimeter
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; audience_chamber; DESC_CH025_SC002; DESC_CH025_SC002_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: environment reference for the scene location
- image2_asset: audience chamber

# Continuity Notes
- Scene: CH025_SC002 / SC002.
- Variant: Primary Keyframe.
- Broken state of golden chains
- Scattered glass shards on floor
- Dejah Thoris ceremonial attire integrity
- Window smash intrusion
- Resolve Zodangan Nobility/Guards -> Zodangan Nobility/Guards
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH025\CH025_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH025\CH025_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH025\CH025_SC002\SH002\DIALOGUE.json
