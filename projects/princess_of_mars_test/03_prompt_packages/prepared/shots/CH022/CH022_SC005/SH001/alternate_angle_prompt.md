# Title
SH001 Shot Prompt - Alternate Angle

# ID
CH022_SC005_SH001_alternate_angle_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Alternate angle with the same beat and preserved continuity.. Stealthy tension $\rightarrow$ Growing dread.. Stable medium framing that keeps action and character readable.. Readable medium composition in featuring, .. Characters: . Environment: described environment with stable spatial continuity. Keep continuity exact across costume, silhouette, lighting, and spatial relationships.. Avoid prope...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH022_SC005; SHOT_INDEX; DIALOGUE; None; None; None; None
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: neutral_reference
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: alternate_angle
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH022_SC005
- chapter_id: CH022
- shot_type: medium
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in Labyrinthine palace corridors featuring John Carter (hidden), Guards (off-screen/background).
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH022_SC005 / Build suspense and establish the threat level of the palace guards..
- Variant: Alternate Angle.
- Sound design (footsteps, muffled voices)
- Lighting/Shadow placement for Carter's concealment.
- While navigating the labyrinthine palace
- Carter hides and overhears guards discussing the massacre in the antechamber. He then listens to Than Kosis and Notan discuss the mysterious
- superhuman man on the loose.
- Resolve John Carter (hidden) -> John Carter (hidden)
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH022\CH022_SC005.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH022\CH022_SC005\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH022\CH022_SC005\SH001\DIALOGUE.json
