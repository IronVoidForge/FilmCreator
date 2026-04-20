# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T07:11:05.482710+00:00
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

Chapter id: CH007

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

Chapter VII details the community's child-raising ceremony on Mars. The narrator is escorted by Sola to an incubator where young Martians are hatched after five years of incubation. A gauntlet ceremony releases them into the community, with women and children capturing them for communal upbringing. The chapter explains the harsh Martian social system regarding offspring selection, survival, and the lack of parental bonds. Following the event, the narrator trains with Sola, learning the simple Martian language and developing one-way telepathic communication that provides an advantage over local inhabitants.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index - Mars Child-Raising Ceremony

## Incubator
- Role: Primary setting for hatching ceremony
- Architecture: Controlled climate chamber with observation windows
- Lighting: Soft, warm ambient glow from incubation systems
- Atmosphere: Sterile yet nurturing, five-year growth cycle evident
- Scale: Large enough to house multiple young Martians simultaneously

## Gauntlet Release Area
- Role: Transit setting for community integration
- Architecture: Open ceremonial space with gathering platforms
- Lighting: Bright daylight transitioning to evening shadows
- Atmosphere: Tense excitement, communal energy building
- Scale: Community-wide gathering capacity, women and children present

## Training Ground
- Role: Secondary setting for narrator development
- Architecture: Simple outdoor or controlled practice area
- Lighting: Natural light with telepathic communication cues
- Atmosphere: Focused learning environment, simple Martian language acquisition
- Scale: Personal to small group training space

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: incubator_chamber_location



[[SECTION markdown]]

# Incubator Chamber Location

Short, grounded environment markdown.

## Environment Role
Primary setting for the hatching ceremony where young Martians emerge after five years of incubation.

## Architecture
Controlled climate chamber with observation windows allowing community viewing during the release event.

## Lighting and Atmosphere
Soft, warm ambient glow from incubation systems creating a sterile yet nurturing environment. The atmosphere reflects the harsh Martian social system regarding offspring selection and survival.

## Scale Cues
Large enough to house multiple young Martians simultaneously, with space for ceremonial gathering around observation points.

## Environmental Anchors
Incubation growth cycle markers, release mechanism interface, community viewing platforms.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: gauntlet_release_area_location



[[SECTION markdown]]

# Gauntlet Release Area Location

Short, grounded environment markdown.

## Environment Role
Transit setting for the gauntlet ceremony where young Martians are released into the community for communal upbringing.

## Architecture
Open ceremonial space with gathering platforms designed for women and children to capture emerging young Martians.

## Lighting and Atmosphere
Bright daylight transitioning to evening shadows during the release event. Tense excitement builds as the harsh Martian social system regarding offspring selection becomes evident.

## Scale Cues
Community-wide gathering capacity, with space for multiple women and children participating in the capture ritual.

## Environmental Anchors
Ceremonial platforms, capture zones, community viewing areas, release mechanism interface.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: training_ground_location



[[SECTION markdown]]

# Training Ground Location

Short, grounded environment markdown.

## Environment Role
Secondary setting for narrator development following the hatching ceremony event.

## Architecture
Simple practice area where narrator trains with Sola, learning the simple Martian language and developing one-way telepathic communication.

## Lighting and Atmosphere
Natural light with telepathic communication cues providing advantage over local inhabitants. Focused learning environment reflecting the narrator's development.

## Scale Cues
Personal to small group training space, accommodating narrator and Sola for instruction sessions.

## Environmental Anchors
Training equipment, language acquisition markers, telepathic communication interface points.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: mars_community_gathering_space_location



[[SECTION markdown]]

# Mars Community Gathering Space Location

Short, grounded environment markdown.

## Environment Role
Primary setting for the broader community context during the child-raising ceremony event.

## Architecture
Large communal space where women and children gather to participate in capturing young Martians after release from incubation.

## Lighting and Atmosphere
Bright daylight with evening shadows as the ceremony progresses. Communal energy builds reflecting the harsh Martian social system regarding offspring selection and survival.

## Scale Cues
Community-wide gathering capacity, accommodating multiple participants in the capture ritual for communal upbringing.

## Environmental Anchors
Gathering platforms, capture zones, community viewing areas, ceremonial markers.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: incubator_observation_deck_location



[[SECTION markdown]]

# Incubator Observation Deck Location

Short, grounded environment markdown.

## Environment Role
Secondary setting for community viewing during the hatching ceremony event.

## Architecture
Observation deck with windows overlooking the incubation chamber where young Martians are hatched after five years of incubation.

## Lighting and Atmosphere
Soft, warm ambient glow from incubation systems visible through observation windows. Sterile yet nurturing atmosphere evident to viewers.

## Scale Cues
Large enough for multiple community members to observe the release event simultaneously.

## Environmental Anchors
Observation windows, growth cycle markers, release mechanism interface, viewing platforms.

[[/SECTION]]

[[FILMCREATOR_PACKET]]
````
