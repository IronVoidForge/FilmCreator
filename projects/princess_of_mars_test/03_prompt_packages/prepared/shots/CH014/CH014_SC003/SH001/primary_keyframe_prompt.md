# Title
SH001 Shot Prompt - Primary Keyframe

# ID
CH014_SC003_SH001_primary_keyframe_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Primary keyframe with balanced composition and clear subject placement.. Ition $\rightarrow$ Resentment $\rightarrow$ Destructive Action.. Wide establishing frame with a steady or lightly drifting camera.. balanced framing with clear spatial separation. Characters: described character with stable costume and silhouette. Environment: described environment with stable spatial continuity. Keep conti...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH014_SC003; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris; sola; None
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
- scene_id: CH014_SC003
- chapter_id: CH014
- shot_type: establishing_wide
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: balanced framing with clear spatial separation
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH014_SC003 / Escalate the hostility and demonstrate the group's destructive path..
- Variant: Primary Keyframe.
- The direction of travel
- debris from the destroyed incubator.
- During the march toward Thark
- Dejah Thoris communicates her contempt for Carter via Sola
- deepening Carter's sense of isolation and homesickness. The party destroys a Warhoon incubator during their trek.
- Resolve Green Men (Warhoon) -> Green Men (Warhoon)
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH014\CH014_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH014\CH014_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH014\CH014_SC003\SH001\DIALOGUE.json
