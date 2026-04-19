# Title
CH008_SC005 CL004 Fix 01 Prompt

# ID
CH008_SC005_CL004_fix_01_prompt

# Purpose
Corrective still-generation prompt that preserves medium background shot composition with prisoner being dragged through corridor depth, maintaining visual continuity from CL003 emotional context while fixing local rendering issues on prisoner figure and dragging motion clarity.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
Medium background shot of interior corridor with upper floors and windows visible in distance, slender girlish human female prisoner with light reddish copper skin being dragged right to left through background view, coal black hair waving caught loosely into strange coiffure, large lustrous eyes visible, highly wrought ornaments on body, Green Martian females dragging her by arms, daylight lighting with smoke from fire and missile impact flames in air, corridor depth showing architectural structure, urgency atmosphere, prisoner full body visible in background plane, minimal foreground presence for depth reference, Martian city building interior environment.

# Negative Prompt
close-up on faces, wrong character placement, missing prisoner figure, inconsistent lighting between foreground and background, wrong skin tone on prisoner, hair not coal black, ornaments missing or wrong style, corridor walls too plain, daylight without smoke effects, prisoner facing wrong direction, dragging motion unclear, Green Martians with wrong skin color, anatomy distortion on prisoner limbs, fire flames in wrong location, building interior too open like plaza.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC005
- clip_id: CL004
- duration_seconds: 5
- required_refs: CH008_SC005/BEAT_INDEX.md BT002, CH008_SC005/BT002.md Start State
- optional_refs: None
- visible_character_assets: prisoner_human_female
- look_continuity_policy: maintain Martian city building interior aesthetic from chapter description
- intended_lighting_change: preserve daylight with smoke and fire effects from corridor scene
- composition_type: medium background shot
- continuity_mode: cutaway
- starting_keyframe_strategy: static frame showing corridor depth with prisoner moving right to left in background
- dependency_policy: depends on CL003 establishing emotional context; no reverse dependency
- auto_advance_policy: hold on prisoner movement before transition to CL005
- fallback_strategy: tighten to close-up on prisoner face or widen to show more dragging motion if action unclear
- consistency_assist_policy: preserve prisoner visual characteristics from chapter description
- consistency_assist_method: match skin tone, hair color, ornament style from canonical character index
- anatomy_repair_policy: ensure prisoner figure maintains slender girlish proportions with correct limb placement
- consistency_targets: prisoner_human_female physical presence and movement trajectory
- style_profile: Martian city building interior with daylight smoke fire effects
- batch_role: still_fix corrective iteration
- fix_of: CH008_SC005_CL004_fix_01_prompt previous version

# Continuity Notes
- Maintain prisoner visual characteristics from chapter description: light reddish copper skin, coal black hair in strange coiffure, large lustrous eyes, highly wrought ornaments, slender girlish figure
- Preserve corridor depth showing architectural structure with upper floors and windows visible in distance
- Keep dragging motion right to left through background plane consistent with starting keyframe strategy
- Match daylight lighting with smoke from fire and missile impact flames in air from environment index
- Ensure Green Martian females dragging prisoner maintain green skin and ornament style from character index
- Hold on prisoner movement before transition to CL005 eye contact reaction shot
- Preserve emotional context from CL003 where Sola reaches Carter while showing conflict element in background

# Repair Notes
- Fix any rendering issues on prisoner figure skin tone to match light reddish copper from chapter description
- Correct hair color to coal black with waving texture caught loosely into strange coiffure
- Ensure ornaments are highly wrought and visible on prisoner body as per character index
- Repair dragging motion clarity to show right to left movement through corridor depth
- Fix any anatomy distortion on prisoner limbs to maintain slender girlish proportions
- Correct lighting consistency between foreground corridor structure and background prisoner figure
- Ensure smoke from fire and missile impact flames appear in air without overwhelming scene composition
- Maintain medium background shot composition without shifting to close-up or wide unless fallback needed

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC005/CL004.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC005.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC005/CH008_SC005_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
