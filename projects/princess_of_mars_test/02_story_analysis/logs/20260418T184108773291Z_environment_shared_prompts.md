# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T18:41:08.773291+00:00
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

Asset id: plaza_street_level

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



Environment breakdown path: projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/plaza_street_level.md

# Plaza Street Level - Ground Action Zone

## Environment Role
Primary transit and action setting for fleet approach, battle sequence, and prisoner movement. Central ground-level zone connecting all other environments.

## Architecture and Geography
Open plaza space surrounded by building facades at street level. Wide paved surfaces with multiple entry points to buildings. Ground-level view of approaching airships from distance.

## Lighting and Atmosphere Cues
Full daylight with sunlight reflecting off ship devices visible from ground. Smoke and flame from burning vessel create dramatic atmospheric effects. Green Martian fire volleys illuminate plaza space.

## Scale and Environmental Anchors
City-scale open plaza with building facades as vertical anchors. Airships appear at varying distances across sky. Building entrances serve as compositional entry points. Ground level provides human-scale reference for action sequences.

## Descriptive Noun Phrases for Render Prompts
- Open plaza space
- Building facade surrounds
- Paved ground surfaces
- Multiple building entrances
- Approaching airship silhouettes
- Smoke and flame effects
- Daylight atmospheric haze
- Ground-level action zone

````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_shared_prompts
version: 1

[[FILMCREATOR_RECORD]]
type: environment_prompt
asset_id: plaza_street_level

[[SECTION purpose]]
Primary transit and action setting for fleet approach, battle sequence, and prisoner movement. Central ground-level zone connecting all other environments with open plaza space surrounded by building facades at street level. Wide paved surfaces with multiple entry points to buildings. Ground-level view of approaching airships from distance.
[[/SECTION]]

[[SECTION positive_prompt]]
Open plaza space, building facade surrounds, paved ground surfaces, multiple building entrances, approaching airship silhouettes, smoke and flame effects, daylight atmospheric haze, ground-level action zone, city-scale open plaza, vertical anchors, compositional entry points, human-scale reference for action sequences, green fire volleys illuminating plaza
[[/SECTION]]

[[SECTION negative_prompt]]
indoor spaces, underground areas, aerial perspective only, night scenes, dark shadows, enclosed rooms, single building entrance, distant airships only, artificial lighting, foggy conditions, abstract compositions, floating elements, minimal ground contact, isolated structures
[[/SECTION]]

[[SECTION inputs_markdown]]
- Open plaza space
- Building facade surrounds
- Paved ground surfaces
- Multiple building entrances
- Approaching airship silhouettes
- Smoke and flame effects
- Daylight atmospheric haze
- Ground-level action zone
- City-scale open plaza
- Vertical anchors
- Compositional entry points
- Human-scale reference for action sequences
- Green fire volleys illuminating plaza
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
Plaza serves as central transit connecting all other environments. Building facades provide vertical anchors while paved ground offers human-scale reference. Airships appear at varying distances across sky with smoke and flame creating dramatic atmospheric effects. Ground level provides consistent action zone for fleet approach, battle sequence, and prisoner movement sequences. Green Martian fire volleys illuminate plaza space consistently throughout action scenes.
[[/SECTION]]

[[SECTION repair_notes_markdown]]
Ensure airship silhouettes maintain varying distances across sky rather than fixed positions. Verify smoke and flame effects remain atmospheric without obscuring key compositional entry points. Confirm daylight atmospheric haze reflects off ship devices visible from ground level. Maintain city-scale proportions for plaza space while keeping human-scale reference points for action sequences.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
