# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T17:21:36.744321+00:00
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

Asset id: building_roofs

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



Environment breakdown path: projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/building_roofs.md

# Building Roofs

## Environment Role
Secondary transit setting for elevated movement and observation.

## Architecture and Geography
Flat rooftop surfaces atop city buildings. Multiple roof levels create tiered urban landscape. Open-air exposure to Martian sky.

## Lighting and Atmosphere Cues
Direct sunlight on exposed surfaces. Sharp shadows between adjacent structures. Dust particles visible in light beams suggesting atmospheric density.

## Scale Cues and Environmental Anchors
Roof edges establish building height references. Adjacent rooftops provide depth markers across cityscape.

## Descriptive Noun Phrases
- "flat rooftop surface"
- "tiered urban landscape"
- "exposed Martian sky"
- "adjacent roof levels"
- "cityscape depth markers"

````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_shared_prompts
version: 1

[[FILMCREATOR_RECORD]]
type: environment_prompt
asset_id: building_roofs

[[SECTION purpose]]
Secondary transit setting for elevated movement and observation. Flat rooftop surfaces atop city buildings create tiered urban landscape with open-air exposure to dusty red sky. Roof edges establish building height references while adjacent rooftops provide depth markers across cityscape. Direct sunlight on exposed surfaces creates sharp shadows between structures with dust particles visible in light beams suggesting atmospheric density.
[[/SECTION]]

[[SECTION positive_prompt]]
flat rooftop surface, tiered urban landscape, open-air dusty red sky, direct sunlight on exposed surfaces, sharp shadows between adjacent structures, dust particles visible in light beams, roof edges establishing building height references, adjacent rooftops providing depth markers across cityscape, flat horizontal planes atop vertical structures, multiple roof levels creating layered composition
[[/SECTION]]

[[SECTION negative_prompt]]
enclosed interior spaces, ground level terrain, overcast cloudy skies, smooth surfaces without texture, enclosed corridors, underground passages, vertical walls without rooftop extensions, enclosed glass ceilings, enclosed metal canopies, enclosed concrete slabs, enclosed wooden platforms, enclosed stone terraces, enclosed brick parapets, enclosed tile roofs, enclosed slate surfaces, enclosed shingle coverings, enclosed thatch layers
[[/SECTION]]

[[SECTION inputs_markdown]]
projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/building_roofs.md
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
Maintain consistent rooftop geometry across adjacent structures. Preserve atmospheric density cues with dust particles in light beams. Keep tiered urban landscape composition stable when transitioning between roof levels. Ensure direct sunlight and sharp shadows remain consistent for elevated movement sequences. Maintain open-air exposure to dusty red sky as recurring environmental anchor.
[[/SECTION]]

[[SECTION repair_notes_markdown]]
Verify flat rooftop surfaces do not transition abruptly to enclosed spaces. Confirm dust particles in light beams maintain atmospheric density consistency across adjacent structures. Ensure tiered urban landscape composition remains stable when transitioning between roof levels. Check that direct sunlight and sharp shadows remain consistent for elevated movement sequences. Maintain open-air exposure to dusty red sky as recurring environmental anchor without proper noun references.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
