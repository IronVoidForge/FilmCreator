# Title
SH002 Shot Prompt - Consistency Repair

# ID
CH016_SC004_SH002_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the environment reference for dejah thoris quarters. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. An agile infiltrator climbs into marble quarters only to overhear a devastating betrayal. The subject from image1 is john carter, foreground right within dejah thoris quarters, body tucked against marble wall, rear three-quarter left away from camera, sliding into frame. Preserve the environment from image2 Multi-story vertical scale with winding stairs and high-ceilinged spaces, includes balconies/windows facing outward toward a plaza., monumental scale, dry open Martian terrain, especially window threshold. medium-full, eye level, normal lens, push in, shallow subject, low key night. Readable medium composition in featuring. Carter entering the room and hiding. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH016_SC004; SHOT_INDEX; DIALOGUE; john_carter
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: normal
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: consistency_repair
- review_notes: Prompt body is missing the required subject anchor for an on-screen shot.
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH016_SC004
- chapter_id: CH016
- shot_type: medium
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in dejah_thoris_quarters featuring john_carter.
- shot_size: medium_full
- camera_angle: eye_level
- camera_motion: push_in
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: low_key_night
- subject_visibility: partial
- narration_mode: none
- primary_subject_angle: rear_three_quarter_left
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground right within dejah_thoris_quarters
- primary_subject_scale_relation: body tucked against marble wall
- primary_subject_facing_direction: rear three-quarter left away from camera
- primary_subject_pose_description: sliding into frame
- subject_relation_summary: john_carter carries the frame alone
- scene_short_description: An agile infiltrator climbs into marble quarters only to overhear a devastating betrayal.
- shot_moment_summary: Carter entering the room and hiding
- required_environment_anchor_1: window threshold
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: body tucked against marble wall
- camera_package_description: medium-full, eye level, normal lens, push in, shallow subject, low key night
- environment_subzone: dejah_thoris_quarters
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; dejah_thoris_quarters; DESC_CH016_SC004; DESC_CH016_SC004_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: environment reference for the scene location
- image2_asset: dejah thoris quarters

# Continuity Notes
- Scene: CH016_SC004 / SC004.
- Variant: Consistency Repair.
- Carter's physical proximity to door and window thresholds
- Audio synchronization of overheard dialogue from off-screen
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH016\CH016_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH016\CH016_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH016\CH016_SC004\SH002\DIALOGUE.json
