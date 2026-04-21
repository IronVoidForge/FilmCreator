# Title
SH003 Shot Prompt - Primary Keyframe

# ID
CH003_SC003_SH003_primary_keyframe_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Primary keyframe with balanced composition and clear subject placement.. Terror $\rightarrow$ Adrenaline/Survival Instinct. **Likely Visual Coverage Families:** - Rapid pans and tracking shots of the charging m.... Controlled closing frame that lands the consequence of the beat.. Closing composition in that emphasizes the consequence of **participating characters:** - the protagonist - martian wa...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH003_SC003; SHOT_INDEX; DIALOGUE
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: neutral_reference
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: primary_keyframe
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH003_SC003
- chapter_id: CH003
- shot_type: closing_reaction
- camera_description: Controlled closing frame that lands the consequence of the beat.
- composition: Closing composition in Create high-stakes tension and demonstrate the protagonist's unique a... that emphasizes the consequence of **participating characters:**
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH003_SC003 / Create high-stakes tension and demonstrate the protagonist's unique a....
- Variant: Primary Keyframe.
- **Participating Characters:**
- - The Protagonist
- - Martian Warriors (The Cavalry)
- - The Leader
- **Participating Environments:**
- - The Basin / The Incubator area.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH003\CH003_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC003\SH003\DIALOGUE.json
