# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T07:04:25.972266+00:00
- task: environment_extraction

## System Prompt
````text
You are FilmCreator's chapter analysis engine.
Return only FilmCreator packets with the requested sections and records.
Do not wrap the packet in code fences unless explicitly requested.
Do not produce JSON-only responses.
If a packet asks for markdown sections, emit the section name on its own line and wrap the body in [[SECTION ...]] ... [[/SECTION]].
Keep the response deterministic and grounded in the supplied chapter text.
````

## User Prompt
````text
Project slug: princess_of_mars_test

Chapter id: CH004

Task: extract environment families into an environment index plus one Markdown file per environment family.

Packet contract:
- task: environment_extraction
- version: 1
- first line: [[FILMCREATOR_PACKET]]
- last line: [[/FILMCREATOR_PACKET]]
- required sections: environment_index_markdown
- record type environment: fields=asset_id sections=markdown



Output format:

[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

...index markdown...

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: environment

asset_id: arizona_quartz_vein_location



[[SECTION markdown]]

# Arizona Quartz Vein Location

Short, grounded environment markdown.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]



Asset id rules:

- lowercase snake_case

- stable across later reruns

- emit one explicit environment record per meaningful location or setting family

- every environment record must have a FILMCREATOR_RECORD wrapper with type environment

- include stable environment families rather than every one-off mention

- prefer visible geography and atmosphere over literary abstraction



Each environment Markdown file should include:

- environment role such as primary, secondary, or transit setting

- architecture or geography

- lighting and atmosphere cues

- scale cues and recurring environmental anchors

- useful descriptive noun phrases for later render-facing prompt writing



Chapter summary:

# Chapter IV: A PRISONER Summary

## Setting
Carter and his escort, Tars Tarkas, travel approximately ten miles before reaching the foot of mountains. They traverse a narrow gorge and enter an open valley containing a low table land with an enormous ruined city. The buildings show signs of extreme antiquity, possibly belonging to a long-extinct race, as they are deserted and not greatly decayed.

## Characters
- **John Carter:** The human protagonist, currently a prisoner but attempting to gain favor through physical demonstration.
- **Tars Tarkas:** Vice-chieftain of the community, escort, statesman, and warrior. He explains the situation regarding Carter's capture.
- **Martians (Green Men):** Approximately nine hundred creatures camped in the city. They are naked except for ornaments, have large tusks, long legs, and vary in height (adult females 10-12 feet).
- **Sola:** A young female Martian about eight feet tall, light olive-green, belonging to Tars Tarkas' retinue. She takes Carter to his quarters.
- **Principal Chieftain:** Ruler of the community, seated on a rostrum during the assembly.

## Events
1.  **Arrival at City:** Carter and Tars Tarkas enter the city through a ruined roadway. They observe the Martians camped in the plaza and buildings.
2.  **Martian Culture:** The text details Martian life expectancy (average 300 years after maturity, up to 1000 without violence), their violent death causes (duels, war, hunting), and their voluntary pilgrimage down the river Iss at age 1000.
3.  **Audience Chamber:** Carter is lowered to the ground and brought before the chieftain. A greeting ceremony occurs where names are exchanged between Tars Tarkas and the chieftain.
4.  **Physical Struggles:** Carter attempts to walk but fails, skipping like a grasshopper and bruising himself. He fights a Martian guard after being forced to stand, winning applause for his ability to fight back.
5.  **Demonstration of "Sak":** The Martians demand Carter perform the jump ("sak"). He succeeds in clearing 150 feet and landing squarely.
6.  **Demanding Sustenance:** Hungry and thirsty, Carter ignores further commands to jump and instead signals for food/water. Tars Tarkas arranges for him to be taken by a young female (Sola).
7.  **Quarters:** Sola leads Carter to a spacious chamber decorated with murals and mosaics. She signals for a ten-legged creature to appear, which waddles in like an obedient puppy.

## Key Observations
- The Martians are initially hostile but show approval when Carter demonstrates strength or humor (smiling).
- The architecture suggests a civilization older than the current inhabitants.
- Carter's human physiology is a liability for Martian tasks but becomes an asset when he adapts to their expectations (jumping, fighting).
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

