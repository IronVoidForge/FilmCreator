# Title
SH002 Shot Prompt - Primary Keyframe

# ID
CH026_SC003_SH002_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the environment reference for helium plains. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. Allied forces launch a coordinated multi-pronged charge across open plains to crush remaining Zodangan resistance. The visible subject is midground inside central battlefield, Massive scale disparity between the advancing allied lines and the depleting Zodangan ranks, profile left toward the scene action, charge in motion. Preserve the environment from image1 Wide, expansive flats surrounding the capital, level enough for transit and mass movement., monumental scale, dry open Martian terrain, especially central battlefield. wide, low angle, wide lens, track, deep focus, hard directional. Dynamic composition in clear pursuit vectors and readable movement. The multi-pronged charge hits the Zodangan lines. central battlefield. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH026_SC003; SHOT_INDEX; DIALOGUE; john_carter; tars_tarkas
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: wide
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: primary_keyframe
- review_notes: SH002: visible primary subject id is missing for an on-screen shot.
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH026_SC003
- chapter_id: CH026
- shot_type: action
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: Dynamic composition in helium_plains with clear pursuit vectors and readable movement for Thark Warriors, Heliumite Soldiers, Zodangan Army.
- shot_size: wide
- camera_angle: low_angle
- camera_motion: track
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: hard_directional
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: profile_left
- visible_primary_subject_id: (none)
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: midground inside central battlefield
- primary_subject_scale_relation: Massive scale disparity between the advancing allied lines and the depleting Zodangan ranks.
- primary_subject_facing_direction: profile left toward the scene action
- primary_subject_pose_description: charge in motion
- subject_relation_summary: Thark Warriors, Heliumite Soldiers carries the frame alone
- scene_short_description: Allied forces launch a coordinated multi-pronged charge across open plains to crush remaining Zodangan resistance.
- shot_moment_summary: The multi-pronged charge hits the Zodangan lines
- required_environment_anchor_1: central battlefield
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: Massive scale disparity between the advancing allied lines and the depleting Zodangan ranks.
- camera_package_description: wide, low angle, wide lens, track, deep focus, hard directional
- environment_subzone: central battlefield
- prompt_family: shot_prompt
- reference_asset_ids: helium_plains; DESC_CH026_SC003; DESC_CH026_SC003_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: environment reference for the scene location
- image1_asset: helium plains

# Continuity Notes
- Scene: CH026_SC003 / SC003.
- Variant: Primary Keyframe.
- Movement of the multi-pronged assault lines
- The density of the Zodangan ranks as they are depleted
- The Multi-Pronged Charge
- Resolve Thark Warriors -> Thark Warriors
- Resolve Heliumite Soldiers -> Heliumite Soldiers
- Resolve Zodangan Army -> Zodangan Army
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH026\CH026_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH026\CH026_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH026\CH026_SC003\SH002\DIALOGUE.json
