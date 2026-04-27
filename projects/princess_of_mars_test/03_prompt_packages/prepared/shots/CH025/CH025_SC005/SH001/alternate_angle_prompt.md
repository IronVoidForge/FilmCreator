# Title
SH001 Shot Prompt - Alternate Angle

# ID
CH025_SC005_SH001_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for zodanga palace throne room. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. Two combat-worn figures find quiet intimacy amidst the wreckage of a royal throne room. The subject from image1 is john carter, foreground entry line within central hall floor, characters appear small against the ruined architecture, front three-quarter right toward the scene action, heavy breathing/exhaustion. The subject from image2 is john carter plays against dejah thoris in the same frame. Preserve the environment from image3 Massive scale with high ceilings, includes a central throne platform/raised dais and wide floor space capable of hosting skirmishes or cavalry charges., monumental scale, dry open Martian terrain, especially central hall floor. medium-full, eye level, wide lens, locked off, deep focus, diffuse ambient. Wide composition across placed for immediate spatial orientation. Characters standing in silence amidst debris. central hall floor. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH025_SC005; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris
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
- scene_id: CH025_SC005
- chapter_id: CH025
- shot_type: establishing_wide
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across zodanga_palace_throne_room with john_carter, dejah_thoris placed for immediate spatial orientation.
- shot_size: medium_full
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_right
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: dejah_thoris
- primary_subject_frame_position: foreground entry line within central hall floor
- primary_subject_scale_relation: characters appear small against the ruined architecture
- primary_subject_facing_direction: front three-quarter right toward the scene action
- primary_subject_pose_description: heavy breathing/exhaustion
- subject_relation_summary: john_carter plays against dejah_thoris in the same frame
- scene_short_description: Two combat-worn figures find quiet intimacy amidst the wreckage of a royal throne room.
- shot_moment_summary: Characters standing in silence amidst debris
- required_environment_anchor_1: central hall floor
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: characters appear small against the ruined architecture
- camera_package_description: medium-full, eye level, wide lens, locked off, deep focus, diffuse ambient
- environment_subzone: central hall floor
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; dejah_thoris; zodanga_palace_throne_room; DESC_CH025_SC005; DESC_CH025_SC005_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: identity reference for the secondary visible subject
- image2_asset: dejah thoris
- image3_role: environment reference for the scene location
- image3_asset: zodanga palace throne room

# Continuity Notes
- Scene: CH025_SC005 / SC005.
- Variant: Alternate Angle.
- Character dishevelment (sweat, torn clothing)
- Presence of battle debris in throne room
- Silence amidst the aftermath
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH025\CH025_SC005.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH025\CH025_SC005\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH025\CH025_SC005\SH001\DIALOGUE.json
