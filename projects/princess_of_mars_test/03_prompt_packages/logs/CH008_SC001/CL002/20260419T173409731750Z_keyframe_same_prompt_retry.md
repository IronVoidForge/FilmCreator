# FilmCreator Prompt Writing Exchange
- timestamp_utc: 2026-04-19T17:34:09.731750+00:00
- stage: keyframe
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
Target stage: keyframe
Stage guidance: Write the exact visible state at cut start as a single frozen still. Avoid proper nouns. Use descriptive noun phrases only.
Use descriptive noun phrases and avoid proper nouns in prompt text.
Keep duration and workflow metadata in inputs_markdown, not in the prompt body.
Follow the requested section names exactly.
````

## User Prompt
````text
Project: princess_of_mars_test

Scene: CH008_SC001

Clip: CL002

Prompt title: CH008_SC001 CL002 Keyframe Prompt

Prompt id: CH008_SC001_CL002_keyframe_prompt

Workflow type: still.scene_build.four_ref.klein.distilled

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

stage: keyframe

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

## CL002 - Martian Retreat (BT002)

**Continuity Mode:** cutaway  
**Composition Type:** Medium Group  
**Starting Keyframe Strategy:** eastern sector marked as retreat destination  
**Dependency Policy:** none required  
**Fallback Strategy:** static observation angle from window if tracking fails  
**Visible Character Assets:** Green Martians in formation, coordinated movement  
**Required Refs:** BT002.md, character placement notes  
**Optional Refs:** environmental dust continuity notes  
**Opening Keyframe Intent:** show Martians positioned at city perimeter ready for engagement  
**Cut Motion Intent:** camera follows retreat path from fixed position  
**Interval Beats:** 
- 0s: Martians at city perimeter in formation
- 2s: Coordinated movement toward eastern sector begins
- 4s: Dust kicked up by retreating troops visible

**Staging Notes:**
- Ground forces maintain consistent spacing
- Environmental dust requires continuity notes
- Green Martians move in unison maintaining formation
- City boundary serves as visual reference for movement direction

**Test Clip Priority:** MEDIUM - Threat level establishment

## Scene Breakdown

Scene Purpose: Establish context of return and introduce threat.
Scene Summary: Procession returns, Martians retreat, Carter observes fleet arrival.
Participating Characters: John Carter, Green Martians (general).
Participating Environments: Open ground outside city, upper floor window.
Dominant Emotional Shift: Anticipation to Tension.
Likely Visual Coverage Families: Wide shots of procession, medium shots at window, establishing shots of airships.
Likely Continuity Sensitivities: Gray-painted airships, strange banners, odd devices on prow.

Staging Facts:
- Scene opens with wide exterior shot showing city perimeter and approaching ground forces
- Camera tracks along procession path maintaining eye-level perspective
- Cut to upper floor window establishing Carter's observation position
- Martians retreat in coordinated fashion toward eastern sector
- Airships descend from northern sky, visible against horizon
- Carter remains stationary at window throughout scene
- Gray-painted airships maintain consistent color grading across all shots
- Strange banners on prow require specific prop placement notes
- Odd devices on prow need continuity tracking for close-ups

## Beat Bundles

## BT001.md
Beat Purpose: Establish returning ground forces and set scene geography.

Beat Start State: Empty city perimeter with distant horizon visible.

Beat End State: Procession fully enters frame, camera tracks along path.

Character Placement and Movement Logic: Camera moves forward tracking procession; no character movement within shot except approaching figures.

Geography, Axis, or Eyeline Facts: Wide exterior angle showing city boundary line as visual anchor; horizon serves as eyeline reference point.

Prop, Vehicle, Crowd, and Environmental State: Gray-painted airships visible in background; strange banners on prow require specific prop placement notes; odd devices on prow need continuity tracking for close-ups.

Likely Coverage Families: Wide establishing shot, medium tracking shot, extreme long shot of horizon.

## BT002.md
Beat Purpose: Show coordinated Martian withdrawal and establish threat level.

Beat Start State: Martians positioned at city perimeter ready for engagement.

Beat End State: Martians retreat in organized fashion toward eastern sector.

Character Placement and Movement Logic: Green Martians move in unison maintaining formation; camera follows retreat path from fixed position.

Geography, Axis, or Eyeline Facts: Eastern sector marked as retreat destination; city boundary serves as visual reference for movement direction.

Prop, Vehicle, Crowd, and Environmental State: Ground forces maintain consistent spacing; environmental dust kicked up by retreating troops requires continuity notes.

