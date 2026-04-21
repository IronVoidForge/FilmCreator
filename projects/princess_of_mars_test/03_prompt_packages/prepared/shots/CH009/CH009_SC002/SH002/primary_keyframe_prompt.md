# Title
SH002 Shot Prompt - Primary Keyframe

# ID
CH009_SC002_SH002_primary_keyframe_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Primary keyframe with balanced composition and clear subject placement.. Curiosity and growing empathy/indignation. **Likely Visual Coverage Families:** - Close-ups of the protagonist studying or listening inte.... Tight detail framing focused on a single visual object or gesture.. balanced framing with clear spatial separation. Characters: . Environment: described environment with stable spatial...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH009_SC002; SHOT_INDEX; DIALOGUE
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: neutral_reference
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: primary_keyframe
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH009_SC002
- chapter_id: CH009
- shot_type: insert_detail
- camera_description: Tight detail framing focused on a single visual object or gesture.
- composition: balanced framing with clear spatial separation
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH009_SC002 / To establish the protagonist's motivation and his intellectual drive....
- Variant: Primary Keyframe.
- Protagonist's level of linguistic fluency/effort shown through facial expressions.
- Carry the emotional arc through: Curiosity and growing empathy/indignation.
- **Likely Visual Coverage Families:**
- - Close-ups of the protagonist studying or listening intently.
- - Flashback/Memory inserts of the Red prisoner (if visually represented)..
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH009\CH009_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH009\CH009_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH009\CH009_SC002\SH002\DIALOGUE.json
