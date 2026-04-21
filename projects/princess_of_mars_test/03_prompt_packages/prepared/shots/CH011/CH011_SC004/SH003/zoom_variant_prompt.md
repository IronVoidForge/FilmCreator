# Title
SH003 Shot Prompt - Tighter Zoom

# ID
CH011_SC004_SH003_zoom_variant_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Tighter zoom with the same beat and preserved continuity.. Peace/Connection $\rightarrow$ Sudden Urgency/Duty. **Likely Visual Coverage Families:** - Medium shot of the interruption (the messenger.... Controlled closing frame that lands the consequence of the beat.. tighter framing on the same moment. Characters: described character with stable costume and silhouette. Environment: described envir...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
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
- shot_type: closing_reaction
- camera_description: Controlled closing frame that lands the consequence of the beat.
- composition: tighter framing on the same moment
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH011_SC004 / To disrupt the growing intimacy and propel the plot toward the next m....
- Variant: Tighter Zoom.
- The timing of the interruption relative to the previous dialogue
- the physical movement of the messenger entering the space.
- Land the scene consequence or transition cleanly.
- Resolve Messenger -> Messenger
- Resolve The luxurious ancient quarters -> The luxurious ancient quarters
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH011\CH011_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH011\CH011_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH011\CH011_SC004\SH003\DIALOGUE.json
