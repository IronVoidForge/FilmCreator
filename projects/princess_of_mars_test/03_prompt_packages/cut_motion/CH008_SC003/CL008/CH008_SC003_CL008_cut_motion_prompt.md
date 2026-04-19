# Title
CH008_SC003 CL008 Cut Motion Prompt

# ID
CH008_SC003_CL008_cut_motion_prompt

# Purpose
Track drifting burning ship southeast, maintain continuity with CL007, show fire spread and ash scatter.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
burning gray low-profile vessel drifting southeast vector smoke plume ash scattering water surface fire intensity increasing urban Martian valley background distant green warriors observing funeral pyre atmosphere warm glow cool sky contrast

# Negative Prompt
static image sudden movement human figures on vessel cold fire distorted smoke flickering grade extra limbs morphing hull wrong lighting shift

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC003
- clip_id: CL008
- duration_seconds: 5
- required_refs: BT003.md Scene Summary
- optional_refs: Continuity Notes
- visible_character_assets: None on vessel Warriors distant
- look_continuity_policy: insert
- intended_lighting_change: consistent with CL007
- composition_type: tracking shot
- continuity_mode: insert
- starting_keyframe_strategy: open on burning ship drift vector
- dependency_policy: depends on CL007
- auto_advance_policy: smooth drift follow
- fallback_strategy: cutaway if needed
- consistency_assist_policy: enabled
- consistency_assist_method: frame interpolation
- anatomy_repair_policy: disabled
- consistency_targets: ship hull smoke fire
- style_profile: cinematic war drama
- batch_role: tracking shot
- fix_of: CL007

# Continuity Notes
- Maintain southeast drift vector throughout. Ensure fire spread pattern matches BT003 start state. Ash scattering must align with wind direction established in previous clips.

# Repair Notes
- If smoke coherence breaks, re-render with stronger diffusion guidance. If lighting shifts too cool, warm up highlights to match funeral pyre glow.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CL008.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC003.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CH008_SC003_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
