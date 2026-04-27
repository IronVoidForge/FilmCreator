# Title
SH003 Shot Prompt - Consistency Repair

# ID
CH027_SC001_SH003_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for dejah thoris. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for helium palace sunken gardens. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. A peaceful domestic moment in a lush garden is interrupted by news of a murder and atmospheric collapse. The subject from image1 is dejah thoris, foreground inside helium palace sunken gardens nesting area, Micro-scale intimacy (lovers) vs Macro-scale catastrophe (planetary air pressure), front three-quarter right toward the scene action, shocked expression. The subject from image2 is dejah thoris plays against john carter in the same frame. Preserve the environment from image3 Large-scale terraced gardens with tiered palace terraces, includes royal seating areas and central botanical anchors., monumental scale, dry open Martian terrain. Keep one readable subject anchor: shocked expression. close-up, low angle, portrait lens, handheld, zoom strong in, shallow subject, high contrast ceremonial. Intimate composition that isolates, against to capture the beat's emotional turn. realization of air pressure drop. nesting area. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH027_SC001; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris; tardos_mors
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: portrait
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: consistency_repair
- review_notes: SH003: environment anchor is typed like a subject/celestial detail instead of a set anchor.
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH027_SC001
- chapter_id: CH027
- shot_type: reaction_closeup
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates dejah_thoris, john_carter against helium_palace_sunken_gardens to capture the beat's emotional turn.
- shot_size: close_up
- camera_angle: low_angle
- camera_motion: handheld
- zoom_behavior: strong_in
- focus_strategy: shallow_subject
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: front_three_quarter_right
- visible_primary_subject_id: dejah_thoris
- visible_secondary_subject_ids: john_carter
- primary_subject_frame_position: foreground inside helium_palace_sunken_gardens_nesting_area
- primary_subject_scale_relation: Micro-scale intimacy (lovers) vs Macro-scale catastrophe (planetary air pressure).
- primary_subject_facing_direction: front three-quarter right toward the scene action
- primary_subject_pose_description: shocked expression
- subject_relation_summary: dejah_thoris plays against john_carter in the same frame
- scene_short_description: A peaceful domestic moment in a lush garden is interrupted by news of a murder and atmospheric collapse.
- shot_moment_summary: realization of air pressure drop
- required_environment_anchor_1: helium_palace_sunken_gardens_nesting_area
- required_subject_anchor_1: shocked expression
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: Micro-scale intimacy (lovers) vs Macro-scale catastrophe (planetary air pressure).
- camera_package_description: close-up, low angle, portrait lens, handheld, zoom strong in, shallow subject, high contrast ceremonial
- environment_subzone: helium_palace_sunken_gardens_nesting_area
- prompt_family: shot_prompt
- reference_asset_ids: dejah_thoris; john_carter; helium_palace_sunken_gardens; DESC_CH027_SC001; DESC_CH027_SC001_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: dejah thoris
- image2_role: identity reference for the secondary visible subject
- image2_asset: john carter
- image3_role: environment reference for the scene location
- image3_asset: helium palace sunken gardens

# Continuity Notes
- Scene: CH027_SC001 / SC001.
- Variant: Consistency Repair.
- Transition from relaxed lover postures to sudden royal council tension
- Realization of the atmospheric catastrophe and plummeting pressure
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH027\CH027_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH027\CH027_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH027\CH027_SC001\SH003\DIALOGUE.json
