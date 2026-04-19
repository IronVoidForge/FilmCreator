# Title
CH008_SC004 CL004 Cut Motion Prompt

# ID
CH008_SC004_CL004_cut_motion_prompt

# Purpose
Interpolate motion from keyframe at ship exterior to keyframe entering building portal, maintaining lighting grade and camera POV stability. Ensure visible motion flows horizontally toward the entrance while preserving character appearance details like green skin and oval face.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
green-skinned female warriors dragging slender human prisoner into building entrance, oval face visible, interior light glowing through portal, horizontal movement forward, ship exterior background fading, dark building interior visible

# Negative Prompt
static image, distorted limbs, wrong lighting, extra characters, blurry motion, bright sunlight, ship interior details, closed eyes

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC004
- clip_id: CL004
- duration_seconds: 5
- required_refs: BT002.md
- optional_refs: POV dragging into building notes
- visible_character_assets: Female Martians, Prisoner figure, Building portal
- look_continuity_policy: preserve_keyframe_lighting
- intended_lighting_change: portal_threshold_contrast
- composition_type: POV
- continuity_mode: insert
- starting_keyframe_strategy: ship_exterior_oval_face
- dependency_policy: independent
- auto_advance_policy: none
- fallback_strategy: close_up_prisoner_face
- consistency_assist_policy: enabled
- consistency_assist_method: 
- anatomy_repair_policy: strict
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 

# Continuity Notes
- Lighting must match keyframe portal glow
- Motion should flow from ship exterior to portal entry
- Character anatomy (green skin, oval face) must remain consistent
- Camera POV must stay stable during dragging action
- Interior light contrast through portal is critical for depth

# Repair Notes
- If dragging motion looks unnatural, adjust limb connection
- Ensure interior light is visible through portal
- Fix any green skin distortion on warriors or prisoner
- Maintain horizontal axis movement toward building entrance

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CL004.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC004.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CH008_SC004_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
