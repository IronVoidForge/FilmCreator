# Title
SH003 Shot Prompt - Primary Keyframe

# ID
CH011_SC002_SH003_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for dejah thoris. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for ancient opulent quarters. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. Characters move into opulent ancient apartments overlooking a vast plaza. The subject from image1 is dejah thoris, foreground inside plaza view threshold, Massive scale of ancient marble architecture vs intimate character proximity, front three-quarter right toward the scene action, Dejah listening. The subject from image2 is dejah thoris plays against john carter in the same frame. Preserve the environment from image3 monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, broad processional paths and stairs, especially plaza view threshold. Keep one readable subject anchor: tight focus on faces. close-up, eye level, portrait lens, locked off, shallow subject, soft even. Intimate composition that isolates, against to capture the beat's emotional turn. Dejah Thoris explains Martian telescopes. plaza view threshold. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH011_SC002; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris; sola
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: portrait
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
- scene_id: CH011_SC002
- chapter_id: CH011
- shot_type: reaction_closeup
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates dejah_thoris, john_carter against ancient_opulent_quarters to capture the beat's emotional turn.
- shot_size: close_up
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: soft_even
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: front_three_quarter_right
- visible_primary_subject_id: dejah_thoris
- visible_secondary_subject_ids: john_carter
- primary_subject_frame_position: foreground inside plaza_view_threshold
- primary_subject_scale_relation: Massive scale of ancient marble architecture vs intimate character proximity.
- primary_subject_facing_direction: front three-quarter right toward the scene action
- primary_subject_pose_description: Dejah listening
- subject_relation_summary: dejah_thoris plays against john_carter in the same frame
- scene_short_description: Characters move into opulent ancient apartments overlooking a vast plaza.
- shot_moment_summary: Dejah Thoris explains Martian telescopes
- required_environment_anchor_1: plaza_view_threshold
- required_subject_anchor_1: tight focus on faces
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: Massive scale of ancient marble architecture vs intimate character proximity.
- camera_package_description: close-up, eye level, portrait lens, locked off, shallow subject, soft even
- environment_subzone: plaza_view_threshold
- prompt_family: shot_prompt
- reference_asset_ids: dejah_thoris; john_carter; ancient_opulent_quarters; DESC_CH011_SC002; DESC_CH011_SC002_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: dejah thoris
- image2_role: identity reference for the secondary visible subject
- image2_asset: john carter
- image3_role: environment reference for the scene location
- image3_asset: ancient opulent quarters

# Continuity Notes
- Scene: CH011_SC002 / SC002.
- Variant: Primary Keyframe.
- Transition from harsh exterior lighting to soft, luxurious interior lighting
- Character placement within the new quarters relative to the plaza view
- The revelation of Earth
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH011\CH011_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH011\CH011_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH011\CH011_SC002\SH003\DIALOGUE.json
