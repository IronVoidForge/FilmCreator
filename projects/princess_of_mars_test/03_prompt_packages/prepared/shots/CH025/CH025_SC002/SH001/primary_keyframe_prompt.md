# Title
SH001 Shot Prompt - Primary Keyframe

# ID
CH025_SC002_SH001_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for dejah thoris. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for audience chamber. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. A formal ceremony is violently interrupted by a man smashing through a window and leaping into the hall. The subject from image1 is dejah thoris, foreground inside ritual center, Large scale audience chamber vs single intruder, front three-quarter right toward the scene action, solemn ritual movement. The subject from image2 is dejah thoris plays against sab than in the same frame. Preserve the environment from image3 monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, broad processional paths and stairs, especially ritual center. medium-close, eye level, portrait lens, locked off, shallow subject, high contrast ceremonial. Intimate composition that isolates, against to capture the beat's emotional turn. Dejah being bound by golden chains. ritual center. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH025_SC002; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris; sab_than; than_kosis
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
- scene_id: CH025_SC002
- chapter_id: CH025
- shot_type: reaction_closeup
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates dejah_thoris, sab_than against audience_chamber to capture the beat's emotional turn.
- shot_size: medium_close
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_right
- visible_primary_subject_id: dejah_thoris
- visible_secondary_subject_ids: sab_than
- primary_subject_frame_position: foreground inside ritual_center
- primary_subject_scale_relation: Large scale audience chamber vs single intruder.
- primary_subject_facing_direction: front three-quarter right toward the scene action
- primary_subject_pose_description: solemn ritual movement
- subject_relation_summary: dejah_thoris plays against sab_than in the same frame
- scene_short_description: A formal ceremony is violently interrupted by a man smashing through a window and leaping into the hall.
- shot_moment_summary: Dejah being bound by golden chains
- required_environment_anchor_1: ritual_center
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: Large scale audience chamber vs single intruder.
- camera_package_description: medium-close, eye level, portrait lens, locked off, shallow subject, high contrast ceremonial
- environment_subzone: ritual_center
- prompt_family: shot_prompt
- reference_asset_ids: dejah_thoris; sab_than; audience_chamber; DESC_CH025_SC002; DESC_CH025_SC002_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: dejah thoris
- image2_role: identity reference for the secondary visible subject
- image2_asset: sab than
- image3_role: environment reference for the scene location
- image3_asset: audience chamber

# Continuity Notes
- Scene: CH025_SC002 / SC002.
- Variant: Primary Keyframe.
- Broken state of golden chains
- Scattered glass shards on floor
- Dejah Thoris ceremonial attire integrity
- Solemn binding ceremony
- Resolve Zodangan Nobility/Guards -> Zodangan Nobility/Guards
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH025\CH025_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH025\CH025_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH025\CH025_SC002\SH001\DIALOGUE.json
