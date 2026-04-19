# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T02:59:07.043217+00:00
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

Asset id: building_upper_floors_windows

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



Environment breakdown path: projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/building_upper_floors_windows.md

# Building Upper Floors / Windows

## Environment Role
Secondary setting for captive discovery and prisoner dragging.

## Architecture or Geography
Building upper floors, windows.

## Lighting and Atmosphere Cues
Interior light, view of outside, deserted feel.

## Scale Cues and Recurring Environmental Anchors
Window frames, floor levels, prisoners dragged into building.

## Useful Descriptive Noun Phrases
"Building window", "Upper floor interior", "Prisoner entry point".

````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_shared_prompts
version: 1

[[FILMCREATOR_RECORD]]
type: environment_prompt
asset_id: building_upper_floors_windows

[[SECTION purpose]]
Secondary setting for captive discovery and prisoner dragging sequences. Environment reference for building upper floors and window interiors. Stable asset id: building_upper_floors_windows.
[[/SECTION]]

[[SECTION positive_prompt]]
Building window frames, upper floor interior spaces, interior light sources, view of outside through glass, deserted atmosphere, window frame structures, floor level transitions, prisoner entry points, architectural geometry, atmospheric lighting cues, environmental anchors, structural elements, spatial depth, window panes, building facade details.
[[/SECTION]]

[[SECTION negative_prompt]]
proper nouns, specific location names, brand identifiers, overly detailed textures, character elements, furniture pieces, decorative objects, electrical devices, modern technology indicators, crowded scenes, active movement sources, bright daylight conditions, outdoor weather effects, interior clutter, personal items, identifiable landmarks.
[[/SECTION]]

[[SECTION inputs_markdown]]
projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/building_upper_floors_windows.md
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
Window frames serve as recurring environmental anchors. Floor levels establish spatial hierarchy. Interior lighting creates atmospheric consistency. View of outside through windows provides visual connection to exterior environment. Prisoner entry points mark narrative transition zones. Building architecture maintains structural integrity across shots.
[[/SECTION]]

[[SECTION repair_notes_markdown]]
Ensure window frame descriptions remain consistent with architectural geometry. Maintain interior lighting atmosphere without introducing proper nouns. Verify floor level transitions are clear and visible. Check that prisoner entry points are identifiable through descriptive noun phrases only.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
