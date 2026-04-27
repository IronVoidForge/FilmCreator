# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T07:12:13.743716+00:00
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
Project slug: wizard_of_oz

Chapter id: CH012

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

**Setting:** The rugged, untilled lands of the West, moving toward the Wicked Witch's castle.

**Characters:**
* **Dorothy & Toto:** Traveling toward the West; Dorothy discovers her green clothes have turned white.
* **The Scarecrow & Tin Woodman:** Act as protectors for the group during various attacks.
* **The Cowardly Lion:** Provides intimidation against the Witch's slaves but is eventually captured.
* **The Wicked Witch of the West:** A one-eyed, powerful antagonist who uses magic and minions to stop the travelers.
* **The Winged Monkeys:** Magical creatures summoned by the Golden Cap to capture the group.
* **The Winkies:** The Witch's yellow-clad slaves.

**Key Events:**
* **Departure from Emerald City:** The group heads West after receiving directions from the Guardian of the Gates.
* **The Witch's Failed Attacks:** The Witch sends a pack of wolves (defeated by the Tin Woodman), a flock of crows (defeated by the Scarecrow), and a swarm of black bees (neutralized by the Scarecrow using straw to protect Dorothy and the Lion) to destroy the travelers.
* **The Golden Cap:** In desperation, the Witch uses the last charge of the Golden Cap to summon the Winged Monkeys.
* **Capture of the Companions:** The Monkeys drop the Tin Woodman on sharp rocks, strip the Scarecrow of his straw, and bind the Lion to take him to the castle. They leave Dorothy unharmed due to the mark of the Good Witch on her forehead.
* **Imprisonment:** Dorothy is forced into domestic servitude in the Witch's kitchen, while the Lion is imprisoned in the courtyard and starved. Dorothy secretly feeds the Lion at night.
* **The Theft of the Silver Shoe:** The Witch uses invisible magic to trip Dorothy, allowing her to steal one of the Silver Shoes.
* **The Death of the Witch:** Enraged by the theft, Dorothy throws a bucket of water at the Witch. Because the Witch has a mortal vulnerability to water, she melts into a shapeless mass on the kitchen floor.
* **Resolution:** Dorothy retrieves her shoe and rushes to free the Lion and her other friends.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [western_rugged_lands](western_rugged_lands)
- [wicked_witch_castle_interior](wicked_witch_castle_interior)
- [wicked_witch_castle_courtyard](wicked_witch_castle_courtyard)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: western_rugged_lands

[[SECTION markdown]]

# Western Rugged Lands

**Role:** Primary transit setting.

**Architecture or Geography:** Untilled, rugged terrain of the West; vast, open landscapes characterized by harsh, uncultivated earth and wild vegetation.

**Lighting and Atmosphere Cues:** Harsh, direct sunlight; exposed and unforgiving atmosphere; sense of isolation and vulnerability to elements/predators.

**Scale Cues and Recurring Environmental Anchors:** Wide-angle vistas; expansive horizons; scattered natural obstacles (rocks, thickets) used for ambushes.

**Descriptive Noun Phrases:** Rugged western wasteland, untilled wilderness, sun-scorched plains, exposed terrain, vast desolate landscape.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: wicked_witch_castle_interior

[[SECTION markdown]]

# Wicked Witch Castle Interior

**Role:** Primary setting for climax and imprisonment.

**Architecture or Geography:** A dark, oppressive domestic space; includes a kitchen area with stone floors and utilitarian surfaces.

**Lighting and Atmosphere Cues:** Dim, shadowy lighting; heavy, claustrophobic atmosphere; sense of magical dread and servitude.

**Scale Cues and Recurring Environmental Anchors:** Enclosed rooms; heavy stone masonry; kitchen hearth/floors where the Witch melts.

**Descriptive Noun Phrases:** Oppressive castle interior, dim witch's kitchen, shadow-drenched stone halls, claustrophobic domestic space, magical stronghold.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: wicked_witch_castle_courtyard

[[SECTION markdown]]

# Wicked Witch Castle Courtyard

**Role:** Secondary setting for imprisonment.

**Architecture or Geography:** An outdoor enclosure within the castle walls; likely stone-paved or hard-packed earth.

**Lighting and Atmosphere Cues:** Stark, lonely lighting; atmosphere of neglect and starvation; high-walled confinement.

**Scale Cues and Recurring Environmental Anchors:** High perimeter walls; open but enclosed space; prison area for captured creatures.

**Descriptive Noun Phrases:** Enclosed castle courtyard, stone-walled prison yard, desolate courtyard, fortified enclosure.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
