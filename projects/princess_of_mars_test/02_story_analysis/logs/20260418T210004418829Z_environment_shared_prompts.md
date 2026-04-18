# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T21:00:04.418829+00:00
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

Asset id: plaza_return

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



Environment breakdown path: projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/plaza_return.md

**Role:** Secondary setting / Gathering space

**Architecture/Geography:** Plaza where warriors return after danger of air craft passed for a week. Building interior spaces visible as prisoner dragged into building by green Martian females.

**Lighting/Atmosphere:** Interior daylight with relief atmosphere after battle danger passes. Mixed emotions create atmospheric tension despite physical safety.

**Scale:** Medium-scale plaza space accommodating warrior gatherings and prisoner transport. Building interiors provide vertical depth for observation from upper floors.

**Anchors:** Plaza gathering areas, building entrance points, interior observation spaces, prisoner transport paths, warrior assembly zones.

**Descriptive Phrases:** Plaza return zone, danger passed atmosphere, green Martian female figures, building interior spaces, prisoner drag path, warrior assembly area.

````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_shared_prompts
version: 1

[[FILMCREATOR_RECORD]]
type: environment_prompt
asset_id: plaza_return

[[SECTION purpose]]
Generate stable environment reference prompt for secondary gathering space where warriors return after danger passes. Focus on medium-scale plaza architecture with building interior visibility, interior daylight atmosphere, and prisoner transport paths as recurring environmental anchors. Use asset id plaza_return for stable generation consistency.
[[/SECTION]]

[[SECTION positive_prompt]]
medium scale plaza gathering space, building interior spaces visible from upper floors, interior daylight lighting, relief atmosphere after battle danger passes, warrior assembly zones, prisoner drag path through entrance points, green Martian female figures transporting prisoners, vertical depth observation spaces, mixed emotions atmospheric tension, physical safety environment, plaza return zone architecture, danger passed atmosphere, building entrance points, interior observation spaces
[[/SECTION]]

[[SECTION negative_prompt]]
proper nouns, specific names, air craft references, week duration markers, prisoner resistance, warrior injury details, exterior daylight, night time, chaotic battle scenes, empty plaza, single figure composition, high scale architecture, low scale intimate spaces, dark atmosphere, relief tension absence, physical danger present, green skin tones, red color palette, abstract forms, geometric distortion
[[/SECTION]]

[[SECTION inputs_markdown]]
project: princess_of_mars_test
asset_id: plaza_return
role: secondary setting gathering space
architecture: plaza with building interior visibility
lighting: interior daylight relief atmosphere
scale: medium scale plaza space
anchors: plaza gathering areas, building entrance points, interior observation spaces, prisoner transport paths, warrior assembly zones
descriptive phrases: plaza return zone, danger passed atmosphere, green Martian female figures, building interior spaces, prisoner drag path, warrior assembly area
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
Plaza return zone maintains consistent medium-scale architecture across all generated frames. Building interior visibility from upper floors remains stable anchor point. Interior daylight lighting conditions preserved for relief atmosphere consistency. Warrior assembly zones and prisoner transport paths function as recurring environmental anchors throughout sequence. Green Martian female figures maintain consistent visual presence during prisoner transport sequences. Danger passed atmosphere creates unified emotional tone despite physical safety environment.
[[/SECTION]]

[[SECTION repair_notes_markdown]]
Monitor proper noun usage in prompt bodies to ensure descriptive noun phrase consistency. Verify interior daylight lighting conditions remain stable across generated frames. Check building interior visibility from upper floors maintains architectural continuity. Ensure medium-scale plaza architecture does not drift toward high or low scale extremes. Confirm prisoner transport paths and warrior assembly zones function as consistent environmental anchors throughout sequence generation.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
