# Title
SH001 Shot Prompt - Consistency Repair

# ID
CH014_SC004_SH001_consistency_repair_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships.. Rest/Lull $\rightarrow$ Aggression/Challenge.. Active camera with tracking energy and clear spatial orientation.. Dynamic composition in with crossing the frame and maintaining readable movement.. Characters: described character with stable costume and silhouette. Environment: described environment with sta...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH014_SC004; SHOT_INDEX; DIALOGUE; john_carter; zad; sarkoja; tars_tarkas; dejah_thoris
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
- scene_id: CH014_SC004
- chapter_id: CH014
- shot_type: action
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: Dynamic composition in Rest camp/Open terrain with zad crossing the frame and maintaining readable movement.
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH014_SC004 / Trigger the physical climax of the chapter through provocation..
- Variant: Consistency Repair.
- Weapon placement
- character positioning around the camp.
- During a rest halt
- Zad provokes Carter into a formal duel. The tension shifts from verbal/social hostility to immediate physical threat.
- Resolve Rest camp/Open terrain -> Rest camp/Open terrain
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH014\CH014_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH014\CH014_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH014\CH014_SC004\SH001\DIALOGUE.json
