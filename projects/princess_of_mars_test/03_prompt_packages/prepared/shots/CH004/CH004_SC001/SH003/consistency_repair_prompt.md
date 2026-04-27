# Title
SH003 Shot Prompt - Consistency Repair

# ID
CH004_SC001_SH003_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the environment reference for ancient martian city ruins. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. A duo traverses a massive white marble city inlaid with gold while observing callous Martian crowds. The visible subject is foreground inside Grand Streets, Architecture and Martians are oversized relative to the narrator, profile left toward the scene action, close up on tusk. Preserve the environment from image1 monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, broad processional paths and stairs, especially Grand Streets. close-up, eye level, portrait lens, locked off, shallow subject, high contrast ceremonial. Detail composition centered on the key physical action or prop inside. Close observation of Martian biology. Grand Streets. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH004_SC001; SHOT_INDEX; DIALOGUE; tars_tarkas
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: portrait
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: consistency_repair
- review_notes: SH003: visible primary subject id is missing for an on-screen shot.
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH004_SC001
- chapter_id: CH004
- shot_type: insert_detail
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Tight detail framing focused on a single visual object or gesture.
- composition: Detail composition centered on the key physical action or prop inside ancient_martian_city_ruins.
- shot_size: close_up
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: internal_monologue
- primary_subject_angle: profile_left
- visible_primary_subject_id: (none)
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground inside Grand Streets
- primary_subject_scale_relation: Architecture and Martians are oversized relative to the narrator.
- primary_subject_facing_direction: profile left toward the scene action
- primary_subject_pose_description: close up on tusk
- subject_relation_summary: Martian_crowd carries the frame alone
- scene_short_description: A duo traverses a massive white marble city inlaid with gold while observing callous Martian crowds.
- shot_moment_summary: Close observation of Martian biology
- required_environment_anchor_1: Grand Streets
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: Architecture and Martians are oversized relative to the narrator.
- camera_package_description: close-up, eye level, portrait lens, locked off, shallow subject, high contrast ceremonial
- environment_subzone: Grand Streets
- prompt_family: shot_prompt
- reference_asset_ids: ancient_martian_city_ruins; DESC_CH004_SC001; DESC_CH004_SC001_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: environment reference for the scene location
- image1_asset: ancient martian city ruins

# Continuity Notes
- Scene: CH004_SC001 / SC001.
- Variant: Consistency Repair.
- Scale comparison between narrator and oversized architecture/Martians
- Lighting consistency in the open plaza
- Observing Martian culture/biology
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH004\CH004_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH004\CH004_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH004\CH004_SC001\SH003\DIALOGUE.json
