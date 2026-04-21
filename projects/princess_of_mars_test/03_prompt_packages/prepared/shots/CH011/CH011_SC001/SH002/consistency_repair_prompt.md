# Title
SH002 Shot Prompt - Consistency Repair

# ID
CH011_SC001_SH002_consistency_repair_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships.. Tension/Conflict $\rightarrow$ Security/Status Recognition. **Likely Visual Coverage Families:** - Wide shots of the elaborate architectu.... Stable medium framing that keeps action and character readable.. Readable medium composition in featuring .. Characters: described character with stable costume and s...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH011_SC001; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris; sola
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
- scene_id: CH011_SC001
- chapter_id: CH011
- shot_type: medium
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in Ancient building near the audience chamber (Korad) featuring dejah_thoris.
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH011_SC001 / To establish the new status quo for Carter and Dejah Thoris, providin....
- Variant: Consistency Repair.
- The transition from the rugged Thark environment to the refined
- ancient architecture
- the physical state of the characters after the previous conflict.
- Carry the emotional arc through: Tension/Conflict $\rightarrow$ Security/Status Recognition.
- **Likely Visual Coverage Families:**
- - Wide shots of the elaborate architecture and frescoes.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH011\CH011_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH011\CH011_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH011\CH011_SC001\SH002\DIALOGUE.json
