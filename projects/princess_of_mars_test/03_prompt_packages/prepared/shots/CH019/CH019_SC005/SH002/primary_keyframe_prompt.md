# Title
SH002 Shot Prompt - Primary Keyframe

# ID
CH019_SC005_SH002_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the environment reference for warhoon eastern hills. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. A man slips through dark shadows toward distant hills while a figure claims freedom in the background. The subject from image1 is john carter, foreground right within Dark outskirts, Large scale transition from localized arena perimeter to expansive eastern hill landscape, profile left toward the scene action, low crouch in dark. Preserve the environment from image2 Functions as an escape route or transit corridor., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially Dark outskirts. medium-full, eye level, normal lens, track, shallow subject, low key night. Readable medium composition in featuring. carter slips through shadows. Dark outskirts. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH019_SC005; SHOT_INDEX; DIALOGUE; john_carter; kantos_kan
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
- scene_id: CH019_SC005
- chapter_id: CH019
- shot_type: medium
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in warhoon_eastern_hills featuring john_carter.
- shot_size: medium_full
- camera_angle: eye_level
- camera_motion: track
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: low_key_night
- subject_visibility: partial
- narration_mode: none
- primary_subject_angle: profile_left
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground right within Dark outskirts
- primary_subject_scale_relation: Large scale transition from localized arena perimeter to expansive eastern hill landscape.
- primary_subject_facing_direction: profile left toward the scene action
- primary_subject_pose_description: low crouch in dark
- subject_relation_summary: john_carter carries the frame alone
- scene_short_description: A man slips through dark shadows toward distant hills while a figure claims freedom in the background.
- shot_moment_summary: carter slips through shadows
- required_environment_anchor_1: Dark outskirts
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: Large scale transition from localized arena perimeter to expansive eastern hill landscape.
- camera_package_description: medium-full, eye level, normal lens, track, shallow subject, low key night
- environment_subzone: Dark outskirts
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; warhoon_eastern_hills; DESC_CH019_SC005; DESC_CH019_SC005_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: environment reference for the scene location
- image2_asset: warhoon eastern hills

# Continuity Notes
- Scene: CH019_SC005 / SC005.
- Variant: Primary Keyframe.
- Lighting consistency between moonlight and torchlight sources
- Physical condition of john_carter (injuries from previous scenes)
- Carter moves through the dark outskirts
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH019\CH019_SC005.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH019\CH019_SC005\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH019\CH019_SC005\SH002\DIALOGUE.json
