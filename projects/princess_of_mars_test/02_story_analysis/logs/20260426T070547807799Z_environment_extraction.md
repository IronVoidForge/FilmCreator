# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-26T07:05:47.807799+00:00
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
John Carter's aircraft is shot down during a massive battle between Tharks and Warhoons. He intervenes to save Tars Tarkas from being killed by three Warhoon warriors, cementing a new friendship between them. Following the battle, John Carter reunites with his faithful hound, Woola. 

The narrative shifts to political maneuvering within Thark. To avoid the wrath of the current Jeddak, Tal Hajus, John Carter and Tars Tarkas decide to face him in council. Beforehand, they intimidate the priestess Sarkoja into fleeing. In the council, John Carter publicly challenges Tal Hajus's fitness to rule, citing his cowardice in battle. The council decrees a duel between Tal Hajus and Tars Tarkas; Tars Tarkas wins, becoming the new Jeddak and elevating John Carter to the rank of chieftain.

Leveraging this new power, John Carter proposes an alliance to the Thark hordes: a raid on Zodanga to rescue Dejah Thoris and seize their wealth. The Tharks enthusiastically agree. A massive force of 150,000 Green Martians marches on Zodanga. Under the cover of night, John Carter leads a small group in a daring infiltration of the city by scaling the walls using a human ladder. He successfully enters the palace grounds and begins coordinating a silent takeover of the city gates to prepare for the main assault.

**Characters:**
- **John Carter:** The protagonist; a skilled warrior and strategist who uses his Earthly ingenuity to lead Thark forces.
- **Tars Tarkas:** A mighty Thark warrior who becomes Jeddak after defeating Tal Hajus.
- **Woola:** John Carter's loyal, giant hound.
- **Tal Hajus:** The former Jeddak of Thark; a coward and tyrant defeated by Tars Tarkas.
- **Sarkoja:** A priestess who flees Thark after being threatened by Tars Tarkas.
- **Lorquas Ptomel:** A Thark chieftain who supports the challenge against Tal Hajus.

**Settings:**
- **The Battlefield:** A plain near an ancient dead city where the Thark/Warhoon conflict occurs.
- **Thark (City):** The seat of power for the Green Martians.
- **Zodanga:** A great walled city of the Red Martians, characterized by massive carborundum walls and a central palace.
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
- [thark_city_complex](thark_city_complex)
- [zodanga_walled_city](zodanga_walled_city)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: battlefield_plains

[[SECTION markdown]]

# Battlefield Plains

**Role:** Primary (Conflict Setting)

**Geography:** An expansive, desolate plain situated near the ruins of an ancient dead city. The terrain is rugged and scarred by heavy combat.

**Lighting and Atmosphere:** Chaotic and dust-filled; atmosphere dominated by the smoke of battle and the debris of downed aircraft. High-contrast lighting from Martian sun filtered through dust clouds.

**Scale Cues:** Vast open spaces capable of hosting massive clashes between Thark and Warhoon hordes; punctuated by the skeletal remains of ancient architecture.

**Prompt Phrases:** Desolate Martian plain, ruins of a dead city, battlefield debris, dust-choked atmosphere, wide combat expanse, scarred wasteland.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: thark_city_complex

[[SECTION markdown]]

# Thark City Complex

**Role:** Primary (Political/Social Setting)

**Geography:** The central seat of power for the Green Martians; a structured urban center designed for Thark biology and social hierarchy.

**Lighting and Atmosphere:** Harsh, utilitarian lighting; atmosphere of tension and political maneuvering.

**Scale Cues:** Large council chambers and communal areas capable of holding high-ranking chieftains and priestesses.

**Prompt Phrases:** Green Martian city, Thark architecture, tribal urban center, martial settlement, stone and metal structures.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: zodanga_walled_city

[[SECTION markdown]]

# Zodanga Walled City

**Role:** Primary (Infiltration/Assault Setting)

**Geography:** A massive, fortified metropolis belonging to the Red Martians. Features immense carborundum walls and a central palace complex.

**Lighting and Atmosphere:** Nocturnal/Low-light; shadows used for infiltration; high-stakes tension during silent takeovers.

**Scale Cues:** Monumental scale; towering defensive walls requiring human ladders for scaling; sprawling palace grounds.

**Prompt Phrases:** Massive carborundum walls, Red Martian metropolis, fortified city gates, grand central palace, nocturnal urban landscape, monumental fortifications.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
