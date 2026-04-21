# Title
SH004 Shot Prompt - Primary Keyframe

# ID
CH021_SC001_SH004_primary_keyframe_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Primary keyframe with balanced composition and clear subject placement.. Curiosity $\rightarrow$ Somberness/Dread.. Active camera with tracking energy and clear spatial orientation.. Dynamic composition in with crossing the frame and maintaining readable movement.. Characters: [], unknown. Environment: described environment with stable spatial continuity. Keep continuity exact across costume, sil...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH004
- source_artifact_ids: CH021_SC001; SHOT_INDEX; DIALOGUE; john_carter
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
- scene_id: CH021_SC001
- chapter_id: CH021
- shot_type: action
- previous_shot_id: SH003
- next_shot_id: (none)
- shot_lineage_ids: SH003; SH004
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: Dynamic composition in Martian agricultural tracts (underground water conduits/refined flora) with john_carter crossing the frame and maintaining readable movement.
- prompt_family: shot_prompt
- reference_asset_ids: john_carter
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH021_SC001 / SC001.
- Variant: Primary Keyframe.
- Consistency of john_carter travel gear/appearance
- Specific visual design of "refined" Martian flora
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH021\CH021_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH021\CH021_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH021\CH021_SC001\SH004\DIALOGUE.json
