# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T07:37:49.952633+00:00
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
John Carter infiltrates the city of Thark to rescue Dejah Thoris from the clutches of the Thark Jeddak, Tal Hajus. After witnessing Tal Hajus's cruel intentions and his plan to torture the Princess, Carter intervenes, knocking the Jeddak unconscious with a single blow. Carter, Dejah Thoris, and Sola escape the city on thoats, heading northeast across a mossy waste toward Helium. 

The journey becomes perilous as the party runs out of food and water, eventually becoming lost. During their trek, they are joined by John Carter's faithful hound, Woola. After one of their thoats collapses from exhaustion, the group is spotted by a Thark scouting party. A chieftain discovers them with a fieldglass and charges toward them. To ensure the escape of Dejah Thoris and Sola, Carter uses his Martian rifle to kill the charging chieftain and then stays behind to provide cover fire against a massive force of Thark warriors. After exhausting his ammunition, Carter attempts to flee using superhuman leaps but is eventually overtaken and beaten into unconsciousness by the pursuing warriors.

**Characters:**
* **John Carter:** The protagonist; heroically rescues Dejah Thoris and sacrifices his safety to ensure her escape.
* **Dejah Thoris:** Princess of Helium; maintains her dignity even in captivity and expresses profound love for Carter during their escape.
* **Sola:** Dejah Thoris's companion; assists in the escape and helps manage the thoat.
* **Tal Hajus:** The cruel and bestial Jeddak of the Tharks; defeated by Carter.
* **Tars Tarkas:** A Thark chieftain who watches the scene with silent loathing for Tal Hajus.
* **Woola:** John Carter's loyal Martian hound who tracks the party through the waste.

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

- [thark_city_settlement](thark_city_settlement)
- [mossy_waste_expanse](mossy_waste_expanse)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: thark_city_settlement

[[SECTION markdown]]

# Thark City Settlement

**Role:** Primary (Conflict/Infiltration Setting)

**Architecture & Geography:** A fortified settlement characterized by large circular halls and elevated high platforms. The structure is built for the physiology of the green-skinned Tharks, emphasizing verticality and communal gathering spaces.

**Lighting & Atmosphere:** Harsh, imposing, and oppressive. The atmosphere is defined by the presence of the Jeddak's court and the tension of captivity.

**Scale & Anchors:** Large-scale circular architecture; high platforms overlooking central halls; fortified perimeter walls.

**Prompt Phrases:** Fortified Thark settlement, large circular stone halls, elevated viewing platforms, green-skinned warrior architecture, imposing Martian city.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: mossy_waste_expanse

[[SECTION markdown]]

# Mossy Waste Expanse

**Role:** Secondary (Transit/Peril Setting)

**Architecture & Geography:** A vast, trackless expanse of terrain located between Thark and Helium. The landscape is characterized by low mountains and a lack of visible waterways, making it a desolate trek.

**Lighting & Atmosphere:** Desolate, exposed, and punishing. The environment feels endless and provides little cover, contributing to the sense of being lost and vulnerable.

**Scale & Anchors:** Vast horizons; rolling low mountains; sparse vegetation; trackless terrain.

**Prompt Phrases:** Trackless mossy waste, desolate Martian landscape, low mountain silhouettes, arid expanse, vast barren plains.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
