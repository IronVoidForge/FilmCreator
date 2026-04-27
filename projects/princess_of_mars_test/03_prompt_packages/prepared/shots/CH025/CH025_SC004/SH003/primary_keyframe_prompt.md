# Title
SH003 Shot Prompt - Primary Keyframe

# ID
CH025_SC004_SH003_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for kantos kan. Use image2 as the environment reference for zodanga palace dungeons. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. Warriors descend into dark subterranean cells to retrieve keys from a corpse and free a prisoner. The subject from image1 is kantos kan, foreground right within cell block, Narrow, claustrophobic dungeon corridors vs. the scale of heavy iron cell doors, facing directly toward camera, inserting key. Preserve the environment from image2 Cramped cells connected by narrow corridors, underground palace vault structure., monumental scale, dry open Martian terrain, especially cell block. insert-detail, eye level, portrait lens, locked off, rack focus, torch firelight. Detail composition centered on the key physical action or prop inside. unlocking the cell door. cell block. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH025_SC004; SHOT_INDEX; DIALOGUE; john_carter; kantos_kan
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
- scene_id: CH025_SC004
- chapter_id: CH025
- shot_type: insert_detail
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Tight detail framing focused on a single visual object or gesture.
- composition: Detail composition centered on the key physical action or prop inside zodanga_palace_dungeons.
- shot_size: insert_detail
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: none
- focus_strategy: rack_focus
- lighting_style: torch_firelight
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front
- visible_primary_subject_id: kantos_kan
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground right within cell_block
- primary_subject_scale_relation: Narrow, claustrophobic dungeon corridors vs. the scale of heavy iron cell doors.
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: inserting key
- subject_relation_summary: kantos_kan carries the frame alone
- scene_short_description: Warriors descend into dark subterranean cells to retrieve keys from a corpse and free a prisoner.
- shot_moment_summary: unlocking the cell door
- required_environment_anchor_1: cell_block
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: Narrow, claustrophobic dungeon corridors vs. the scale of heavy iron cell doors.
- camera_package_description: insert-detail, eye level, portrait lens, locked off, rack focus, torch firelight
- environment_subzone: cell_block
- prompt_family: shot_prompt
- reference_asset_ids: kantos_kan; zodanga_palace_dungeons; DESC_CH025_SC004; DESC_CH025_SC004_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: kantos kan
- image2_role: environment reference for the scene location
- image2_asset: zodanga palace dungeons

# Continuity Notes
- Scene: CH025_SC004 / SC004.
- Variant: Primary Keyframe.
- Torch/lighting source consistency
- Dirt/grime levels on characters post-battle
- Freeing Kantos Kan
- Resolve Thark Warriors -> Thark Warriors
- Resolve Fallen Jailer (corpse/background) -> Fallen Jailer (corpse/background)
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH025\CH025_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH025\CH025_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH025\CH025_SC004\SH003\DIALOGUE.json
