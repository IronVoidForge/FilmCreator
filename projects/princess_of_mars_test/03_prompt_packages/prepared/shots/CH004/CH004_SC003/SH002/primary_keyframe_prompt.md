# Title
SH002 Shot Prompt - Primary Keyframe

# ID
CH004_SC003_SH002_primary_keyframe_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Primary keyframe with balanced composition and clear subject placement.. Anticipation $\rightarrow$ Triumph/Awe. **Likely Visual Coverage Families:** * Wide shots to capture the full arc of the 150-foot leap. *.... Active camera with tracking energy and clear spatial orientation.. Dynamic composition in with crossing the frame and maintaining readable movement.. Characters: . Environment: describ...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH004_SC003; SHOT_INDEX; DIALOGUE
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
- scene_id: CH004_SC003
- chapter_id: CH004
- shot_type: action
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: Dynamic composition in Demonstrate the Narrator's physical prowess and ability to command re... with scene_character crossing the frame and maintaining readable movement.
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH004_SC003 / Demonstrate the Narrator's physical prowess and ability to command re....
- Variant: Primary Keyframe.
- The height and distance of the jump
- the Narrator's physical state (exhaustion vs. energy).
- Carry the emotional arc through: Anticipation $\rightarrow$ Triumph/Awe.
- **Likely Visual Coverage Families:**
- * Wide shots to capture the full arc of the 150-foot leap.
- * Slow-motion or dynamic tracking of the jump.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH004\CH004_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH004\CH004_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH004\CH004_SC003\SH002\DIALOGUE.json
