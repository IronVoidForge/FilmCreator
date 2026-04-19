# Title
CH008_SC005 CL004 Cut Motion Prompt

# ID
CH008_SC005_CL004_cut_motion_prompt

# Purpose
Introduce conflict element via background action; show prisoner's desperate state without interrupting emotional flow between Carter and Sola. Cut from CL003 close-up to this background cutaway as Sola reaches Carter, creating contrast between connection and conflict.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Corridor depth view, static foreground reference, slender human female prisoner moving right to left in background, dragging motion evident, daylight lighting with smoke haze, distant hills visible beyond corridor opening, Green Martian females pulling prisoner through view, fire glow from burning ship in distance, medium background shot composition.

# Negative Prompt
distorted anatomy, sudden jump cuts, close up on faces, static image, blurry motion, extra limbs, wrong lighting night, distorted background, flickering fire, morphing characters, foreground interruption, wrong character focus.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC005
- clip_id: CL004
- duration_seconds: 5
- required_refs: CH008_SC005/BEAT_INDEX.md BT002, CH008_SC005/BT002.md Start State
- optional_refs: None
- visible_character_assets: Prisoner (full body visible in background)
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: Medium background shot
- continuity_mode: cutaway
- starting_keyframe_strategy: Static frame showing corridor depth with prisoner moving right-to-left in background
- dependency_policy: Depends on CL003 establishing emotional context; no reverse dependency
- auto_advance_policy: 
- fallback_strategy: If prisoner action unclear, tighten to close-up on prisoner's face or widen to show more of dragging motion
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 

# Continuity Notes
- Maintain keyframe lighting and grade from CL003. Ensure prisoner moving right-to-left in background without foreground interruption. Keep corridor depth static. Match fire glow intensity from burning ship.

# Repair Notes
- If prisoner movement appears jerky, apply smoothing filter. If background shifts unnaturally, stabilize camera. Check anatomy of dragging figures.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC005/CL004.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC005.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC005/CH008_SC005_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
