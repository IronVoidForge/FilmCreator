# Title
SH001 Shot Prompt - Primary Keyframe

# ID
CH017_SC002_SH001_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the secondary visible subject. Use image2 as the environment reference for mossy waste. Use image3 as the identity reference for an additional visible subject. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. A small group on mounts traverses a vast, trackless expanse of mossy terrain. The visible subject is midground inside mossy waste horizon, tiny figures vs horizon, profile right toward the scene action, wide view of landscape. The subject from image1 is The Narrator plays against dejah thoris, sola in the same frame. Preserve the environment from image2 Vast horizon, endless mossy plains, no visible landmarks., monumental scale, especially mossy waste horizon. wide, eye level, ultra-wide lens, pan, deep focus, diffuse ambient. Wide composition across placed for immediate spatial orientation. group moving across vast moss. horizon. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH017_SC002; SHOT_INDEX; DIALOGUE; dejah_thoris; sola; woola
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: ultra_wide
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: primary_keyframe
- review_notes: SH001: visible primary subject id is missing for an on-screen shot.
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH017_SC002
- chapter_id: CH017
- shot_type: establishing_wide
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across mossy_waste with The Narrator, dejah_thoris, sola placed for immediate spatial orientation.
- shot_size: wide
- camera_angle: eye_level
- camera_motion: pan
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: profile_right
- visible_primary_subject_id: (none)
- visible_secondary_subject_ids: dejah_thoris; sola
- primary_subject_frame_position: midground inside mossy_waste_horizon
- primary_subject_scale_relation: tiny figures vs horizon
- primary_subject_facing_direction: profile right toward the scene action
- primary_subject_pose_description: wide view of landscape
- subject_relation_summary: The Narrator plays against dejah_thoris, sola in the same frame
- scene_short_description: A small group on mounts traverses a vast, trackless expanse of mossy terrain.
- shot_moment_summary: group moving across vast moss
- required_environment_anchor_1: mossy_waste_horizon
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: tiny figures vs horizon
- camera_package_description: wide, eye level, ultra-wide lens, pan, deep focus, diffuse ambient
- environment_subzone: mossy_waste_horizon
- prompt_family: shot_prompt
- reference_asset_ids: dejah_thoris; sola; mossy_waste; DESC_CH017_SC002; DESC_CH017_SC002_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the secondary visible subject
- image1_asset: dejah thoris
- image2_role: environment reference for the scene location
- image2_asset: mossy waste
- image3_role: identity reference for an additional visible subject
- image3_asset: sola

# Continuity Notes
- Scene: CH017_SC002 / SC002.
- Variant: Primary Keyframe.
- Physical condition and exhaustion level of the thoats
- Depletion levels of group supplies (food/water)
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH017\CH017_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH017\CH017_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH017\CH017_SC002\SH001\DIALOGUE.json
