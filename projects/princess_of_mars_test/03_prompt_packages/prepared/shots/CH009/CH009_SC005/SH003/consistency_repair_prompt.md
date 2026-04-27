# Title
SH003 Shot Prompt - Consistency Repair

# ID
CH009_SC005_SH003_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for protagonist. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for communal sleeping quarters. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. A group of Martian women argue intensely around a central point regarding a captive. The subject from image1 is protagonist, foreground inside communal sleeping quarters periphery, observer distance, profile left toward the scene action, sola falls silent. The subject from image2 is protagonist plays against sola in the same frame. Preserve the environment from image3 monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, broad processional paths and stairs, especially communal sleeping quarters periphery. medium-close, eye level, normal lens, locked off, rack focus, low key night. Intimate composition that ites, against to capture the beat's emotional turn. protagonist watches sola. periphery. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH009_SC005; SHOT_INDEX; DIALOGUE; sola; sarkoja; protagonist
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
- scene_id: CH009_SC005
- chapter_id: CH009
- shot_type: reaction_closeup
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Close framing that ites reaction and emotional emphasis.
- composition: Intimate composition that isolates protagonist, sola against communal_sleeping_quarters to capture the beat's emotional turn.
- shot_size: medium_close
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: none
- focus_strategy: rack_focus
- lighting_style: low_key_night
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: profile_left
- visible_primary_subject_id: protagonist
- visible_secondary_subject_ids: sola
- primary_subject_frame_position: foreground inside communal_sleeping_quarters_periphery
- primary_subject_scale_relation: observer distance
- primary_subject_facing_direction: profile left toward the scene action
- primary_subject_pose_description: sola falls silent
- subject_relation_summary: protagonist plays against sola in the same frame
- scene_short_description: A group of Martian women argue intensely around a central point regarding a captive.
- shot_moment_summary: protagonist watches sola
- required_environment_anchor_1: communal_sleeping_quarters_periphery
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: observer distance
- camera_package_description: medium-close, eye level, normal lens, locked off, rack focus, low key night
- environment_subzone: communal_sleeping_quarters_periphery
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; sola; communal_sleeping_quarters; DESC_CH009_SC005; DESC_CH009_SC005_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: protagonist
- image2_role: identity reference for the secondary visible subject
- image2_asset: sola
- image3_role: environment reference for the scene location
- image3_asset: communal sleeping quarters

# Continuity Notes
- Scene: CH009_SC005 / SC005.
- Variant: Consistency Repair.
- Emotional intensity levels must scale from heated to somber
- Character placement within the circular group formation
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH009\CH009_SC005.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH009\CH009_SC005\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH009\CH009_SC005\SH003\DIALOGUE.json
