# Title
SH004 Shot Prompt - Tighter Zoom

# ID
CH028_SC004_SH004_zoom_variant_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Tighter zoom with the same beat and preserved continuity.. Loneliness $\rightarrow$ Spiritual Connection/Hope **Likely Visual Coverage Families:** - Soft focus/Dreamlike lighting for the vision -.... Shoulder-level framing with visible foreground presence.. Over-the-shoulder composition in with sharing the frame.. Characters: . Environment: described environment with stable spatial continuity. Ke...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH004
- source_artifact_ids: CH028_SC004; SHOT_INDEX; DIALOGUE
- reference_mode: shot_prompt_bundle
- variant_name: zoom_variant
- lens_family: neutral_reference
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: zoom_variant
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH028_SC004
- chapter_id: CH028
- shot_type: over_the_shoulder
- previous_shot_id: SH003
- next_shot_id: (none)
- shot_lineage_ids: SH003; SH004
- camera_description: Shoulder-level framing with visible foreground presence.
- composition: Over-the-shoulder composition in SC004 with scene_character sharing the frame.
- prompt_family: shot_prompt
- reference_asset_ids: 
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH028_SC004 / SC004.
- Variant: Tighter Zoom.
- Lighting shift from realistic study light to ethereal vision quality
- Visual consistency of Dejah Thoris and Child visions
- Carter experiences a shift from isolation to spiritual hope/connection.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH028\CH028_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH028\CH028_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH028\CH028_SC004\SH004\DIALOGUE.json
