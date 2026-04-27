# Title
SH002 Shot Prompt - Primary Keyframe

# ID
CH013_SC002_SH002_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for lorquas ptomel. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for green martian city complex. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. A massive assembly of green warriors prepares for a march under two moons. The subject from image1 is lorquas ptomel, foreground inside green martian city complex assembly plaza, anklet vs hand size, front three-quarter left toward the scene action, Carter standing before Ptomel. The subject from image2 is lorquas ptomel plays against john carter in the same frame. Preserve the environment from image3 Features wide thoroughfares, central leadership hubs, and large-scale enclosures/pens for beasts., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially green martian city complex assembly plaza. medium-close, eye level, portrait lens, locked off, zoom subtle in, shallow subject, high contrast ceremonial. Intimate composition that isolates, against to capture the beat's emotional turn. Lorquas Ptomel presents the gold anklet. assembly plaza. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH013_SC002; SHOT_INDEX; DIALOGUE; john_carter; lorquas_ptomel
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: portrait
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
- shot_type: reaction_closeup
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates lorquas_ptomel, john_carter against green_martian_city_complex to capture the beat's emotional turn.
- shot_size: medium_close
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: subtle_in
- focus_strategy: shallow_subject
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: front_three_quarter_left
- visible_primary_subject_id: lorquas_ptomel
- visible_secondary_subject_ids: john_carter
- primary_subject_frame_position: foreground inside green_martian_city_complex_assembly_plaza
- primary_subject_scale_relation: anklet vs hand size
- primary_subject_facing_direction: front three-quarter left toward the scene action
- primary_subject_pose_description: Carter standing before Ptomel
- subject_relation_summary: lorquas_ptomel plays against john_carter in the same frame
- scene_short_description: A massive assembly of green warriors prepares for a march under two moons.
- shot_moment_summary: Lorquas Ptomel presents the gold anklet
- required_environment_anchor_1: green_martian_city_complex_assembly_plaza
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: anklet vs hand size
- camera_package_description: medium-close, eye level, portrait lens, locked off, zoom subtle in, shallow subject, high contrast ceremonial
- environment_subzone: green_martian_city_complex_assembly_plaza
- prompt_family: shot_prompt
- reference_asset_ids: lorquas_ptomel; john_carter; green_martian_city_complex; DESC_CH013_SC002; DESC_CH013_SC002_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: lorquas ptomel
- image2_role: identity reference for the secondary visible subject
- image2_asset: john carter
- image3_role: environment reference for the scene location
- image3_asset: green martian city complex

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
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH013\CH013_SC002\SH002\DIALOGUE.json
