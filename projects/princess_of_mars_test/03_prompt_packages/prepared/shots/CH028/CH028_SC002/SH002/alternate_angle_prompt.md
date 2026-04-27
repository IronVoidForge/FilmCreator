# Title
SH002 Shot Prompt - Alternate Angle

# ID
CH028_SC002_SH002_alternate_angle_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for mummified woman. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for arizona cave system. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Alternate angle with the same beat and preserved continuity. A man explores a dark cave discovering ritualistic remains and hanging human skeletons. The subject from image1 is An old, mummified female corpse., Elderly / Ancient, lean athletic build, decisive, efficient movement, foreground inside ritual site, powder texture vs hand size, front three-quarter left toward the scene action, focus on burner. The subject from image2 is mummified woman plays against john carter in the same frame. Preserve the environment from image3 monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, broad processional paths and stairs, especially ritual site. close-up, low angle, normal lens, locked off, rack focus, torch firelight. Intimate composition that isolates, against to capture the beat's emotional turn. close up of green powder and burner. ritual site. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH028_SC002; SHOT_INDEX; DIALOGUE; john_carter; mummified_woman
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
- scene_id: CH028_SC002
- chapter_id: CH028
- shot_type: reaction_closeup
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates mummified_woman, john_carter against arizona_cave_system to capture the beat's emotional turn.
- shot_size: close_up
- camera_angle: low_angle
- camera_motion: locked_off
- zoom_behavior: none
- focus_strategy: rack_focus
- lighting_style: torch_firelight
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_left
- visible_primary_subject_id: mummified_woman
- visible_secondary_subject_ids: john_carter
- primary_subject_frame_position: foreground inside ritual site
- primary_subject_scale_relation: powder texture vs hand size
- primary_subject_facing_direction: front three-quarter left toward the scene action
- primary_subject_pose_description: focus on burner
- subject_relation_summary: mummified_woman plays against john_carter in the same frame
- scene_short_description: A man explores a dark cave discovering ritualistic remains and hanging human skeletons.
- shot_moment_summary: close up of green powder and burner
- required_environment_anchor_1: ritual site
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: powder texture vs hand size
- camera_package_description: close-up, low angle, normal lens, locked off, rack focus, torch firelight
- environment_subzone: ritual site
- prompt_family: shot_prompt
- reference_asset_ids: mummified_woman; john_carter; arizona_cave_system; DESC_CH028_SC002; DESC_CH028_SC002_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: mummified woman
- image2_role: identity reference for the secondary visible subject
- image2_asset: john carter
- image3_role: environment reference for the scene location
- image3_asset: arizona cave system

# Continuity Notes
- Scene: CH028_SC002 / SC002.
- Variant: Alternate Angle.
- mummified_woman position relative to john_carter
- lighting source from charcoal burner
- discovery of mummified woman
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH028\CH028_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH028\CH028_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH028\CH028_SC002\SH002\DIALOGUE.json
