# Title
SH001 Shot Prompt - Consistency Repair

# ID
CH024_SC001_SH001_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the environment reference for battlefield plains. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. A downed aircraft crashes into a massive battlefield, leading to a rescue mission amidst heavy combat. The subject from image1 is john carter, midground inside crash site, Massive scale of Thark vs Warhoon battle contrasted with intimate combat skirmish, facing directly toward camera, sky view of aircraft. Preserve the environment from image2 Wide combat expanse near ancient city ruins, terrain is rugged and scarred., monumental scale, dry open Martian terrain, especially crash site. wide, high angle, ultra-wide lens, crane, environment priority, diffuse ambient. Dynamic composition in clear pursuit vectors and readable movement. aircraft plummeting toward the battlefield. crash site. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH024_SC001; SHOT_INDEX; DIALOGUE; john_carter; tars_tarkas; woola
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: ultra_wide
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
- scene_id: CH024_SC001
- chapter_id: CH024
- shot_type: action
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: Dynamic composition in battlefield_plains with clear pursuit vectors and readable movement for john_carter, Warhoon Warriors.
- shot_size: wide
- camera_angle: high_angle
- camera_motion: crane
- zoom_behavior: none
- focus_strategy: environment_priority
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: midground inside crash_site
- primary_subject_scale_relation: Massive scale of Thark vs Warhoon battle contrasted with intimate combat skirmish.
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: sky view of aircraft
- subject_relation_summary: john_carter carries the frame alone
- scene_short_description: A downed aircraft crashes into a massive battlefield, leading to a rescue mission amidst heavy combat.
- shot_moment_summary: aircraft plummeting toward the battlefield
- required_environment_anchor_1: crash_site
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: Massive scale of Thark vs Warhoon battle contrasted with intimate combat skirmish.
- camera_package_description: wide, high angle, ultra-wide lens, crane, environment priority, diffuse ambient
- environment_subzone: crash_site
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; battlefield_plains; DESC_CH024_SC001; DESC_CH024_SC001_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: environment reference for the scene location
- image2_asset: battlefield plains

# Continuity Notes
- Scene: CH024_SC001 / SC001.
- Variant: Consistency Repair.
- Aircraft debris location relative to crash site
- Blood and dirt accumulation levels on characters post-combat
- Woola's proximity/positioning relative to john_carter
- Aircraft crash into the battlefield
- Resolve Warhoon Warriors -> Warhoon Warriors
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH024\CH024_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH024\CH024_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH024\CH024_SC001\SH001\DIALOGUE.json
