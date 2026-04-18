# FilmCreator Prompt Writing Exchange
- timestamp_utc: 2026-04-18T21:11:49.709793+00:00
- stage: cut_motion
- clip_id: CL004
- retry_kind: same_prompt_retry

## System Prompt
````text
You are writing one FilmCreator prompt package for a local generation pipeline.
Return exactly one FILMCREATOR packet in Markdown.
Do not return JSON.
Do not use markdown fences.
Do not add commentary before or after the packet.
Target stage: cut_motion
Stage guidance: Write a short-cut motion prompt that starts from the approved opening frame. Preserve the keyframe lighting and grade by default. Focus on visible motion, camera behavior, and environment change.
Use descriptive noun phrases and avoid proper nouns in prompt text.
Keep duration and workflow metadata in inputs_markdown, not in the prompt body.
Follow the requested section names exactly.
````

## User Prompt
````text
Project: princess_of_mars_test

Scene: SC001

Clip: CL004

Prompt title: SC001 CL004 Cut Motion Prompt

Prompt id: SC001_CL004_cut_motion_prompt

Workflow type: video.cut_motion.wan.i2v

Write improved content for this canonical prompt package.

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

# Project Title
A Princess of Mars

# Author
Edgar Rice Burroughs

# Setting
Green Martian City, Valley, Plaza

# Key Characters
Narrator (Green Warrior), Sola, Woola (hound)

# Context
The story follows a Green Warrior on Mars who has been captured by Martians. He lives among them and observes their society, warfare, and technology. The narrative involves conflict between the Green Warriors and an Air Fleet of unknown origin.

# Visual Continuity
- **Architecture:** Spacious doorways, upper floors with windows overlooking valley/hills.
- **Technology:** Incubator ceremony, chariots, mastodons, mounted warriors, air craft (gray-painted, long/low).
- **Warfare:** Green warriors fire from building windows; Air fleet uses guns and sighting apparatus.

# Narrative Tone
Sci-fi adventure with themes of war, observation, and the intersection of Martian and Earthly aesthetics.

## Chapter Summaries

## CH001_summary.md
# Chapter Title
Chapter VIII - A Fair Captive from the Sky

# Scene 1: Retreat & Investigation
- **Event:** Martians retreat immediately after incubation ceremony procession debouches into open ground.
- **Action:** Narrator investigates cause of sudden retreat from upper floor window.
- **Visual:** Twenty gray air ships swing slowly over hill crests, each carrying strange banners and odd devices on prows.

# Scene 2: Battle
- **Event:** Green warriors fire a terrific volley from building windows facing the valley.
- **Action:** Air fleet returns fire with guns; ships move parallel to firing line then turn back.
- **Visual:** Banners dissolve in spurts of flame; green figures drop at bullet explosions; fire from vessels is ineffectual due to suddenness of first volley.
- **Outcome:** Fleet limps away; one ship receives brunt of fire, appears unmanned and helpless.

# Scene 3: Disabled Ship & Loot
- **Event:** Warriors chase disabled ship; board with spears and grappling hooks.
- **Action:** Ship hauled to ground; systematic rifling of vessel.
- **Visual:** Loot includes arms, ammunition, silks, furs, jewels, stone vessels, food/water.
- **Outcome:** Ship towed out, emptied, set on fire by missile from last warrior. Drifts away as floating funeral pyre.

# Scene 4: Return & Prisoner
- **Event:** Warriors return to plaza; danger of air craft passed for a week.
- **Action:** Narrator sees prisoner dragged into building by green Martian females.
- **Visual:** Slender girlish figure, Earthly woman appearance, oval face, coal black hair, light reddish copper skin, naked except ornaments.
- **Interaction:** She looks at narrator, makes sign (appeal for help), then is dragged away. Narrator feels hope and dejection.

# Emotional Beats
- **Depression:** Narrator feels defeat of kindred people rather than routing of horde.
- **Hope:** Mixed surge of hope, fear, exultation, and depression upon seeing prisoner.
- **Regret:** Realizes he did not answer her signal for succor due to ignorance of Martian customs.

