# Title
CH008_SC002 CL002 Scene Stage Prompt

# ID
CH008_SC002_CL002_scene_stage_prompt

# Purpose
Establish the volley fire sequence from a building window perspective to escalate tension during the aerial conflict. Depict Martian warriors firing projectiles at approaching gray airships while maintaining continuity with the initial approach phase. Focus on muzzle flash illumination and projectile impact registration without premature structural failure or boarding visuals.

# Workflow Type
authoring.scene_stage

# Positive Prompt
Martian warriors positioned at multi-story building windows, gray airships descending over valley floor, muzzle flashes erupting from window frames, projectiles arcing through sky, hills beyond city visible, daylight illumination with fire glow accents, narrator observing from interior, smoke rising from hull impacts, deserted buildings intact.

# Negative Prompt
Airship crew visible on deck, building structures collapsing or damaged, Earthling woman present in plaza, loot items collected prematurely, close-up of ship boarding equipment, night lighting conditions, structural breaches without fire, Martians leaving window positions during volley sequence.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL002
- duration_seconds: 5.0
- required_refs: Muzzle flashes, projectile impacts on ship hulls
- optional_refs: Window frame
- visible_character_assets: Martians at building windows (active), Narrator observing from window
- look_continuity_policy: reframe_same_moment
- intended_lighting_change: Daylight to dramatic fire illumination during salvage sequence
- composition_type: Medium/Close-up
- continuity_mode: reframe_same_moment
- starting_keyframe_strategy: pan_in
- dependency_policy: linear_sequence
- auto_advance_policy: cut_to_previous_angle
- fallback_strategy: insert
- consistency_assist_policy: linear_sequence
- consistency_assist_method: reblock_same_scene
- anatomy_repair_policy: consistent_targets
- consistency_targets: Number of ships (20), specific loot items, state of burning ship
- style_profile: Urban Transit Settings, Combat Cover Environments
- batch_role: BT002
- fix_of: CL001

# Continuity Notes
- Maintain count of twenty approaching vessels throughout sequence.
- Ensure projectile impacts register on hulls without immediate structural failure or explosion.
- Martians remain at window positions during volley sequence; no boarding equipment visible yet.
- Lighting shifts from daylight to dramatic fire glow only after salvage begins (BT007).
- Window POV establishes narrator's vantage point throughout scene.
- Damage progression must align with BT003 wide coverage shots for subsequent beats.

# Repair Notes
- Sync muzzle flash timing precisely with projectile trajectory across valley floor.
- Verify no boarding equipment visible yet; salvage sequence begins in BT004/BT005.
- Ensure hull damage is visible but not catastrophic until BT003 transition.
- Check that Martians do not leave window positions prematurely during volley fire.
- Confirm lighting remains daylight with fire glow accents only, avoiding night conditions.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL002.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