Likely Coverage Families: Medium group shot, wide tracking shot, static observation angle from window.

## BT003.md
Beat Purpose: Establish airship fleet arrival and introduce visual threat elements.

Beat Start State: Northern sky clear with no visible aircraft.

Beat End State: Multiple gray-painted airships descend into frame from northern horizon.

Character Placement and Movement Logic: Airships maintain consistent descent angle; camera holds static position to capture full approach.

Geography, Axis, or Eyeline Facts: Northern sky serves as entry point; horizon line marks arrival altitude reference.

Prop, Vehicle, Crowd, and Environmental State: Gray-painted airships maintain consistent color grading across all shots; strange banners on prow require specific prop placement notes; odd devices on prow need continuity tracking for close-ups.

Likely Coverage Families: Extreme long shot of sky, medium establishing shot, wide angle showing full fleet formation.

## BT004.md
Beat Purpose: Establish Carter's observation position and emotional response to scene events.

Beat Start State: Carter positioned at upper floor window with city view.

Beat End State: Carter maintains observation stance throughout scene progression.

Character Placement and Movement Logic: Carter remains stationary at window; camera alternates between wide exterior and interior window angle.

Geography, Axis, or Eyeline Facts: Window frame serves as visual boundary; eyeline follows procession path from interior perspective.

Prop, Vehicle, Crowd, and Environmental State: Window sill requires specific prop placement notes; upper floor location needs continuity tracking for lighting consistency.

Likely Coverage Families: Medium shot at window, wide exterior angle showing window position, static observation angle from interior.

## Clip Roster

# Clip Roster - CH008_SC001

| Clip ID | Beat Reference | Duration Target | Continuity Mode | Composition Type |
|---------|----------------|-----------------|-----------------|------------------|
| CL001 | BT001 - Procession Approach | 5s | reblock_same_scene | Wide Exterior |
| CL002 | BT002 - Martian Retreat | 5s | cutaway | Medium Group |
| CL003 | BT003 - Fleet Arrival | 5s | insert | Extreme Long Sky |
| CL004 | BT004 - Carter Observation | 5s | reframe_same_moment | Medium Window |

## Clip State

