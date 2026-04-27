# Title
SH002 Shot Prompt - Primary Keyframe

# ID
CH020_SC002_SH002_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the old man. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for atmosphere factory. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. A traveler enters a massive industrial factory and meets a deceptive host amidst heavy machinery. The subject from image1 is An elderly, solitary guardian., Elderly., lean athletic build, decisive, efficient movement, foreground right within central machinery hub, preserve readable body-to-environment scale in frame, front three-quarter right toward the scene action, the old man standing still. The subject from image2 is the old man plays against john carter in the same frame. Preserve the environment from image3 Massive scale featuring a central core of machinery and towering doors., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially central machinery hub. Keep one readable subject anchor: standing face-to-face. medium, eye level, normal lens, locked off, shallow subject, diffuse ambient. Over-the-shoulder composition in sharing the frame for dialogue or tension. the old man greets carter hospitably. central machinery hub. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH020_SC002; SHOT_INDEX; DIALOGUE; john_carter; the_old_man
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
- scene_id: CH020_SC002
- chapter_id: CH020
- shot_type: over_the_shoulder
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Shoulder-level conversational framing with visible foreground presence.
- composition: Over-the-shoulder composition in atmosphere_factory with the_old_man, john_carter sharing the frame for dialogue or tension.
- shot_size: medium
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: front_three_quarter_right
- visible_primary_subject_id: the_old_man
- visible_secondary_subject_ids: john_carter
- primary_subject_frame_position: foreground right within central_machinery_hub
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: front three-quarter right toward the scene action
- primary_subject_pose_description: the_old_man standing still
- subject_relation_summary: the_old_man plays against john_carter in the same frame
- scene_short_description: A traveler enters a massive industrial factory and meets a deceptive host amidst heavy machinery.
- shot_moment_summary: the old man greets carter hospitably
- required_environment_anchor_1: central_machinery_hub
- required_subject_anchor_1: standing face-to-face
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: preserve readable body-to-environment scale in frame
- camera_package_description: medium, eye level, normal lens, locked off, shallow subject, diffuse ambient
- environment_subzone: central_machinery_hub
- prompt_family: shot_prompt
- reference_asset_ids: the_old_man; john_carter; atmosphere_factory; DESC_CH020_SC002; DESC_CH020_SC002_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: the old man
- image2_role: identity reference for the secondary visible subject
- image2_asset: john carter
- image3_role: environment reference for the scene location
- image3_asset: atmosphere factory

# Continuity Notes
- Scene: CH020_SC002 / SC002.
- Variant: Primary Keyframe.
- Diadem presence and exact placement
- Shifting light patterns within industrial machinery zones
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH020\CH020_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH020\CH020_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH020\CH020_SC002\SH002\DIALOGUE.json
