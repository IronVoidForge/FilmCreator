# Title
SH001 Shot Prompt - Consistency Repair

# ID
CH012_SC001_SH001_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for thark audience chamber. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. A human prisoner stands before a Tharkian leader within a formal, high-tension chamber. The subject from image1 is john carter, foreground entry line within central floor, Carter's smallness relative to chamber architecture, front three-quarter right toward the scene action, Carter entering frame. The subject from image2 is john carter plays against lorquas ptomel in the same frame. Preserve the environment from image3 Large scale, designed for high-ranking Tharkian leadership and warriors., monumental scale, dry open Martian terrain, especially central floor. medium-full, eye level, wide lens, track, deep focus, high contrast ceremonial. Readable medium composition in featuring. Carter approaches the leader. central floor. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH012_SC001; SHOT_INDEX; DIALOGUE; john_carter; lorquas_ptomel
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: wide
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
- scene_id: CH012_SC001
- chapter_id: CH012
- shot_type: medium
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in thark_audience_chamber featuring john_carter, lorquas_ptomel.
- shot_size: medium_full
- camera_angle: eye_level
- camera_motion: track
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: front_three_quarter_right
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: lorquas_ptomel
- primary_subject_frame_position: foreground entry line within central floor
- primary_subject_scale_relation: Carter's smallness relative to chamber architecture
- primary_subject_facing_direction: front three-quarter right toward the scene action
- primary_subject_pose_description: Carter entering frame
- subject_relation_summary: john_carter plays against lorquas_ptomel in the same frame
- scene_short_description: A human prisoner stands before a Tharkian leader within a formal, high-tension chamber.
- shot_moment_summary: Carter approaches the leader
- required_environment_anchor_1: central floor
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: Carter's smallness relative to chamber architecture
- camera_package_description: medium-full, eye level, wide lens, track, deep focus, high contrast ceremonial
- environment_subzone: central floor
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; lorquas_ptomel; thark_audience_chamber; DESC_CH012_SC001; DESC_CH012_SC001_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: identity reference for the secondary visible subject
- image2_asset: lorquas ptomel
- image3_role: environment reference for the scene location
- image3_asset: thark audience chamber

# Continuity Notes
- Scene: CH012_SC001 / SC001.
- Variant: Consistency Repair.
- Carter's posture (defensive vs. proud)
- Presence of weapons or ceremonial items in audience_chamber
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH012\CH012_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH012\CH012_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH012\CH012_SC001\SH001\DIALOGUE.json
