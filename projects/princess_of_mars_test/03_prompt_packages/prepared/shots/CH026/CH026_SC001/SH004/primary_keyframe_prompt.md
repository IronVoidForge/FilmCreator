# Title
SH004 Shot Prompt - Primary Keyframe

# ID
CH026_SC001_SH004_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for tars tarkas. Use image2 as the environment reference for aerial battle skies. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. Massive aerial fleets clash in the Martian skies before a ritualistic surrender. The subject from image1 is Zodangan Commanders, foreground inside aerial battle skies command decks, Fleet vs. Fleet scale hierarchy, front three-quarter left toward the scene action, Zodangan command vessels lose combat footing. Preserve the environment from image2 High-altitude, expansive vertical combat space., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially aerial battle skies command decks. close-up, eye level, portrait lens, push in, zoom subtle in, shallow subject, hard directional. Intimate composition that isolates, against to capture the beat's emotional turn. Ritualistic surrender/suicide. command decks. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH004
- source_artifact_ids: CH026_SC001; SHOT_INDEX; DIALOGUE; john_carter; tars_tarkas; kantos_kan
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: portrait
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
- scene_id: CH026_SC001
- chapter_id: CH026
- shot_type: reaction_closeup
- previous_shot_id: SH003
- next_shot_id: (none)
- shot_lineage_ids: SH003; SH004
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates Zodangan Commanders, tars_tarkas against aerial_battle_skies to capture the beat's emotional turn.
- shot_size: close_up
- camera_angle: eye_level
- camera_motion: push_in
- zoom_behavior: subtle_in
- focus_strategy: shallow_subject
- lighting_style: hard_directional
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_left
- visible_primary_subject_id: tars_tarkas
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground inside aerial_battle_skies_command_decks
- primary_subject_scale_relation: Fleet vs. Fleet scale hierarchy.
- primary_subject_facing_direction: front three-quarter left toward the scene action
- primary_subject_pose_description: Zodangan command vessels lose combat footing
- subject_relation_summary: Zodangan Commanders carries the frame alone
- scene_short_description: Massive aerial fleets clash in the Martian skies before a ritualistic surrender.
- shot_moment_summary: Ritualistic surrender/suicide
- required_environment_anchor_1: aerial_battle_skies_command_decks
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: Fleet vs. Fleet scale hierarchy.
- camera_package_description: close-up, eye level, portrait lens, push in, zoom subtle in, shallow subject, hard directional
- environment_subzone: aerial_battle_skies_command_decks
- prompt_family: shot_prompt
- reference_asset_ids: tars_tarkas; aerial_battle_skies; DESC_CH026_SC001; DESC_CH026_SC001_SH004
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: tars tarkas
- image2_role: environment reference for the scene location
- image2_asset: aerial battle skies

# Continuity Notes
- Scene: CH026_SC001 / SC001.
- Variant: Primary Keyframe.
- Vessel positions in the sky relative to fleet formation
- Total count of remaining ships during melee
- Direction of flight paths during combat maneuvers
- Ritualistic surrender/suicide
- Resolve Zodangan Commanders -> Zodangan Commanders
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH026\CH026_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH026\CH026_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH026\CH026_SC001\SH004\DIALOGUE.json
