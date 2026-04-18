# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T23:36:18.481193+00:00
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

Asset id: city_buildings

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



Environment breakdown path: projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/city_buildings.md

**Environment Role:** Primary / Observation Point (Transit Setting)

**Architecture or Geography:** Deserted city buildings with upper floors and rooftops. Valley floor context visible beyond structures. Hills beyond the city horizon.

**Lighting and Atmosphere Cues:** Sunlight illuminating building facades. Green Martians firing from windows. Devices gleam in sunlight. Open daylight conditions.

**Scale Cues and Recurring Environmental Anchors:** Multi-story structures providing elevation for warriors. Windows used as firing positions. Rooftops accessible for climbing. Building entrance where prisoner is dragged.

**Descriptive Noun Phrases for Render-Facing Prompts:** Deserted city buildings with upper floors, windows used for firing, rooftops with grappling hooks, valley floor beyond structures, hills in background horizon.

````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_shared_prompts
version: 1

[[FILMCREATOR_RECORD]]
type: environment_prompt
asset_id: city_buildings

[[SECTION purpose]]
Generate stable local environment reference prompts for deserted city buildings with upper floors and rooftops. Prompts should capture multi-story structures providing elevation for warriors, windows used as firing positions, rooftops accessible for climbing, valley floor beyond structures, hills in background horizon. Architecture emphasizes deserted urban setting with sunlight illuminating building facades and devices gleaming in open daylight conditions.
[[/SECTION]]

[[SECTION positive_prompt]]
Deserted city buildings with upper floors, windows used for firing, rooftops with grappling hooks, valley floor beyond structures, hills in background horizon, sunlight illuminating building facades, devices gleam in sunlight, multi-story structures providing elevation, open daylight conditions.
[[/SECTION]]

[[SECTION negative_prompt]]
proper nouns, specific names, indoor lighting, night time, dark shadows, enclosed spaces, underground areas, modern technology, neon lights, artificial illumination, crowded scenes, people inside buildings, vehicles, machinery, industrial equipment.
[[/SECTION]]

[[SECTION inputs_markdown]]
Project: princess_of_mars_test
Asset: city_buildings
Environment Role: Primary / Observation Point (Transit Setting)
Architecture or Geography: Deserted city buildings with upper floors and rooftops. Valley floor context visible beyond structures. Hills beyond the city horizon.
Lighting and Atmosphere Cues: Sunlight illuminating building facades. Green Martians firing from windows. Devices gleam in sunlight. Open daylight conditions.
Scale Cues and Recurring Environmental Anchors: Multi-story structures providing elevation for warriors. Windows used as firing positions. Rooftops accessible for climbing. Building entrance where prisoner is dragged.
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
Environmental anchors remain consistent across shots: building facades illuminated by sunlight, windows serving as firing positions, rooftops with grappling hooks visible, valley floor beyond structures, hills in background horizon. Scale maintained through multi-story structures providing elevation for warriors. Lighting conditions stay open daylight with devices gleaming in sunlight throughout sequence.
[[/SECTION]]

[[SECTION repair_notes_markdown]]
Review prompts to ensure no proper nouns appear in positive or negative prompt bodies. Verify environmental anchors are consistently described using descriptive noun phrases. Check that scale cues emphasize multi-story structures and elevation points. Confirm lighting conditions maintain open daylight atmosphere across all generated images.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
