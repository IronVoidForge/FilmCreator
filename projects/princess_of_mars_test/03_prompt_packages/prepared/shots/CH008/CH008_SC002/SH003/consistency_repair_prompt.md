# Title
SH003 Shot Prompt - Consistency Repair

# ID
CH008_SC002_SH003_consistency_repair_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships.. Chaos $\rightarrow$ Methodical Efficiency $\rightarrow$ Somber Spectacle. **Likely Visual Coverage Families:** - Low angle shots of grapp.... Controlled closing frame that lands the consequence of the beat.. Closing composition in that emphasizes the consequence of **participating characters:** - green mart...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH008_SC002; SHOT_INDEX; DIALOGUE
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
- scene_id: CH008_SC002
- chapter_id: CH008
- shot_type: closing_reaction
- camera_description: Controlled closing frame that lands the consequence of the beat.
- composition: Closing composition in Show the aftermath of the battle and the ritualistic destruction of t... that emphasizes the consequence of **participating characters:**
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH008_SC002 / Show the aftermath of the battle and the ritualistic destruction of t....
- Variant: Consistency Repair.
- The movement/drift of the burning ship
- the amount of loot being carried away.
- **Participating Characters:**
- - Green Martian Warriors (Looters)
- **Participating Environments:**
- - Ground near the city/valleys
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH008\CH008_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH008\CH008_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH008\CH008_SC002\SH003\DIALOGUE.json
