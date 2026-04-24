# Title
SH003 Shot Prompt - Consistency Repair

# ID
CH002_SC001_SH003_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the primary visible subject. Use image2 as the environment reference for the scene location. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships.. A man lies paralyzed in a dark, vapor-filled cave experiencing sensory isolation.. The subject from image1 is described character with stable costume and silhouette, foreground inside cave interior, Microscopic physiological detail vs. claustrophobic environmental scale., facing directly toward camera, blurry view. Preserve described environment with stable spatial continuity from image2, especially cave wall texture. blurred vision depth. medium-close, eye level, wide lens, handheld, environment priority, low key night. Intimate composition that isolates against to capture the beat's emotional turn.. Blurred POV of the dark cave walls. cave interior. Keep continuity exact across costume, silhouette, lighting, and spatial relationships.. Avoid proper nouns in the prompt body unless text is meant to appear on screen.. No text, no watermark, no logo.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH002_SC001; SHOT_INDEX; DIALOGUE; protagonist
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
- scene_id: CH002_SC001
- chapter_id: CH002
- shot_type: reaction_closeup
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates protagonist against arizona_mountain_cave to capture the beat's emotional turn.
- shot_size: medium_close
- camera_angle: eye_level
- camera_motion: handheld
- zoom_behavior: none
- focus_strategy: environment_priority
- lighting_style: low_key_night
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front
- visible_primary_subject_id: protagonist
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground inside cave interior
- primary_subject_scale_relation: Microscopic physiological detail vs. claustrophobic environmental scale.
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: blurry view
- subject_relation_summary: arizona_mountain_cave plays against protagonist in the same frame
- scene_short_description: A man lies paralyzed in a dark, vapor-filled cave experiencing sensory isolation.
- shot_moment_summary: Blurred POV of the dark cave walls
- required_environment_anchor_1: cave wall texture
- required_scale_proof_detail: blurred vision depth
- camera_package_description: medium-close, eye level, wide lens, handheld, environment priority, low key night
- environment_subzone: cave interior
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; arizona_mountain_cave; DESC_CH002_SC001; DESC_CH002_SC001_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: protagonist
- image2_role: environment reference for the scene location
- image2_asset: arizona mountain cave

# Continuity Notes
- Scene: CH002_SC001 / SC001.
- Variant: Consistency Repair.
- Pupil dilation and eye movement tracking
- Vapor density and visual quality/texture
- Escalation to helpless terror and isolation
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH002\CH002_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH002\CH002_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH002\CH002_SC001\SH003\DIALOGUE.json
