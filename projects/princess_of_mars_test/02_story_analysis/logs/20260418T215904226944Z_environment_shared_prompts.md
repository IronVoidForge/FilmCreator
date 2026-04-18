# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T21:59:04.226944+00:00
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

Asset id: city_plaza_exterior

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



Environment breakdown path: projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/city_plaza_exterior.md

Role: Primary setting for action and aftermath.
Architecture: Multi-story buildings with doorways, windows, portals. Paved plaza and streets.
Lighting: Bright sunlight casting shadows on buildings. Dim interiors visible through windows.
Atmosphere: Initially bustling (procession), then deserted after battle. Smoke from burning ship.
Scale: Urban structures towering over the plaza.
Anchors: Building doorways, upper floor windows, building portals.

````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_shared_prompts
version: 1

[[FILMCREATOR_RECORD]]
type: environment_prompt
asset_id: city_plaza_exterior

[[SECTION purpose]]
Shared reference prompt for generating consistent city plaza exterior scenes across the project. Defines architectural scale, lighting conditions, atmospheric states, and environmental anchors to maintain visual continuity during regeneration cycles. Supports both bustling procession and post-battle deserted states while preserving structural integrity of multi-story buildings and paved surfaces.
[[/SECTION]]

[[SECTION positive_prompt]]
Multi-story urban buildings with doorways and windows. Paved plaza ground surface with street pathways. Bright sunlight illumination casting distinct shadows on building facades. Dim interior spaces visible through window openings. Towering architectural structures above plaza level. Building portals at ground floor entrances. Smoke rising from distant burning ship location. Urban geography with vertical scale emphasis. Recurring environmental anchors at doorways and upper windows.
[[/SECTION]]

[[SECTION negative_prompt]]
Blurry or indistinct building details. Dark interior spaces without window visibility. Overexposed sunlight losing shadow definition. Missing paved plaza surface texture. Inconsistent architectural scale between buildings. Absent structural doorways or windows. Floating smoke without ground connection. Improper urban geography alignment. Missing environmental anchor points at portals and upper floors.
[[/SECTION]]

[[SECTION inputs_markdown]]
Project path: projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/city_plaza_exterior.md
Asset identifier: city_plaza_exterior
Environment breakdown location: 02_story_analysis folder structure
Regeneration context: Shared environment-reference prompt draft for stable local generation
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
Maintain multi-story building architecture consistency across all regeneration cycles. Preserve paved plaza surface texture and lighting shadow patterns. Keep environmental anchors at doorways and upper windows visible in every generated scene. Match atmospheric states between bustling procession and post-battle deserted conditions while preserving structural integrity. Ensure smoke from burning ship remains distant anchor point without dominating foreground composition.
[[/SECTION]]

[[SECTION repair_notes_markdown]]
If regeneration produces inconsistent building scale, adjust architectural height parameters to match multi-story urban structures. When shadow definition is lost in bright sunlight, recalibrate lighting intensity to preserve distinct shadow patterns on building facades. If environmental anchors become obscured, increase visibility of doorways and upper windows through window openings. For atmospheric state transitions between bustling and deserted conditions, maintain structural continuity while adjusting smoke density and crowd presence levels.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
