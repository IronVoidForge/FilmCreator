# Title
SH003 Shot Prompt - Primary Keyframe

# ID
CH015_SC001_SH003_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for dejah thoris. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for caravan camp hills. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. A wounded man recovers amidst a caravan camp while observing a woman in deep mourning. The subject from image1 is dejah thoris, foreground right within caravan camp hills mourning zone, preserve readable body-to-environment scale in frame, front three-quarter left toward the scene action, Dejah looking down. The subject from image2 is dejah thoris plays against john carter in the same frame. Preserve the environment from image3 Located at the foot of rising hills where the terrain transitions from the flat mossy sea to elevated topography., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially caravan camp hills mourning zone. Keep one readable subject anchor: Dejah's expression. medium, eye level, portrait lens, locked off, shallow subject, low key night. Closing composition in that emphasizes the consequence of observation of dejah's grief. Dejah Thoris in silent mourning. mourning zone. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH015_SC001; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris; sola
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: portrait
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: primary_keyframe
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH015_SC001
- chapter_id: CH015
- shot_type: closing_reaction
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Controlled closing frame that lands the consequence of the beat.
- composition: Closing composition in caravan_camp_hills that emphasizes the consequence of observation of dejah's grief.
- shot_size: medium
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: low_key_night
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_left
- visible_primary_subject_id: dejah_thoris
- visible_secondary_subject_ids: john_carter
- primary_subject_frame_position: foreground right within caravan_camp_hills_mourning_zone
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: front three-quarter left toward the scene action
- primary_subject_pose_description: Dejah looking down
- subject_relation_summary: dejah_thoris plays against john_carter in the same frame
- scene_short_description: A wounded man recovers amidst a caravan camp while observing a woman in deep mourning.
- shot_moment_summary: Dejah Thoris in silent mourning
- required_environment_anchor_1: caravan_camp_hills_mourning_zone
- required_subject_anchor_1: Dejah's expression
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: preserve readable body-to-environment scale in frame
- camera_package_description: medium, eye level, portrait lens, locked off, shallow subject, low key night
- environment_subzone: caravan_camp_hills_mourning_zone
- prompt_family: shot_prompt
- reference_asset_ids: dejah_thoris; john_carter; caravan_camp_hills; DESC_CH015_SC001; DESC_CH015_SC001_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: dejah thoris
- image2_role: identity reference for the secondary visible subject
- image2_asset: john carter
- image3_role: environment reference for the scene location
- image3_asset: caravan camp hills

# Continuity Notes
- Scene: CH015_SC001 / SC001.
- Variant: Primary Keyframe.
- Specific placement and severity of the sword thrust wound to John Carter's chest
- Visible state/bandaging of Sola's injuries from Sarkoja encounter
- Observation of Dejah's grief
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH015\CH015_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH015\CH015_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH015\CH015_SC001\SH003\DIALOGUE.json
