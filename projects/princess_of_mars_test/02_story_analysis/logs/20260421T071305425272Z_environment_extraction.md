# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T07:13:05.425272+00:00
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

Chapter id: CH011

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
John Carter secures Dejah Thoris's safety by assigning Sola as her guardian and issuing a threat to the cruel Sarkoja. He moves Dejah Thoris and Sola into more luxurious, ancient quarters in a building featuring elaborate frescoes of a long-extinct, fair-skinned race. During their time in the new quarters, John Carter reveals his true origin—that he is from Earth—and explains how Martian technology allows them to observe other planets via advanced imaging. Dejah Thoris accepts his claim through "feminine logic," despite the impossibility of it. The chapter concludes with a messenger delivering a summons from Lorquas Ptomel, requiring John Carter to appear before the council.

**Characters:**
- **John Carter:** A man from Earth (Virginia) who is navigating his rising status among the Tharks and his growing feelings for Dejah Thoris.
- **Dejah Thoris:** A noblewoman of the red race; she is curious, intelligent, and shows a deep connection to her planet's history.
- **Sola:** An ally to John Carter who takes on the role of protector/attendant for Dejah Thoris.
- **Sarkoja:** A hostile figure who remains a threat despite John Carter's warnings.
- **Lorquas Ptomel:** The high-ranking leader of the community who summons John Carter.
- **Tars Tarkas:** A prominent Thark chieftain present during the council sessions.

**Settings:**
- **The New Quarters:** A pretentious, ancient building near the audience chamber, characterized by marble ceilings, gold chains, and magnificent frescoes depicting a lost, fair-haired civilization.
- **The Audience Chamber:** The location where Lorquas Ptomel and Tars Tarkas preside over the community.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [ancient_luxurious_quarters](ancient_luxurious_quarters)
- [audience_chamber](audience_chamber)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: ancient_luxurious_quarters

[[SECTION markdown]]

# Ancient Luxurious Quarters

**Role:** Primary / Residential

**Architecture & Geography:** An ancient, pretentious building featuring high marble ceilings and heavy gold chains used for structural or decorative elements. The walls are adorned with magnificent, elaborate frescoes depicting a long-extinct, fair-skinned, and fair-haired civilization.

**Lighting & Atmosphere:** Opulent, historical, and reverent; the atmosphere is thick with the weight of a lost era.

**Scale & Anchors:** Large-scale architectural features (marble ceilings); recurring visual anchor: detailed mythological frescoes.

**Prompt Phrases:** ancient marble halls, gold chain accents, elaborate prehistoric frescoes, fair-skinned civilization murals, opulent Martian ruins, high ceilinged chambers.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: audience_chamber

[[SECTION markdown]]

# Audience Chamber

**Role:** Secondary / Political

**Architecture & Geography:** A formal communal space designed for presiding over the community and council sessions.

**Lighting & Atmosphere:** Formal, authoritative, and high-stakes; a place of judgment and social hierarchy.

**Scale & Anchors:** Large assembly space; recurring visual anchor: seating or platforms for leaders like Lorquas Ptomel and Tars Tarkas.

**Prompt Phrases:** grand council chamber, Martian political hall, formal assembly space, authoritative architecture, high-status meeting room.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
