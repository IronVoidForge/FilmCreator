# Title
SH002 Shot Prompt - Consistency Repair

# ID
CH027_SC001_SH002_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for tardos mors. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for helium palace sunken gardens. Use image4 as the identity reference for an additional visible subject. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. A peaceful domestic moment in a lush garden is interrupted by news of a murder and atmospheric collapse. The subject from image1 is Human male of high status., Elder., lean but durable soldier's frame, Ruler status implied, foreground right within helium palace sunken gardens flora, sudden distance change, facing directly toward camera, peaceful garden. The subject from image2 is tardos mors plays against john carter, dejah thoris in the same frame. Preserve the environment from image3 Large-scale terraced gardens with tiered palace terraces, includes royal seating areas and central botanical anchors., monumental scale, dry open Martian terrain. medium, eye level, normal lens, handheld, rack focus, hard directional. Readable medium composition in featuring. tardos mors delivers news of murder. flora. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH027_SC001; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris; tardos_mors
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: normal
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: consistency_repair
- review_notes: SH002: environment anchor is typed like a subject/celestial detail instead of a set anchor.; Prompt body is missing the required subject anchor for an on-screen shot.
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH027_SC001
- chapter_id: CH027
- shot_type: medium
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in helium_palace_sunken_gardens featuring tardos_mors, john_carter, dejah_thoris.
- shot_size: medium
- camera_angle: eye_level
- camera_motion: handheld
- zoom_behavior: none
- focus_strategy: rack_focus
- lighting_style: hard_directional
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: front
- visible_primary_subject_id: tardos_mors
- visible_secondary_subject_ids: john_carter; dejah_thoris
- primary_subject_frame_position: foreground right within helium_palace_sunken_gardens_flora
- primary_subject_scale_relation: sudden distance change
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: peaceful garden
- subject_relation_summary: tardos_mors plays against john_carter, dejah_thoris in the same frame
- scene_short_description: A peaceful domestic moment in a lush garden is interrupted by news of a murder and atmospheric collapse.
- shot_moment_summary: tardos_mors delivers news of murder
- required_environment_anchor_1: helium_palace_sunken_gardens_flora
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: sudden distance change
- camera_package_description: medium, eye level, normal lens, handheld, rack focus, hard directional
- environment_subzone: helium_palace_sunken_gardens_flora
- prompt_family: shot_prompt
- reference_asset_ids: tardos_mors; john_carter; dejah_thoris; helium_palace_sunken_gardens; DESC_CH027_SC001; DESC_CH027_SC001_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: tardos mors
- image2_role: identity reference for the secondary visible subject
- image2_asset: john carter
- image3_role: environment reference for the scene location
- image3_asset: helium palace sunken gardens
- image4_role: identity reference for an additional visible subject
- image4_asset: dejah thoris

# Continuity Notes
- Scene: CH027_SC001 / SC001.
- Variant: Consistency Repair.
- Transition from relaxed lover postures to sudden royal council tension
- News of the Keeper's murder arrives via Tardos Mors
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH027\CH027_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH027\CH027_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH027\CH027_SC001\SH002\DIALOGUE.json
