# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T07:40:11.203332+00:00
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

Chapter id: CH014

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

John Carter reflects on his love for Dejah Thoris as they prepare to travel from Korad to Thark. Dejah is chained by Sarkoja's order to ensure security during the journey. Tars Tarkas intervenes, taking custody of the key and promising to protect her from Sarkoja's harassment. During the march, John Carter engages in a duel with Zad, a warrior who struck his animal. The fight is interrupted when Dejah Thoris throws a mirror that blinds Zad, allowing him to strike John in the shoulder. Sarkoja attempts to stab Dejah Thoris, but Sola intercepts. The chapter culminates in a fierce sword fight where John Carter is stabbed in the chest and collapses, ending on a cliffhanger of his potential death or unconsciousness.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

## The March/Journey Route

- **Role:** Primary setting for action sequences
- **Geography:** Open terrain between Korad and Thark
- **Atmosphere:** Tense, dangerous journey environment
- **Scale:** Extended march route with multiple encounter points
- **Anchors:** Chained Dejah Thoris, Sarkoja's presence, Zad warrior

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: environment

asset_id: march_journey_route_location



[[SECTION markdown]]

# March/Journey Route Location

## Environment Role
Primary setting for action sequences during the dangerous journey from Korad to Thark.

## Architecture and Geography
Open terrain route connecting Korad and Thark, featuring extended march path with multiple encounter points along the way. The environment supports both foot travel and combat engagement across the landscape.

## Lighting and Atmosphere
Tense, dangerous atmosphere throughout the march. Lighting conditions vary across the open terrain, creating shadows and visibility challenges during combat sequences. The journey route carries an underlying sense of urgency and peril as characters move between settlements.

## Scale Cues and Environmental Anchors
Extended march route with multiple encounter points:
- Chained Dejah Thoris serves as a central anchor point throughout the journey
- Sarkoja's presence marks dangerous zones along the route
- Zad warrior encounter occurs at specific terrain features during the march
- Sword fight climax takes place in open combat area of the journey path

## Descriptive Noun Phrases for Render-Facing Prompts
- Dangerous journey route between settlements
- Open terrain march path with combat engagement points
- Tense atmosphere along extended travel corridor
- Multiple encounter zones across landscape
- Chained prisoner anchor point on journey route
- Combat-ready open terrain environment
- Perilous march through hostile territory

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: environment

asset_id: korad_destination_location



[[SECTION markdown]]

# Korad Destination Location

## Environment Role
Secondary setting - starting point of the journey from Korad to Thark.

## Architecture and Geography
Settlement location serving as departure point for the dangerous march route. Features infrastructure supporting travel preparation and character interactions before departure.

## Lighting and Atmosphere
Preparation atmosphere with underlying tension regarding Dejah Thoris's chained status and Sarkoja's orders. Settlement environment carries weight of impending dangerous journey.

## Scale Cues and Environmental Anchors
- Travel preparation zone for John Carter and Dejah Thoris
- Departure point marking beginning of march route
- Location where journey preparations occur before dangerous travel begins

## Descriptive Noun Phrases for Render-Facing Prompts
- Settlement departure location
- Journey preparation environment
- Starting point of dangerous march route
- Pre-departure settlement infrastructure
- Character interaction zone before journey begins

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: environment

asset_id: thark_destination_location



[[SECTION markdown]]

# Thark Destination Location

## Environment Role
Secondary setting - ultimate destination of the journey from Korad to Thark.

## Architecture and Geography
Settlement location serving as final destination of the dangerous march route. Features infrastructure supporting arrival and character interactions after the perilous journey.

## Lighting and Atmosphere
Arrival atmosphere following the dangerous journey. Settlement environment carries weight of completed travel and potential consequences of the march's events.

## Scale Cues and Environmental Anchors
- Journey completion point for march route
- Final destination marking end of dangerous travel
- Arrival zone for characters after perilous journey

## Descriptive Noun Phrases for Render-Facing Prompts
- Settlement arrival location
- Journey completion environment
- Final destination of dangerous march route
- Post-journey settlement infrastructure
- Character interaction zone after travel concludes

[[/SECTION]]



Asset id rules:

- lowercase snake_case
- stable across later reruns
- emit one explicit environment record per meaningful location or setting family
- every environment record must have a FILMCREATOR_RECORD wrapper with type environment
- include stable environment families rather than every one-off mention
- prefer visible geography and atmosphere over literary abstraction
````
