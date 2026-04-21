# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T07:20:51.990663+00:00
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
Following a violent skirmish, John Carter recovers from a non-fatal wound inflicted by Zad. He is treated by his Martian retinue and reunites with Dejah Thoris and Sola. While Dejah Thoris mourns Carter (believing him dead), Carter observes her grief from a distance. That night, at the edge of a southern sea, Sola reveals her secret history to Carter. She recounts how her mother and a Thark warrior fell in love against tradition, leading to her mother's imprisonment and death under torture by Tal Hajus. Sola reveals that she was hidden among the community children to survive, and finally discloses the identity of her father: Tars Tarkas.

**Characters:**
- **John Carter:** Recovering from a chest wound; listener to Sola's confession.
- **Sola:** A green Martian woman who reveals her tragic lineage and her true parentage.
- **Dejah Thoris:** Mourning John Carter in silence.
- **Sola's Mother (deceased):** A Thark woman who died protecting the secret of her child and lover.
- **Sola's Father (Tars Tarkas):** Revealed to be the high-ranking green Martian warrior traveling with the caravan.
- **Sarkoja:** The antagonist from Sola's past who betrayed Sola's mother.
- **Tal Hajus:** The Thark chieftain responsible for the death of Sola's mother.

**Settings:**
- **The Ancient Sea Bottom:** A trackless, moss-covered expanse on Barsoom that leaves no tracks or dust.
- **The Caravan Camp:** A massive, colorful procession of two hundred and fifty chariots, warriors, and animals (thoats and zitidars) moving across the yellow landscape toward the southern hills.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [ancient_sea_bottom](ancient_sea_bottom)
- [caravan_camp_landscape](caravan_camp_landscape)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: ancient_sea_bottom

[[SECTION markdown]]

# Ancient Sea Bottom

**Role:** Primary / Secondary setting (Confessional site)

**Geography:** A trackless, vast expanse of a dried-up seabed. The surface is covered in a thick, resilient layer of moss that absorbs all impact.

**Lighting and Atmosphere:** Quiet, nocturnal atmosphere; the ground is soft and silent, leaving no footprints or dust clouds despite movement.

**Scale Cues:** An endless, featureless horizon that provides isolation for intimate dialogue.

**Prompt Phrases:** trackless mossy expanse, ancient dried seabed, footprint-less terrain, soft green moss carpet, vast Barsoomian basin.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: caravan_camp_landscape

[[SECTION markdown]]

# Caravan Camp Landscape

**Role:** Transit setting

**Geography:** A massive procession moving across a yellow, arid landscape toward distant southern hills.

**Lighting and Atmosphere:** Bright, harsh Martian daylight; dusty and expansive.

**Scale Cues:** Massive scale involving two hundred and fifty chariots, numerous warriors, and large beasts of burden (thoats and zitidars).

**Prompt Phrases:** vast yellow wasteland, moving chariot procession, Thark caravan, arid southern hills, massive desert transit, Martian animal herds.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
