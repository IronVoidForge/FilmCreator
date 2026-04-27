# Title
SH001 Shot Prompt - Alternate Angle

# ID
CH019_SC004_SH001_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for kantos kan. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for subterranean amphitheater arena. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. A massive warrior falls before a staged execution in a subterranean arena. The subject from image1 is kantos kan, midground inside fighting pit, warrior height vs Kan, front three-quarter right toward the scene action, combat engagement. The subject from image2 is kantos kan plays against john carter in the same frame. Preserve the environment from image3 monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, broad processional paths and stairs, especially fighting pit. wide, low angle, wide lens, track, deep focus, high contrast ceremonial. Wide composition across placed for immediate spatial orientation. Kan strikes the massive warrior. fighting pit. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH019_SC004; SHOT_INDEX; DIALOGUE; john_carter; kantos_kan; warhoon_horde
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: wide
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
- scene_id: CH019_SC004
- chapter_id: CH019
- shot_type: establishing_wide
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across subterranean_amphitheater_arena with kantos_kan, * Massive Green Warrior, john_carter placed for immediate spatial orientation.
- shot_size: wide
- camera_angle: low_angle
- camera_motion: track
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_right
- visible_primary_subject_id: kantos_kan
- visible_secondary_subject_ids: john_carter
- primary_subject_frame_position: midground inside fighting_pit
- primary_subject_scale_relation: warrior height vs Kan
- primary_subject_facing_direction: front three-quarter right toward the scene action
- primary_subject_pose_description: combat engagement
- subject_relation_summary: kantos_kan plays against john_carter in the same frame
- scene_short_description: A massive warrior falls before a staged execution in a subterranean arena.
- shot_moment_summary: Kan strikes the massive warrior
- required_environment_anchor_1: fighting_pit
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: warrior height vs Kan
- camera_package_description: wide, low angle, wide lens, track, deep focus, high contrast ceremonial
- environment_subzone: fighting_pit
- prompt_family: shot_prompt
- reference_asset_ids: kantos_kan; john_carter; subterranean_amphitheater_arena; DESC_CH019_SC004; DESC_CH019_SC004_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: kantos kan
- image2_role: identity reference for the secondary visible subject
- image2_asset: john carter
- image3_role: environment reference for the scene location
- image3_asset: subterranean amphitheater arena

# Continuity Notes
- Scene: CH019_SC004 / SC004.
- Variant: Alternate Angle.
- Exact trajectory of the killing blow
- Distinction between real blood splatter and fake blood splatter
- Weapon states (damage/positioning) during transition from combat to duel
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH019\CH019_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH019\CH019_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH019\CH019_SC004\SH001\DIALOGUE.json
