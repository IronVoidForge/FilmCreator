# Title
CH008_SC002 CL006 Cut Motion Prompt

# ID
CH008_SC002_CL006_cut_motion_prompt

# Purpose
Depict fleet returning fire with arcs towards ridge, debris falling from impacts, daylight illumination, green Martian fleet crew members firing return volley.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Wide shot of fleet ships firing return volley, fire arcs towards ridge, debris falling from impacts, daylight illumination, green Martian fleet crew members, ship storage areas accessible, resource acquisition details, valley floor marked with previous damage

# Negative Prompt
close-up framing, static hold, blurry focus, distorted hands, morphing items, narration voice, dark shadows, smoke (unless impact), crew activity, resistance

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL006
- duration_seconds: 5.0
- required_refs: BT002 index, CL005 close-up
- optional_refs: Window frame
- visible_character_assets: Fleet ships, return fire vectors
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: Wide shot
- continuity_mode: cut
- starting_keyframe_strategy: static on valley floor
- dependency_policy: sequential to broadside formation change
- auto_advance_policy: 
- fallback_strategy: insert debris falling if fire arcs heavy
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 

# Continuity Notes
- Maintain wide shot framing on fleet ships and fire arcs throughout the sequence.
- Ensure fleet ships appear consistent with previous shots in scene (BT001).
- Preserve lighting continuity from salvage sequence (daylight or storage illumination).
- Avoid showing crew activity or resistance on the ship deck.

# Repair Notes
- Fix any anatomy distortions on crew members firing weapons to ensure natural grip.
- Ensure fire arcs do not morph into each other during cuts.
- Correct any lighting shifts that deviate from the approved keyframe grade.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL006.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
