# Title
SH001 Shot Prompt - Consistency Repair

# ID
CH007_SC004_SH001_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for protagonist. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for the dead city. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. Intensive Martian language training and telepathic discovery within a desolate urban environment. The subject from image1 is protagonist, foreground inside training zone, Individual mental struggle against external psychic pressure, front three-quarter right toward the scene action, protagonist looking at text/symbols. The subject from image2 is protagonist plays against sola in the same frame. Preserve the environment from image3 An expansive, ruined urban center., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially training zone. Keep one readable subject anchor: training area floor/surface. medium-close, eye level, normal lens, locked off, shallow subject, diffuse ambient. Intimate composition that ites, against to capture the beat's emotional turn. protagonist studying Martian language. training zone. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH007_SC004; SHOT_INDEX; DIALOGUE; protagonist; sola; young_martian
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: normal
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: consistency_repair
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH007_SC004
- chapter_id: CH007
- shot_type: reaction_closeup
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Close framing that ites reaction and emotional emphasis.
- composition: Intimate composition that isolates protagonist, sola against the_dead_city to capture the beat's emotional turn.
- shot_size: medium_close
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: front_three_quarter_right
- visible_primary_subject_id: protagonist
- visible_secondary_subject_ids: sola
- primary_subject_frame_position: foreground inside training_zone
- primary_subject_scale_relation: Individual mental struggle against external psychic pressure.
- primary_subject_facing_direction: front three-quarter right toward the scene action
- primary_subject_pose_description: protagonist looking at text/symbols
- subject_relation_summary: protagonist plays against sola in the same frame
- scene_short_description: Intensive Martian language training and telepathic discovery within a desolate urban environment.
- shot_moment_summary: protagonist studying Martian language
- required_environment_anchor_1: training_zone
- required_subject_anchor_1: training area floor/surface
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: Individual mental struggle against external psychic pressure.
- camera_package_description: medium-close, eye level, normal lens, locked off, shallow subject, diffuse ambient
- environment_subzone: training_zone
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; sola; the_dead_city; DESC_CH007_SC004; DESC_CH007_SC004_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: protagonist
- image2_role: identity reference for the secondary visible subject
- image2_asset: sola
- image3_role: environment reference for the scene location
- image3_asset: the dead city

# Continuity Notes
- Scene: CH007_SC004 / SC004.
- Variant: Consistency Repair.
- Visual consistency of telepathic effect representation
- Physical interaction mechanics between protagonist and young_martian
- Intensive Martian language training
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH007\CH007_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH007\CH007_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH007\CH007_SC004\SH001\DIALOGUE.json
