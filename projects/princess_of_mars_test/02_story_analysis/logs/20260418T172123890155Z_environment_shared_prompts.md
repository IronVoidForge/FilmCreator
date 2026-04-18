# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T17:21:23.890155+00:00
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

Asset id: building_interior

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



Environment breakdown path: projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/building_interior.md

# Building Interior Depths

## Environment Role
Secondary portal setting for depth transitions and movement.

## Architecture and Geography
Interior corridors and rooms within city buildings. Doorways serve as transition points between interior and exterior spaces. Portal-like entrances leading to deeper levels.

## Lighting and Atmosphere Cues
Dimmer interior lighting compared to exterior. Shadows created by architectural elements. Smoke from burning airship may penetrate through doorways.

## Scale Cues and Environmental Anchors
Doorway frames establish passage scale. Interior walls define enclosed space boundaries. Depth markers visible through portal entrances.

## Descriptive Noun Phrases
- "interior corridor space"
- "doorway transition points"
- "enclosed architectural walls"
- "portal entrance depths"
- "dimmer interior lighting"

````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_shared_prompts
version: 1

[[FILMCREATOR_RECORD]]
type: environment_prompt
asset_id: building_interior

[[SECTION purpose]]
Shared environment reference prompt for interior corridor spaces within city buildings in princess_of_mars_test project. Used for depth transitions and movement through enclosed architectural walls with doorway transition points and portal entrance depths. Establishes dimmer interior lighting conditions compared to exterior spaces, with smoke penetration through doorways from burning vessel sources. Defines scale markers via doorway frames and interior wall boundaries for consistent spatial architecture.
[[/SECTION]]

[[SECTION positive_prompt]]
interior corridor space with enclosed architectural walls, doorway transition points between interior and exterior, portal entrance depths showing depth markers, dimmer interior lighting conditions, shadows cast by architectural elements, smoke penetration through doorways from burning vessel sources, interior wall boundaries defining enclosed space, doorway frames establishing passage scale, interior room spaces within city building structures
[[/SECTION]]

[[SECTION negative_prompt]]
exterior bright lighting conditions, open outdoor spaces without enclosure, clear windows without smoke penetration, proper nouns like airship or specific location names, exterior daylight sources, unobstructed sky views, bright sunlit corridors, open plaza spaces, exterior street scenes, direct sunlight through doorways, exterior architectural elements
[[/SECTION]]

[[SECTION inputs_markdown]]
asset_id: building_interior
project_slug: princess_of_mars_test
environment_role: secondary portal setting for depth transitions and movement
architecture_type: interior corridors and rooms within city buildings
transition_points: doorways between interior and exterior spaces
portal_depths: entrance leading to deeper levels
lighting_condition: dimmer interior lighting compared to exterior
atmosphere_cues: smoke from burning vessel may penetrate through doorways
scale_markers: doorway frames establish passage scale
environmental_anchors: interior walls define enclosed space boundaries, depth markers visible through portal entrances
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
This environment prompt maintains consistent interior corridor spaces across building interiors in the princess_of_mars_test project. Doorway transition points should always show clear distinction between interior and exterior spaces. Enclosed architectural walls must define boundary conditions for all interior scenes. Portal entrance depths require visible depth markers to establish spatial progression. Dimmer interior lighting conditions should be maintained consistently compared to any exterior references. Smoke penetration through doorways from burning vessel sources creates atmospheric continuity across interior corridor spaces. Doorway frames establish passage scale that remains consistent throughout the environment. Interior wall boundaries define enclosed space conditions for all building interior scenes.
[[/SECTION]]

[[SECTION repair_notes_markdown]]
Smoke visibility may need adjustment based on lighting intensity - ensure smoke is visible but not overwhelming. Lighting balance between dimmer interior and any exterior references through doorways requires careful calibration. Doorway frame scale markers should remain consistent across different interior corridor spaces to maintain spatial continuity. Portal entrance depth markers must be clearly visible without competing with smoke effects.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
