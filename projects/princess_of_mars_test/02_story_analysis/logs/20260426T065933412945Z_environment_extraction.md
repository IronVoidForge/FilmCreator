# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-26T06:59:33.412945+00:00
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

Chapter id: CH020

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

**Events:**
After two weeks of wandering through the Martian wilderness, during which he is attacked by wild beasts and aided by his faithful calot Woola, John Carter reaches a massive Atmosphere Factory. Inside, he is hosted by an elderly man who possesses a diadem with a unique "ninth ray" stone. Through his telepathic abilities, Carter learns that this facility is vital to the survival of all life on Mars, as it produces the planet's atmosphere. 

The host, sensing Carter is an outsider, secretly plots to kill him to protect the plant's secrets. However, Carter uses his telepathy to intercept the nine thought-waves required to operate the factory's massive doors, allowing him and Woola to escape. Following his escape, Carter is found by a group of hospitable Red Martian government officers on a farm. They provide him with food, rest, and assistance in disguising himself as a local Red Martian—anointing his skin with red oil and cutting his hair to match the fashion—to help him blend in as he travels toward Zodanga.

**Characters:**
- **John Carter:** Exhausted and starving, but increasingly proficient in using telepathy to read minds and manipulate technology.
- **Woola:** Carter's loyal calot who saves him from a multi-legged beast and accompanies him on his journey.
- **The Old Man (Atmosphere Plant Host):** A solitary guardian of the atmosphere machinery who views Carter as a threat to Barsoom's stability.
- **The Ptor Family:** A group of Red Martian government officers who provide Carter with hospitality, supplies, and a disguise.

**Settings:**
- **The Atmosphere Factory:** A massive, unassailable concrete structure containing radium pumps and the machinery that generates the Martian atmosphere using the ninth ray.
- **The Ptor Farm:** A collection of Red Martian homes raised on metal shafts to avoid danger, located near a broad white turnpike.
- **The Martian Wilderness:** A harsh landscape filled with strange beasts and vegetation providing "vegetable milk."
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [martian_wilderness](martian_wilderness)
- [atmosphere_factory](atmosphere_factory)
- [ptor_farmstead](ptor_farmstead)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: martian_wilderness

[[SECTION markdown]]

# Martian Wilderness

**Role:** Primary / Transit Setting

**Geography:** A harsh, sprawling landscape of alien terrain; vast stretches of desolate wilderness punctuated by strange vegetation capable of producing "vegetable milk."

**Lighting and Atmosphere:** Harsh, unfiltered sunlight; high-contrast shadows; an atmosphere that feels thin and perilous.

**Scale and Anchors:** Vast, open horizons; scattered patches of exotic flora; territory inhabited by multi-legged beasts.

**Prompt Phrases:** Desolate Martian plains, alien vegetation, harsh wilderness, vast Barsoomian landscape, predatory fauna habitat.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: atmosphere_factory

[[SECTION markdown]]

# Atmosphere Factory

**Role:** Primary Setting

**Architecture:** A massive, unassailable concrete structure; heavy industrial design featuring radium pumps and complex machinery.

**Lighting and Atmosphere:** Industrial gloom; mechanical hum; localized light from the "ninth ray" stone; high-tech/low-life atmosphere of ancient vital technology.

**Scale and Anchors:** Massive scale; towering doors operated by thought-waves; central core containing atmospheric generation machinery.

**Prompt Phrases:** Brutalist concrete monolith, radium pump machinery, massive industrial doors, ninth ray glow, planetary life-support facility.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: ptor_farmstead

[[SECTION markdown]]

# Ptor Farmstead

**Role:** Secondary / Transit Setting

**Architecture:** Red Martian residential structures raised on high metal shafts to provide safety from ground-level threats; located near a broad white turnpike.

**Lighting and Atmosphere:** Domestic, hospitable, and relatively safe; bright daylight reflecting off the white road.

**Scale and Anchors:** Elevated dwellings; wide access roads; clustered farmstead layout.

**Prompt Phrases:** Elevated Martian homes, metal shaft architecture, white turnpike, Red Martian settlement, high-ground farmstead.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