## mountain_foot_gorge_location
- Role: Transit Setting
- Geography: Narrow gorge traversed before reaching city
- Atmosphere: Mountainous, enclosed passage

## open_valley_ruined_city_location
- Role: Primary Setting
- Geography: Open valley with low table land
- Atmosphere: Ancient, deserted, enormous ruined city

## martian_plaza_building_complex
- Role: Primary Setting
- Geography: Plaza and buildings within ruined city
- Atmosphere: Camped Martians, extreme antiquity architecture

## chieftain_rostrum_audience_chamber
- Role: Primary Setting
- Geography: Rostrum seating area
- Atmosphere: Assembly hall, ceremonial space

## solas_quarters_mural_chamber
- Role: Secondary Setting
- Geography: Spacious chamber with murals and mosaics
- Atmosphere: Decorated, intimate quarters

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: mountain_foot_gorge_location



[[SECTION markdown]]

# Mountain Foot Gorge Location

Short, grounded environment markdown.

## Environment Role
Transit setting - narrow passage traversed before reaching the city

## Architecture or Geography
Narrow gorge carved through mountainous terrain, enclosed passage leading toward open valley

## Lighting and Atmosphere Cues
Mountain shadows, enclosed natural lighting, sense of approaching destination

## Scale Cues and Recurring Environmental Anchors
Mountain walls framing the path, distant city visible at gorge exit

## Descriptive Noun Phrases
Narrow mountain passage, gorge entrance, mountain foot approach, enclosed valley corridor

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: open_valley_ruined_city_location



[[SECTION markdown]]

# Open Valley Ruined City Location

Short, grounded environment markdown.

## Environment Role
Primary setting - main location where chapter events unfold

## Architecture or Geography
Open valley containing low table land with enormous ruined city, deserted buildings showing extreme antiquity

## Lighting and Atmosphere Cues
Natural daylight illuminating ancient structures, sense of abandonment, vast open space

## Scale Cues and Recurring Environmental Anchors
Enormous ruined city dominating the landscape, distant mountain ranges, plaza within city

## Descriptive Noun Phrases
Open valley floor, low table land, enormous ruined city, deserted ancient buildings, mountain foot approach

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: martian_plaza_building_complex



[[SECTION markdown]]

# Martian Plaza Building Complex

Short, grounded environment markdown.

## Environment Role
Primary setting - where Martians are camped and Carter is brought before chieftain

## Architecture or Geography
Plaza and buildings within ruined city, structures showing signs of extreme antiquity possibly belonging to long-extinct race

## Lighting and Atmosphere Cues
Natural daylight on ancient architecture, deserted atmosphere, sense of ancient civilization

## Scale Cues and Recurring Environmental Anchors
Ruined roadway entrance, plaza space with Martians camped, building facades showing age

## Descriptive Noun Phrases
Martian plaza, ruined city buildings, ancient architecture, deserted structures, mountain foot approach

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: chieftain_rostrum_audience_chamber



[[SECTION markdown]]

# Chieftain Rostrum Audience Chamber

Short, grounded environment markdown.

## Environment Role
Primary setting - ceremonial space where principal chieftain is seated during assembly

## Architecture or Geography
Rostrum seating area within audience chamber, formal assembly hall space

## Lighting and Atmosphere Cues
Ceremonial lighting, formal atmosphere, sense of authority and importance

## Scale Cues and Recurring Environmental Anchors
Principal chieftain's elevated position, rostrum structure, ceremonial gathering space

## Descriptive Noun Phrases
Chieftain rostrum, audience chamber, assembly hall, ceremonial seating area, principal ruler's throne

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: solas_quarters_mural_chamber



[[SECTION markdown]]

# Sola's Quarters Mural Chamber

Short, grounded environment markdown.

## Environment Role
Secondary setting - intimate quarters where Carter is taken by Sola

## Architecture or Geography
Spacious chamber decorated with murals and mosaics, ten-legged creature appears like obedient puppy

## Lighting and Atmosphere Cues
Intimate lighting, decorative atmosphere, sense of personal space within ancient city

## Scale Cues and Recurring Environmental Anchors
Mural decorations covering walls, mosaic floor patterns, spacious interior dimensions

## Descriptive Noun Phrases
Spacious chamber, mural decorations, mosaic flooring, decorated quarters, intimate ancient room

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
