# Title
SH003 Shot Prompt - Primary Keyframe

# ID
CH017_SC004_SH003_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the environment reference for mossy waste. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. A lone figure defends against a swarm of warriors across vast green mossy plains. The visible subject is foreground inside mossy waste open expanse, preserve readable body-to-environment scale in frame, facing directly toward camera, Narrator falling to knees. Preserve the environment from image1 Vast horizon, endless mossy plains, no visible landmarks., monumental scale, especially mossy waste open expanse. close-up, low angle, portrait lens, handheld, zoom subtle in, shallow subject, low key night. Intimate composition that isolates, against to capture the beat's emotional turn. The final beating and loss of consciousness. open expanse. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH017_SC004; SHOT_INDEX; DIALOGUE
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: portrait
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: primary_keyframe
- review_notes: SH003: visible primary subject id is missing for an on-screen shot.
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH017_SC004
- chapter_id: CH017
- shot_type: reaction_closeup
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates The Narrator, Thark Warriors against mossy_waste to capture the beat's emotional turn.
- shot_size: close_up
- camera_angle: low_angle
- camera_motion: handheld
- zoom_behavior: subtle_in
- focus_strategy: shallow_subject
- lighting_style: low_key_night
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front
- visible_primary_subject_id: (none)
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground inside mossy_waste_open_expanse
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: Narrator falling to knees
- subject_relation_summary: The Narrator carries the frame alone
- scene_short_description: A lone figure defends against a swarm of warriors across vast green mossy plains.
- shot_moment_summary: The final beating and loss of consciousness
- required_environment_anchor_1: mossy_waste_open_expanse
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: preserve readable body-to-environment scale in frame
- camera_package_description: close-up, low angle, portrait lens, handheld, zoom subtle in, shallow subject, low key night
- environment_subzone: mossy_waste_open_expanse
- prompt_family: shot_prompt
- reference_asset_ids: mossy_waste; DESC_CH017_SC004; DESC_CH017_SC004_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: environment reference for the scene location
- image1_asset: mossy waste

# Continuity Notes
- Scene: CH017_SC004 / SC004.
- Variant: Primary Keyframe.
- Exact count of Thark Warriors appearing in waves
- Physical damage state of the Narrator's rifle and equipment
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH017\CH017_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH017\CH017_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH017\CH017_SC004\SH003\DIALOGUE.json
