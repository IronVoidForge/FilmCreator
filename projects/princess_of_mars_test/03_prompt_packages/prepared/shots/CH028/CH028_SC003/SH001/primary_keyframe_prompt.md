# Title
SH001 Shot Prompt - Primary Keyframe

# ID
CH028_SC003_SH001_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the environment reference for arizona desert landscape. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. A man emerges from a dark cave into the blinding, vast expanse of the Arizona desert. The subject from image1 is john carter, foreground entry line within cave interior, contrast of dark silhouette against bright opening, back to camera with head turned toward the action, darkness. Preserve the environment from image2 monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, broad processional paths and stairs, especially cave interior. medium-full, eye level, wide lens, push in, shallow subject, low key night. Wide composition across placed for immediate spatial orientation. subject moves toward the cave mouth. cave interior. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH028_SC003; SHOT_INDEX; DIALOGUE; john_carter
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: wide
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: primary_keyframe
- review_notes: SH001: subject anchor is missing or not body/detail-specific enough.; Prompt body is using a non-body/detail subject anchor.
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH028_SC003
- chapter_id: CH028
- shot_type: establishing_wide
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across arizona_desert_landscape with john_carter placed for immediate spatial orientation.
- shot_size: medium_full
- camera_angle: eye_level
- camera_motion: push_in
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: low_key_night
- subject_visibility: silhouette
- narration_mode: none
- primary_subject_angle: back
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground entry line within cave interior
- primary_subject_scale_relation: contrast of dark silhouette against bright opening
- primary_subject_facing_direction: back to camera with head turned toward the action
- primary_subject_pose_description: darkness
- subject_relation_summary: john_carter carries the frame alone
- scene_short_description: A man emerges from a dark cave into the blinding, vast expanse of the Arizona desert.
- shot_moment_summary: subject moves toward the cave mouth
- required_environment_anchor_1: cave interior
- required_subject_anchor_1: cave mouth
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: contrast of dark silhouette against bright opening
- camera_package_description: medium-full, eye level, wide lens, push in, shallow subject, low key night
- environment_subzone: cave interior
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; arizona_desert_landscape; DESC_CH028_SC003; DESC_CH028_SC003_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: environment reference for the scene location
- image2_asset: arizona desert landscape

# Continuity Notes
- Scene: CH028_SC003 / SC003.
- Variant: Primary Keyframe.
- Rapid exposure shift from dark cave to high-key desert sunlight
- Physical state and clothing condition of john_carter post-cave exit
- Movement toward the light
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH028\CH028_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH028\CH028_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH028\CH028_SC003\SH001\DIALOGUE.json
