# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T21:58:13.412516+00:00
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

## Display Name & Role
**Name:** Lorquas Ptomel  
**Role:** Warrior Leader / Local

## Presence Status
**Status:** Referenced  
**Note:** Character remains at deserted city until danger passed.

## Physical Description
**Supported Details:** None provided in this chapter.  
**Uncertainty Notes:** No physical traits (height, build, hair color, skin tone) are described in the text. Only actions ("remains at deserted city") are recorded.

## Costume & Silhouette
**Details:** Unknown.  
**Continuity Traits:** None specified in this chapter.

## Render-Facing Prompt Phrases
- "Warrior figure remaining at city"
- "Uncertain physical build"
- "Martian attire (implied)"

# Aliases

None



# Canonical Character ID

lorquas_ptomel



# Fully Identified

true

# Manual Description Input Required

No



# Manual Description Reason

None




Manual character description path: projects/princess_of_mars_test/01_source/character_descriptions/lorquas_ptomel_manual_description.md

(missing)
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
Shared reference prompt for generating consistent images of Lorquas Ptomel, focusing on the warrior leader archetype and implied Martian context. Acknowledges current lack of specific physical details to ensure stability without inventing traits. Prioritizes silhouette, attire logic, and environmental status (deserted city) over scene-specific blocking.
[[/SECTION]]
[[SECTION positive_prompt]]
Warrior leader standing at deserted city, implied Martian attire, uncertain physical build, local figure silhouette, stable face, consistent costume logic, atmospheric lighting, neutral expression, static pose
[[/SECTION]]
[[SECTION negative_prompt]]
modern clothing, crowded scene, specific human skin tone, modern technology, blurry, deformed hands, excessive detail on unknown features, proper nouns, dynamic action, bright sunlight, indoor setting
[[/SECTION]]
[[SECTION inputs_markdown]]
Project: princess_of_mars_test
Asset ID: lorquas_ptomel
Path: projects/princess_of_mars_test/02_story_analysis/character_breakdowns/lorquas_ptomel.md
Status: Referenced
Note: Character remains at deserted city until danger passed.
[[/SECTION]]
[[SECTION continuity_notes_markdown]]
Physical Description: None provided in chapter. Uncertainty Notes: No physical traits (height, build, hair color, skin tone) are described in text. Only actions recorded.
Costume & Silhouette: Unknown. Continuity Traits: None specified in chapter.
Render-Facing Phrases: "Warrior figure remaining at city", "Uncertain physical build", "Martian attire (implied)".
Current Status: Referenced. Character remains at deserted city until danger passed.
[[/SECTION]]
[[SECTION repair_notes_markdown]]
Manual Description Input Required: No. Manual Description Reason: None.
Recommendation: Future iterations should seek manual input for physical traits to resolve uncertainty in continuity notes.
Status Check: Ensure generated images maintain "uncertain physical build" logic rather than defaulting to specific human features not described in source text.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
````
