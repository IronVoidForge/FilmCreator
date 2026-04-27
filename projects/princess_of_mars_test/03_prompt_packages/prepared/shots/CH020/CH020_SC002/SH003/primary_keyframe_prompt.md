# Title
SH003 Shot Prompt - Primary Keyframe

# ID
CH020_SC002_SH003_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the environment reference for atmosphere factory. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. A traveler enters a massive industrial factory and meets a deceptive host amidst heavy machinery. The subject from image1 is diadem, foreground right within central machinery hub, extreme detail of stone, facing directly toward camera, diadem obscured. Preserve the environment from image2 Massive scale featuring a central core of machinery and towering doors., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially central machinery hub. Keep one readable subject anchor: static, tense posture. insert-detail, eye level, telephoto lens, locked off, shallow subject, hard directional. Detail composition centered on the key physical action or prop inside. macro shot of the Ninth Ray diadem. central machinery hub. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH020_SC002; SHOT_INDEX; DIALOGUE; john_carter; the_old_man
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: telephoto
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
- shot_type: insert_detail
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Tight detail framing focused on a single visual object or gesture.
- composition: Detail composition centered on the key physical action or prop inside atmosphere_factory.
- shot_size: insert_detail
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: hard_directional
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground right within central_machinery_hub
- primary_subject_scale_relation: extreme detail of stone
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: diadem obscured
- subject_relation_summary: diadem carries the frame alone
- scene_short_description: A traveler enters a massive industrial factory and meets a deceptive host amidst heavy machinery.
- shot_moment_summary: macro shot of the Ninth Ray diadem
- required_environment_anchor_1: central_machinery_hub
- required_subject_anchor_1: static, tense posture
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: extreme detail of stone
- camera_package_description: insert-detail, eye level, telephoto lens, locked off, shallow subject, hard directional
- environment_subzone: central_machinery_hub
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; atmosphere_factory; DESC_CH020_SC002; DESC_CH020_SC002_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: environment reference for the scene location
- image2_asset: atmosphere factory

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
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH020\CH020_SC002\SH003\DIALOGUE.json
