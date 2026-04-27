# Title
SH003 Shot Prompt - Consistency Repair

# ID
CH009_SC001_SH003_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for sola. Use image2 as the environment reference for communal sleeping quarters. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. A menacing warrior presents oversized arms to a smaller man while women remodel the gear. The subject from image1 is sola, foreground right within communal sleeping quarters workshop, Martian equipment is significantly larger than the protagonist's Earthly frame, front three-quarter left toward the scene action, tools touching gear. Preserve the environment from image2 monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, broad processional paths and stairs, especially communal sleeping quarters workshop. Keep one readable subject anchor: group circle around work surface. medium, eye level, wide lens, track, shallow subject, soft even. Closing composition in that emphasizes the consequence of communal remodeling process. women working together to remodel gear. workshop. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH009_SC001; SHOT_INDEX; DIALOGUE; protagonist; sola
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
- scene_id: CH009_SC001
- chapter_id: CH009
- shot_type: closing_reaction
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Controlled closing frame that lands the consequence of the beat.
- composition: Closing composition in communal_sleeping_quarters that emphasizes the consequence of communal remodeling process.
- shot_size: medium
- camera_angle: eye_level
- camera_motion: track
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: soft_even
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_left
- visible_primary_subject_id: sola
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground right within communal_sleeping_quarters_workshop
- primary_subject_scale_relation: Martian equipment is significantly larger than the protagonist's Earthly frame.
- primary_subject_facing_direction: front three-quarter left toward the scene action
- primary_subject_pose_description: tools touching gear
- subject_relation_summary: sola carries the frame alone
- scene_short_description: A menacing warrior presents oversized arms to a smaller man while women remodel the gear.
- shot_moment_summary: women working together to remodel gear
- required_environment_anchor_1: communal_sleeping_quarters_workshop
- required_subject_anchor_1: group circle around work surface
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: Martian equipment is significantly larger than the protagonist's Earthly frame.
- camera_package_description: medium, eye level, wide lens, track, shallow subject, soft even
- environment_subzone: communal_sleeping_quarters_workshop
- prompt_family: shot_prompt
- reference_asset_ids: sola; communal_sleeping_quarters; DESC_CH009_SC001; DESC_CH009_SC001_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: sola
- image2_role: environment reference for the scene location
- image2_asset: communal sleeping quarters

# Continuity Notes
- Scene: CH009_SC001 / SC001.
- Variant: Consistency Repair.
- Fit and scale of remodeled armor vs protagonist frame
- Visual state of remodeling tools
- Communal remodeling process
- Resolve Other Female Martians -> Other Female Martians
- Resolve unnamed Martian warrior -> unnamed Martian warrior
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH009\CH009_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH009\CH009_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH009\CH009_SC001\SH003\DIALOGUE.json
