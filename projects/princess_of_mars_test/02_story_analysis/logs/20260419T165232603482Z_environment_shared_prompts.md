# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T16:52:32.604486+00:00
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

Asset id: valley

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



Environment breakdown path: projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/valley.md

# Valley - CH008 Environment

## Environment Role
Secondary background geography establishing regional scale and context.

## Architecture and Geography
- Valley floor beyond city buildings
- Open terrain extending from plaza area
- Distant horizon line visible from upper levels
- Regional geography providing spatial orientation
- Background landscape for fleet movement context

## Lighting and Atmosphere Cues
- Daylight conditions across valley floor
- Atmospheric haze at distant horizon
- Light reflecting off valley surfaces
- Smoke patterns drifting into valley space
- Valley visibility from building windows

## Scale Cues and Environmental Anchors
- Valley depth establishes regional scale
- Distance from city buildings defines background relationship
- Hill crests beyond valley provide directional reference
- Fleet movement paths extending toward valley horizon
- Valley floor visible from plaza level

## Descriptive Noun Phrases for Render-Facing Prompts
- "valley floor beyond city buildings"
- "open terrain extending from plaza area"
- "distant horizon line visible from upper levels"
- "regional geography providing spatial orientation"
- "background landscape for fleet movement context"

````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_shared_prompts
version: 1
[[FILMCREATOR_RECORD]]
type: environment_prompt
asset_id: valley
[[SECTION purpose]]
Secondary background geography establishing regional scale and context for fleet movement paths extending toward distant horizon line visible from upper levels. Open terrain providing spatial orientation beyond city buildings with atmospheric haze at distant horizon creating depth perception across valley floor surfaces.
[[/SECTION]]
[[SECTION positive_prompt]]
valley floor beyond city buildings, open terrain extending from plaza area, distant horizon line visible from upper levels, regional geography providing spatial orientation, background landscape for fleet movement context, daylight conditions across valley floor, atmospheric haze at distant horizon, light reflecting off valley surfaces, smoke patterns drifting into valley space, hill crests beyond valley provide directional reference
[[/SECTION]]
[[SECTION negative_prompt]]
proper nouns, specific location names, indoor scenes, close-up details, night conditions, heavy shadows, urban density, building interiors, city center views, detailed architecture, human figures, vehicles, smoke obscuring visibility, dark atmosphere, enclosed spaces, vertical structures dominating frame
[[/SECTION]]
[[SECTION inputs_markdown]]
- Environment Role: Secondary background geography establishing regional scale and context
- Architecture and Geography: Valley floor beyond city buildings, open terrain extending from plaza area, distant horizon line visible from upper levels, regional geography providing spatial orientation, background landscape for fleet movement context
- Lighting and Atmosphere Cues: Daylight conditions across valley floor, atmospheric haze at distant horizon, light reflecting off valley surfaces, smoke patterns drifting into valley space, valley visibility from building windows
- Scale Cues and Environmental Anchors: Valley depth establishes regional scale, distance from city buildings defines background relationship, hill crests beyond valley provide directional reference, fleet movement paths extending toward valley horizon, valley floor visible from plaza level
[[/SECTION]]
[[SECTION continuity_notes_markdown]]
Valley serves as consistent secondary background geography across multiple shots. Atmospheric haze and daylight conditions remain stable for regional scale perception. Hill crests and distant horizon line function as recurring directional anchors. Valley floor visibility from plaza level maintains spatial relationship with city buildings. Smoke patterns provide subtle atmospheric movement without obscuring environmental anchors.
[[/SECTION]]
[[SECTION repair_notes_markdown]]
Monitor valley depth consistency across different camera angles to maintain regional scale perception. Ensure atmospheric haze remains visible at distant horizon without becoming too dense. Verify hill crests remain identifiable as directional reference points. Check that smoke patterns drift naturally into valley space without blocking environmental anchors. Confirm daylight conditions reflect properly off valley surfaces for consistent lighting.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
