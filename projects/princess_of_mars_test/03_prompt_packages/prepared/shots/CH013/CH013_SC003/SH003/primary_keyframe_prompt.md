# Title
SH003 Shot Prompt - Primary Keyframe

# ID
CH013_SC003_SH003_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for sola. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for martian night plaza. Use image4 as the identity reference for an additional visible subject. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. A reunion in a Martian plaza under two moons turns into a revelation of sabotage. The subject from image1 is sola, foreground right within martian night plaza center, preserve readable body-to-environment scale in frame, profile left toward the scene action, Sola speaking. The subject from image2 is sola plays against dejah thoris, john carter in the same frame. Preserve the environment from image3 Expansive open spaces with large-scale architecture casting shadows., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially martian night plaza center. medium, eye level, normal lens, locked off, rack focus, low key night. Over-the-shoulder composition in sharing the frame for dialogue or tension. Sola explains the sabotage/labor. center. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH013_SC003; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris; sola
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: normal
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: primary_keyframe
- review_notes: SH003: subject anchor is missing or not body/detail-specific enough.; Prompt body is using a non-body/detail subject anchor.
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH013_SC003
- chapter_id: CH013
- shot_type: over_the_shoulder
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Shoulder-level conversational framing with visible foreground presence.
- composition: Over-the-shoulder composition in martian_night_plaza with sola, dejah_thoris, john_carter sharing the frame for dialogue or tension.
- shot_size: medium
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: none
- focus_strategy: rack_focus
- lighting_style: low_key_night
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: profile_left
- visible_primary_subject_id: sola
- visible_secondary_subject_ids: dejah_thoris; john_carter
- primary_subject_frame_position: foreground right within martian_night_plaza center
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: profile left toward the scene action
- primary_subject_pose_description: Sola speaking
- subject_relation_summary: sola plays against dejah_thoris, john_carter in the same frame
- scene_short_description: A reunion in a Martian plaza under two moons turns into a revelation of sabotage.
- shot_moment_summary: Sola explains the sabotage/labor
- required_environment_anchor_1: martian_night_plaza center
- required_subject_anchor_1: Over-the-shoulder shots between characters
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: preserve readable body-to-environment scale in frame
- camera_package_description: medium, eye level, normal lens, locked off, rack focus, low key night
- environment_subzone: martian_night_plaza center
- prompt_family: shot_prompt
- reference_asset_ids: sola; dejah_thoris; john_carter; martian_night_plaza; DESC_CH013_SC003; DESC_CH013_SC003_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: sola
- image2_role: identity reference for the secondary visible subject
- image2_asset: dejah thoris
- image3_role: environment reference for the scene location
- image3_asset: martian night plaza
- image4_role: identity reference for an additional visible subject
- image4_asset: john carter

# Continuity Notes
- Scene: CH013_SC003 / SC003.
- Variant: Primary Keyframe.
- Dejah Thoris physical signs of fatigue and labor (sweat, grime, exhaustion)
- Proximity of Sola to Dejah
- Revelation of the sabotage and radium labor
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH013\CH013_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH013\CH013_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH013\CH013_SC003\SH003\DIALOGUE.json
