# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T07:56:24.666070+00:00
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

- include stable environment families rather than every one-off mention

- prefer visible geography and atmosphere over literary abstraction



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
- Role: Primary setting (initial capture location)
- Architecture: Interior chamber with sleeping silks and furs
- Lighting: Dim, intimate illumination
- Atmosphere: Captive confinement, therapeutic care

## Warhoon Camp
- Role: Transit setting (night stop for main column)
- Architecture: Open-air warrior encampment
- Lighting: Nighttime, campfire glow
- Atmosphere: Active military presence, pursuit underway

## Dark Dungeon in City of Warhoon
- Role: Primary setting (imprisonment and escape)
- Architecture: Underground cell with chains
- Lighting: Darkness, creeping shadows
- Atmosphere: Horror, unseen threats, fiery eyes

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: small_room_sleeping_silks_furs



[[SECTION markdown]]

# Small Room with Sleeping Silks and Furs

Short, grounded environment markdown.

Role: Primary setting (initial capture location)
Architecture: Interior chamber with sleeping silks and furs
Lighting: Dim, intimate illumination
Atmosphere: Captive confinement, therapeutic care
Scale cues: Confined personal space
Environmental anchors: Sleeping silks, furs, healing instruments

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: warhoon_camp



[[SECTION markdown]]

# Warhoon Camp

Short, grounded environment markdown.

Role: Transit setting (night stop for main column)
Architecture: Open-air warrior encampment
Lighting: Nighttime, campfire glow
Atmosphere: Active military presence, pursuit underway
Scale cues: Large horde of warriors
Environmental anchors: Tents, fire pits, mounted warriors

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: dark_dungeon_city_warhoon



[[SECTION markdown]]

# Dark Dungeon in City of Warhoon

Short, grounded environment markdown.

Role: Primary setting (imprisonment and escape)
Architecture: Underground cell with chains
Lighting: Darkness, creeping shadows
Atmosphere: Horror, unseen threats, fiery eyes
Scale cues: Deep underground confinement
Environmental anchors: Chains, floor, walls, creeping things, fiery eyes

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

Asset id rules:

- lowercase snake_case

- stable across later reruns

- emit one explicit environment record per meaningful location or setting family

- every environment record must have a FILMCREATOR_RECORD wrapper with type environment

- include stable environment families rather than every one-off mention

- prefer visible geography and atmosphere over literary abstraction
````
