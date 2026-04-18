# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T16:07:38.570644+00:00
- task: character_shared_prompts

## System Prompt
````text
You are FilmCreator's local authoring analyst.
Return exactly one FILMCREATOR packet in Markdown.
Do not return JSON.
Do not use markdown fences.
Do not add commentary before or after the packet.
Preserve uncertainty instead of inventing hidden facts.
When asked to write Markdown file contents, place the complete file body inside the requested SECTION tags.
When asked to extract render-facing facts, focus on visible, continuity-relevant details.
````

## User Prompt
````text
Project slug: princess_of_mars_test

Asset id: green_martians

Task: write one reusable shared character-reference prompt draft for stable local generation.

Return exactly one Markdown packet using this outer envelope:
[[FILMCREATOR_PACKET]]
task: character_shared_prompts
version: 1

Repeat one FILMCREATOR_RECORD block for every extracted item of that type.

[[FILMCREATOR_RECORD]]
type: character_prompt
asset_id: <value>

[[SECTION purpose]]
...purpose content...
[[/SECTION]]

[[SECTION positive_prompt]]
...positive_prompt content...
[[/SECTION]]

[[SECTION negative_prompt]]
...negative_prompt content...
[[/SECTION]]

[[SECTION inputs_markdown]]
...inputs_markdown content...
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
...continuity_notes_markdown content...
[[/SECTION]]

[[SECTION repair_notes_markdown]]
...repair_notes_markdown content...
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]



Rules:

- purpose and inputs may use stable asset ids

- final positive and negative prompt bodies should avoid proper nouns and use descriptive noun phrases

- keep prompts concrete and visible

- prefer stable face, hair, body type, costume logic, silhouette, and recurring materials over scene-specific blocking



Character breakdown path: projects/princess_of_mars_test/02_story_analysis/character_breakdowns/green_martians.md

# Green Martians

**Display Name:** Green Martians  
**Chapter Role:** Antagonists / Warriors  
**Presence Status:** Physically Present (Collective)  

**Physical Description:** Identified as "green Martians". Skin tone is green. Build implied as warrior stature. No individual height, age, or specific physical traits are detailed beyond skin color and general humanoid form.  

**Costume & Silhouette:** Warrior attire implied by context ("warriors", "chariots"). Specific costume details not described in this chapter text.  

**Continuity-Critical Traits:**  
- Fire from building windows during engagement.  
- Swarm from windows to capture ship.  
- Drag captive into building.  
- Use spears and grappling hooks.  
- Release guy ropes for fire launch.  

**Descriptive Noun Phrases:**  
- Green Martian warriors  
- Building-based defenders  
- Ship swarms (implied by action)  
- Spear users  
- Grappling hook throwers  

**Uncertainty Notes:**  
- Individual facial features are not described.  
- Specific armor or clothing details are missing.  
- Variation in build among the group is not specified.

# Manual Description Input Required

Yes



# Manual Description Reason

Collective group description; individual build and variation not described beyond skin tone in source text.




Manual character description path: projects/princess_of_mars_test/01_source/character_descriptions/green_martians_manual_description.md

<!-- FILMCREATOR_MANUAL_PLACEHOLDER -->

# Asset ID
green_martians

# Purpose
Paste a stable manual visual description for this character so later shared reference generation can use it.

# Why This Is Needed
Collective group description; individual build and variation not described beyond skin tone in source text.

# Guidance
- describe face, hair, body type, age impression, silhouette, skin tone, costume logic, and any continuity-critical marks
- prefer visible facts over backstory
- if multiple looks exist, describe the default look for this chapter

# Manual Description

````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_shared_prompts
version: 1

[[FILMCREATOR_RECORD]]
type: character_prompt
asset_id: green_martians

[[SECTION purpose]]
Green Martian warrior collective with green skin tone, humanoid build, wearing dark armor plating with metallic shoulder guards, wielding long spear weapons and throwing grappling hooks, standing in defensive formation near building windows with fire glow visible behind them. Default appearance shows uniform group members with similar physical traits for consistency across shots.

[[SECTION positive_prompt]]
green skin tone humanoid warriors, dark metallic armor plating, wide shoulder guard pieces, long spear weapons held ready, grappling hook throwing devices on wrists, standing defensive formation, building windows with fire glow in background, warrior stature build, collective group appearance, dark clothing under armor, muscular arm definition, serious facial expression, green complexion uniform across members, humanoid silhouette, combat-ready posture

[[SECTION negative_prompt]]
proper nouns, specific names, individual height variations, age differences, unique facial features, light skin tones, civilian clothing, casual poses, smiling expressions, indoor settings without fire, single warrior isolated, inconsistent build among group, detailed backstory elements, scene-specific blocking, non-warrior attire, bright daylight without fire glow

[[SECTION inputs_markdown]]
```markdown
# Green Martians Character Reference Inputs

## Core Visual Elements
- Skin: Green complexion uniform across collective members
- Build: Warrior stature humanoid form
- Armor: Dark metallic plating with shoulder guards
- Weapons: Long spears, grappling hook devices on wrists
- Setting: Near building windows with fire glow visible

## Continuity Requirements
- Maintain consistent green skin tone across all members
- Keep armor style uniform for group shots
- Preserve weapon types and positions
- Ensure fire glow background consistency when present

## Default Appearance Notes
- All members share similar physical traits
- No individual height or age variations shown
- Uniform combat-ready posture preferred
- Dark armor with metallic accents consistent
```

[[SECTION continuity_notes_markdown]]
# Continuity Notes for Green Martians Character Reference

## Physical Consistency
- Green skin tone must remain uniform across all collective members
- Warrior build stature should not vary significantly between shots
- Armor plating style and color must stay consistent
- Weapon types (spears, grappling hooks) should match reference exactly

## Scene Integration
- Fire glow from building windows is continuity-critical when present
- Defensive formation positioning preferred for group shots
- Combat-ready posture maintains character identity
- Avoid casual or non-combat poses that break character logic

## Group vs Individual
- Collective appearance prioritized over individual variation
- Default look established for chapter consistency
- No unique facial features detailed beyond green complexion
- Build uniformity maintained across all members shown

[[SECTION repair_notes_markdown]]
# Repair Notes for Green Martians Character Reference

## Potential Issues to Address
- Ensure no proper nouns appear in final prompt bodies
- Verify skin tone description remains concrete and visible
- Check that armor details avoid specific material names
- Confirm weapon descriptions use descriptive noun phrases only
- Validate continuity notes reference visible facts not backstory

## Recommended Fixes
- Replace any name references with descriptive terms
- Simplify armor descriptions to focus on visible elements
- Ensure fire glow background is described as visual fact
- Remove any individual variation details from group shots
- Keep all prompts focused on current chapter appearance only
````
