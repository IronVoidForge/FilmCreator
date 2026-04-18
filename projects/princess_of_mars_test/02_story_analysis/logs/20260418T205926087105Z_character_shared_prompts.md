# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T20:59:26.087105+00:00
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

Asset id: narrator

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



Character breakdown path: projects/princess_of_mars_test/02_story_analysis/character_breakdowns/narrator.md

# The Narrator

**Chapter Role:** Observer / Investigator  
**Physical Presence:** Referenced (not physically present in scenes)  

## Physical Description
*No physical description provided in source material.*

## Costume & Silhouette
*Unknown - no visual documentation available.*

## Continuity-Critical Traits
- Observes events from upper floor window
- Investigates cause of Martians' sudden retreat
- Witnesses prisoner being dragged into building
- Experiences mixed emotions: hope, fear, exultation, depression
- Feels defeat of kindred people rather than routing of horde

## Render-Facing Prompt Notes
**Uncertainty:** Physical appearance completely undefined in source. Any image generation would require manual description specification.  
**Key Phrases for Later Use:** "observer from upper floor," "witness to Martian events," "investigator of sudden retreat"

## Important Notes
This character's physical identity is stable (narrator role) but visually undefined. Manual description required before any image generation can proceed reliably.

# Aliases

None



# Canonical Character ID

narrator



# Fully Identified

true

# Manual Description Input Required

No



# Manual Description Reason

None




Manual character description path: projects/princess_of_mars_test/01_source/character_descriptions/narrator_manual_description.md

(missing)
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_shared_prompts
version: 1

[[FILMCREATOR_RECORD]]
type: character_prompt
asset_id: narrator

[[SECTION purpose]]
Character role is Observer/Investigator with physical appearance undefined in source material. Manual description specification required before reliable image generation can proceed. Character observes events from upper floor window, investigates cause of Martians' sudden retreat, witnesses prisoner being dragged into building, experiences mixed emotions including hope, fear, exultation, depression, and defeat of kindred people rather than routing of horde.
[[/SECTION]]

[[SECTION positive_prompt]]
observer standing at upper floor window, witness to Martian events, investigator of sudden retreat, figure with contemplative expression, silhouette framed against building interior, materials suggesting period costume, posture indicating investigation and observation, emotional complexity visible in facial features, stable face type for character consistency, recurring hair style for visual continuity, body type appropriate for observer role, costume logic matching historical setting
[[/SECTION]]

[[SECTION negative_prompt]]
proper nouns, specific names, modern clothing, contemporary technology, bright studio lighting, cartoonish proportions, distorted anatomy, inconsistent facial features, mismatched costume elements, scene-specific blocking, dynamic action poses, exaggerated expressions, low resolution, blurry details, text overlays, watermarks, artifacts, noise, color banding, overexposed areas, underexposed shadows
[[/SECTION]]

[[SECTION inputs_markdown]]
Manual description path: projects/princess_of_mars_test/01_source/character_descriptions/narrator_manual_description.md (missing - requires creation)
Character breakdown path: projects/princess_of_mars_test/02_story_analysis/character_breakdowns/narrator.md
Canonical character ID: narrator
Fully identified: true
Manual description input required: No (but physical appearance undefined)
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
- Observes events from upper floor window
- Investigates cause of Martians' sudden retreat
- Witnesses prisoner being dragged into building
- Experiences mixed emotions: hope, fear, exultation, depression
- Feels defeat of kindred people rather than routing of horde
- Physical presence is Referenced (not physically present in scenes)
- No physical description provided in source material
- Unknown costume and silhouette documentation
[[/SECTION]]

[[SECTION repair_notes_markdown]]
Physical appearance completely undefined in source - requires manual description specification before any image generation can proceed reliably. Key phrases for later use: "observer from upper floor," "witness to Martian events," "investigator of sudden retreat." Character identity is stable (narrator role) but visually undefined. Manual description required before any image generation can proceed reliably.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
