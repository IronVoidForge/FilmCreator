# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T05:17:45.543591+00:00
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

Asset id: airship_fleet

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



Environment breakdown path: projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/airship_fleet.md

# Airship Fleet Environment

## Environment Role
Primary transit setting for Martian fleet operations and battle engagement.

## Architecture or Geography
Gray low-profile vessels with long shape, banners mounted on stem and stern, glowing devices positioned on prow. Fleet sails toward valley with swinging motion from window perspective.

## Lighting and Atmosphere Cues
Glowing devices emit light from prow positions. Banners dissolve in flame during battle sequence. Ships swing majestically then erratically through air. Gray color palette dominates fleet appearance.

## Scale Cues and Recurring Environmental Anchors
Twenty vessels visible from narrator's window position. Fleet retreats with several craft limping after twenty minutes. Lead vessel completes circle swinging broadside. Drifting ship intercepted before hitting buildings south of position.

## Useful Descriptive Noun Phrases
Gray airship fleet, glowing prow devices, banner-stem stern, drifting unmanned vessel, funeral pyre ship, swinging broadside vessel, limping retreat craft, gray low-profile vessels, banner-mounted stem stern, glowing device prow.

````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_shared_prompts
version: 1

[[FILMCREATOR_RECORD]]
type: environment_prompt
asset_id: airship_fleet

[[SECTION purpose]]
Primary transit setting for Martian fleet operations and battle engagement.
[[/SECTION]]

[[SECTION positive_prompt]]
Gray low-profile airship fleet with long shape, banners mounted on stem and stern, glowing devices positioned on prow. Fleet sails toward valley with swinging motion from window perspective. Glowing devices emit light from prow positions. Banners dissolve in flame during battle sequence. Ships swing majestically then erratically through air. Gray color palette dominates fleet appearance.
[[/SECTION]]

[[SECTION negative_prompt]]
Proper nouns, specific names, bright colors, static vessels, buildings north of position.
[[/SECTION]]

[[SECTION inputs_markdown]]
projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/airship_fleet.md
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
Twenty vessels visible from narrator's window position. Fleet retreats with several craft limping after twenty minutes. Lead vessel completes circle swinging broadside. Drifting ship intercepted before hitting buildings south of position.
[[/SECTION]]

[[SECTION repair_notes_markdown]]
Banners dissolve in flame during battle sequence needs to be handled carefully to avoid visual confusion.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
