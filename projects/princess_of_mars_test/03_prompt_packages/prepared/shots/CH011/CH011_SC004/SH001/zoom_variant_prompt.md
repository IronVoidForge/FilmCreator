# Title
SH001 Shot Prompt - Tighter Zoom

# ID
CH011_SC004_SH001_zoom_variant_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Tighter zoom with the same beat and preserved continuity.. Peace/Connection $\rightarrow$ Sudden Urgency/Duty. **Likely Visual Coverage Families:** - Medium shot of the interruption (the messenger.... Stable medium framing that keeps action and character readable.. tighter framing on the same moment. Characters: described character with stable costume and silhouette. Environment: described enviro...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH011_SC004; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris; None
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
- scene_id: CH011_SC004
- chapter_id: CH011
- shot_type: medium
- camera_description: Stable medium framing that keeps action and character readable.
- composition: tighter framing on the same moment
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH011_SC004 / To disrupt the growing intimacy and propel the plot toward the next m....
- Variant: Tighter Zoom.
- The timing of the interruption relative to the previous dialogue
- the physical movement of the messenger entering the space.
- The quiet
- revelatory moment between Carter and Dejah Thoris is broken by a messenger. A summons arrives from Lorquas Ptomel
- demanding Carter's immediate presence at the audience chamber.
- Resolve Messenger -> Messenger
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH011\CH011_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH011\CH011_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH011\CH011_SC004\SH001\DIALOGUE.json
