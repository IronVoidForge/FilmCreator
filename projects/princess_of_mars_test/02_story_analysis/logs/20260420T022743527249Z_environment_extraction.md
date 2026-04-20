# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T02:27:43.527249+00:00
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

Chapter id: CH012

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

Story: Carter is summoned by Lorquas Ptomel and accused of plotting an escape with Dejah Thoris ("red girl"). He faces a trial on return to Thark. Tars Tarkas offers him quarters in the building adjoining Sola's, explaining Thark retinue customs and distributing loot (weapons, silks, food). Carter selects a room on the third floor near Dejah Thoris's apartment to establish communication.

Visual: Audience chamber interior -> Plaza exterior -> Winding corridor -> Upper floors overlooking moss-covered court with fountains/statuary -> Back rooms receiving loads of weapons/silks/furs/cooking utensils.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Thark Environment Index

## Primary Settings
- audience_chamber_interior - Trial and summoning location
- back_rooms_quarters - Storage and living quarters for retinue

## Transit Settings
- plaza_exterior - Open public space between buildings
- winding_corridor - Internal passage connecting floors
- upper_floors_overlooking_moss_court - Elevated viewing area with fountains/statuary

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: audience_chamber_interior

[[SECTION markdown]]
# Audience Chamber Interior

## Environment Role
Primary setting for trial and summoning sequences

## Architecture or Geography
Formal interior space within Thark building, designed for official proceedings with elevated seating areas and central focal point for speaker positioning

## Lighting and Atmosphere Cues
Dim ambient lighting with focused illumination on central platform, creating dramatic shadows along walls and floor. Stone surfaces reflect minimal light, maintaining serious tone throughout chamber

## Scale Cues and Recurring Environmental Anchors
High ceiling with decorative arches framing upper perimeter. Central raised dais serves as primary anchor point. Audience seating arranged in tiered rows along curved walls. Doorway entrance marked by heavy stone threshold

## Useful Descriptive Noun Phrases
- formal trial space
- elevated speaking platform
- tiered audience seating
- stone-walled chamber interior
- dramatic shadow play
- official proceedings room
- central focal point dais
- curved wall arrangement
- heavy stone threshold entrance
- dim ambient illumination

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: plaza_exterior

[[SECTION markdown]]
# Plaza Exterior

## Environment Role
Transit setting between buildings and public gathering space

## Architecture or Geography
Open-air exterior courtyard with paved ground surface, surrounded by building facades on multiple sides. Features open sky exposure with architectural elements framing perimeter boundaries

## Lighting and Atmosphere Cues
Natural daylight illumination with clear visibility across entire space. Open sky provides even lighting distribution. Ground surfaces show minimal shadow variation under direct sun exposure

## Scale Cues and Recurring Environmental Anchors
Large paved area spanning building-to-building distances. Building entrances serve as primary access points marked by doorways and arches. Ground level features provide orientation reference points throughout plaza expanse

## Useful Descriptive Noun Phrases
- open-air courtyard space
- paved ground surface
- building facade perimeter
- natural daylight illumination
- clear visibility area
- architectural framing elements
- public gathering location
- exterior transit zone
- multi-sided courtyard layout
- ground level orientation markers

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: winding_corridor

[[SECTION markdown]]
# Winding Corridor

## Environment Role
Transit setting connecting interior floors and spaces

## Architecture or Geography
Internal passage with curved or angled layout, featuring multiple directional turns. Enclosed space with walls on both sides creating defined pathway through building structure

## Lighting and Atmosphere Cues
Artificial lighting sources mounted along ceiling or wall surfaces providing consistent illumination throughout corridor length. Narrow space creates focused light patterns along floor and wall surfaces

## Scale Cues and Recurring Environmental Anchors
Continuous passage length with multiple directional turns. Doorways at intervals mark access points to adjacent rooms. Ceiling height maintains consistent proportions throughout winding path

## Useful Descriptive Noun Phrases
- internal passage way
- curved corridor layout
- enclosed pathway space
- artificial lighting sources
- multiple directional turns
- doorways at intervals
- consistent ceiling height
- defined pathway through structure
- interior transit zone
- wall-mounted illumination

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: upper_floors_overlooking_moss_court

[[SECTION markdown]]
# Upper Floors Overlooking Moss-Covered Court

## Environment Role
Viewing and transit setting with elevated perspective over courtyard area

## Architecture or Geography
Elevated interior space with large windows or openings providing view downward to moss-covered court below. Features fountains and statuary visible from upper vantage point within courtyard landscape

## Lighting and Atmosphere Cues
Natural light filtering through upper windows creating soft illumination patterns on interior surfaces. Moss-covered court below provides contrasting green tones against stone architecture. Fountains add subtle movement reflections in ambient light

## Scale Cues and Recurring Environmental Anchors
Elevated position overlooking entire courtyard expanse. Large window openings frame view of fountains and statuary below. Interior space maintains height proportion to provide clear downward perspective. Courtyard features serve as primary visual anchors from upper level

## Useful Descriptive Noun Phrases
- elevated viewing space
- large window openings
- moss-covered court view
- fountain landscape below
- statuary arrangement
- soft natural illumination
- interior courtyard perspective
- green stone contrast
- downward vantage point
- ambient movement reflections

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: back_rooms_quarters

[[SECTION markdown]]
# Back Rooms Quarters

## Environment Role
Secondary setting for storage and living quarters within Thark building

## Architecture or Geography
Interior rooms receiving and storing various goods including weapons, silks, furs, and cooking utensils. Features storage areas with organized shelving or hanging racks for different item categories

## Lighting and Atmosphere Cues
Functional lighting sufficient for inventory and movement tasks. Mixed light sources from windows and artificial fixtures create practical illumination throughout storage spaces. Various materials (metal weapons, fabric silks, fur pelts) reflect different light qualities

## Scale Cues and Recurring Environmental Anchors
Room dimensions accommodate multiple storage categories with designated zones for each item type. Shelving units and hanging racks serve as primary organizational anchors. Doorways provide access points to adjacent spaces within building structure

## Useful Descriptive Noun Phrases
- storage quarters interior
- weapons storage area
- silk fabric collection
- fur pelt display
- cooking utensil storage
- organized shelving units
- hanging rack systems
- functional lighting sources
- mixed material reflections
- designated item zones

[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