## Character Index

# Character Index - Chapter VIII - A Fair Captive from the Sky

| Asset ID | Canonical Character ID | Display Name | Role | Physical Presence | Description Status |
|----------|------------------------|--------------|------|-------------------|-------------------|
| narrator | CH001_NARRATOR | The Narrator | Observer/Investigator | Referenced | Manual description required |
| green_martian_females | CH001_GREEN_MARTIAN_FEMALES | Green Martian Females | Warriors/Captors | Referenced | Manual description required |
| earthly_woman_prisoner | CH001_EARTHLY_WOMAN_PRISONER | Earthly Woman / Prisoner | Captive/Subject | Physically Present | Fully identified |
| green_warriors | CH001_GREEN_WARRIORS | Green Warriors | Combatants | Referenced | Manual description required |

**Notes:**
- All characters except the prisoner lack sufficient physical description for dependable image generation
- The narrator's identity is stable but physically undefined in source material
- Martian warriors appear as a group without individual differentiation
- Prisoner has detailed visual description but may require cultural clarification

## Environment Index

# Environment Index - Chapter VIII

## Primary Environments
- **open_ground_hill** - Main retreat location with air ships visible over hill crests
- **valley_battlefield** - Central battle zone where green warriors fire from building windows

## Secondary Environments  
- **building_windows_upper_floor** - Narrator's observation point for investigation
- **plaza_return** - Gathering space after danger passes, prisoner brought here
- **disabled_martian_ship** - Looting target, towed to ground and set ablaze

## Transit/Functional Environments
- All environments serve as staging grounds for Martian fleet movements and warrior operations

## Clip Plan

# CL004 - Close-Up Banner Design Focus

## Continuity Mode
reblock_same_scene

## Composition Type
Close-up shot of banner designs

## Starting Keyframe Strategy
insert_banner_detail_focus

## Dependency Policy
dependent_on_fleet_position_and_banner_visibility

## Fallback Strategy
cutaway_to_device_shape_detail

## Visible Character Assets
- Green Warriors - static or minimal movement on selected vessels with visible banners
- Narrator - eyeline shifts to specific ships for detail examination

## Required Refs
- SC001 beat bundle BT003.md
- Banner designs continuity markers across shots
- Device shapes on individual ship prows

## Optional Refs
- Hill crests depth context for close-ups
- Lighting consistency notes
- Ship prow details visible in frame

## Opening Keyframe Intent
Focus narrator's eyeline shift from wide formation to close detail of banner designs on individual ships

## Cut Motion Intent
Transition from over-the-shoulder (CL003) to close-up maintaining banner design continuity markers

## Interval Beats
- 0s: Fleet in wide formation visible from observation point
- 2.5s: Eyeline zooms from wide formation to close detail of banners
- 5s: Close examination of banners and devices on individual ships, specific design elements identifiable

## Scene Breakdown

# SC001: Retreat & Investigation

## Scene Purpose
Establish the sudden Martian retreat and narrator's investigation of cause from observation point

## Scene Summary
Martians withdraw immediately after incubation ceremony procession debouches into open ground. Narrator observes from upper floor window as twenty gray air ships swing slowly over hill crests, each carrying strange banners and odd devices on prows. The visual emphasizes the scale of retreat and narrator's curiosity about what triggered it.

## Beat Breakdown
- **BT001**: Window Observation - Establishing retreat from safe distance
- **BT002**: Fleet Movement - Showing scale across hill crests
- **BT003**: Detail Focus - Banners and devices on ship prows

## Participating Characters
- **Narrator** (Earth human) - Observer from upper floor
- **Green Warriors** (Martian) - Retreatting fleet personnel

## Participating Environments
- Upper floor observation point
- Hill crests
- Open ground where procession ended

## Dominant Emotional Shift
Curiosity → Concern about sudden retreat of kindred people

## Likely Visual Coverage Families
- Wide establishing shots of air ships over hill crests
- Medium shots from window perspective showing narrator observing
- Close-ups on banners and devices on ship prows
- Over-the-shoulder shots from narrator's viewpoint

