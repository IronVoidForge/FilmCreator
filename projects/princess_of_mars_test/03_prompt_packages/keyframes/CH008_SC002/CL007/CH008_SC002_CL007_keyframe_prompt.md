# Title
CH008_SC002 CL007 Keyframe Prompt

# ID
CH008_SC002_CL007_keyframe_prompt

# Purpose
Establish the conclusion of the battle sequence by depicting the damaged fleet retreating from the valley floor with clear visual indicators of structural damage and smoke trails, maintaining continuity with the preceding engagement beat.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Wide aerial perspective capturing gray low-profile vessels retreating across open valley floor. Several craft displaying visible structural damage with smoke trails rising from hulls. Banners attached to stem and stern showing signs of flame damage. Glowing devices mounted on prow remain active. Ships moving away from engagement point leaving dust and debris in wake. Atmospheric lighting suggests late afternoon conditions.

# Negative Prompt
Close-up shots, human faces, green-skinned warriors in foreground, intact vessels, bright midday sun, clear sky without smoke, static composition, text overlays, logos, watermarks, sharp focus on individual crew members, vibrant colors inconsistent with damage state.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL007
- duration_seconds: 5
- required_refs: BT004.md
- optional_refs: Wide retreat tracking shots coverage families
- visible_character_assets: Enemy Fleet (multiple vessels showing damage), Smoke trails
- look_continuity_policy: Maintain damage progression consistency across interval frames
- intended_lighting_change: None
- composition_type: Wide aerial shot tracking fleet moving away from battle zone
- continuity_mode: Wide tracking shot following fleet departure from valley
- starting_keyframe_strategy: Open on fleet in damaged condition, several craft limping
- dependency_policy: Hard dependency on BT004 beat
- auto_advance_policy: 
- fallback_strategy: Use reblock_same_scene if need to adjust retreat path angle
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 

# Continuity Notes
- Ensure smoke trails originate from damaged hulls and persist throughout the retreat motion.
- Verify banners on stem and stern show progressive flame damage consistent with previous engagement shots.
- Maintain wide tracking perspective without cutting to close-ups of individual vessels unless specified in subsequent frames.
- Confirm retreat path angle matches established trajectory from valley floor exit point.

# Repair Notes
- If ship structure appears too intact, apply damage overlays to hulls and engines.
- Adjust banner opacity to reflect burning state if flame damage is inconsistent with previous beats.
- Ensure smoke density correlates with engine failure indicators on limping craft.
- Correct any perspective distortion that breaks the wide aerial tracking flow.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL007.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
