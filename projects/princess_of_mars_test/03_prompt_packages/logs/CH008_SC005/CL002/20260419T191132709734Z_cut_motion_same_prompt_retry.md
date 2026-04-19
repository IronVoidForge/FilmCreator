# FilmCreator Prompt Writing Exchange
- timestamp_utc: 2026-04-19T19:11:32.710234+00:00
- stage: cut_motion
- clip_id: CL002
- retry_kind: same_prompt_retry

## System Prompt
````text
You are writing one FilmCreator prompt package for a local generation pipeline.
Your first output line must be exactly [[FILMCREATOR_PACKET]].
Your last output line must be exactly [[/FILMCREATOR_PACKET]].
Return exactly one FILMCREATOR packet in Markdown.
Do not return JSON.
Do not use markdown fences.
Do not add commentary before or after the packet.
Do not omit the outer packet envelope.
Target stage: cut_motion
Stage guidance: Write a short-cut motion prompt that starts from the approved opening frame. Preserve the keyframe lighting and grade by default. Focus on visible motion, camera behavior, and environment change.
Use descriptive noun phrases and avoid proper nouns in prompt text.
Keep duration and workflow metadata in inputs_markdown, not in the prompt body.
Follow the requested section names exactly.
````

## User Prompt
````text
Project: princess_of_mars_test

Scene: CH008_SC005

Clip: CL002

Prompt title: CH008_SC005 CL002 Cut Motion Prompt

Prompt id: CH008_SC005_CL002_cut_motion_prompt

Workflow type: video.cut_motion.wan.i2v

Write improved content for this canonical prompt package.

Output rules:

1. First line must be [[FILMCREATOR_PACKET]]

2. Last line must be [[/FILMCREATOR_PACKET]]

3. No text before the first line

4. No text after the last line

5. Every required section must appear exactly once



Use this exact packet envelope and section names:

[[FILMCREATOR_PACKET]]

task: clip_prompt

stage: cut_motion

version: 1



[[SECTION purpose]]

...purpose text...

[[/SECTION]]



[[SECTION positive_prompt]]

...positive prompt text...

[[/SECTION]]



[[SECTION negative_prompt]]

...negative prompt text...

[[/SECTION]]



[[SECTION inputs_markdown]]

- key: value

[[/SECTION]]



[[SECTION continuity_notes_markdown]]

- note

[[/SECTION]]



[[SECTION repair_notes_markdown]]

- note

[[/SECTION]]

[[/FILMCREATOR_PACKET]]



Clip context:

## Project Summary

# Project Summary

**Title:** A Princess of Mars Test Project
**Slug:** princess_of_mars_test

**Setting:** Barsoom (Mars). Primary locations include a large Martian city with spacious doorways, upper floors, roofs, and the surrounding valley/hills. The environment features open plains and distant hills.

**Key Characters:**
- **John Carter:** Human protagonist, observer of events from windows/roofs.
- **Sola:** Companion, present in the plaza and procession.
- **Woola:** Hound companion, follows Carter closely.
- **Green Martians:** Warriors inhabiting the city buildings; use chariots, mastodons, mounted warriors.
- **Air Fleet Crews:** Operate large gray-painted air craft with wireless finding apparatus.

**Core Themes:** Aerial warfare, inter-species conflict (Green Martians vs. Air Fleet), rescue operations, discovery of new life forms.

**Tone:** Action-oriented, awe-inspiring, tense during combat sequences, melancholic regarding the destruction of the fleet.

## Chapter Summaries

## CH008_summary.md
# Chapter Summary: CH008 - A Fair Captive from the Sky

## Story Summary
The narrative begins on the third day after an incubator ceremony. The procession retreats to a city building due to an immediate order. From a window, John Carter observes the arrival of twenty large gray air craft. A battle ensues between Green Martians firing from buildings and the Air Fleet returning fire. The fleet retreats after damage; one ship is disabled and unmanned. Warriors loot the vessel (arms, jewels, water), burn it, and tow it away before it explodes. Carter witnesses a human female prisoner being dragged from the burning ship into a nearby building by Green Martian females. At the city plaza, the prisoner turns to Carter as she enters the building; he fails to respond to her signal of appeal. She is dragged away into the depths of the edifice.

