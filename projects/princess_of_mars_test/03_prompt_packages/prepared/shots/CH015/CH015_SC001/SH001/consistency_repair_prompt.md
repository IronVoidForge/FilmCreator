# Title
SH001 Shot Prompt - Consistency Repair

# ID
CH015_SC001_SH001_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the environment reference for caravan camp hills. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. A wounded man recovers amidst a caravan camp while observing a woman in deep mourning. The subject from image1 is john carter, foreground inside caravan camp hills recovery zone, preserve readable body-to-environment scale in frame, front three-quarter right toward the scene action, Carter breathing heavily. Preserve the environment from image2 Located at the foot of rising hills where the terrain transitions from the flat mossy sea to elevated topography., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially caravan camp hills recovery zone. Keep one readable subject anchor: Carter's wound site. close-up, eye level, portrait lens, locked off, shallow subject, diffuse ambient. Intimate composition that isolates against to capture the beat's emotional turn. Carter feeling the pain of the chest wound. recovery zone. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH015_SC001; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris; sola
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: portrait
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
- scene_id: CH015_SC001
- chapter_id: CH015
- shot_type: reaction_closeup
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates john_carter against caravan_camp_hills to capture the beat's emotional turn.
- shot_size: close_up
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_right
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground inside caravan_camp_hills_recovery_zone
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: front three-quarter right toward the scene action
- primary_subject_pose_description: Carter breathing heavily
- subject_relation_summary: john_carter carries the frame alone
- scene_short_description: A wounded man recovers amidst a caravan camp while observing a woman in deep mourning.
- shot_moment_summary: Carter feeling the pain of the chest wound
- required_environment_anchor_1: caravan_camp_hills_recovery_zone
- required_subject_anchor_1: Carter's wound site
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: preserve readable body-to-environment scale in frame
- camera_package_description: close-up, eye level, portrait lens, locked off, shallow subject, diffuse ambient
- environment_subzone: caravan_camp_hills_recovery_zone
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; caravan_camp_hills; DESC_CH015_SC001; DESC_CH015_SC001_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: environment reference for the scene location
- image2_asset: caravan camp hills

# Continuity Notes
- Scene: CH015_SC001 / SC001.
- Variant: Consistency Repair.
- Specific placement and severity of the sword thrust wound to John Carter's chest
- Visible state/bandaging of Sola's injuries from Sarkoja encounter
- Carter recovers from the sword wound
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH015\CH015_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH015\CH015_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH015\CH015_SC001\SH001\DIALOGUE.json
