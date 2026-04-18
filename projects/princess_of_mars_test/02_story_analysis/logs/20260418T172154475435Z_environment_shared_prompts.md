# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T17:21:54.475435+00:00
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

Asset id: plaza

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



Environment breakdown path: projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/plaza.md

# Martian Plaza

## Environment Role
Primary action arena for crowd gatherings and combat sequences.

## Architecture and Geography
Open paved public square surrounded by building facades. Crowded with green Martian figures. Central gathering space for procession activities.

## Lighting and Atmosphere Cues
Ambient daylight illuminating open plaza space. Smoke and fire effects from naval engagement create dynamic lighting conditions. Dust clouds from combat activity.

## Scale Cues and Environmental Anchors
Building perimeters define plaza boundaries. Crowd density provides human scale reference. Central plaza area serves as focal point for action sequences.

## Descriptive Noun Phrases
- "open paved square"
- "surrounding building facades"
- "green Martian crowd"
- "combat smoke effects"
- "central gathering space"

````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_shared_prompts
version: 1

[[FILMCREATOR_RECORD]]
type: environment_prompt
asset_id: plaza

[[SECTION purpose]]
Generate stable environmental reference for open paved public square surrounded by building facades with green Martian crowd figures. Central gathering space for procession and combat sequences with ambient daylight illumination, smoke effects from naval engagement, dust clouds from combat activity. Building perimeters define plaza boundaries with crowd density providing human scale reference. Central plaza area serves as focal point for action sequences.
[[/SECTION]]

[[SECTION positive_prompt]]
open paved square surrounded by building facades green Martian crowd figures ambient daylight illumination smoke effects from naval engagement dust clouds from combat activity building perimeters define plaza boundaries crowd density provides human scale reference central plaza area serves as focal point for action sequences
[[/SECTION]]

[[SECTION negative_prompt]]
proper nouns specific names closed spaces dark lighting static atmosphere empty square no crowd no smoke no fire no dust no building facades no green figures no ambient light no combat activity no naval engagement no procession activities no gathering space no central plaza area no human scale reference no action sequences
[[/SECTION]]

[[SECTION inputs_markdown]]
- Open paved public square with surrounding building facades
- Green Martian crowd figures throughout plaza space
- Ambient daylight illumination on open plaza surface
- Smoke and fire effects from naval engagement creating dynamic lighting
- Dust clouds from combat activity visible in air
- Building perimeters defining plaza boundaries clearly
- Crowd density providing human scale reference points
- Central plaza area serving as focal point for action sequences
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
Environmental anchors remain consistent across shots: building facades frame the square, green Martian figures populate the space, ambient daylight maintains consistent illumination level. Smoke and fire effects from naval engagement create temporary lighting variations but central plaza remains focal point. Crowd density provides stable human scale reference throughout sequences. Building perimeters maintain plaza boundaries without changing architecture or geography.
[[/SECTION]]

[[SECTION repair_notes_markdown]]
Monitor smoke and fire effect intensity to prevent obscuring building facade details. Ensure green Martian figures remain visible against ambient daylight illumination. Maintain crowd density consistency across shots for stable human scale reference. Verify central plaza area remains clear focal point without being overwhelmed by combat effects. Check that building perimeters continue defining plaza boundaries throughout action sequences.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
