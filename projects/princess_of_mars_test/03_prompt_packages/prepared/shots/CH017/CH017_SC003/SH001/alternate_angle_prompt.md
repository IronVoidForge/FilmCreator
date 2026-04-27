# Title
SH001 Shot Prompt - Alternate Angle

# ID
CH017_SC003_SH001_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for thark chieftain. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for mossy waste. Use image4 as the identity reference for an additional visible subject. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. A group flees through a mossy waste as a rifleman holds back approaching hunters. The subject from image1 is Thark Chieftain, foreground entry line within hunter vantage, chieftain size relative to distant landscape, profile left toward the scene action, chieftain scanning. The subject from image2 is Thark Chieftain plays against dejah thoris, sola in the same frame. Preserve the environment from image3 Vast horizon, endless mossy plains, no visible landmarks., monumental scale, especially low mountains. medium, eye level, telephoto lens, pan, deep focus, diffuse ambient. Readable medium composition in featuring. Chieftain spots group through fieldglass. hunter vantage. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH017_SC003; SHOT_INDEX; DIALOGUE; dejah_thoris; sola
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: telephoto
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: alternate_angle
- review_notes: Prompt body is missing the required subject anchor for an on-screen shot.
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH017_SC003
- chapter_id: CH017
- shot_type: medium
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in mossy_waste featuring Thark Chieftain, dejah_thoris, sola.
- shot_size: medium
- camera_angle: eye_level
- camera_motion: pan
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: profile_left
- visible_primary_subject_id: thark chieftain
- visible_secondary_subject_ids: dejah_thoris; sola
- primary_subject_frame_position: foreground entry line within hunter_vantage
- primary_subject_scale_relation: chieftain size relative to distant landscape
- primary_subject_facing_direction: profile left toward the scene action
- primary_subject_pose_description: chieftain scanning
- subject_relation_summary: Thark Chieftain plays against dejah_thoris, sola in the same frame
- scene_short_description: A group flees through a mossy waste as a rifleman holds back approaching hunters.
- shot_moment_summary: Chieftain spots group through fieldglass
- required_environment_anchor_1: low mountains
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: chieftain size relative to distant landscape
- camera_package_description: medium, eye level, telephoto lens, pan, deep focus, diffuse ambient
- environment_subzone: hunter_vantage
- prompt_family: shot_prompt
- reference_asset_ids: dejah_thoris; sola; mossy_waste; DESC_CH017_SC003; DESC_CH017_SC003_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: thark chieftain
- image2_role: identity reference for the secondary visible subject
- image2_asset: dejah thoris
- image3_role: environment reference for the scene location
- image3_asset: mossy waste
- image4_role: identity reference for an additional visible subject
- image4_asset: sola

# Continuity Notes
- Scene: CH017_SC003 / SC003.
- Variant: Alternate Angle.
- Exact position of the collapsed thoat relative to characters
- Detection of the group by Thark Chieftain
- Direction of narrator's cover fire must be opposite to the direction of Dejah Thoris and Sola's retreat
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH017\CH017_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH017\CH017_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH017\CH017_SC003\SH001\DIALOGUE.json
