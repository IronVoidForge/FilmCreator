# Title
SH003 Shot Prompt - Alternate Angle

# ID
CH026_SC003_SH003_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for john carter. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for helium plains. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. Allied forces launch a coordinated multi-pronged charge across open plains to crush remaining Zodangan resistance. The subject from image1 is john carter, tars tarkas, foreground inside central battlefield, Massive scale disparity between the advancing allied lines and the depleting Zodangan ranks, front three-quarter right toward the scene action, clash of blades. The subject from image2 is john carter, tars tarkas plays against tars tarkas in the same frame. Preserve the environment from image3 Wide, expansive flats surrounding the capital, level enough for transit and mass movement., monumental scale, dry open Martian terrain, especially central battlefield. medium-close, eye level, normal lens, handheld, shallow subject, high contrast ceremonial. Intimate composition that isolates, against to capture the beat's emotional turn. Close combat between riders and infantry. central battlefield. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH026_SC003; SHOT_INDEX; DIALOGUE; john_carter; tars_tarkas
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: normal
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
- scene_id: CH026_SC003
- chapter_id: CH026
- shot_type: reaction_closeup
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates john_carter, tars_tarkas against helium_plains to capture the beat's emotional turn.
- shot_size: medium_close
- camera_angle: eye_level
- camera_motion: handheld
- zoom_behavior: none
- focus_strategy: shallow_subject
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_right
- visible_primary_subject_id: john_carter
- visible_secondary_subject_ids: tars_tarkas
- primary_subject_frame_position: foreground inside central battlefield
- primary_subject_scale_relation: Massive scale disparity between the advancing allied lines and the depleting Zodangan ranks.
- primary_subject_facing_direction: front three-quarter right toward the scene action
- primary_subject_pose_description: clash of blades
- subject_relation_summary: john_carter, tars_tarkas plays against tars_tarkas in the same frame
- scene_short_description: Allied forces launch a coordinated multi-pronged charge across open plains to crush remaining Zodangan resistance.
- shot_moment_summary: Close combat between riders and infantry
- required_environment_anchor_1: central battlefield
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: Massive scale disparity between the advancing allied lines and the depleting Zodangan ranks.
- camera_package_description: medium-close, eye level, normal lens, handheld, shallow subject, high contrast ceremonial
- environment_subzone: central battlefield
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; tars_tarkas; helium_plains; DESC_CH026_SC003; DESC_CH026_SC003_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: john carter
- image2_role: identity reference for the secondary visible subject
- image2_asset: tars tarkas
- image3_role: environment reference for the scene location
- image3_asset: helium plains

# Continuity Notes
- Scene: CH026_SC003 / SC003.
- Variant: Alternate Angle.
- Movement of the multi-pronged assault lines
- The density of the Zodangan ranks as they are depleted
- Decisive Destruction
- Resolve Thark Warriors -> Thark Warriors
- Resolve Heliumite Soldiers -> Heliumite Soldiers
- Resolve Zodangan Army -> Zodangan Army
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH026\CH026_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH026\CH026_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH026\CH026_SC003\SH003\DIALOGUE.json
