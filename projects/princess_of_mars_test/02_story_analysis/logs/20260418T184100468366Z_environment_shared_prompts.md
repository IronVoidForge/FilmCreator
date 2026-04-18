# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T18:41:00.468366+00:00
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

Asset id: building_interiors

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



Environment breakdown path: projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/building_interiors.md

# Building Interiors - Enclosed Spaces

## Environment Role
Secondary setting for prisoner movement and interior observation points. Enclosed spaces contrasting with exterior daylight environments.

## Architecture and Geography
Enclosed interior spaces within city buildings. Multiple rooms or corridors connecting different areas. Interior walls, doors, and structural elements define space boundaries.

## Lighting and Atmosphere Cues
Interior lighting may be dimmer than exterior daylight. Natural light enters through windows or doorways creating contrast zones. Smoke from burning vessel may drift into interior spaces.

## Scale and Environmental Anchors
Human-scale enclosed spaces with architectural features as anchors. Doorways and windows serve as compositional entry points to exterior views. Interior walls define spatial boundaries.

## Descriptive Noun Phrases for Render Prompts
- Enclosed interior spaces
- Interior wall surfaces
- Doorway openings
- Window light contrast
- Dimmer interior lighting
- Smoke drift into interiors
- Human-scale enclosed rooms
- Structural boundary elements

````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_shared_prompts
version: 1

[[FILMCREATOR_RECORD]]
type: environment_prompt
asset_id: building_interiors

[[SECTION purpose]]
Secondary setting for prisoner movement and interior observation points within city buildings. Enclosed spaces contrasting with exterior daylight environments. Human-scale rooms with architectural features serving as compositional anchors. Doorways and windows function as entry points to exterior views while interior walls define spatial boundaries.
[[/SECTION]]

[[SECTION positive_prompt]]
Enclosed interior spaces, interior wall surfaces, doorway openings, window light contrast, dimmer interior lighting, smoke drift into interiors, human-scale enclosed rooms, structural boundary elements, multiple connected corridors, natural light entering through windows, atmospheric smoke presence, architectural feature anchors
[[/SECTION]]

[[SECTION negative_prompt]]
exterior daylight environments, outdoor scenes, bright sunlight, open sky, proper nouns, named locations, specific character references, exterior views from inside, burning vessel flames directly visible, excessive brightness, overexposed lighting, undefined spaces, abstract compositions
[[/SECTION]]

[[SECTION inputs_markdown]]
projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/building_interiors.md
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
Interior spaces maintain consistent dimmer lighting compared to exterior daylight. Smoke from burning vessel drifts into interior areas creating atmospheric presence. Doorways and windows serve as recurring compositional entry points. Human-scale architecture with structural elements defining spatial boundaries remains stable across scenes. Natural light contrast zones through windows create visual interest while maintaining enclosed atmosphere.
[[/SECTION]]

[[SECTION repair_notes_markdown]]
Ensure smoke drift maintains subtle atmospheric presence without overwhelming interior visibility. Verify doorway and window compositions remain consistent as entry points to exterior views. Check that lighting contrast between interior dimness and natural light sources stays balanced across all interior scenes. Maintain human-scale architectural proportions throughout enclosed spaces.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
