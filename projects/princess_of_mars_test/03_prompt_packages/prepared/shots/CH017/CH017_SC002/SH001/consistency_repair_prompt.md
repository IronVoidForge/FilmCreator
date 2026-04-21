# Title
SH001 Shot Prompt - Consistency Repair

# ID
CH017_SC002_SH001_consistency_repair_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships.. Relief $\rightarrow$ Desperation/Exhaustion.. Wide establishing frame with a steady or lightly drifting camera.. Wide composition across with, placed for immediate spatial orientation.. Characters: described character with stable costume and silhouette. Environment: described environment with stable spatial...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH017_SC002; SHOT_INDEX; DIALOGUE; protagonist; dejah_thoris; sola
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: neutral_reference
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: consistency_repair
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH017_SC002
- chapter_id: CH017
- shot_type: establishing_wide
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across The Mossy Waste (vast, trackless, desolate) with protagonist, dejah_thoris, sola placed for immediate spatial orientation.
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH017_SC002 / To transition the characters from the immediate danger of the city to....
- Variant: Consistency Repair.
- Thoa movement/speed
- level of dehydration/sweat on characters.
- The group escapes on thoats
- heading northeast across a two-hundred-mile mossy waste toward Helium
- suffering from extreme exhaustion and lack of supplies.
- Resolve The Mossy Waste (vast, trackless, desolate) -> The Mossy Waste (vast, trackless, desolate)
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH017\CH017_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH017\CH017_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH017\CH017_SC002\SH001\DIALOGUE.json
