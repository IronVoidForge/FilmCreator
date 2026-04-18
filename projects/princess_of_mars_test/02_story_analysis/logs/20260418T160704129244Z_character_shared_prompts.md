# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T16:07:04.129244+00:00
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
Green-skinned humanoid warriors, collective group presence, muscular build, dark warrior attire, holding spears and grappling hooks, associated with fire effects from building windows, shadowy silhouette.
[[/SECTION]]

[[SECTION positive_prompt]]
green skin, humanoid figure, muscular build, dark armored clothing, spear in hand, grappling hook visible, fire glow, shadowy background, multiple figures standing together, warrior stance, intense expression, detailed texture on armor, volumetric lighting from fire.
[[/SECTION]]

[[SECTION negative_prompt]]
pale skin, human facial features, civilian clothes, text, watermark, blurry, low quality, deformed hands, blue eyes, bright daylight, soft focus, cartoonish style, missing limbs, extra fingers, distorted face, generic background, simple shapes.
[[/SECTION]]

[[SECTION inputs_markdown]]
Asset ID: green_martians
Source Path: projects/princess_of_mars_test/02_story_analysis/character_breakdowns/green_martians.md
Manual Description Path: projects/princess_of_mars_test/01_source/character_descriptions/green_martians_manual_description.md
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
Green skin tone must remain consistent across all figures in the collective group. Warrior gear (spears, grappling hooks) serves as key identifier for this character type. Fire effects are associated with their presence near building windows. Silhouette should convey threat and warrior stature. Avoid individual facial variations unless specified in future updates; maintain generic warrior face structure for stability.
[[/SECTION]]

[[SECTION repair_notes_markdown]]
Individual facial features are not described in source text; use generic warrior face structure to ensure generation stability. Specific armor or clothing details are implied by context ("warriors", "chariots"); prioritize silhouette and material logic over intricate texture if uncertain. Variation in build among the group is not specified; maintain consistent muscular build for all figures.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
