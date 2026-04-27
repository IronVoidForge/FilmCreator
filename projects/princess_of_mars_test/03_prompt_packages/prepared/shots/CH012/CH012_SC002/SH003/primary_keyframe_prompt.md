# Title
SH003 Shot Prompt - Primary Keyframe

# ID
CH012_SC002_SH003_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the environment reference for thark city plaza. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. A man moves through a vast alien cityscape while processing a sudden realization of betrayal. The subject from image1 is john carter, foreground inside thark city streets, Individual human scale vs massive, surveillance-heavy Tharkian architecture, profile left toward the scene action, stiffening posture. Preserve the environment from image2 Large scale, features wide streets and expansive communal gathering zones., monumental scale, dry open Martian terrain, especially thark city streets. Keep one readable subject anchor: stiffening posture. medium-close, low angle, normal lens, track, shallow subject, hard directional. Intimate composition that isolates against to capture the beat's emotional turn. Carter hardens resolve to escape. thark city streets. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH012_SC002; SHOT_INDEX; DIALOGUE; john_carter
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: normal
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
- scene_id: CH012_SC002
- chapter_id: CH012
- shot_type: reaction_closeup
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates john_carter against thark_city_plaza to capture the beat's emotional turn.
- shot_size: medium_close
- camera_angle: low_angle
- camera_motion: track
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: hard_directional
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: profile_left
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground inside thark_city_streets
- primary_subject_scale_relation: Individual human scale vs massive, surveillance-heavy Tharkian architecture.
- primary_subject_facing_direction: profile left toward the scene action
- primary_subject_pose_description: stiffening posture
- subject_relation_summary: john_carter carries the frame alone
- scene_short_description: A man moves through a vast alien cityscape while processing a sudden realization of betrayal.
- shot_moment_summary: Carter hardens resolve to escape
- required_environment_anchor_1: thark_city_streets
- required_subject_anchor_1: stiffening posture
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: Individual human scale vs massive, surveillance-heavy Tharkian architecture.
- camera_package_description: medium-close, low angle, normal lens, track, shallow subject, hard directional
- environment_subzone: thark_city_streets
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; thark_city_plaza; DESC_CH012_SC002; DESC_CH012_SC002_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: environment reference for the scene location
- image2_asset: thark city plaza

# Continuity Notes
- Scene: CH012_SC002 / SC002.
- Variant: Primary Keyframe.
- Carter's movement through the city streets
- Time of day consistency during transition from chamber to street
- Hardening of resolve to escape and save Dejah Thoris
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH012\CH012_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH012\CH012_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH012\CH012_SC002\SH003\DIALOGUE.json
