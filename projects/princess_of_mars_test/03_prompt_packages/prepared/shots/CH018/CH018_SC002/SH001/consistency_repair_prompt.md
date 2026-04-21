# Title
SH001 Shot Prompt - Consistency Repair

# ID
CH018_SC002_SH001_consistency_repair_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships.. Tension $\rightarrow$ Chaos/Violence $\rightarrow$ Shock/Awe. **Likely Visual Coverage Families:** - Mid-shots of the confrontation betwe.... Stable medium framing that keeps action and character readable.. continuity-preserving framing with exact pose and costume locks. Characters: described character with...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH018_SC002; SHOT_INDEX; DIALOGUE; None; dak_kova; None; warhoon_warriors
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
- scene_id: CH018_SC002
- chapter_id: CH018
- shot_type: medium
- camera_description: Stable medium framing that keeps action and character readable.
- composition: continuity-preserving framing with exact pose and costume locks
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH018_SC002 / To execute a major narrative pivot through character conflict and the....
- Variant: Consistency Repair.
- Blood splatter patterns
- weapon positions
- Dak Kova's physical state before/after the kill.
- Dak Kova openly defies Jeddak Bar Comas.
- Resolve Protagonist (observer) -> Protagonist (observer)
- Resolve Bar Comas -> Bar Comas
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH018\CH018_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH018\CH018_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH018\CH018_SC002\SH001\DIALOGUE.json
