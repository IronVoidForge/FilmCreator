# Title
SH002 Shot Prompt - Alternate Angle

# ID
CH024_SC004_SH002_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for tars tarkas. Use image2 as the environment reference for thark city complex. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. A leader proposes a massive raid leading to the mobilization of a vast Martian army. The subject from image1 is Thark Hordes, midground inside thark city complex assembly zone, Individual proposal scales up to 150,000 marching soldiers, facing directly toward camera, silence after proposal. Preserve the environment from image2 Massive scale with wide thoroughfares and high-ceilinged communal areas., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially thark city complex assembly zone. wide, low angle, wide lens, pan, deep focus, diffuse ambient. Detail composition centered on the key physical action or prop inside. The Thark hordes react with excitement. assembly zone. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH024_SC004; SHOT_INDEX; DIALOGUE; john_carter; tars_tarkas
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: wide
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: alternate_angle
- review_notes: Prompt body is missing the required subject anchor for an on-screen shot.
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH024_SC004
- chapter_id: CH024
- shot_type: insert_detail
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Tight detail framing focused on a single visual object or gesture.
- composition: Detail composition centered on the key physical action or prop inside thark_city_complex.
- shot_size: wide
- camera_angle: low_angle
- camera_motion: pan
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: front
- visible_primary_subject_id: tars_tarkas
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: midground inside thark_city_complex assembly zone
- primary_subject_scale_relation: Individual proposal scales up to 150,000 marching soldiers.
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: silence after proposal
- subject_relation_summary: Thark Hordes carries the frame alone
- scene_short_description: A leader proposes a massive raid leading to the mobilization of a vast Martian army.
- shot_moment_summary: The Thark hordes react with excitement
- required_environment_anchor_1: thark_city_complex assembly zone
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: Individual proposal scales up to 150,000 marching soldiers.
- camera_package_description: wide, low angle, wide lens, pan, deep focus, diffuse ambient
- environment_subzone: thark_city_complex assembly zone
- prompt_family: shot_prompt
- reference_asset_ids: tars_tarkas; thark_city_complex; DESC_CH024_SC004; DESC_CH024_SC004_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: tars tarkas
- image2_role: environment reference for the scene location
- image2_asset: thark city complex

# Continuity Notes
- Scene: CH024_SC004 / SC004.
- Variant: Alternate Angle.
- Army size must visually represent 150,000 units
- Time of day transition from daylight to dusk/night
- The Thark hordes enthusiastically agree to the plan
- Resolve Thark Hordes -> Thark Hordes
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH024\CH024_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH024\CH024_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH024\CH024_SC004\SH002\DIALOGUE.json
