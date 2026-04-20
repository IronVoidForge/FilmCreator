# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T18:00:22.624549+00:00
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

After surviving a near-fatal sword thrust from Zad, John Carter is treated by his retinue of Martian women. He discovers that Dejah Thoris is in deep mourning, believing him to be dead. As the massive caravan moves silently across a moss-covered sea bottom toward a range of hills, Carter meets with Sola.

Sola shares the tragic and unconventional history of her parentage. She reveals that her mother, a sensitive Thark woman who felt alienated from her cruel society, fell in love with a warrior and raised Sola in secret within an ancient tower to protect her from the judgment of their people. The secrecy was shattered when Sarkoja discovered them; despite torture by Tal Hajus, Sola's mother remained silent to protect her daughter, eventually dying after successfully hiding Sola among a group of young Tharks. Sola concludes her story by revealing that her father—a man driven by a desire for vengeance against Tal Hajus—is none other than Tars Tarkas.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [arizona_quartz_vein_location](#arizona_quartz_vein_location) (Note: Placeholder for context, though chapter focuses on transit/hills)
- [moss_covered_sea_bottom](#moss_covered_sea_bottom)
- [ancient_tower_ruins](#ancient_tower_ruins)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: moss_covered_sea_bottom

[[SECTION markdown]]

# Moss Covered Sea Bottom

**Role:** Transit setting

**Geography:** A vast, undulating expanse of a dried Martian seabed, characterized by thick layers of organic growth.

**Lighting and Atmosphere:** Muted, diffused light filtering through a thin atmosphere; heavy, silent, and somber mood as the caravan moves across the floor.

**Scale and Anchors:** Massive scale; the horizon is dominated by distant ranges of hills; the slow, rhythmic movement of the large caravan provides a sense of scale against the vast seabed.

**Prompt Phrases:** moss-covered sea bed, ancient dried ocean floor, undulating organic textures, silent Martian wasteland, distant hill silhouettes.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: ancient_tower_ruins

[[SECTION markdown]]

# Ancient Tower Ruins

**Role:** Secondary (Flashback/Historical setting)

**Geography:** A secluded, ancient stone tower used for concealment; isolated from the main Thark settlements.

**Lighting and Atmosphere:** Secretive, dim, sheltered; a sense of isolation and protective enclosure amidst a harsh landscape.

**Scale and Anchors:** Vertical architecture; narrow interior spaces; a singular landmark of refuge within the Thark territory.

**Prompt Phrases:** ancient stone tower, secluded Martian ruins, hidden sanctuary, weathered masonry, isolated desert outpost.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
