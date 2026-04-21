# Title
SH001 Shot Prompt - Tighter Zoom

# ID
CH019_SC001_SH001_zoom_variant_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Tighter zoom with the same beat and preserved continuity.. Confusion $\rightarrow$ Realization of helplessness. **Likely Visual Coverage Families:** - Extreme close-ups (eyes, hands in dark) - Low.... Close framing that isolates reaction and emotional emphasis.. tighter framing on the same moment. Characters: . Environment: described environment with stable spatial continuity. Keep continuity exa...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH019_SC001; SHOT_INDEX; DIALOGUE
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
- scene_id: CH019_SC001
- chapter_id: CH019
- shot_type: reaction_closeup
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: tighter framing on the same moment
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH019_SC001 / Establish the dire situation and the loss of agency..
- Variant: Tighter Zoom.
- Lighting levels in the cell
- Carter's physical state/injuries from previous capture.
- John Carter is left in darkness within his cell
- only to realize that the jailer's keys have been stolen by creatures from a nearby lair
- leaving him without immediate means of escape.
- **Participating Characters:**
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH019\CH019_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH019\CH019_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH019\CH019_SC001\SH001\DIALOGUE.json
