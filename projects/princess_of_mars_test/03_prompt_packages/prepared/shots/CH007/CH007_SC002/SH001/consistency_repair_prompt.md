# Title
SH001 Shot Prompt - Consistency Repair

# ID
CH007_SC002_SH001_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for sola. Use image2 as the environment reference for the incubator enclosure. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. A ritualized capture of three-to-four-foot hatchlings emerging from an incubator enclosure. The subject from image1 is Newly Hatched Martians, foreground inside egg cluster zone, 3-4ft hatchling size vs egg, facing directly toward camera, still eggs. Preserve the environment from image2 Walled perimeter enclosing a central egg-hatching zone and a communal gathering area., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially egg cluster zone. close-up, eye level, portrait lens, locked off, shallow subject, high contrast ceremonial. Intimate composition that ites, against to capture the beat's emotional turn. eggs begin to crack and vibrate. egg cluster zone. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH007_SC002; SHOT_INDEX; DIALOGUE; protagonist; sola
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
- scene_id: CH007_SC002
- chapter_id: CH007
- shot_type: reaction_closeup
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Close framing that ites reaction and emotional emphasis.
- composition: Intimate composition that isolates Newly Hatched Martians, sola against the_incubator_enclosure to capture the beat's emotional turn.
- shot_size: close_up
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front
- visible_primary_subject_id: sola
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground inside egg_cluster_zone
- primary_subject_scale_relation: 3-4ft hatchling size vs egg
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: still eggs
- subject_relation_summary: Newly Hatched Martians carries the frame alone
- scene_short_description: A ritualized capture of three-to-four-foot hatchlings emerging from an incubator enclosure.
- shot_moment_summary: eggs begin to crack and vibrate
- required_environment_anchor_1: egg_cluster_zone
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: 3-4ft hatchling size vs egg
- camera_package_description: close-up, eye level, portrait lens, locked off, shallow subject, high contrast ceremonial
- environment_subzone: egg_cluster_zone
- prompt_family: shot_prompt
- reference_asset_ids: sola; the_incubator_enclosure; DESC_CH007_SC002; DESC_CH007_SC002_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: sola
- image2_role: environment reference for the scene location
- image2_asset: the incubator enclosure

# Continuity Notes
- Scene: CH007_SC002 / SC002.
- Variant: Consistency Repair.
- Physical size of Newly Hatched Martians (3 to 4 feet tall)
- The cracking of the eggs
- Movement patterns and rhythm of the gauntlet
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH007\CH007_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH007\CH007_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH007\CH007_SC002\SH001\DIALOGUE.json
