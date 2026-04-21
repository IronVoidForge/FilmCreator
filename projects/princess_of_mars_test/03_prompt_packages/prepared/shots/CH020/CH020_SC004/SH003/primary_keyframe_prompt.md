# Title
SH003 Shot Prompt - Primary Keyframe

# ID
CH020_SC004_SH003_primary_keyframe_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Primary keyframe with balanced composition and clear subject placement.. Desperation $\rightarrow$ Safety/Comfort.. Active camera with tracking energy and clear spatial orientation.. Dynamic composition in with, crossing the frame and maintaining readable movement.. Characters: [], unknown, [], No visual description is provided in the available evidence., unknown. Environment: described environme...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH020_SC004; SHOT_INDEX; DIALOGUE; protagonist; woola
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
- scene_id: CH020_SC004
- chapter_id: CH020
- shot_type: action
- previous_shot_id: SH002
- next_shot_id: SH004
- shot_lineage_ids: SH002; SH003; SH004
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: Dynamic composition in The Ptor Farm (Raised homes on metal shafts) with protagonist, woola crossing the frame and maintaining readable movement.
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; woola
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH020_SC004 / SC004.
- Variant: Primary Keyframe.
- Food and prop placement on the table during meal sequence
- Protagonist cleanliness levels (transitioning from wild to guest)
- Meal service and interaction demonstrating Red Martian hospitality.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH020\CH020_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH020\CH020_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH020\CH020_SC004\SH003\DIALOGUE.json
