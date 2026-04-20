# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T18:21:17.557608+00:00
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

Chapter id: CH024

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

While flying over an ancient dead city, John Carter's craft is shot down during a massive battle between thousands of green warriors. After crashing into the combat, Carter intervenes to save Tars Tarkas from being killed by three Warhoons, and the two fight side-by-side until the enemy retreats. Upon returning to Thark, Carter is reunited with Woola, but faces immediate political peril when the jeddak, Tal Hajus, orders him to be brought before the council for punishment. After a brief encounter with Sarkoja, Carter is brought to the palace where Tal Hajus reacts with rage and orders his torture.

Carter successfully appeals to the Thark council, challenging Tal Hajus's legitimacy by accusing him of cowardice and proposing Tars Tarkas as a superior leader. Following a duel in which Tars Tarkas kills the jeddak, Tars Tarkas is proclaimed the new jeddak and Carter is elevated to the rank of chieftain. To capitalize on the warriors' desire for plunder, Carter proposes an alliance to rescue Princess Dejah Thoris from Zodanga. Tars Tarkas assembles a massive expeditionary force of 150,000 Tharks, which marches under the cover of night to reach the walls of Zodanga. Once there, Carter leads an infiltration team that scales the city's carborundum walls. Having secured knowledge on how to open the gates, Carter coordinates a plan to seize the great gates while leading a detachment toward the palace to strike at the heart of the city.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [ancient_dead_city_battlefield](ancient_dead_city_battlefield)
- [thark_palace_council_chamber](thark_palace_council_chamber)
- [zodanga_walls](zodanga_walls)
- [zodanga_palace_interior](zodanga_palace_interior)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: ancient_dead_city_battlefield

[[SECTION markdown]]

# Ancient Dead City Battlefield

**Role:** Primary / Combat Setting

**Geography:** Ruins of an ancient, sprawling dead city; debris-strewn terrain littered with the wreckage of fallen crafts and thousands of combatants.

**Lighting & Atmosphere:** Chaotic, dust-filled air; flashes of combat; high-intensity battle atmosphere.

**Scale & Anchors:** Massive scale involving thousands of green warriors; ruins serving as vertical obstacles and cover.

**Prompt Phrases:** ancient ruined city, battlefield debris, war-torn landscape, massive scale combat, dusty atmosphere, fallen spacecraft wreckage.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: thark_palace_council_chamber

[[SECTION markdown]]

# Thark Palace Council Chamber

**Role:** Primary / Political Setting

**Geography:** Formal assembly hall within the Thark stronghold; structured for council proceedings and judicial duels.

**Lighting & Atmosphere:** Somber, high-tension, authoritative; heavy atmosphere of political peril and judgment.

**Scale & Anchors:** Large enough to accommodate the Thark council; central area for dueling and formal proclamations.

**Prompt Phrases:** martial palace hall, council chamber, stone assembly room, tense political setting, ceremonial combat arena.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: zodanga_walls

[[SECTION markdown]]

# Zodanga Walls

**Role:** Transit / Infiltration Setting

**Geography:** Massive, imposing defensive fortifications; carborundum-based construction.

**Lighting & Atmosphere:** Nighttime setting; shadows and moonlight; high-stakes stealth atmosphere.

**Scale & Anchors:** Immense vertical scale; sheer carborundum surfaces; massive gates at the base.

**Prompt Phrases:** colossal city walls, carborundum fortifications, night infiltration, massive defensive ramparts, steep scaling surfaces.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: zodanga_palace_interior

[[SECTION markdown]]

# Zodanga Palace Interior

**Role:** Primary / Objective Setting

**Geography:** The central seat of power within the city of Zodanga; high-value target for infiltration.

**Lighting & Atmosphere:** Grand, fortified, interior palace lighting; high-tension combat environment during siege.

**Scale & Anchors:** Large scale halls; heart of the city; architectural center of Zodanga.

**Prompt Phrases:** grand palace interior, urban citadel, fortified central hall, siege target, opulent martial architecture.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
