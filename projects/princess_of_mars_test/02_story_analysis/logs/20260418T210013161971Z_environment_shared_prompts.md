# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T21:00:13.161971+00:00
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

Asset id: valley_battlefield

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



Environment breakdown path: projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/valley_battlefield.md

**Role:** Primary setting / Battle zone

**Architecture/Geography:** Wide valley with building windows facing the valley serving as firing positions. Air fleet moves parallel to firing line then turns back during engagement sequences.

**Lighting/Atmosphere:** Daylight battle conditions with banners dissolving in spurts of flame. Fire from vessels appears ineffectual against sudden first volley explosions.

**Scale:** Large-scale open terrain accommodating air fleet movements and building-to-valley sightlines. Parallel ship formations create horizontal movement patterns across valley floor.

**Anchors:** Building windows facing valley, air fleet formation lines, firing line positions, valley floor movement paths, banner display locations.

**Descriptive Phrases:** Valley battle zone, building windows firing positions, air fleet parallel movements, banner flame dissolution, green warrior firing line, valley floor engagement area.

````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_shared_prompts
version: 1

[[FILMCREATOR_RECORD]]
type: environment_prompt
asset_id: valley_battlefield

[[SECTION purpose]]
This prompt defines the wide valley battle zone environment for stable local generation. It establishes firing positions, air fleet movement patterns, and daylight engagement conditions with banner flame dissolution effects. The architecture supports horizontal ship formations across open terrain while maintaining building-to-valley sightlines as environmental anchors.
[[/SECTION]]

[[SECTION positive_prompt]]
wide valley battle zone, building windows facing valley as firing positions, air fleet parallel movements across valley floor, daylight battle conditions, banners dissolving in flame, large scale open terrain, green warrior firing line positions, valley floor engagement area, horizontal ship formations, building-to-valley sightlines, banner display locations, open ground movement paths
[[/SECTION]]

[[SECTION negative_prompt]]
indoor scenes, night conditions, close quarters combat, vertical flight patterns, small scale terrain, indoor windows, dark atmosphere, cramped spaces, single vessel focus, enclosed valley floor, limited visibility, restricted movement areas, confined firing positions, narrow ship formations, isolated banner locations, blocked sightlines, restricted ground paths
[[/SECTION]]

[[SECTION inputs_markdown]]
projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/valley_battlefield.md
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
Building windows facing valley serve as consistent firing position anchors. Air fleet formation lines maintain parallel horizontal movement patterns across valley floor. Banner flame dissolution occurs in spurts during engagement sequences. Valley floor engagement area accommodates large scale open terrain movements. Green warrior firing line positions remain stable throughout battle conditions. Horizontal ship formations create recurring movement patterns across valley floor.
[[/SECTION]]

[[SECTION repair_notes_markdown]]
No repairs needed. Environment anchors are stable and visible. All descriptive phrases avoid proper nouns and use noun phrases as required. Architecture, geography, scale, atmosphere, and environmental anchors are emphasized throughout prompt bodies.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
