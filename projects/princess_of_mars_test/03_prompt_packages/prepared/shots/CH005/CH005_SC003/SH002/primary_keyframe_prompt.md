# Title
SH002 Shot Prompt - Primary Keyframe

# ID
CH005_SC003_SH002_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for the watch dog. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for captive chamber murals. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. A restless prisoner tests his guard by moving toward a threshold under watchful eyes. The subject from image1 is [source:C:/FilmCreator MC/projects/princess of mars test/02 story analysis/character breakdowns/chapters/CH005/.md] Physical Description: A ferocious Martian creature with short legs. It is characterized by e., readable production deta, foreground inside captive chamber murals, preserve readable body-to-environment scale in frame, front three-quarter right toward the scene action, the watch dog stationary. The subject from image2 is the watch dog plays against protagonist in the same frame. Preserve the environment from image3 Interior cell containing a sleeping area, a Watch Dog is positioned at the threshold., monumental scale, dry open Martian terrain, especially captive chamber murals. Keep one readable subject anchor: stationary gaze. close-up, low angle, portrait lens, locked off, zoom subtle in, shallow subject, high contrast ceremonial. Intimate composition that isolates, against to capture the beat's emotional turn. the watch dog watches the movement. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH005_SC003; SHOT_INDEX; DIALOGUE; protagonist; the_watch_dog
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: portrait
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: primary_keyframe
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH005_SC003
- chapter_id: CH005
- shot_type: reaction_closeup
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates watch_dog, protagonist against captive_chamber_murals to capture the beat's emotional turn.
- shot_size: close_up
- camera_angle: low_angle
- camera_motion: locked_off
- zoom_behavior: subtle_in
- focus_strategy: shallow_subject
- lighting_style: high_contrast_ceremonial
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_right
- visible_primary_subject_id: the_watch_dog
- visible_secondary_subject_ids: protagonist
- primary_subject_frame_position: foreground inside captive_chamber_murals
- primary_subject_scale_relation: preserve readable body-to-environment scale in frame
- primary_subject_facing_direction: front three-quarter right toward the scene action
- primary_subject_pose_description: the_watch_dog stationary
- subject_relation_summary: the_watch_dog plays against protagonist in the same frame
- scene_short_description: A restless prisoner tests his guard by moving toward a threshold under watchful eyes.
- shot_moment_summary: the_watch_dog watches the movement
- required_environment_anchor_1: captive_chamber_murals
- required_subject_anchor_1: stationary gaze
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: preserve readable body-to-environment scale in frame
- camera_package_description: close-up, low angle, portrait lens, locked off, zoom subtle in, shallow subject, high contrast ceremonial
- environment_subzone: captive_chamber_murals
- prompt_family: shot_prompt
- reference_asset_ids: the_watch_dog; protagonist; captive_chamber_murals; DESC_CH005_SC003; DESC_CH005_SC003_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: the watch dog
- image2_role: identity reference for the secondary visible subject
- image2_asset: protagonist
- image3_role: environment reference for the scene location
- image3_asset: captive chamber murals

# Continuity Notes
- Scene: CH005_SC003 / SC003.
- Variant: Primary Keyframe.
- Physical distance between protagonist and the_watch_dog
- Lighting transition from captive_chamber_murals to deserted_martian_cityscape
- testing the guard's reaction
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH005\CH005_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH005\CH005_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH005\CH005_SC003\SH002\DIALOGUE.json
