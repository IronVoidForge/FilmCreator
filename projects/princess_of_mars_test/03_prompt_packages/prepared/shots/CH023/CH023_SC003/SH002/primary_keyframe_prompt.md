# Title
SH002 Shot Prompt - Primary Keyframe

# ID
CH023_SC003_SH002_primary_keyframe_prompt

# Purpose
Prepare a structured multi-reference shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Use image1 as the identity reference for kantos kan. Use image2 as the identity reference for the secondary visible subject. Use image3 as the environment reference for martian sky aerial corridors. Maintain the project visual language: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic. Primary keyframe with balanced composition and clear subject placement. High-speed aerial chase through Martian sky involving interception and mechanical failure. The subject from image1 is kantos kan, foreground right within darkness void, vertical distance of dive, profile right toward the scene action, interception. The subject from image2 is kantos kan plays against john carter in the same frame. Preserve the environment from image3 Vast, open expanses defined by aerial transit paths., monumental scale, dry open Martian terrain, ancient stone and ceremonial architecture, especially darkness void. full, high angle, wide lens, tilt, environment priority, low key night. Dynamic composition in clear pursuit vectors and readable movement. Kantos Kan dives into darkness to evade. darkness void. Keep continuity exact across costume, silhouette, lighting, and spatial relationships. Avoid proper nouns in the prompt body unless text is meant to appear on screen. No text, no watermark, no logo

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH023_SC003; SHOT_INDEX; DIALOGUE; john_carter; kantos_kan
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
- scene_id: CH023_SC003
- chapter_id: CH023
- shot_type: action
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: Dynamic composition in martian_sky_aerial_corridors with clear pursuit vectors and readable movement for kantos_kan, john_carter, Zodangan Air Patrols.
- shot_size: full
- camera_angle: high_angle
- camera_motion: tilt
- zoom_behavior: none
- focus_strategy: environment_priority
- lighting_style: low_key_night
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: profile_right
- visible_primary_subject_id: kantos_kan
- visible_secondary_subject_ids: john_carter
- primary_subject_frame_position: foreground right within darkness_void
- primary_subject_scale_relation: vertical distance of dive
- primary_subject_facing_direction: profile right toward the scene action
- primary_subject_pose_description: interception
- subject_relation_summary: kantos_kan plays against john_carter in the same frame
- scene_short_description: High-speed aerial chase through Martian sky involving interception and mechanical failure.
- shot_moment_summary: Kantos Kan dives into darkness to evade
- required_environment_anchor_1: darkness_void
- required_subject_anchor_1: (none)
- required_celestial_anchor_1: (none)
- required_scale_proof_detail: vertical distance of dive
- camera_package_description: full, high angle, wide lens, tilt, environment priority, low key night
- environment_subzone: darkness_void
- prompt_family: shot_prompt
- reference_asset_ids: kantos_kan; john_carter; martian_sky_aerial_corridors; DESC_CH023_SC003; DESC_CH023_SC003_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor
- image1_role: identity reference for the primary visible subject
- image1_asset: kantos kan
- image2_role: identity reference for the secondary visible subject
- image2_asset: john carter
- image3_role: environment reference for the scene location
- image3_asset: martian sky aerial corridors

# Continuity Notes
- Scene: CH023_SC003 / SC003.
- Variant: Primary Keyframe.
- Flight paths of machines must maintain relative velocity
- Directional vector of projectile fire from cruiser to Carter
- Heliumite gearing speed increase vs. baseline machine speed
- Kantos Kan's evasion dive
- Resolve Zodangan Air Patrols -> Zodangan Air Patrols
- Preserve reference-image roles, continuity, and canonical spatial relationships.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH023\CH023_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH023\CH023_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH023\CH023_SC003\SH002\DIALOGUE.json
