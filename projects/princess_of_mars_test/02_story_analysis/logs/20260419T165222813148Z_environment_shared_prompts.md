# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T16:52:22.813148+00:00
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

Asset id: open_ground_plaza

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



Environment breakdown path: projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/open_ground_plaza.md

# Open Ground Plaza - CH008 Environment

## Environment Role
Transit setting for fleet movement and battle effects. Primary ground-level action zone.

## Architecture and Geography
- Open ground plaza area adjacent to city buildings
- Flat terrain suitable for air craft landing approaches
- Ground level connecting building upper floors to valley beyond
- Plaza boundaries defined by surrounding structures
- Missile impact zones on open surface

## Lighting and Atmosphere Cues
- Daylight conditions across entire plaza surface
- Spurt of flame from missile impacts visible on ground
- Fire effects creating atmospheric disturbance
- Light reflecting off building surfaces into plaza
- Smoke patterns drifting across open area

## Scale Cues and Environmental Anchors
- Plaza width establishes horizontal scale for fleet movement
- Building proximity creates foreground-background relationship
- Valley visibility beyond plaza defines regional context
- Hill crests visible from plaza provide directional reference
- Air craft approach paths defined by plaza boundaries

## Descriptive Noun Phrases for Render-Facing Prompts
- "open ground plaza area adjacent to city buildings"
- "flat terrain suitable for air craft landing approaches"
- "missile impact zones on open surface"
- "spurt of flame from missile impacts visible on ground"
- "fire effects creating atmospheric disturbance"

````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_shared_prompts
version: 1
[[FILMCREATOR_RECORD]]
type: environment_prompt
asset_id: open_ground_plaza
[[SECTION purpose]]
Generate stable environment reference for transit setting enabling fleet movement and battle effects. Primary ground-level action zone adjacent to city buildings with flat terrain suitable for aircraft landing approaches. Establishes horizontal scale for fleet operations while connecting building upper floors to valley beyond. Defines regional context through visible hill crests and valley visibility beyond plaza boundaries.
[[/SECTION]]
[[SECTION positive_prompt]]
open ground plaza area adjacent to city buildings, flat terrain suitable for air craft landing approaches, missile impact zones on open surface, daylight conditions across entire plaza surface, spurt of flame from missile impacts visible on ground, fire effects creating atmospheric disturbance, smoke patterns drifting across open area, building proximity creates foreground-background relationship, valley visibility beyond plaza defines regional context, hill crests visible from plaza provide directional reference
[[/SECTION]]
[[SECTION negative_prompt]]
proper nouns, specific brand names, character references, indoor settings, underground locations, water surfaces, mountain peaks, forest areas, desert terrain, urban skyscrapers, residential buildings, industrial zones, military bases, space environments, fantasy realms, historical periods, fictional kingdoms, magical elements, supernatural creatures, time distortions, reality shifts
[[/SECTION]]
[[SECTION inputs_markdown]]
- Asset ID: open_ground_plaza
- Project: princess_of_mars_test
- Environment Role: Transit setting for fleet movement and battle effects. Primary ground-level action zone.
- Architecture: Open ground plaza area adjacent to city buildings, flat terrain suitable for air craft landing approaches, Ground level connecting building upper floors to valley beyond, Plaza boundaries defined by surrounding structures
- Lighting/Atmosphere: Daylight conditions across entire plaza surface, Spurt of flame from missile impacts visible on ground, Fire effects creating atmospheric disturbance, Light reflecting off building surfaces into plaza, Smoke patterns drifting across open area
- Scale: Plaza width establishes horizontal scale for fleet movement, Building proximity creates foreground-background relationship, Valley visibility beyond plaza defines regional context, Hill crests visible from plaza provide directional reference, Air craft approach paths defined by plaza boundaries
[[/SECTION]]
[[SECTION continuity_notes_markdown]]
- Maintain consistent daylight conditions across all shots of open ground plaza area
- Ensure missile impact zones remain on open surface without structural damage to adjacent buildings
- Fire effects should create atmospheric disturbance visible from multiple angles
- Building proximity must preserve foreground-background relationship throughout sequence
- Valley visibility beyond plaza boundaries defines regional context consistently
- Hill crests provide directional reference points for fleet movement paths
- Aircraft approach paths defined by plaza boundaries must remain clear and unobstructed
- Smoke patterns drifting across open area should not obscure critical environmental anchors
[[/SECTION]]
[[SECTION repair_notes_markdown]]
- Verify missile impact zones do not extend into building structures
- Confirm fire effects maintain atmospheric disturbance without overwhelming scene visibility
- Check that valley visibility beyond plaza boundaries remains consistent across shots
- Ensure hill crests visible from plaza provide clear directional reference throughout sequence
- Validate aircraft approach paths defined by plaza boundaries remain unobstructed
- Review smoke patterns drifting across open area for proper environmental integration
- Confirm building proximity maintains foreground-background relationship in all compositions
- Check that daylight conditions remain consistent without unwanted shadows or lighting shifts
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
