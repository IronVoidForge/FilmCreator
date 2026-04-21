# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T07:31:54.374032+00:00
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
After two weeks of wandering through the Barsoomian wilderness, surviving attacks by wild beasts with the help of his telepathic warnings and his faithful calot, Woola, the protagonist reaches a massive Atmosphere Factory. He is admitted by an invisible host who uses advanced technology to scan him. The protagonist meets an elderly Martian caretaker who reveals that the plant uses "the ninth ray" to generate the planet's atmosphere via radium pumps. 

The protagonist discovers through telepathy that the caretaker intends to murder him to protect the secret of the plant and prevent any potential disruption to the atmosphere. Using his newfound ability to mimic the nine specific thought-waves required for the facility's locks, the protagonist escapes the factory with Woola. He eventually encounters a group of hospitable Red Martian government officers on a farm. They provide him with food, rest, and disguise him (using reddish oil and a specific haircut) to look like a local Red Martian. They also provide him with a bullthoat for transport and Zodangan money, advising him to seek military service in Zodanga to establish his credibility.

**Characters:**
* **The Protagonist:** A man from Earth, physically distinct from Martians, possessing telepathic abilities that allow him to read thoughts and manipulate thought-wave locks.
* **Woola:** The protagonist's faithful, large calot who protects him from wild beasts.
* **The Caretaker:** An elderly, dried-up Martian living in isolation at the Atmosphere Factory; he is highly skilled in mental control but views the protagonist as a threat to Barsoom.
* **The Ptor Family:** A group of Red Martian government officers who provide hospitality and disguise to the protagonist.

**Settings:**
* **The Barsoomian Wilderness:** A dangerous landscape filled with strange beasts and scarce resources.
* **The Atmosphere Factory:** A massive, unassailable concrete structure (four square miles) containing the machinery and radium pumps that sustain the Martian atmosphere.
* **The Ptor Farm:** A collection of Red Martian homes raised on metal shafts to protect against danger, situated near a broad white turnpike.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [barsoomian_wilderness](barsoomian_wilderness)
- [atmosphere_factory](atmosphere_factory)
- [ptor_farmstead](ptor_farmstead)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: barsoomian_wilderness

[[SECTION markdown]]

# Barsoomian Wilderness

**Role:** Primary / Transit Setting

**Geography:** Vast, desolate landscapes characterized by extreme scarcity and rugged terrain. A wilderness populated by predatory fauna and strange biological anomalies.

**Lighting & Atmosphere:** Harsh, exposed sunlight; high-contrast shadows; sense of isolation and constant environmental threat.

**Scale & Anchors:** Expansive horizons; unpredictable terrain shifts; presence of wild beast territories.

**Prompt Phrases:** desolate Martian wasteland, rugged Barsoomian terrain, predatory wilderness, vast arid plains, alien flora and fauna.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: atmosphere_factory

[[SECTION markdown]]

# Atmosphere Factory

**Role:** Primary Setting

**Architecture:** A massive, unassailable concrete monolith spanning four square miles. Contains high-tech internal chambers and complex machinery.

**Lighting & Atmosphere:** Industrial, sterile, and highly controlled. Features specialized lighting related to "the ninth ray" and radium-based energy sources.

**Scale & Anchors:** Colossal scale; massive radium pumps; advanced technological locks requiring specific thought-wave frequencies; vast interior industrial halls.

**Prompt Phrases:** monolithic concrete factory, massive Martian industrial complex, radium pump machinery, high-tech atmosphere plant, colossal brutalist architecture.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: ptor_farmstead

[[SECTION markdown]]

# Ptor Farmstead

**Role:** Secondary / Transit Setting

**Architecture:** Red Martian residential structures elevated on high metal shafts to provide protection from ground-level threats. Located near a broad white turnpike.

**Lighting & Atmosphere:** Domestic and hospitable; bright, open vistas; sense of organized civilization amidst the wild.

**Scale & Anchors:** Elevated dwellings; wide transit roads (white turnpikes); agrarian Martian layout.

**Prompt Phrases:** elevated Martian farmhouses, metal shaft architecture, Red Martian settlement, broad white turnpike, high-ground residential structures.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
