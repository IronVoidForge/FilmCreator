# Title
CH008_SC002 CL003 Keyframe Prompt

# ID
CH008_SC002_CL003_keyframe_prompt

# Purpose
Establish the opening state of the enemy vessel's return fire sequence, capturing the initial broadside positioning before the full swing arc completes.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Gray low-profile airship vessel with banners on stem and stern, glowing devices on prow, crew members positioned on deck for firing operations, smoke trails from active weapons, valley floor visible in background, dynamic aerial perspective, wide shot composition, weapons charging state, green-skinned warriors in building windows firing downward, distant hills under cloudy sky.

# Negative Prompt
Blurry, distorted anatomy, static composition, wrong color palette, missing banners, obscured details, low resolution, text overlays, human faces not matching continuity, bright daylight without atmospheric haze, ship rotation incomplete, crew members frozen unnaturally.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL003
- duration_seconds: 5
- required_refs: BT002.md
- optional_refs: Scene breakdown for ship swing arc completion verification
- visible_character_assets: Enemy Fleet (lead vessel), Crew on deck, Smoke trails
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: Wide aerial shot tracking lead vessel's 360-degree swing
- continuity_mode: Dynamic aerial tracking shot following ship movement
- starting_keyframe_strategy: Open on ship in initial position, weapons charging
- dependency_policy: Hard dependency on BT002 beat; must show full circle completion
- auto_advance_policy: 
- fallback_strategy: Use reblock_same_scene if swing arc timing needs adjustment
- consistency_assist_policy: Apply to smoke trails and weapon glow intensity
- consistency_assist_method: 
- anatomy_repair_policy: Enable for crew members on deck
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 
- workflow_type: still.scene_build.four_ref.klein.distilled

# Continuity Notes
- Maintain ship swing arc progression from initial position to full circle.
- Ensure banner damage tracks with previous shots in the sequence.
- Keep crew positioning consistent with firing operations and weapon discharge timing.
- Verify valley floor perspective remains stable across tracking frames.

# Repair Notes
- Apply anatomy repair policy for crew members if distortion occurs during swing.
- Use consistency assist method to align smoke trails and weapon glow intensity.
- Check ship rotation angle against beat bundle requirements for full circle completion.
- Adjust banner flame damage progression to match visual continuity from earlier shots.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL003.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
