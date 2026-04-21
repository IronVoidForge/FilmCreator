# Title
SH003 Shot Prompt - Tighter Zoom

# ID
CH006_SC001_SH003_zoom_variant_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Tighter zoom with the same beat and preserved continuity.. Terror $\rightarrow$ Desperation $\rightarrow$ Violent Escalation. **Likely Visual Coverage Families:** - Tight close-ups on the protagon.... Active camera with tracking energy and clear spatial orientation.. tighter framing on the same moment. Characters: . Environment: described environment with stable spatial continuity. Keep continuit...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH006_SC001; SHOT_INDEX; DIALOGUE
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
- scene_id: CH006_SC001
- chapter_id: CH006
- shot_type: action
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: tighter framing on the same moment
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH006_SC001 / To establish immediate life-threatening peril and introduce the comba....
- Variant: Tighter Zoom.
- **Participating Characters:**
- - The Protagonist
- - The Watch-thing
- - Ape-creature 1 (The Pinner)
- - Ape-creature 2 (The Attacker)
- Resolve Interior chamber/area overlooking a plaza -> Interior chamber/area overlooking a plaza
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH006\CH006_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH006\CH006_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH006\CH006_SC001\SH003\DIALOGUE.json
