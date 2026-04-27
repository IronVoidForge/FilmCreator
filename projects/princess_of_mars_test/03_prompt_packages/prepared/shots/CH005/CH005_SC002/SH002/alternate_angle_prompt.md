# Title
SH002 Shot Prompt - Alternate Angle

# ID
CH005_SC002_SH002_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for sola. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for captive chamber murals. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. A caregiver provides food and heavy furs to a naked captive as the environment darkens. The subject from image1 is food containers, foreground inside resting zone, hand size vs container, facing directly toward camera, containers held near protagonist. The subject from image2 is food containers plays against protagonist in the same frame. Preserve the environment from image3 Interior cell containing a sleeping area, a Watch Dog is positioned at the threshold., monumental scale, dry open Martian terrain, especially resting zone. Keep one readable subject anchor: sola's hands moving. close-up, eye level, portrait lens, locked off, shallow subject, low key night. Detail composition centered on the key physical action or prop inside. close up of cheese and milk. resting zone. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH005_SC002; SHOT_INDEX; DIALOGUE; protagonist; sola
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: portrait
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
- scene_id: CH005_SC002
- chapter_id: CH005
- shot_type: insert_detail
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Tight detail framing focused on a single visual object or gesture.
- composition: Detail composition centered on the key physical action or prop inside captive_chamber_murals.
- shot_size: close_up
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: low_key_night
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front
- visible_primary_subject_id: sola
- visible_secondary_subject_ids: protagonist
- primary_subject_frame_position: foreground inside resting zone
- primary_subject_scale_relation: hand size vs container
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: containers held near protagonist
- subject_relation_summary: food containers plays against protagonist in the same frame
- scene_short_description: A caregiver provides food and heavy furs to a naked captive as the environment darkens.
- shot_moment_summary: close up of cheese and milk
- required_environment_anchor_1: resting zone
- required_subject_anchor_1: sola's hands moving
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: hand size vs container
- camera_package_description: close-up, eye level, portrait lens, locked off, shallow subject, low key night
- environment_subzone: resting zone
- prompt_family: shot_prompt
- reference_asset_ids: sola; protagonist; captive_chamber_murals; DESC_CH005_SC002; DESC_CH005_SC002_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: sola
- image2_role: identity reference for the secondary visible subject
- image2_asset: protagonist
- image3_role: environment reference for the scene location
- image3_asset: captive chamber murals

# Continuity Notes
- Scene: CH005_SC002 / SC002.
- Variant: Alternate Angle.
- Food and plant milk levels in containers
- Volume and placement of furs used to cover protagonist
- Lighting transition from dusk to cold Martian night
- Provision of food and drink
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH005\CH005_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH005\CH005_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH005\CH005_SC002\SH002\DIALOGUE.json
