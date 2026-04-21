# Title
SH003 Shot Prompt - Tighter Zoom

# ID
CH014_SC003_SH003_zoom_variant_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Tighter zoom with the same beat and preserved continuity.. Isolation $\rightarrow$ Resentment $\rightarrow$ Destructive Action.. Controlled closing frame that lands the consequence of the beat.. Closing composition in that emphasizes the consequence of land the scene consequence or transition cleanly... Characters: described character with stable costume and silhouette. Environment: described env...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH014_SC003; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris; sola; None
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
- scene_id: CH014_SC003
- chapter_id: CH014
- shot_type: closing_reaction
- camera_description: Controlled closing frame that lands the consequence of the beat.
- composition: Closing composition in Barsoomian wilderness/Marching route that emphasizes the consequence of land the scene consequence or transition cleanly..
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH014_SC003 / Escalate the hostility and demonstrate the group's destructive path..
- Variant: Tighter Zoom.
- The direction of travel
- debris from the destroyed incubator.
- Land the scene consequence or transition cleanly.
- Resolve Green Men (Warhoon) -> Green Men (Warhoon)
- Resolve Barsoomian wilderness/Marching route -> Barsoomian wilderness/Marching route
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH014\CH014_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH014\CH014_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH014\CH014_SC003\SH003\DIALOGUE.json
