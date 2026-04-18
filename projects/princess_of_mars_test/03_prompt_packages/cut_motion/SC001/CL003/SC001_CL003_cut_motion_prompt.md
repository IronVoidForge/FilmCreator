# Title
SC001 CL003 Cut Motion Prompt

# ID
SC001_CL003_cut_motion_prompt

# Purpose
Generate cut motion transition from window approach to POV exterior view and close-up on narrator's reaction, maintaining emotional weight and lighting consistency.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Camera moves towards upper floor window frame, establishing view of empty valley and hills outside, natural sunlight contrasts with dim interior room, transition to close-up shot of narrator's anxious facial expression, emotional weight conveyed through lighting and gaze, interior depth visible near window

# Negative Prompt
distorted faces, extra limbs, sudden camera jumps not in plan, bright interior lighting mismatch, crowded plaza visible through window, green martians appearing unexpectedly, text overlays, blurry motion, inconsistent lighting grade, narrator expression too neutral, wrong background environment

# Inputs
- project_id: princess_of_mars_test
- scene_id: SC001
- clip_id: CL003
- duration_seconds: 5
- required_refs: BT003.md, Scene SC001 breakdown
- optional_refs: Valley/hills landscape details, natural light contrast
- visible_character_assets: Narrator (at window), Woola (nearby)
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: POV window view → Close-up on narrator's anxious expression
- continuity_mode: insert
- starting_keyframe_strategy: Approach window position, establish exterior view first
- dependency_policy: Dependent on CL002 for spatial positioning
- auto_advance_policy: 
- fallback_strategy: Use static POV if camera movement unavailable
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 

# Continuity Notes
- Preserve keyframe lighting and grade by default
- Maintain interior dimness against exterior sunlight
- Ensure narrator's position matches previous clip end
- Avoid sudden appearance of green martians or ships in window view
- Keep Woola out of direct POV line unless specified
- Match emotional tone of abandonment through lighting and gaze

# Repair Notes
- If lighting shifts too much towards exterior brightness, dampen interior highlights
- If narrator expression is too neutral, enhance anxious micro-expressions
- Ensure window frame remains visible during transition
- Correct any drift in valley landscape consistency
- Fix sudden cuts that break the 0-2s approach to 2-4s POV flow

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/CL003.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
