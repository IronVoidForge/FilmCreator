# Title
SH002 Shot Prompt - Alternate Angle

# ID
CH016_SC006_SH002_alternate_angle_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Alternate angle with the same beat and preserved continuity.. Hopeful Action $\rightarrow$ Confusion $\rightarrow$ Terror/Realization of Trap.. Close framing that isolates reaction and emotional emphasis.. Intimate composition that isolates, against to capture the beat's emotional turn.. Characters: [], unknown, . Environment: described environment with stable spatial continuity. Keep continuity...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH016_SC006; SHOT_INDEX; DIALOGUE; john_carter
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
- scene_id: CH016_SC006
- chapter_id: CH016
- shot_type: reaction_closeup
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates john_carter, Thark Chieftain (off-screen/overheard) against City outskirts to capture the beat's emotional turn.
- prompt_family: shot_prompt
- reference_asset_ids: john_carter
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH016_SC006 / SC006.
- Variant: Alternate Angle.
- Nighttime lighting and shadow consistency across locations
- Movement patterns/choreography of the Thark warriors
- Sound design synchronization for overheard dialogue
- John realizes the rendezvous is compromised and hides his animals.
- Resolve Thark Chieftain (off-screen/overheard) -> Thark Chieftain (off-screen/overheard)
- Resolve Thark Warriors -> Thark Warriors
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH016\CH016_SC006.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH016\CH016_SC006\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH016\CH016_SC006\SH002\DIALOGUE.json
