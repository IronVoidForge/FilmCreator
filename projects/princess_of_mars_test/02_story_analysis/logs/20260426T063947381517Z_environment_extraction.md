# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-26T06:39:47.381517+00:00
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

Chapter id: CH006

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

**Setting:** An interior chamber within a Martian building, overlooking a plaza.

**Characters:**
* **The Protagonist (Earthman):** A survivor who uses Earthly combat tactics to defend himself.
* **The Watch-thing:** A loyal, multi-legged, beast-like creature that acts as the protagonist's guardian.
* **The Bull Apes:** Two massive, ten-to-fifteen-foot tall, ape-like creatures with four arms and immense strength.
* **Tars Tarkas:** A Martian warrior who observes and respects the protagonist's combat skills.
* **Sola:** A Martian woman who shows uncharacteristic compassion and solicitude toward the protagonist.
* **Martian Warriors:** A group of warriors who value physical bravery above all else.

**Events:**
* **The Ambush:** The protagonist is pinned by one massive bull ape while its mate approaches with a stone cudgel to kill him.
* **The Battle of the Beasts:** The protagonist's watch-thing intervenes, engaging the first ape in a ferocious struggle. As the watch-thing begins to succumb to the ape's strength, the protagonist seizes the fallen cudgel and crushes the ape's skull.
* **The Second Duel:** The second bull ape, enraged by its mate's death, charges the protagonist. Despite the overwhelming physical disadvantage, the protagonist uses a combination of throwing the cudgel and tactical hand-to-hand strikes to incapacitate and kill the creature.
* **Martian Observation:** Tars Tarkas, Sola, and a group of warriors arrive, having witnessed the fight. They applaud the protagonist's prowess, viewing his combat as a demonstration of high social value.
* **Conflict over the Beast:** The Martians attempt to execute the wounded watch-thing. The protagonist intervenes physically to stop a warrior from shooting the creature. 
* **Resolution:** Tars Tarkas allows the protagonist to keep his beast. The protagonist realizes he has formed two distinct types of bonds: a compassionate connection with Sola and a loyal, primal bond with his watch-thing.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

| Asset ID | Description |
| :--- | :--- |
| martian_interior_chamber | An interior chamber overlooking a plaza, serving as the site of the combat and observation. |

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: martian_interior_chamber

[[SECTION markdown]]

# Martian Interior Chamber

**Role:** Primary setting for combat and social observation.

**Architecture or Geography:** An interior chamber within a Martian structure, featuring an overlook that faces a large plaza. The space is designed to accommodate massive creatures (Bull Apes) and provides vantage points for observing warriors below.

**Lighting and Atmosphere Cues:** Harsh, dramatic lighting typical of Martian interiors; high-contrast shadows during the combat struggle; atmosphere of tension and primal violence transitioning into social reverence.

**Scale Cues and Recurring Environmental Anchors:** Large enough to host ten-to-fifteen-foot tall Bull Apes; features an overlook/balcony structure; open floor space suitable for beast-on-beast combat.

**Descriptive Noun Phrases:** Martian stone architecture, plaza overlook, high-contrast interior, combat arena chamber, massive scale masonry.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
