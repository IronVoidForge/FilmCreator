# Title
SH001 Shot Prompt - Alternate Angle

# ID
CH004_SC004_SH001_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for sola. Use image2 as the environment reference for martian sleeping quarters. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. A weary traveler is led through hallways into a warm, decorated chamber containing a strange creature. The subject from image1 is sola, foreground entry line within Interior Hallways, humanoid scale comparison, profile left toward the scene action, narrator requesting food/water. Preserve the environment from image2 monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, broad processional paths and stairs, especially Interior Hallways. Keep one readable subject anchor: sola walking slightly ahead of narrator. medium-full, eye level, normal lens, track, shallow subject, diffuse ambient. Readable medium composition in Interior Hallways featuring, The Narrator. sola leads the narrator through the hallway. Interior Hallways. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH004_SC004; SHOT_INDEX; DIALOGUE; sola
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: normal
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: alternate_angle
- review_notes: Environment reference conflict: prompt variables align more with `none` than bound `martian_sleeping_quarters`.
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH004_SC004
- chapter_id: CH004
- shot_type: medium
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in Interior Hallways featuring sola, The Narrator.
- shot_size: medium_full
- camera_angle: eye_level
- camera_motion: track
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: profile_left
- visible_primary_subject_id: sola
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground entry line within Interior Hallways
- primary_subject_scale_relation: humanoid scale comparison
- primary_subject_facing_direction: profile left toward the scene action
- primary_subject_pose_description: narrator requesting food/water
- subject_relation_summary: sola carries the frame alone
- scene_short_description: A weary traveler is led through hallways into a warm, decorated chamber containing a strange creature.
- shot_moment_summary: sola leads the narrator through the hallway
- required_environment_anchor_1: Interior Hallways
- required_subject_anchor_1: sola walking slightly ahead of narrator
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: humanoid scale comparison
- camera_package_description: medium-full, eye level, normal lens, track, shallow subject, diffuse ambient
- environment_subzone: Interior Hallways
- prompt_family: shot_prompt
- reference_asset_ids: sola; martian_sleeping_quarters; DESC_CH004_SC004; DESC_CH004_SC004_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: sola
- image2_role: environment reference for the scene location
- image2_asset: martian sleeping quarters

# Continuity Notes
- Scene: CH004_SC004 / SC004.
- Variant: Alternate Angle.
- Movement and limb count of the ten-legged creature
- Lighting transition from grand hall to private quarters
- Request for sustenance and guidance
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH004\CH004_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH004\CH004_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH004\CH004_SC004\SH001\DIALOGUE.json
