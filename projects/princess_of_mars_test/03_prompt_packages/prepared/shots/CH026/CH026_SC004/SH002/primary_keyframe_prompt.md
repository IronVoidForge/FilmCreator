# Title
SH002 Shot Prompt - Primary Keyframe

# ID
CH026_SC004_SH002_primary_keyframe_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Primary keyframe with balanced composition and clear subject placement.. Exhaustion $\rightarrow$ Grandeur $\rightarrow$ Solemn Unity.. Stable medium framing that keeps action and character readable.. Readable medium composition in featuring, .. Characters: described character with stable costume and silhouette. Environment: described environment with stable spatial continuity. Keep continuity ex...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH026_SC004; SHOT_INDEX; DIALOGUE; john_carter; tars_tarkas; tardos_mors; dejah_thoris; None
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
- scene_id: CH026_SC004
- chapter_id: CH026
- shot_type: medium
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in The streets/palace of Helium (Greater City) featuring john_carter, tars_tarkas.
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH026_SC004 / To formalize the political alliance and provide emotional resolution..
- Variant: Primary Keyframe.
- The level of "battle grime" on the characters (should be present but transitioning to ceremonial)
- The scale of the crowd/procession length.
- Carry the emotional arc through: Exhaustion $\rightarrow$ Grandeur $\rightarrow$ Solemn Unity..
- Resolve Heliumite Citizens -> Heliumite Citizens
- Resolve The streets/palace of Helium (Greater City) -> The streets/palace of Helium (Greater City)
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH026\CH026_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH026\CH026_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH026\CH026_SC004\SH002\DIALOGUE.json
