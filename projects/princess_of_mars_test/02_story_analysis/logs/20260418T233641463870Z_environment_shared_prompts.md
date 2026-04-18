# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T23:36:41.463870+00:00
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

Asset id: open_plaza

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



Environment breakdown path: projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/open_plaza.md

**Environment Role:** Secondary / Retreat Destination (Transit Setting)

**Architecture or Geography:** Open ground/plaza at valley floor level. Ground space in front of city buildings. Entrance to building where prisoner is dragged.

**Lighting and Atmosphere Cues:** Open daylight conditions. Clear visibility for Carter's observation from window/balcony. No specific weather effects noted, standard ambient lighting.

**Scale Cues and Recurring Environmental Anchors:** Ground level space allowing dragging action. Building entrance serves as transition point to interior. Open space allows fleet arrival context.

**Descriptive Noun Phrases for Render-Facing Prompts:** Open ground plaza at valley floor, building entrance with prisoner being dragged, open daylight on plaza surface, transition space between fleet and city interior.

````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_shared_prompts
version: 1

[[FILMCREATOR_RECORD]]
type: environment_prompt
asset_id: open_plaza

[[SECTION purpose]]
Secondary transit destination environment for prisoner movement and fleet arrival context. Open plaza space at valley floor level serving as transition zone between exterior ground and city interior. Ground space positioned in front of building structures with clear daylight visibility conditions. Entrance point functions as architectural anchor for dragging action sequences and character observation from elevated positions.
[[/SECTION]]

[[SECTION positive_prompt]]
Open ground plaza at valley floor, building entrance with prisoner being dragged, open daylight on plaza surface, transition space between fleet and city interior, ground level space allowing dragging action, clear visibility conditions, ambient lighting without weather effects, exterior ground positioned in front of city buildings, architectural transition point to interior spaces.
[[/SECTION]]

[[SECTION negative_prompt]]
character names, proper nouns, specific weather conditions, rain or snow effects, night time, indoor scenes, close-up character faces, dialogue bubbles, text overlays, branded logos, fictional location names, mountain peaks, water features, vegetation growth, ornate decorations, dramatic shadows.
[[/SECTION]]

[[SECTION inputs_markdown]]
Project: princess_of_mars_test
Asset: open_plaza
Environment Role: Secondary / Retreat Destination (Transit Setting)
Architecture or Geography: Open ground/plaza at valley floor level. Ground space in front of city buildings. Entrance to building where prisoner is dragged.
Lighting and Atmosphere Cues: Open daylight conditions. Clear visibility for Carter's observation from window/balcony. No specific weather effects noted, standard ambient lighting.
Scale Cues and Recurring Environmental Anchors: Ground level space allowing dragging action. Building entrance serves as transition point to interior. Open space allows fleet arrival context.
Descriptive Noun Phrases for Render-Facing Prompts: Open ground plaza at valley floor, building entrance with prisoner being dragged, open daylight on plaza surface, transition space between fleet and city interior.
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
Maintain consistent valley floor elevation across all plaza scenes. Keep daylight conditions uniform without introducing weather variations. Preserve architectural relationship between plaza ground and building entrances. Ensure dragging action sequences occur at same ground level height. Building entrance transition points must remain visible as anchor for character movement between exterior and interior spaces. Fleet arrival context should utilize open space without obstructing plaza visibility.
[[/SECTION]]

[[SECTION repair_notes_markdown]]
Review prompt bodies to ensure no proper nouns slipped into positive_prompt section. Verify negative_prompt includes all mentioned weather effects that are not part of standard ambient lighting. Check that continuity notes reference specific architectural anchors consistently across scene variations. Confirm asset_id open_plaza is only used in inputs_markdown and not embedded in render-facing prompt text. Ensure scale cues maintain ground level consistency without introducing elevation changes that contradict valley floor positioning.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