{
  "project_id": "princess_of_mars_test",
  "scene_id": "CH008_SC001",
  "clip_id": "CL002",
  "status": "planning",
  "inputs": {
    "shared_character_refs": [],
    "shared_environment_refs": [],
    "scene_prompt_package": "projects/princess_of_mars_test/03_prompt_packages/scenes/CH008_SC001/CL002/CH008_SC001_CL002_scene_stage_prompt.md",
    "scene_stage_prompt_package": "projects/princess_of_mars_test/03_prompt_packages/scenes/CH008_SC001/CL002/CH008_SC001_CL002_scene_stage_prompt.md",
    "keyframe_prompt_package": "projects/princess_of_mars_test/03_prompt_packages/keyframes/CH008_SC001/CL002/CH008_SC001_CL002_keyframe_prompt.md",
    "fix_prompt_packages": [
      "projects/princess_of_mars_test/03_prompt_packages/fixes/CH008_SC001/CL002/CH008_SC001_CL002_fix_01_prompt.md"
    ],
    "anchor_prompt_packages": [],
    "video_prompt_package": "projects/princess_of_mars_test/03_prompt_packages/cut_motion/CH008_SC001/CL002/CH008_SC001_CL002_cut_motion_prompt.md",
    "cut_motion_prompt_package": "projects/princess_of_mars_test/03_prompt_packages/cut_motion/CH008_SC001/CL002/CH008_SC001_CL002_cut_motion_prompt.md",
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
CH008_SC001 CL002 Keyframe Prompt

# ID
CH008_SC001_CL002_keyframe_prompt

# Purpose
Establish John Carter's perspective watching twenty large gray air craft descend toward city building from upper floor window, capturing the pivotal arrival moment with valley and hills beyond maintaining geographical continuity.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
wide establishing shot, long low gray-painted vessels descending from upper sky toward city building facade, twenty air craft visible with strange banners on prows, valley below and hills beyond framing edges, daylight illuminating scene, figures crowding forward decks, cinematic lighting, high fidelity still, smoke from fire visible in background, missile impact flames spurt, open ground plaza below, distant horizon maintaining continuity.

# Negative Prompt
blur, distortion, extra limbs, missing characters, wrong character count, human protagonist, bright interior lighting, overexposed, low resolution, cartoonish, 3d render, plastic skin, bad anatomy, mismatched lighting, static pose, lack of motion, crowded composition, out of focus, burning, flames, fire, naval vessels, airships (wrong type), wrong vessel appearance

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL002
- duration_seconds: 5
- required_refs: BT002.md air_craft_descending_beat_documentation
- optional_refs: CH008_SC001_scene_breakdown, CL001_wide_establishing_first
- visible_character_assets: none_vessel_focus
- look_continuity_policy: dependent_on_CL001_wide_establishing_first
- intended_lighting_change: exterior_daylight_maintained
- composition_type: wide_establishing_shot
- continuity_mode: insert
- starting_keyframe_strategy: first_craft_visible_in_distance
- dependency_policy: none
- auto_advance_policy: none
- fallback_strategy: cut_to_wide_static_if_movement_disrupted
- consistency_assist_policy: enabled
- consistency_assist_method: reference_alignment
- anatomy_repair_policy: strict
- consistency_targets: vessel_count, banner_appearance, valley_hills_continuity
- style_profile: cinematic_warfare_era
- batch_role: interval_frame
- fix_of: CL001_wide_establishing_first

# Continuity Notes
- Maintain air craft appearance consistency (long low gray-painted vessels with strange banners).
- Ensure valley and hills background maintains geographical continuity from preceding clip.
- Keep vessel count at twenty visible throughout keyframe sequence.
- Capture descent trajectory from upper sky to lower city level.
- Avoid showing character details or command signals in this establishing shot.

# Repair Notes
- Correct any vessel appearance inconsistencies that don't match gray-painted long low design.
- Ensure banner and device placement on prows matches scene breakdown specifications.
- Fix lighting mismatches from preceding clip to maintain exterior daylight continuity.
- Verify valley and hills background maintains geographical consistency.
- Adjust vessel count if wrong number appears in composition.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CL002.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CH008_SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md

````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: clip_prompt
stage: keyframe
version: 1

[[SECTION purpose]]
Establish green-skinned warrior formation along city boundary line, beginning coordinated retreat toward eastern sector, maintaining continuity with preceding wide establishing shot.
[[/SECTION]]

[[SECTION positive_prompt]]
medium group shot, green-skinned warriors in ornate armor positioned along city boundary line, coordinated movement toward eastern horizon, dust kicked up by retreating troops visible, daylight illuminating scene, upper floor window frame visible in foreground for context, cinematic lighting, high fidelity still, smoke from fire visible in background.
[[/SECTION]]

[[SECTION negative_prompt]]
blur, distortion, extra limbs, missing characters, wrong character count, human protagonist, bright interior lighting, overexposed, low resolution, cartoonish, 3d render, plastic skin, bad anatomy, mismatched lighting, static pose, lack of motion, crowded composition, out of focus, burning, flames, fire, naval vessels, airships (wrong type), wrong vessel appearance.
[[/SECTION]]

[[SECTION inputs_markdown]]
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL002
- duration_seconds: 5
- required_refs: BT002.md martian_retreat_beat_documentation
- optional_refs: CH008_SC001_scene_breakdown, CL001_wide_establishing_first
- visible_character_assets: green_martian_warriors
- look_continuity_policy: dependent_on_CL001_wide_establishing_first
- intended_lighting_change: exterior_daylight_maintained
- composition_type: medium_group_shot
- continuity_mode: cutaway
- starting_keyframe_strategy: martians_at_city_perimeter
- dependency_policy: none
- auto_advance_policy: none
- fallback_strategy: cut_to_static_if_movement_disrupted
- consistency_assist_policy: enabled
- consistency_assist_method: reference_alignment
- anatomy_repair_policy: strict
- consistency_targets: formation_spacing, dust_continuity, city_boundary_reference
- style_profile: cinematic_warfare_era
- batch_role: interval_frame
- fix_of: CL001_wide_establishing_first
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
- Maintain green-skinned warrior appearance consistency (green skin, ornate armor). Ensure city boundary background maintains geographical continuity from preceding clip. Keep formation spacing consistent with retreat motion. Capture dust kicked up by retreating troops. Avoid showing character details or command signals in this establishing shot.
[[/SECTION]]

[[SECTION repair_notes_markdown]]
- Correct any green-skinned warrior appearance inconsistencies that don't match green skin/ornate armor design. Ensure city boundary and horizon matches scene breakdown specifications. Fix lighting mismatches from preceding clip to maintain exterior daylight continuity. Verify dust continuity with retreating troops. Adjust formation spacing if wrong number appears in composition.
[[/SECTION]]

[[/FILMCREATOR_PACKET]]
````
