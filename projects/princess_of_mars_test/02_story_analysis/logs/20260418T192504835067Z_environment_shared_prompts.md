# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T19:25:04.835067+00:00
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

Asset id: valley

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



Environment breakdown path: projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/valley.md

# Valley - Secondary Setting

## Environment Role
Secondary setting where burning ship drifts southeast; open space for ship to soar majestically into air and rise higher as flames eat wooden parts.

## Architecture or Geography
Open valley floor allowing ship to drift southeast; space large enough for warship to soar into air; directional flow toward southeast.

## Lighting and Atmosphere Cues
Southeasterly direction visible; flames rising higher as they eat wooden parts; open sky above valley floor.

## Scale Cues and Recurring Environmental Anchors
Valley large enough for great warship to soar majestically into air; space allowing ship to drift southeast; directional flow toward southeast; atmospheric openness for fire rise.

## Descriptive Noun Phrases
- open valley floor
- southeast drift direction
- soaring warship space
- flame rise zone
- open sky above valley

````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_shared_prompts
version: 1

[[FILMCREATOR_RECORD]]
type: environment_prompt
asset_id: valley

[[SECTION purpose]]
Secondary setting prompt for open valley floor where warship drifts southeast and flames rise higher; space allowing ship to soar into air with atmospheric openness for fire movement and directional flow toward southeast
[[/SECTION]]

[[SECTION positive_prompt]]
open valley floor, southeast drift direction, soaring warship space, flame rise zone, open sky above valley, large enough for great warship to soar majestically into air, space allowing ship to drift southeast, atmospheric openness for fire rise
[[/SECTION]]

[[SECTION negative_prompt]]
proper nouns, closed spaces, wrong directional flow, cramped environment, restricted movement, confined atmosphere, limited sky visibility, small scale for warship, blocked southeast direction, constrained flame movement
[[/SECTION]]

[[SECTION inputs_markdown]]
projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/valley.md
asset_id: valley
environment_role: secondary setting where burning ship drifts southeast
architecture_geography: open valley floor allowing ship to drift southeast; space large enough for warship to soar into air; directional flow toward southeast
lighting_atmosphere: southeasterly direction visible; flames rising higher as they eat wooden parts; open sky above valley floor
scale_environmental_anchors: valley large enough for great warship to soar majestically into air; space allowing ship to drift southeast; atmospheric openness for fire rise
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
This valley setting connects to the burning ship drifting southeast as a secondary environment where flames eat wooden parts and ship rises higher into open sky. The directional flow toward southeast maintains consistency with the ship's movement path. Atmospheric openness for fire rise ensures visual continuity with flame movement across the scene.
[[/SECTION]]

[[SECTION repair_notes_markdown]]
Ensure all descriptive noun phrases avoid proper nouns in final prompt bodies. Verify scale cues maintain consistency with warship size requirements. Check that directional flow toward southeast remains visible and unobstructed in generated imagery. Confirm atmospheric openness allows flame movement without visual constraints.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
