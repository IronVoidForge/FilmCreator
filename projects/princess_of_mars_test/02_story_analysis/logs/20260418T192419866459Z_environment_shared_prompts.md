# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T19:24:19.866459+00:00
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

Asset id: airship

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



Environment breakdown path: projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/airship.md

# Airship - Secondary Setting

## Environment Role
Secondary setting as crashed vessel; focal point for recovery, burning, and prisoner extraction operations.

## Architecture or Geography
Wooden parts including upper works and decks; steering gear/propellers; wireless finding/sighting apparatus; smaller guns; gunners positions; officers quarters; crew member areas; carboys on dead sailors/decks.

## Lighting and Atmosphere Cues
Sunlight gleaming on odd devices painted on prows; banners dissolve in spurts of flame; upper works a mass of roaring flames; faint spurt of flame rises from missile.

## Scale Cues and Recurring Environmental Anchors
Large enough to carry twenty crew members; wooden parts large enough for flames to eat; decks large enough for bodies strewn about; upper works large enough for banners to dissolve in flame; craft large enough to soar into air.

## Descriptive Noun Phrases
- crashed vessel structure
- wooden deck surfaces
- upper works flame zone
- steering gear apparatus
- wireless finding equipment
- banner dissolution area
- crew strewn decks

````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_shared_prompts
version: 1

[[FILMCREATOR_RECORD]]
type: environment_prompt
asset_id: airship

[[SECTION purpose]]
Create reusable shared environment-reference prompt for stable local generation of crashed vessel setting with wooden architecture, flame zones, and crew strewn decks. Purpose is to establish secondary setting as focal point for recovery operations with visible atmospheric anchors.
[[/SECTION]]

[[SECTION positive_prompt]]
crashed vessel structure with wooden deck surfaces, upper works flame zone, steering gear apparatus, wireless finding equipment, banner dissolution area, crew strewn decks, sunlight gleaming on odd devices painted on prows, banners dissolving in spurts of flame, upper works mass of roaring flames, faint spurt of flame rising from missile, large enough to carry twenty crew members, wooden parts large enough for flames to eat, decks large enough for bodies strewn about
[[/SECTION]]

[[SECTION negative_prompt]]
proper nouns, specific brand names, fictional character references, indoor settings, modern technology, clean surfaces without damage, organized crew positions, intact structures without burning, peaceful atmosphere, bright daylight without fire effects, empty vessel without debris, small scale objects, detailed mechanical parts without weathering
[[/SECTION]]

[[SECTION inputs_markdown]]
- Project: princess_of_mars_test
- Asset ID: airship
- Environment Role: Secondary setting as crashed vessel; focal point for recovery, burning, and prisoner extraction operations
- Architecture Elements: wooden parts including upper works and decks; steering gear/propellers; wireless finding/sighting apparatus; smaller guns; gunners positions; officers quarters; crew member areas; carboys on dead sailors/decks
- Lighting Cues: sunlight gleaming on odd devices painted on prows; banners dissolve in spurts of flame; upper works a mass of roaring flames; faint spurt of flame rises from missile
- Scale Information: large enough to carry twenty crew members; wooden parts large enough for flames to eat; decks large enough for bodies strewn about; upper works large enough for banners to dissolve in flame; craft large enough to soar into air
- Descriptive Noun Phrases: crashed vessel structure, wooden deck surfaces, upper works flame zone, steering gear apparatus, wireless finding equipment, banner dissolution area, crew strewn decks
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
Environment serves as secondary setting with crashed vessel architecture. Wooden parts and upper works are primary structural elements visible in scene. Flame zones on upper works create atmospheric anchors for recovery operations. Crew strewn decks establish scale and aftermath of crash. Wireless finding equipment and steering gear provide technological context without proper noun references. Banner dissolution area marks time progression through fire effects. All elements maintain consistent scale relative to twenty crew member capacity.
[[/SECTION]]

[[SECTION repair_notes_markdown]]
Review flame zone intensity on upper works for visual consistency across shots. Ensure wooden deck surfaces show appropriate weathering and damage patterns matching crash aftermath. Verify wireless finding equipment placement maintains visibility without cluttering scene composition. Check banner dissolution area timing aligns with fire progression in sequence. Confirm scale cues remain consistent when vessel appears at different distances or angles. Monitor crew strewn decks density to avoid overcrowding while maintaining narrative clarity about recovery operations.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
