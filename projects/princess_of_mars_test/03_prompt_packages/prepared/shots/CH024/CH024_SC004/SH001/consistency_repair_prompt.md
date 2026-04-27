# Title
SH001 Shot Prompt - Consistency Repair

# ID
CH024_SC004_SH001_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for thark city complex. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. A leader proposes a massive raid leading to the mobilization of a vast Martian army. The subject from image1 is john carter, foreground entry line within thark city complex assembly zone, Individual proposal scales up to 150,000 marching soldiers, front three-quarter right toward the scene action, Carter speaking. The subject from image2 is john carter plays against tars tarkas in the same frame. Preserve the environment from image3 Massive scale with wide thoroughfares and high-ceilinged communal areas., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially thark city complex assembly zone. medium, eye level, normal lens, push in, zoom subtle in, shallow subject, diffuse ambient. Detail composition centered on the key physical action or prop inside. Carter proposes the raid on Zodanga. assembly zone. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH024_SC004; SHOT_INDEX; DIALOGUE; john_carter; tars_tarkas
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: normal
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
- scene_id: CH024_SC004
- chapter_id: CH024
- shot_type: insert_detail
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Tight detail framing focused on a single visual object or gesture.
- composition: Detail composition centered on the key physical action or prop inside thark_city_complex.
- shot_size: medium
- camera_angle: eye_level
- camera_motion: push_in
- zoom_behavior: subtle_in
- focus_strategy: shallow_subject
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: front_three_quarter_right
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: tars_tarkas
- primary_subject_frame_position: foreground entry line within thark_city_complex assembly zone
- primary_subject_scale_relation: Individual proposal scales up to 150,000 marching soldiers.
- primary_subject_facing_direction: front three-quarter right toward the scene action
- primary_subject_pose_description: Carter speaking
- subject_relation_summary: john_carter plays against tars_tarkas in the same frame
- scene_short_description: A leader proposes a massive raid leading to the mobilization of a vast Martian army.
- shot_moment_summary: Carter proposes the raid on Zodanga
- required_environment_anchor_1: thark_city_complex assembly zone
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: Individual proposal scales up to 150,000 marching soldiers.
- camera_package_description: medium, eye level, normal lens, push in, zoom subtle in, shallow subject, diffuse ambient
- environment_subzone: thark_city_complex assembly zone
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; tars_tarkas; thark_city_complex; DESC_CH024_SC004; DESC_CH024_SC004_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: identity reference for the secondary visible subject
- image2_asset: tars tarkas
- image3_role: environment reference for the scene location
- image3_asset: thark city complex

# Continuity Notes
- Scene: CH024_SC004 / SC004.
- Variant: Consistency Repair.
- Army size must visually represent 150,000 units
- Time of day transition from daylight to dusk/night
- Carter proposes the raid on Zodanga to rescue Dejah Thoris and seize wealth
- Resolve Thark Hordes -> Thark Hordes
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH024\CH024_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH024\CH024_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH024\CH024_SC004\SH001\DIALOGUE.json
