# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T07:56:53.229730+00:00
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

Chapter id: CH018

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

- keep the environment set small and useful

- use concise visible descriptions



Each environment Markdown file should include:

- environment role such as primary, secondary, or transit setting

- architecture or geography

- lighting and atmosphere cues

- scale cues and recurring environmental anchors

- useful descriptive noun phrases for later render-facing prompt writing



Chapter summary:

# Chapter 18 Summary: CHAINED IN WARHOON

## Major Events
- Narrator regains consciousness after capture, discovering he is alive among Warhoon warriors
- Dak Kova (the jed who captured him) reveals plans to use narrator as sport for the great games
- Narrator is strapped to a wild thoat and pursued after the main column toward Warhoon
- Upon reaching Warhoon camp, narrator is taken before Bar Comas, young jeddak of Warhoon
- Dak Kova displays insubordination toward Bar Comas, leading to brutal hand-to-hand combat
- Bar Comas wins but is killed by Dak Kova, who then assumes title of Jeddak of Warhoon
- Expedition abandoned until after great games; ten thousand warriors turn back toward Warhoon
- Narrator imprisoned in dark dungeon, chained to floor and walls for indeterminate period
- Narrator kills his jailer with a chain, retrieves keys from dead man's neck
- Six pairs of eyes watch narrator retreat into darkness as he gains freedom

## Characters Introduced
- **Dak Kova**: The jed who captured the narrator, now Jeddak of Warhoon after killing Bar Comas
- **Bar Comas**: Young jeddak of Warhoon, killed by Dak Kova in a brutal fight
- **Ancient Female Warrior**: Attends to narrator's wounds, reveals therapeutic skills
- **Narrator**: Captured outsider experiencing captivity and eventual escape

## Settings
- Small room with sleeping silks and furs (initial capture location)
- Warhoon camp where main column makes night stop
- Dark dungeon in city of Warhoon, filled with creeping things and fiery eyes

## Key Themes
- Brutality of Warhoon culture (more ferocious than Tharks despite smaller horde)
- Power struggles within warrior societies
- Narrator's resilience and cunning in captivity
- Horror of darkness and unseen threats
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

## Small Room with Sleeping Silks and Furs
- Initial capture location where narrator regains consciousness
- Intimate, enclosed space with soft furnishings

## Warhoon Camp
- Night stop location for the main column
- Open-air warrior encampment setting

## Dark Dungeon in City of Warhoon
- Imprisonment cell within Warhoon city
- Horror-filled underground space with creeping threats

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: small_room_capture_location



[[SECTION markdown]]

# Small Room Capture Location

Short, grounded environment markdown.

## Environment Role
Primary setting for initial capture and awakening sequence.

## Architecture or Geography
Small enclosed room with sleeping silks and furs lining the space. Soft furnishings create intimate atmosphere despite captivity context.

## Lighting and Atmosphere Cues
Dim, subdued lighting suggesting interior chamber. Quiet, still air with therapeutic presence from ancient female warrior attending to wounds.

## Scale Cues and Recurring Environmental Anchors
Personal scale room - narrator can move freely but remains confined. Sleeping silks and furs serve as primary visual anchors within the space.

## Descriptive Noun Phrases for Render-Facing Prompt Writing
Sleeping silks, soft furs, intimate chamber, therapeutic presence, wounded captive, enclosed interior, quiet atmosphere, personal scale room

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: warhoon_camp_location



[[SECTION markdown]]

# Warhoon Camp Location

Short, grounded environment markdown.

## Environment Role
Secondary setting for main column night stop and transition point.

## Architecture or Geography
Open-air warrior encampment with temporary structures. Large-scale outdoor space accommodating ten thousand warriors during great games period.

## Lighting and Atmosphere Cues
Night-time illumination from campfires and torches. Active, bustling atmosphere with warriors preparing for departure toward Warhoon city.

## Scale Cues and Recurring Environmental Anchors
Campfire clusters serve as primary lighting anchors. Main column formation provides scale reference point within the larger encampment space.

## Descriptive Noun Phrases for Render-Facing Prompt Writing
Warrior encampment, campfire clusters, torch-lit night, main column formation, open-air setting, temporary structures, bustling atmosphere, departure preparation

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: dark_dungeon_warhoon_city



[[SECTION markdown]]

# Dark Dungeon Warhoon City

Short, grounded environment markdown.

## Environment Role
Primary setting for imprisonment and escape sequence within city of Warhoon.

## Architecture or Geography
Underground dungeon cell with chains attached to floor and walls. Creeping things and fiery eyes populate the darkness beyond immediate cell space.

## Lighting and Atmosphere Cues
Pitch-black interior with only chain reflections visible. Horror-filled atmosphere with unseen threats lurking in shadows. Fiery eyes provide ominous illumination from beyond cell boundaries.

## Scale Cues and Recurring Environmental Anchors
Chains serve as primary environmental anchors - attached to floor, walls, and narrator's body. Darkness itself functions as scale-defying anchor creating disorienting spatial experience.

## Descriptive Noun Phrases for Render-Facing Prompt Writing
Dark dungeon cell, chains attached to floor, chains attached to walls, creeping things, fiery eyes, pitch-black interior, horror-filled atmosphere, unseen threats, underground prison, chain reflections

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: warhoon_city_interior



[[SECTION markdown]]

# Warhoon City Interior

Short, grounded environment markdown.

## Environment Role
Transit setting connecting dungeon imprisonment to city escape sequence.

## Architecture or Geography
City interior spaces beyond immediate dungeon cell. Urban environment with multiple chambers and corridors leading toward freedom.

## Lighting and Atmosphere Cues
Dim urban lighting with shadows creating depth. Transition from darkness of dungeon to broader city illumination as narrator gains keys and moves through space.

## Scale Cues and Recurring Environmental Anchors
Six pairs of eyes serve as primary visual anchors watching narrator's retreat into darkness. City corridors provide scale reference for movement toward freedom.

## Descriptive Noun Phrases for Render-Facing Prompt Writing
City interior spaces, urban corridors, six pairs of eyes, transition lighting, shadow depth, broader city illumination, movement through space, corridor navigation, urban environment

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_PACKET]]
````
