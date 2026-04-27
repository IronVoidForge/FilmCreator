# Title
SH002 Shot Prompt - Consistency Repair

# ID
CH016_SC002_SH002_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for sola. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for dejah thoris quarters. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. Intimate declaration of devotion shifts into frantic midnight escape planning within a plaza building. The subject from image1 is sola, foreground inside private seating/intimate area, preserve readable body-to-environment scale in frame, profile left toward the scene action, sola entering frame. The subject from image2 is sola plays against dejah thoris in the same frame. Preserve the environment from image3 Multi-story vertical scale with winding stairs and high-ceilinged spaces, includes balconies/windows facing outward toward a plaza., monumental scale, dry open Martian terrain, especially doorway. medium-close, eye level, normal lens, locked off, rack focus, low key night. Intimate composition that ites, against to capture the beat's emotional turn. Sola breaks news of death sentence. private seating/intimate area. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH016_SC002; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris; sola
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
- scene_id: CH016_SC002
- chapter_id: CH016
- shot_type: reaction_closeup
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Close framing that ites reaction and emotional emphasis.
- composition: Intimate composition that isolates sola, dejah_thoris against dejah_thoris_quarters to capture the beat's emotional turn.
- shot_size: medium_close
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: none
- focus_strategy: rack_focus
- lighting_style: low_key_night
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: profile_left
- visible_primary_subject_id: sola
- visible_secondary_subject_ids: dejah_thoris
- primary_subject_frame_position: foreground inside private seating/intimate area
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: profile left toward the scene action
- primary_subject_pose_description: sola entering frame
- subject_relation_summary: sola plays against dejah_thoris in the same frame
- scene_short_description: Intimate declaration of devotion shifts into frantic midnight escape planning within a plaza building.
- shot_moment_summary: Sola breaks news of death sentence
- required_environment_anchor_1: doorway
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: preserve readable body-to-environment scale in frame
- camera_package_description: medium-close, eye level, normal lens, locked off, rack focus, low key night
- environment_subzone: private seating/intimate area
- prompt_family: shot_prompt
- reference_asset_ids: sola; dejah_thoris; dejah_thoris_quarters; DESC_CH016_SC002; DESC_CH016_SC002_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: sola
- image2_role: identity reference for the secondary visible subject
- image2_asset: dejah thoris
- image3_role: environment reference for the scene location
- image3_asset: dejah thoris quarters

# Continuity Notes
- Scene: CH016_SC002 / SC002.
- Variant: Consistency Repair.
- Lighting levels transitioning from dusk toward night
- Character positioning relative to maps or architectural layouts
- Sola delivers news of Sarkoja's manipulation and death sentence
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH016\CH016_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH016\CH016_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH016\CH016_SC002\SH002\DIALOGUE.json
