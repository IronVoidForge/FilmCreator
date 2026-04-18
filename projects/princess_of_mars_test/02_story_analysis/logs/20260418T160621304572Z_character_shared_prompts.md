# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T16:06:21.305071+00:00
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

Asset id: lorquas_ptomel

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



Character breakdown path: projects/princess_of_mars_test/02_story_analysis/character_breakdowns/lorquas_ptomel.md

# Lorquas Ptomel

**Display Name:** Lorquas Ptomel  
**Chapter Role:** Warrior Leader  
**Presence Status:** Referenced (Not in immediate scene)  

**Physical Description:** None supported by source text. Character is identified only as "old warrior". No height, build, hair color, or skin tone details are provided in this chapter.  

**Costume & Silhouette:** None described. Attire is not mentioned in the source material for this specific scene.  

**Continuity-Critical Traits:**  
- Keeps caravan in deserted city for safety.  
- Astute old warrior (implied experience).  
- Part of the cavalcade leadership.  

**Descriptive Noun Phrases:**  
- Old Martian warrior  
- Caravan leader  
- Strategic planner (implied by action)  

**Uncertainty Notes:**  
- Physical appearance is entirely unknown based on this source text.  
- Attire details are missing.  
- Facial features and body type cannot be determined from the provided material.

# Manual Description Input Required

Yes



# Manual Description Reason

Referenced warrior; no physical description provided in source text.




Manual character description path: projects/princess_of_mars_test/01_source/character_descriptions/lorquas_ptomel_manual_description.md

<!-- FILMCREATOR_MANUAL_PLACEHOLDER -->

# Asset ID
lorquas_ptomel

# Purpose
Paste a stable manual visual description for this character so later shared reference generation can use it.

# Why This Is Needed
Referenced warrior; no physical description provided in source text.

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
asset_id: lorquas_ptomel

[[SECTION purpose]]
Referenced old warrior leader with no physical description provided in source text. Character identified only as experienced caravan keeper maintaining safety in deserted city. Manual visual description required for shared reference generation.
[[/SECTION]]

[[SECTION positive_prompt]]
old Martian warrior, weathered face, mature build, practical combat attire, desert-appropriate clothing, strategic posture, experienced leader silhouette, continuity-critical marks on hands and arms, aged skin texture, functional armor pieces, caravan leadership presence
[[/SECTION]]

[[SECTION negative_prompt]]
scene-specific blocking, modern technology, indoor settings, young appearance, elaborate costumes, detailed facial features beyond age impression, specific hair color details, skin tone specifics, proper nouns, character names, scene numbers, location identifiers
[[/SECTION]]

[[SECTION inputs_markdown]]
projects/princess_of_mars_test/02_story_analysis/character_breakdowns/lorquas_ptomel.md
projects/princess_of_mars_test/01_source/character_descriptions/lorquas_ptomel_manual_description.md
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
Physical appearance entirely unknown based on source text. Attire details missing from chapter material. Facial features and body type cannot be determined from provided documentation. Character identified only as old warrior with implied experience. Manual visual description required before shared reference generation can proceed. Continuity-critical traits focus on role (caravan leader, strategic planner) rather than physical specifics.
[[/SECTION]]

[[SECTION repair_notes_markdown]]
Manual character description path requires completion at projects/princess_of_mars_test/01_source/character_descriptions/lorquas_ptomel_manual_description.md. Physical details must be added including face, hair, body type, age impression, silhouette, skin tone, costume logic, and any continuity-critical marks. Prefer visible facts over backstory when describing appearance.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
