# Title
SH001 Shot Prompt - Consistency Repair

# ID
CH014_SC002_SH001_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for warhoon incubator site. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. A party discovers a Warhoon incubator containing green eggs before it is violently destroyed. The subject from image1 is green martian eggs, foreground inside incubator site, egg size relative to incubator walls, facing directly toward camera, eggs resting still. The subject from image2 is green martian eggs plays against tars tarkas in the same frame. Preserve the environment from image3 Contains specialized incubation chambers for biological preservation., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially incubator site. extreme-close-up, eye level, portrait lens, locked off, shallow subject, diffuse ambient. Intimate composition that isolates, against to capture the beat's emotional turn. close up of green eggs inside the incubator. incubator site. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH014_SC002; SHOT_INDEX; DIALOGUE; john_carter; tars_tarkas; sarkoja; dejah_thoris
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: portrait
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
- scene_id: CH014_SC002
- chapter_id: CH014
- shot_type: reaction_closeup
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates john_carter, tars_tarkas against warhoon_incubator_site to capture the beat's emotional turn.
- shot_size: extreme_close_up
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: tars_tarkas
- primary_subject_frame_position: foreground inside incubator_site
- primary_subject_scale_relation: egg size relative to incubator walls
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: eggs resting still
- subject_relation_summary: green_martian_eggs plays against tars_tarkas in the same frame
- scene_short_description: A party discovers a Warhoon incubator containing green eggs before it is violently destroyed.
- shot_moment_summary: close up of green eggs inside the incubator
- required_environment_anchor_1: incubator_site
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: egg size relative to incubator walls
- camera_package_description: extreme-close-up, eye level, portrait lens, locked off, shallow subject, diffuse ambient
- environment_subzone: incubator_site
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; tars_tarkas; warhoon_incubator_site; DESC_CH014_SC002; DESC_CH014_SC002_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: identity reference for the secondary visible subject
- image2_asset: tars tarkas
- image3_role: environment reference for the scene location
- image3_asset: warhoon incubator site

# Continuity Notes
- Scene: CH014_SC002 / SC002.
- Variant: Consistency Repair.
- Incubator state transition (intact to destroyed)
- Debris pattern consistency post-destruction
- Discovery of the Warhoon incubator and green eggs
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH014\CH014_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH014\CH014_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH014\CH014_SC002\SH001\DIALOGUE.json
