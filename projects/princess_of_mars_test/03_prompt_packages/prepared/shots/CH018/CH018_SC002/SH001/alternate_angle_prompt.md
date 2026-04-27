# Title
SH001 Shot Prompt - Alternate Angle

# ID
CH018_SC002_SH001_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for dak kova. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for martian plains march route. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. Two leaders engage in a savage hand-to-hand duel amidst a surrounding horde on open plains. The subject from image1 is dak kova, foreground entry line within combat circle, height differential between leaders and horde, front three-quarter left toward the scene action, Dak Kova standing still. The subject from image2 is A dignified Warhoon leader., Young., lean athletic build, Warhoon culture, dak kova plays against bar comas in the same frame. Preserve the environment from image3 Vast, open plains suitable for epic military marches., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially combat circle. Keep one readable subject anchor: Duelists face each other; horde forms a ring. Keep celestial anchor Dak Kova stares down Bar Comas stable in the frame. medium-full, low angle, wide lens, push in, deep focus, diffuse ambient. Readable medium composition in featuring. Dak Kova stares down Bar Comas. combat circle. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH018_SC002; SHOT_INDEX; DIALOGUE; dak_kova; bar_comas
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: wide
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
- scene_id: CH018_SC002
- chapter_id: CH018
- shot_type: medium
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in martian_plains_march_route featuring dak_kova, bar_comas, Warhoon Warriors (spectators).
- shot_size: medium_full
- camera_angle: low_angle
- camera_motion: push_in
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: front_three_quarter_left
- visible_primary_subject_id: dak_kova
- visible_secondary_subject_ids: bar_comas
- primary_subject_frame_position: foreground entry line within combat_circle
- primary_subject_scale_relation: height differential between leaders and horde
- primary_subject_facing_direction: front three-quarter left toward the scene action
- primary_subject_pose_description: Dak Kova standing still
- subject_relation_summary: dak_kova plays against bar_comas in the same frame
- scene_short_description: Two leaders engage in a savage hand-to-hand duel amidst a surrounding horde on open plains.
- shot_moment_summary: Dak Kova stares down Bar Comas
- required_environment_anchor_1: combat_circle
- required_subject_anchor_1: Duelists face each other; horde forms a ring
- required_celestial_anchor_1: Dak Kova stares down Bar Comas
- required_scale_proof_detail: height differential between leaders and horde
- camera_package_description: medium-full, low angle, wide lens, push in, deep focus, diffuse ambient
- environment_subzone: combat_circle
- prompt_family: shot_prompt
- reference_asset_ids: dak_kova; bar_comas; martian_plains_march_route; DESC_CH018_SC002; DESC_CH018_SC002_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: dak kova
- image2_role: identity reference for the secondary visible subject
- image2_asset: bar comas
- image3_role: environment reference for the scene location
- image3_asset: martian plains march route

# Continuity Notes
- Scene: CH018_SC002 / SC002.
- Variant: Alternate Angle.
- Blood splatter patterns on terrain and characters
- Final positioning of the fallen Bar Comas
- Dak Kova's physical state (scars, sweat, blood) post-combat
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH018\CH018_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH018\CH018_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH018\CH018_SC002\SH001\DIALOGUE.json
