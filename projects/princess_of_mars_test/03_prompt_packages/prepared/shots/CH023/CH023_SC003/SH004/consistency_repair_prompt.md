# Title
SH004 Shot Prompt - Consistency Repair

# ID
CH023_SC003_SH004_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the environment reference for martian sky aerial corridors. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. High-speed aerial chase through Martian sky involving interception and mechanical failure. The subject from image1 is john carter, foreground right within martian sky aerial corridors, Individual flight craft vs. Zodangan air patrol fleet scale, rear three-quarter left away from camera, high speed flight. Preserve the environment from image2 Vast, open expanses defined by aerial transit paths., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially martian sky aerial corridors. medium-full, dutch, wide lens, handheld, rack focus, high contrast ceremonial. Dynamic composition in clear pursuit vectors and readable movement. Projectile from cruiser strikes Carter's machine. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH004
- source_artifact_ids: CH023_SC003; SHOT_INDEX; DIALOGUE; john_carter; kantos_kan
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
- scene_id: CH023_SC003
- chapter_id: CH023
- shot_type: action
- previous_shot_id: SH003
- next_shot_id: (none)
- shot_lineage_ids: SH003; SH004
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: Dynamic composition in martian_sky_aerial_corridors with clear pursuit vectors and readable movement for john_carter, Zodangan Air Patrols.
- shot_size: medium_full
- camera_angle: dutch
- camera_motion: handheld
- zoom_behavior: none
- focus_strategy: rack_focus
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: rear_three_quarter_left
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground right within martian_sky_aerial_corridors
- primary_subject_scale_relation: Individual flight craft vs. Zodangan air patrol fleet scale.
- primary_subject_facing_direction: rear three-quarter left away from camera
- primary_subject_pose_description: high speed flight
- subject_relation_summary: john_carter carries the frame alone
- scene_short_description: High-speed aerial chase through Martian sky involving interception and mechanical failure.
- shot_moment_summary: Projectile from cruiser strikes Carter's machine
- required_environment_anchor_1: martian_sky_aerial_corridors
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: Individual flight craft vs. Zodangan air patrol fleet scale.
- camera_package_description: medium-full, dutch, wide lens, handheld, rack focus, high contrast ceremonial
- environment_subzone: martian_sky_aerial_corridors
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; martian_sky_aerial_corridors; DESC_CH023_SC003; DESC_CH023_SC003_SH004
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: environment reference for the scene location
- image2_asset: martian sky aerial corridors

# Continuity Notes
- Scene: CH023_SC003 / SC003.
- Variant: Consistency Repair.
- Flight paths of machines must maintain relative velocity
- Directional vector of projectile fire from cruiser to Carter
- Heliumite gearing speed increase vs. baseline machine speed
- Projectile strike and machine failure
- Resolve Zodangan Air Patrols -> Zodangan Air Patrols
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH023\CH023_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH023\CH023_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH023\CH023_SC003\SH004\DIALOGUE.json
