# Title
SH002 Shot Prompt - Alternate Angle

# ID
CH014_SC004_SH002_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for sarkoja. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for duel arena open plains. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. A high-intensity sword duel under bright sunlight interrupted by a blinding light reflection. The subject from image1 is sarkoja, foreground inside duel arena open plains, handheld mirror size, profile left toward the scene action, sarkoja watching duel. The subject from image2 is sarkoja plays against john carter in the same frame. Preserve the environment from image3 A wide combat clearing providing sufficient space for chariot maneuvering and formal dueling., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially duel arena open plains. close-up, eye level, portrait lens, locked off, shallow subject, hard directional. Intimate composition that isolates, against to capture the beat's emotional turn. Sarkoja tilts the mirror. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH014_SC004; SHOT_INDEX; DIALOGUE; john_carter; zad; sarkoja
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: portrait
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
- scene_id: CH014_SC004
- chapter_id: CH014
- shot_type: reaction_closeup
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates sarkoja, john_carter against duel_arena_open_plains to capture the beat's emotional turn.
- shot_size: close_up
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: hard_directional
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: profile_left
- visible_primary_subject_id: sarkoja
- visible_secondary_subject_ids: john_carter
- primary_subject_frame_position: foreground inside duel_arena_open_plains
- primary_subject_scale_relation: handheld mirror size
- primary_subject_facing_direction: profile left toward the scene action
- primary_subject_pose_description: sarkoja watching duel
- subject_relation_summary: sarkoja plays against john_carter in the same frame
- scene_short_description: A high-intensity sword duel under bright sunlight interrupted by a blinding light reflection.
- shot_moment_summary: Sarkoja tilts the mirror
- required_environment_anchor_1: duel_arena_open_plains
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: handheld mirror size
- camera_package_description: close-up, eye level, portrait lens, locked off, shallow subject, hard directional
- environment_subzone: duel_arena_open_plains
- prompt_family: shot_prompt
- reference_asset_ids: sarkoja; john_carter; duel_arena_open_plains; DESC_CH014_SC004; DESC_CH014_SC004_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: sarkoja
- image2_role: identity reference for the secondary visible subject
- image2_asset: john carter
- image3_role: environment reference for the scene location
- image3_asset: duel arena open plains

# Continuity Notes
- Scene: CH014_SC004 / SC004.
- Variant: Alternate Angle.
- Sun angle relative to camera and actors
- Mirror position and reflection trajectory
- Sword positions during the strike
- Sarkoja prepares the betrayal
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH014\CH014_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH014\CH014_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH014\CH014_SC004\SH002\DIALOGUE.json
