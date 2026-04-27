# Title
SH002 Shot Prompt - Consistency Repair

# ID
CH027_SC003_SH002_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for helium palace sunken gardens. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. A dying woman slips into unconsciousness while a man experiences a sudden, intense mental breakthrough. The subject from image1 is john carter, foreground inside helium palace sunken gardens, preserve readable body-to-environment scale in frame, facing directly toward camera, staring blankly. The subject from image2 is john carter plays against dejah thoris in the same frame. Preserve the environment from image3 Large-scale terraced gardens with tiered palace terraces, includes royal seating areas and central botanical anchors., monumental scale, dry open Martian terrain. Keep one readable subject anchor: john carter's eyes. extreme-close-up, eye level, portrait lens, push in, zoom subtle in, shallow subject, high contrast ceremonial. Intimate composition that isolates, against to capture the beat's emotional turn. Sudden mental breakthrough and recall of thought waves. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH027_SC003; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: portrait
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: consistency_repair
- review_notes: SH002: environment anchor is typed like a subject/celestial detail instead of a set anchor.
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH027_SC003
- chapter_id: CH027
- shot_type: reaction_closeup
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates john_carter, dejah_thoris against helium_palace_sunken_gardens to capture the beat's emotional turn.
- shot_size: extreme_close_up
- camera_angle: eye_level
- camera_motion: push_in
- zoom_behavior: subtle_in
- focus_strategy: shallow_subject
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: dejah_thoris
- primary_subject_frame_position: foreground inside helium_palace_sunken_gardens
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: staring blankly
- subject_relation_summary: john_carter plays against dejah_thoris in the same frame
- scene_short_description: A dying woman slips into unconsciousness while a man experiences a sudden, intense mental breakthrough.
- shot_moment_summary: Sudden mental breakthrough and recall of thought waves
- required_environment_anchor_1: helium_palace_sunken_gardens
- required_subject_anchor_1: john_carter's eyes
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: preserve readable body-to-environment scale in frame
- camera_package_description: extreme-close-up, eye level, portrait lens, push in, zoom subtle in, shallow subject, high contrast ceremonial
- environment_subzone: helium_palace_sunken_gardens
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; dejah_thoris; helium_palace_sunken_gardens; DESC_CH027_SC003; DESC_CH027_SC003_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: identity reference for the secondary visible subject
- image2_asset: dejah thoris
- image3_role: environment reference for the scene location
- image3_asset: helium palace sunken gardens

# Continuity Notes
- Scene: CH027_SC003 / SC003.
- Variant: Consistency Repair.
- Precise synchronization of Dejah Thoris coma onset with John Carter's mental epiphany
- John Carter experiences mental breakthrough
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH027\CH027_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH027\CH027_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH027\CH027_SC003\SH002\DIALOGUE.json
