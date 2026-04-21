# Title
SH001 Shot Prompt - Consistency Repair

# ID
CH027_SC003_SH001_consistency_repair_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships.. Despair $\rightarrow$ Focused Determination/Adrenaline. **Likely Visual Coverage Families:** - Fast-paced, rhythmic editing during the ma.... Stable medium framing that keeps action and character readable.. continuity-preserving framing with exact pose and costume locks. Characters: described character with...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH027_SC003; SHOT_INDEX; DIALOGUE; john_carter
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
- scene_id: CH027_SC003
- chapter_id: CH027
- shot_type: medium
- camera_description: Stable medium framing that keeps action and character readable.
- composition: continuity-preserving framing with exact pose and costume locks
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH027_SC003 / Transition from despair to action; provide the "hero's realization.".
- Variant: Consistency Repair.
- The state of the stripped-down air-scout
- the visual density/clarity of the atmosphere (getting thinner as he flies).
- John Carter recalls the nine "thought waves" required to unlock the plant. He frantically modifies a high-speed air-scout machine
- stripping it of all non-essential weight to race through the thinning atmosphere toward the plant.
- Resolve Palace/Hangar area -> Palace/Hangar area
- Resolve The sky above Barsoom -> The sky above Barsoom
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH027\CH027_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH027\CH027_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH027\CH027_SC003\SH001\DIALOGUE.json
