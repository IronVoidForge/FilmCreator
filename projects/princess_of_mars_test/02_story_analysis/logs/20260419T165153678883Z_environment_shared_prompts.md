# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T16:51:53.678883+00:00
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

# City Buildings - CH008 Environment

## Environment Role
Primary setting for observation and action sequences. Multiple vertical levels utilized throughout chapter.

## Architecture and Geography
- Urban structures with upper floors, windows, and roofs
- Building facades facing open plaza area
- Interior spaces accessible from exterior levels
- Rooftop positions for Green Martian firing positions
- Window openings serving as vantage points for Carter's observation

## Lighting and Atmosphere Cues
- Daylight conditions throughout primary sequences
- Smoke accumulation from fire damage
- Missile impact flames spurt from building surfaces
- Fire-induced atmospheric disturbance visible from plaza
- Light reddish copper skin tones of prisoner contrast against building interiors

## Scale Cues and Environmental Anchors
- Building height establishes vertical scale for air craft approach
- Window-to-ground distance defines observation perspective
- Rooftop elevation provides firing platform context
- Plaza proximity creates foreground-background relationship
- Valley visibility from upper levels indicates regional geography

## Descriptive Noun Phrases for Render-Facing Prompts
- "upper floor windows with daylight illumination"
- "building facades facing open plaza area"
- "rooftop positions with Green Martian firing stances"
- "interior spaces accessible from exterior levels"
- "missile impact flames spurt from building surfaces"
- "smoke accumulation from fire damage"

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
This environment prompt defines the urban building structures used in observation and action sequences, establishing vertical scale and atmospheric conditions for the plaza setting. The architecture supports multiple vertical levels with consistent daylight illumination and fire damage effects that maintain visibility of foreground-background relationships.
[[/SECTION]]
[[SECTION positive_prompt]]
upper floor windows with daylight illumination, building facades facing open plaza area, interior spaces accessible from exterior levels, rooftop positions with firing stances, missile impact flames spurt from building surfaces, smoke accumulation from fire damage, valley visibility from upper levels indicating regional geography, vertical scale established through window-to-ground distances
[[/SECTION]]
[[SECTION negative_prompt]]
proper nouns, character names, specific brand identifiers, indoor lighting without daylight, dark interiors, closed windows, empty rooftops, no smoke or fire effects, flat perspective, lack of vertical scale, artificial lighting sources, obscured plaza visibility
[[/SECTION]]
[[SECTION inputs_markdown]]
asset_id: city_buildings
project_slug: princess_of_mars_test
environment_role: Primary setting for observation and action sequences. Multiple vertical levels utilized throughout chapter.
architecture_geography: Urban structures with upper floors, windows, and roofs; Building facades facing open plaza area; Interior spaces accessible from exterior levels; Rooftop positions for firing stances; Window openings serving as vantage points.
lighting_atmosphere: Daylight conditions throughout primary sequences; Smoke accumulation from fire damage; Missile impact flames spurt from building surfaces; Fire-induced atmospheric disturbance visible from plaza.
scale_anchors: Building height establishes vertical scale for air craft approach; Window-to-ground distance defines observation perspective; Rooftop elevation provides firing platform context; Plaza proximity creates foreground-background relationship; Valley visibility from upper levels indicates regional geography.
[[/SECTION]]
[[SECTION continuity_notes_markdown]]
The building structures maintain consistent daylight illumination across all sequences without introducing artificial lighting sources. Smoke and fire effects are present but do not obscure the plaza area or valley visibility. Vertical scale is established through window-to-ground distances and rooftop elevations that remain constant throughout shots. The foreground-background relationship between plaza proximity and upper levels is preserved in every frame.
[[/SECTION]]
[[SECTION repair_notes_markdown]]
Ensure proper nouns like "Green Martian" are replaced with descriptive terms such as "firing stances". Maintain daylight conditions without introducing artificial lighting sources. Keep smoke accumulation visible but not overwhelming to the plaza area. Preserve the plaza foreground-background relationship throughout all shots and ensure valley visibility remains constant as a regional anchor.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
