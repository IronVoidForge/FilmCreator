# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T20:59:35.034811+00:00
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

Asset id: building_windows_upper_floor

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



Environment breakdown path: projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/building_windows_upper_floor.md

**Role:** Secondary setting / Observation point

**Architecture/Geography:** Multi-story building with upper floor windows facing valley and open ground. Green warriors fire from building windows facing the valley during battle sequences.

**Lighting/Atmosphere:** Interior daylight with exterior battle smoke visible through windows. Bullet explosions create intermittent light flashes from outside.

**Scale:** Medium-scale interior space with window frames providing viewing corridors to exterior environment. Building height creates vertical separation between narrator and action below.

**Anchors:** Window frames, upper floor observation deck, building facade facing valley, interior walls separating from exterior view.

**Descriptive Phrases:** Upper floor windows facing valley, green warriors firing positions, interior observation point, window frame viewing corridors, building facade battle line.

````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_shared_prompts
version: 1

[[FILMCREATOR_RECORD]]
type: environment_prompt
asset_id: building_windows_upper_floor

[[SECTION purpose]]
Stable local generation prompt for upper floor building windows facing valley and open ground. Defines interior observation point with window frame viewing corridors to exterior battle environment. Supports green warriors firing positions from building facade during battle sequences. Maintains medium-scale interior space with vertical separation between narrator and action below.
[[/SECTION]]

[[SECTION positive_prompt]]
Upper floor windows facing valley, interior daylight through glass panes, exterior battle smoke visible outside window frames, bullet explosions creating intermittent light flashes from exterior environment, green warriors firing positions from building facade, multi-story building architecture, window frame viewing corridors to open ground, interior observation deck, building facade battle line, vertical separation between interior and exterior action, medium-scale interior space, upper floor observation point, window frames providing viewing corridors
[[/SECTION]]

[[SECTION negative_prompt]]
proper nouns, character names, location names, specific brand references, indoor artificial lighting only, dark shadows obscuring view, blurred window frames, distorted building geometry, low ceiling height, cramped interior space, missing exterior visibility through windows, static battle smoke, uniform light without flashes, single-story structure, ground floor perspective, closed or blocked windows
[[/SECTION]]

[[SECTION inputs_markdown]]
building_windows_upper_floor, princess_of_mars_test, 02_story_analysis, environment_breakdowns, building_windows_upper_floor.md
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
Maintain consistent window frame geometry across all shots. Preserve vertical separation between interior observation point and exterior battle action. Keep green warriors firing positions aligned with building facade facing valley. Ensure exterior battle smoke and light flashes remain visible through windows without obscuring interior daylight. Maintain medium-scale interior space proportions.
[[/SECTION]]

[[SECTION repair_notes_markdown]]
If window frames appear distorted, adjust to maintain consistent geometry. If exterior visibility is blocked, ensure glass panes remain transparent. If lighting becomes too uniform, reintroduce intermittent light flashes from bullet explosions. Verify vertical separation between narrator and action below remains clear. Check that building height creates proper scale relative to valley environment.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
