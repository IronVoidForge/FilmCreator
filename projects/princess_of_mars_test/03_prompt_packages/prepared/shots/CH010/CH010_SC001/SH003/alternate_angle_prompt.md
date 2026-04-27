# Title
SH003 Shot Prompt - Alternate Angle

# ID
CH010_SC001_SH003_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for woola. Use image2 as the identity reference for the secondary visible subject. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. An Earthman uses affection to command a large Martian hound within his living quarters. The subject from image1 is woola, foreground right within Carter's confinement area/living quarters, woola's size vs john carter's physical stature, facing directly toward camera, contact established. The subject from image2 is woola plays against john carter in the same frame. Preserve described environment with stable spatial continuity. Keep one readable subject anchor: woola relaxes posture near john carter. medium, eye level, normal lens, locked off, deep focus, soft even. Closing composition in that emphasizes the consequence of. woola submits to the bond. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH010_SC001; SHOT_INDEX; DIALOGUE; john_carter; woola
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: normal
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: alternate_angle
- review_notes: Prompt body is missing an environment image role for a bound environment.; SH003: environment clause still contains generic filler.
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH010_SC001
- chapter_id: CH010
- shot_type: closing_reaction
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Controlled closing frame that lands the consequence of the beat.
- composition: Closing composition in Carter's confinement area/living quarters that emphasizes the consequence of establishment of undisputed mastery.
- shot_size: medium
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: soft_even
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front
- visible_primary_subject_id: woola
- visible_secondary_subject_ids: john_carter
- primary_subject_frame_position: foreground right within Carter's confinement area/living quarters
- primary_subject_scale_relation: woola's size vs john_carter's physical stature.
- primary_subject_facing_direction: facing directly toward camera
- primary_subject_pose_description: contact established
- subject_relation_summary: woola plays against john_carter in the same frame
- scene_short_description: An Earthman uses affection to command a large Martian hound within his living quarters.
- shot_moment_summary: woola submits to the bond
- required_environment_anchor_1: Carter's confinement area/living quarters
- required_subject_anchor_1: woola relaxes posture near john_carter
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: woola's size vs john_carter's physical stature.
- camera_package_description: medium, eye level, normal lens, locked off, deep focus, soft even
- environment_subzone: Carter's confinement area/living quarters
- prompt_family: shot_prompt
- reference_asset_ids: woola; john_carter; DESC_CH010_SC001; DESC_CH010_SC001_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: woola
- image2_role: identity reference for the secondary visible subject
- image2_asset: john carter

# Continuity Notes
- Scene: CH010_SC001 / SC001.
- Variant: Alternate Angle.
- Physical positioning of woola relative to john_carter
- Specific tactile methods (touch) and vocal tones used by john_carter
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH010\CH010_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH010\CH010_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH010\CH010_SC001\SH003\DIALOGUE.json
