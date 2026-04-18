# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T18:04:34.720607+00:00
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

Asset id: deserted_city_buildings

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



Environment breakdown path: projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/deserted_city_buildings.md

# Deserted City Buildings Environment

## Environment Role
Combat and observation setting for urban decay environment during fleet engagement sequence.

## Architecture and Geography
Multiple building structures within city layout showing signs of abandonment or destruction. Building facades serve as elevated positions for green Martian warriors firing volleys from windows. Urban architecture provides vertical elements contrasting with horizontal airship movement across sky.

## Lighting and Atmosphere Cues
Daylight conditions with natural illumination across building surfaces. Atmospheric tension conveyed through combat visuals: figures dropping at bullet explosions, banners dissolving in flame, ships swinging broadside. Building interiors suggest abandonment while exteriors show active engagement during fleet battle.

## Scale Cues and Environmental Anchors
Building facades serve as primary vertical anchors for warrior positions. Window openings provide elevated firing positions. Height comparison between green Martian warriors (erect walking) and prisoner establishes scale reference within urban environment. Distant valley/hills vista visible beyond city perimeter provides landscape context.

## Descriptive Noun Phrases for Render-Facing Prompts
- abandoned urban architecture
- building facade vertical elements
- window opening elevated positions
- daylight natural illumination
- combat engagement surfaces
- deserted city structures
- urban decay environment
- distant valley vista visibility

````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_shared_prompts
version: 1

[[FILMCREATOR_RECORD]]
type: environment_prompt
asset_id: deserted_city_buildings

[[SECTION purpose]]
Combat and observation setting for urban decay environment during fleet engagement sequence. Multiple building structures within city layout showing signs of abandonment or destruction. Building facades serve as elevated positions for green Martian warriors firing volleys from windows. Urban architecture provides vertical elements contrasting with horizontal airship movement across sky. Daylight conditions with natural illumination across building surfaces. Atmospheric tension conveyed through combat visuals: figures dropping at bullet explosions, banners dissolving in flame, ships swinging broadside. Building interiors suggest abandonment while exteriors show active engagement during fleet battle.
[[/SECTION]]

[[SECTION positive_prompt]]
abandoned urban architecture, building facade vertical elements, window opening elevated positions, daylight natural illumination, combat engagement surfaces, deserted city structures, urban decay environment, distant valley vista visibility, multiple building structures within city layout, signs of abandonment or destruction, green Martian warriors firing volleys from windows, horizontal airship movement across sky, figures dropping at bullet explosions, banners dissolving in flame, ships swinging broadside
[[/SECTION]]

[[SECTION negative_prompt]]
proper nouns, specific names, modern clean architecture, pristine buildings, night conditions, artificial lighting, indoor only scenes, static composition, no combat elements, no fleet engagement, no Martian warriors, no airships, overexposed shadows, underexposed highlights, blurry details, distorted perspective, unrealistic scale, missing environmental anchors
[[/SECTION]]

[[SECTION inputs_markdown]]
Project slug: princess_of_mars_test
Asset id: deserted_city_buildings
Environment breakdown path: projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/deserted_city_buildings.md
Architecture and Geography: Multiple building structures within city layout showing signs of abandonment or destruction. Building facades serve as elevated positions for green Martian warriors firing volleys from windows. Urban architecture provides vertical elements contrasting with horizontal airship movement across sky.
Lighting and Atmosphere Cues: Daylight conditions with natural illumination across building surfaces. Atmospheric tension conveyed through combat visuals: figures dropping at bullet explosions, banners dissolving in flame, ships swinging broadside. Building interiors suggest abandonment while exteriors show active engagement during fleet battle.
Scale Cues and Environmental Anchors: Building facades serve as primary vertical anchors for warrior positions. Window openings provide elevated firing positions. Height comparison between green Martian warriors (erect walking) and prisoner establishes scale reference within urban environment. Distant valley/hills vista visible beyond city perimeter provides landscape context.
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
Maintain consistent building facade vertical elements across all renders of this environment. Keep daylight natural illumination conditions stable throughout the fleet engagement sequence. Ensure distant valley vista visibility remains present in background composition. Preserve abandoned urban architecture aesthetic without introducing modern clean architecture elements. Building interiors should consistently suggest abandonment while exteriors show active engagement during fleet battle. Height comparison between green Martian warriors and prisoner establishes scale reference within urban environment - maintain this ratio across shots.
[[/SECTION]]

[[SECTION repair_notes_markdown]]
If render shows proper nouns or specific names, replace with descriptive noun phrases. If modern clean architecture appears, remove and restore abandoned urban architecture aesthetic. If night conditions or artificial lighting present, adjust to daylight natural illumination. If static composition dominates, add combat engagement surfaces and fleet movement elements. If indoor only scenes appear, ensure exterior building facades are visible. If blurry details occur, sharpen environmental anchors like building facade vertical elements and window opening elevated positions.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
