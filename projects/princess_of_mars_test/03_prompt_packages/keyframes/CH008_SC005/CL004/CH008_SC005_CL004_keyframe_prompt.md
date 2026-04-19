# Title
CH008_SC005 CL004 Keyframe Prompt

# ID
CH008_SC005_CL004_keyframe_prompt

# Purpose
Establish emotional anchor through close-up reaction on primary character face showing visual connection and processing of background conflict; static frame capturing single moment of emotional impact without interruption from foreground movement or background action; medium shot composition with clear sightlines to all parties maintaining continuity across reaction shots

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Exterior corridor entrance threshold with daylight lighting and smoke from fire effects visible in atmosphere. Close-up on primary character face showing emotional processing and visual awareness of approaching figure. Background elements visible for spatial context including building upper floor windows and corridor depth perspective. High contrast shadows from fire smoke creating mood without obscuring facial features. Static frozen still capturing single moment of emotional reaction to established visual connection. Daylight illumination with atmospheric haze from smoke effects. Clear sightlines between all parties maintaining continuity across shots

# Negative Prompt
No medium background shots or full body figures visible in frame. No close-up shots on secondary character face or facial features. No foreground characters interrupting emotional connection flow. No interior room shots or enclosed spaces. No explosion or dramatic destruction visible in this frame. No reverse shot angle or different perspective. No sudden camera movement or dynamic action sequences. No proper nouns or character names appearing in visual description

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC005
- clip_id: CL004
- duration_seconds: 5
- required_refs: CH008_SC005/BEAT_INDEX.md BT003, CH008_SC005/BT003.md Start State
- optional_refs: None
- visible_character_assets: Primary character (face focus), background elements for context
- look_continuity_policy: Emotional anchor continuity with clear sightlines to all parties
- intended_lighting_change: Daylight with atmospheric haze from smoke effects
- composition_type: Close-up reaction shot
- continuity_mode: emotional_anchor
- starting_keyframe_strategy: Static frame showing primary character face processing visual connection
- dependency_policy: Depends on CL003 establishing emotional context; no reverse dependency
- auto_advance_policy: Cut to CL005 if wide three-shot needed for full emotional context
- fallback_strategy: Tighten to extreme close-up if facial expression unclear or widen to show more background elements
- consistency_assist_policy: Maintain character position and lighting state across reaction shots
- consistency_assist_method: Reference previous shot composition and lighting conditions
- anatomy_repair_policy: Ensure facial features remain clear without smoke obscuration
- consistency_targets: Primary character face focus, background elements for spatial context
- style_profile: Cinematic compositional with atmospheric effects
- batch_role: Emotional anchor keyframe
- fix_of: CL003 establishing emotional context
- workflow_type: still.scene_build.four_ref.klein.distilled

# Continuity Notes
- Close-up reaction shot establishing emotional impact of visual connection between all parties
- Primary character face focus showing processing of background conflict without interruption
- Static frame composition maintaining continuity across reaction shots
- Background elements visible for spatial context including building windows and corridor depth
- Depends on CL003 close-up establishing emotional context before this reaction shot
- Clear sightlines between all parties maintaining visual connection across shots

# Repair Notes
- If facial expression unclear, tighten framing to extreme close-up for better detail
- If smoke obscuration too heavy, reduce atmospheric haze intensity while maintaining mood
- If background elements insufficient, widen shot slightly to show more corridor depth and windows
- If visual connection not clear, adjust eyeline direction to establish gaze dynamics
- If continuity breaks between shots, reference previous composition and lighting conditions
- If emotional impact insufficient, enhance facial expression detail without proper nouns

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC005/CL004.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC005.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC005/CH008_SC005_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
