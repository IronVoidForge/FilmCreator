# Title
SH002 Shot Prompt - Primary Keyframe

# ID
CH017_SC003_SH002_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the environment reference for mossy waste. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. A group flees through a mossy waste as a rifleman holds back approaching hunters. The visible subject is foreground inside mossy waste center, rifle recoil vs body stability, front three-quarter right toward the scene action, aiming. Preserve the environment from image1 Vast horizon, endless mossy plains, no visible landmarks., monumental scale, especially mossy waste center. medium-close, low angle, normal lens, handheld, shallow subject, hard directional. Intimate composition that isolates, against to capture the beat's emotional turn. Narrator fires rifle at Chieftain. center. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH017_SC003; SHOT_INDEX; DIALOGUE; dejah_thoris; sola
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: normal
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: primary_keyframe
- review_notes: SH002: visible primary subject id is missing for an on-screen shot.
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH017_SC003
- chapter_id: CH017
- shot_type: reaction_closeup
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates The Narrator, Thark Chieftain against mossy_waste to capture the beat's emotional turn.
- shot_size: medium_close
- camera_angle: low_angle
- camera_motion: handheld
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: hard_directional
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_right
- visible_primary_subject_id: (none)
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground inside mossy_waste_center
- primary_subject_scale_relation: rifle recoil vs body stability
- primary_subject_facing_direction: front three-quarter right toward the scene action
- primary_subject_pose_description: aiming
- subject_relation_summary: The Narrator carries the frame alone
- scene_short_description: A group flees through a mossy waste as a rifleman holds back approaching hunters.
- shot_moment_summary: Narrator fires rifle at Chieftain
- required_environment_anchor_1: mossy_waste_center
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: rifle recoil vs body stability
- camera_package_description: medium-close, low angle, normal lens, handheld, shallow subject, hard directional
- environment_subzone: mossy_waste_center
- prompt_family: shot_prompt
- reference_asset_ids: mossy_waste; DESC_CH017_SC003; DESC_CH017_SC003_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: environment reference for the scene location
- image1_asset: mossy waste

# Continuity Notes
- Scene: CH017_SC003 / SC003.
- Variant: Primary Keyframe.
- Exact position of the collapsed thoat relative to characters
- Direction of narrator's cover fire must be opposite to the direction of Dejah Thoris and Sola's retreat
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH017\CH017_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH017\CH017_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH017\CH017_SC003\SH002\DIALOGUE.json
