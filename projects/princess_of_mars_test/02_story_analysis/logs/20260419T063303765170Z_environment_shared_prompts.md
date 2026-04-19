# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T06:33:03.765170+00:00
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

Asset id: city_plaza

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



Environment breakdown path: projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/city_plaza.md

# City Plaza - Valley Gathering Space

## Environment Role
Primary setting for chapter opening and closing sequences; central transit hub where procession returns and captive arrives

## Architecture and Geography
Open plaza space within valley city structure. Multi-story buildings surround plaza perimeter with doorways and windows facing inward. Hills visible beyond city limits in background. Ground level paved or compacted earth surface. Building entrances create natural thresholds between interior and exterior spaces.

## Lighting and Atmosphere Cues
Daylight conditions during initial retreat order sequence. Dramatic fire illumination during salvage aftermath when warship burns as funeral pyre. Sudden scurrying creates dynamic shadows across plaza floor. Crimson glow from captive's skin contrasts with ambient daylight. Atmospheric tension conveyed through rapid movement and vanishing Martians within three-minute window.

## Scale Cues and Environmental Anchors
Large open plaza accommodates procession of chariots, mastodons, mounted warriors, and Martian groups. Building doorways serve as entry/exit points for melting crowds. Window openings at multiple heights provide firing positions and observation vantage points. Hills beyond establish valley context and distance scale.

## Descriptive Noun Phrases
- Valley city plaza with surrounding buildings
- Doorway thresholds between interior and exterior
- Multi-story windows facing plaza center
- Hills visible beyond city limits
- Paved or compacted ground surface
- Procession gathering space
- Transit hub for Martian warriors
- Observation deck level windows
- Building entrance archways
- Plaza floor with dynamic shadow play

## Render-Facing Prompt Elements
```
plaza in valley city, multi-story buildings surrounding, hills beyond, daylight to fire illumination transition, doorway thresholds, window openings at multiple heights, chariots and mastodons scale reference, Martian warriors melting into doorways, captive with copper skin visible, crimson glow on cheeks and lips, sudden scurrying shadows
```

````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_shared_prompts
version: 1

[[FILMCREATOR_RECORD]]
type: environment_prompt
asset_id: city_plaza

[[SECTION purpose]]
Stable local generation prompt for valley city plaza scenes, supporting chapter opening and closing sequences where procession returns and captive arrives. Provides consistent environmental reference across multiple shots while maintaining architectural and atmospheric continuity.
[[/SECTION]]

[[SECTION positive_prompt]]
open plaza space within valley city structure, multi-story buildings facing inward toward plaza center, distant hills visible beyond city limits, building entrance archways creating interior exterior transitions, windows at multiple elevation levels providing observation vantage points, procession gathering space with large scale transportation elements, groups of warriors dispersing through building entrances, figure with metallic skin tone contrasting ambient light, warm reddish illumination on facial features, rapid movement creating dynamic shadow patterns
[[/SECTION]]

[[SECTION negative_prompt]]
proper nouns, specific character names, overly detailed textures that break stability, inconsistent lighting conditions, mismatched scale references, static composition lacking dynamic elements, unclear architectural relationships between buildings and plaza
[[/SECTION]]

[[SECTION inputs_markdown]]
```
projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/city_plaza.md
```
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
Maintain consistent building heights and window placements across all plaza shots. Keep hill background scale stable regardless of camera position. Ensure doorway thresholds remain clear visual anchors for character movement transitions. Preserve daylight to fire illumination transition capability for scene variation while keeping core architectural elements recognizable.
[[/SECTION]]

[[SECTION repair_notes_markdown]]
Adjust shadow intensity based on lighting condition variations without altering building geometry. If metallic skin tone appears too dominant, reduce saturation while maintaining contrast with ambient light. Ensure procession scale reference remains visible even when character count varies across shots.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
