# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T07:32:39.022271+00:00
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
Following his duel with Zad, John Carter recovers from a non-fatal wound inflicted by a sword thrust to the chest. He reunites with his retinue and finds Dejah Thoris in deep mourning, believing him dead. Sola, who was injured during her encounter with Sarkoja, reveals that Dejah's grief is due to her profound affection for Carter. As the massive caravan—comprising hundreds of chariots, warriors, and animals—moves silently across a trackless mossy sea bottom, they camp at the foot of southern hills. That night, Sola shares her tragic history with Carter. She reveals that she is the daughter of a Thark woman and a high-ranking warrior who fell in love in secret. Her mother was discovered by Sarkoja and subsequently tortured to death by Tal Hajus for refusing to reveal the father's identity. Sola concludes by revealing that her father is Tars Tarkas, who remains unaware of her true identity.

**Characters:**
* **John Carter:** Recovering from a chest wound; observes the scale of the Martian caravan.
* **Sola:** A Green Martian woman who reveals her secret lineage and tragic past.
* **Dejah Thoris:** Shown in a state of intense grief, mourning Carter's perceived death.
* **Sarkoja:** Mentioned as the antagonist who discovered Sola's mother and caused her downfall.
* **Tars Tarkas:** Revealed to be Sola's father; currently traveling with the caravan.
* **Sola's Mother:** (Flashback) A Thark woman who died protecting her child and her lover's identity.

**Settings:**
* **The Mossy Sea Bottom:** A vast, silent, trackless waste covered in moss that absorbs the tracks of the passing caravan.
* **The Caravan Camp:** Located at the foot of hills marking the southern boundary of the sea; a site of rest after two days of travel.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [mossy_sea_bottom](mossy_sea_bottom)
- [caravan_camp_southern_hills](caravan_camp_southern_hills)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: mossy_sea_bottom

[[SECTION markdown]]

# Mossy Sea Bottom

**Role:** Transit setting

**Geography:** A vast, trackless waste characterized by a flat, expansive seabed. The surface is covered in a thick layer of moss that swallows footprints and chariot tracks.

**Lighting and Atmosphere:** Silent, desolate, and immense. The atmosphere is heavy with the sense of an endless, featureless void.

**Scale and Anchors:** Massive scale; hundreds of chariots and warriors appear small against the horizon. The primary anchor is the uniform, absorbing texture of the mossy floor.

**Prompt Phrases:** trackless mossy sea bottom, vast silent waste, absorbent moss surface, endless Martian seabed, featureless expanse.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: caravan_camp_southern_hills

[[SECTION markdown]]

# Caravan Camp Southern Hills

**Role:** Secondary setting / Rest site

**Geography:** A campsite situated at the base of southern hills that serve as a boundary to the mossy sea bottom.

**Lighting and Atmosphere:** Nighttime setting; provides a sense of temporary refuge and communal rest amidst a harsh landscape.

**Scale and Anchors:** Large-scale encampment containing hundreds of chariots, warriors, and animals. The recurring anchor is the silhouette of the southern hills against the night sky.

**Prompt Phrases:** caravan camp at hill foot, southern Martian hills, nocturnal military encampment, chariot resting site, hillside boundary.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
