# Title
SH003 Shot Prompt - Alternate Angle

# ID
CH005_SC003_SH003_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for protagonist. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for deserted martian cityscape. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. A restless prisoner tests his guard by moving toward a threshold under watchful eyes. The subject from image1 is protagonist, foreground right within chamber threshold, preserve readable body-to-environment scale in frame, rear three-quarter left away from camera, walking toward door. The subject from image2 is [source:C:/FilmCreator MC/projects/princess of mars test/02 story analysis/character breakdowns/chapters/CH005/.md] Physical Description: A ferocious Martian creature with short legs. It is characterized by e., readable production deta, protagonist plays against watch dog in the same frame. Preserve the environment from image3 Wide streets leading to the city edge, significant vertical scale with high window ledges and sills., monumental scale, dry open Martian terrain, especially chamber threshold. medium, eye level, wide lens, handheld, rack focus, hard directional. Closing composition in that emphasizes the consequence of crossing the threshold. protagonist approaches the exit. chamber threshold. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH005_SC003; SHOT_INDEX; DIALOGUE; protagonist; the_watch_dog
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
- scene_id: CH005_SC003
- chapter_id: CH005
- shot_type: closing_reaction
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Controlled closing frame that lands the consequence of the beat.
- composition: Closing composition in deserted_martian_cityscape that emphasizes the consequence of crossing the threshold.
- shot_size: medium
- camera_angle: eye_level
- camera_motion: handheld
- zoom_behavior: none
- focus_strategy: rack_focus
- lighting_style: hard_directional
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: rear_three_quarter_left
- visible_primary_subject_id: protagonist
- visible_secondary_subject_ids: the_watch_dog
- primary_subject_frame_position: foreground right within chamber_threshold
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: rear three-quarter left away from camera
- primary_subject_pose_description: walking toward door
- subject_relation_summary: protagonist plays against watch_dog in the same frame
- scene_short_description: A restless prisoner tests his guard by moving toward a threshold under watchful eyes.
- shot_moment_summary: protagonist approaches the exit
- required_environment_anchor_1: chamber_threshold
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: preserve readable body-to-environment scale in frame
- camera_package_description: medium, eye level, wide lens, handheld, rack focus, hard directional
- environment_subzone: chamber_threshold
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; the_watch_dog; deserted_martian_cityscape; DESC_CH005_SC003; DESC_CH005_SC003_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: protagonist
- image2_role: identity reference for the secondary visible subject
- image2_asset: the watch dog
- image3_role: environment reference for the scene location
- image3_asset: deserted martian cityscape

# Continuity Notes
- Scene: CH005_SC003 / SC003.
- Variant: Alternate Angle.
- Physical distance between protagonist and the_watch_dog
- Lighting transition from captive_chamber_murals to deserted_martian_cityscape
- crossing the threshold
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH005\CH005_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH005\CH005_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH005\CH005_SC003\SH003\DIALOGUE.json
