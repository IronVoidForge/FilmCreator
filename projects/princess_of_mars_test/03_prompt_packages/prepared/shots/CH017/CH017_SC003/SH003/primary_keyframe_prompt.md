# Title
SH003 Shot Prompt - Primary Keyframe

# ID
CH017_SC003_SH003_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for dejah thoris. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for mossy waste. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. A group flees through a mossy waste as a rifleman holds back approaching hunters. The subject from image1 is dejah thoris, midground inside hill approach, women size relative to hill slope, back to camera with head turned toward the action, running toward hills. The subject from image2 is dejah thoris plays against sola in the same frame. Preserve the environment from image3 Vast horizon, endless mossy plains, no visible landmarks., monumental scale, especially low mountains. Keep one readable subject anchor: back to camera with head turned toward the action. wide, high angle, wide lens, track, deep focus, diffuse ambient. Dynamic composition in clear pursuit vectors and readable movement. High angle view of women fleeing. hill approach. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH017_SC003; SHOT_INDEX; DIALOGUE; dejah_thoris; sola
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: wide
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
- scene_id: CH017_SC003
- chapter_id: CH017
- shot_type: action
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: Dynamic composition in mossy_waste with clear pursuit vectors and readable movement for dejah_thoris, sola, The Narrator.
- shot_size: wide
- camera_angle: high_angle
- camera_motion: track
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: back
- visible_primary_subject_id: dejah_thoris
- visible_secondary_subject_ids: sola
- primary_subject_frame_position: midground inside hill_approach
- primary_subject_scale_relation: women size relative to hill slope
- primary_subject_facing_direction: back to camera with head turned toward the action
- primary_subject_pose_description: running toward hills
- subject_relation_summary: dejah_thoris plays against sola in the same frame
- scene_short_description: A group flees through a mossy waste as a rifleman holds back approaching hunters.
- shot_moment_summary: High angle view of women fleeing
- required_environment_anchor_1: low mountains
- required_subject_anchor_1: back to camera with head turned toward the action
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: women size relative to hill slope
- camera_package_description: wide, high angle, wide lens, track, deep focus, diffuse ambient
- environment_subzone: hill_approach
- prompt_family: shot_prompt
- reference_asset_ids: dejah_thoris; sola; mossy_waste; DESC_CH017_SC003; DESC_CH017_SC003_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: dejah thoris
- image2_role: identity reference for the secondary visible subject
- image2_asset: sola
- image3_role: environment reference for the scene location
- image3_asset: mossy waste

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
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH017\CH017_SC003\SH003\DIALOGUE.json
