# Title
SH004 Shot Prompt - Primary Keyframe

# ID
CH024_SC001_SH004_primary_keyframe_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Primary keyframe with balanced composition and clear subject placement.. Chaos/Peril $\rightarrow$ Heroic Intervention $\rightarrow$ Mutual Respect.. Active camera with tracking energy and clear spatial orientation.. Dynamic composition in with, crossing the frame and maintaining readable movement.. Characters: [], unknown, . Environment: described environment with stable spatial continuity. Keep...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH004
- source_artifact_ids: CH024_SC001; SHOT_INDEX; DIALOGUE; john_carter; tars_tarkas
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: neutral_reference
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
- scene_id: CH024_SC001
- chapter_id: CH024
- shot_type: action
- previous_shot_id: SH003
- next_shot_id: SH005
- shot_lineage_ids: SH003; SH004; SH005
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: Dynamic composition in The Battlefield (Plains near an ancient dead city) with john_carter, Warhoon Warriors crossing the frame and maintaining readable movement.
- prompt_family: shot_prompt
- reference_asset_ids: john_carter
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH024_SC001 / SC001.
- Variant: Primary Keyframe.
- Damage state of John Carter's craft
- Blood/injury status of Tars Tarkas
- Weaponry consistency used in the melee
- John Carter intervenes using sheer strength to fight off the Warhoon warriors.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH024\CH024_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH024\CH024_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH024\CH024_SC001\SH004\DIALOGUE.json
