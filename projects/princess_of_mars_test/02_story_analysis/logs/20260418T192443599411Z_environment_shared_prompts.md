# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T19:24:43.599411+00:00
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

Asset id: city

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



Environment breakdown path: projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/city.md

# City - Primary Setting

## Environment Role
Primary setting where Carter and Sola return after incubation ceremony; remains deserted for over a week due to fear of air craft attack.

## Architecture or Geography
Urban structures with windows serving as firing positions for Martian warriors; streets accessible for street emergence; buildings near crash site for prisoner recovery.

## Lighting and Atmosphere Cues
Sunlight gleaming on odd devices painted on prows; gray-painted airships visible against city backdrop; deserted atmosphere with fear of return attack.

## Scale Cues and Recurring Environmental Anchors
City scale large enough to see fleet arriving over hills; windows at building heights for volley firing; streets accessible for street emergence; buildings near crash site for recovery operations.

## Descriptive Noun Phrases
- deserted urban streets
- window firing positions
- gray-painted airship arrival zone
- fear of return attack atmosphere
- street emergence points
- deserted cityscape

````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_shared_prompts
version: 1

[[FILMCREATOR_RECORD]]
type: environment_prompt
asset_id: city

[[SECTION purpose]]
Primary setting for incubation return characters; remains deserted due to fear of air craft attack.
[[/SECTION]]

[[SECTION positive_prompt]]
deserted urban streets with window firing positions, gray-painted airship arrival zone, fear of return attack atmosphere, street emergence points, deserted cityscape, sunlight gleaming on odd devices, fleet arriving over hills
[[/SECTION]]

[[SECTION negative_prompt]]
crowds, modern technology, bright colors, characters with names, peaceful atmosphere, green vegetation
[[/SECTION]]

[[SECTION inputs_markdown]]
project slug princess_of_mars_test, asset id city
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
incubation return characters, deserted state for over a week, crash site near buildings, windows as firing positions
[[/SECTION]]

[[SECTION repair_notes_markdown]]
ensure windows are clearly firing positions, maintain gray-painted airships visibility
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
