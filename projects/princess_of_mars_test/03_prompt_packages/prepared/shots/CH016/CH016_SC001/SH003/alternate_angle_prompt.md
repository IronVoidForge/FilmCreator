# Title
SH003 Shot Prompt - Alternate Angle

# ID
CH016_SC001_SH003_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for dejah thoris. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for dejah thoris quarters. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. A weary traveler enters a massive city plaza to find long-awaited companionship. The subject from image1 is dejah thoris, foreground inside Great Plaza of Thark, Architecture dwarfs the human-sized characters to emphasize Thark's magnitude, facing directly toward camera, Carter seeing them. The subject from image2 is dejah thoris plays against john carter in the same frame. Preserve the environment from image3 Multi-story vertical scale with winding stairs and high-ceilinged spaces, includes balconies/windows facing outward toward a plaza., monumental scale, dry open Martian terrain, especially Great Plaza of Thark. medium-close, eye level, portrait lens, push in, zoom subtle in, shallow subject, soft even. Intimate composition that isolates, against to capture the beat's emotional turn. Carter reunites with Dejah Thoris and Sola. Great Plaza of Thark. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH016_SC001; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris; sola
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: portrait
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
- scene_id: CH016_SC001
- chapter_id: CH016
- shot_type: reaction_closeup
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates dejah_thoris, john_carter against dejah_thoris_quarters to capture the beat's emotional turn.
- shot_size: medium_close
- camera_angle: eye_level
- camera_motion: push_in
- zoom_behavior: subtle_in
- focus_strategy: shallow_subject
- lighting_style: soft_even
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: front
- visible_primary_subject_id: dejah_thoris
- visible_secondary_subject_ids: john_carter
- primary_subject_frame_position: foreground inside Great Plaza of Thark
- primary_subject_scale_relation: Architecture dwarfs the human-sized characters to emphasize Thark's magnitude.
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: Carter seeing them
- subject_relation_summary: dejah_thoris plays against john_carter in the same frame
- scene_short_description: A weary traveler enters a massive city plaza to find long-awaited companionship.
- shot_moment_summary: Carter reunites with Dejah Thoris and Sola
- required_environment_anchor_1: Great Plaza of Thark
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: Architecture dwarfs the human-sized characters to emphasize Thark's magnitude.
- camera_package_description: medium-close, eye level, portrait lens, push in, zoom subtle in, shallow subject, soft even
- environment_subzone: Great Plaza of Thark
- prompt_family: shot_prompt
- reference_asset_ids: dejah_thoris; john_carter; dejah_thoris_quarters; DESC_CH016_SC001; DESC_CH016_SC001_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: dejah thoris
- image2_role: identity reference for the secondary visible subject
- image2_asset: john carter
- image3_role: environment reference for the scene location
- image3_asset: dejah thoris quarters

# Continuity Notes
- Scene: CH016_SC001 / SC001.
- Variant: Alternate Angle.
- Travel-worn clothing and dirtied appearance for john_carter and companions
- Massive architectural scale relative to character height
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH016\CH016_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH016\CH016_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH016\CH016_SC001\SH003\DIALOGUE.json
