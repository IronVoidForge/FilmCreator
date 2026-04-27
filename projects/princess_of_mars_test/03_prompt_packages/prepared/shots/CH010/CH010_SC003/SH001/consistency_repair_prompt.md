# Title
SH001 Shot Prompt - Consistency Repair

# ID
CH010_SC003_SH001_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for dejah thoris. Use image2 as the environment reference for lorquas ptomel audience chamber. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. A sudden strike against a noblewoman triggers a violent struggle between an Earthman and a giant warrior. The subject from image1 is Young Thark Warrior, foreground inside thark audience chamber central floor, warrior height vs dejah, profile left toward the scene action, peaceful tension. Preserve the environment from image2 Large scale, centered around a focal point for the presiding chieftain., monumental scale, dry open Martian terrain, especially thark audience chamber central floor. close-up, eye level, portrait lens, handheld, shallow subject, high contrast ceremonial. Intimate composition that isolates, against to capture the beat's emotional turn. Young Thark Warrior strikes Dejah Thoris. thark audience chamber central floor. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH010_SC003; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris; sarkoja
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: portrait
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
- scene_id: CH010_SC003
- chapter_id: CH010
- shot_type: reaction_closeup
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates Young Thark Warrior, dejah_thoris against lorquas_ptomel_audience_chamber to capture the beat's emotional turn.
- shot_size: close_up
- camera_angle: eye_level
- camera_motion: handheld
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: profile_left
- visible_primary_subject_id: dejah_thoris
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground inside thark_audience_chamber central floor
- primary_subject_scale_relation: warrior height vs dejah
- primary_subject_facing_direction: profile left toward the scene action
- primary_subject_pose_description: peaceful tension
- subject_relation_summary: Young Thark Warrior carries the frame alone
- scene_short_description: A sudden strike against a noblewoman triggers a violent struggle between an Earthman and a giant warrior.
- shot_moment_summary: Young Thark Warrior strikes Dejah Thoris
- required_environment_anchor_1: thark_audience_chamber central floor
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: warrior height vs dejah
- camera_package_description: close-up, eye level, portrait lens, handheld, shallow subject, high contrast ceremonial
- environment_subzone: thark_audience_chamber central floor
- prompt_family: shot_prompt
- reference_asset_ids: dejah_thoris; lorquas_ptomel_audience_chamber; DESC_CH010_SC003; DESC_CH010_SC003_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: dejah thoris
- image2_role: environment reference for the scene location
- image2_asset: lorquas ptomel audience chamber

# Continuity Notes
- Scene: CH010_SC003 / SC003.
- Variant: Consistency Repair.
- Directional vector of the blow to Dejah's face
- Choreography and sequence of the kill
- Final resting positions of bodies post-combat
- The strike against Dejah Thoris
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH010\CH010_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH010\CH010_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH010\CH010_SC003\SH001\DIALOGUE.json
