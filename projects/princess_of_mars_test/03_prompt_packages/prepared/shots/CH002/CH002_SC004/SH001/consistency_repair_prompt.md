# Title
SH001 Shot Prompt - Consistency Repair

# ID
CH002_SC004_SH001_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the environment reference for the scene location. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships.. A naked man flees a dark cavern into the vast, moonlit Arizona mountain night.. The subject from image1 is described character with stable costume and silhouette, foreground inside Cave Interior (Transitioning), tight enclosure vs moving body, rear three-quarter left away from camera, protagonist in shadow. Preserve described environment with stable spatial continuity from image2, especially Cave Interior (Transitioning). tight enclosure vs moving body. medium-close, low angle, wide lens, track, shallow subject, low key night. Intimate composition that isolates against to capture the beat's emotional turn.. protagonist scrambling through dark cave. Cave Interior (Transitioning). Keep continuity exact across costume, silhouette, lighting, and spatial relationships.. Avoid proper nouns in the prompt body unless text is meant to appear on screen.. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH002_SC004; SHOT_INDEX; DIALOGUE; protagonist
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: wide
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
- scene_id: CH002_SC004
- chapter_id: CH002
- shot_type: reaction_closeup
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates protagonist against rocky_gorge_canyon to capture the beat's emotional turn.
- shot_size: medium_close
- camera_angle: low_angle
- camera_motion: track
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: low_key_night
- subject_visibility: partial
- narration_mode: none
- primary_subject_angle: rear_three_quarter_left
- visible_primary_subject_id: protagonist
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground inside Cave Interior (Transitioning)
- primary_subject_scale_relation: tight enclosure vs moving body
- primary_subject_facing_direction: rear three-quarter left away from camera
- primary_subject_pose_description: protagonist in shadow
- subject_relation_summary: protagonist carries the frame alone
- scene_short_description: A naked man flees a dark cavern into the vast, moonlit Arizona mountain night.
- shot_moment_summary: protagonist scrambling through dark cave
- required_environment_anchor_1: Cave Interior (Transitioning)
- required_scale_proof_detail: tight enclosure vs moving body
- camera_package_description: medium-close, low angle, wide lens, track, shallow subject, low key night
- environment_subzone: Cave Interior (Transitioning)
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; rocky_gorge_canyon; DESC_CH002_SC004; DESC_CH002_SC004_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: protagonist
- image2_role: environment reference for the scene location
- image2_asset: rocky gorge canyon

# Continuity Notes
- Scene: CH002_SC004 / SC004.
- Variant: Consistency Repair.
- Protagonist nudity and physical state across light level shifts
- Physical condition post-gas paralysis
- Protagonist flees the dark cave interior
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH002\CH002_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH002\CH002_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH002\CH002_SC004\SH001\DIALOGUE.json
