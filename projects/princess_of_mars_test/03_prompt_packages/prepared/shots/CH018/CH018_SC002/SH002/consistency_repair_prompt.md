# Title
SH002 Shot Prompt - Consistency Repair

# ID
CH018_SC002_SH002_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for dak kova. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for martian plains march route. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. Two leaders engage in a savage hand-to-hand duel amidst a surrounding horde on open plains. The subject from image1 is dak kova, foreground right within combat circle, preserve readable body-to-environment scale in frame, profile left toward the scene action, clash of bodies. The subject from image2 is A dignified Warhoon leader., Young., lean athletic build, Warhoon culture, dak kova plays against bar comas in the same frame. Preserve the environment from image3 Vast, open plains suitable for epic military marches., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially combat circle. medium, eye level, normal lens, handheld, shallow subject, high contrast ceremonial. Detail composition centered on the key physical action or prop inside. The primal hand-to-hand struggle. combat circle. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH018_SC002; SHOT_INDEX; DIALOGUE; dak_kova; bar_comas
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: normal
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
- scene_id: CH018_SC002
- chapter_id: CH018
- shot_type: insert_detail
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Tight detail framing focused on a single visual object or gesture.
- composition: Detail composition centered on the key physical action or prop inside martian_plains_march_route.
- shot_size: medium
- camera_angle: eye_level
- camera_motion: handheld
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: profile_left
- visible_primary_subject_id: dak_kova
- visible_secondary_subject_ids: bar_comas
- primary_subject_frame_position: foreground right within combat_circle
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: profile left toward the scene action
- primary_subject_pose_description: clash of bodies
- subject_relation_summary: dak_kova plays against bar_comas in the same frame
- scene_short_description: Two leaders engage in a savage hand-to-hand duel amidst a surrounding horde on open plains.
- shot_moment_summary: The primal hand-to-hand struggle
- required_environment_anchor_1: combat_circle
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: preserve readable body-to-environment scale in frame
- camera_package_description: medium, eye level, normal lens, handheld, shallow subject, high contrast ceremonial
- environment_subzone: combat_circle
- prompt_family: shot_prompt
- reference_asset_ids: dak_kova; bar_comas; martian_plains_march_route; DESC_CH018_SC002; DESC_CH018_SC002_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: dak kova
- image2_role: identity reference for the secondary visible subject
- image2_asset: bar comas
- image3_role: environment reference for the scene location
- image3_asset: martian plains march route

# Continuity Notes
- Scene: CH018_SC002 / SC002.
- Variant: Consistency Repair.
- Blood splatter patterns on terrain and characters
- Final positioning of the fallen Bar Comas
- Dak Kova's physical state (scars, sweat, blood) post-combat
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH018\CH018_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH018\CH018_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH018\CH018_SC002\SH002\DIALOGUE.json