## Visual Continuity
- **Air Craft:** Long, low, gray-painted vessels with strange banners and odd devices on prows. Figures crowd forward decks.
- **Green Martians:** Green skin, wear ornaments, carry spears, fire from windows/roofs.
- **Prisoner:** Slender, girlish figure. Skin is light reddish copper. Features finely chiseled. Eyes large/lustrous. Hair coal black, waving, caught loosely into a strange coiffure. Naked except for highly wrought ornaments. Cheeks crimson, lips ruby.
- **Locations:** City buildings (upper floors, windows, roofs), open ground/plaza, valley, hills beyond.
- **Action Details:** Ships swing broadside, dip below hill crests, drift southeast/southwesterly. Fire causes spurt of flame from missile impact. Guy ropes release simultaneously.

## Character Index

# Character Index - Chapter CH008

| Asset ID | Canonical Character ID | Display Name | Role | Physical Presence |
|----------|------------------------|--------------|------|-------------------|
| john_carter | john_carter | John Carter | Observer, Witness | Present |
| human_female_prisoner | prisoner_human_female | Human Female Prisoner | Captive, Appeal Signal | Referenced |
| green_martian_warriors | green_martian_warrior | Green Martian Warriors | Combatants, Looters | Referenced |
| green_martian_females | green_martian_female | Green Martian Females | Draggers, Enforcers | Referenced |

**Notes:**
- John Carter: Physically present observing from window; witnesses prisoner's appeal
- Human Female Prisoner: Detailed visual description provided in chapter; signals to Carter
- Green Martians: Multiple individuals; described as group with consistent physical traits
- All characters have sufficient identification for continuity tracking

## Environment Index

# Environment Index - CH008

## Extracted Environments

| Asset ID | Role | Primary Geography | Atmosphere Cues |
|----------|------|-------------------|-----------------|
| city_buildings | primary | urban structures, upper floors, windows, roofs | daylight, smoke from fire, missile impact flames |
| open_ground_plaza | transit | open ground, plaza area | daylight, spurt of flame from impacts |
| valley | secondary | valley floor beyond city | daylight, distant horizon |
| hills_beyond | secondary | hill crests, slopes southeast/southwesterly | daylight, dip below crests |

## Environment Families Summary

- **city_buildings**: Primary observation and action setting with multiple levels
- **open_ground_plaza**: Transit zone for fleet movement and battle effects
- **valley**: Background geography establishing scale
- **hills_beyond**: Distant geography providing directional context

## Clip Plan

# CL002 - Prisoner Dragged Through View (Conflict Introduction)

## Continuity Mode
- **Mode**: cutaway_to_action
- **Policy**: Ensure background movement continuity; prisoner's clothing state must match BT002 start/end.

## Composition Type
- **Type**: wide_shot
- **Focus**: Full background movement showing building entrance threshold and interior.

## Starting Keyframe Strategy
- **Strategy**: insert_from_background
- **Intent**: Begin with prisoner visible in background plane, moving right-to-left across entrance.

## Dependency Policy
- **Policy**: reblock_same_scene
- **Fallback**: If wide shot unavailable, use medium shot (Carter/Sola foreground with prisoner visible in background).

## Fallback Strategy
- **Fallback**: rack_focus_between_foreground_and_background if depth layering is critical for coverage.

## Visible Character Assets
- **Prisoner**: Full body visible in background plane, dragging motion through entrance.
- **Carter**: Upper body visible in foreground observing prisoner movement.
- **Sola**: May be partially visible in foreground reacting to prisoner's appearance.

## Required Refs
- `projects/princess_of_mars_test/02_story_analysis/beat_bundles/CH008_SC005/BEAT_INDEX.md`
- `projects/princess_of_mars_test/02_story_analysis/beat_bundles/CH008_SC005/BT002.md`

## Optional Refs
- `projects/princess_of_mars_test/02_story_analysis/shot_plans/CL002_shot_plan.md` (if exists)

## Opening Keyframe Intent
- **Intent**: Establish prisoner's forced movement and threat presence; maintain depth layering.

## Cut Motion Intent
- **Motion**: smooth_background_trajectory
- **Note**: Ensure prisoner's movement vector is clear without obscuring foreground characters.

## Interval Beats
- **Beat 1 (0s-2s)**: Prisoner enters frame right, moving left across building entrance threshold.
- **Beat 2 (2s-4s)**: Prisoner continues dragging motion through interior; Carter/Sola observe movement.
- **Beat 3 (4s-5s)**: Prisoner disappears into building interior; establishing threat/conflict presence.

