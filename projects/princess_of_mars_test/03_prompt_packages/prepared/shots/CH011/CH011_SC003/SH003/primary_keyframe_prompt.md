# Title
SH003 Shot Prompt - Primary Keyframe

# ID
CH011_SC003_SH003_primary_keyframe_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Primary keyframe with balanced composition and clear subject placement.. Intimacy $\rightarrow$ Intellectual Wonder/Awe. **Likely Visual Coverage Families:** - Medium shots of as she lectures/explains. - Cutawa.... Controlled closing frame that lands the consequence of the beat.. balanced framing with clear spatial separation. Characters: described character with stable costume and silhouette. En...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH011_SC003; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris
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
- scene_id: CH011_SC003
- chapter_id: CH011
- shot_type: closing_reaction
- camera_description: Controlled closing frame that lands the consequence of the beat.
- composition: balanced framing with clear spatial separation
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH011_SC003 / To provide world-building exposition regarding Martian technology and....
- Variant: Primary Keyframe.
- Hand gestures used during explanation
- positioning relative to the wall frescoes.
- Land the scene consequence or transition cleanly.
- Resolve The luxurious ancient quarters (amidst frescoes of the ancient race) -> The luxurious ancient quarters (amidst frescoes of the ancient race)
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH011\CH011_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH011\CH011_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH011\CH011_SC003\SH003\DIALOGUE.json
