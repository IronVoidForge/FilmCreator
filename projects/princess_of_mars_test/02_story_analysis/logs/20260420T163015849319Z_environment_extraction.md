# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T16:30:15.849319+00:00
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

Chapter id: CH001

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

### Summary
Following the end of the Civil War, Captain John Carter and Captain James K. Powell discover a massive gold vein in the Arizona mountains. When Powell leaves to secure mining machinery, Carter witnesses suspicious movement on the trail and suspects an Apache ambush. Driven by a sense of duty, Carter pursues the trail, discovers a large Apache camp, and launches a solo charge that scatters the warriors. However, the raid reveals that Powell has been killed by arrows. In a desperate attempt to escape the pursuing Apache party, Carter flees into the mountains, eventually stumbling upon a large, ancient cave. Upon entering the cave to scout, an inexplicable and overwhelming drowsiness overcomes him.

### Characters
* **John Carter (Captain Jack Carter):** A former Confederate cavalry captain and veteran of the Sioux wars; a man driven by duty who possesses mysterious knowledge regarding Mars.
* **Captain James K. Powell:** A mining engineer and Carter's partner in prospecting; killed during an Apache ambush.

### Settings
* **Arizona Mountains/Hills:** The rugged, desolate landscape where the gold mine is located and where the pursuit takes place.
* **The Apache Camp:** A large plateau filled with hundreds of tepees and warriors.
* **The Cave:** A large, ancient-looking chamber found at the end of a high cliff trail, characterized by a smooth floor and mysterious shadows.

### Key Events
* **The Discovery:** Carter and Powell locate a million-dollar gold vein in 1865.
* **The Ambush:** Carter observes suspicious tracks and pursues what he believes is an attack on Powell.
* **The Charge:** Carter singlehandedly attacks the Apache camp, causing a rout.
* **The Death of Powell:** Carter finds his friend dead from arrow wounds.
* **The Flight and the Cave:** While fleeing pursuit, Carter enters a mysterious cave and falls into a sudden, deep sleep.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [arizona_mountains_hills](#arizona_mountains_hills)
- [apache_camp_plateau](#apache_camp_plateau)
- [ancient_cave_chamber](#ancient_cave_chamber)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: arizona_mountains_hills

[[SECTION markdown]]

# Arizona Mountains/Hills

**Role:** Primary discovery site and transit setting.

**Geography:** Rugged, desolate mountain terrain characterized by rocky outcrops and steep, gold-bearing veins.

**Lighting and Atmosphere:** Harsh, sun-bleached landscape; dusty, isolated, and high-contrast lighting.

**Scale and Anchors:** Expansive, rugged hillsides; prominent quartz/gold veins in rock faces.

**Prompt Phrases:** "rugged desert mountains", "desolate rocky terrain", "sun-scorched canyon walls", "dusty mountain trails".

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: apache_camp_plateau

[[SECTION markdown]]

# Apache Camp Plateau

**Role:** Secondary conflict setting.

**Geography:** A large, expansive plateau.

**Architecture and Features:** A dense encampment consisting of hundreds of traditional tepees.

**Lighting and Atmosphere:** Wide-open vistas; dusty atmosphere driven by high activity and movement.

**Scale and Anchors:** Massive scale; a vast sea of canvas tepees stretching across the highland.

**Prompt Phrases:** "expansive plateau", "vast tepee encampment", "wide highland plains", "large-scale indigenous camp".

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: ancient_cave_chamber

[[SECTION markdown]]

# Ancient Cave Chamber

**Role:** Primary transition and climax setting.

**Geography:** A large, cavernous chamber situated at the terminus of a high cliff trail.

**Architecture and Features:** Smooth, worn stone floor; ancient, hollowed-out geological structure.

**Lighting and Atmosphere:** Deep, mysterious shadows; dim, oppressive lighting; an atmosphere of heavy, overwhelming stillness/drowsiness.

**Scale and Anchors:** Large subterranean chamber; smooth floor surface; high cliff entrance.

**Prompt Phrases:** "ancient cavernous chamber", "smooth stone cave floor", "shadowy limestone interior", "mysterious deep cave".

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
