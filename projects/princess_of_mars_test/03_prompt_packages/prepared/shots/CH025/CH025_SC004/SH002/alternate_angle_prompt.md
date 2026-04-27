# Title
SH002 Shot Prompt - Alternate Angle

# ID
CH025_SC004_SH002_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the environment reference for zodanga palace dungeons. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. Warriors descend into dark subterranean cells to retrieve keys from a corpse and free a prisoner. The subject from image1 is Fallen Jailer (corpse/background), foreground inside dungeon corridors, hand size vs key ring, profile left toward the scene action, approaching corpse. Preserve the environment from image2 Cramped cells connected by narrow corridors, underground palace vault structure., monumental scale, dry open Martian terrain, especially dungeon corridors. close-up, eye level, normal lens, locked off, shallow subject, torch firelight. Detail composition centered on the key physical action or prop inside. finding keys on corpse. dungeon corridors. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH025_SC004; SHOT_INDEX; DIALOGUE; john_carter; kantos_kan
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: normal
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
- scene_id: CH025_SC004
- chapter_id: CH025
- shot_type: insert_detail
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Tight detail framing focused on a single visual object or gesture.
- composition: Detail composition centered on the key physical action or prop inside zodanga_palace_dungeons.
- shot_size: close_up
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: torch_firelight
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: profile_left
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground inside dungeon_corridors
- primary_subject_scale_relation: hand size vs key ring
- primary_subject_facing_direction: profile left toward the scene action
- primary_subject_pose_description: approaching corpse
- subject_relation_summary: Fallen Jailer (corpse/background) carries the frame alone
- scene_short_description: Warriors descend into dark subterranean cells to retrieve keys from a corpse and free a prisoner.
- shot_moment_summary: finding keys on corpse
- required_environment_anchor_1: dungeon_corridors
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: hand size vs key ring
- camera_package_description: close-up, eye level, normal lens, locked off, shallow subject, torch firelight
- environment_subzone: dungeon_corridors
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; zodanga_palace_dungeons; DESC_CH025_SC004; DESC_CH025_SC004_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: environment reference for the scene location
- image2_asset: zodanga palace dungeons

# Continuity Notes
- Scene: CH025_SC004 / SC004.
- Variant: Alternate Angle.
- Torch/lighting source consistency
- Dirt/grime levels on characters post-battle
- Locating the keys
- Resolve Thark Warriors -> Thark Warriors
- Resolve Fallen Jailer (corpse/background) -> Fallen Jailer (corpse/background)
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH025\CH025_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH025\CH025_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH025\CH025_SC004\SH002\DIALOGUE.json
