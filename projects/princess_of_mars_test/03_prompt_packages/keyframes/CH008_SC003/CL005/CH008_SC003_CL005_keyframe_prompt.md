# Title
CH008_SC003 CL005 Keyframe Prompt

# ID
CH008_SC003_CL005_keyframe_prompt

# Purpose
Capture precise close-up detail of looting action for continuity tracking, focusing on item removal from vessel interior while maintaining visual consistency with previous shots.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Green-skinned hands removing food containers and water carboys from gray vessel interior, lifeless bodies visible in background, close-up framing, looting operation, detailed textures, cinematic lighting, smoke haze, metallic surfaces, organic decay, systematic search action.

# Negative Prompt
blurry, extra limbs, distorted anatomy, text, watermark, bright sunlight, wrong colors, floating objects, clean hands, modern clothing, vibrant green skin on humans, facial features on hands, clean background, high contrast shadows, noise, grainy, low resolution.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC003
- clip_id: CL005
- duration_seconds: 5
- required_refs: BT002.md, Scene Summary
- optional_refs: Continuity Notes
- visible_character_assets: Martians (hands), Dead Sailors (stationary)
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: close-up
- continuity_mode: insert
- starting_keyframe_strategy: open on specific item removal detail
- dependency_policy: depends on CL004
- auto_advance_policy: 
- fallback_strategy: cutaway if needed
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 
- workflow_type: still.scene_build.four_ref.klein.distilled

# Continuity Notes
- Track specific items removed (food, water) for inventory consistency across looting sequence.
- Ensure background lifeless bodies remain stationary and consistent with previous wide shots.
- Maintain lighting match from preceding clip to avoid jarring transitions during insert mode.
- Verify hand anatomy reflects green-skinned figure characteristics without human facial features.

# Repair Notes
- If hands appear too human-like, adjust skin tone and texture to match green-skinned figure profile.
- If lighting is too bright, reduce exposure to match interior vessel ambiance.
- If background bodies are missing, insert subtle silhouettes consistent with dead sailor count.
- Ensure item removal motion is smooth and deliberate for continuity tracking.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CL005.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC003.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CH008_SC003_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