## Likely Continuity Sensitivities
- Ship positions relative to hill crests must remain consistent
- Banner designs must be identifiable across shots
- Window framing and interior elements must stay consistent
- Number of ships (twenty) must be maintained in wide shots

## Beat Bundles

## BT001.md
# BT001 - Window Observation

## Beat Purpose
Establish narrator's position and initial observation of fleet retreat from safe distance

## Start State
- Narrator standing at upper floor window
- Ships just visible on horizon line
- Interior lighting warm, establishing safety contrast to exterior

## End State
- Full view of twenty ships over hill crests established
- Narrator's curiosity visually confirmed through eyeline movement
- Exterior scale now understood by audience

## Character Placement and Movement Logic
- **Narrator**: Static position at window frame, slight body turn toward observation point
- **Green Warriors**: Distant fleet formation, minimal individual movement, collective retreat pattern
- Movement follows ship trajectory across horizontal axis from left to right

## Geography, Axis, or Eyeline Facts
- Window frame establishes interior boundary and safe zone
- Eyeline follows ship movement along horizontal plane
- Hill crests create depth reference points for ship positioning
- Vertical axis: interior (warm) vs exterior (cool) lighting contrast

## Prop, Vehicle, Crowd, and Environmental State
- **Vehicles**: Twenty gray air ships in formation
- **Props**: Strange banners on prows, odd devices visible
- **Environment**: Hill crests, open ground below, upper floor observation point
- **Continuity**: Ship count (20), window framing elements, interior lighting level

## Likely Coverage Families
- Medium shot from window showing narrator's eyeline
- Wide establishing exterior of ships over hill crests
- Over-the-shoulder from narrator to fleet
- Cutaway to ship details in distance

## BT002.md
# BT002 - Fleet Movement

## Beat Purpose
Show scale of retreat and synchronized fleet movement across terrain

## Start State
- Ships positioned at base of first hill crest
- Fleet beginning coordinated movement pattern
- Narrator observing from fixed position

## End State
- Fleet distributed across multiple hill crests in formation
- Scale of retreat fully established through positioning
- Movement timing consistent with retreat urgency

## Character Placement and Movement Logic
- **Narrator**: Static observation point, body remains at window
- **Green Warriors**: Coordinated fleet movement, ships following established pattern
- Movement follows terrain contours with elevation changes

## Geography, Axis, or Eyeline Facts
- Hill crests create depth axis for ship positioning
- Ships move along horizontal plane with slight elevation variations
- Eyeline tracks fleet distribution across multiple reference points
- Vertical axis: hill base to crest creates scale reference

## Prop, Vehicle, Crowd, and Environmental State
- **Vehicles**: Twenty gray air ships maintaining formation
- **Props**: Banners visible on ship prows, devices on individual vessels
- **Environment**: Hill crests, open ground, upper floor observation point
- **Continuity**: Ship positions relative to crests, banner visibility, movement timing

## Likely Coverage Families
- Wide exterior shots showing fleet across hill crests
- Over-the-shoulder from narrator to fleet
- Cutaway to individual ship positioning
- Establishing shot of retreat scale

## BT003.md
# BT003 - Detail Focus

## Beat Purpose
Emphasize mysterious elements on ship prows and banner designs

## Start State
- Fleet in wide formation visible from observation point
- Narrator's eyeline available for detail shifts
- Banner designs partially visible in wide shots

## End State
- Close examination of banners and devices on individual ships
- Specific design elements now identifiable
- Narrator's curiosity focused on mysterious objects

## Character Placement and Movement Logic
- **Narrator**: Eyeline shifts to specific ships, minimal body movement
- **Green Warriors**: Static or minimal movement on selected vessels
- Focus axis moves from fleet-wide to individual ship prows

## Geography, Axis, or Eyeline Facts
- Eyeline zooms from wide formation to close detail
- Focus axis moves from horizontal fleet distribution to vertical ship prow details
- Banner designs create visual reference points across shots
- Device shapes establish continuity markers

