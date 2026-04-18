# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T19:24:27.944428+00:00
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

Asset id: buildings

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



Environment breakdown path: projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/buildings.md

# Buildings - Secondary Setting

## Environment Role
Secondary setting for window firing positions; urban structures where warriors swarm onto craft from windows just before it strikes.

## Architecture or Geography
Building windows at height for volley firing; urban structures near crash site; windows serving as access points to craft recovery.

## Lighting and Atmosphere Cues
Sunlight gleaming on odd devices painted on prows visible from buildings; green warriors fire from building windows; urban lighting conditions.

## Scale Cues and Recurring Environmental Anchors
Windows at height for volley firing; buildings near crash site for warrior swarm access; urban scale allowing multiple window positions; structures large enough for craft to strike buildings.

## Descriptive Noun Phrases
- window firing positions
- urban structure windows
- warrior swarm access points
- building height zones
- crash site proximity structures

````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_shared_prompts
version: 1
[[FILMCREATOR_RECORD]]
type: environment_prompt
asset_id: buildings
[[SECTION purpose]]
Secondary setting prompt for urban structures where warriors swarm onto craft from windows before impact; defines window firing positions, building height zones, and crash site proximity structures for stable local generation.
[[/SECTION]]
[[SECTION positive_prompt]]
window firing positions at height, urban structure windows near crash site, warrior swarm access points on buildings, building height zones for volley firing, crash site proximity structures, sunlight gleaming on devices painted on prows visible from buildings, green warriors fire from building windows, urban lighting conditions, large enough structures for craft to strike buildings.
[[/SECTION]]
[[SECTION negative_prompt]]
proper nouns, specific names, indoor scenes without window access, small scale buildings, dark atmosphere without sunlight cues, isolated structures away from crash site, single window positions, non-urban architecture, daytime without green warrior presence, miniature or toy-like structures.
[[/SECTION]]
[[SECTION inputs_markdown]]
projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/buildings.md, princess_of_mars_test/story_analysis/environment_breakdowns/buildings.md, buildings/secondary_setting/window_firing_positions.md, buildings/crash_site_proximity/urban_structures.md.
[[/SECTION]]
[[SECTION continuity_notes_markdown]]
Maintain consistent window height zones across all building structures; ensure crash site proximity remains visible from multiple angles; keep urban scale uniform for volley firing positions; preserve sunlight gleaming on devices painted on prows as recurring environmental anchor; green warrior presence should match lighting conditions.
[[/SECTION]]
[[SECTION repair_notes_markdown]]
Review window height consistency across all building assets; verify crash site proximity structures are visible from multiple camera angles; ensure urban scale remains uniform for volley firing positions; check that sunlight cues on devices painted on prows appear consistently; confirm green warrior presence matches lighting conditions in each scene.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
