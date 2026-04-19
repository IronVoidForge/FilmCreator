# Title
CH008_SC002 CL007 Cut Motion Prompt

# ID
CH008_SC002_CL007_cut_motion_prompt

# Purpose
Execute funeral pyre ritual through wide-to-medium shots establishing solemnity and emotional climax. Camera transitions from wide shot showing entire burning ship to medium shots of Martians around fire; cuts between fire and observer reactions.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Green Martian warriors surrounding gray airship fully ablaze, flames consuming hull structure, thick smoke rising into valley sky, warm fire glow illuminating faces, solemn atmosphere, camera panning across burning vessel, window frame visible in foreground, Narrator observing ritual from distance, fire flickering intensely, no crew remaining on deck.

# Negative Prompt
Human crew members, ship not burning, cold daylight without fire illumination, distorted Martian anatomy, sudden lighting changes unrelated to fire, missing limbs, wrong character count, blurry fire effects, green skin turning brown.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL007
- duration_seconds: 5.0
- required_refs: Ship fully ablaze, smoke rising, fire consuming ship structure, no visible crew remaining
- optional_refs: Window frame
- visible_character_assets: Martians surrounding burning ship; Narrator observing pyre ritual
- look_continuity_policy: reframe_same_moment
- intended_lighting_change: Fire illumination dominant, warm glow on faces
- composition_type: Wide/Medium/POV
- continuity_mode: reframe_same_moment
- starting_keyframe_strategy: pan_across
- dependency_policy: linear_sequence
- auto_advance_policy: 
- fallback_strategy: 
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 

# Continuity Notes
- Maintain fire intensity and ship consumption state throughout motion sequence.
- Ensure camera transitions align with wide-to-medium shot progression described in beat plan.
- Preserve window frame visibility if present to anchor Narrator POV perspective.
- Keep Martian green skin tone consistent under fire illumination without washing out.

# Repair Notes
- If ship appears not fully ablaze, increase fire intensity and smoke density in prompt.
- If crew members appear on deck, remove them to match required refs.
- If lighting shifts away from warm fire glow, correct to maintain ritual solemnity.
- Ensure Martians remain surrounding the ship rather than moving away prematurely.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL007.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
