# Title
SH002 Shot Prompt - Alternate Angle

# ID
CH017_SC002_SH002_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for dejah thoris. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for mossy waste. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. A small group on mounts traverses a vast, trackless expanse of mossy terrain. The subject from image1 is Dejah Thoris, foreground inside mossy waste track, Tiny character silhouettes against an immense, featureless horizon, front three-quarter left toward the scene action, medium shot of mount. The subject from image2 is Dejah Thoris plays against sola in the same frame. Preserve the environment from image3 Vast horizon, endless mossy plains, no visible landmarks., monumental scale, especially mossy waste track. Keep one readable subject anchor: slumped postures on thoats. Keep celestial anchor The physical toll of starvation and dehydration sets in stable in the frame. close-up, eye level, portrait lens, track, zoom subtle in, shallow subject, diffuse ambient. Intimate composition that ites, against to capture the beat's emotional turn. close up of parched lips and weary eyes. track. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH017_SC002; SHOT_INDEX; DIALOGUE; dejah_thoris; sola; woola
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: portrait
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: alternate_angle
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH017_SC002
- chapter_id: CH017
- shot_type: reaction_closeup
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Close framing that ites reaction and emotional emphasis.
- composition: Intimate composition that isolates dejah_thoris, sola against mossy_waste to capture the beat's emotional turn.
- shot_size: close_up
- camera_angle: eye_level
- camera_motion: track
- zoom_behavior: subtle_in
- focus_strategy: shallow_subject
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_left
- visible_primary_subject_id: dejah_thoris
- visible_secondary_subject_ids: sola
- primary_subject_frame_position: foreground inside mossy_waste_track
- primary_subject_scale_relation: Tiny character silhouettes against an immense, featureless horizon.
- primary_subject_facing_direction: front three-quarter left toward the scene action
- primary_subject_pose_description: medium shot of mount
- subject_relation_summary: Dejah Thoris plays against sola in the same frame
- scene_short_description: A small group on mounts traverses a vast, trackless expanse of mossy terrain.
- shot_moment_summary: close up of parched lips and weary eyes
- required_environment_anchor_1: mossy_waste_track
- required_subject_anchor_1: slumped postures on thoats
- required_celestial_anchor_1: The physical toll of starvation and dehydration sets in
- required_scale_proof_detail: Tiny character silhouettes against an immense, featureless horizon.
- camera_package_description: close-up, eye level, portrait lens, track, zoom subtle in, shallow subject, diffuse ambient
- environment_subzone: mossy_waste_track
- prompt_family: shot_prompt
- reference_asset_ids: dejah_thoris; sola; mossy_waste; DESC_CH017_SC002; DESC_CH017_SC002_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: dejah thoris
- image2_role: identity reference for the secondary visible subject
- image2_asset: sola
- image3_role: environment reference for the scene location
- image3_asset: mossy waste

# Continuity Notes
- Scene: CH017_SC002 / SC002.
- Variant: Alternate Angle.
- Physical condition and exhaustion level of the thoats
- Depletion levels of group supplies (food/water)
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH017\CH017_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH017\CH017_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH017\CH017_SC002\SH002\DIALOGUE.json
