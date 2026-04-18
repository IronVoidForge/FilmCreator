# Title
SC001 CL003 Cut Motion Prompt

# ID
SC001_CL003_cut_motion_prompt

# Purpose
Generate cut motion transition from window approach to POV exterior view and close-up on narrator reaction, maintaining emotional weight and lighting consistency

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Camera pushes forward through open window frame, exterior daylight floods interior space, male warrior turns head slightly towards approaching fleet, facial expression shifts from curiosity to concern, dim room shadows deepen against bright outside light

# Negative Prompt
distorted faces, extra limbs, sudden camera jumps not in plan, bright interior lighting mismatch, crowded plaza visible through window, enemy warriors appearing unexpectedly, text overlays, blurry motion, inconsistent lighting grade, wrong background environment

# Inputs
- project_id: princess_of_mars_test
- scene_id: SC001
- clip_id: CL003
- duration_seconds: 5
- required_refs: BT003.md, Scene SC001 breakdown
- optional_refs: Valley hills landscape details, natural light contrast
- visible_character_assets: male warrior at window, companion hound nearby
- look_continuity_policy: preserve keyframe lighting and grade by default
- intended_lighting_change: interior dimness against exterior sunlight
- composition_type: POV window view to close-up on narrator anxious expression
- continuity_mode: insert
- starting_keyframe_strategy: Approach window position, establish exterior view first
- dependency_policy: Dependent on CL002 for spatial positioning
- auto_advance_policy: none
- fallback_strategy: Use static POV if camera movement unavailable
- consistency_assist_policy: enable
- consistency_assist_method: lighting grade match
- anatomy_repair_policy: strict
- consistency_targets: window frame, valley landscape, facial expression
- style_profile: cinematic_compositional
- batch_role: cut_motion
- fix_of: none

# Continuity Notes
- Preserve keyframe lighting and grade by default
- Maintain interior dimness against exterior sunlight
- Ensure narrator position matches previous clip end
- Avoid sudden appearance of enemy warriors or ships in window view
- Keep companion hound out of direct POV line unless specified
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
