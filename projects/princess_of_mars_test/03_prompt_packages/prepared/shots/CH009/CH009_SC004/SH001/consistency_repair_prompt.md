# Title
SH001 Shot Prompt - Consistency Repair

# ID
CH009_SC004_SH001_consistency_repair_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for protagonist. Use image2 as the environment reference for communal sleeping quarters. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships. A protagonist listens from the shadows as Martian adults discuss an impending execution. The subject from image1 is protagonist, foreground inside shadow zone, protagonist size relative to shadow depth, profile left toward the scene action, protagonist still. Preserve the environment from image2 monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, broad processional paths and stairs, especially shadow zone. close-up, eye level, portrait lens, locked off, shallow subject, low key night. Intimate composition that isolates, against to capture the beat's emotional turn. protagonist listening to distant voices. shadow zone. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH009_SC004; SHOT_INDEX; DIALOGUE; protagonist; sarkoja
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: portrait
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
- scene_id: CH009_SC004
- chapter_id: CH009
- shot_type: reaction_closeup
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates protagonist, Other Martians (voices) against communal_sleeping_quarters to capture the beat's emotional turn.
- shot_size: close_up
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: low_key_night
- subject_visibility: partial
- narration_mode: in_scene_speaker
- primary_subject_angle: profile_left
- visible_primary_subject_id: protagonist
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground inside shadow_zone
- primary_subject_scale_relation: protagonist size relative to shadow depth
- primary_subject_facing_direction: profile left toward the scene action
- primary_subject_pose_description: protagonist still
- subject_relation_summary: protagonist carries the frame alone
- scene_short_description: A protagonist listens from the shadows as Martian adults discuss an impending execution.
- shot_moment_summary: protagonist listening to distant voices
- required_environment_anchor_1: shadow_zone
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: protagonist size relative to shadow depth
- camera_package_description: close-up, eye level, portrait lens, locked off, shallow subject, low key night
- environment_subzone: shadow_zone
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; communal_sleeping_quarters; DESC_CH009_SC004; DESC_CH009_SC004_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: protagonist
- image2_role: environment reference for the scene location
- image2_asset: communal sleeping quarters

# Continuity Notes
- Scene: CH009_SC004 / SC004.
- Variant: Consistency Repair.
- Dialogue regarding Thark, execution, and Tal Hajus must be audibly distinct
- Protagonist remains in a listening/eavesdropping position throughout the revelation
- Resolve Other Martians (voices) -> Other Martians (voices)
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH009\CH009_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH009\CH009_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH009\CH009_SC004\SH001\DIALOGUE.json
