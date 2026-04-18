# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T20:59:14.960445+00:00
- task: character_shared_prompts

## System Prompt
````text
You are FilmCreator's local authoring analyst.
Work like a careful local planning assistant for chapter analysis and shot-prep authoring.
Return exactly one FILMCREATOR packet in Markdown.
Do not return JSON.
Do not use markdown fences.
Do not add commentary before or after the packet.
Preserve uncertainty instead of inventing hidden facts.
Prefer short, concrete section bodies over long prose.
Follow the requested headings and record fields exactly.
When asked to write Markdown file contents, place the complete file body inside the requested SECTION tags.
When asked to extract render-facing facts, focus on visible, continuity-relevant details.
If information is missing, say so briefly instead of guessing.
````

## User Prompt
````text
Project slug: princess_of_mars_test

Asset id: green_warriors

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



Character breakdown path: projects/princess_of_mars_test/02_story_analysis/character_breakdowns/green_warriors.md

# Green Warriors

**Chapter Role:** Combatants / Fleet Operators  
**Physical Presence:** Referenced (not individually present)  

## Physical Description
*Only described as "green figures" in source material. No detailed physical features documented.*

## Costume & Silhouette
*Unknown - no visual documentation available beyond color descriptor.*

## Continuity-Critical Traits
- Fire terrific volley from building windows facing valley
- Air fleet returns fire with guns
- Ships move parallel to firing line then turn back
- Chase disabled ship; board with spears and grappling hooks
- Systematically rifle vessel for loot (arms, ammunition, silks, furs, jewels, stone vessels, food/water)
- Set disabled ship on fire as floating funeral pyre

## Render-Facing Prompt Notes
**Uncertainty:** Physical appearance extremely limited. "Green figures" is only documented feature.  
**Key Phrases for Later Use:** "green warriors," "combatants from building windows," "boarders of disabled ship," "riflers of vessel loot"

## Important Notes
- Character identification too weak for stable reruns without clarification
- May already exist under different cultural name or designation
- Manual description required before any image generation can proceed reliably

# Aliases

None



# Canonical Character ID

green_warriors



# Fully Identified

false

# Manual Description Input Required

No



# Manual Description Reason

None




Manual character description path: projects/princess_of_mars_test/01_source/character_descriptions/green_warriors_manual_description.md

(missing)
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_shared_prompts
version: 1

[[FILMCREATOR_RECORD]]
type: character_prompt
asset_id: green_warriors

[[SECTION purpose]]
Draft a reusable shared character-reference prompt for stable local generation of the green warriors asset within the princess_of_mars_test project, focusing on known color and role traits while preserving uncertainty regarding physical features.
[[/SECTION]]

[[SECTION positive_prompt]]
green figures, combatants, fleet operators, firing from windows, boarding disabled ship, spears, grappling hooks, rifling vessel loot, stone vessels, silks, furs, jewels, action pose, dynamic lighting, cinematic composition
[[/SECTION]]

[[SECTION negative_prompt]]
human face details, specific hair styles, skin tones other than green, modern clothing, civilian attire, blurry, distorted, extra limbs, low resolution, text, watermark
[[/SECTION]]

[[SECTION inputs_markdown]]
- Project: princess_of_mars_test
- Asset ID: green_warriors
- Source Path: projects/princess_of_mars_test/02_story_analysis/character_breakdowns/green_warriors.md
- Manual Description Path: (missing)
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
- Physical appearance extremely limited. "Green figures" is only documented feature.
- Character identification too weak for stable reruns without clarification.
- May already exist under different cultural name or designation.
- Manual description required before any image generation can proceed reliably.
- Continuity-Critical Traits include fire from windows, air fleet returns fire, board disabled ship with spears and grappling hooks, rifle vessel for loot (arms, ammunition, silks, furs, jewels, stone vessels, food/water), set disabled ship on fire as floating funeral pyre.
[[/SECTION]]

[[SECTION repair_notes_markdown]]
- Prompts must avoid proper nouns and use descriptive noun phrases.
- Keep prompts concrete and visible.
- Prefer stable face, hair, body type, costume logic, silhouette, and recurring materials over scene-specific blocking (though currently unknown).
- If generating specific shots, rely on color coding for identity rather than facial features.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
