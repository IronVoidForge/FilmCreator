# Title
SH001 Shot Prompt - Alternate Angle

# ID
CH016_SC004_SH001_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the environment reference for dejah thoris quarters. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. An agile infiltrator climbs into marble quarters only to overhear a devastating betrayal. The subject from image1 is john carter, midground inside inner courts, height relative to courtyard floor, profile right toward the scene action, climbing motion. Preserve the environment from image2 Multi-story vertical scale with winding stairs and high-ceilinged spaces, includes balconies/windows facing outward toward a plaza., monumental scale, dry open Martian terrain, especially inner courts. wide, high angle, wide lens, track, deep focus, low key night. Wide composition across placed for immediate spatial orientation. Carter scaling the architecture. inner courts. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH016_SC004; SHOT_INDEX; DIALOGUE; john_carter
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: wide
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
- scene_id: CH016_SC004
- chapter_id: CH016
- shot_type: establishing_wide
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across dejah_thoris_quarters with john_carter placed for immediate spatial orientation.
- shot_size: wide
- camera_angle: high_angle
- camera_motion: track
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: low_key_night
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: profile_right
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: midground inside inner_courts
- primary_subject_scale_relation: height relative to courtyard floor
- primary_subject_facing_direction: profile right toward the scene action
- primary_subject_pose_description: climbing motion
- subject_relation_summary: john_carter carries the frame alone
- scene_short_description: An agile infiltrator climbs into marble quarters only to overhear a devastating betrayal.
- shot_moment_summary: Carter scaling the architecture
- required_environment_anchor_1: inner_courts
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: height relative to courtyard floor
- camera_package_description: wide, high angle, wide lens, track, deep focus, low key night
- environment_subzone: inner_courts
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; dejah_thoris_quarters; DESC_CH016_SC004; DESC_CH016_SC004_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: environment reference for the scene location
- image2_asset: dejah thoris quarters

# Continuity Notes
- Scene: CH016_SC004 / SC004.
- Variant: Alternate Angle.
- Carter's physical proximity to door and window thresholds
- Audio synchronization of overheard dialogue from off-screen
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH016\CH016_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH016\CH016_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH016\CH016_SC004\SH001\DIALOGUE.json