## Prop, Vehicle, Crowd, and Environmental State
- **Vehicles**: Individual ships with visible prows and devices
- **Props**: Strange banners on prows, odd devices on vessels
- **Environment**: Hill crests provide depth context for close-ups
- **Continuity**: Banner designs, device shapes, ship prow details, lighting consistency

## Likely Coverage Families
- Close-up shots of banner designs
- Detail inserts of devices on ship prows
- Over-the-shoulder with focus pull to specific ships
- Cutaway detail shots maintaining continuity markers

## Clip Roster

# SC001 Clip Roster - Retreat & Investigation

## Overview
Six clips covering BT001-BT003 beats, establishing narrator observation and Martian fleet retreat from upper floor window perspective

## Clip Sequence

| Clip ID | Beat | Duration | Composition | Primary Action |
|---------|------|----------|-------------|----------------|
| CL001 | BT001 | 5s | Medium Shot | Narrator at window, eyeline to horizon ships |
| CL002 | BT001→BT002 | 5s | Wide Exterior | Twenty gray air ships over hill crests |
| CL003 | BT002 | 5s | Over-the-Shoulder | Narrator observing fleet movement |
| CL004 | BT003 | 5s | Close-Up | Banner designs on ship prows |
| CL005 | BT003 | 5s | Detail Insert | Devices on individual vessels |
| CL006 | BT003→End | 5s | Cutaway Detail | Continuity markers maintained |

## Coverage Notes
- All clips target ~5 seconds duration
- Continuity elements: ship count (20), window framing, banner designs, device shapes
- Emotional arc: Curiosity → Concern about sudden retreat
- Primary character assets: Narrator (Earth human), Green Warriors (Martian fleet)

## Clip State

{
  "project_id": "princess_of_mars_test",
  "scene_id": "SC001",
  "clip_id": "CL004",
  "status": "planning",
  "inputs": {
    "shared_character_refs": [],
    "shared_environment_refs": [],
    "scene_prompt_package": "projects/princess_of_mars_test/03_prompt_packages/scenes/SC001/CL004/SC001_CL004_scene_stage_prompt.md",
    "scene_stage_prompt_package": "projects/princess_of_mars_test/03_prompt_packages/scenes/SC001/CL004/SC001_CL004_scene_stage_prompt.md",
    "keyframe_prompt_package": "projects/princess_of_mars_test/03_prompt_packages/keyframes/SC001/CL004/SC001_CL004_keyframe_prompt.md",
    "fix_prompt_packages": [
      "projects/princess_of_mars_test/03_prompt_packages/fixes/SC001/CL004/SC001_CL004_fix_01_prompt.md"
    ],
    "anchor_prompt_packages": [],
    "video_prompt_package": "projects/princess_of_mars_test/03_prompt_packages/cut_motion/SC001/CL004/SC001_CL004_cut_motion_prompt.md",
    "cut_motion_prompt_package": "projects/princess_of_mars_test/03_prompt_packages/cut_motion/SC001/CL004/SC001_CL004_cut_motion_prompt.md",
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
    },
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
    }
  }
}



Existing prompt draft:

# Title
SC001 CL004 Cut Motion Prompt

# ID
SC001_CL004_cut_motion_prompt

# Purpose
Generate cut motion video for human male warrior observing approaching alien fleet from window, transitioning from mid-distance to plaza level with rising tension

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Medium shot human male warrior standing at dark wood window frame, hands moving from sill to chest position, weight shifting forward toward glass, outside view shows gray airships descending toward plaza street level, green-skinned alien warriors visible in distant fleet formation, midday sunlight reflecting off ship devices, camera slight push-in on warrior reaction, atmosphere tense anticipation, smoke and flame visible in background valley

# Negative Prompt
morphing faces, flickering lights, extra limbs, distorted anatomy, sudden jumps, static image, wrong character count, blurry text, inconsistent lighting, background shifting, glitchy movement, incorrect character identity, interior corridor space, female figure entrance, empty room transition

