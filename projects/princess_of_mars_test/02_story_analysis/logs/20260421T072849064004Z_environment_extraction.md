# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T07:28:49.064004+00:00
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

Chapter id: CH019

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

**Setting:** A subterranean amphitheater within a ruined, ancient city inhabited by the Warhoon horde; later, the hills east of the city.

**Characters:**
- **John Carter:** A prisoner of the Warhoons, fighting for survival in the arena.
- **Kantos Kan:** A padwar (lieutenant) from Helium and a fellow prisoner; he provides intelligence on the search for Dejah Thoris.
- **Dak Kova:** The leader of the Warhoon horde, presiding over the games.
- **Warhoon Horde:** A bloodthirsty green Martian community hosting gladiatorial games.

**Events:**
- **Loss of Keys:** John Carter realizes his jailer's keys have been stolen by creatures in the darkness.
- **Meeting Kantos Kan:** Carter meets a fellow prisoner, Kantos Kan, who reveals that Helium has launched massive fleets to find Dejah Thoris and explains how he was captured while scouting the Warhoon city.
- **The Arena Games:** The prisoners are taken to an immense, excavated amphitheater for a ten-day tournament where only one survivor is granted freedom. Carter witnesses brutal contests between women and beasts.
- **Combat Success:** Carter dominates his matches using his superior strength and agility, eventually becoming one of the final three combatants alongside Kantos Kan and a massive northern green warrior.
- **The Final Duel:** Kantos Kan uses a specialized Martian swordsmanship technique to kill the giant warrior. 
- **The Escape Plan:** To avoid killing each other, Carter and Kantos Kan stage a fake death. Kantos Kan appears to deliver a fatal blow to Carter, but the blade misses vital organs. Kantos Kan claims his freedom, while Carter uses the cover of darkness to escape the arena and head toward the eastern hills.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [warhoon_subterranean_amphitheater](warhoon_subterranean_amphitheater)
- [eastern_martian_hills](eastern_martian_hills)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: warhoon_subterranean_amphitheater

[[SECTION markdown]]

# Warhoon Subterranean Amphitheater

**Role:** Primary setting (Arena/Combat zone)

**Architecture & Geography:** A massive, excavated subterranean amphitheater carved into the Martian crust. Features a central combat floor surrounded by tiered seating or viewing areas for the Warhoon horde. The structure is part of an ancient, ruined city.

**Lighting & Atmosphere:** Harsh, dramatic lighting typical of gladiatorial arenas; shadows cast by the surrounding rock walls and the presence of darkness in the peripheral tunnels/cells. Atmospheric tension driven by the roar of a bloodthirsty crowd.

**Scale & Anchors:** Immense scale capable of holding thousands of spectators; central combat pit serves as the recurring anchor for action sequences.

**Prompt Phrases:** excavated stone amphitheater, ancient ruined Martian city, subterranean arena, tiered rock seating, gladiatorial combat pit, cavernous hollow, shadows and torchlight.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: eastern_martian_hills

[[SECTION markdown]]

# Eastern Martian Hills

**Role:** Secondary setting (Transit/Escape zone)

**Architecture & Geography:** Rolling, rugged hills located east of the Warhoon city. Characterized by uneven terrain and natural geological formations.

**Lighting & Atmosphere:** Open-air lighting; likely transitioning from the darkness of the arena escape to the natural Martian sky. Atmospheric sense of isolation and movement.

**Scale & Anchors:** Expansive landscape; horizon lines and undulating hilltops serve as visual anchors.

**Prompt Phrases:** rugged martian hills, rolling rocky terrain, eastern wasteland, desolate highlands, vast martian landscape, uneven earth.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
