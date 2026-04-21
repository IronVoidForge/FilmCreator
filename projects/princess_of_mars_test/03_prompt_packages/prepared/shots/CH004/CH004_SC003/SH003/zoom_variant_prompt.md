# Title
SH003 Shot Prompt - Tighter Zoom

# ID
CH004_SC003_SH003_zoom_variant_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Tighter zoom with the same beat and preserved continuity.. Anticipation $\rightarrow$ Triumph/Awe. **Likely Visual Coverage Families:** * Wide shots to capture the full arc of the 150-foot leap. *.... Controlled closing frame that lands the consequence of the beat.. Closing composition in that emphasizes the consequence of land the scene consequence or transition cleanly... Characters: . Environm...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH004_SC003; SHOT_INDEX; DIALOGUE
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
- scene_id: CH004_SC003
- chapter_id: CH004
- shot_type: closing_reaction
- camera_description: Controlled closing frame that lands the consequence of the beat.
- composition: Closing composition in Demonstrate the Narrator's physical prowess and ability to command re... that emphasizes the consequence of land the scene consequence or transition cleanly..
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH004_SC003 / Demonstrate the Narrator's physical prowess and ability to command re....
- Variant: Tighter Zoom.
- The height and distance of the jump
- the Narrator's physical state (exhaustion vs. energy).
- Land the scene consequence or transition cleanly.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH004\CH004_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH004\CH004_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH004\CH004_SC003\SH003\DIALOGUE.json
