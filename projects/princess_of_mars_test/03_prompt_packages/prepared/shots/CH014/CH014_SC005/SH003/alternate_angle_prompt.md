# Title
SH003 Shot Prompt - Alternate Angle

# ID
CH014_SC005_SH003_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for duel arena open plains. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. A chaotic duel in the open plains erupts into sudden violence leaving two characters wounded. The subject from image1 is john carter, foreground inside duel arena open plains center, preserve readable body-to-environment scale in frame, facing directly toward camera, Carter distracted by Sola's injury. The subject from image2 is john carter plays against Zad in the same frame. Preserve the environment from image3 A wide combat clearing providing sufficient space for chariot maneuvering and formal dueling., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially duel arena open plains center. Keep one readable subject anchor: ground surface. close-up, low angle, portrait lens, handheld, zoom subtle in, shallow subject, diffuse ambient. Intimate composition that isolates, against to capture the beat's emotional turn. Zad delivers fatal thrust to Carter. center. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH014_SC005; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris; sola; sarkoja; zad
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: portrait
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: alternate_angle
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH014_SC005
- chapter_id: CH014
- shot_type: reaction_closeup
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates john_carter, Zad against duel_arena_open_plains to capture the beat's emotional turn.
- shot_size: close_up
- camera_angle: low_angle
- camera_motion: handheld
- zoom_behavior: subtle_in
- focus_strategy: shallow_subject
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: zad
- primary_subject_frame_position: foreground inside duel_arena_open_plains center
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: Carter distracted by Sola's injury
- subject_relation_summary: john_carter plays against Zad in the same frame
- scene_short_description: A chaotic duel in the open plains erupts into sudden violence leaving two characters wounded.
- shot_moment_summary: Zad delivers fatal thrust to Carter
- required_environment_anchor_1: duel_arena_open_plains center
- required_subject_anchor_1: ground surface
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: preserve readable body-to-environment scale in frame
- camera_package_description: close-up, low angle, portrait lens, handheld, zoom subtle in, shallow subject, diffuse ambient
- environment_subzone: duel_arena_open_plains center
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; zad; duel_arena_open_plains; DESC_CH014_SC005; DESC_CH014_SC005_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: identity reference for the secondary visible subject
- image2_asset: zad
- image3_role: environment reference for the scene location
- image3_asset: duel arena open plains

# Continuity Notes
- Scene: CH014_SC005 / SC005.
- Variant: Alternate Angle.
- Blood splatter and wound locations on Sola and Carter
- Character positions during the melee transition
- Lighting shifts if sun position changes significantly
- Carter's fatal wound and aftermath
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH014\CH014_SC005.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH014\CH014_SC005\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH014\CH014_SC005\SH003\DIALOGUE.json
