# Title
SH002 Shot Prompt - Consistency Repair

# ID
CH005_SC005_SH002_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the colossal creature. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for colossal creature lair. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. A man pulls himself onto a ledge before being snatched by a massive ape-like creature. The subject from image1 is the colossal creature, foreground inside windowsill, Human scale vs Colossal predator scale, rear three-quarter left away from camera, protagonist breathing relief. The subject from image2 is the colossal creature plays against protagonist in the same frame. Preserve the environment from image3 Building interior with large windows overlooking a vast valley, high-altitude containment structure., monumental scale, dry open Martian terrain, especially windowsill. medium-close, eye level, wide lens, handheld, rack focus, high contrast ceremonial. Detail composition centered on the key physical action or prop inside. creature hands seize protagonist from behind. windowsill. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH005_SC005; SHOT_INDEX; DIALOGUE; protagonist; the_colossal_creature
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: wide
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: consistency_repair
- review_notes: Prompt body is missing the required subject anchor for an on-screen shot.
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH005_SC005
- chapter_id: CH005
- shot_type: insert_detail
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Tight detail framing focused on a single visual object or gesture.
- composition: Detail composition centered on the key physical action or prop inside colossal_creature_lair.
- shot_size: medium_close
- camera_angle: eye_level
- camera_motion: handheld
- zoom_behavior: none
- focus_strategy: rack_focus
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: rear_three_quarter_left
- visible_primary_subject_id: the_colossal_creature
- visible_secondary_subject_ids: protagonist
- primary_subject_frame_position: foreground inside windowsill
- primary_subject_scale_relation: Human scale vs Colossal predator scale.
- primary_subject_facing_direction: rear three-quarter left away from camera
- primary_subject_pose_description: protagonist breathing relief
- subject_relation_summary: the_colossal_creature plays against protagonist in the same frame
- scene_short_description: A man pulls himself onto a ledge before being snatched by a massive ape-like creature.
- shot_moment_summary: creature hands seize protagonist from behind
- required_environment_anchor_1: windowsill
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: Human scale vs Colossal predator scale.
- camera_package_description: medium-close, eye level, wide lens, handheld, rack focus, high contrast ceremonial
- environment_subzone: windowsill
- prompt_family: shot_prompt
- reference_asset_ids: the_colossal_creature; protagonist; colossal_creature_lair; DESC_CH005_SC005; DESC_CH005_SC005_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: the colossal creature
- image2_role: identity reference for the secondary visible subject
- image2_asset: protagonist
- image3_role: environment reference for the scene location
- image3_asset: colossal creature lair

# Continuity Notes
- Scene: CH005_SC005 / SC005.
- Variant: Consistency Repair.
- Physical contact point between the_colossal_creature and protagonist
- Hand placement during the grip
- Transition from windowsill to interior room floor
- the creature seizes the protagonist
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH005\CH005_SC005.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH005\CH005_SC005\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH005\CH005_SC005\SH002\DIALOGUE.json
