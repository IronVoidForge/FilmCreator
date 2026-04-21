# Title
SH003 Shot Prompt - Consistency Repair

# ID
CH010_SC002_SH003_consistency_repair_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships.. Curiosity/Observation to heightened political tension.. Shoulder-level conversational framing with visible foreground presence.. Over-the-shoulder composition in with, sharing the frame for dialogue or tension.. Characters: described character with stable costume and silhouette. Environment: described envir...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH010_SC002; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris; sarkoja; lorquas_ptomel; None
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
- scene_id: CH010_SC002
- chapter_id: CH010
- shot_type: over_the_shoulder
- camera_description: Shoulder-level conversational framing with visible foreground presence.
- composition: Over-the-shoulder composition in The City Plaza / Council area with john_carter, dejah_thoris sharing the frame for dialogue or tension.
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH010_SC002 / Setup tension and introduce the political stakes..
- Variant: Consistency Repair.
- Carter's hiding spot/positioning relative to the Council members.
- Land the scene consequence or transition cleanly.
- Resolve Thark Council members -> Thark Council members
- Resolve The City Plaza / Council area -> The City Plaza / Council area
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH010\CH010_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH010\CH010_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH010\CH010_SC002\SH003\DIALOGUE.json
