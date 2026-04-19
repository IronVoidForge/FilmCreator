# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T02:59:25.730982+00:00
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

Asset id: disabled_airship_interior_deck

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



Environment breakdown path: projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/disabled_airship_interior_deck.md

# Disabled Airship Interior / Deck

## Environment Role
Secondary setting for looting and burning.

## Architecture or Geography
Airship hull interior, decks, upper works.

## Lighting and Atmosphere Cues
Roaring flames, smoke, wooden parts eaten away, high accuracy targeting weak points.

## Scale Cues and Recurring Environmental Anchors
Drifting altitude (fifty feet), ship length, erratically limping vessel.

## Useful Descriptive Noun Phrases
"Airship deck", "Upper works", "Flame-filled hull", "Disabled vessel interior".

````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_shared_prompts
version: 1

[[FILMCREATOR_RECORD]]
type: environment_prompt
asset_id: disabled_airship_interior_deck

[[SECTION purpose]]
Secondary setting for looting and burning operations within airship hull interior. Focus on upper works, decks, and damaged wooden structures with high atmospheric intensity from flames and smoke.
[[/SECTION]]

[[SECTION positive_prompt]]
Airship deck interior, upper works structure, flame-filled hull, disabled vessel interior, drifting altitude fifty feet, ship length scale, erratically limping vessel, roaring flames, smoke atmosphere, wooden parts eaten away, high accuracy targeting weak points, atmospheric anchors, environmental geography, stable architecture, recurring structural elements, damaged wooden framework, floating deck platform, burning interior spaces
[[/SECTION]]

[[SECTION negative_prompt]]
proper nouns, brand names, specific character references, modern technology, clean structures, intact woodwork, calm atmosphere, ground level, stationary vessel, bright lighting, pristine surfaces, contemporary materials, sharp edges, unburnt sections, stable platforms, clear visibility, organized spaces, new construction, polished surfaces, undamaged framework
[[/SECTION]]

[[SECTION inputs_markdown]]
Environment Role: Secondary setting for looting and burning.

Architecture or Geography: Airship hull interior, decks, upper works.

Lighting and Atmosphere Cues: Roaring flames, smoke, wooden parts eaten away, high accuracy targeting weak points.

Scale Cues and Recurring Environmental Anchors: Drifting altitude (fifty feet), ship length, erratically limping vessel.

Useful Descriptive Noun Phrases: Airship deck, Upper works, Flame-filled hull, Disabled vessel interior.
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
Maintain consistent airship interior scale across all shots. Keep flame and smoke density proportional to damage level. Ensure upper works and deck structures remain recognizable as part of same vessel. Preserve drifting altitude visual cues throughout sequence. Match wooden framework damage patterns with burning intensity.
[[/SECTION]]

[[SECTION repair_notes_markdown]]
Review flame source consistency between environment shots. Check that structural anchors (decks, upper works) maintain proper spatial relationships. Verify altitude drift is visually represented in each frame. Ensure damaged woodwork shows progressive deterioration matching fire exposure. Confirm vessel limping motion translates to interior perspective shifts.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
