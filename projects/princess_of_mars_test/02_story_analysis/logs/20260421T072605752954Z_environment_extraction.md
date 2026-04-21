# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T07:26:05.752954+00:00
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

Chapter id: CH017

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
John Carter infiltrates the city of Thark to rescue Dejah Thoris from the clutches of the Thark Jeddak, Tal Hajus. After observing the terrifying presence of Tal Hajus and witnessing Tars Tarkas's silent loathing for the beast, Carter intervenes just as Tal Hajus attempts to seize the Princess. Instead of using his sword, Carter knocks the Jeddak unconscious with a single blow. 

Carter, Dejah Thoris, and Sola escape the city on thoats, heading northeast across a mossy waste toward Helium. The journey becomes a desperate struggle for survival as they run out of food and water. Their progress is slowed by the exhaustion of their mounts; one thoat collapses, forcing Carter and Sola to walk while Dejah Thoris rides. 

The group is eventually spotted by a Thark scouting party. A chieftain discovers them with a fieldglass and leads a charge. To ensure the escape of the women, Carter uses his Martian rifle to kill the charging chieftain and then stays behind to provide cover fire. After exhausting his ammunition, he uses his superior physical abilities to distract the approaching thousand-man Thark army. While successfully leading the warriors away from Dejah Thoris, Carter is eventually overtaken and beaten into unconsciousness by the pursuing force.

**Characters:**
* **John Carter:** The protagonist; a resourceful and brave warrior who sacrifices his own safety to ensure Dejah Thoris's escape.
* **Dejah Thoris:** Princess of Helium; maintains her dignity even in captivity and expresses profound love for Carter during their escape.
* **Sola:** Dejah Thoris's companion; assists in the escape and helps manage the Princess during the flight.
* **Tal Hajus:** The cruel and bestial Jeddak of the Tharks; defeated by Carter.
* **Tars Tarkas:** A Thark warrior who harbors deep hatred for Tal Hajus but fails to intervene in time.
* **Woola:** Carter's faithful Martian hound, who tracks the group through the waste.

**Settings:**
* **The City of Thark:** A fortified settlement inhabited by the green-skinned Tharks, featuring large circular halls and high platforms.
* **The Mossy Waste:** A vast, trackless, and dangerous expanse between Thark and Helium, characterized by a lack of waterways and low mountains.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [city_of_thark](city_of_thark)
- [mossy_waste](mossy_waste)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: city_of_thark

[[SECTION markdown]]

# City of Thark

**Role:** Primary setting (conflict/climax location).

**Architecture & Geography:** A fortified Martian settlement characterized by large circular halls and elevated high platforms. The architecture is designed for the physiology of the Tharks, emphasizing verticality and communal gathering spaces.

**Lighting & Atmosphere:** Harsh, imposing, and oppressive. The atmosphere is heavy with the presence of the Jeddak's court, feeling both ancient and brutal.

**Scale & Anchors:** Massive circular structures; high-altitude platforms overlooking the settlement; central halls used for ruling and judgment.

**Prompt Keywords:** fortified Martian city, Thark architecture, large circular halls, elevated stone platforms, brutalist alien settlement, high-altitude vantage points.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: mossy_waste

[[SECTION markdown]]

# Mossy Waste

**Role:** Secondary setting (transit/survival location).

**Architecture & Geography:** A vast, trackless expanse of terrain located northeast of Thark. The landscape is characterized by low mountains and a lack of natural waterways. The ground is covered in thick, mossy textures.

**Lighting & Atmosphere:** Desolate, exposed, and draining. The atmosphere is one of scarcity and exhaustion; a dry, sun-bleached environment where survival is difficult due to the absence of water.

**Scale & Anchors:** Endless horizons; low, rolling mountains; sparse vegetation consisting primarily of mossy ground cover; vast open plains.

**Prompt Keywords:** trackless wasteland, mossy terrain, low Martian mountains, arid expanse, desolate landscape, barren plains, sun-scorched earth.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
