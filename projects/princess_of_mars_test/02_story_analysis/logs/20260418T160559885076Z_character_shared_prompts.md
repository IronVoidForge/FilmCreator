# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T16:05:59.885076+00:00
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
Shared visual reference description for Green Martians collective group, focusing on stable physical traits and recurring materials for consistent generation across scenes.
[[/SECTION]]

[[SECTION positive_prompt]]
green skin tone humanoid form warrior build stature warrior attire silhouette spear users grappling hook throwers collective group presence continuity-critical marks visible facts over backstory default look for chapter
[[/SECTION]]

[[SECTION negative_prompt]]
individual facial features specific armor details clothing variations in build among group scene-specific blocking proper nouns backstory elements age or height specifications
[[/SECTION]]

[[SECTION inputs_markdown]]
Asset ID: green_martians
Manual description path: projects/princess_of_mars_test/01_source/character_descriptions/green_martians_manual_description.md
Story analysis path: projects/princess_of_mars_test/02_story_analysis/character_breakdowns/green_martians.md
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
Green Martians appear as collective group with no individual variation specified beyond green skin tone. Warrior attire and build implied through context of spears, grappling hooks, and building-based defense actions. Continuity-critical traits include fire from windows during engagement and swarm behavior to capture ship. Individual facial features, specific armor or clothing details, and build variation among the group remain unspecified in source material.
[[/SECTION]]

[[SECTION repair_notes_markdown]]
Uncertainty around individual facial features requires descriptive focus on skin tone and silhouette rather than detailed face generation. Specific costume logic should reference warrior attire without inventing armor details not present in source text. Build variation should be treated as uniform collective presence rather than individual differences. Scene-specific blocking should be avoided to maintain reusable character reference across multiple shots.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