## Scene Breakdown

# CH008_SC005 - Carter & Prisoner Connection

## Scene Purpose
Establish connection between Carter and prisoner through Sola's intervention.

## Scene Summary
Sola rushes to Carter, glimpse of prisoner dragged into building, eye contact established between all parties.

## Staging Facts
- **Location**: Exterior corridor / Building entrance threshold
- **Axis**: Sola enters from left; Carter stands center-right facing camera; Prisoner moves background right-to-left
- **Time**: Immediate urgency (Sola's rush implies chase or rescue)
- **Key Props**: None specific, focus on physical movement and gaze

## Beat Breakdown
1. **BT001**: Sola Rushes In (Connection Initiation)
2. **BT002**: Prisoner Dragged Through View (Conflict Introduction)
3. **BT003**: Eye Contact & Reaction (Emotional Anchor)

## Beat Bundles

## BT001.md
# BT001 - Sola Rushes In (Connection Initiation)

## Beat Purpose
Initiate connection between Carter and Sola through urgent physical approach.

## Start State
Sola visible at distance, moving toward Carter who stands stationary center-right.

## End State
Sola reaches Carter's position, establishes physical contact or close proximity.

## Character Placement & Movement Logic
- **Sola**: Enters from left frame, diagonal movement toward center-right where Carter stands
- **Carter**: Stationary, facing camera, minimal movement during beat
- **Prisoner**: Background movement right-to-left, out of primary focus but present

## Geography, Axis, Eyeline Facts
- Primary axis: Left-to-center-right (Sola to Carter)
- Secondary axis: Background right-to-left (Prisoner movement)
- Eyeline: Sola's gaze directed at Carter; Carter's gaze initially neutral then reactive

## Prop, Vehicle, Crowd, Environmental State
- **Environment**: Exterior corridor with building entrance threshold visible
- **Crowd**: Minimal to none, focus on three main characters
- **Props**: None specific, emphasis on physical presence and movement
- **Continuity**: Sola's clothing state upon arrival affects subsequent scene coverage

## Likely Coverage Families
- Wide two-shot (Sola approaching Carter)
- Medium close-up (Carter reaction)
- Over-the-shoulder (Sola's perspective of Carter)
- Tracking shot following Sola's movement

## BT002.md
# BT002 - Prisoner Dragged Through View (Conflict Introduction)

## Beat Purpose
Introduce conflict element through prisoner's forced movement across frame.

## Start State
Prisoner visible in background, moving right-to-left across building entrance threshold.

## End State
Prisoner disappears into building interior, establishing threat/conflict presence.

## Character Placement & Movement Logic
- **Prisoner**: Background movement right-to-left, dragging motion through entrance
- **Carter**: Maintains position, observes prisoner movement
- **Sola**: May react to prisoner's appearance depending on beat timing

## Geography, Axis, Eyeline Facts
- Primary axis: Background right-to-left (prisoner trajectory)
- Secondary axis: Left-to-center-right (maintained from BT001)
- Eyeline: Carter and Sola may shift gaze toward prisoner movement
- Depth layering: Prisoner in background plane, Carter/Sola in foreground

## Prop, Vehicle, Crowd, Environmental State
- **Environment**: Building entrance threshold with interior visible behind
- **Crowd**: None specific, focus on prisoner's isolated movement
- **Props**: Dragging motion may involve unseen restraint or force
- **Continuity**: Prisoner's clothing state upon entry affects subsequent coverage

## Likely Coverage Families
- Wide shot showing full background movement
- Medium shot (Carter/Sola foreground with prisoner visible in background)
- Over-the-shoulder from Carter observing prisoner
- Rack focus between foreground characters and background prisoner

## BT003.md
# BT003 - Eye Contact & Reaction (Emotional Anchor)

## Beat Purpose
Establish emotional anchor through gaze exchange between all parties.

## Start State
All three characters positioned for potential gaze interaction after previous beats.

## End State
Emotional reaction registered, scene tension peaks, connection established.

## Character Placement & Movement Logic
- **Carter**: Central position, reactive to both Sola's arrival and prisoner's presence
- **Sola**: Positioned near Carter, may maintain or shift gaze based on emotional state
- **Prisoner**: Background position, may make eye contact if visible in coverage

## Geography, Axis, Eyeline Facts
- Primary axis: Left-to-center-right (Sola to Carter connection)
- Secondary axis: Background right-to-left (prisoner presence)
- Eyeline: Multi-directional gaze exchange between all parties
- Emotional beats require clear eyeline tracking for coverage planning

## Prop, Vehicle, Crowd, Environmental State
- **Environment**: Exterior corridor with building entrance threshold
- **Crowd**: Minimal, focus on character emotional states
- **Props**: None specific, emphasis on facial expressions and body language
- **Continuity**: Character positioning affects subsequent scene emotional beats

## Likely Coverage Families
- Close-up (Carter reaction)
- Medium close-up (Sola and Carter together)
- Wide shot showing all three parties in frame
- Over-the-shoulder from Sola observing Carter's reaction
- Rack focus between foreground characters and background prisoner

## Clip Roster

# CH008_SC005 - Clip Roster

| Clip ID | Beat Reference | Description | Duration (Target) |
|---------|----------------|--------------|-------------------|
| CL001 | BT001 | Sola Rushes In (Connection Initiation) | 5s |
| CL002 | BT002 | Prisoner Dragged Through View (Conflict Introduction) | 5s |
| CL003 | BT003 | Eye Contact & Reaction (Emotional Anchor) | 5s |

## Clip State

{
  "project_id": "princess_of_mars_test",
  "scene_id": "CH008_SC005",
  "clip_id": "CL002",
  "status": "planning",
  "inputs": {
    "shared_character_refs": [],
    "shared_environment_refs": [],
    "scene_prompt_package": "projects/princess_of_mars_test/03_prompt_packages/scenes/CH008_SC005/CL002/CH008_SC005_CL002_scene_stage_prompt.md",
    "scene_stage_prompt_package": "projects/princess_of_mars_test/03_prompt_packages/scenes/CH008_SC005/CL002/CH008_SC005_CL002_scene_stage_prompt.md",
    "keyframe_prompt_package": "projects/princess_of_mars_test/03_prompt_packages/keyframes/CH008_SC005/CL002/CH008_SC005_CL002_keyframe_prompt.md",
    "fix_prompt_packages": [
      "projects/princess_of_mars_test/03_prompt_packages/fixes/CH008_SC005/CL002/CH008_SC005_CL002_fix_01_prompt.md"
    ],
    "anchor_prompt_packages": [],
    "video_prompt_package": "projects/princess_of_mars_test/03_prompt_packages/cut_motion/CH008_SC005/CL002/CH008_SC005_CL002_cut_motion_prompt.md",
    "cut_motion_prompt_package": "projects/princess_of_mars_test/03_prompt_packages/cut_motion/CH008_SC005/CL002/CH008_SC005_CL002_cut_motion_prompt.md",
    "legacy_anchor_prompt_packages": [],
    "legacy_video_prompt_package": null
  },
  "approved_assets": {
    "golden_frame": null,
    "approved_keyframe": null,
    "approved_video": null,
    "still_fixes": [],
    "anchor_frames": [],
    "interval_frames": [],
    "cut_motion_videos": []
  },
  "approved_video_last_frame": null,
  "current_continuity_source": null,
  "latest_runs": {},
  "review_batches": [],
  "latest_review_decision": null,
  "notes": [],
  "stage_style_preferences": {
    "cut_motion": {
      "literal_descriptive": {
        "appearances": 0,
        "top_two": 0,
        "wins": 0
      },
      "cinematic_compositional": {
        "appearances": 0,
        "top_two": 0,
        "wins": 0
      },
      "performance_action_led": {
        "appearances": 0,
        "top_two": 0,
        "wins": 0
      },
      "sparse_conservative": {
        "appearances": 0,
        "top_two": 0,
        "wins": 0
      }
    },
    "keyframe": {
      "literal_descriptive": {
        "appearances": 0,
        "top_two": 0,
        "wins": 0
      },
      "cinematic_compositional": {
        "appearances": 0,
        "top_two": 0,
        "wins": 0
      },
      "performance_action_led": {
        "appearances": 0,
        "top_two": 0,
        "wins": 0
      },
      "sparse_conservative": {
        "appearances": 0,
        "top_two": 0,
        "wins": 0
      }
    },
    "still_fix": {
      "literal_descriptive": {
        "appearances": 0,
        "top_two": 0,
        "wins": 0
      },
      "cinematic_compositional": {
        "appearances": 0,
        "top_two": 0,
        "wins": 0
      },
      "performance_action_led": {
        "appearances": 0,
        "top_two": 0,
        "wins": 0
      },
      "sparse_conservative": {
        "appearances": 0,
        "top_two": 0,
        "wins": 0
      }
    }
  }
}



Existing prompt draft:

# Title
CH008_SC005 CL002 Cut Motion Prompt

# ID
CH008_SC005_CL002_cut_motion_prompt

# Purpose
Fill in the stage intent here. Transition from wide establishing shot to tighter medium two-shot as approaching companion reaches proximity, maintaining spatial context and lighting continuity.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Medium two shot, over the shoulder view, stationary observer shoulder profile foreground left, approaching companion full face upper body moving diagonally from background right, daylight illumination, building exterior corridor entrance threshold, smoke haze distant hills visible horizon, intimate perspective, cinematic lighting grade consistent with previous clip.

# Negative Prompt
static image, single shot, wide angle, distorted faces, extra limbs, morphing characters, inconsistent lighting, blurry motion, low resolution, dark shadows, indoor artificial light, green screen background.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC005
- clip_id: CL002
- duration_seconds: 5
- required_refs: CH008_SC005/BEAT_INDEX.md BT001, CH008_SC005/BT001.md End State
- optional_refs: None
- visible_character_assets: Carter (shoulder/back profile), Sola (full face and upper body)
- look_continuity_policy: Preserve keyframe lighting and grade by default
- intended_lighting_change: None
- composition_type: Medium two shot, over-the-shoulder from Carter's perspective
- continuity_mode: reframe_same_moment
- starting_keyframe_strategy: Shoulder of Carter in foreground left, Sola approaching from background right
- dependency_policy: Depends on CL001 establishing spatial context; no reverse dependency
- auto_advance_policy: None
- fallback_strategy: If shoulder framing is unclear, shift to medium shot with both characters fully visible
- consistency_assist_policy: None
- consistency_assist_method: None
- anatomy_repair_policy: None
- consistency_targets: None
- style_profile: Action-oriented, awe-inspiring, daylight haze
- batch_role: cut_motion
- fix_of: None

# Continuity Notes
- Lighting must match previous clip keyframe exactly to maintain visual continuity.
- Character count and identity must remain consistent with established assets.
- Motion flow should reflect approaching trajectory without sudden jumps in position.
- Background environment (corridor/plaza threshold) must stay stable during motion.

# Repair Notes
- If anatomy appears distorted, apply repair to match canonical character structure.
- If lighting shifts unexpectedly, revert to base keyframe illumination values.
- Ensure no morphing occurs between the stationary observer and approaching figure.
- Check for any artifacts from the cut transition and smooth them out if visible.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC005/CL002.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC005.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC005/CH008_SC005_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md

````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: clip_prompt
stage: cut_motion
version: 1

[[SECTION purpose]]
Transition from wide establishing shot to tighter medium two-shot as approaching companion reaches proximity, maintaining spatial context and lighting continuity.
[[/SECTION]]

[[SECTION positive_prompt]]
Medium two shot composition, over the shoulder perspective, stationary male observer shoulder profile foreground left, approaching female companion full face upper body moving diagonally from background right, daylight illumination, building exterior corridor entrance threshold, smoke haze distant hills visible horizon, intimate perspective, cinematic lighting grade consistent with previous clip.
[[/SECTION]]

[[SECTION negative_prompt]]
static image, single shot, wide angle, distorted faces, extra limbs, morphing characters, inconsistent lighting, blurry motion, low resolution, dark shadows, indoor artificial light, green screen background.
[[/SECTION]]

[[SECTION inputs_markdown]]
- project_id: princess_of_mars_test
- scene_id: CH008_SC005
- clip_id: CL002
- duration_seconds: 5
- required_refs: CH008_SC005/BEAT_INDEX.md BT001, CH008_SC005/BT001.md End State
- optional_refs: None
- visible_character_assets: male observer (shoulder/back profile), female companion (full face and upper body)
- look_continuity_policy: Preserve keyframe lighting and grade by default
- intended_lighting_change: None
- composition_type: Medium two shot, over-the-shoulder from male observer's perspective
- continuity_mode: reframe_same_moment
- starting_keyframe_strategy: Shoulder of male observer in foreground left, female companion approaching from background right
- dependency_policy: Depends on CL001 establishing spatial context;
````
