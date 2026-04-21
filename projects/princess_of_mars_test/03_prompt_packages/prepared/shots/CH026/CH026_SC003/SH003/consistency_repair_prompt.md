# Title
SH003 Shot Prompt - Consistency Repair

# ID
CH026_SC003_SH003_consistency_repair_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships.. Determination $\rightarrow$ High-Stakes Combat $\rightarrow$ Decisive Victory.. Active camera with tracking energy and clear spatial orientation.. continuity-preserving framing with exact pose and costume locks. Characters: described character with stable costume and silhouette. Environment: described envir...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH026_SC003; SHOT_INDEX; DIALOGUE; john_carter; tars_tarkas; thark_warriors; None; None
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
- scene_id: CH026_SC003
- chapter_id: CH026
- shot_type: action
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: continuity-preserving framing with exact pose and costume locks
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH026_SC003 / To resolve the remaining ground-based threat and demonstrate Thark ma....
- Variant: Consistency Repair.
- The number of troops visible in wide shots
- The direction of the charge
- Weaponry usage (small arms vs melee).
- Land the scene consequence or transition cleanly.
- Resolve Heliumite Reinforcements -> Heliumite Reinforcements
- Resolve Zodangan Ground Forces -> Zodangan Ground Forces
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH026\CH026_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH026\CH026_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH026\CH026_SC003\SH003\DIALOGUE.json
