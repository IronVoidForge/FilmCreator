# Title
SH001 Shot Prompt - Alternate Angle

# ID
CH023_SC001_SH001_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for zodanga urban complex. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. Two men meet in shadows near a massive urban complex to devise a desperate assassination and escape plan. The subject from image1 is john carter, midground inside zodanga urban complex periphery, Small scale human conspiracy set against the vast, isolated backdrop of the Zodanga outskirts, front three-quarter left toward the scene action, distant figures approaching. The subject from image2 is john carter plays against kantos kan in the same frame. Preserve the environment from image3 Dense urban layout with significant vertical scale, dominated by massive barracks and palace towers creating deep canyons., monumental scale, dry open Martian terrain, especially zodanga urban complex periphery. Keep one readable subject anchor: zodanga urban complex silhouette. wide, eye level, wide lens, locked off, deep focus, low key night. Wide composition across placed for immediate spatial orientation. Wide shot of the two figures meeting in the dark. periphery. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH023_SC001; SHOT_INDEX; DIALOGUE; john_carter; kantos_kan
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: wide
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: alternate_angle
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH023_SC001
- chapter_id: CH023
- shot_type: establishing_wide
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across zodanga_urban_complex with john_carter, kantos_kan placed for immediate spatial orientation.
- shot_size: wide
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: low_key_night
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_left
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: kantos_kan
- primary_subject_frame_position: midground inside zodanga_urban_complex periphery
- primary_subject_scale_relation: Small scale human conspiracy set against the vast, isolated backdrop of the Zodanga outskirts.
- primary_subject_facing_direction: front three-quarter left toward the scene action
- primary_subject_pose_description: distant figures approaching
- subject_relation_summary: john_carter plays against kantos_kan in the same frame
- scene_short_description: Two men meet in shadows near a massive urban complex to devise a desperate assassination and escape plan.
- shot_moment_summary: Wide shot of the two figures meeting in the dark
- required_environment_anchor_1: zodanga_urban_complex periphery
- required_subject_anchor_1: zodanga_urban_complex silhouette
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: Small scale human conspiracy set against the vast, isolated backdrop of the Zodanga outskirts.
- camera_package_description: wide, eye level, wide lens, locked off, deep focus, low key night
- environment_subzone: zodanga_urban_complex periphery
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; kantos_kan; zodanga_urban_complex; DESC_CH023_SC001; DESC_CH023_SC001_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: identity reference for the secondary visible subject
- image2_asset: kantos kan
- image3_role: environment reference for the scene location
- image3_asset: zodanga urban complex

# Continuity Notes
- Scene: CH023_SC001 / SC001.
- Variant: Alternate Angle.
- Nighttime lighting levels and shadow density
- Character proximity and relative positioning during planning
- Reaction to the betrothal news
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH023\CH023_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH023\CH023_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH023\CH023_SC001\SH001\DIALOGUE.json
