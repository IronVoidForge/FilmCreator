# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T06:33:13.709572+00:00
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

# Deserted City Buildings - Tactical Cover Positions

## Environment Role
Secondary setting for combat cover and window fire positions; transit spaces between plaza and interior rooms

## Architecture and Geography
Multi-story structures with numerous windows facing plaza center. Doorways at street level create entry points. Interior spaces accessible through doorways and stairwells implied by multi-level construction. Buildings positioned throughout valley city with consistent architectural style. Windows serve as primary observation and firing positions.

## Lighting and Atmosphere Cues
Daylight conditions during retreat order sequence. Fire illumination from burning warship casts dramatic shadows across building facades. Sudden scurrying creates dynamic shadow movement on building surfaces. Interior spaces dimly lit compared to plaza exterior. Window frames create strong geometric patterns against sky background.

## Scale Cues and Environmental Anchors
Building height accommodates multiple levels of window openings. Doorway width accommodates full-sized chariots and mastodons passage. Window size allows clear observation of plaza activity below. Building mass establishes valley city scale relative to hills beyond. Interior spaces implied through doorway thresholds and shadow depth.

## Descriptive Noun Phrases
- Multi-story buildings with numerous windows
- Doorway thresholds at street level
- Window openings facing plaza center
- Interior spaces accessible through doorways
- Building facades with geometric window patterns
- Deserted structures in valley city
- Tactical cover positions for warriors
- Observation vantage points at multiple heights
- Stairwells implied by multi-level construction
- Building mass establishing valley scale

## Render-Facing Prompt Elements
```
multi-story buildings in valley city, numerous windows facing plaza center, doorway thresholds at street level, interior spaces dimly lit, window frames creating geometric patterns against sky, deserted structures with consistent architectural style, building height accommodating multiple levels, doorway width for chariots and mastodons passage, fire illumination casting dramatic shadows on facades
```

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
Secondary setting for combat cover and window fire positions; transit spaces between plaza and interior rooms. Multi-story structures with numerous windows facing plaza center. Doorways at street level create entry points. Interior spaces accessible through doorways and stairwells implied by multi-level construction. Buildings positioned throughout valley city with consistent architectural style. Windows serve as primary observation and firing positions.
[[/SECTION]]

[[SECTION positive_prompt]]
multi-story buildings in valley city, numerous windows facing plaza center, doorway thresholds at street level, interior spaces dimly lit, window frames creating geometric patterns against sky, deserted structures with consistent architectural style, building height accommodating multiple levels, doorway width for chariots and mastodons passage, fire illumination casting dramatic shadows on facades
[[/SECTION]]

[[SECTION negative_prompt]]
proper nouns, specific character names, interior rooms not accessible through doorways, single-story buildings, windows without geometric patterns, night conditions without fire illumination, inconsistent architectural style, building mass not establishing valley scale
[[/SECTION]]

[[SECTION inputs_markdown]]
projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/deserted_city_buildings.md
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
Building facades maintain consistent architectural style throughout valley city. Window frames create strong geometric patterns against sky background. Fire illumination from burning warship casts dramatic shadows across building facades. Interior spaces dimly lit compared to plaza exterior. Doorway width accommodates full-sized chariots and mastodons passage. Building height accommodates multiple levels of window openings.
[[/SECTION]]

[[SECTION repair_notes_markdown]]
Ensure all prompts use descriptive noun phrases without proper nouns. Maintain stable architecture, geography, scale, atmosphere, and recurring environmental anchors. Verify building mass establishes valley city scale relative to hills beyond. Confirm interior spaces accessible through doorways and stairwells implied by multi-level construction.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
