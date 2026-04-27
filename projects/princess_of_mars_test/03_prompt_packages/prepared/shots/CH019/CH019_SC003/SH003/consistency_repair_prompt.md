# Title
SH003 Shot Prompt - Consistency Repair

# ID
CH019_SC003_SH003_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for subterranean amphitheater arena. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. Prisoners enter a massive subterranean amphitheater for a ten-day gladiatorial tournament. The subject from image1 is various beasts, foreground right within arena floor, size of beast vs Carter, profile left toward the scene action, beast charge. The subject from image2 is various beasts plays against warhoon horde in the same frame. Preserve the environment from image3 monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, broad processional paths and stairs, especially arena floor. full, eye level, wide lens, track, rack focus, high contrast ceremonial. Dynamic composition in clear pursuit vectors and readable movement. Carter fights a beast. arena floor. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH019_SC003; SHOT_INDEX; DIALOGUE; john_carter; kantos_kan; warhoon_horde
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: wide
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
- scene_id: CH019_SC003
- chapter_id: CH019
- shot_type: action
- previous_shot_id: SH002
- next_shot_id: SH004
- shot_lineage_ids: SH002; SH003; SH004
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: Dynamic composition in subterranean_amphitheater_arena with clear pursuit vectors and readable movement for * Various Beasts, john_carter, warhoon_horde.
- shot_size: full
- camera_angle: eye_level
- camera_motion: track
- zoom_behavior: none
- focus_strategy: rack_focus
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: profile_left
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: warhoon_horde
- primary_subject_frame_position: foreground right within arena_floor
- primary_subject_scale_relation: size of beast vs Carter
- primary_subject_facing_direction: profile left toward the scene action
- primary_subject_pose_description: beast charge
- subject_relation_summary: various_beasts plays against warhoon_horde in the same frame
- scene_short_description: Prisoners enter a massive subterranean amphitheater for a ten-day gladiatorial tournament.
- shot_moment_summary: Carter fights a beast
- required_environment_anchor_1: arena_floor
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: size of beast vs Carter
- camera_package_description: full, eye level, wide lens, track, rack focus, high contrast ceremonial
- environment_subzone: arena_floor
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; warhoon_horde; subterranean_amphitheater_arena; DESC_CH019_SC003; DESC_CH019_SC003_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: identity reference for the secondary visible subject
- image2_asset: warhoon horde
- image3_role: environment reference for the scene location
- image3_asset: subterranean amphitheater arena

# Continuity Notes
- Scene: CH019_SC003 / SC003.
- Variant: Consistency Repair.
- Blood and wound placement on john_carter
- Weapon handling consistency across multiple fights
- Crowd noise levels scaling with combat intensity
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH019\CH019_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH019\CH019_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH019\CH019_SC003\SH003\DIALOGUE.json
