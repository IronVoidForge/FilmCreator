# Title
SH002 Shot Prompt - Consistency Repair

# ID
CH024_SC002_SH002_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for sarkoja. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for thark city complex. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. Two warriors intercept a priestess in a dim interior to force her departure. The subject from image1 is sarkoja, foreground inside thark city interior corridor, preserve readable body-to-environment scale in frame, facing directly toward camera, Sarkoja frozen. The subject from image2 is sarkoja plays against john carter in the same frame. Preserve the environment from image3 Massive scale with wide thoroughfares and high-ceilinged communal areas., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially thark city interior corridor. close-up, low angle, portrait lens, locked off, zoom subtle in, shallow subject, hard directional. Intimate composition that isolates, against to capture the beat's emotional turn. Close up of Sarkoja reacting to the threat. thark city interior corridor. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH024_SC002; SHOT_INDEX; DIALOGUE; john_carter; tars_tarkas; sarkoja
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
- scene_id: CH024_SC002
- chapter_id: CH024
- shot_type: reaction_closeup
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates sarkoja, john_carter against thark_city_complex to capture the beat's emotional turn.
- shot_size: close_up
- camera_angle: low_angle
- camera_motion: locked_off
- zoom_behavior: subtle_in
- focus_strategy: shallow_subject
- lighting_style: hard_directional
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: front
- visible_primary_subject_id: sarkoja
- visible_secondary_subject_ids: john_carter
- primary_subject_frame_position: foreground inside thark_city_interior_corridor
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: Sarkoja frozen
- subject_relation_summary: sarkoja plays against john_carter in the same frame
- scene_short_description: Two warriors intercept a priestess in a dim interior to force her departure.
- shot_moment_summary: Close up of Sarkoja reacting to the threat
- required_environment_anchor_1: thark_city_interior_corridor
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: preserve readable body-to-environment scale in frame
- camera_package_description: close-up, low angle, portrait lens, locked off, zoom subtle in, shallow subject, hard directional
- environment_subzone: thark_city_interior_corridor
- prompt_family: shot_prompt
- reference_asset_ids: sarkoja; john_carter; thark_city_complex; DESC_CH024_SC002; DESC_CH024_SC002_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: sarkoja
- image2_role: identity reference for the secondary visible subject
- image2_asset: john carter
- image3_role: environment reference for the scene location
- image3_asset: thark city complex

# Continuity Notes
- Scene: CH024_SC002 / SC002.
- Variant: Consistency Repair.
- Thark interior lighting levels
- Character positioning relative to the threat
- Intimidation of the priestess
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH024\CH024_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH024\CH024_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH024\CH024_SC002\SH002\DIALOGUE.json
