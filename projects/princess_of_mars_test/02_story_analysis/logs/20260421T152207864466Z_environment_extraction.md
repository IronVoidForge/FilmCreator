# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T15:22:07.864974+00:00
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

Chapter id: CH018

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

**Summary:**
After being rescued from certain death by a group of Warhoon warriors, the protagonist regains consciousness and is prepared for transport to the main Warhoon column. He is treated by an ancient female healer and strapped to a wild thoat to be ridden as a prize for "the great games." Upon reaching the camp, he witnesses a violent power struggle between the young Jeddak Bar Comas and his insubordinate lieutenant, Dak Kova. The two engage in a savage, primal duel that results in the death of Bar Comas and the ascension of Dak Kova to leadership.

The Warhoon horde, characterized by extreme ferocity and frequent ritualistic combat, marches back to their city. The protagonist is imprisoned in a pitch-black dungeon, where he endures prolonged isolation and psychological terror amidst crawling creatures. In a moment of desperate survival, he ambushes his food deliverer with a heavy chain, killing the man and retrieving a set of keys. As he regains his sanity through this act, he is confronted by several pairs of glowing eyes in the darkness that watch him before retreating into the shadows.

**Characters:**
- **The Protagonist:** A human survivor, recovering from wounds and enduring psychological torture in captivity.
- **Dak Kova:** A scarred, ferocious Warhoon warrior/lieutenant who kills Bar Comas to become Jeddak.
- **Bar Comas:** The young, dignified Jeddak of Warhoon, killed in a duel by Dak Kova.
- **The Healer:** An ancient female Warhoon who treats the protagonist's wounds.
- **The Jailer:** A silent emissary who delivers food to the protagonist's cell.

**Settings:**
- **Warhoon Camp:** A mobile military camp characterized by extreme violence and ritualistic combat.
- **City of Warhoon:** The home of the Warhoon horde.
- **The Dungeon:** A pitch-black, terrifying subterranean cell filled with unknown crawling creatures and glowing eyes.

**Key Events:**
- The protagonist is healed and transported via thoat to the Warhoon main body.
- The duel between Bar Comas and Dak Kova, resulting in a brutal death and a change in leadership.
- The long period of isolation and sensory deprivation in the dungeon.
- The protagonist kills his jailer with a chain to obtain keys.
- The appearance of mysterious, glowing eyes watching the protagonist from the dark.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [warhoon_mobile_camp](warhoon_mobile_camp)
- [warhoon_city](warhoon_city)
- [subterranean_dungeon](subterranean_dungeon)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: warhoon_mobile_camp

[[SECTION markdown]]

# Warhoon Mobile Camp

**Role:** Secondary / Transit Setting

**Architecture or Geography:** A sprawling, mobile military encampment organized around a central column of warriors. Characterized by temporary structures and high-traffic transit paths for beasts of burden.

**Lighting and Atmosphere Cues:** Harsh, exposed lighting; dusty and chaotic atmosphere filled with the movement of large animals (thoats) and aggressive warrior movements.

**Scale Cues and Recurring Environmental Anchors:** Large scale; dominated by the presence of the Warhoon horde and massive thoat mounts.

**Descriptive Noun Phrases:** Mobile military encampment, warband camp, dusty transit paths, beast-taming grounds, ritualistic combat arena.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: warhoon_city

[[SECTION markdown]]

# Warhoon City

**Role:** Primary Setting (Destination)

**Architecture or Geography:** The permanent urban stronghold of the Warhoon horde; a site of concentrated power and ritualistic violence.

**Lighting and Atmosphere Cues:** Intense, martial atmosphere; high-tension social environment defined by sudden shifts in leadership and primal combat.

**Scale Cues and Recurring Environmental Anchors:** Large scale urban center; serves as the anchor for the horde's movement.

**Descriptive Noun Phrases:** Warhoon stronghold, tribal city, seat of the Jeddak, martial urban center.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: subterranean_dungeon

[[SECTION markdown]]

# Subterranean Dungeon

**Role:** Primary Setting (Psychological)

**Architecture or Geography:** A pitch-black, enclosed subterranean cell; cramped and claustrophobic.

**Lighting and Atmosphere Cues:** Absolute darkness; sensory deprivation; punctuated only by the occasional glow of eyes in the shadows. Oppressive, terrifying, and damp atmosphere.

**Scale Cues and Recurring Environmental Anchors:** Small scale/enclosed; defined by heavy chains, stone walls, and unseen crawling creatures.

**Descriptive Noun Phrases:** Pitch-black cell, subterranean prison, lightless dungeon, shadow-filled void, claustrophobic stone chamber.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
