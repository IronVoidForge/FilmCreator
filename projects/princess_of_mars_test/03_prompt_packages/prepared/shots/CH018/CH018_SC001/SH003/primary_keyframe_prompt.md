# Title
SH003 Shot Prompt - Primary Keyframe

# ID
CH018_SC001_SH003_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for protagonist. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for martian plains march route. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. A wounded man regains consciousness in a camp before being bound to a beast for transport. The subject from image1 is protagonist, midground inside martian plains march route, preserve readable body-to-environment scale in frame, profile right toward the scene action, straps tightening. The subject from image2 is An ancient, ugly Warhoon woman., Ancient / Elderly, lean athletic build, Warhoon culture/setting, protagonist plays against female healer in the same frame. Preserve the environment from image3 Vast, open plains suitable for epic military marches., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially martian plains march route. wide shot showing landscape vs beast. wide, low angle, ultra-wide lens, track, deep focus, diffuse ambient. Wide composition across placed for immediate spatial orientation. wide view of transport. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH018_SC001; SHOT_INDEX; DIALOGUE; protagonist; female_healer
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: ultra_wide
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: primary_keyframe
- review_notes: Prompt body is missing the required subject anchor for an on-screen shot.
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH018_SC001
- chapter_id: CH018
- shot_type: establishing_wide
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across martian_plains_march_route with protagonist, female_healer, Warhoon Warriors (background) placed for immediate spatial orientation.
- shot_size: wide
- camera_angle: low_angle
- camera_motion: track
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: profile_right
- visible_primary_subject_id: protagonist
- visible_secondary_subject_ids: female_healer
- primary_subject_frame_position: midground inside martian_plains_march_route
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: profile right toward the scene action
- primary_subject_pose_description: straps tightening
- subject_relation_summary: protagonist plays against female_healer in the same frame
- scene_short_description: A wounded man regains consciousness in a camp before being bound to a beast for transport.
- shot_moment_summary: wide view of transport
- required_environment_anchor_1: martian_plains_march_route
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: wide shot showing landscape vs beast
- camera_package_description: wide, low angle, ultra-wide lens, track, deep focus, diffuse ambient
- environment_subzone: martian_plains_march_route
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; female_healer; martian_plains_march_route; DESC_CH018_SC001; DESC_CH018_SC001_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: protagonist
- image2_role: identity reference for the secondary visible subject
- image2_asset: female healer
- image3_role: environment reference for the scene location
- image3_asset: martian plains march route

# Continuity Notes
- Scene: CH018_SC001 / SC001.
- Variant: Primary Keyframe.
- Wound placement and severity on naked protagonist
- Binding/strap tension and configuration to the thoat
- Securing for transport
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH018\CH018_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH018\CH018_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH018\CH018_SC001\SH003\DIALOGUE.json
