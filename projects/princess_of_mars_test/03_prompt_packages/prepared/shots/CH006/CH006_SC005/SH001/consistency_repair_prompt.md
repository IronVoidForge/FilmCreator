# Title
SH001 Shot Prompt - Consistency Repair

# ID
CH006_SC005_SH001_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for tars tarkas. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for martian interior chamber. Use image4 as the identity reference for an additional visible subject. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. A quieted interior chamber where a survivor reflects on his dual bonds amidst the stillness. The subject from image1 is tars tarkas, foreground entry line within martian interior chamber central floor, tars tarkas height relative to protagonist, front three-quarter right toward the scene action, active tension. The subject from image2 is tars tarkas plays against protagonist, watch thing in the same frame. Preserve the environment from image3 monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, broad processional paths and stairs, especially martian interior chamber central floor. medium-full, eye level, normal lens, locked off, deep focus, diffuse ambient. Readable medium composition in featuring. Tars Tarkas yields control of the beast to the protagonist. central floor. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH006_SC005; SHOT_INDEX; DIALOGUE; protagonist; sola; tars_tarkas; watch_thing
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
- scene_id: CH006_SC005
- chapter_id: CH006
- shot_type: medium
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in martian_interior_chamber featuring tars_tarkas, protagonist, watch_thing.
- shot_size: medium_full
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: front_three_quarter_right
- visible_primary_subject_id: tars_tarkas
- visible_secondary_subject_ids: protagonist; watch_thing
- primary_subject_frame_position: foreground entry line within martian_interior_chamber central floor
- primary_subject_scale_relation: tars_tarkas height relative to protagonist
- primary_subject_facing_direction: front three-quarter right toward the scene action
- primary_subject_pose_description: active tension
- subject_relation_summary: tars_tarkas plays against protagonist, watch_thing in the same frame
- scene_short_description: A quieted interior chamber where a survivor reflects on his dual bonds amidst the stillness.
- shot_moment_summary: Tars Tarkas yields control of the beast to the protagonist.
- required_environment_anchor_1: martian_interior_chamber central floor
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: tars_tarkas height relative to protagonist
- camera_package_description: medium-full, eye level, normal lens, locked off, deep focus, diffuse ambient
- environment_subzone: martian_interior_chamber central floor
- prompt_family: shot_prompt
- reference_asset_ids: tars_tarkas; protagonist; watch_thing; martian_interior_chamber; DESC_CH006_SC005; DESC_CH006_SC005_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: tars tarkas
- image2_role: identity reference for the secondary visible subject
- image2_asset: protagonist
- image3_role: environment reference for the scene location
- image3_asset: martian interior chamber
- image4_role: identity reference for an additional visible subject
- image4_asset: watch thing

# Continuity Notes
- Scene: CH006_SC005 / SC005.
- Variant: Consistency Repair.
- Post-battle physical state (bruises, dirt)
- Protagonist nudity/metamorphosis status
- Tars Tarkas concedes the beast to the protagonist
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH006\CH006_SC005.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH006\CH006_SC005\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH006\CH006_SC005\SH001\DIALOGUE.json
