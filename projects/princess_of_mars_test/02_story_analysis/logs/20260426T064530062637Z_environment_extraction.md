# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-26T06:45:30.062637+00:00
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

Chapter id: CH010

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

**Setting:** The city of the Tharks (Green Men) and the audience chamber of Lorquas Ptomel.

**Characters:**
- **John Carter:** An Earthman from Virginia, now possessing the status of a Martian chieftain through combat.
- **Woola:** A large, loyal Martian hound who has formed a deep bond with Carter.
- **Dejah Thoris:** The captive Princess of Helium, characterized by her grace and intelligence.
- **Tars Tarkas:** A Thark warrior/leader who observes Carter with curiosity and respect.
- **Lorquas Ptomel:** A Thark chieftain presiding over the council.
- **Sola:** A kind Martian woman (an "atavism") who has been teaching Carter the Martian language.
- **Sarkoja:** A cruel Green Martian woman guarding the prisoner.

**Events:**
- **Bonding with Woola:** Early in the morning, Carter tests his bond with Woola by using affection to overcome the creature's instinctual duty to keep him confined. He successfully establishes himself as Woola's undisputed master.
- **The Audience Chamber:** Carter observes a trial where Dejah Thoris defends her people's role in maintaining Mars' atmosphere against the "brutal" Green Men. Her plea for amity momentarily touches the Thark council, including Tars Tarkas.
- **The Outburst of Violence:** A young Thark warrior breaks the tension by striking Dejah Thoris across the face. Infuriated, John Carter intervenes, engaging the twelve-foot warrior in combat and killing him.
- **Ascension to Chieftaincy:** By killing the warrior, Carter inadvertently wins the "spoils" of the deceased, including regalia and weapons. Under Martian custom, he is now recognized as a Thark chieftain.
- **Confrontation with Tars Tarkas:** Tars Tarkas questions Carter's sudden mastery of the language and warns him of the responsibilities and dangers of his new status. Carter asserts his moral code, declaring that he will protect Dejah Thoris from any further insult or injury.
- **Departure:** Recognized as a conqueror/chieftain, Carter escorts Dejah Thoris out of the audience chamber, accompanied by Woola.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [thark_city_complex](thark_city_complex)
- [lorquas_ptomel_audience_chamber](lorquas_ptomel_audience_chamber)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: thark_city_complex

[[SECTION markdown]]

# Thark City Complex

**Role:** Primary / Transit Setting

**Architecture & Geography:** A sprawling, rugged urban settlement inhabited by the Green Men. The architecture is built to accommodate twelve-foot warriors, characterized by large-scale structures and communal spaces designed for martial culture.

**Lighting & Atmosphere:** Harsh, exposed Martian light; a sense of brutalist functionality and constant tension.

**Scale & Anchors:** Massive scale suitable for giant inhabitants; wide thoroughfares and high-ceilinged communal areas.

**Prompt Phrases:** Brutalist Martian architecture, colossal green-man settlement, rugged red-dust urbanity, massive scale structures, martial Thark city.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: lorquas_ptomel_audience_chamber

[[SECTION markdown]]

# Lorquas Ptomel Audience Chamber

**Role:** Primary Setting (Political/Conflict)

**Architecture & Geography:** A formal, high-stakes assembly hall within the Thark city. It serves as a central hub for council meetings and judicial proceedings.

**Lighting & Atmosphere:** Dramatic, heavy atmosphere; shadows cast by large warriors; tension-filled lighting suitable for trials and sudden outbursts of violence.

**Scale & Anchors:** Large enough to hold a council of Thark chieftains and prisoners; centered around a focal point for the presiding chieftain.

**Prompt Phrases:** Grand Martian council hall, imposing Thark audience chamber, ceremonial martial assembly, high-tension political arena, cavernous stone meeting hall.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
