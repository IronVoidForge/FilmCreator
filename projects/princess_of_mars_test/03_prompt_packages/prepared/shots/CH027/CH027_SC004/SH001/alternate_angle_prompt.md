# Title
SH001 Shot Prompt - Alternate Angle

# ID
CH027_SC004_SH001_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the environment reference for helium palace sunken gardens. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. A stripped air-scout machine flies through turbulent, thinning atmosphere toward a distant plant. The subject from image1 is john carter, foreground inside Air-scout Machine cockpit, preserve readable body-to-environment scale in frame, front three-quarter left toward the scene action, John grabbing a component. Preserve the environment from image2 Large-scale terraced gardens with tiered palace terraces, includes royal seating areas and central botanical anchors., monumental scale, dry open Martian terrain, especially Air-scout Machine cockpit. medium-close, eye level, normal lens, handheld, shallow subject, hard directional. Intimate composition that isolates against to capture the beat's emotional turn. John Carter stripping parts from the machine. Air-scout Machine cockpit. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH027_SC004; SHOT_INDEX; DIALOGUE; john_carter
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: normal
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: alternate_angle
- review_notes: Environment reference conflict: prompt variables align more with `none` than bound `helium_palace_sunken_gardens`.; Prompt body is missing the required subject anchor for an on-screen shot.
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH027_SC004
- chapter_id: CH027
- shot_type: reaction_closeup
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates john_carter against helium_palace_sunken_gardens to capture the beat's emotional turn.
- shot_size: medium_close
- camera_angle: eye_level
- camera_motion: handheld
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: hard_directional
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_left
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground inside Air-scout Machine cockpit
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: front three-quarter left toward the scene action
- primary_subject_pose_description: John grabbing a component
- subject_relation_summary: john_carter carries the frame alone
- scene_short_description: A stripped air-scout machine flies through turbulent, thinning atmosphere toward a distant plant.
- shot_moment_summary: John Carter stripping parts from the machine
- required_environment_anchor_1: Air-scout Machine cockpit
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: preserve readable body-to-environment scale in frame
- camera_package_description: medium-close, eye level, normal lens, handheld, shallow subject, hard directional
- environment_subzone: Air-scout Machine cockpit
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; helium_palace_sunken_gardens; DESC_CH027_SC004; DESC_CH027_SC004_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: environment reference for the scene location
- image2_asset: helium palace sunken gardens

# Continuity Notes
- Scene: CH027_SC004 / SC004.
- Variant: Alternate Angle.
- Machine must show progressively removed components/stripped weight
- John Carter exhibits increasing respiratory struggle/difficulty breathing
- Stripping the machine of weight
- Resolve The sky over Barsoom -> The sky over Barsoom
- Resolve Air-scout Machine -> Air-scout Machine
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH027\CH027_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH027\CH027_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH027\CH027_SC004\SH001\DIALOGUE.json