# Inputs
- project_id: princess_of_mars_test
- scene_id: SC001
- clip_id: CL004
- duration_seconds: 5
- required_refs: Beat BT004.md, Scene Summary, Chapter Summary daylight conditions
- optional_refs: Medium shot warrior + fleet in frame, POV from warrior looking at approaching ships
- visible_character_assets: human male warrior, green-skinned alien warriors, gray airships
- look_continuity_policy: Midday Light Established - Midday light fully established by end of beat
- intended_lighting_change: soft morning light transitioning to bright midday
- composition_type: medium_shot_to_close_up
- continuity_mode: cutaway
- starting_keyframe_strategy: Fleet at mid-distance, human male warrior maintaining observation posture with neutral expression
- dependency_policy: dependent_on_previous_clip
- auto_advance_policy: 
- fallback_strategy: 
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 
- workflow_type: video.cut_motion.wan.i2v

# Continuity Notes
- Match keyframe lighting and grade by default
- Preserve interior shadows and depth cues from opening frame
- Ensure fleet entrance is deliberate not glitchy
- Maintain character consistency with previous clips in scene
- Keep warrior and window positioning stable during motion

# Repair Notes
- If fleet appears too fast, slow motion slightly
- If lighting shifts, revert to base grade from keyframe
- If anatomy distorts on entrance, regenerate with stricter constraints
- If camera push is too abrupt, smooth out transition

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/CL004.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/SC001_clip_roster.md
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

Generate cut motion video for close-up banner design continuity markers on Martian airship prows, maintaining visible design elements across shots while preserving lighting and grade from approved keyframe

[[/SECTION]]



[[SECTION positive_prompt]]

Close examination of banners and devices on individual ships, specific design elements identifiable, green warriors static or minimal movement on selected vessels with visible banners, narrator eyeline shifts to specific ships for detail examination, midday sunlight reflecting off ship devices, hill crests provide depth context for close-ups, camera slight focus pull to banner details, atmosphere mysterious observation

[[/SECTION]]



[[SECTION negative_prompt]]

morphing faces, flickering lights, extra limbs, distorted anatomy, sudden jumps, static image, wrong character count, blurry text, inconsistent lighting, background shifting, glitchy movement, incorrect character identity, interior corridor space, female figure entrance, empty room transition, banner design changes, device shape inconsistencies, ship position drifts

[[/SECTION]]



[[SECTION inputs_markdown]]

- project_id: princess_of_mars_test
- scene_id: SC001
- clip_id: CL004
- duration_seconds: 5
- required_refs: Beat BT003.md, Scene Summary, Chapter Summary daylight conditions
- optional_refs: Close-up banner designs continuity markers, Hill crests depth context, Ship prow details visible in frame
- visible_character_assets: Green Warriors static minimal movement, Narrator eyeline shifts to specific ships
- look_continuity_policy: Midday Light Established - Midday light fully established by end of beat
- intended_lighting_change: soft morning light transitioning to bright midday
- composition_type: close_up_banner_detail
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: insert_banner_detail_focus
- dependency_policy: dependent_on_fleet_position_and_banner_visibility
- auto_advance_policy: 
- fallback_strategy: cutaway_to_device_shape_detail
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: banner designs, device shapes, ship prow details, lighting consistency
- style_profile: sci_fi_adventure_war_observation
- batch_role: 
- fix_of: 
- workflow_type: video.cut_motion.wan.i2v

[[/SECTION]]



[[SECTION continuity_notes_markdown]]

- Match keyframe lighting and grade by default
- Preserve interior shadows and depth cues from opening frame
- Ensure banner designs are identifiable across shots
- Maintain character consistency with previous clips in scene
- Keep ship positions relative to hill crests consistent
- Preserve device shapes on individual ship prows
- Maintain window framing elements if visible

[[/SECTION]]



[[SECTION repair_notes_markdown]]

- If banner designs appear unclear, regenerate with stricter constraints
- If camera focus is too abrupt, smooth out transition
- If lighting shifts, revert to base grade from keyframe
- If ship position drifts, maintain continuity markers
- If device shapes are inconsistent, regenerate with proper references
- If anatomy distorts on entrance, regenerate with stricter constraints

[[/SECTION]]



[[FILMCREATOR_PACKET]]
````
