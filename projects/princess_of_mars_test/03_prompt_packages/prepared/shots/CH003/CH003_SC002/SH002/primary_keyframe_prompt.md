# Title
SH002 Shot Prompt - Primary Keyframe

# ID
CH003_SC002_SH002_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for protagonist. Use image2 as the environment reference for martian incubator enclosure. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. A man approaches a glass-roofed enclosure filled with hundreds of large white eggs and emerging creatures. The subject from image1 is protagonist, foreground right within martian incubator enclosure interior, The low, walled martian incubator enclosure contains hundreds of eggs relative to the protagonist's size, profile left toward the scene action, protagonist face near glass. Preserve the environment from image2 Low walled enclosure with a glass roof., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially martian incubator enclosure interior. Keep one readable subject anchor: protagonist face near glass. medium, eye level, normal lens, push in, zoom subtle in, rack focus, diffuse ambient. Detail composition centered on the key physical action or prop inside. protagonist peering through the glass at hundreds of eggs. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH003_SC002; SHOT_INDEX; DIALOGUE; protagonist
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: normal
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
- scene_id: CH003_SC002
- chapter_id: CH003
- shot_type: insert_detail
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Tight detail framing focused on a single visual object or gesture.
- composition: Detail composition centered on the key physical action or prop inside martian_incubator_enclosure.
- shot_size: medium
- camera_angle: eye_level
- camera_motion: push_in
- zoom_behavior: subtle_in
- focus_strategy: rack_focus
- lighting_style: diffuse_ambient
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: profile_left
- visible_primary_subject_id: protagonist
- visible_secondary_subject_ids: (none)
- primary_subject_frame_position: foreground right within martian_incubator_enclosure_interior
- primary_subject_scale_relation: The low, walled martian_incubator_enclosure contains hundreds of eggs relative to the protagonist's size.
- primary_subject_facing_direction: profile left toward the scene action
- primary_subject_pose_description: protagonist face near glass
- subject_relation_summary: protagonist carries the frame alone
- scene_short_description: A man approaches a glass-roofed enclosure filled with hundreds of large white eggs and emerging creatures.
- shot_moment_summary: protagonist peering through the glass at hundreds of eggs
- required_environment_anchor_1: martian_incubator_enclosure_interior
- required_subject_anchor_1: protagonist face near glass
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: The low, walled martian_incubator_enclosure contains hundreds of eggs relative to the protagonist's size.
- camera_package_description: medium, eye level, normal lens, push in, zoom subtle in, rack focus, diffuse ambient
- environment_subzone: martian_incubator_enclosure_interior
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; martian_incubator_enclosure; DESC_CH003_SC002; DESC_CH003_SC002_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: protagonist
- image2_role: environment reference for the scene location
- image2_asset: martian incubator enclosure

# Continuity Notes
- Scene: CH003_SC002 / SC002.
- Variant: Primary Keyframe.
- Egg state (hatched vs unhatched) must remain consistent per shot
- Six-limbed creature movement patterns must be uniform
- observation of the eggs
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH003\CH003_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC002\SH002\DIALOGUE.json
