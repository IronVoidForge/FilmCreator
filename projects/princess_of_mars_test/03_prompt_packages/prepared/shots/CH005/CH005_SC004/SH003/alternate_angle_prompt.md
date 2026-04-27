# Title
SH003 Shot Prompt - Alternate Angle

# ID
CH005_SC004_SH003_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for protagonist. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for deserted martian cityscape. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. A predator charges across a desolate street toward a fleeing figure leaping for a high window. The subject from image1 is protagonist, midground inside building exterior, 30 foot vertical height, profile right toward the scene action, protagonist at base of wall. The subject from image2 is [source:C:/FilmCreator MC/projects/princess of mars test/02 story analysis/character breakdowns/chapters/CH005/.md] Physical Description: A ferocious Martian creature with short legs. It is characterized by e., readable production deta, protagonist plays against watch dog in the same frame. Preserve the environment from image3 Wide streets leading to the city edge, significant vertical scale with high window ledges and sills., monumental scale, dry open Martian terrain, especially building exterior. wide, low angle, ultra-wide lens, crane, deep focus, backlit. Wide composition across placed for immediate spatial orientation. the 30ft leap. building exterior. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH005_SC004; SHOT_INDEX; DIALOGUE; protagonist; the_watch_dog
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: ultra_wide
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
- scene_id: CH005_SC004
- chapter_id: CH005
- shot_type: establishing_wide
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across deserted_martian_cityscape with protagonist, watch_dog placed for immediate spatial orientation.
- shot_size: wide
- camera_angle: low_angle
- camera_motion: crane
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: backlit
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: profile_right
- visible_primary_subject_id: protagonist
- visible_secondary_subject_ids: the_watch_dog
- primary_subject_frame_position: midground inside building exterior
- primary_subject_scale_relation: 30 foot vertical height
- primary_subject_facing_direction: profile right toward the scene action
- primary_subject_pose_description: protagonist at base of wall
- subject_relation_summary: protagonist plays against watch_dog in the same frame
- scene_short_description: A predator charges across a desolate street toward a fleeing figure leaping for a high window.
- shot_moment_summary: the 30ft leap
- required_environment_anchor_1: building exterior
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: 30 foot vertical height
- camera_package_description: wide, low angle, ultra-wide lens, crane, deep focus, backlit
- environment_subzone: building exterior
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; the_watch_dog; deserted_martian_cityscape; DESC_CH005_SC004; DESC_CH005_SC004_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: protagonist
- image2_role: identity reference for the secondary visible subject
- image2_asset: the watch dog
- image3_role: environment reference for the scene location
- image3_asset: deserted martian cityscape

# Continuity Notes
- Scene: CH005_SC004 / SC004.
- Variant: Alternate Angle.
- Speed of the_watch_dog charge
- Vertical height of window (30 feet)
- Direction of movement through deserted_martian_cityscape
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH005\CH005_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH005\CH005_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH005\CH005_SC004\SH003\DIALOGUE.json
