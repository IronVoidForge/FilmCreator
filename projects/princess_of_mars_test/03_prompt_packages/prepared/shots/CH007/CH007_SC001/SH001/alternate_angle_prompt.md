# Title
SH001 Shot Prompt - Alternate Angle

# ID
CH007_SC001_SH001_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for sola. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for dead sea bottom. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. A massive procession of decorated chariots travels across a desert floor toward an incubator site. The subject from image1 is various Martian warriors/drivers, midground inside dead sea bottom, 250 chariots and enormous beasts relative to protagonist size, profile left toward the scene action, wide vista. The subject from image2 is various Martian warriors/drivers plays against protagonist in the same frame. Preserve the environment from image3 monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, broad processional paths and stairs, especially dead sea bottom valley floor. 250 chariots drawn by enormous beasts relative to the protagonist's size. wide, eye level, ultra-wide lens, pan, deep focus, diffuse ambient. Wide composition across placed for immediate spatial orientation. massive cavalcade moving across the valley. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH007_SC001; SHOT_INDEX; DIALOGUE; protagonist; sola; lorquas_ptomel_jed
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: ultra_wide
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: alternate_angle
- review_notes: Prompt body is missing the required subject anchor for an on-screen shot.
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH007_SC001
- chapter_id: CH007
- shot_type: establishing_wide
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across dead_sea_bottom with various Martian warriors/drivers, sola, protagonist placed for immediate spatial orientation.
- shot_size: wide
- camera_angle: eye_level
- camera_motion: pan
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: profile_left
- visible_primary_subject_id: sola
- visible_secondary_subject_ids: protagonist
- primary_subject_frame_position: midground inside dead_sea_bottom
- primary_subject_scale_relation: 250 chariots and enormous beasts relative to protagonist size
- primary_subject_facing_direction: profile left toward the scene action
- primary_subject_pose_description: wide vista
- subject_relation_summary: various Martian warriors/drivers plays against protagonist in the same frame
- scene_short_description: A massive procession of decorated chariots travels across a desert floor toward an incubator site.
- shot_moment_summary: massive cavalcade moving across the valley
- required_environment_anchor_1: dead_sea_bottom valley floor
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: 250 chariots drawn by enormous beasts relative to the protagonist's size
- camera_package_description: wide, eye level, ultra-wide lens, pan, deep focus, diffuse ambient
- environment_subzone: dead_sea_bottom
- prompt_family: shot_prompt
- reference_asset_ids: sola; protagonist; dead_sea_bottom; DESC_CH007_SC001; DESC_CH007_SC001_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: sola
- image2_role: identity reference for the secondary visible subject
- image2_asset: protagonist
- image3_role: environment reference for the scene location
- image3_asset: dead sea bottom

# Continuity Notes
- Scene: CH007_SC001 / SC001.
- Variant: Alternate Angle.
- Chariot decoration patterns must remain consistent
- Physical height ratio between enormous beasts and protagonist
- Chariot decoration patterns must remain consistent across wide and medium shots
- Sequential order of chariot jump obstacles
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH007\CH007_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH007\CH007_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH007\CH007_SC001\SH001\DIALOGUE.json
