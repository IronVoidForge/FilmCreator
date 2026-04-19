# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T22:13:02.435722+00:00
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

## Story Summary (CH001)

- **Opening:** Carter reflects on his agelessness and fear of death despite having died twice. He decides to write a chronicle of his life and death.
- **Backstory:** Post-Civil War veteran with Confederate funds. Carter and Powell locate a gold vein in Arizona winter 1865.
- **Inciting Incident:** Powell leaves to buy machinery; Carter guards the claim.
- **Rising Action:** Powell's party is ambushed by Apaches. Carter discovers tracks of pursuing horsemen.
- **Climax:** Carter chases the attackers. Finds Powell dead on a plateau surrounded by tepees.
- **Falling Action:** Carter shoots at warriors, escapes pursuit into a defile leading to a cave.
- **Resolution:** Enters cave entrance. Collapses from fatigue and excitement.

## Visual Continuity Facts (CH001)

- **Environment:** Arizona hills, clear mornings, moonlight nights. Terrain includes mountainside, valley, plateau, gorge, pass.
- **Lighting:** Moonlight scenes during chase; daylight at cave entry.
- **Tracks:** Powell's tracks vs. Apache pony tracks (unshod ponies).
- **Camp:** White with Indian tepees; half a thousand warriors clustered around center object.
- **Cave Interior:** Large chamber (~100ft diameter, 30-40ft height), smooth floor, dense shadow at back.
- **Weapons:** Colt revolvers (two), carbine, cartridge belts.
- **Mounts:** Saddle horse (poor beast), burros (Powell's).
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - CH001

## arizona_hills_mountainside
Primary setting. Arizona hills with mountainside terrain, clear morning light, moonlight nights. Mountains and valleys visible.

## valley_plateau_gorge
Transit settings. Valley floor, plateau surface, gorge passage. Terrain varies between open and enclosed spaces.

## cave_interior
Secondary setting. Large chamber approximately 100ft diameter, 30-40ft height. Smooth floor, dense shadow at back wall.

## camp_tepees
Secondary scene environment. White camp with Indian tepees, half a thousand warriors clustered around center object. Open terrain surrounding camp.

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: arizona_hills_mountainside

[[SECTION markdown]]
# Arizona Hills & Mountainside

## Environment Role
Primary setting for Carter's chronicle and chase sequences.

## Architecture or Geography
Rugged Arizona hills with mountainside terrain. Open valleys visible between peaks. Natural formations create multiple elevation levels.

## Lighting and Atmosphere Cues
Clear mornings with bright daylight. Moonlight nights during chase sequences. High contrast between illuminated slopes and shadowed valleys. Winter 1865 atmosphere with crisp air.

## Scale Cues and Recurring Environmental Anchors
Mountain peaks serve as distant landmarks. Valley floors provide open spaces for movement. Elevation changes create natural barriers and passages. Ridge lines form visual horizons.

## Descriptive Noun Phrases
- Arizona hills
- Mountainside terrain  
- Clear morning light
- Moonlight nights
- Open valleys
- Natural formations
- Elevated peaks
- Shadowed slopes
- Winter atmosphere
- Crisp mountain air

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: valley_plateau_gorge

[[SECTION markdown]]
# Valley, Plateau & Gorge

## Environment Role
Transit settings for Carter's movement between locations.

## Architecture or Geography
Valley floor with open terrain. Plateau surface providing elevated ground. Gorge passage creating enclosed route through mountains. Natural terrain variations between open and confined spaces.

## Lighting and Atmosphere Cues
Daylight during valley crossing. Moonlight during plateau chase sequences. Enclosed gorge creates darker conditions with limited light penetration. Terrain shadows vary by time of day.

## Scale Cues and Recurring Environmental Anchors
Valley width determines movement space. Plateau elevation provides vantage points. Gorge depth creates natural barriers. Mountain walls frame passage routes. Horizon visibility changes between valley and plateau.

## Descriptive Noun Phrases
- Valley floor
- Open terrain
- Plateau surface
- Elevated ground
- Gorge passage
- Enclosed route
- Natural barriers
- Mountain walls
- Vantage points
- Passage routes

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: cave_interior

[[SECTION markdown]]
# Cave Interior

## Environment Role
Secondary setting for Carter's final resting place and discovery.

## Architecture or Geography
Large chamber approximately 100ft diameter, 30-40ft height. Smooth floor surface throughout. Dense shadow at back wall creating depth. Natural rock formations define chamber boundaries. Entrance leads from defile outside.

## Lighting and Atmosphere Cues
Daylight at cave entrance transitioning to interior shadows. Dense shadow at back wall creates mysterious atmosphere. Limited light penetration from entrance illuminates front of chamber. Interior remains dimly lit with natural ambient light.

## Scale Cues and Recurring Environmental Anchors
Chamber diameter provides spatial reference for movement. Height determines standing clearance. Entrance width marks transition point. Back wall shadow serves as visual anchor. Floor smoothness indicates natural formation.

## Descriptive Noun Phrases
- Large chamber
- One hundred foot diameter
- Thirty to forty foot height
- Smooth floor surface
- Dense shadow
- Back wall
- Natural rock formations
- Cave entrance
- Interior shadows
- Dimly lit space

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: camp_tepees

[[SECTION markdown]]
# Camp with Tepees

## Environment Role
Secondary scene environment for Carter's discovery of Powell's death.

## Architecture or Geography
White camp with Indian tepees arranged around center object. Half a thousand warriors clustered in open terrain surrounding camp. Tepee structures create circular arrangement. Open ground provides movement space between structures.

## Lighting and Atmosphere Cues
Daylight conditions during scene. Moonlight visible on surrounding hills. Camp interior shadows under tepees. Warriors gathered creating human-scale density against landscape scale. Clear morning or evening light based on narrative timing.

## Scale Cues and Recurring Environmental Anchors
Tepee cluster defines camp boundaries. Center object serves as focal point. Warrior cluster creates human mass reference. Open terrain surrounding camp provides spatial context. Mountain hills visible in background establish location.

## Descriptive Noun Phrases
- White camp
- Indian tepees
- Center object
- Warrior cluster
- Half a thousand warriors
- Tepee structures
- Circular arrangement
- Open ground
- Surrounding terrain
- Background hills

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
