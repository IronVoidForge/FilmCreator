# Title
SH001 Shot Prompt - Primary Keyframe

# ID
CH020_SC001_SH001_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for martian wilderness. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. Exhausted travelers traverse a harsh landscape before discovering a massive concrete industrial structure. The subject from image1 is john carter, foreground entry line within martian wilderness plains, preserve readable body-to-environment scale in frame, profile right toward the scene action, walking. The subject from image2 is john carter plays against woola in the same frame. Preserve the environment from image3 Vast, open scale with scattered patches of flora across desolate plains., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially martian wilderness plains. medium-full, eye level, normal lens, track, shallow subject, diffuse ambient. Wide composition across placed for immediate spatial orientation. Carter trudging through dust. plains. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH020_SC001; SHOT_INDEX; DIALOGUE; john_carter; woola
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
- scene_id: CH020_SC001
- chapter_id: CH020
- shot_type: establishing_wide
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across martian_wilderness with john_carter, woola placed for immediate spatial orientation.
- shot_size: medium_full
- camera_angle: eye_level
- camera_motion: track
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: profile_right
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: woola
- primary_subject_frame_position: foreground entry line within martian_wilderness_plains
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: profile right toward the scene action
- primary_subject_pose_description: walking
- subject_relation_summary: john_carter plays against woola in the same frame
- scene_short_description: Exhausted travelers traverse a harsh landscape before discovering a massive concrete industrial structure.
- shot_moment_summary: Carter trudging through dust
- required_environment_anchor_1: martian_wilderness_plains
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: preserve readable body-to-environment scale in frame
- camera_package_description: medium-full, eye level, normal lens, track, shallow subject, diffuse ambient
- environment_subzone: martian_wilderness_plains
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; woola; martian_wilderness; DESC_CH020_SC001; DESC_CH020_SC001_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: identity reference for the secondary visible subject
- image2_asset: woola
- image3_role: environment reference for the scene location
- image3_asset: martian wilderness

# Continuity Notes
- Scene: CH020_SC001 / SC001.
- Variant: Primary Keyframe.
- Carter's physical grime and exhaustion level
- Woola's post-combat condition
- The grueling trek through the wilderness
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH020\CH020_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH020\CH020_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH020\CH020_SC001\SH001\DIALOGUE.json
