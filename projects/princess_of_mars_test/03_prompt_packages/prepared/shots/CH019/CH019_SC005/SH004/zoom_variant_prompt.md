# Title
SH004 Shot Prompt - Tighter Zoom

# ID
CH019_SC005_SH004_zoom_variant_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Tighter zoom with the same beat and preserved continuity.. High Tension $\rightarrow$ Relief $\rightarrow$ Determination. **Likely Visual Coverage Families:** - Close-ups on the "killing" blow - L.... Controlled closing frame that lands the consequence of the beat.. tighter framing on the same moment. Characters: . Environment: described environment with stable spatial continuity. Keep continuity...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH004
- source_artifact_ids: CH019_SC005; SHOT_INDEX; DIALOGUE
- reference_mode: shot_prompt_bundle
- variant_name: zoom_variant
- lens_family: neutral_reference
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: zoom_variant
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH019_SC005
- chapter_id: CH019
- shot_type: closing_reaction
- camera_description: Controlled closing frame that lands the consequence of the beat.
- composition: tighter framing on the same moment
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH019_SC005 / Execute the climax and transition to the next narrative phase..
- Variant: Tighter Zoom.
- The specific wound location on Carter
- transition from arena floor to exterior terrain.
- **Participating Characters:**
- - John Carter
- - Kantos Kan
- - Warhoon Horde (dispersing)
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH019\CH019_SC005.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH019\CH019_SC005\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH019\CH019_SC005\SH004\DIALOGUE.json
