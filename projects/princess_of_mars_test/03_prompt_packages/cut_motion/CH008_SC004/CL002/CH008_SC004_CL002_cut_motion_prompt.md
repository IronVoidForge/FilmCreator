# Title
CH008_SC004 CL002 Cut Motion Prompt

# ID
CH008_SC004_CL002_cut_motion_prompt

# Purpose
Define the stage intent for CL002 cut motion within CH008_SC004. Establish the transition from ship interior view to wide exterior shot while maintaining dragging action continuity and dim industrial lighting grade. Focus on camera behavior following movement trajectory and environment change from interior to exterior portal threshold.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Wide shot gray ship hull exterior open portal green-skinned warriors dragging slender human figure dim industrial lighting building interior light contrast camera panning out movement trajectory visible motion camera following subject path environment transition interior to exterior

# Negative Prompt
bright sunlight clear sky distorted anatomy missing limbs static image low resolution watermark text extra fingers morphing objects wrong color palette overexposed shadows blurry details

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC004
- clip_id: CL002
- duration_seconds: 5
- required_refs: BT001.md, BT002.md
- optional_refs: Wide shot warriors dragging action notes
- visible_character_assets: Green Warriors, Human Woman, Female Martians
- look_continuity_policy: dim lighting, industrial texture
- intended_lighting_change: interior to exterior transition
- composition_type: Wide ship exterior showing portal
- continuity_mode: cutaway
- starting_keyframe_strategy: Starting keyframe interior to exterior transition
- dependency_policy: No hard dependencies - can be shot independently
- auto_advance_policy: 
- fallback_strategy: Use medium shot warriors dragging if wide unavailable
- consistency_assist_policy: Maintain character appearance details (slender girlish figure)
- consistency_assist_method: 
- anatomy_repair_policy: Ensure green skin and prisoner features are clear
- consistency_targets: 
- style_profile: Industrial, dim, Martian city aesthetic
- batch_role: Cut Motion Stage
- fix_of: 
- workflow_type: video.cut_motion.wan.i2v

# Continuity Notes
- Preserve keyframe lighting and grade by default (dim industrial texture).
- Maintain camera behavior following movement trajectory from interior to exterior.
- Ensure environment change reflects ship hull boundary and open portal visibility.
- Keep character continuity for green-skinned warriors and slender human figure appearance.
- Avoid sudden brightness shifts that contradict the dim lighting policy.

# Repair Notes
- If lighting shifts too bright, revert to dim industrial state immediately.
- Ensure portal remains open as per ending keyframe intent during motion.
- Correct any morphing of ship hull or warrior anatomy during transition.
- Verify dragging motion is continuous across the cut without snapping.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CL002.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC004.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CH008_SC004_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
