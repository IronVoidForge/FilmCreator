# Title
SH003 Shot Prompt - Primary Keyframe

# ID
CH013_SC002_SH003_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for lorquas ptomel. Use image2 as the environment reference for green martian city complex. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. A massive assembly of green warriors prepares for a march under two moons. The subject from image1 is Green Martian Horde, foreground right within green martian city complex assembly plaza, individual faces in crowd, facing directly toward camera, ceremony concludes. Preserve the environment from image2 Features wide thoroughfares, central leadership hubs, and large-scale enclosures/pens for beasts., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially green martian city complex assembly plaza. medium, eye level, normal lens, handheld, shallow subject, low key night. Closing composition in that emphasizes the consequence of communal recognition. Warriors reacting to the honor. assembly plaza. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH013_SC002; SHOT_INDEX; DIALOGUE; john_carter; lorquas_ptomel
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: normal
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: primary_keyframe
- review_notes: Prompt body is missing the required subject anchor for an on-screen shot.
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH013_SC002
- chapter_id: CH013
- shot_type: closing_reaction
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Controlled closing frame that lands the consequence of the beat.
- composition: Closing composition in green_martian_city_complex that emphasizes the consequence of communal recognition.
- shot_size: medium
- camera_angle: eye_level
- camera_motion: handheld
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: low_key_night
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front
- visible_primary_subject_id: lorquas_ptomel
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground right within green_martian_city_complex_assembly_plaza
- primary_subject_scale_relation: individual faces in crowd
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: ceremony concludes
- subject_relation_summary: Green Martian Horde carries the frame alone
- scene_short_description: A massive assembly of green warriors prepares for a march under two moons.
- shot_moment_summary: Warriors reacting to the honor
- required_environment_anchor_1: green_martian_city_complex_assembly_plaza
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: individual faces in crowd
- camera_package_description: medium, eye level, normal lens, handheld, shallow subject, low key night
- environment_subzone: green_martian_city_complex_assembly_plaza
- prompt_family: shot_prompt
- reference_asset_ids: lorquas_ptomel; green_martian_city_complex; DESC_CH013_SC002; DESC_CH013_SC002_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: lorquas ptomel
- image2_role: environment reference for the scene location
- image2_asset: green martian city complex

# Continuity Notes
- Scene: CH013_SC002 / SC002.
- Variant: Primary Keyframe.
- Presence and placement of the gold anklet on john_carter
- Readiness level/equipment state of the Green Martian Horde troops
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH013\CH013_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH013\CH013_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH013\CH013_SC002\SH003\DIALOGUE.json
