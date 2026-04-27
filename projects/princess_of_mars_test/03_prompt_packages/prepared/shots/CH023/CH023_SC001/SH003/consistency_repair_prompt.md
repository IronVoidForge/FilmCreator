# Title
SH003 Shot Prompt - Consistency Repair

# ID
CH023_SC001_SH003_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for zodanga urban complex. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. Two men meet in shadows near a massive urban complex to devise a desperate assassination and escape plan. The subject from image1 is john carter, foreground inside secluded shadow pocket, Small scale human conspiracy set against the vast, isolated backdrop of the Zodanga outskirts, front three-quarter right toward the scene action, desperate expression. The subject from image2 is john carter plays against kantos kan in the same frame. Preserve the environment from image3 Dense urban layout with significant vertical scale, dominated by massive barracks and palace towers creating deep canyons., monumental scale, dry open Martian terrain, especially secluded shadow pocket. Keep one readable subject anchor: desperate expression. close-up, eye level, portrait lens, locked off, shallow subject, low key night. Intimate composition that isolates, against to capture the beat's emotional turn. Close up on Carter's face showing resolve. secluded shadow pocket. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH023_SC001; SHOT_INDEX; DIALOGUE; john_carter; kantos_kan
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: portrait
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: consistency_repair
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH023_SC001
- chapter_id: CH023
- shot_type: reaction_closeup
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates john_carter, kantos_kan against zodanga_urban_complex to capture the beat's emotional turn.
- shot_size: close_up
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: low_key_night
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: front_three_quarter_right
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: kantos_kan
- primary_subject_frame_position: foreground inside secluded shadow pocket
- primary_subject_scale_relation: Small scale human conspiracy set against the vast, isolated backdrop of the Zodanga outskirts.
- primary_subject_facing_direction: front three-quarter right toward the scene action
- primary_subject_pose_description: desperate expression
- subject_relation_summary: john_carter plays against kantos_kan in the same frame
- scene_short_description: Two men meet in shadows near a massive urban complex to devise a desperate assassination and escape plan.
- shot_moment_summary: Close up on Carter's face showing resolve
- required_environment_anchor_1: secluded shadow pocket
- required_subject_anchor_1: desperate expression
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: Small scale human conspiracy set against the vast, isolated backdrop of the Zodanga outskirts.
- camera_package_description: close-up, eye level, portrait lens, locked off, shallow subject, low key night
- environment_subzone: secluded shadow pocket
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; kantos_kan; zodanga_urban_complex; DESC_CH023_SC001; DESC_CH023_SC001_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: identity reference for the secondary visible subject
- image2_asset: kantos kan
- image3_role: environment reference for the scene location
- image3_asset: zodanga urban complex

# Continuity Notes
- Scene: CH023_SC001 / SC001.
- Variant: Consistency Repair.
- Nighttime lighting levels and shadow density
- Character proximity and relative positioning during planning
- Commitment to action
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH023\CH023_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH023\CH023_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH023\CH023_SC001\SH003\DIALOGUE.json
