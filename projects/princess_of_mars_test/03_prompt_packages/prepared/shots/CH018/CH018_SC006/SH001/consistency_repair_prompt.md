# Title
SH001 Shot Prompt - Consistency Repair

# ID
CH018_SC006_SH001_consistency_repair_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships.. Hope $\rightarrow$ Pure Terror/Paranoia. **Likely Visual Coverage Families:** - Shallow depth of field focusing on the gleaming eyes. - S.... Close framing that isolates reaction and emotional emphasis.. Intimate composition that isolates against to capture the beat's emotional turn.. Characters: described...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH018_SC006; SHOT_INDEX; DIALOGUE; protagonist; None
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
- scene_id: CH018_SC006
- chapter_id: CH018
- shot_type: reaction_closeup
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates protagonist against Dark dungeon to capture the beat's emotional turn.
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH018_SC006 / To introduce a new, supernatural or predatory threat and end the chap....
- Variant: Consistency Repair.
- Eye placement in the frame
- lighting levels.
- As the protagonist prepares to use the keys
- he realizes he is not alone; multiple pairs of eyes emerge from the darkness
- watching him before retreating.
- Resolve Unseen Entities (Eyes in the dark) -> Unseen Entities (Eyes in the dark)
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH018\CH018_SC006.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH018\CH018_SC006\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH018\CH018_SC006\SH001\DIALOGUE.json
