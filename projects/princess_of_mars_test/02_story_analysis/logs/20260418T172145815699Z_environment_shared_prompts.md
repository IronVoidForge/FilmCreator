# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T17:21:45.815699+00:00
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

Asset id: disabled_airship

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



Environment breakdown path: projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/disabled_airship.md

# Disabled Airship Hull

## Environment Role
Recovery operation zone for looting and destruction sequences.

## Architecture and Geography
Large metallic airship hull structure with open deck areas. Damaged vessel with bodies strewn across decks. Grappling hooks attached to hull exterior.

## Lighting and Atmosphere Cues
Fire and flame effects from burning interior. Smoke billowing from damaged sections. Daylight illuminating exterior hull surfaces.

## Scale Cues and Environmental Anchors
Hull dimensions establish massive scale compared to human figures. Deck areas provide flat ground reference. Grappling hooks mark attachment points.

## Descriptive Noun Phrases
- "metallic airship hull"
- "open deck areas"
- "damaged vessel structure"
- "grappled hull exterior"
- "burning interior effects"

````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_shared_prompts
version: 1
[[FILMCREATOR_RECORD]]
type: environment_prompt
asset_id: disabled_airship
[[SECTION purpose]]
Recovery operation zone for looting and destruction sequences. Large metallic airship hull structure with open deck areas. Damaged vessel with bodies strewn across decks. Grappling hooks attached to hull exterior. Fire and flame effects from burning interior. Smoke billowing from damaged sections. Daylight illuminating exterior hull surfaces. Hull dimensions establish massive scale compared to human figures. Deck areas provide flat ground reference.
[[/SECTION]]
[[SECTION positive_prompt]]
metallic airship hull, open deck areas, damaged vessel structure, grappled hull exterior, burning interior effects, smoke billowing from sections, daylight on exterior surfaces, massive scale architecture, flat ground reference decks, fire and flame effects, grappling hooks attached to hull
[[/SECTION]]
[[SECTION negative_prompt]]
proper nouns, character names, specific locations, indoor settings, night scenes, calm atmosphere, intact structure, small scale, enclosed spaces, peaceful environment, clean surfaces, no damage, no fire, no smoke, no daylight, no debris, no bodies, no destruction
[[/SECTION]]
[[SECTION inputs_markdown]]
- Architecture: metallic airship hull, open deck areas
- Geography: large metallic structure, flat ground reference (decks)
- Lighting: fire/flame effects, smoke billowing, daylight on exterior
- Scale: massive compared to human figures
- Anchors: grappling hooks attached to hull
[[/SECTION]]
[[SECTION continuity_notes_markdown]]
Environment serves as recovery operation zone for looting and destruction sequences. Hull dimensions establish massive scale compared to human figures. Deck areas provide flat ground reference. Grappling hooks mark attachment points on exterior hull. Fire and flame effects from burning interior sections. Smoke billowing from damaged sections. Daylight illuminating exterior hull surfaces. Bodies strewn across decks indicate recent destruction activity.
[[/SECTION]]
[[SECTION repair_notes_markdown]]
Ensure metallic airship hull maintains consistent damage patterns across shots. Grappling hooks should appear at same attachment points in continuity. Fire and smoke effects need to match intensity and location from previous scenes. Daylight exterior illumination must remain consistent with time of day established. Deck areas should show same debris patterns for continuity. Hull structure damage should not change between consecutive shots.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
