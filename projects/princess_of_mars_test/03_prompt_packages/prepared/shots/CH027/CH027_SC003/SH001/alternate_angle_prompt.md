# Title
SH001 Shot Prompt - Alternate Angle

# ID
CH027_SC003_SH001_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for dejah thoris. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for helium palace sunken gardens. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. A dying woman slips into unconsciousness while a man experiences a sudden, intense mental breakthrough. The subject from image1 is dejah thoris, foreground inside helium palace sunken gardens, physical lethargy vs garden scale, front three-quarter left toward the scene action, eyes fluttering. The subject from image2 is dejah thoris plays against john carter in the same frame. Preserve the environment from image3 Large-scale terraced gardens with tiered palace terraces, includes royal seating areas and central botanical anchors., monumental scale, dry open Martian terrain. Keep one readable subject anchor: eyes fluttering. medium-close, eye level, normal lens, locked off, shallow subject, low key night. Intimate composition that isolates, against to capture the beat's emotional turn. Dejah Thoris eyes closing as she slips into coma. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH027_SC003; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: normal
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: alternate_angle
- review_notes: SH001: environment anchor is typed like a subject/celestial detail instead of a set anchor.
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH027_SC003
- chapter_id: CH027
- shot_type: reaction_closeup
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates dejah_thoris, john_carter against helium_palace_sunken_gardens to capture the beat's emotional turn.
- shot_size: medium_close
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: low_key_night
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_left
- visible_primary_subject_id: dejah_thoris
- visible_secondary_subject_ids: john_carter
- primary_subject_frame_position: foreground inside helium_palace_sunken_gardens
- primary_subject_scale_relation: physical lethargy vs garden scale
- primary_subject_facing_direction: front three-quarter left toward the scene action
- primary_subject_pose_description: eyes fluttering
- subject_relation_summary: dejah_thoris plays against john_carter in the same frame
- scene_short_description: A dying woman slips into unconsciousness while a man experiences a sudden, intense mental breakthrough.
- shot_moment_summary: Dejah Thoris eyes closing as she slips into coma
- required_environment_anchor_1: helium_palace_sunken_gardens
- required_subject_anchor_1: eyes fluttering
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: physical lethargy vs garden scale
- camera_package_description: medium-close, eye level, normal lens, locked off, shallow subject, low key night
- environment_subzone: helium_palace_sunken_gardens
- prompt_family: shot_prompt
- reference_asset_ids: dejah_thoris; john_carter; helium_palace_sunken_gardens; DESC_CH027_SC003; DESC_CH027_SC003_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: dejah thoris
- image2_role: identity reference for the secondary visible subject
- image2_asset: john carter
- image3_role: environment reference for the scene location
- image3_asset: helium palace sunken gardens

# Continuity Notes
- Scene: CH027_SC003 / SC003.
- Variant: Alternate Angle.
- Precise synchronization of Dejah Thoris coma onset with John Carter's mental epiphany
- Dejah Thoris slips into a coma
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH027\CH027_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH027\CH027_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH027\CH027_SC003\SH001\DIALOGUE.json
