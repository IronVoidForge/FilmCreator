# Title
SH003 Shot Prompt - Alternate Angle

# ID
CH018_SC003_SH003_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for dak kova. Use image2 as the environment reference for warhoon subterranean dungeon. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. A massive horde of ten thousand warriors marches across open plains toward a city. The subject from image1 is Warhoon Warriors, midground inside warhoon subterranean dungeon, preserve readable body-to-environment scale in frame, back to camera with head turned toward the action, approaching city entrance. Preserve the environment from image2 Underground prison structure, specific spatial dimensions are unstated., monumental scale, dry open Martian terrain, especially warhoon subterranean dungeon. Keep one readable subject anchor: back to camera with head turned toward the action. diminishing light/increasing darkness. wide, high angle, normal lens, push in, environment priority, low key night. Wide composition across placed for immediate spatial orientation. The horde enters the pitch-black dungeon. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH018_SC003; SHOT_INDEX; DIALOGUE; dak_kova
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: normal
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
- scene_id: CH018_SC003
- chapter_id: CH018
- shot_type: establishing_wide
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across warhoon_subterranean_dungeon with Warhoon Warriors, dak_kova placed for immediate spatial orientation.
- shot_size: wide
- camera_angle: high_angle
- camera_motion: push_in
- zoom_behavior: none
- focus_strategy: environment_priority
- lighting_style: low_key_night
- subject_visibility: silhouette
- narration_mode: none
- primary_subject_angle: back
- visible_primary_subject_id: dak_kova
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: midground inside warhoon_subterranean_dungeon
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: back to camera with head turned toward the action
- primary_subject_pose_description: approaching city entrance
- subject_relation_summary: Warhoon Warriors carries the frame alone
- scene_short_description: A massive horde of ten thousand warriors marches across open plains toward a city.
- shot_moment_summary: The horde enters the pitch-black dungeon
- required_environment_anchor_1: warhoon_subterranean_dungeon
- required_subject_anchor_1: back to camera with head turned toward the action
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: diminishing light/increasing darkness
- camera_package_description: wide, high angle, normal lens, push in, environment priority, low key night
- environment_subzone: warhoon_subterranean_dungeon
- prompt_family: shot_prompt
- reference_asset_ids: dak_kova; warhoon_subterranean_dungeon; DESC_CH018_SC003; DESC_CH018_SC003_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: dak kova
- image2_role: environment reference for the scene location
- image2_asset: warhoon subterranean dungeon

# Continuity Notes
- Scene: CH018_SC003 / SC003.
- Variant: Alternate Angle.
- Consistent direction of travel toward Warhoon city
- Lighting transition from open Martian plains to subterranean darkness
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH018\CH018_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH018\CH018_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH018\CH018_SC003\SH003\DIALOGUE.json
