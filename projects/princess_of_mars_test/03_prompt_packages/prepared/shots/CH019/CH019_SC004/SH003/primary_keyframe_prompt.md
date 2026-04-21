# Title
SH003 Shot Prompt - Primary Keyframe

# ID
CH019_SC004_SH003_primary_keyframe_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Primary keyframe with balanced composition and clear subject placement.. Tension $\rightarrow$ Adrenaline/Exhilaration. **Likely Visual Coverage Families:** - Action coverage (medium shots of combat) - Slow mot.... Controlled closing frame that lands the consequence of the beat.. Closing composition in that emphasizes the consequence of **participating characters:** - john carter - kantos kan - v...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH019_SC004; SHOT_INDEX; DIALOGUE
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
- scene_id: CH019_SC004
- chapter_id: CH019
- shot_type: closing_reaction
- camera_description: Controlled closing frame that lands the consequence of the beat.
- composition: Closing composition in Demonstrate character competence through action. that emphasizes the consequence of **participating characters:**
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH019_SC004 / Demonstrate character competence through action..
- Variant: Primary Keyframe.
- Blood/injury progression over the ten days
- weapon states.
- **Participating Characters:**
- - John Carter
- - Kantos Kan
- - Various Warriors/Martian Beasts
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH019\CH019_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH019\CH019_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH019\CH019_SC004\SH003\DIALOGUE.json
