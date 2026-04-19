# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T02:57:27.784139+00:00
- task: environment_extraction

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

Chapter id: CH008

Task: extract environment families into an environment index plus one Markdown file per environment family.

Return exactly one Markdown packet using this outer envelope:
[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
...environment_index_markdown content...
[[/SECTION]]

Repeat one FILMCREATOR_RECORD block for every extracted item of that type.

[[FILMCREATOR_RECORD]]
type: environment
asset_id: <value>

[[SECTION markdown]]
...markdown content...
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]



Asset id rules:

- lowercase snake_case

- stable across later reruns

- include stable environment families rather than every one-off mention

- prefer visible geography and atmosphere over literary abstraction



Each environment Markdown file should include:

- environment role such as primary, secondary, or transit setting

- architecture or geography

- lighting and atmosphere cues

- scale cues and recurring environmental anchors

- useful descriptive noun phrases for later render-facing prompt writing



Chapter summary:

# Chapter Summary: CH008 - A Fair Captive from the Sky

## Story Beats (Decomposition Ready)
1.  **Return Interrupted:** Procession returns to city after incubation ceremony; sudden retreat order given immediately upon entering open ground.
2.  **Fleet Sighting:** Carter observes gray-painted airships approaching from hill crest; fleet count approximates twenty vessels.
3.  **Battle Engagement:** Green Martians fire first volley; enemy ships return fire with high accuracy targeting specific weak points (guns, officers, steering).
4.  **Ship Disabled:** One vessel limps erratically, unmanned, drifting southeast. Warriors rush to intercept before it hits buildings.
5.  **Looting & Burning:** Warriors board disabled ship, remove loot (arms, jewels, water), empty carboys over dead sailors, then burn vessel from within using missile.
6.  **Emotional Aftermath:** Carter feels depression and yearning for the enemy fleet; fears return attack; city remains deserted for a week.
7.  **Captive Discovery:** As prisoners are dragged into building, Carter sees a slender girlish figure with copper skin and black hair. She signals him before being taken inside.

## Visual Continuity Facts
- **Airships:** Long, low, gray-painted hulls; banners swung from stem to stern; odd devices painted on prow.
- **Warriors:** Green Martians; mounted or in chariots; fire from windows/roofs; carry spears and grappling hooks.
- **Disabled Ship:** Drifting southeast at approx fifty feet altitude; decks and upper works mass of roaring flames later; wooden parts eaten away.
- **Captive Appearance:** Slender, girlish figure; oval face; light reddish copper skin; coal black waving hair (loose coiffure); naked except highly wrought ornaments; crimson cheeks/ruby lips.
- **Locations:** City plaza, building upper floors/windows, open ground/valley, outlying hills.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - CH008

- city_plaza_open_ground
- outlying_hills_hill_crest
- disabled_airship_interior_deck
- building_upper_floors_windows
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: city_plaza_open_ground

[[SECTION markdown]]
# City Plaza / Open Ground

## Environment Role
Primary setting for the procession return and initial retreat order.

## Architecture or Geography
City plaza, open ground/valley floor leading to building facades.

## Lighting and Atmosphere Cues
Daylight, sudden tension, deserted city feel later (city remains deserted for a week).

## Scale Cues and Recurring Environmental Anchors
Procession scale, distant hills, building facades, fifty feet altitude reference for drifting ship.

## Useful Descriptive Noun Phrases
"City plaza", "Open valley floor", "Procession route", "Building facades".
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: outlying_hills_hill_crest

[[SECTION markdown]]
# Outlying Hills / Hill Crest

## Environment Role
Secondary setting for fleet sighting and approach.

## Architecture or Geography
Outlying hills, hill crest elevation.

## Lighting and Atmosphere Cues
Distant view, gray sky implied by airships, approach from elevation.

## Scale Cues and Recurring Environmental Anchors
Hill crest, distant city skyline, fleet count approximates twenty vessels.

## Useful Descriptive Noun Phrases
"Hill crest", "Outlying ridge", "Fleet approach path".
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: disabled_airship_interior_deck

[[SECTION markdown]]
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
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: building_upper_floors_windows

[[SECTION markdown]]
# Building Upper Floors / Windows

## Environment Role
Secondary setting for captive discovery and prisoner dragging.

## Architecture or Geography
Building upper floors, windows.

## Lighting and Atmosphere Cues
Interior light, view of outside, deserted feel.

## Scale Cues and Recurring Environmental Anchors
Window frames, floor levels, prisoners dragged into building.

## Useful Descriptive Noun Phrases
"Building window", "Upper floor interior", "Prisoner entry point".
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
