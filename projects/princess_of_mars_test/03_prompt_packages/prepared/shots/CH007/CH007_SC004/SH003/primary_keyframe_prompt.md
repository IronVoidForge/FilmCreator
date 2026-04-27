# Title
SH003 Shot Prompt - Primary Keyframe

# ID
CH007_SC004_SH003_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for young martian. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for the dead city. Use image4 as the identity reference for an additional visible subject. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. Intensive Martian language training and telepathic discovery within a desolate urban environment. The subject from image1 is Small, humanoid non-human male., Newly hatched / infant stage of life., Three-to-four-foot-tall, described as "physically perfect.", foreground right within training zone, Individual mental struggle against external psychic pressure, profile left toward the scene action, young martian enters frame. The subject from image2 is young martian plays against protagonist, sola in the same frame. Preserve the environment from image3 An expansive, ruined urban center., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially training zone. medium-full, low angle, wide lens, track, deep focus, diffuse ambient. Dynamic composition in clear pursuit vectors and readable movement. young martian approaches. training zone. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH007_SC004; SHOT_INDEX; DIALOGUE; protagonist; sola; young_martian
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: wide
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: primary_keyframe
- review_notes: Prompt body is missing the required subject anchor for an on-screen shot.
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH007_SC004
- chapter_id: CH007
- shot_type: action
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: Dynamic composition in the_dead_city with clear pursuit vectors and readable movement for young_martian, protagonist, sola.
- shot_size: medium_full
- camera_angle: low_angle
- camera_motion: track
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: in_scene_speaker
- primary_subject_angle: profile_left
- visible_primary_subject_id: young_martian
- visible_secondary_subject_ids: protagonist; sola
- primary_subject_frame_position: foreground right within training_zone
- primary_subject_scale_relation: Individual mental struggle against external psychic pressure.
- primary_subject_facing_direction: profile left toward the scene action
- primary_subject_pose_description: young_martian enters frame
- subject_relation_summary: young_martian plays against protagonist, sola in the same frame
- scene_short_description: Intensive Martian language training and telepathic discovery within a desolate urban environment.
- shot_moment_summary: young_martian approaches
- required_environment_anchor_1: training_zone
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: Individual mental struggle against external psychic pressure.
- camera_package_description: medium-full, low angle, wide lens, track, deep focus, diffuse ambient
- environment_subzone: training_zone
- prompt_family: shot_prompt
- reference_asset_ids: young_martian; protagonist; sola; the_dead_city; DESC_CH007_SC004; DESC_CH007_SC004_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: young martian
- image2_role: identity reference for the secondary visible subject
- image2_asset: protagonist
- image3_role: environment reference for the scene location
- image3_asset: the dead city
- image4_role: identity reference for an additional visible subject
- image4_asset: sola

# Continuity Notes
- Scene: CH007_SC004 / SC004.
- Variant: Primary Keyframe.
- Visual consistency of telepathic effect representation
- Physical interaction mechanics between protagonist and young_martian
- Encounter with young_martian
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH007\CH007_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH007\CH007_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH007\CH007_SC004\SH003\DIALOGUE.json
