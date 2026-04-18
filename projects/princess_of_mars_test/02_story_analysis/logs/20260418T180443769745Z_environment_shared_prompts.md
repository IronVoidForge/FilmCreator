# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T18:04:43.770250+00:00
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

Asset id: plaza_encounter_space

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



Environment breakdown path: projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/plaza_encounter_space.md

# Plaza Encounter Space Environment

## Environment Role
Transit and encounter setting for public gathering space where prisoner is dragged into building.

## Architecture and Geography
Open ground/plaza within deserted city buildings. Public square or town center space with multiple building facades surrounding open area. Ground level position accessible from street, serving as transition zone between interior buildings and exterior valley vista.

## Lighting and Atmosphere Cues
Daylight conditions with natural illumination across open plaza surface. Atmospheric weight conveyed through prisoner's dejection and narrator's depression following fleet defeat. Open space allows visibility of distant burning ship while maintaining intimate encounter focus.

## Scale Cues and Environmental Anchors
Plaza ground plane serves as primary spatial anchor. Surrounding building facades provide vertical boundaries. Height comparison between green Martian warriors (erect walking) and prisoner (considerably less than half their height) establishes scale reference within open space. Distant valley/hills vista visible beyond plaza perimeter.

## Descriptive Noun Phrases for Render-Facing Prompts
- open ground public square
- deserted city plaza space
- building facade boundaries
- daylight natural illumination
- transition zone between interior-exterior
- prisoner encounter location
- street level gathering area
- distant valley vista visibility

````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_shared_prompts
version: 1

[[FILMCREATOR_RECORD]]
type: environment_prompt
asset_id: plaza_encounter_space

[[SECTION purpose]]
Transit and encounter setting for public gathering space where prisoner is dragged into building. Open ground public square within deserted city buildings. Public square or town center space with multiple building facades surrounding open area. Ground level position accessible from street, serving as transition zone between interior buildings and exterior valley vista.
[[/SECTION]]

[[SECTION positive_prompt]]
open ground public square, deserted city plaza space, building facade boundaries, daylight natural illumination, transition zone between interior-exterior, prisoner encounter location, street level gathering area, distant valley vista visibility, open space atmosphere, multiple surrounding facades, ground plane spatial anchor, vertical boundary structures, natural light across surface, intimate encounter focus
[[/SECTION]]

[[SECTION negative_prompt]]
proper nouns, specific names, indoor enclosed spaces, night conditions, artificial lighting, crowded interior rooms, close quarters, burning ship in foreground, green Martian warriors, fleet defeat context, prisoner dejection expressions, narrator depression, valley vista blocked, building facades missing, open area obstructed, street level inaccessible, exterior vista hidden
[[/SECTION]]

[[SECTION inputs_markdown]]
projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/plaza_encounter_space.md
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
Plaza ground plane serves as primary spatial anchor. Surrounding building facades provide vertical boundaries. Height comparison between green Martian warriors (erect walking) and prisoner (considerably less than half their height) establishes scale reference within open space. Distant valley/hills vista visible beyond plaza perimeter. Daylight conditions with natural illumination across open plaza surface. Open space allows visibility of distant burning ship while maintaining intimate encounter focus.
[[/SECTION]]

[[SECTION repair_notes_markdown]]
Ensure building facades remain as boundaries without blocking distant vista. Maintain daylight illumination consistency across plaza surface. Preserve scale relationship between prisoner and surrounding structures. Keep transition zone function clear between interior buildings and exterior valley vista. Avoid proper nouns in prompt bodies. Use descriptive noun phrases for all environmental elements.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
