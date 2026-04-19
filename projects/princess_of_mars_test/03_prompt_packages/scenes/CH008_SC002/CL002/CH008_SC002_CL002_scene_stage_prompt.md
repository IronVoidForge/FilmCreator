# Title
CH008_SC002 CL002 Scene Stage Prompt

# ID
CH008_SC002_CL002_scene_stage_prompt

# Purpose
Establish coordinated volley fire sequence from building window perspective to escalate aerial conflict tension. Depict Green Martian warriors discharging projectiles at approaching gray airships while maintaining structural continuity with initial approach phase. Focus on muzzle flash illumination and projectile impact registration without premature structural failure or boarding equipment visibility.

# Workflow Type
authoring.scene_stage

# Positive Prompt
Green Martian hands positioned at multi-story building window frames, gray airships descending over valley floor, muzzle flashes erupting from weapon barrels, projectiles arcing through daylight sky, hills beyond city visible, smoke rising from hull impact points, deserted buildings structurally intact, fire glow accents illuminating scene.

# Negative Prompt
Airship crew members visible on forward decks, building structures collapsing or damaged, Earthling woman present in plaza area, loot items collected prematurely, boarding equipment visible on airships, night lighting conditions, structural breaches without fire effects, Martians leaving window positions during volley sequence.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL002
- duration_seconds: 5.0
- required_refs: Muzzle flashes, projectile impacts on ship hulls
- optional_refs: Window frame structure
- visible_character_assets: Martians at building windows (active), Narrator observing from window interior
- look_continuity_policy: reframe_same_moment
- intended_lighting_change: Daylight with dramatic fire glow accents during salvage sequence
- composition_type: Close-up
- continuity_mode: reframe_same_moment
- starting_keyframe_strategy: motion blur on weapon barrel
- dependency_policy: parallel to wide shot for coverage
- auto_advance_policy: cut_to_previous_angle
- fallback_strategy: insert
- consistency_assist_policy: linear_sequence
- consistency_assist_method: reblock_same_scene
- anatomy_repair_policy: consistent_targets
- consistency_targets: Number of ships (20), specific loot items, state of burning ship
- style_profile: Urban Transit Settings, Combat Cover Environments
- batch_role: BT001
- fix_of: CL001

# Continuity Notes
- Maintain count of twenty approaching vessels throughout sequence.
- Ensure projectile impacts register on hulls without immediate structural failure or explosion.
- Martians remain at window positions during volley sequence; no boarding equipment visible yet.
- Lighting shifts from daylight to dramatic fire glow only after salvage begins in subsequent beat.
- Window POV establishes narrator's vantage point throughout scene.
- Damage progression must align with BT003 wide coverage shots for subsequent beats.

# Repair Notes
- Sync muzzle flash timing precisely with projectile trajectory across valley floor.
- Verify no boarding equipment visible yet; salvage sequence begins in subsequent beat.
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
