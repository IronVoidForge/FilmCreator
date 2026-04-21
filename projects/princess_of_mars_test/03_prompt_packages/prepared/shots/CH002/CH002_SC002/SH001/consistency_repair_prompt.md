# Title
SH001 Shot Prompt - Consistency Repair

# ID
CH002_SC002_SH001_consistency_repair_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships.. Struggle $\rightarrow$ Shock/Existential Horror **Likely Visual Coverage Families:** - Macro shots (The physical body's features) - POV s.... Close framing that isolates reaction and emotional emphasis.. Intimate composition that isolates against to capture the beat's emotional turn.. Characters: . Environm...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH002_SC002; SHOT_INDEX; DIALOGUE
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
- scene_id: CH002_SC002
- chapter_id: CH002
- shot_type: reaction_closeup
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates scene_character against Execute the supernatural reveal of the protagonist's dual existence. to capture the beat's emotional turn.
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH002_SC002 / Execute the supernatural reveal of the protagonist's dual existence..
- Variant: Consistency Repair.
- After hours of mental struggle
- the protagonist breaks free from the paralysis only to realize he has undergone a metamorphosis; his new
- naked self stands above his original
- clothed body which remains lifeless on the cave floor.
- **Participating Characters:**
- - The Protagonist (New/Astral form)
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH002\CH002_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH002\CH002_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH002\CH002_SC002\SH001\DIALOGUE.json
