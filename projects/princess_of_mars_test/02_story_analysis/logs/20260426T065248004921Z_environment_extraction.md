# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-26T06:52:48.004921+00:00
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

Chapter id: CH015

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
Following his combat with Zad, John Carter recovers from a non-fatal wound inflicted by a sword thrust to his chest. He reunites with his retinue and finds Dejah Thoris in deep mourning, believing him dead. Sola, who was injured during the encounter with Sarkoja, reveals that she is an outcast among her people due to her capacity for emotion. That night, while the massive caravan of two hundred and fifty chariots moves silently across a moss-covered sea bottom, Sola shares her secret history with Carter. She recounts how her mother and a Thark warrior fell in love, leading to Sola's clandestine upbringing. Her mother was eventually discovered by Sarkoja and executed by Tal Hajus after refusing to reveal the father's identity. Sola concludes her story by revealing that her father is Tars Tarkas, who remains unaware of her true identity.

**Characters:**
* **John Carter:** Recovering from a wound; observes the grief of Dejah Thoris and listens to Sola's confession.
* **Sola:** A green Martian woman who reveals her tragic lineage and her father's identity.
* **Dejah Thoris:** Mourning John Carter in silence, unaware of his survival.
* **Sarkoja (Mentioned/Flashback):** The antagonist who discovered Sola's mother and reported her "sin."
* **Sola's Mother (Flashback):** A Thark woman who died under torture to protect her child and lover.
* **Tars Tarkas:** Revealed to be Sola's father; a high-ranking warrior traveling with the caravan.
* **Tal Hajus (Mentioned/Flashback):** The Thark chieftain responsible for the death of Sola's mother.

**Settings:**
* **The Mossy Sea Bottom:** A vast, trackless, and silent expanse of ochre moss that leaves no spoor as the massive caravan traverses it.
* **The Caravan Camp:** A campsite at the foot of hills marking the southern boundary of the sea, where the group rests after two days of marching.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [mossy_sea_bottom](#mossy_sea_bottom)
- [caravan_camp_hills](#caravan_camp_hills)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: mossy_sea_bottom

[[SECTION markdown]]

# Mossy Sea Bottom

**Role:** Transit setting

**Geography:** A vast, trackless expanse of a dried-up sea bed. The surface is entirely covered in a thick layer of ochre-colored moss.

**Lighting and Atmosphere:** Silent, expansive, and desolate. The terrain offers no visual landmarks or tracks, creating a sense of endless, featureless movement.

**Scale and Anchors:** Massive scale; accommodates a caravan of two hundred and fifty chariots moving silently across the surface. The lack of spoor or footprints makes the landscape feel unnervingly smooth.

**Prompt Phrases:** vast ochre moss sea bed, trackless Martian plains, silent chariot transit, thick velvet-like moss, featureless ochre expanse.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: caravan_camp_hills

[[SECTION markdown]]

# Caravan Camp Hills

**Role:** Secondary setting

**Geography:** A campsite located at the southern boundary of the mossy sea, situated at the foot of rising hills.

**Lighting and Atmosphere:** Grounded and stationary; provides a sense of respite after long travel across the plains.

**Scale and Anchors:** Defined by the transition from the flat sea bottom to the rising topography of the hills. Serves as a temporary anchor for the large traveling retinue.

**Prompt Phrases:** foothills at sea boundary, Martian caravan campsite, rocky hill base, desert encampment, transitional terrain.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
