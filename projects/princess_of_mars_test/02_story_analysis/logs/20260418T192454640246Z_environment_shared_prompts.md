# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T19:24:54.640246+00:00
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

Asset id: hills

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



Environment breakdown path: projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/hills.md

# Hills - Transit Setting

## Environment Role
Transit setting where airships arrive over crest and dip below until only one visible; atmospheric transition zone between city and valley.

## Architecture or Geography
Hill crests serving as arrival/dip zones for airship fleet; elevated terrain above city; slopes leading to valley floor.

## Lighting and Atmosphere Cues
Sunlight gleaming on odd devices painted on prows; ships swing slowly over crest in sunlight; atmospheric transition from hill to valley.

## Scale Cues and Recurring Environmental Anchors
Hills large enough to see fleet arriving over them; crests at height above city; dip zones below hill crests until only one ship visible; atmospheric boundary between city and valley.

## Descriptive Noun Phrases
- hill crest arrival zone
- airship dip below point
- elevated terrain above city
- fleet swing over crest
- atmospheric transition boundary

````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_shared_prompts
version: 1

[[FILMCREATOR_RECORD]]
type: environment_prompt
asset_id: hills

[[SECTION purpose]]
Transit setting where airships arrive over crest and dip below until only one visible; atmospheric transition zone between city and valley. Hill crests serving as arrival/dip zones for airship fleet; elevated terrain above city; slopes leading to valley floor. Sunlight gleaming on odd devices painted on prows; ships swing slowly over crest in sunlight; atmospheric transition from hill to valley. Hills large enough to see fleet arriving over them; crests at height above city; dip zones below hill crests until only one ship visible; atmospheric boundary between city and valley.
[[/SECTION]]

[[SECTION positive_prompt]]
hill crest arrival zone, airship dip below point, elevated terrain above city, fleet swing over crest, atmospheric transition boundary, sunlight gleaming on devices painted on prows, ships swinging slowly over crest in sunlight, atmospheric transition from hill to valley, hills large enough to see fleet arriving over them, crests at height above city, dip zones below hill crests until only one ship visible, atmospheric boundary between city and valley
[[/SECTION]]

[[SECTION negative_prompt]]
proper nouns, specific names, character faces, dialogue text, indoor scenes, night time, dark shadows, low resolution, blurry details, distorted geometry, inconsistent lighting, missing elements, extra objects, wrong scale, flat terrain, no atmosphere, static composition, crowded frame, cluttered background
[[/SECTION]]

[[SECTION inputs_markdown]]
projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/hills.md
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
Hill crests serve as arrival and dip zones for airship fleet. Elevated terrain positioned above city with slopes leading to valley floor. Sunlight gleams on devices painted on prows of ships. Ships swing slowly over crest in sunlight. Atmospheric transition occurs from hill to valley. Hills are large enough to see fleet arriving over them. Crests maintain height above city. Dip zones positioned below hill crests until only one ship visible. Atmospheric boundary exists between city and valley.
[[/SECTION]]

[[SECTION repair_notes_markdown]]
Ensure atmospheric transition is clearly visible between city and valley regions. Maintain consistent scale for hills relative to airship fleet. Verify sunlight gleaming on devices painted on prows remains visible throughout scene. Check that dip zones below hill crests show progression until only one ship visible. Confirm elevated terrain above city maintains proper height relationship with slopes leading to valley floor.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
