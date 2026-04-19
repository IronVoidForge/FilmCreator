# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T02:59:16.972691+00:00
- task: environment_shared_prompts

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

Asset id: city_plaza_open_ground

Task: write one reusable shared environment-reference prompt draft for stable local generation.

Return exactly one Markdown packet using this outer envelope:
[[FILMCREATOR_PACKET]]
task: environment_shared_prompts
version: 1

Repeat one FILMCREATOR_RECORD block for every extracted item of that type.

[[FILMCREATOR_RECORD]]
type: environment_prompt
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

- emphasize stable architecture, geography, scale, atmosphere, and recurring environmental anchors



Environment breakdown path: projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/city_plaza_open_ground.md

# City Plaza / Open Ground

## Environment Role
Primary setting for the procession return and initial retreat order.

## Architecture or Geography
City plaza, open ground/valley floor leading to building facades.

## Lighting and Atmosphere Cues
Daylight, sudden tension, deserted city feel later (city remains deserted for a week).

## Scale Cues and Recurring Environmental Anchors
Procession scale, distant hills, building facades, fifty feet altitude reference for drifting ship.

## Useful Descriptive Noun Phrases
"City plaza", "Open valley floor", "Procession route", "Building facades".

````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_shared_prompts
version: 1
[[FILMCREATOR_RECORD]]
type: environment_prompt
asset_id: city_plaza_open_ground
[[SECTION purpose]]
Defines the visual environment for the city plaza scene, ensuring consistency with the story's progression from procession return to initial retreat order. Focuses on architecture, geography, scale, and atmosphere anchors.
[[/SECTION]]
[[SECTION positive_prompt]]
City plaza, open valley floor, building facades, procession route, daylight, distant hills, deserted atmosphere, fifty feet altitude reference, drifting ship anchor, wide composition, clear sky, urban geometry, ground level perspective.
[[/SECTION]]
[[SECTION negative_prompt]]
Proper nouns, specific character names, indoor scenes, night time, crowded city, modern technology, text overlays, close up shots, vertical composition, foggy weather, cluttered background.
[[/SECTION]]
[[SECTION inputs_markdown]]
projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/city_plaza_open_ground.md
[[/SECTION]]
[[SECTION continuity_notes_markdown]]
City remains deserted for a week after the procession. Tension builds during the day. Drifting ship is at fifty feet altitude relative to buildings. Open ground leads to building facades. Procession scale matches distant hills.
[[/SECTION]]
[[SECTION repair_notes_markdown]]
Ensure "fifty feet" is interpreted as scale relative to buildings, not absolute height if context implies otherwise. Keep "deserted" consistent with later scenes. Verify open valley floor connects visually to building facades without obstruction.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
