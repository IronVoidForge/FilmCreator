# Title
CH008_SC002 CL008 Scene Stage Prompt

# ID
CH008_SC002_CL008_scene_stage_prompt

# Purpose
Define the visual resolution of the airship salvage sequence, focusing on the wide shot of the burning vessel being towed away from the valley city, establishing finality for the battle and transition to the next narrative beat.

# Workflow Type
authoring.scene_stage

# Positive Prompt
Wide angle view of a large gray airship engulfed in flames being towed across the valley floor. Green Martian warriors operate heavy towing machinery near the vessel's hull. Smoke billows upward into the sky. In the background, deserted city buildings and hills are visible under daylight transitioning to fire glow. Camera maintains static wide composition showing ship departure path.

# Negative Prompt
No visible crew members on ship deck, no intact hull sections remaining, no additional airships in frame, no human faces other than narrator if applicable, no green skin on Martians, no daylight without fire glow transition, no distorted towing equipment.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL008
- duration_seconds: 5.0
- required_refs: Ship fully consumed by fire, towing equipment deployed, ship moving away from building
- optional_refs: Window frame
- visible_character_assets: Martians operating towing equipment; Narrator watching resolution
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: Wide/POV
- continuity_mode: cutaway
- starting_keyframe_strategy: static_hold
- dependency_policy: linear_sequence
- auto_advance_policy: 
- fallback_strategy: cut_to_previous_angle
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 

# Continuity Notes
- Ensure ship is fully ablaze before tow begins. Towing equipment must be visible and functional. Maintain wide shot composition throughout resolution. Narrator's POV must align with window frame obstruction.

# Repair Notes
- If ship flame intensity is low, increase fire coverage on hull. If Martian anatomy is distorted, apply repair policy for green skin and muscular build.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL008.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
