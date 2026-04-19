# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T05:18:01.862526+00:00
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

Asset id: building_interior_portal

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



Environment breakdown path: projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/building_interior_portal.md

# Building Interior/Portal Environment

## Environment Role
Secondary transit setting for human capture sequence and prisoner reveal.

## Architecture or Geography
Building entrance where prisoner dragged through portal by female Martians. Warriors drag small figure from ship into building interior. Portal serves as transition point between exterior fleet operations and interior captivity.

## Lighting and Atmosphere Cues
Prisoner dragged roughly through portal creating dramatic lighting effect. Female Martian figures create intimate lighting contrast to battle exterior. Interior space contrasts with gray airship exterior.

## Scale Cues and Recurring Environmental Anchors
Small figure dragged from ship into building. Warriors drag small figure from disabled vessel. Human woman being dragged into building by female Martians. Portal serves as entry point for prisoner reveal sequence.

## Useful Descriptive Noun Phrases
Building entrance portal, prisoner drag sequence, female Martian figures, interior captivity space, exterior-to-interior transition, small figure reveal, human woman capture, warrior drag sequence, portal entry point, female Martian captors.

````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_shared_prompts
version: 1
[[FILMCREATOR_RECORD]]
type: environment_prompt
asset_id: building_interior_portal
[[SECTION purpose]]
This environment prompt defines the secondary transit setting for the prisoner reveal sequence. It establishes the building entrance portal as a transition point between exterior fleet operations and interior captivity, focusing on lighting contrast and scale dynamics during the drag motion.
[[/SECTION]]
[[SECTION positive_prompt]]
building entrance portal, prisoner drag sequence, alien female figures, interior captivity space, exterior-to-interior transition, small figure reveal, prisoner capture, warrior drag sequence, portal entry point, dramatic lighting effect, intimate lighting contrast, gray airship exterior, disabled vessel, rough dragging motion, atmospheric shadows, scale difference between prisoner and captors
[[/SECTION]]
[[SECTION negative_prompt]]
blurry, distorted faces, wrong scale, floating objects, bright sunlight, clean interior, modern furniture, text, watermark, low resolution, overexposed, underexposed, deformed limbs, extra fingers, missing portal structure, inconsistent lighting, proper nouns, specific names
[[/SECTION]]
[[SECTION inputs_markdown]]
- Asset ID: building_interior_portal
- Context: Secondary transit setting for human capture sequence
- Story Arc: Transition from exterior fleet operations to interior captivity space
[[/SECTION]]
[[SECTION continuity_notes_markdown]]
This scene connects to exterior fleet operations (previous) and leads into interior captivity space (next). The portal serves as the visual anchor for the transition from battle to imprisonment. Lighting shifts from gray airship exterior to intimate interior contrast. Scale remains consistent with small prisoner figure relative to alien captors.
[[/SECTION]]
[[SECTION repair_notes_markdown]]
Ensure lighting contrast between exterior gray airship and interior space is maintained. Verify scale of prisoner remains small relative to alien figures. Avoid proper nouns in prompt generation. Focus on descriptive noun phrases for stability.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
