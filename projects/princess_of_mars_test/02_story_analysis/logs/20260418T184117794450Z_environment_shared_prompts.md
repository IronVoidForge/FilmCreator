# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T18:41:17.794450+00:00
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

Asset id: rooftops

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



Environment breakdown path: projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/rooftops.md

# Rooftops - City Rooftop Network

## Environment Role
Secondary setting for elevated positions, transit zone between plaza and building interiors, vantage points for Green Martian Warriors.

## Architecture and Geography
Network of connected rooftop surfaces across city buildings. Elevated platforms with parapets and access points. Open-air spaces with multiple levels visible from different angles.

## Lighting and Atmosphere Cues
Daylight with sunlight reflecting off ship devices mounted on rooftops. Smoke and flame from burning vessel drift upward through air. Green Martian fire volleys create bright flashes against daylight sky.

## Scale and Environmental Anchors
City-scale elevated network with multiple building heights visible. Rooftop edges define horizontal boundaries. Parapets and access points serve as compositional anchors. Distant plaza appears below at reduced scale.

## Descriptive Noun Phrases for Render Prompts
- Connected rooftop surfaces
- Elevated city platforms
- Ship device reflections
- Smoke drift upward
- Green Martian fire volleys
- Rooftop parapets
- Multiple building heights
- Open-air elevated spaces

````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_shared_prompts
version: 1

[[FILMCREATOR_RECORD]]
type: environment_prompt
asset_id: rooftops

[[SECTION purpose]]
Secondary setting for elevated positions and transit zone between plaza and building interiors. Vantage points for Green Martian Warriors with multiple levels visible from different angles. Open-air spaces with parapets and access points serving as compositional anchors across city-scale elevated network.
[[/SECTION]]

[[SECTION positive_prompt]]
Connected rooftop surfaces, elevated city platforms, ship device reflections, smoke drift upward, Green Martian fire volleys, rooftop parapets, multiple building heights, open-air elevated spaces, daylight sky with sunlight reflecting off mounted devices, horizontal boundaries defined by edges, distant plaza below at reduced scale
[[/SECTION]]

[[SECTION negative_prompt]]
indoor scenes, enclosed spaces, proper nouns, single level views, dark night sky, indoor lighting, ground floor perspective, closed parapets, solid walls without access points, static atmosphere, low angle shots from plaza level
[[/SECTION]]

[[SECTION inputs_markdown]]
projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/rooftops.md
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
Stable architecture: network of connected rooftop surfaces across city buildings with parapets and access points. Geography: elevated platforms with multiple building heights visible from different angles. Scale: city-scale elevated network with distant plaza appearing below at reduced scale. Atmosphere: daylight with smoke and flame drifting upward through air, Green Martian fire volleys creating bright flashes against sky. Recurring environmental anchors: rooftop edges defining horizontal boundaries, parapets and access points serving as compositional anchors.
[[/SECTION]]

[[SECTION repair_notes_markdown]]
Ensure ship device reflections remain visible on connected surfaces. Maintain smoke drift direction consistent with upward movement through air. Keep Green Martian fire volleys appearing against daylight sky without contradicting lighting conditions. Verify multiple building heights are visible from different angles to maintain elevated perspective continuity.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
