# Title
SH002 Shot Prompt - Tighter Zoom

# ID
CH027_SC004_SH002_zoom_variant_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Tighter zoom with the same beat and preserved continuity.. Intense Concentration $\rightarrow$ Relief $\rightarrow$ Physical Collapse. **Likely Visual Coverage Families:** - Wide shots of the mass.... Tight detail framing focused on a single visual object or gesture.. Detail composition centered on the key physical action or prop inside .. Characters: described character with stable costume and s...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH027_SC004; SHOT_INDEX; DIALOGUE; john_carter; surviving_technician
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
- scene_id: CH027_SC004
- chapter_id: CH027
- shot_type: insert_detail
- camera_description: Tight detail framing focused on a single visual object or gesture.
- composition: Detail composition centered on the key physical action or prop inside The Atmosphere Plant (Interior/Exterior).
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH027_SC004 / The Climax; resolve the immediate threat through mental and physical....
- Variant: Tighter Zoom.
- The mechanical state of the pumps
- the visual representation of the thought waves (if any)
- the physical exhaustion level of John Carter.
- Carry the emotional arc through: Intense Concentration $\rightarrow$ Relief $\rightarrow$ Physical Collapse.
- **Likely Visual Coverage Families:**
- - Wide shots of the massive
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH027\CH027_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH027\CH027_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH027\CH027_SC004\SH002\DIALOGUE.json
