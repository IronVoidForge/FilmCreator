# Title
SH002 Shot Prompt - Alternate Angle

# ID
CH027_SC001_SH002_alternate_angle_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Alternate angle with the same beat and preserved continuity.. Contentment/Peace $\rightarrow$ Panic/Urgency. **Likely Visual Coverage Families:** - Warm, golden-hued close-ups of the incubator and th.... Tight detail framing focused on a single visual object or gesture.. Detail composition centered on the key physical action or prop inside .. Characters: described character with stable costume an...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH027_SC001; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris; tardos_mors; None
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: neutral_reference
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: alternate_angle
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH027_SC001
- chapter_id: CH027
- shot_type: insert_detail
- camera_description: Tight detail framing focused on a single visual object or gesture.
- composition: Detail composition centered on the key physical action or prop inside The Palace in Helium (Rooftop Shrine/Sunken Garden).
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH027_SC001 / Establish the status quo of peace and introduce the inciting incident....
- Variant: Alternate Angle.
- The appearance/age of the characters over the nine-year jump
- the physical state of the golden incubator.
- Carry the emotional arc through: Contentment/Peace $\rightarrow$ Panic/Urgency.
- **Likely Visual Coverage Families:**
- - Warm
- golden-hued close-ups of the incubator and the couple.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH027\CH027_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH027\CH027_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH027\CH027_SC001\SH002\DIALOGUE.json
