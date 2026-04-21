# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T07:10:01.297096+00:00
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

**Setting:** The city of the Tharks (green Martians) and its surrounding hills/ravines.

**Characters:**
- **John Carter:** An Earthman, now recognized as a Tharkian chieftain due to his combat prowess.
- **Woola:** A loyal, large Martian creature (white ape-like/hound-like) who serves as Carter's protector.
- **Dejah Thoris:** The Princess of Helium (a red Martian), currently held captive by the Tharks.
- **Sola:** A kind and civilized green Martian woman who has been instructing Carter in the Martian language.
- **Tars Tarkas:** A prominent Tharkian warrior/leader.
- **Lorquas Ptomel:** A Thark chieftain presiding over a council.
- **Sarkoja:** A cruel green Martian woman acting as a guard for the prisoner.

**Events:**
- **Bonding with Woola:** Carter explores the outskirts of the city and successfully uses affection to establish a deeper bond of friendship and authority with Woola, overcoming the creature's instinctual warnings.
- **The Audience Chamber:** Carter observes the trial of Dejah Thoris. The Princess delivers a powerful plea for amity and civilization, appealing to the Tharks' sense of humanity, which briefly touches even the hardened warriors like Tars Tarkas.
- **The Outburst:** A young Thark warrior breaks the tension by striking Dejah Thoris in the face as a form of "humor." 
- **Combat and Ascension:** Enraged, John Carter intervenes and kills the young warrior in single combat. Because he killed a fellow warrior, he is immediately accorded the status and regalia of a Tharkian chieftain.
- **Meeting Dejah Thoris:** Carter tends to the Princess's injuries and reveals his identity as an Earthman from Virginia. 
- **Diplomatic Stand:** Tars Tarkas informs Carter that while he is respected as a chieftain, he is still responsible for being delivered to the supreme ruler, Tal Hajus. Carter delivers a defiant speech asserting his moral code and his intent to protect Dejah Thoris from any further insult or injury.
- **Departure:** Having gained status through combat, Carter leads Dejah Thoris out of the audience chamber, accompanied by Woola.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [thark_city_outskirts](thark_city_outskirts)
- [thark_audience_chamber](thark_audience_chamber)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: thark_city_outskirts

[[SECTION markdown]]

# Thark City Outskirts

**Role:** Secondary / Transit Setting

**Geography:** Rugged Martian terrain consisting of hills and deep ravines surrounding the green Martian settlement. The landscape is characterized by rocky outcrops and uneven ground suitable for large creatures.

**Lighting and Atmosphere:** Harsh, open Martian light; dusty and windswept atmosphere typical of the red planet's surface.

**Scale Cues:** Expansive vistas of canyons and hills; wide-open spaces that allow for the movement of large beasts like Woola.

**Prompt Phrases:** rugged martian ravines, rocky hill outcrops, dusty canyon terrain, vast martian landscape, arid wasteland.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: thark_audience_chamber

[[SECTION markdown]]

# Thark Audience Chamber

**Role:** Primary Setting

**Architecture:** A large, imposing communal hall or chamber used by the Thark chieftains for trials and councils. It is designed to accommodate many large, green Martian warriors.

**Lighting and Atmosphere:** Dimly lit, heavy, and tense; a sense of primitive authority and martial gravity.

**Scale Cues:** Large-scale interior capable of holding a council of warriors; high ceilings or wide spans to accommodate the physical presence of Tharks.

**Prompt Phrases:** primitive martian council chamber, cavernous warrior hall, dim tribal assembly, imposing stone architecture, heavy atmosphere of martial law.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
