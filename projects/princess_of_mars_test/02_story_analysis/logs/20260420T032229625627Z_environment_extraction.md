# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T03:22:29.625627+00:00
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

Chapter id: CH001

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

Visual Continuity: Arizona hills, clear mornings, moonlight, horse/burro tracks, Apache tepees, cave chamber with smooth floor and shadowed back.

Story Summary: March 3, 1866. Powell departs to buy mining equipment. Carter follows his trail after discovering signs of an Apache ambush at a water hole. He finds Powell dead in the cave. Carter enters the cave, lays Powell down, and succumbs to drowsiness/exhaustion on the floor.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - March 3, 1866

## Arizona Hills (arizona_hills)
Primary setting for Powell's departure and Carter's trail following. Clear morning lighting with moonlight presence. Horse and burro tracks visible across terrain.

## Apache Tepees (apache_tepees)
Secondary environment representing Apache structures. Transitional space between wilderness and settlement.

## Cave Chamber (cave_chamber)
Critical location where Powell is found dead. Smooth floor surface with shadowed back wall. Interior chamber space for final scene.

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: arizona_hills

[[SECTION markdown]]
# Arizona Hills

## Environment Role
Primary setting - main wilderness location where trail following occurs

## Architecture and Geography
Open desert terrain with rolling hills. Natural landscape without man-made structures. Wide expanse allowing for tracking movement across ground.

## Lighting and Atmosphere
Clear morning light transitioning to moonlight presence. Bright visibility during day hours. Atmospheric clarity typical of high desert conditions.

## Scale and Anchors
Large scale environment spanning multiple miles. Horse tracks and burro tracks serve as recurring environmental anchors marking passage through terrain.

## Descriptive Noun Phrases
- Desert rolling hills
- Clear morning light
- Moonlit wilderness
- Animal track paths
- Open terrain expanse

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: apache_tepees

[[SECTION markdown]]
# Apache Tepees

## Environment Role
Secondary setting - transitional space between wilderness and settlement

## Architecture and Geography
Traditional Apache structures made from natural materials. Conical shelter forms with open framework. Settlement-style arrangement of multiple tepee units.

## Lighting and Atmosphere
Natural daylight filtering through structure openings. Interior shadows created by conical roof design. Warm ambient lighting typical of enclosed spaces.

## Scale and Anchors
Medium scale environment within settlement area. Tepee frames and entranceways serve as recurring environmental anchors for movement between structures.

## Descriptive Noun Phrases
- Conical Apache shelters
- Natural material construction
- Settlement arrangement
- Open framework structures
- Interior shadowed spaces

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: cave_chamber

[[SECTION markdown]]
# Cave Chamber

## Environment Role
Critical location - interior chamber where final scene occurs

## Architecture and Geography
Natural rock formation creating enclosed interior space. Smooth floor surface with distinct shadowed back wall. Interior chamber dimensions suitable for body placement.

## Lighting and Atmosphere
Limited natural light entering through cave openings. Shadowed back wall creates depth perception. Dim interior lighting typical of underground spaces.

## Scale and Anchors
Small to medium scale interior environment. Floor surface and back wall serve as recurring environmental anchors for character positioning and scene composition.

## Descriptive Noun Phrases
- Smooth floor surface
- Shadowed back wall
- Interior rock chamber
- Underground enclosure
- Dim natural lighting

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
