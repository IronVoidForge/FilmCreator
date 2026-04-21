# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T15:25:30.350502+00:00
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

**Events:**
John Carter's craft is shot down during a battle between Tharks and Warhoons. He intervenes to save Tars Tarkas from being killed by three Warhoon warriors, establishing a bond of friendship between them. Following the battle, John Carter reunites with his faithful hound, Woola. 

The narrative shifts to political maneuvering within Thark. To avoid the wrath of the current Jeddak, Tal Hajus, John Carter and Tars Tarkas decide to face him in council. Beforehand, Tars Tarkas uses a clever threat to force the treacherous Sarkoja to flee. In the council, John Carter publicly challenges Tal Hajus's fitness to rule, citing his cowardice in battle. The council decrees a combat between Tal Hajus and Tars Tarkas; Tars Tarkas wins, becoming the new Jeddak and elevating John Carter to the rank of chieftain.

Leveraging this new power, John Carter proposes an alliance to the Thark hordes: a raid on Zodanga to rescue Dejah Thoris and seize their wealth. The Tharks enthusiastically agree, amassing a force of 150,000 warriors. After a ten-day march, the army reaches Zodanga. John Carter leads a small group in a stealthy infiltration of the city by scaling the massive carborundum walls using a human ladder and leather straps. He successfully enters the palace grounds and begins coordinating a silent takeover of the city gates to prepare for the main assault.

**Characters:**
- **John Carter:** The protagonist; uses his Earthly strength and tactical mind to rise to chieftain status.
- **Tars Tarkas:** A mighty Thark warrior who becomes Jeddak after defeating Tal Hajus.
- **Woola:** John Carter's loyal, giant hound.
- **Tal Hajus:** The former Jeddak of Thark; a coward defeated in combat.
- **Sarkoja:** A treacherous Thark woman forced into exile by Tars Tarkas.
- **Lorquas Ptomel:** A Thark chieftain who supports the challenge against Tal Hajus.

**Settings:**
- **The Battlefield:** A plain near an ancient dead city where the Thark/Warhoon conflict occurs.
- **Thark (City):** The seat of power for the Green Martians.
- **Zodanga:** A massive, walled city built of carborundum; the target of the Thark expedition.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [battlefield_plains](battlefield_plains)
- [thark_city_settlement](thark_city_settlement)
- [zodanga_walled_city](zodanga_walled_city)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: battlefield_plains

[[SECTION markdown]]

# Battlefield Plains

**Role:** Secondary / Transit Setting

**Geography:** An expansive, desolate plain situated near the ruins of an ancient dead city. The terrain is rugged and scarred by conflict.

**Lighting and Atmosphere:** Harsh, open exposure; dusty atmosphere filled with the debris of combat and the aftermath of aerial/ground skirmishes.

**Scale Cues:** Vast horizons; punctuated by the wreckage of downed crafts and the scattered remains of warring hordes.

**Descriptive Noun Phrases:** Desolate Martian plain, ancient dead city ruins, scarred battlefield, dust-choked expanse, war-torn wasteland.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: thark_city_settlement

[[SECTION markdown]]

# Thark City Settlement

**Role:** Primary Setting (Political)

**Geography:** The seat of power for the Green Martian Tharks; a structured settlement designed for martial governance and council gatherings.

**Lighting and Atmosphere:** Formal, heavy atmosphere; interior spaces or central plazas used for high-stakes political maneuvering and combat trials.

**Scale Cues:** Large council chambers capable of holding many warriors; areas defined by the presence of Jeddak leadership.

**Descriptive Noun Phrases:** Thark seat of power, martial council chamber, Green Martian settlement, chieftain's stronghold.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: zodanga_walled_city

[[SECTION markdown]]

# Zodanga Walled City

**Role:** Primary Setting (Tactical/Infiltration)

**Geography:** A massive, fortified metropolis characterized by immense carborundum walls. Includes high-altitude palace grounds and heavily guarded gates.

**Lighting and Atmosphere:** High-contrast lighting; shadows cast by massive fortifications; tense, silent atmosphere during stealth operations.

**Scale Cues:** Colossal carborundum walls; verticality emphasized by scaling maneuvers; sprawling urban layout within the perimeter.

**Descriptive Noun Phrases:** Carborundum walled city, massive fortification, palace grounds, high-altitude ramparts, fortified metropolitan gates.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
