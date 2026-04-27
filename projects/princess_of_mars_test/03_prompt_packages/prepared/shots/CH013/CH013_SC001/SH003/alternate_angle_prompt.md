# Title
SH003 Shot Prompt - Alternate Angle

# ID
CH013_SC001_SH003_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for tars tarkas. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for green martian city complex. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. A human man uses gentle authority to tame large, aggressive Martian beasts within a city complex. The subject from image1 is tars tarkas, foreground right within warrior observation deck, observer distance to arena, front three-quarter left toward the scene action, observing intently. The subject from image2 is tars tarkas plays against john carter in the same frame. Preserve the environment from image3 Features wide thoroughfares, central leadership hubs, and large-scale enclosures/pens for beasts., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially warrior observation deck. medium, eye level, normal lens, pan, rack focus, diffuse ambient. Closing composition in that emphasizes the consequence of teaching the warriors. Tars Tarkas watching the success. warrior observation deck. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH013_SC001; SHOT_INDEX; DIALOGUE; john_carter; tars_tarkas; green_martian_warriors
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
- scene_id: CH013_SC001
- chapter_id: CH013
- shot_type: closing_reaction
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Controlled closing frame that lands the consequence of the beat.
- composition: Closing composition in green_martian_city_complex that emphasizes the consequence of teaching the warriors.
- shot_size: medium
- camera_angle: eye_level
- camera_motion: pan
- zoom_behavior: none
- focus_strategy: rack_focus
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_left
- visible_primary_subject_id: tars_tarkas
- visible_secondary_subject_ids: john_carter
- primary_subject_frame_position: foreground right within warrior_observation_deck
- primary_subject_scale_relation: observer distance to arena
- primary_subject_facing_direction: front three-quarter left toward the scene action
- primary_subject_pose_description: observing intently
- subject_relation_summary: tars_tarkas plays against john_carter in the same frame
- scene_short_description: A human man uses gentle authority to tame large, aggressive Martian beasts within a city complex.
- shot_moment_summary: Tars Tarkas watching the success
- required_environment_anchor_1: warrior_observation_deck
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: observer distance to arena
- camera_package_description: medium, eye level, normal lens, pan, rack focus, diffuse ambient
- environment_subzone: warrior_observation_deck
- prompt_family: shot_prompt
- reference_asset_ids: tars_tarkas; john_carter; green_martian_city_complex; DESC_CH013_SC001; DESC_CH013_SC001_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: tars tarkas
- image2_role: identity reference for the secondary visible subject
- image2_asset: john carter
- image3_role: environment reference for the scene location
- image3_asset: green martian city complex

# Continuity Notes
- Scene: CH013_SC001 / SC001.
- Variant: Alternate Angle.
- Physical behavior shift of thoats from wild to docile
- Carter's training attire consistency
- Specific hand/body movements used in taming process
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH013\CH013_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH013\CH013_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH013\CH013_SC001\SH003\DIALOGUE.json
